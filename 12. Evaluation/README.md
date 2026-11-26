<div align="center">

# 12 · Evaluation

<img src="https://img.shields.io/badge/Chapters-11-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-0-10B981?style=for-the-badge" alt="done"/>

**Measuring retrieval and generation, and finding where a wrong answer came from.**

</div>

<p align="center"><a href="../11.%20Context%20and%20Generation/README.md">Previous group: 11 Context and Generation</a> | <a href="../README.md">Home</a> | <a href="../13.%20Advanced%20RAG%20Architectures/README.md">Next group: 13 Advanced RAG Architectures</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 RAG<br/>Evaluation<br/>Fundamentals"] --> n2["02 Precision at<br/>K and Recall at<br/>K"] --> n3["03 Hit Rate<br/>Success at K"] --> n4["04 MRR Mean<br/>Reciprocal Rank"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R1["05 to 08"]
        direction LR
        n5["05 MAP Mean<br/>Average<br/>Precision"] --> n6["06 NDCG"] --> n7["07 Compare<br/>Retrieval<br/>Strategies"] --> n8["08 Generation<br/>Metrics"]
    end
    style R1 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R2["09 to 11"]
        direction LR
        n9["09 RAG<br/>Evaluation<br/>Frameworks"] --> n10["10 Synthetic<br/>Evaluation<br/>Datasets"] --> n11["11 Failure<br/>Analysis and<br/>Retrieval<br/>Debugging"]
    end
    style R2 fill:#F8FAFC,stroke:#CBD5E1
    R0 --> R1
    R1 --> R2
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="6%">Sr&nbsp;No</th><th width="22%">Chapter</th><th width="46%">Key Concepts</th><th width="8%">Interview Priority</th><th width="6%">Notes</th><th width="6%">Notebook</th><th width="6%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>RAG Evaluation Fundamentals</b></td><td>Why evaluating RAG is hard; offline vs online evaluation; retrieval evaluation basics; Relevance labels, offline evaluation, metric selection</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">02</td><td><b>Precision at K and Recall at K</b></td><td>Precision@K, Recall@K, worked examples; Precision@K, Recall@K, Hit rate, MRR, MAP, NDCG derived and computed by hand</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td><b>Hit Rate Success at K</b></td><td>Hit rate, Success@K, when a single hit is enough</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">04</td><td><b>MRR Mean Reciprocal Rank</b></td><td>Reciprocal rank, MRR across queries</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">05</td><td><b>MAP Mean Average Precision</b></td><td>Average precision, MAP across queries</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">06</td><td><b>NDCG</b></td><td>Graded relevance, DCG, IDCG, NDCG@K</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">07</td><td><b>Compare Retrieval Strategies</b></td><td>BM25 vs dense vs weighted vs RRF vs reranker on Recall, MRR, NDCG, latency, cost</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">08</td><td><b>Generation Metrics</b></td><td>Faithfulness, groundedness, hallucination rate</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">09</td><td><b>RAG Evaluation Frameworks</b></td><td>RAGAS, DeepEval, TruLens, LLM-as-a-judge</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">10</td><td><b>Synthetic Evaluation Datasets</b></td><td>Generating ground truth, hard negatives, evaluation-set design</td><td align="center">Medium</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">11</td><td><b>Failure Analysis and Retrieval Debugging</b></td><td>Attributing a wrong answer to ingestion, retrieval or generation; retrieval debugging; Failure modes, diagnostic logging per stage, debugging retrieval</td><td align="center">High</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
