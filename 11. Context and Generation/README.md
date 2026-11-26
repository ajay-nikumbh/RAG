<div align="center">

# 11 · Context and Generation

<img src="https://img.shields.io/badge/Chapters-5-6366F1?style=for-the-badge" alt="chapters"/> <img src="https://img.shields.io/badge/Notes%20done-0-10B981?style=for-the-badge" alt="done"/>

**From retrieved chunks to a grounded, cited answer.**

</div>

<p align="center"><a href="../10.%20Reranking/README.md">Previous group: 10 Reranking</a> | <a href="../README.md">Home</a> | <a href="../12.%20Evaluation/README.md">Next group: 12 Evaluation</a></p>

## Learning flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#EEF2FF','primaryBorderColor':'#6366F1','primaryTextColor':'#1E1B4B','lineColor':'#6366F1'}}}%%
flowchart TB
    subgraph R0["01 to 04"]
        direction LR
        n1["01 Context<br/>Construction"] --> n2["02 Contextual<br/>Compression"] --> n3["03 Prompt<br/>Engineering for<br/>RAG"] --> n4["04 Generation<br/>Layer"]
    end
    style R0 fill:#F8FAFC,stroke:#CBD5E1
    subgraph R1["05 to 05"]
        direction LR
        n5["05<br/>Conversational<br/>RAG"]
    end
    style R1 fill:#F8FAFC,stroke:#CBD5E1
    R0 --> R1
```

## Chapters

**Done** = notes + notebook · **Notebook** = notebook ready, notes coming · **Planned** = folder ready

<table width="100%">
<thead><tr><th width="7%">Sr No</th><th width="25%">Chapter</th><th width="44%">Key Concepts</th><th width="8%">Notes</th><th width="8%">Notebook</th><th width="8%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="01.%20Context%20Construction"><b>Context Construction</b></a></td><td>The lost-in-the-middle problem, deduplication, ordering retrieved chunks</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">02</td><td><a href="02.%20Contextual%20Compression"><b>Contextual Compression</b></a></td><td>Extractive vs LLM-based compression under a token budget</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td><a href="03.%20Prompt%20Engineering%20for%20RAG"><b>Prompt Engineering for RAG</b></a></td><td>Grounding instructions, citation prompting, handling insufficient evidence</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">04</td><td><a href="04.%20Generation%20Layer"><b>Generation Layer</b></a></td><td>Temperature, faithfulness, structured and citation-backed output</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
<tr><td align="center">05</td><td><a href="05.%20Conversational%20RAG"><b>Conversational RAG</b></a></td><td>History-aware retrieval, query rewriting, short vs long-term memory, token-efficient history</td><td align="center">-</td><td align="center">-</td><td align="center">Planned</td></tr>
</tbody>
</table>
