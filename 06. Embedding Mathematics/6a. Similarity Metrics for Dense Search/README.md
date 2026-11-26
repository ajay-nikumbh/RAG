<div align="center">

# 6a · Similarity Metrics for Dense Search

<img src="https://img.shields.io/badge/Part%20I%20%C2%B7%20Foundations-6366F1?style=for-the-badge" alt="part"/> <img src="https://img.shields.io/badge/Diagrams-42-FF3670?style=for-the-badge" alt="diagrams"/> <img src="https://img.shields.io/badge/Code%20examples-17-0EA5E9?style=for-the-badge" alt="code"/>

**Cosine, dot product and Euclidean distance: how dense search decides what is close.**

</div>

<p align="center"><a href="../README.md">Previous: 06 Embedding Mathematics</a> | <a href="../../README.md">Home</a> | <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md">Notes</a> | <a href="../README.md">Chapter 06: Embedding Mathematics</a> | <a href="../../07.%20Vector%20Databases/README.md">Next: 07 Vector Databases</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md">Open</a></td></tr>
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
<tr><td align="center">01</td><td>Vectors, magnitude and direction</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#3-vector-refresher">Section 3</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#4-magnitude-and-direction">Section 4</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>Cosine similarity</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#5-cosine-similarity">Section 5</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#6-cosine-similarity-from-scratch">Section 6</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>Dot product</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#7-dot-product">Section 7</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#8-dot-product-from-scratch">Section 8</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>Euclidean distance</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#9-euclidean-distance">Section 9</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#10-euclidean-distance-from-scratch">Section 10</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>Similarity vs distance and sort direction</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#11-similarity-vs-distance">Section 11</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#20-top-k-search">Section 20</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>Normalization and its effect on ranking</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#12-vector-normalization">Section 12</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#13-why-normalization-changes-rankings">Section 13</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#16-when-metrics-become-equivalent">Section 16</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>Comparing metrics</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#14-cosine-vs-dot-product">Section 14</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#15-cosine-vs-euclidean-distance">Section 15</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#17-ranking-example-with-three-documents">Section 17</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>Metric choice in models and vector databases</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#18-metric-choice-in-real-embedding-models">Section 18</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#19-metric-choice-in-vector-databases">Section 19</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#26-metric-mismatch-failure">Section 26</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#27-normalization-mismatch-failure">Section 27</a></td><td align="center">Done</td></tr>
<tr><td align="center">09</td><td>Scores, thresholds and numerical issues</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#21-score-interpretation">Section 21</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#22-thresholds">Section 22</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#23-numerical-stability">Section 23</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#24-zero-vectors">Section 24</a></td><td align="center">Done</td></tr>
<tr><td align="center">10</td><td>Similarity metrics in ANN and Hybrid Search</td><td align="center"><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#28-similarity-metrics-and-ann">Section 28</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#30-bm25-scores-vs-dense-similarity-scores">Section 30</a> · <a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#31-similarity-metrics-inside-hybrid-search">Section 31</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#basic-definitions-in-simple-words"><b>Basic Definitions in Simple Words</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">02</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#1-where-similarity-metrics-fit"><b>1. Where Similarity Metrics Fit</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">03</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#2-why-we-need-a-similarity-function"><b>2. Why We Need a Similarity Function</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#3-vector-refresher"><b>3. Vector Refresher</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">05</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#4-magnitude-and-direction"><b>4. Magnitude and Direction</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">06</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#5-cosine-similarity"><b>5. Cosine Similarity</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">07</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#6-cosine-similarity-from-scratch"><b>6. Cosine Similarity From Scratch</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">08</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#7-dot-product"><b>7. Dot Product</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">09</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#8-dot-product-from-scratch"><b>8. Dot Product From Scratch</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">-</td></tr>
<tr><td align="center">10</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#9-euclidean-distance"><b>9. Euclidean Distance</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#10-euclidean-distance-from-scratch"><b>10. Euclidean Distance From Scratch</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">12</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#11-similarity-vs-distance"><b>11. Similarity vs Distance</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">13</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#12-vector-normalization"><b>12. Vector Normalization</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">14</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#13-why-normalization-changes-rankings"><b>13. Why Normalization Changes Rankings</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">15</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#14-cosine-vs-dot-product"><b>14. Cosine vs Dot Product</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">16</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#15-cosine-vs-euclidean-distance"><b>15. Cosine vs Euclidean Distance</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">17</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#16-when-metrics-become-equivalent"><b>16. When Metrics Become Equivalent</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">18</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#17-ranking-example-with-three-documents"><b>17. Ranking Example With Three Documents</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">19</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#18-metric-choice-in-real-embedding-models"><b>18. Metric Choice in Real Embedding Models</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">20</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#19-metric-choice-in-vector-databases"><b>19. Metric Choice in Vector Databases</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">21</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#20-top-k-search"><b>20. Top-K Search</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">1</td></tr>
<tr><td align="center">22</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#21-score-interpretation"><b>21. Score Interpretation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">23</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#22-thresholds"><b>22. Thresholds</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">24</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#23-numerical-stability"><b>23. Numerical Stability</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">25</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#24-zero-vectors"><b>24. Zero Vectors</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">26</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#25-high-dimensional-intuition"><b>25. High-Dimensional Intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">27</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#26-metric-mismatch-failure"><b>26. Metric Mismatch Failure</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">28</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#27-normalization-mismatch-failure"><b>27. Normalization Mismatch Failure</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">29</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#28-similarity-metrics-and-ann"><b>28. Similarity Metrics and ANN</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">30</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#29-dense-retrieval-debugging"><b>29. Dense Retrieval Debugging</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">31</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#30-bm25-scores-vs-dense-similarity-scores"><b>30. BM25 Scores vs Dense Similarity Scores</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">32</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#31-similarity-metrics-inside-hybrid-search"><b>31. Similarity Metrics Inside Hybrid Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">33</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#end-to-end-example--three-metrics-on-real-embeddings"><b>End-to-End Example — Three Metrics on Real Embeddings</b></a></td><td align="center">6</td><td align="center">5</td><td align="center">2</td></tr>
<tr><td align="center">34</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#32-checkpoints-with-answers"><b>32. Checkpoints With Answers</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">35</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#33-interview-questions"><b>33. Interview Questions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">36</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#34-interview-scenarios"><b>34. Interview Scenarios</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">37</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#35-one-page-revision-map"><b>35. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">38</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#36-practice-tasks"><b>36. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">39</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#37-final-takeaways"><b>37. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">40</td><td><a href="notes/6a.%20Similarity%20Metrics%20for%20Dense%20Search.md#next-chapter--chapter-9-approximate-nearest-neighbor-search"><b>Next Chapter — Chapter 9: Approximate Nearest Neighbor Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
