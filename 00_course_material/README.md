# Course Material

The source PDFs this course is built from. Each notebook in the repo corresponds to one
of these chapters, expanded with runnable code.

| File | Becomes |
|------|---------|
| `00. RAG syllabus.pdf` | The 55-chapter roadmap in the root [README](../README.md) |
| `01. RAG Fundamentals.pdf` | [Chapter 1](../01_rag_fundamentals/) |
| `02. Documents, Data Sources & Ingestion for RAG.pdf` | [Chapter 2](../02_documents_data_sources_ingestion/) |

## Adding a new chapter

When you receive the next chapter PDF:

1. Drop it in this folder with its `NN. ` numeric prefix
2. Create `NN_snake_case_name/` at the repo root
3. Add `NN_snake_case_name.ipynb` and `README.md` inside it
4. Flip the status in the root README roadmap table from ⬜ to ✅

> **Note:** these PDFs are exports of a ChatGPT conversation and are kept here for
> reference. They are the *source*, not the deliverable — the notebooks are.
