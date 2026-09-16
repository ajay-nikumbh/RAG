# Chapter 1 — RAG Fundamentals

- **Notebook:** [`01. Rag fundamentals.ipynb`](01.%20Rag%20fundamentals.ipynb)
- **Prerequisites:** None. This is the starting point.
- **Next:** [Chapter 2 — Documents, Data Sources & Ingestion](../02.%20Documents%20data%20sources%20ingestion/)

## 60-second summary

RAG = **Retrieval-Augmented Generation**. Instead of asking an LLM to answer from memory
alone, you first *retrieve* relevant external documents and paste them into the prompt as
context.

The value is a separation of concerns: **reasoning stays in the model's weights, knowledge
moves to an external store you can update, inspect, cite and permission-control.**

## What the notebook covers

| Section | Topic | Why it matters | What you build |
|---|---|---|---|
| 1 | What exactly is RAG — architecture and naming | The name "Retrieval-Augmented Generation" describes the exact three-step mechanism, not marketing | Nothing yet — vocabulary first |
| 2 | Why we need it — the frozen-knowledge problem | Explains *why* RAG exists at all, not just what it does | A concrete example of an LLM confidently answering from stale knowledge |
| 3 | Parametric vs non-parametric knowledge | The distinction interviewers use to test whether you actually understand RAG or just used a framework | Vocabulary |
| 4 | The exam analogy — why retrieval quality caps everything | The single mental model that explains almost every RAG bug you'll ever debug | Intuition |
| 5 | The two pipelines (offline indexing, online query) | Confusing these two is the most common RAG system-design mistake | Mental model |
| 6 | The mathematics of retrieval | Cosine similarity, Top-K, and the probabilistic view of why RAG has two independent failure points | Cosine similarity, implemented by hand |
| 7 | Build it: naive RAG from scratch | Seeing the whole pipeline in about 10 small functions removes the "magic" from every framework built on top of it | A complete, working RAG system with real embeddings, real retrieval, real generation |
| 8 | The hallucination problem | The interview trap: RAG reduces hallucination, it never eliminates it | A live demo of similarity not equalling answerability |
| 9 | RAG vs fine-tuning vs long-context LLMs | The most frequently asked GenAI interview question, answered with a decision rule instead of a vague comparison | Decision framework |
| 10 | Failure modes and the debugging ladder | The exact order to check things when a RAG answer is wrong | A live demo of the retrieval bottleneck at k=1 |
| 11 | Interview traps and model answers | Seven specific wrong statements people make, and the correct version of each | Interview prep |
| 12 | Summary, key equations, exercises | Consolidation before moving to Chapter 2 | Review |

## Key takeaways

1. RAG means retrieving external knowledge and providing it to an LLM during generation.
2. LLM weights hold parametric knowledge; the external store is non-parametric knowledge.
3. RAG normally does not modify LLM weights — documents go into the prompt.
4. The basic pipeline: `Documents → Chunk → Embed → Index`, then `Query → Retrieve → Context → LLM → Answer`.
5. RAG is valuable for private, fresh, domain-specific and large-scale knowledge.
6. RAG does not eliminate hallucination.
7. RAG does not require a vector database — BM25, SQL, graphs and APIs all work.
8. Always separate failures into retrieval failure vs generation failure.

## Key equations

| Formula | Meaning | Where it shows up in the notebook |
|---|---|---|
| $E(x) \rightarrow \mathbb{R}^d$ | Embedding function: text → fixed-length vector | Section 6, Section 7 step 2 |
| $\cos(q, d) = \dfrac{q \cdot d}{\lVert q \rVert \lVert d \rVert}$ | Cosine similarity between query and document | Section 6, implemented by hand in Section 7 step 4 |
| $D_K = \text{TopK}_{d_i}\,\text{sim}(E(Q), E(d_i))$ | Top-K retrieval: keep the K best-scoring documents | Section 7 step 6, Section 10 (the retrieval bottleneck) |
| $P(Y \mid Q, D_K)$ vs $P(Y \mid Q)$ | Generation with RAG vs plain generation | Section 6.4, Section 9 |
| $P(y\mid x) = \sum_z P(z\mid x) P(y \mid x, z)$ | The two independent uncertainties in every RAG answer: did I retrieve right, and did I generate right | Section 6.5, the debugging ladder in Section 10 |

## Interview traps

| Wrong statement | Why it's wrong | Correct version |
|---|---|---|
| "RAG removes hallucination." | Confuses reducing a failure mode with eliminating it | RAG reduces hallucination by grounding generation in evidence — it does not eliminate it |
| "RAG requires a vector database." | Vector search is one retrieval implementation, not the definition of RAG | BM25, SQL, Elasticsearch, graph databases, and plain APIs all work as the retrieval half of RAG |
| "RAG trains the LLM on documents." | Confuses fine-tuning with in-context retrieval | RAG does not modify weights. Retrieved context is forgotten the moment the request ends |
| "Highest cosine similarity = correct answer." | Similarity measures topical closeness, not whether the passage contains the answer | Similarity does not equal answerability — this is the entire justification for reranking |
| "Large context windows make RAG obsolete." | Confuses "can fit more text" with "retrieval becomes unnecessary" | Long context and RAG are complementary — long context still needs something to decide what to put in it |
| "If retrieval is correct, the answer is correct." | Ignores that generation is a second, independent failure point | Generation can still misread, ignore, or contradict correctly retrieved context |
| "Fine-tuning replaces RAG." | Treats two different tools as substitutes | They solve different problems (behavior vs knowledge) and combine well in production |

## Running it

Requires `numpy`, `matplotlib`, `scikit-learn` (for the PCA visualizations), plus
`openai` and Azure/OpenAI credentials in `.env` for the live sections. The notebook
degrades gracefully — without credentials, the maths and cosine-similarity sections
still run; only the API-dependent cells (including all visualizations, since they plot
real embeddings) are skipped.

```bash
pip install -r ../requirements.txt
jupyter lab "01. Rag fundamentals.ipynb"
```

### Visualizations

The notebook plots real embedding vectors at five points, so "1536-dimensional vector"
stops being an abstraction.

1. Single embedding as a bar chart plus full-vector heatmap strip — an embedding is
   just floats, nothing more mysterious than that.
2. All four document embeddings side by side (heatmap) plus projected to 2D via PCA —
   documents with related meaning end up geometrically close, without ever being told
   they're related.
3. The query projected into that same PCA space, with a line to its nearest document —
   retrieval is, visually, nothing but "find the nearest point."
4. Similarity scores as a sorted, colour-graded bar chart — the margin between scores,
   which matters once you're choosing a Top-K cutoff.
5. The Top-K cutoff — which documents reach the LLM and which are silently dropped, the
   exact moment information either survives into the prompt or disappears forever.

## Exercises in the notebook

1. Remove the "if the answer cannot be determined" escape hatch and ask about a policy
   that doesn't exist. Watch the model invent a confident, wrong answer the moment
   grounding is removed.
2. Add unrelated documents and find the `k` at which retrieval breaks. Builds intuition
   for how Top-K interacts with corpus size.
3. Reproduce the chunking failure that loses a condition clause. Shows why chunk
   boundaries can silently delete meaning.
4. Test similarity not equalling answerability on your own chunk pairs. Reinforces
   Section 8 with a self-authored example instead of the notebook's.
5. Implement Euclidean distance and compare rankings with cosine. Makes the "why
   cosine, not Euclidean" argument concrete rather than assumed.
