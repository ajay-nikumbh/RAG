<div align="center">

# 08 · Query Understanding and Transformation

<img src="https://img.shields.io/badge/Chapters-6-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-0-10B981?style=for-the-badge" alt="done"/>

**Cleaning, expanding and rewriting the query before retrieval.**

</div>

<p align="center"><a href="../07.%20Hybrid%20Search/README.md">Previous group: 07 Hybrid Search</a> | <a href="../README.md">Home</a> | <a href="../09.%20Advanced%20Retrieval%20Strategies/README.md">Next group: 09 Advanced Retrieval Strategies</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 Query<br/>Preprocessing"] --> n2["02 Query<br/>Expansion"] --> n3["03 Query<br/>Transformation"] --> n4["04 Multi-Query<br/>Retrieval"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R1["05 to 06"]
        direction LR
        n5["05 HyDE<br/>Hypothetical<br/>Document<br/>Embeddings"] --> n6["06 Query<br/>Rewriting for<br/>Conversational<br/>RAG"]
    end
    style R1 fill:#F8FAFC,stroke:#CBD5E1
    R0 --> R1
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="7%">Sr No</th><th width="25%">Chapter</th><th width="44%">Key Concepts</th><th width="8%">Notes</th><th width="8%">Notebook</th><th width="8%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="01.%20Query%20Preprocessing"><b>Query Preprocessing</b></a></td><td>Lowercasing, punctuation, stopwords, spell correction, preserving IDs and numbers; Spell correction, intent detection, entity extraction before retrieval</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">02</td><td><a href="02.%20Query%20Expansion"><b>Query Expansion</b></a></td><td>Synonym expansion, LLM expansion, metadata expansion, domain dictionaries</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td><a href="03.%20Query%20Transformation"><b>Query Transformation</b></a></td><td>Query expansion, HyDE, Query2Doc, step-back prompting, multi-query retrieval</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">04</td><td><a href="04.%20Multi-Query%20Retrieval"><b>Multi-Query Retrieval</b></a></td><td>LLM-generated sub-queries, parallel retrieval, fusing multiple result lists</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">05</td><td><a href="05.%20HyDE%20Hypothetical%20Document%20Embeddings"><b>HyDE Hypothetical Document Embeddings</b></a></td><td>Hypothetical answer generation, embedding the answer, vector search</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">06</td><td><a href="06.%20Query%20Rewriting%20for%20Conversational%20RAG"><b>Query Rewriting for Conversational RAG</b></a></td><td>Conversational context, follow-up rewriting, standalone queries</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
