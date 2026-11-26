<div align="center">

# 07 · Hybrid Search

<img src="https://img.shields.io/badge/Chapters-8-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-0-10B981?style=for-the-badge" alt="done"/>

**Combining sparse and dense retrieval: normalization, fusion, RRF and tuning.**

</div>

<p align="center"><a href="../06.%20Dense%20Retrieval%20and%20Vector%20Search/README.md">Previous group: 06 Dense Retrieval and Vector Search</a> | <a href="../README.md">Home</a> | <a href="../08.%20Query%20Understanding%20and%20Transformation/README.md">Next group: 08 Query Understanding and Transformation</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 Why Combine<br/>BM25 and Dense<br/>Retrieval"] --> n2["02 Hybrid Search<br/>Architecture"] --> n3["03 Score<br/>Normalization"] --> n4["04 Weighted<br/>Score Fusion"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R1["05 to 08"]
        direction LR
        n5["05 Dynamic<br/>Hybrid Weighting"] --> n6["06 Reciprocal<br/>Rank Fusion RRF"] --> n7["07 Alpha Fusion<br/>Weight<br/>Optimization"] --> n8["08 Top-K<br/>Strategy and<br/>Candidate Pool<br/>Tuning"]
    end
    style R1 fill:#F8FAFC,stroke:#CBD5E1
    R0 --> R1
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="6%">Sr&nbsp;No</th><th width="22%">Chapter</th><th width="46%">Key Concepts</th><th width="8%">Interview Priority</th><th width="6%">Notes</th><th width="6%">Notebook</th><th width="6%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Why Combine BM25 and Dense Retrieval</b></td><td>Where BM25 wins, where dense wins, both succeed, both fail, complementary signals</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">02</td><td><b>Hybrid Search Architecture</b></td><td>Parallel sparse and dense branches, candidate pools, fusion, reranker, LLM; Why combine BM25 and dense, score normalization, weighted fusion, Reciprocal Rank Fusion, tuning alpha</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td><b>Score Normalization</b></td><td>Min-max, z-score, score scaling, relative score normalization</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">04</td><td><b>Weighted Score Fusion</b></td><td>HybridScore = alpha x dense + (1 - alpha) x sparse, choosing weights</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">05</td><td><b>Dynamic Hybrid Weighting</b></td><td>Query-dependent alpha, exact vs semantic query detection, production heuristics</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">06</td><td><b>Reciprocal Rank Fusion RRF</b></td><td>RRF formula, k parameter, rank-based fusion, why RRF is robust, RRF vs weighted</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">07</td><td><b>Alpha Fusion Weight Optimization</b></td><td>Alpha grid search on evaluation sets, picking the best weight</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">08</td><td><b>Top-K Strategy and Candidate Pool Tuning</b></td><td>Top-K per retriever, candidate pool size, recall vs reranker cost</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
