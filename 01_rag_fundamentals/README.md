# Chapter 1 — RAG Fundamentals

> **Notebook:** [`01_rag_fundamentals.ipynb`](01_rag_fundamentals.ipynb)
> **Prerequisites:** None. This is the starting point.
> **Next:** [Chapter 2 — Documents, Data Sources & Ingestion](../02_documents_data_sources_ingestion/)

---

## 60-second summary

RAG = **Retrieval-Augmented Generation**. Instead of asking an LLM to answer from memory
alone, you first *retrieve* relevant external documents and paste them into the prompt as
context.

The value is a separation of concerns: **reasoning stays in the model's weights, knowledge
moves to an external store you can update, inspect, cite and permission-control.**

---

## What the notebook covers

| § | Topic |
|---|-------|
| 1 | What exactly is RAG — architecture and naming |
| 2 | Why we need it — the frozen-knowledge problem |
| 3 | Parametric vs non-parametric knowledge |
| 4 | The exam analogy — and why retrieval quality caps everything |
| 5 | The two pipelines (offline indexing + online query) |
| 6 | The mathematics of retrieval — cosine similarity, Top-K, the probabilistic view |
| 7 | **Build it:** naive RAG from scratch, 10 steps, no frameworks |
| 8 | The hallucination problem — and why RAG doesn't eliminate it |
| 9 | RAG vs fine-tuning vs long-context LLMs |
| 10 | Failure modes and the debugging ladder |
| 11 | Interview traps & model answers |
| 12 | Summary, key equations, exercises |

---

## Key takeaways

1. **RAG = retrieve external knowledge and provide it to an LLM during generation.**
2. LLM weights hold **parametric knowledge**; the external store is **non-parametric knowledge**.
3. RAG normally **does not modify LLM weights** — documents go into the *prompt*.
4. The basic pipeline: `Documents → Chunk → Embed → Index`, then `Query → Retrieve → Context → LLM → Answer`.
5. RAG is valuable for **private, fresh, domain-specific and large-scale** knowledge.
6. RAG **does not eliminate hallucination**.
7. RAG **does not require a vector database** — BM25, SQL, graphs and APIs all work.
8. Always separate failures into **retrieval failure vs generation failure**.

---

## Key equations

| Formula | Meaning |
|---|---|
| $E(x) \rightarrow \mathbb{R}^d$ | Embedding function: text → vector |
| $\cos(q, d) = \dfrac{q \cdot d}{\lVert q \rVert \lVert d \rVert}$ | Cosine similarity |
| $D_K = \text{TopK}_{d_i}\,\text{sim}(E(Q), E(d_i))$ | Top-K retrieval |
| $P(Y \mid Q, D_K)$ | Generation *with* RAG (vs $P(Y \mid Q)$ without) |
| $P(y\mid x) = \sum_z P(z\mid x) P(y \mid x, z)$ | The two uncertainties: *did I retrieve right?* × *did I generate right?* |

---

## The one diagram to memorize

```
             KNOWLEDGE PIPELINE

Documents → Parse → Chunk → Embed → Index → Vector / Search Database


               QUERY PIPELINE

User Query → Query Understanding → Retrieval → Relevant Evidence
          → Context Construction → LLM → Grounded Answer
```

And every RAG bug divides into:

```
        RAG QUALITY
             │
      ┌──────┴──────┐
  Retrieval     Generation
   Quality       Quality
```

---

## Interview traps

| ❌ Wrong | ✅ Right |
|---|---|
| "RAG removes hallucination." | It *reduces* it by grounding generation in evidence. |
| "RAG requires a vector database." | BM25, SQL, Elasticsearch, graphs, APIs all work. |
| "RAG trains the LLM on documents." | It does not modify weights. Context is forgotten after the request. |
| "Highest cosine similarity = correct answer." | Similarity ≠ answerability. This is why reranking exists. |
| "Large context windows make RAG obsolete." | Complementary, not competing. |
| "If retrieval is correct, the answer is correct." | Generation can still fail. |
| "Fine-tuning replaces RAG." | Different problems; they combine well. |

---

## Running it

Requires `numpy`, `matplotlib`, `scikit-learn` (for the PCA visualizations), plus
`openai` + Azure/OpenAI credentials in `.env` for the live sections.
The notebook **degrades gracefully** — without credentials, the maths and
cosine-similarity sections still run; only the API-dependent cells (including all
visualizations, since they plot real embeddings) are skipped.

```bash
pip install -r ../requirements.txt
jupyter lab 01_rag_fundamentals.ipynb
```

### Visualizations

The notebook plots real embedding vectors at five points, so "1536-dimensional vector"
stops being an abstraction:

1. A single embedding as a bar chart + full-vector heatmap strip
2. All four document embeddings side by side (heatmap) + projected to 2D via PCA
3. The query projected into that same PCA space, with a line to its nearest document
4. Similarity scores as a sorted, colour-graded bar chart
5. The Top-K cutoff — which documents reach the LLM and which are silently dropped

---

## Exercises in the notebook

1. Remove the "if the answer cannot be determined" escape hatch and watch the model invent a policy
2. Add unrelated documents and find the `k` at which retrieval breaks
3. Reproduce the chunking failure that loses a condition clause
4. Test similarity ≠ answerability on your own chunk pairs
5. Implement Euclidean distance and compare rankings with cosine
