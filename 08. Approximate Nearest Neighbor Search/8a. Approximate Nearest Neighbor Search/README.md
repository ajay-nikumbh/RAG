<div align="center">

# 8a · Approximate Nearest Neighbor Search

<img src="https://img.shields.io/badge/Part%20II%20%C2%B7%20Storage%20and%20Search-6366F1?style=for-the-badge" alt="part"/> <img src="https://img.shields.io/badge/Diagrams-34-FF3670?style=for-the-badge" alt="diagrams"/> <img src="https://img.shields.io/badge/Code%20examples-11-0EA5E9?style=for-the-badge" alt="code"/>

**Search only the promising part of vector space: trade a little recall for a lot of speed.**

</div>

<p align="center"><a href="../README.md">Previous: 08 Approximate Nearest Neighbor Search</a> | <a href="../../README.md">Home</a> | <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md">Notes</a> | <a href="../README.md">Chapter 08: Approximate Nearest Neighbor Search</a> | <a href="../8b.%20HNSW%20Fundamentals/README.md">Next: 8b HNSW Fundamentals</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md">Open</a></td></tr>
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
<tr><td align="center">01</td><td>Exact nearest-neighbor search</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#4-exact-nearest-neighbor-search">Section 4</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#5-brute-force-search">Section 5</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#6-time-complexity-intuition">Section 6</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#24-simple-exact-search-in-python">Section 24</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>ANN</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#7-what-is-approximate-nearest-neighbor-search">Section 7</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#8-why-approximation-helps">Section 8</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#10-ann-search-pipeline">Section 10</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#12-candidate-generation">Section 12</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#25-simple-ann-simulation">Section 25</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>Flat search</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#13-flat-index">Section 13</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>HNSW</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#14-hnsw-overview">Section 14</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>IVF</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#15-ivf-overview">Section 15</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>PQ</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#16-product-quantization-overview">Section 16</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>Recall vs latency trade-off</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#9-recall-vs-latency">Section 9</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#18-recallk-for-ann">Section 18</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#22-search-parameters">Section 22</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#26-exact-vs-approximate-ranking-comparison">Section 26</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>Benchmarking, memory and build time</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#19-latency-measurement">Section 19</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#20-index-build-time">Section 20</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#21-memory-trade-offs">Section 21</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#27-benchmarking-ann">Section 27</a></td><td align="center">Done</td></tr>
<tr><td align="center">09</td><td>Failure modes and debugging</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#28-failure-modes">Section 28</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#29-debugging-ann">Section 29</a></td><td align="center">Done</td></tr>
<tr><td align="center">10</td><td>ANN in vector databases and Hybrid Search</td><td align="center"><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#30-ann-in-vector-databases">Section 30</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#31-ann-inside-dense-retrieval">Section 31</a> · <a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#32-ann-inside-hybrid-search">Section 32</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#1-where-ann-fits"><b>1. Where ANN Fits</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">02</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#2-definitions"><b>2. Definitions</b></a></td><td align="center">10</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#3-why-exact-vector-search-becomes-expensive"><b>3. Why Exact Vector Search Becomes Expensive</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#4-exact-nearest-neighbor-search"><b>4. Exact Nearest Neighbor Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">05</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#5-brute-force-search"><b>5. Brute-Force Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">06</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#6-time-complexity-intuition"><b>6. Time Complexity Intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">07</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#7-what-is-approximate-nearest-neighbor-search"><b>7. What Is Approximate Nearest Neighbor Search?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">08</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#8-why-approximation-helps"><b>8. Why Approximation Helps</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">09</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#9-recall-vs-latency"><b>9. Recall vs Latency</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">10</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#10-ann-search-pipeline"><b>10. ANN Search Pipeline</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#11-index-build-vs-query-search"><b>11. Index Build vs Query Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">12</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#12-candidate-generation"><b>12. Candidate Generation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">13</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#13-flat-index"><b>13. Flat Index</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">14</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#14-hnsw-overview"><b>14. HNSW Overview</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">15</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#15-ivf-overview"><b>15. IVF Overview</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">16</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#16-product-quantization-overview"><b>16. Product Quantization Overview</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">17</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#17-ann-families-compared"><b>17. ANN Families Compared</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">18</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#18-recallk-for-ann"><b>18. Recall@K for ANN</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">19</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#19-latency-measurement"><b>19. Latency Measurement</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">20</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#20-index-build-time"><b>20. Index Build Time</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">21</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#21-memory-trade-offs"><b>21. Memory Trade-offs</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">22</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#22-search-parameters"><b>22. Search Parameters</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">23</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#23-ann-and-similarity-metrics"><b>23. ANN and Similarity Metrics</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">24</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#24-simple-exact-search-in-python"><b>24. Simple Exact Search in Python</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">25</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#25-simple-ann-simulation"><b>25. Simple ANN Simulation</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">26</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#26-exact-vs-approximate-ranking-comparison"><b>26. Exact vs Approximate Ranking Comparison</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">27</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#27-benchmarking-ann"><b>27. Benchmarking ANN</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">28</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#28-failure-modes"><b>28. Failure Modes</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">29</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#29-debugging-ann"><b>29. Debugging ANN</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">30</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#30-ann-in-vector-databases"><b>30. ANN in Vector Databases</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">31</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#31-ann-inside-dense-retrieval"><b>31. ANN Inside Dense Retrieval</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">32</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#32-ann-inside-hybrid-search"><b>32. ANN Inside Hybrid Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">33</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#end-to-end-example--from-exact-search-to-a-tiny-ivf-index"><b>End-to-End Example — From Exact Search to a Tiny IVF Index</b></a></td><td align="center">7</td><td align="center">6</td><td align="center">3</td></tr>
<tr><td align="center">34</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#33-checkpoints-with-answers"><b>33. Checkpoints With Answers</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">35</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#34-interview-questions"><b>34. Interview Questions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">36</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#35-interview-scenarios"><b>35. Interview Scenarios</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">37</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#36-one-page-revision-map"><b>36. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">38</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#37-practice-tasks"><b>37. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">39</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#38-final-takeaways"><b>38. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">40</td><td><a href="notes/8a.%20Approximate%20Nearest%20Neighbor%20Search.md#next-chapter--chapter-10-hnsw-fundamentals"><b>Next Chapter — Chapter 10: HNSW Fundamentals</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
