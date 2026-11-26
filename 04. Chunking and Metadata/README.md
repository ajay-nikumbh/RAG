<div align="center">

# 04 · Chunking and Metadata

<img src="https://img.shields.io/badge/Chapters-4-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-0-10B981?style=for-the-badge" alt="done"/>

**How documents are split and labelled before indexing.**

</div>

<p align="center"><a href="../03.%20Data%20Ingestion/README.md">Previous group: 03 Data Ingestion</a> | <a href="../README.md">Home</a> | <a href="../05.%20Sparse%20Retrieval/README.md">Next group: 05 Sparse Retrieval</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 Document<br/>Chunking"] --> n2["02 Chunking for<br/>Hybrid Search"] --> n3["03 Metadata<br/>Indexing and<br/>Filtering"] --> n4["04 Field-Aware<br/>Search"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="7%">Sr No</th><th width="25%">Chapter</th><th width="44%">Key Concepts</th><th width="8%">Notes</th><th width="8%">Notebook</th><th width="8%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="01.%20Document%20Chunking"><b>Document Chunking</b></a></td><td>Why chunk size and overlap decide retrieval quality; fixed, semantic, recursive and structure-aware chunking</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">02</td><td><a href="02.%20Chunking%20for%20Hybrid%20Search"><b>Chunking for Hybrid Search</b></a></td><td>Fixed, recursive, semantic, paragraph, sliding-window, parent-child chunking</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td><a href="03.%20Metadata%20Indexing%20and%20Filtering"><b>Metadata Indexing and Filtering</b></a></td><td>Metadata schema, pre-filtering vs post-filtering, structured + unstructured search; Pre- vs post-filtering, self-query retrieval, access-control filters, field-aware search</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">04</td><td><a href="04.%20Field-Aware%20Search"><b>Field-Aware Search</b></a></td><td>Title, summary and body fields, field weights, BM25F-style boosting</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
