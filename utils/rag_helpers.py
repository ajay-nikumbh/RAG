"""
Shared helpers used across all RAG course notebooks.

Why this file exists
--------------------
Every notebook needs the same three boring things:
  1. Load API credentials from .env
  2. Turn text into embeddings
  3. Ask an LLM a question

Rather than copy-pasting that setup into 55 notebooks, we write it once here.
The *teaching* code (cosine similarity, chunking, retrieval, ...) always stays
inside the notebooks so you can see it. Only the plumbing lives here.

Supports both Azure OpenAI (default) and plain OpenAI. Azure differs from
OpenAI in three ways this module handles for you:
  - auth is api_key + endpoint + api_version, not just api_key
  - you call a DEPLOYMENT name, not a model name (e.g. "my-gpt4o" rather
    than "gpt-4o-mini" - you chose that deployment name in Azure yourself)
  - the SDK class is `AzureOpenAI` instead of `OpenAI`

Usage inside a notebook
-----------------------
    import sys
    sys.path.append("..")            # so Python can find the utils/ folder
    from utils.rag_helpers import embed_texts, chat
"""

# `os` lets us read environment variables (where credentials live).
import os

# `Path` gives us a clean way to build file paths that work on Mac/Linux/Windows.
from pathlib import Path

# `List` is only used for type hints, which make function signatures readable.
from typing import List, Optional


# ----------------------------------------------------------------------------
# 1. Environment setup
# ----------------------------------------------------------------------------

def load_env() -> bool:
    """
    Load variables from the project's .env file into the environment.

    Returns True if usable credentials are now available for the configured
    provider, False otherwise. We return a bool instead of raising, so a
    notebook can degrade gracefully when no key is configured.
    """
    # Import here rather than at module top so that a missing python-dotenv
    # install produces a clear message at call time instead of on import.
    from dotenv import load_dotenv

    # This file lives in <project>/utils/, so the project root is one level up.
    project_root = Path(__file__).resolve().parent.parent

    # Read <project>/.env and copy its key=value pairs into os.environ.
    load_dotenv(project_root / ".env")

    # Which provider are we configured for. Default to Azure.
    provider = os.getenv("LLM_PROVIDER", "azure").lower()

    if provider == "azure":
        # Azure needs all three of these to make a single API call.
        key = os.getenv("AZURE_OPENAI_API_KEY", "")
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
        return (
            bool(key) and not key.startswith("your-azure-key")
            and bool(endpoint) and "your-resource-name" not in endpoint
        )

    # Plain OpenAI just needs the one key.
    key = os.getenv("OPENAI_API_KEY", "")
    return bool(key) and not key.startswith("sk-your-key")


def get_provider() -> str:
    """Return the configured provider: "azure" or "openai"."""
    # Read after load_env() has had a chance to populate os.environ.
    return os.getenv("LLM_PROVIDER", "azure").lower()


def get_client():
    """
    Build and return an authenticated client for the configured provider.

    Raises a friendly RuntimeError if credentials are missing, because a raw
    SDK auth error is confusing the first time you hit it.
    """
    # Make sure .env has been read before we look for credentials.
    if not load_env():
        provider = get_provider()
        if provider == "azure":
            raise RuntimeError(
                "Azure OpenAI credentials not found.\n"
                "Fix: copy .env.example to .env and fill in AZURE_OPENAI_API_KEY, "
                "AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_VERSION."
            )
        raise RuntimeError(
            "No OPENAI_API_KEY found.\n"
            "Fix: copy .env.example to .env and paste your key into it."
        )

    # Import lazily so notebooks that never call an API don't need the package.
    from openai import AzureOpenAI, OpenAI

    if get_provider() == "azure":
        # AzureOpenAI needs the endpoint and api_version in addition to the key.
        return AzureOpenAI(
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"),
        )

    # Plain OpenAI reads OPENAI_API_KEY from the environment automatically.
    return OpenAI()


# Read the deployment/model names once, with sensible defaults if .env doesn't set them.
load_env()

if get_provider() == "azure":
    # On Azure these are DEPLOYMENT names you chose in Azure OpenAI Studio,
    # not the underlying model names.
    EMBEDDING_MODEL = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small")
    CHAT_MODEL = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT", "gpt-4o-mini")
else:
    EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
    CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")


# ----------------------------------------------------------------------------
# 2. Embeddings
# ----------------------------------------------------------------------------

def embed_texts(texts: List[str], model: Optional[str] = None):
    """
    Convert a list of strings into a list of embedding vectors.

    Parameters
    ----------
    texts : the strings to embed. Passing many at once is much cheaper and
            faster than one call per string (this is "batching").
    model : override the embedding model/deployment; defaults to .env value.

    Returns
    -------
    A numpy array of shape (len(texts), embedding_dimension).
    """
    # numpy is imported here so this module stays importable without it.
    import numpy as np

    # Fall back to the project-wide default model when none is given.
    # On Azure this is a DEPLOYMENT name, not a raw model name.
    model = model or EMBEDDING_MODEL

    # Get an authenticated client (raises a clear error if credentials are missing).
    client = get_client()

    # One API call embeds the whole batch of texts.
    response = client.embeddings.create(model=model, input=texts)

    # The API returns objects; pull the raw float list out of each one.
    vectors = [item.embedding for item in response.data]

    # float32 halves memory versus float64 and is plenty precise for similarity.
    return np.array(vectors, dtype="float32")


def embed_text(text: str, model: Optional[str] = None):
    """
    Convenience wrapper: embed a single string and return a 1-D vector.

    Internally it just calls embed_texts with a one-item list and unwraps it.
    """
    # Wrap the single string in a list, then take row 0 of the result.
    return embed_texts([text], model=model)[0]


# ----------------------------------------------------------------------------
# 3. LLM generation
# ----------------------------------------------------------------------------

def chat(
    prompt: str,
    system: str = "You are a helpful assistant.",
    model: Optional[str] = None,
    temperature: float = 0.0,
) -> str:
    """
    Send one prompt to the chat model and return the text reply.

    Parameters
    ----------
    prompt      : the user message (in RAG, this is context + question).
    system      : the system message, used to set behaviour and grounding rules.
    model       : override the chat model/deployment; defaults to .env value.
    temperature : 0.0 makes output nearly deterministic, which is what you want
                  for RAG — we are extracting facts, not writing poetry.
    """
    # Fall back to the project-wide default model when none is given.
    # On Azure this is a DEPLOYMENT name, not a raw model name.
    model = model or CHAT_MODEL

    # Get an authenticated client.
    client = get_client()

    # Send the two-message conversation to the model.
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    )

    # Pull the assistant's text out of the first (and only) choice.
    return response.choices[0].message.content


# ----------------------------------------------------------------------------
# 4. Token counting (used from Chapter 4 onward, handy everywhere)
# ----------------------------------------------------------------------------

def count_tokens(text: str, model: Optional[str] = None) -> int:
    """
    Count how many tokens a piece of text costs for a given model.

    Tokens — not characters or words — are what you pay for and what fills the
    context window, so this is the unit that actually matters in RAG budgeting.

    Note: tiktoken looks up encodings by MODEL name, not Azure deployment name.
    If your deployment name doesn't match a known model name (e.g. a custom
    deployment alias), pass the underlying model name explicitly via `model`.
    """
    # tiktoken is OpenAI's tokenizer library.
    import tiktoken

    # Fall back to the project-wide default model when none is given.
    model = model or CHAT_MODEL

    try:
        # Ask tiktoken which encoding this specific model uses.
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Deployment alias not recognized, or a newer model tiktoken doesn't
        # know yet - o200k_base is the encoding modern GPT-4o-class models use.
        encoding = tiktoken.get_encoding("o200k_base")

    # Encoding turns text into a list of token IDs; its length is the token count.
    return len(encoding.encode(text))
