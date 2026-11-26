<div align="center">

# 13 · Advanced RAG Architectures

<img src="https://img.shields.io/badge/Chapters-12-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-0-10B981?style=for-the-badge" alt="done"/>

**Corrective, self-reflective, agentic, graph, multimodal and structured-data RAG.**

</div>

<p align="center"><a href="../12.%20Evaluation/README.md">Previous group: 12 Evaluation</a> | <a href="../README.md">Home</a> | <a href="../14.%20Production%20RAG/README.md">Next group: 14 Production RAG</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 Advanced RAG<br/>Architectures"] --> n2["02 Corrective<br/>RAG CRAG"] --> n3["03 Self-RAG"] --> n4["04 Adaptive RAG"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R1["05 to 08"]
        direction LR
        n5["05 Agentic RAG"] --> n6["06 Multi-Hop RAG"] --> n7["07 RAPTOR"] --> n8["08 Graph RAG"]
    end
    style R1 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R2["09 to 12"]
        direction LR
        n9["09 Knowledge<br/>Graph and RAG"] --> n10["10 Multimodal<br/>RAG"] --> n11["11 Table RAG"] --> n12["12 Text-to-SQL<br/>and RAG"]
    end
    style R2 fill:#F8FAFC,stroke:#CBD5E1
    R0 --> R1
    R1 --> R2
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="7%">Sr No</th><th width="25%">Chapter</th><th width="44%">Key Concepts</th><th width="8%">Notes</th><th width="8%">Notebook</th><th width="8%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="01.%20Advanced%20RAG%20Architectures"><b>Advanced RAG Architectures</b></a></td><td>Naive vs advanced vs modular RAG, where each variant earns its complexity</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">02</td><td><a href="02.%20Corrective%20RAG%20CRAG"><b>Corrective RAG CRAG</b></a></td><td>Relevance grading and web-search fallback when retrieval confidence is low</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td><a href="03.%20Self-RAG"><b>Self-RAG</b></a></td><td>Reflection tokens: the model checking its own retrieval and output</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">04</td><td><a href="04.%20Adaptive%20RAG"><b>Adaptive RAG</b></a></td><td>Routing simple vs complex queries to different retrieval strategies</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">05</td><td><a href="05.%20Agentic%20RAG"><b>Agentic RAG</b></a></td><td>Tool-calling retrievers, multi-hop reasoning, retry loops with LangGraph</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">06</td><td><a href="06.%20Multi-Hop%20RAG"><b>Multi-Hop RAG</b></a></td><td>Query decomposition and evidence chaining across documents</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">07</td><td><a href="07.%20RAPTOR"><b>RAPTOR</b></a></td><td>Recursive summarization trees for hierarchical retrieval</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">08</td><td><a href="08.%20Graph%20RAG"><b>Graph RAG</b></a></td><td>Knowledge graphs, community detection, local vs global search</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">09</td><td><a href="09.%20Knowledge%20Graph%20and%20RAG"><b>Knowledge Graph and RAG</b></a></td><td>Entity linking, Cypher/SPARQL, hybrid vector + graph retrieval</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">10</td><td><a href="10.%20Multimodal%20RAG"><b>Multimodal RAG</b></a></td><td>Text + images, CLIP-style embeddings, vision-language retrieval</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">11</td><td><a href="11.%20Table%20RAG"><b>Table RAG</b></a></td><td>Why serialization alone fails on numeric tables, and what to do instead</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">12</td><td><a href="12.%20Text-to-SQL%20and%20RAG"><b>Text-to-SQL and RAG</b></a></td><td>Schema retrieval, SQL generation, grounding results back to natural language</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
