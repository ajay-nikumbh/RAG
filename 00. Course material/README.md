# Course Material

The source PDFs this course is built from. Each notebook in the repo corresponds to one
of these chapters, expanded with runnable code.

| File | Becomes |
|------|---------|
| `00. RAG syllabus.pdf` | The 55-chapter roadmap in the root [README](../README.md) |
| `01. RAG Fundamentals.pdf` | [Chapter 1](../01.%20Rag%20fundamentals/) |
| `02. Documents, Data Sources & Ingestion for RAG.pdf` | [Chapter 2](../02.%20Documents%20data%20sources%20ingestion/) |

## Adding a new chapter

When the next chapter PDF arrives:

1. Drop it in this folder with its `NN. ` numeric prefix
2. Create a folder at the repo root named `NN. Title Case Name`
3. Add a notebook and `README.md` inside it, sharing that same folder name
4. Flip the status in the root README roadmap table from "Planned" to "Done"

These PDFs are exports of a ChatGPT conversation, kept here for reference. They are the
source, not the deliverable — the notebooks are.

## Hybrid Search syllabus (former Hybrid-RAG repo)

The second source is the Hybrid Search RAG syllabus (45 chapters plus 3 projects). Its chapters were merged into this
course as **modules** inside the matching RAG chapter, for example the old chapter 04 TF-IDF is now module `9c` inside
chapter 09 Sparse Retrieval. The full old-to-new mapping is in the root [README](../README.md#where-the-former-hybrid-rag-chapters-are-now).

## Adding a module

1. Create `NN. Chapter Name/Nx. Module Name/` with `notes/`, `notebooks/`, `diagrams/`, `datasets/`, `exercises/`
2. Name the notes file and notebook after the module folder
3. Update the status in the root README and in the chapter README
