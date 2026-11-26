<div align="center">

# 10 · Reranking

<img src="https://img.shields.io/badge/Chapters-4-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-0-10B981?style=for-the-badge" alt="done"/>

**A second, more precise pass over the retrieved candidates.**

</div>

<p align="center"><a href="../09.%20Advanced%20Retrieval%20Strategies/README.md">Previous group: 09 Advanced Retrieval Strategies</a> | <a href="../README.md">Home</a> | <a href="../11.%20Context%20and%20Generation/README.md">Next group: 11 Context and Generation</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 Why Hybrid<br/>Search Still<br/>Needs Reranking"] --> n2["02 Bi-Encoder vs<br/>Cross-Encoder"] --> n3["03 Cross-Encoder<br/>Reranking"] --> n4["04 LLM-Based<br/>Reranking"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="7%">Sr No</th><th width="25%">Chapter</th><th width="44%">Key Concepts</th><th width="8%">Notes</th><th width="8%">Notebook</th><th width="8%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="01.%20Why%20Hybrid%20Search%20Still%20Needs%20Reranking"><b>Why Hybrid Search Still Needs Reranking</b></a></td><td>Hybrid gives candidates, reranker gives precision, Top-50 to Top-5; Cross-encoders vs bi-encoders, LLM reranking, why similar isn't relevant</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">02</td><td><a href="02.%20Bi-Encoder%20vs%20Cross-Encoder"><b>Bi-Encoder vs Cross-Encoder</b></a></td><td>Bi-encoder vs cross-encoder, joint query-document scoring, speed vs accuracy</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td><a href="03.%20Cross-Encoder%20Reranking"><b>Cross-Encoder Reranking</b></a></td><td>BGE, Cohere and Jina rerankers, candidate size, latency budget</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">04</td><td><a href="04.%20LLM-Based%20Reranking"><b>LLM-Based Reranking</b></a></td><td>Pointwise, pairwise and listwise LLM reranking, token cost, latency</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
