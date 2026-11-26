<div align="center">

# 02.03 · Lexical vs Semantic Retrieval

<img src="https://img.shields.io/badge/02%20%C2%B7%20RAG%20Introduction-6366F1?style=for-the-badge" alt="group"/> <img src="https://img.shields.io/badge/Status-Done-10B981?style=for-the-badge" alt="status"/>

**FastAPI, Milvus or Elasticsearch, BM25, dense search, RRF, reranker, LLM.**

</div>

<p align="center"><a href="../02.%20What%20is%20Hybrid%20Search%20RAG/README.md">Previous: 02.02 What is Hybrid Search RAG</a> | <a href="../../README.md">Home</a> | <a href="../README.md">Group 02: RAG Introduction</a> | <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md">Notes</a> | <a href="../../03.%20Data%20Ingestion/01.%20Ingestion%20Overview/README.md">Next: 03.01 Ingestion Overview</a></p>


## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Jupyter notebook</b></td><td>Original notebook with full code and outputs</td><td align="center"><a href="notebooks/03.%20Lexical%20vs%20Semantic%20Retrieval.ipynb">Open</a></td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Result charts from the notebook (3 used in the notes)</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Chapter datasets (the notebook builds its corpus inline)</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks (last section of the notes)</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Syllabus coverage

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="50%">Syllabus subtopic</th><th width="30%">Covered in</th><th width="12%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td>Exact keyword matching</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#5-lexical-retrieval--first-principles">Section 5</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#6-simplest-lexical-idea--token-overlap">Section 6</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#10-exact-match-strength">Section 10</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>Semantic similarity</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#11-semantic--dense-retrieval">Section 11</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#12-cosine-similarity--from-zero">Section 12</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#13-dense-search--full-internal-flow">Section 13</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#14-semantic-neighborhood">Section 14</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>Vocabulary mismatch problem</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#7-vocabulary-mismatch">Section 7</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>Synonyms</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#7-vocabulary-mismatch">Section 7</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#14-semantic-neighborhood">Section 14</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>Acronyms</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#22-acronyms-and-domain-language">Section 22</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>Product/model numbers</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#52-tokenization-can-affect-ids">Section 5.2</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#17-product-ids--dense-search-weakness">Section 17</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#19-version-numbers">Section 19</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>Legal/regulatory terminology</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#18-article-numbers">Section 18</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#20-number-sensitivity">Section 20</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#21-negation">Section 21</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>Rare entities</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#8-tf-idf--better-lexical-weighting">Section 8</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#22-acronyms-and-domain-language">Section 22</a></td><td align="center">Done</td></tr>
<tr><td align="center">09</td><td>Comparison examples</td><td align="center"><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#16-compare-sparse-and-dense-search-directly">Section 16</a> · <a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#32-failure-matrix">Section 32</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#1-what-is-a-vector"><b>1. What Is a Vector?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">02</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#2-why-do-we-need-two-retrieval-styles"><b>2. Why Do We Need Two Retrieval Styles?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#3-build-a-small-enterprise-style-corpus"><b>3. Build a Small Enterprise-Style Corpus</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">04</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#4-basic-retrieval-vocabulary"><b>4. Basic Retrieval Vocabulary</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">05</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#5-lexical-retrieval--first-principles"><b>5. Lexical Retrieval — First Principles</b></a></td><td align="center">2</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">06</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#6-simplest-lexical-idea--token-overlap"><b>6. Simplest Lexical Idea — Token Overlap</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">07</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#7-vocabulary-mismatch"><b>7. Vocabulary Mismatch</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">08</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#8-tf-idf--better-lexical-weighting"><b>8. TF-IDF — Better Lexical Weighting</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">09</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#9-sparse-search--full-internal-flow"><b>9. Sparse Search — Full Internal Flow</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">10</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#10-exact-match-strength"><b>10. Exact-Match Strength</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">11</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#checkpoint-1"><b>CHECKPOINT 1</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">12</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#11-semantic--dense-retrieval"><b>11. Semantic / Dense Retrieval</b></a></td><td align="center">2</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">13</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#12-cosine-similarity--from-zero"><b>12. Cosine Similarity — From Zero</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">14</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#13-dense-search--full-internal-flow"><b>13. Dense Search — Full Internal Flow</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">15</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#14-semantic-neighborhood"><b>14. Semantic Neighborhood</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">16</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#15-visualize-embeddings-in-2d"><b>15. Visualize Embeddings in 2D</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">17</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#checkpoint-2"><b>CHECKPOINT 2</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">18</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#16-compare-sparse-and-dense-search-directly"><b>16. Compare Sparse and Dense Search Directly</b></a></td><td align="center">3</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">19</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#17-product-ids--dense-search-weakness"><b>17. Product IDs — Dense Search Weakness</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">20</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#18-article-numbers"><b>18. Article Numbers</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">21</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#19-version-numbers"><b>19. Version Numbers</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">22</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#20-number-sensitivity"><b>20. Number Sensitivity</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">23</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#21-negation"><b>21. Negation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">24</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#22-acronyms-and-domain-language"><b>22. Acronyms and Domain Language</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">25</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#23-three-practical-query-types"><b>23. Three Practical Query Types</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">26</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#24-visualize-sparse-vs-dense-score-distributions"><b>24. Visualize Sparse vs Dense Score Distributions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">27</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#25-hybrid-search--combine-both-signals"><b>25. Hybrid Search — Combine Both Signals</b></a></td><td align="center">2</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">28</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#26-alpha-as-a-dial"><b>26. Alpha as a Dial</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">29</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#27-dynamic-weighting--advanced-preview"><b>27. Dynamic Weighting — Advanced Preview</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">30</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#28-retrieval-evaluation"><b>28. Retrieval Evaluation</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">31</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#29-retrieval-debugging-framework"><b>29. Retrieval Debugging Framework</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">32</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#30-production-mental-model"><b>30. Production Mental Model</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">33</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#31-retrieval-is-not-reasoning"><b>31. Retrieval Is Not Reasoning</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">34</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#32-failure-matrix"><b>32. Failure Matrix</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">35</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#checkpoint-3"><b>CHECKPOINT 3</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">36</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#33-interview-questions"><b>33. Interview Questions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">37</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#34-interview-scenarios"><b>34. Interview Scenarios</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">38</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#35-one-page-revision-map"><b>35. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">39</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#36-practice-tasks"><b>36. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">40</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#37-final-takeaways"><b>37. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">41</td><td><a href="notes/03.%20Lexical%20vs%20Semantic%20Retrieval.md#next-chapter"><b>Next Chapter</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
