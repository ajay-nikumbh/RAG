<div align="center">

# 10a · Dense Vector Retrieval

<img src="https://img.shields.io/badge/Part%20II%20%C2%B7%20Storage%20and%20Search-6366F1?style=for-the-badge" alt="part"/> <img src="https://img.shields.io/badge/Diagrams-46-FF3670?style=for-the-badge" alt="diagrams"/> <img src="https://img.shields.io/badge/Code%20examples-9-0EA5E9?style=for-the-badge" alt="code"/>

**Embed text as vectors and rank by meaning, not by shared words.**

</div>

<p align="center"><a href="../README.md">Previous: 10 Dense Retrieval</a> | <a href="../../README.md">Home</a> | <a href="notes/10a.%20Dense%20Vector%20Retrieval.md">Notes</a> | <a href="../README.md">Chapter 10: Dense Retrieval</a> | <a href="../../11.%20Hybrid%20Search/README.md">Next: 11 Hybrid Search</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Jupyter notebook</b></td><td>Not added yet. Results in the notes come from a local run of all-MiniLM-L6-v2.</td><td align="center">-</td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Result charts from the notebook (0 used in the notes)</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Chapter datasets (the notebook builds its corpus inline)</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks (last section of the notes)</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Syllabus coverage

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="50%">Syllabus subtopic</th><th width="30%">Covered in</th><th width="12%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td>Embeddings</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#3-from-text-to-embeddings">Section 3</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#4-what-is-a-dense-vector">Section 4</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>Query embeddings and document embeddings</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#6-query-and-document-embeddings">Section 6</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#7-bi-encoder-architecture">Section 7</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>Semantic similarity</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#5-semantic-similarity">Section 5</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#8-embedding-space-intuition">Section 8</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#16-semantic-neighborhoods">Section 16</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>Cosine similarity</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#9-cosine-similarity">Section 9</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#12-which-similarity-metric-should-you-use">Section 12</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>Dot product</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#10-dot-product">Section 10</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#15-why-normalization-matters">Section 15</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>Euclidean distance</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#11-euclidean-distance">Section 11</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>Top-K search</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#13-end-to-end-dense-retrieval">Section 13</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#14-dense-retrieval-with-sentence-transformers">Section 14</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>Strengths and weaknesses of dense retrieval</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#17-dense-retrieval-strengths">Section 17</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#18-vocabulary-mismatch">Section 18</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#19-dense-retrieval-weaknesses">Section 19</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#20-exact-ids-versions-and-numbers">Section 20</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#21-negation-and-near-duplicate-meaning">Section 21</a></td><td align="center">Done</td></tr>
<tr><td align="center">09</td><td>Dense retrieval in Hybrid Search</td><td align="center"><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#31-dense-retrieval-vs-bm25">Section 31</a> · <a href="notes/10a.%20Dense%20Vector%20Retrieval.md#32-how-dense-retrieval-becomes-the-semantic-branch-of-hybrid-search">Section 32</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#1-where-dense-retrieval-fits"><b>1. Where Dense Retrieval Fits</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">02</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#2-why-dense-retrieval-exists"><b>2. Why Dense Retrieval Exists</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#3-from-text-to-embeddings"><b>3. From Text to Embeddings</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#4-what-is-a-dense-vector"><b>4. What Is a Dense Vector?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">05</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#5-semantic-similarity"><b>5. Semantic Similarity</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">06</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#6-query-and-document-embeddings"><b>6. Query and Document Embeddings</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">07</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#7-bi-encoder-architecture"><b>7. Bi-Encoder Architecture</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">08</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#8-embedding-space-intuition"><b>8. Embedding Space Intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">09</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#9-cosine-similarity"><b>9. Cosine Similarity</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">10</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#10-dot-product"><b>10. Dot Product</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#11-euclidean-distance"><b>11. Euclidean Distance</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">12</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#12-which-similarity-metric-should-you-use"><b>12. Which Similarity Metric Should You Use?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">13</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#13-end-to-end-dense-retrieval"><b>13. End-to-End Dense Retrieval</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">14</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#14-dense-retrieval-with-sentence-transformers"><b>14. Dense Retrieval With Sentence Transformers</b></a></td><td align="center">-</td><td align="center">3</td><td align="center">1</td></tr>
<tr><td align="center">15</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#15-why-normalization-matters"><b>15. Why Normalization Matters</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">1</td></tr>
<tr><td align="center">16</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#16-semantic-neighborhoods"><b>16. Semantic Neighborhoods</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">17</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#17-dense-retrieval-strengths"><b>17. Dense Retrieval Strengths</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">18</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#18-vocabulary-mismatch"><b>18. Vocabulary Mismatch</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">19</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#19-dense-retrieval-weaknesses"><b>19. Dense Retrieval Weaknesses</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">20</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#20-exact-ids-versions-and-numbers"><b>20. Exact IDs, Versions, and Numbers</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">21</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#21-negation-and-near-duplicate-meaning"><b>21. Negation and Near-Duplicate Meaning</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">22</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#22-domain-vocabulary"><b>22. Domain Vocabulary</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">23</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#23-chunking-and-dense-retrieval"><b>23. Chunking and Dense Retrieval</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">3</td></tr>
<tr><td align="center">24</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#24-embedding-model-selection"><b>24. Embedding Model Selection</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">25</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#25-index-time-vs-query-time"><b>25. Index-Time vs Query-Time</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">26</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#26-dense-retrieval-api-design"><b>26. Dense Retrieval API Design</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">27</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#27-caching"><b>27. Caching</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">28</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#28-batching"><b>28. Batching</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">1</td></tr>
<tr><td align="center">29</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#29-latency"><b>29. Latency</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">30</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#30-debugging-dense-retrieval"><b>30. Debugging Dense Retrieval</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">31</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#31-dense-retrieval-vs-bm25"><b>31. Dense Retrieval vs BM25</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">32</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#32-how-dense-retrieval-becomes-the-semantic-branch-of-hybrid-search"><b>32. How Dense Retrieval Becomes the Semantic Branch of Hybrid Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">33</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#33-checkpoints-with-answers"><b>33. Checkpoints With Answers</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">34</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#34-interview-questions"><b>34. Interview Questions</b></a></td><td align="center">10</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">35</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#35-interview-scenarios"><b>35. Interview Scenarios</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">36</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#36-one-page-revision-map"><b>36. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">37</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#37-practice-tasks"><b>37. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">38</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#38-final-takeaways"><b>38. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">39</td><td><a href="notes/10a.%20Dense%20Vector%20Retrieval.md#next-chapter--chapter-8-similarity-metrics-for-dense-search"><b>Next Chapter — Chapter 8: Similarity Metrics for Dense Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
