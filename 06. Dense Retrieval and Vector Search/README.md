<div align="center">

# 06 · Dense Retrieval and Vector Search

<img src="https://img.shields.io/badge/Chapters-5-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-2-10B981?style=for-the-badge" alt="done"/>

**Embedding-based retrieval and the indexes that make it fast.**

</div>

<p align="center"><a href="../05.%20Sparse%20Retrieval/README.md">Previous group: 05 Sparse Retrieval</a> | <a href="../README.md">Home</a> | <a href="../07.%20Hybrid%20Search/README.md">Next group: 07 Hybrid Search</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 Dense Vector<br/>Retrieval"] --> n2["02 Vector<br/>Databases"] --> n3["03 Approximate<br/>Nearest Neighbor<br/>Search"] --> n4["04 HNSW<br/>Fundamentals"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R1["05 to 05"]
        direction LR
        n5["05 IVF-Flat and<br/>PQ Indexes"]
    end
    style R1 fill:#F8FAFC,stroke:#CBD5E1
    R0 --> R1
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="7%">Sr No</th><th width="25%">Chapter</th><th width="44%">Key Concepts</th><th width="8%">Notes</th><th width="8%">Notebook</th><th width="8%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="01.%20Dense%20Vector%20Retrieval"><b>Dense Vector Retrieval</b></a></td><td>Embeddings, query and document vectors, embedding models, dense Top-K search; Bi-encoders, Dense Passage Retrieval, why dense alone misses exact matches</td><td align="center"><a href="01.%20Dense%20Vector%20Retrieval/notes/01.%20Dense%20Vector%20Retrieval.md">Read</a></td><td align="center">-</td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td><a href="02.%20Vector%20Databases"><b>Vector Databases</b></a></td><td>FAISS, Milvus, Pinecone, Qdrant, pgvector: when each one fits</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td><a href="03.%20Approximate%20Nearest%20Neighbor%20Search"><b>Approximate Nearest Neighbor Search</b></a></td><td>Exact vs approximate nearest neighbor, recall vs latency, vector databases; HNSW, IVF, product quantization, the recall-vs-latency trade-off</td><td align="center"><a href="03.%20Approximate%20Nearest%20Neighbor%20Search/notes/03.%20Approximate%20Nearest%20Neighbor%20Search.md">Read</a></td><td align="center">-</td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td><a href="04.%20HNSW%20Fundamentals"><b>HNSW Fundamentals</b></a></td><td>HNSW graph layers, M, efConstruction, efSearch, recall and speed trade-offs</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">05</td><td><a href="05.%20IVF-Flat%20and%20PQ%20Indexes"><b>IVF-Flat and PQ Indexes</b></a></td><td>IVF clustering, nlist and nprobe, flat search, product quantization, memory vs accuracy</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
