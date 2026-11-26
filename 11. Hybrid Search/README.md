<div align="center">

# Chapter 11 · Hybrid Search

<img src="https://img.shields.io/badge/Part%20II%20%C2%B7%20Storage%20and%20Search-6366F1?style=for-the-badge" alt="part"/> <img src="https://img.shields.io/badge/Status-Planned-94A3B8?style=for-the-badge" alt="status"/>

**Why combine BM25 and dense, score normalization, weighted fusion, Reciprocal Rank Fusion, tuning alpha.**

</div>

<p align="center"><a href="../10.%20Dense%20Retrieval/10a.%20Dense%20Vector%20Retrieval/README.md">Previous: 10a Dense Vector Retrieval</a> | <a href="../README.md">Home</a> | <a href="#modules">Modules</a> | <a href="11a.%20Why%20Combine%20BM25%20and%20Dense%20Retrieval/README.md">Next: 11a Why Combine BM25 and Dense Retrieval</a></p>

## Modules

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="10%">Module</th><th width="30%">Topic</th><th width="40%">Key Concepts</th><th width="12%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td align="center">11a</td><td><a href="11a.%20Why%20Combine%20BM25%20and%20Dense%20Retrieval">Why Combine BM25 and Dense Retrieval</a></td><td>Where BM25 wins, where dense wins, both succeed, both fail, complementary signals</td><td align="center">Planned</td></tr>
<tr><td align="center">02</td><td align="center">11b</td><td><a href="11b.%20Hybrid%20Search%20Architecture">Hybrid Search Architecture</a></td><td>Parallel sparse and dense branches, candidate pools, fusion, reranker, LLM</td><td align="center">Planned</td></tr>
<tr><td align="center">03</td><td align="center">11c</td><td><a href="11c.%20Score%20Normalization">Score Normalization</a></td><td>Min-max, z-score, score scaling, relative score normalization</td><td align="center">Planned</td></tr>
<tr><td align="center">04</td><td align="center">11d</td><td><a href="11d.%20Weighted%20Score%20Fusion">Weighted Score Fusion</a></td><td>HybridScore = alpha x dense + (1 - alpha) x sparse, choosing weights</td><td align="center">Planned</td></tr>
<tr><td align="center">05</td><td align="center">11e</td><td><a href="11e.%20Dynamic%20Hybrid%20Weighting">Dynamic Hybrid Weighting</a></td><td>Query-dependent alpha, exact vs semantic query detection, production heuristics</td><td align="center">Planned</td></tr>
<tr><td align="center">06</td><td align="center">11f</td><td><a href="11f.%20Reciprocal%20Rank%20Fusion%20RRF">Reciprocal Rank Fusion RRF</a></td><td>RRF formula, k parameter, rank-based fusion, why RRF is robust, RRF vs weighted</td><td align="center">Planned</td></tr>
<tr><td align="center">07</td><td align="center">11g</td><td><a href="11g.%20Alpha%20Fusion%20Weight%20Optimization">Alpha Fusion Weight Optimization</a></td><td>Alpha grid search on evaluation sets, picking the best weight</td><td align="center">Planned</td></tr>
</tbody>
</table>
