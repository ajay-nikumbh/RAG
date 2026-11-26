<div align="center">

# 9e · BM25 Implementation in Practice

<img src="https://img.shields.io/badge/Part%20II%20%C2%B7%20Storage%20and%20Search-6366F1?style=for-the-badge" alt="part"/> <img src="https://img.shields.io/badge/Diagrams-57-FF3670?style=for-the-badge" alt="diagrams"/> <img src="https://img.shields.io/badge/Code%20examples-16-0EA5E9?style=for-the-badge" alt="code"/>

**Turn the BM25 formula into a reusable, testable, debuggable retriever.**

</div>

<p align="center"><a href="../9d.%20BM25/README.md">Previous: 9d BM25</a> | <a href="../../README.md">Home</a> | <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md">Notes</a> | <a href="../README.md">Chapter 09: Sparse Retrieval and Keyword Search</a> | <a href="../9f.%20Sparse%20Neural%20Retrieval/README.md">Next: 9f Sparse Neural Retrieval</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Jupyter notebook</b></td><td>Original notebook with full code and outputs</td><td align="center"><a href="notebooks/9e.%20BM25%20Implementation%20in%20Practice.ipynb">Open</a></td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Result charts from the notebook (0 used in the notes)</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Chapter datasets (the notebook builds its corpus inline)</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks (last section of the notes)</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Syllabus coverage

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="50%">Syllabus subtopic</th><th width="30%">Covered in</th><th width="12%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td>BM25 pipeline: documents, tokenization, index, query, scores, Top-K</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#2-core-mental-model">Section 2</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#6-index-time-corpus-preparation">Section 6</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#8-query-time-search">Section 8</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>Manual (from scratch) BM25 implementation</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#6-index-time-corpus-preparation">Section 6</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#7-reusable-bm25-retriever">Section 7</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#9-explaining-bm25-scores">Section 9</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>Implement BM25 with rank_bm25</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#12-rank_bm25-in-practice">Section 12</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>Batch search and corpus updates</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#10-batch-search">Section 10</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#11-corpus-updates-and-reindexing">Section 11</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>Scores, Top-K and thresholds</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#13-scores-top-k-and-thresholds">Section 13</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>Benchmarking and scaling with an inverted index</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#14-benchmarking">Section 14</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#15-scaling-with-an-inverted-index">Section 15</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>Edge cases, metadata filtering and API shape</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#16-edge-cases">Section 16</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#17-metadata-filtering">Section 17</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#18-api-response-shape">Section 18</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>Regression tests and debugging</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#19-regression-tests">Section 19</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#20-debugging-bm25">Section 20</a></td><td align="center">Done</td></tr>
<tr><td align="center">09</td><td>BM25 inside Hybrid Search</td><td align="center"><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#21-production-architecture">Section 21</a> · <a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#22-bm25-inside-hybrid-search">Section 22</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#1-where-chapter-6-fits"><b>1. Where Chapter 6 Fits</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">02</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#2-core-mental-model"><b>2. Core Mental Model</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#3-bm25-recap"><b>3. BM25 Recap</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#4-practical-corpus-design"><b>4. Practical Corpus Design</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">05</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#5-consistent-tokenization"><b>5. Consistent Tokenization</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">06</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#6-index-time-corpus-preparation"><b>6. Index-Time Corpus Preparation</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">4</td></tr>
<tr><td align="center">07</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#7-reusable-bm25-retriever"><b>7. Reusable BM25 Retriever</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">2</td></tr>
<tr><td align="center">08</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#8-query-time-search"><b>8. Query-Time Search</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">09</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#9-explaining-bm25-scores"><b>9. Explaining BM25 Scores</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">10</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#10-batch-search"><b>10. Batch Search</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">11</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#11-corpus-updates-and-reindexing"><b>11. Corpus Updates and Reindexing</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">4</td></tr>
<tr><td align="center">12</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#12-rank_bm25-in-practice"><b>12. rank_bm25 in Practice</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">13</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#13-scores-top-k-and-thresholds"><b>13. Scores, Top-K, and Thresholds</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">14</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#14-benchmarking"><b>14. Benchmarking</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">3</td></tr>
<tr><td align="center">15</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#15-scaling-with-an-inverted-index"><b>15. Scaling With an Inverted Index</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">16</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#16-edge-cases"><b>16. Edge Cases</b></a></td><td align="center">4</td><td align="center">-</td><td align="center">4</td></tr>
<tr><td align="center">17</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#17-metadata-filtering"><b>17. Metadata Filtering</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">18</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#18-api-response-shape"><b>18. API Response Shape</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">19</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#19-regression-tests"><b>19. Regression Tests</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">20</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#20-debugging-bm25"><b>20. Debugging BM25</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">21</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#21-production-architecture"><b>21. Production Architecture</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">22</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#22-bm25-inside-hybrid-search"><b>22. BM25 Inside Hybrid Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">23</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#23-checkpoints-with-answers"><b>23. Checkpoints With Answers</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">24</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#24-interview-questions"><b>24. Interview Questions</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">25</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#25-interview-scenarios"><b>25. Interview Scenarios</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">26</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#26-one-page-revision-map"><b>26. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">27</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#27-practice-tasks"><b>27. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">28</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#28-final-takeaways"><b>28. Final Takeaways</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">29</td><td><a href="notes/9e.%20BM25%20Implementation%20in%20Practice.md#next-chapter--chapter-7-dense-vector-retrieval"><b>Next Chapter — Chapter 7: Dense Vector Retrieval</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
