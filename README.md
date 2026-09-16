# RAG — Theory + Practice

A hands-on course on **Retrieval-Augmented Generation**, built from a FAANG-interview-oriented
syllabus. Every chapter is one self-contained Jupyter notebook that pairs the theory
(as markdown) with clean, heavily-commented Python you can run and modify.

**Format of every notebook** — intuition → theory → maths → ASCII diagrams → each technique
implemented *separately* in Python (comment above every meaningful line) → trade-offs →
production considerations → interview questions.

---

## Repository layout

```
RAG/
├── README.md                          ← you are here (roadmap + setup)
├── requirements.txt                   ← all Python dependencies
├── .env.example                       ← copy to .env, add your OpenAI key
├── .gitignore
│
├── 00_course_material/                ← the source PDFs this course is built from
│
├── 01_rag_fundamentals/
│   ├── README.md                      ← chapter summary + key takeaways
│   └── 01_rag_fundamentals.ipynb
│
├── 02_documents_data_sources_ingestion/
│   ├── README.md
│   └── 02_documents_data_sources_ingestion.ipynb
│
├── assets/
│   └── sample_data/                   ← toy documents used by the notebooks
│
└── utils/
    └── rag_helpers.py                 ← shared plumbing (API key, embeddings, chat)
```

**Naming convention:** folder and notebook share the same `NN_snake_case_name`. The
two-digit prefix keeps chapters in order in both the file browser and on GitHub.

---

## Setup (one time)

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
cp .env.example .env
# then open .env and paste your OpenAI key

# 4. Launch Jupyter
jupyter lab                        # or: jupyter notebook
```

Models used throughout (configurable in `.env`):
- **Embeddings:** `text-embedding-3-small` — 1536 dimensions, very cheap
- **Generation:** `gpt-4o-mini` — cheap and fast, fine for learning RAG

> Cost note: the whole course costs well under a dollar in API calls. Embedding a few
> dozen toy sentences is fractions of a cent.

---

## Course roadmap

### Part I — Foundations
| # | Chapter | Status |
|---|---------|--------|
| 01 | [RAG Fundamentals](01_rag_fundamentals/) | ✅ Done |
| 02 | [Documents, Data Sources & Ingestion](02_documents_data_sources_ingestion/) | ✅ Done |
| 03 | Document Chunking | ⬜ Planned |
| 04 | Tokens & Tokenization | ⬜ Planned |
| 05 | Embeddings Fundamentals | ⬜ Planned |
| 06 | Embedding Mathematics | ⬜ Planned |

### Part II — Storage & Search
| # | Chapter | Status |
|---|---------|--------|
| 07 | Vector Databases | ⬜ Planned |
| 08 | Approximate Nearest Neighbor Search | ⬜ Planned |
| 09 | Sparse Retrieval / Keyword Search | ⬜ Planned |
| 10 | Dense Retrieval | ⬜ Planned |
| 11 | Hybrid Search | ⬜ Planned |
| 12 | Metadata & Filtered Retrieval | ⬜ Planned |

### Part III — Query & Retrieval Quality
| # | Chapter | Status |
|---|---------|--------|
| 13 | Query Processing | ⬜ Planned |
| 14 | Query Transformation | ⬜ Planned |
| 15 | Retrieval Strategies | ⬜ Planned |
| 16 | Reranking | ⬜ Planned |
| 17 | Context Construction | ⬜ Planned |
| 18 | Contextual Compression | ⬜ Planned |

### Part IV — Generation
| # | Chapter | Status |
|---|---------|--------|
| 19 | Prompt Engineering for RAG | ⬜ Planned |
| 20 | Generation Layer | ⬜ Planned |
| 21 | Conversational RAG | ⬜ Planned |

### Part V — Advanced Architectures
| # | Chapter | Status |
|---|---------|--------|
| 22 | Advanced RAG Architectures | ⬜ Planned |
| 23 | Corrective RAG (CRAG) | ⬜ Planned |
| 24 | Self-RAG | ⬜ Planned |
| 25 | Adaptive RAG | ⬜ Planned |
| 26 | Agentic RAG | ⬜ Planned |
| 27 | Graph RAG | ⬜ Planned |
| 28 | Multi-Hop RAG | ⬜ Planned |
| 29 | RAPTOR | ⬜ Planned |
| 30 | Multimodal RAG | ⬜ Planned |
| 31 | Table RAG | ⬜ Planned |
| 32 | Text-to-SQL + RAG | ⬜ Planned |
| 33 | Knowledge Graph + RAG | ⬜ Planned |

### Part VI — Evaluation
| # | Chapter | Status |
|---|---------|--------|
| 34 | RAG Evaluation Fundamentals | ⬜ Planned |
| 35 | Retrieval Metrics | ⬜ Planned |
| 36 | Generation Metrics | ⬜ Planned |
| 37 | RAG Evaluation Frameworks | ⬜ Planned |
| 38 | Synthetic Evaluation Datasets | ⬜ Planned |
| 39 | Failure Analysis | ⬜ Planned |

### Part VII — Production
| # | Chapter | Status |
|---|---------|--------|
| 40 | RAG Optimization | ⬜ Planned |
| 41 | RAG Latency & Performance | ⬜ Planned |
| 42 | Caching in RAG | ⬜ Planned |
| 43 | Production RAG Architecture | ⬜ Planned |
| 44 | Incremental Indexing | ⬜ Planned |
| 45 | Security & Access-Control RAG | ⬜ Planned |
| 46 | Multi-Tenant RAG | ⬜ Planned |
| 47 | RAG Guardrails | ⬜ Planned |
| 48 | Observability & Monitoring | ⬜ Planned |
| 49 | Feedback Loops | ⬜ Planned |
| 50 | RAG Cost Optimization | ⬜ Planned |

### Part VIII — Frameworks & Interviews
| # | Chapter | Status |
|---|---------|--------|
| 51 | RAG Frameworks | ⬜ Planned |
| 52 | Building RAG From Scratch in Python | ⬜ Planned |
| 53 | Production RAG System Design | ⬜ Planned |
| 54 | RAG Interview Case Studies | ⬜ Planned |
| 55 | FAANG RAG Interview Questions & System Design | ⬜ Planned |

---

## The whole curriculum in one diagram

```
                         RAG
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
    INGESTION         RETRIEVAL         GENERATION
        │                 │                 │
    Parsing           Embeddings         Prompt
    Cleaning          Vector DB          Context
    Chunking          BM25               LLM
    Metadata          Hybrid             Citations
                          │
                      Reranking
                          │
                   Context Assembly
                          │
                ┌─────────┴─────────┐
                │                   │
           EVALUATION          PRODUCTION
                │                   │
           RAGAS/MRR            Scaling
           Recall@K             Security
           NDCG                 Caching
           Faithfulness         Monitoring
                          │
                    ADVANCED RAG
                          │
        ┌──────────┬──────┴──────┬──────────┐
      CRAG      Self-RAG      Agentic    GraphRAG
                          │
                       RAPTOR
                          │
                  Multimodal RAG
```

---

## How to study this

1. Read the chapter README for the 60-second summary.
2. Work through the notebook top to bottom — **run every cell**, don't just read.
3. Break things on purpose: change chunk size, change `top_k`, delete a document
   and watch retrieval fail. The failure modes are where the real learning is.
4. Close the notebook and answer the interview questions at the end from memory.
