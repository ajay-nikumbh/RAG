# Chapter 2 — Documents, Data Sources & Ingestion

> **Prerequisites:** [Chapter 1 — RAG Fundamentals](../01_rag_fundamentals/)
> **Next:** Chapter 3 — Document Chunking

---

## 60-second summary

Chapter 1 ended with `Documents → Chunk → Embed`. This chapter is **everything before that
first arrow** — and it is where most real-world RAG systems quietly fail.

> **A retriever cannot retrieve information that ingestion failed to capture.**

$$Q_{\text{RAG}} \approx Q_{\text{ingestion}} \times Q_{\text{retrieval}} \times Q_{\text{generation}}$$

If ingestion scores 0.4, a perfect retriever and a perfect LLM are still capped at 0.4.

---

## Why this chapter is split into 14 modules

The source material for this chapter is ~170 sections. As one notebook it was unusable —
too long to navigate, too long to re-run, and impossible to dip back into.

Each module below is **self-contained and independently runnable**. Work through them in
order the first time; afterwards treat them as reference.

---

## Modules

| # | Module | What it covers | Real documents used |
|---|--------|----------------|---------------------|
| 2a | [Why Ingestion Matters & The Canonical Document](2a_why_ingestion_and_canonical_documents/) | The quality ceiling · ingestion ≠ chunking · canonical schema · `raw_text` vs `clean_text` · connectors | GDPR (citation example) |
| 2b | [PDF Parsing](2b_pdf_parsing/) | Why PDF is hard · classify before extracting · page provenance · **reading order** · heading detection · what `get_text()` misses | BERT paper, RAG paper, IRS W-4, GDPR |
| 2c | [OCR & Scanned Documents](2c_ocr_and_scanned_documents/) | Rendering to image · **real Tesseract confidence** · three-tier routing · character confusions · cost modelling | Tesseract test scans, IRS W-4 |
| 2d | [DOCX, HTML & Markdown](2d_docx_html_markdown/) | Formats that carry their own structure · heading context · boilerplate removal | Calibre demo DOCX, GDPR HTML |
| 2e | [Structured Data: CSV, JSON, DB, API](2e_structured_data_csv_json_db_api/) | What is one retrievable unit? · row serialization · nested JSON · when *not* to embed · live APIs | Titanic CSV, live GitHub/OpenAlex APIs |
| 2f | [Metadata & Provenance](2f_metadata_and_provenance/) | Six metadata categories · filtering precision · deterministic vs LLM extraction · citation chains | GDPR |
| 2g | [Cleaning & Normalization](2g_cleaning_and_normalization/) | Whitespace · line wrap · hyphenation · Unicode · **header/footer detection on 88 real pages** · the over-cleaning trap | GDPR |
| 2h | [Deduplication & Versioning](2h_deduplication_and_versioning/) | SHA-256 · Jaccard · MinHash/LSH at scale · versions · effective vs publication date · amendments | GDPR PDF vs HTML |
| 2i | [Incremental Ingestion](2i_incremental_ingestion/) | Change detection · **deletion handling** · stable IDs · idempotency · atomic replacement | Corpus checksums |
| 2j | [Tables, Images & Special Formats](2j_tables_images_special_formats/) | Table serialization · when serialization is not enough · figures · PowerPoint, Excel, email, code, legal | IRS W-4 tables, Calibre DOCX tables |
| 2k | [Security & Access Control](2k_security_and_access_control/) | Permissions travel with the document · ACL inheritance · PII · why prompts are not a security boundary | — |
| 2l | [Production Architecture](2l_production_architecture/) | Three-layer storage · batch vs event-driven · queues · backpressure · retries · DLQ · cost | — |
| 2m | [Validation & Observability](2m_validation_and_observability/) | Validate before chunking · anomaly detection · metrics · golden document sets · parser benchmarking | Full corpus |
| 2n | [End-to-End Pipeline](2n_end_to_end_pipeline/) | Everything assembled · anti-patterns · the debugging ladder · interview prep | Full corpus |

---

## Real documents, not dummy ones

Every example in this chapter runs on **real public documents**, fetched and cached by
[`utils/corpus.py`](../utils/corpus.py). Each was chosen because it demonstrates a specific
failure mode that a hand-made file cannot.

```python
from utils.corpus import describe, fetch
describe()                 # see the catalogue and what each document teaches
path = fetch("gdpr_pdf")   # downloads once, cached thereafter
```

| Document | Source | Why it is here |
|---|---|---|
| **GDPR** (88 pp) | EUR-Lex | Real repeated headers on 88/88 pages; `Article N(n)(a)` citations; headings marked by **weight, not size** |
| **BERT paper** | arXiv 1810.04805 | Genuinely two-column — the reading-order problem, reproducible |
| **RAG paper** | arXiv 2005.11401 | **Single**-column — the control case that breaks a naive column splitter |
| **IRS Form W-4** | irs.gov | 48 AcroForm fields that `get_text()` never returns |
| **Calibre demo DOCX** | calibre-ebook.com | Real Heading 1/2 hierarchy, 5 tables, TOC, footnotes |
| **Tesseract scans** | tesseract-ocr/test | Real OCR confidence, including multilingual degradation |
| **Titanic CSV** | datasciencedojo | 891 real rows with genuine missing values |

All are public-domain, EU-reuse-licensed, Apache-2.0 or GPL. The corpus is **git-ignored** —
you download it, you do not redistribute it.

### Things the real documents revealed

These are findings from actually running the code, not hypotheticals:

- **The RAG paper is single-column**, despite being an arXiv NLP paper. A naive
  "academic paper ⇒ two columns" assumption shreds it.
- **GDPR headings are 9.6pt — identical to body text.** A size-based heading detector finds
  **zero** headings; detecting font *weight* recovers the real Article headings.
- **The IRS W-4 hides 48 form fields.** Text extraction reports a confident 26,092
  characters and silently omits every field value.
- **A naive frequency filter flags `'3.'` on 49/88 GDPR pages** — those are list numbers,
  not boilerplate. A real false positive.
- **OCR round-trip recall is 97%** on a real form — and the 3% are plausible-looking
  near-misses, which is what makes them dangerous.

---

## The 12 key principles

1. **Garbage In → Garbage Out.** RAG quality begins with data quality.
2. PDF extraction is **not** trivial text reading.
3. **Preserve structure:** headings · sections · tables · pages · figures.
4. **Keep metadata.**
5. **Keep provenance.**
6. **Carry ACL/security metadata** during ingestion, not after.
7. **Maintain stable document IDs** (never `uuid4()` per run).
8. **Deduplicate** documents.
9. **Handle versions, updates and deletions.**
10. **Keep original/raw content** where feasible.
11. Use **incremental** rather than complete re-indexing.
12. **Do not flatten valuable structure** before chunking.

---

## Key formulas

| Formula | Meaning | Module |
|---|---|---|
| $Q_{\text{RAG}} \approx Q_{\text{ing}} \times Q_{\text{ret}} \times Q_{\text{gen}}$ | Ingestion caps everything downstream | 2a |
| $C_{\text{page}} = \frac{1}{N}\sum c_i$ | Average OCR confidence | 2c |
| $f(l) = \frac{\#\text{pages containing } l}{N}$ | Boilerplate detection frequency | 2g |
| $J(A,B) = \frac{\lvert A \cap B\rvert}{\lvert A \cup B\rvert}$ | Jaccard near-duplicate similarity | 2h |
| $O(N^2)$ | Why naive pairwise dedup fails at scale | 2h |
| $f(f(x)) = f(x)$ | Idempotency | 2i |
| $\text{delay}_n = \min(d_{\max}, d_0 \cdot 2^n)$ | Exponential backoff | 2l |
| $L = T_{\text{indexed}} - T_{\text{source}}$ | Freshness lag vs SLA | 2m |
| $R_\alpha = N_\alpha / N$ | Alphabetic ratio (corruption signal) | 2m |

---

## The architecture to memorize

```
EXTERNAL SOURCES → CONNECTORS → RAW STORAGE → FILE ROUTER
        │
        ├── PDF  → PDF Parser ──┬── text detected
        │                       └── scan → OCR
        ├── DOCX → DOCX Parser
        └── HTML → DOM Parser
        │
        ▼
STRUCTURE LAYER → CLEANING → NORMALIZATION → METADATA
        → SECURITY/ACL → DEDUP/VERSION → VALIDATION
        → CANONICAL DOCUMENT → CHUNKING
```

### Three-layer storage

```
Layer 1 — RAW          Layer 2 — CANONICAL      Layer 3 — RETRIEVAL INDEX
original files         text, layout, tables,    chunks, embeddings,
                       metadata, provenance     BM25 index, filters
```

Change your chunking strategy → re-run Layer 2 → 3 without re-parsing a single PDF.
Find a parser bug → re-run Layer 1 → 2 without re-downloading 10M files.

---

## Setup

```bash
pip install -r ../requirements.txt

# For module 2c only - OCR needs a binary as well as the Python package:
brew install tesseract          # macOS
sudo apt install tesseract-ocr  # Ubuntu
```

**No OpenAI key needed for this chapter** — it is entirely local parsing and text
processing. Every module guards on optional dependencies and skips gracefully.

First run downloads ~5 MB of real documents into `../assets/real_corpus/` (git-ignored,
cached thereafter).

---

## The interview answer

> I separate ingestion into connectors, raw storage, parser routing, structure extraction,
> cleaning and normalization, metadata and ACL enrichment, deduplication/versioning,
> validation, and canonical storage. PDFs may require digital-text extraction or OCR/layout
> parsing depending on their type. I preserve provenance and structural information such as
> sections, pages, tables, and headings because downstream chunking and citations depend on
> it. The pipeline should be incremental, idempotent, observable, retryable, and capable of
> propagating updates and deletions into the retrieval index.
