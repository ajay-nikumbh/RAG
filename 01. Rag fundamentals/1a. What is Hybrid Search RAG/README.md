<div align="center">

# 1a · What is Hybrid Search RAG

<img src="https://img.shields.io/badge/Part%20I%20%C2%B7%20Foundations-6366F1?style=for-the-badge" alt="part"/> <img src="https://img.shields.io/badge/Diagrams-34-FF3670?style=for-the-badge" alt="diagrams"/> <img src="https://img.shields.io/badge/Code%20examples-8-0EA5E9?style=for-the-badge" alt="code"/>

**Sparse finds exact words, dense finds meaning, hybrid combines both.**

</div>

<p align="center"><a href="../README.md">Previous: 01 RAG Fundamentals</a> | <a href="../../README.md">Home</a> | <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md">Notes</a> | <a href="../README.md">Chapter 01: RAG Fundamentals</a> | <a href="../../02.%20Documents%20data%20sources%20ingestion/README.md">Next: 02 Documents, Data Sources and Ingestion</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Jupyter notebook</b></td><td>Original notebook with full code and outputs</td><td align="center"><a href="notebooks/1a.%20What%20is%20Hybrid%20Search%20RAG.ipynb">Open</a></td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Result charts from the notebook (2 used in the notes)</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Chapter datasets (the notebook builds its corpus inline)</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks (last section of the notes)</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Syllabus coverage

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="50%">Syllabus subtopic</th><th width="30%">Covered in</th><th width="12%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td>Traditional RAG recap</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#0-the-big-picture-before-any-code">Section 0</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#1-rag-architecture--visual-mental-model">Section 1</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>Retrieval pipeline</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#1-rag-architecture--visual-mental-model">Section 1</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#6-build-a-sparse-tf-idf-index">Section 6</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#7-sparse-search--show-every-important-internal-step">Section 7</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#11-build-a-dense-embedding-index">Section 11</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>Why vector search alone is insufficient</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#13-why-dense-search-alone-is-not-enough">Section 13</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>Why keyword search alone is insufficient</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#8-where-sparse-search-can-fail--vocabulary-mismatch">Section 8</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>Sparse + dense retrieval</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#3-sparse-retrieval-from-first-principles">Section 3</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#9-dense-retrieval-from-first-principles">Section 9</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#15-hybrid-search--combine-the-signals">Section 15</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>Hybrid Search architecture</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#2-why-hybrid-search-exists">Section 2</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#15-hybrid-search--combine-the-signals">Section 15</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#17-weighted-fusion">Section 17</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#19-fusion-vs-reranking--do-not-confuse-them">Section 19</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>Real-world examples</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#71-experiment--exact-legal-reference">Section 7.1</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#72-experiment--exact-error-code">Section 7.2</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#73-experiment--exact-product-code">Section 7.3</a> · <a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#27-regulatory-example--why-hybrid-is-a-natural-fit">Section 27</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>When Hybrid Search should be used</td><td align="center"><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#26-when-should-you-use-hybrid-search">Section 26</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#0-the-big-picture-before-any-code"><b>0. The Big Picture Before Any Code</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">3</td></tr>
<tr><td align="center">02</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#1-rag-architecture--visual-mental-model"><b>1. RAG Architecture | Visual Mental Model</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">4</td></tr>
<tr><td align="center">03</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#2-why-hybrid-search-exists"><b>2. Why Hybrid Search Exists</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#3-sparse-retrieval-from-first-principles"><b>3. Sparse Retrieval From First Principles</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">05</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#4-create-our-tiny-enterprise-corpus"><b>4. Create Our Tiny Enterprise Corpus</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">06</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#5-tokenization--the-first-hidden-step-in-keyword-search"><b>5. Tokenization | The First Hidden Step in Keyword Search</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">07</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#6-build-a-sparse-tf-idf-index"><b>6. Build a Sparse TF-IDF Index</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">-</td></tr>
<tr><td align="center">08</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#7-sparse-search--show-every-important-internal-step"><b>7. Sparse Search — Show Every Important Internal Step</b></a></td><td align="center">3</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">09</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#8-where-sparse-search-can-fail--vocabulary-mismatch"><b>8. Where Sparse Search Can Fail — Vocabulary Mismatch</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">10</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#9-dense-retrieval-from-first-principles"><b>9. Dense Retrieval From First Principles</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#10-cosine-similarity--explained-before-we-use-it"><b>10. Cosine Similarity — Explained Before We Use It</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">12</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#11-build-a-dense-embedding-index"><b>11. Build a Dense Embedding Index</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">13</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#12-visualize-embedding-space-in-2d"><b>12. Visualize Embedding Space in 2D</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">14</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#13-why-dense-search-alone-is-not-enough"><b>13. Why Dense Search Alone Is Not Enough</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">15</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#14-query-types--a-very-useful-mental-model"><b>14. Query Types — A Very Useful Mental Model</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">16</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#15-hybrid-search--combine-the-signals"><b>15. Hybrid Search = Combine the Signals</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">17</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#16-score-normalization--explain-it-before-using-it"><b>16. Score Normalization — Explain It Before Using It</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">18</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#17-weighted-fusion"><b>17. Weighted Fusion</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">19</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#18-alpha-experiment--see-how-ranking-changes"><b>18. Alpha Experiment — See How Ranking Changes</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">20</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#19-fusion-vs-reranking--do-not-confuse-them"><b>19. Fusion vs Reranking — Do Not Confuse Them</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">3</td></tr>
<tr><td align="center">21</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#20-high-recall-first-high-precision-later"><b>20. High Recall First, High Precision Later</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">22</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#21-why-retrieval-quality-can-limit-the-entire-rag-system"><b>21. Why Retrieval Quality Can Limit the Entire RAG System</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">23</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#22-search-vs-rag--another-important-distinction"><b>22. Search vs RAG — Another Important Distinction</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">24</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#23-hybrid-search-does-not-fix-everything"><b>23. Hybrid Search Does NOT Fix Everything</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">25</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#24-production-debugging-framework"><b>24. Production Debugging Framework</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">26</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#25-a-simple-end-to-end-hybrid-rag-pseudocode"><b>25. A Simple End-to-End Hybrid RAG Pseudocode</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">27</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#26-when-should-you-use-hybrid-search"><b>26. When Should You Use Hybrid Search?</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">28</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#27-regulatory-example--why-hybrid-is-a-natural-fit"><b>27. Regulatory Example — Why Hybrid Is a Natural Fit</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">29</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#28-common-beginner-misconceptions"><b>28. Common Beginner Misconceptions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">30</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#29-interview-questions--with-strong-answers"><b>29. Interview Questions — With Strong Answers</b></a></td><td align="center">7</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">31</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#30-interview-scenarios"><b>30. Interview Scenarios</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">32</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#31-final-concept-map"><b>31. Final Concept Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">33</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#32-chapter-1-revision-cheat-sheet"><b>32. Chapter 1 Revision Cheat Sheet</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">34</td><td><a href="notes/1a.%20What%20is%20Hybrid%20Search%20RAG.md#33-practice-tasks--do-these-before-chapter-2"><b>33. Practice Tasks — Do These Before Chapter 2</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
</tbody>
</table>
