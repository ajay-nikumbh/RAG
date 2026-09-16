"""
Real-document corpus downloader for the RAG course.

Why this exists
---------------
Synthetic documents teach you the happy path. Real documents teach you what actually
breaks: two-column reading order, 88 pages of repeated legal boilerplate, AcroForm
fields that carry no text layer, DOCX files with a table of contents, OCR that
misreads a character.

Every document below is fetched from a public, stable URL and cached on disk, so you
download once and re-run the notebooks offline forever after.

Usage
-----
    import sys; sys.path.append("../..")
    from utils.corpus import fetch, CORPUS, describe

    path = fetch("gdpr_pdf")        # downloads on first call, cached after
    describe()                      # print the full catalogue
"""

# `hashlib` gives us a checksum so we can detect a truncated or corrupted download.
import hashlib

# `Path` builds cross-platform filesystem paths.
from pathlib import Path

# `urlopen` / `Request` perform the HTTP download using only the standard library,
# so this module has zero required third-party dependencies.
from urllib.request import urlopen, Request

# `URLError` lets us catch network failures and report them helpfully.
from urllib.error import URLError


# ----------------------------------------------------------------------------
# Where downloads are cached
# ----------------------------------------------------------------------------

# This file lives in <project>/utils/, so the project root is one level up.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# All real documents land here. It is git-ignored: the corpus is reproducible,
# so there is no reason to commit ~4 MB of PDFs to the repository.
CACHE_DIR = PROJECT_ROOT / "assets" / "real_corpus"


# ----------------------------------------------------------------------------
# The catalogue
# ----------------------------------------------------------------------------
# Each entry records WHY the document is here - the specific property it demonstrates.
# That "teaches" field is the reason a given file was chosen over any other.

CORPUS = {
    # ---------------- PDFs: born-digital ----------------
    "rag_paper": {
        "url": "https://arxiv.org/pdf/2005.11401",
        "filename": "rag_paper_lewis_2020.pdf",
        "kind": "pdf",
        "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
        "source": "arXiv 2005.11401 (Lewis et al., 2020)",
        "licence": "arXiv non-exclusive licence",
        "teaches": "SINGLE-column academic layout with inline equations and figures. "
                   "Used as the control case that shows a naive column-splitter "
                   "produces garbage on a document that has no columns. Also the "
                   "paper that named RAG.",
    },
    "bert_paper": {
        "url": "https://arxiv.org/pdf/1810.04805",
        "filename": "bert_devlin_2019.pdf",
        "kind": "pdf",
        "title": "BERT: Pre-training of Deep Bidirectional Transformers",
        "source": "arXiv 1810.04805 (Devlin et al., 2019)",
        "licence": "arXiv non-exclusive licence",
        "teaches": "A genuine TWO-column layout: default block extraction interleaves "
                   "the columns and breaks sentences mid-flow. The real reading-order "
                   "problem, reproducible on a real paper.",
    },
    "irs_w4": {
        "url": "https://www.irs.gov/pub/irs-pdf/fw4.pdf",
        "filename": "irs_form_w4.pdf",
        "kind": "pdf",
        "title": "IRS Form W-4, Employee's Withholding Certificate",
        "source": "irs.gov",
        "licence": "US Government work, public domain",
        "teaches": "A real government AcroForm: form fields, checkboxes and tables "
                   "that plain text extraction flattens or loses entirely.",
    },
    "gdpr_pdf": {
        "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679",
        "filename": "gdpr_regulation_2016_679.pdf",
        "kind": "pdf",
        "title": "Regulation (EU) 2016/679 (GDPR)",
        "source": "EUR-Lex, CELEX 32016R0679",
        "licence": "© European Union, reuse permitted (Decision 2011/833/EU)",
        "teaches": "88 pages of real legal text: genuine repeated headers on 88/88 "
                   "pages, Article N(n)(a) citations that over-cleaning destroys, "
                   "and numbered lists that fool a naive frequency filter.",
    },

    # ---------------- HTML ----------------
    "gdpr_html": {
        "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679",
        "filename": "gdpr_regulation_2016_679.html",
        "kind": "html",
        "title": "Regulation (EU) 2016/679 (GDPR) - HTML edition",
        "source": "EUR-Lex, CELEX 32016R0679",
        "licence": "© European Union, reuse permitted (Decision 2011/833/EU)",
        "teaches": "The same document as gdpr_pdf but in HTML - a direct, "
                   "controlled comparison of what each format preserves.",
    },

    # ---------------- DOCX ----------------
    "demo_docx": {
        "url": "https://calibre-ebook.com/downloads/demos/demo.docx",
        "filename": "calibre_demo.docx",
        "kind": "docx",
        "title": "Calibre DOCX feature demonstration",
        "source": "calibre-ebook.com",
        "licence": "GPL-3.0 (calibre project demo asset)",
        "teaches": "Real Heading 1/Heading 2 hierarchy, 5 real tables, a table of "
                   "contents, footnotes and list paragraphs.",
    },

    # ---------------- Scanned / OCR ----------------
    "ocr_phototest": {
        "url": "https://raw.githubusercontent.com/tesseract-ocr/test/main/testing/phototest.tif",
        "filename": "ocr_phototest.tif",
        "kind": "image",
        "title": "Tesseract phototest image",
        "source": "github.com/tesseract-ocr/test",
        "licence": "Apache-2.0",
        "teaches": "Clean scan baseline - high OCR confidence to compare against.",
    },
    "ocr_eurotext": {
        "url": "https://raw.githubusercontent.com/tesseract-ocr/test/main/testing/eurotext.tif",
        "filename": "ocr_eurotext.tif",
        "kind": "image",
        "title": "Tesseract eurotext multilingual image",
        "source": "github.com/tesseract-ocr/test",
        "licence": "Apache-2.0",
        "teaches": "Accented multilingual text - where OCR confidence drops and "
                   "Unicode normalization starts to matter.",
    },

    # ---------------- CSV ----------------
    "titanic_csv": {
        "url": "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
        "filename": "titanic.csv",
        "kind": "csv",
        "title": "Titanic passenger dataset",
        "source": "github.com/datasciencedojo/datasets",
        "licence": "Public dataset",
        "teaches": "891 real rows with genuine missing values - row serialization "
                   "and the 'what is one retrievable unit?' question.",
    },
}


# ----------------------------------------------------------------------------
# Downloading
# ----------------------------------------------------------------------------

def fetch(key: str, force: bool = False, quiet: bool = False) -> Path:
    """
    Download a corpus document (if not already cached) and return its local path.

    Parameters
    ----------
    key   : a key from CORPUS, e.g. "gdpr_pdf".
    force : re-download even if a cached copy exists.
    quiet : suppress progress messages.

    Returns
    -------
    Path to the cached file.
    """
    # Fail early with a helpful message if the key is not in the catalogue.
    if key not in CORPUS:
        available = ", ".join(sorted(CORPUS))
        raise KeyError(f"Unknown corpus key {key!r}. Available: {available}")

    # Look up the catalogue entry.
    entry = CORPUS[key]

    # Make sure the cache directory exists before we try to write into it.
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    # The full local path this document will be cached at.
    destination = CACHE_DIR / entry["filename"]

    # If we already have it and are not forcing a refresh, return immediately.
    if destination.exists() and not force:
        if not quiet:
            size_kb = destination.stat().st_size / 1024
            print(f"  cached  {entry['filename']}  ({size_kb:.0f} KB)")
        return destination

    # Announce the download so a slow network does not look like a hang.
    if not quiet:
        print(f"  fetching {entry['filename']} from {entry['source']} ...")

    # Some servers reject requests without a User-Agent header.
    request = Request(entry["url"], headers={"User-Agent": "rag-course/1.0"})

    try:
        # Open the URL and read the whole body.
        with urlopen(request, timeout=60) as response:
            payload = response.read()

    # Convert any network failure into a clear, actionable error.
    except (URLError, OSError) as error:
        raise RuntimeError(
            f"Could not download {key!r} from {entry['url']}\n"
            f"  reason: {error}\n"
            f"  If you are offline, skip this cell - later cells guard on file existence."
        ) from error

    # Refuse to cache a suspiciously small response, which usually means we got an
    # error page rather than the document.
    if len(payload) < 1024:
        raise RuntimeError(
            f"Download for {key!r} was only {len(payload)} bytes - "
            f"the server probably returned an error page rather than the document."
        )

    # Write the bytes to the cache.
    destination.write_bytes(payload)

    # Report success with the size, so you can sanity-check it looks right.
    if not quiet:
        size_kb = len(payload) / 1024
        print(f"  saved   {entry['filename']}  ({size_kb:.0f} KB)")

    # Hand back the local path.
    return destination


def fetch_many(keys, quiet: bool = False) -> dict:
    """
    Download several corpus documents at once and return {key: Path}.

    Failures are collected rather than raised, so one unreachable host does not
    stop the rest of a notebook from running.
    """
    # Collect the successfully fetched paths here.
    results = {}

    # Try each requested key in turn.
    for key in keys:
        try:
            results[key] = fetch(key, quiet=quiet)

        # Report the failure but keep going with the remaining documents.
        except (RuntimeError, KeyError) as error:
            if not quiet:
                print(f"  SKIP {key}: {error}")

    # Return whatever we managed to get.
    return results


def checksum(path: Path) -> str:
    """
    Return the SHA-256 of a file, so you can verify a download is intact.

    Used in the notebooks to show that content hashing (Module 2h) works on real
    files, not just on toy strings.
    """
    # Build a hash object we will feed the file into.
    digest = hashlib.sha256()

    # Read in 64 KB blocks so a large PDF never has to sit in memory all at once.
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)

    # Return the hexadecimal digest.
    return digest.hexdigest()


def describe(kind: str = None) -> None:
    """
    Print the corpus catalogue, optionally filtered to one kind ("pdf", "html", ...).

    Read the "teaches" line for each entry - it explains why that specific document
    was chosen over any other.
    """
    # Header for the listing.
    print(f"Real document corpus  ({CACHE_DIR})\n")

    # Walk the catalogue in a stable, alphabetical order.
    for key, entry in sorted(CORPUS.items()):

        # Skip entries that do not match the requested filter.
        if kind and entry["kind"] != kind:
            continue

        # Show whether this document is already cached locally.
        cached = (CACHE_DIR / entry["filename"]).exists()
        marker = "[cached]" if cached else "[  -   ]"

        # Print the entry.
        print(f"{marker} {key}")
        print(f"          {entry['title']}")
        print(f"          source:  {entry['source']}")
        print(f"          licence: {entry['licence']}")
        print(f"          teaches: {entry['teaches']}")
        print()
