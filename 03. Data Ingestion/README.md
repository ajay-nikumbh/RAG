<div align="center">

# 03 · Data Ingestion

<img src="https://img.shields.io/badge/Chapters-15-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-0-10B981?style=for-the-badge" alt="done"/>

**Turning PDFs, scans, office files and structured data into clean, versioned, retrievable documents.**

</div>

<p align="center"><a href="../02.%20RAG%20Introduction/README.md">Previous group: 02 RAG Introduction</a> | <a href="../README.md">Home</a> | <a href="../04.%20Chunking%20and%20Metadata/README.md">Next group: 04 Chunking and Metadata</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 Ingestion<br/>Overview"] --> n2["02 Why Ingestion<br/>and Canonical<br/>Documents"] --> n3["03 PDF Parsing"] --> n4["04 OCR and<br/>Scanned<br/>Documents"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R1["05 to 08"]
        direction LR
        n5["05 DOCX HTML and<br/>Markdown"] --> n6["06 Structured<br/>Data CSV JSON DB<br/>API"] --> n7["07 Metadata and<br/>Provenance"] --> n8["08 Cleaning and<br/>Normalization"]
    end
    style R1 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R2["09 to 12"]
        direction LR
        n9["09 Deduplication<br/>and Versioning"] --> n10["10 Incremental<br/>Ingestion"] --> n11["11 Tables Images<br/>and Special<br/>Formats"] --> n12["12 Security and<br/>Access Control<br/>in Ingestion"]
    end
    style R2 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R3["13 to 15"]
        direction LR
        n13["13 Production<br/>Ingestion<br/>Architecture"] --> n14["14 Validation<br/>and<br/>Observability"] --> n15["15 End-to-End<br/>Ingestion<br/>Pipeline"]
    end
    style R3 fill:#F8FAFC,stroke:#CBD5E1
    R0 --> R1
    R1 --> R2
    R2 --> R3
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="6%">Sr&nbsp;No</th><th width="22%">Chapter</th><th width="46%">Key Concepts</th><th width="8%">Interview Priority</th><th width="6%">Notes</th><th width="6%">Notebook</th><th width="6%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Ingestion Overview</b></td><td>Why ingestion caps everything downstream, real PDF/OCR/DOCX parsing on real documents, metadata, dedup, versioning, incremental ingestion</td><td align="center">High</td><td align="center">-</td><td align="center"><a href="01.%20Ingestion%20Overview/notebooks/01.%20Ingestion%20Overview.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">02</td><td><b>Why Ingestion and Canonical Documents</b></td><td>The quality ceiling, ingestion ≠ chunking, canonical schema, `raw_text` vs `clean_text`, connectors</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="02.%20Why%20Ingestion%20and%20Canonical%20Documents/notebooks/02.%20Why%20Ingestion%20and%20Canonical%20Documents.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">03</td><td><b>PDF Parsing</b></td><td>PDF is not a text format, page provenance, reading order, heading detection by font weight, what `get_text()` silently misses</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="03.%20PDF%20Parsing/notebooks/03.%20PDF%20Parsing.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">04</td><td><b>OCR and Scanned Documents</b></td><td>Rendering to image, real Tesseract confidence scores, three-tier routing, character confusions, cost modelling</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="04.%20OCR%20and%20Scanned%20Documents/notebooks/04.%20OCR%20and%20Scanned%20Documents.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">05</td><td><b>DOCX HTML and Markdown</b></td><td>Native structure extraction, heading context, boilerplate removal</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="05.%20DOCX%20HTML%20and%20Markdown/notebooks/05.%20DOCX%20HTML%20and%20Markdown.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">06</td><td><b>Structured Data CSV JSON DB API</b></td><td>What is one retrievable unit, row serialization, nested JSON, when not to embed, live APIs</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="06.%20Structured%20Data%20CSV%20JSON%20DB%20API/notebooks/06.%20Structured%20Data%20CSV%20JSON%20DB%20API.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">07</td><td><b>Metadata and Provenance</b></td><td>Six metadata categories, filtering precision, deterministic vs LLM extraction, citation chains</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="07.%20Metadata%20and%20Provenance/notebooks/07.%20Metadata%20and%20Provenance.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">08</td><td><b>Cleaning and Normalization</b></td><td>Whitespace, line wrap, hyphenation, Unicode, header/footer detection on real pages, the over-cleaning trap</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="08.%20Cleaning%20and%20Normalization/notebooks/08.%20Cleaning%20and%20Normalization.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">09</td><td><b>Deduplication and Versioning</b></td><td>SHA-256, Jaccard similarity, MinHash/LSH at scale, effective vs publication date, amendments</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="09.%20Deduplication%20and%20Versioning/notebooks/09.%20Deduplication%20and%20Versioning.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">10</td><td><b>Incremental Ingestion</b></td><td>Change detection, deletion handling, stable IDs, idempotency, atomic replacement</td><td align="center">Medium</td><td align="center">-</td><td align="center"><a href="10.%20Incremental%20Ingestion/notebooks/10.%20Incremental%20Ingestion.ipynb">Open</a></td><td align="center">Notebook</td></tr>
<tr><td align="center">11</td><td><b>Tables Images and Special Formats</b></td><td>Table serialization, figures, PowerPoint, Excel, email, code, legal documents</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">12</td><td><b>Security and Access Control in Ingestion</b></td><td>Permissions travel with the document, ACL inheritance, PII handling</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">13</td><td><b>Production Ingestion Architecture</b></td><td>Three-layer storage, batch vs event-driven, backpressure, retries, dead-letter queues, cost</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">14</td><td><b>Validation and Observability</b></td><td>Pre-chunking validation, anomaly detection, metrics, golden document sets, parser benchmarking</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">15</td><td><b>End-to-End Ingestion Pipeline</b></td><td>Anti-patterns, the debugging ladder, interview preparation</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
