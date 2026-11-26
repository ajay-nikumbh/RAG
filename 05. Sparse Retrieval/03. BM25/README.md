<div align="center">

# 05.03 · BM25

<img src="https://img.shields.io/badge/05%20%C2%B7%20Sparse%20Retrieval-6366F1?style=for-the-badge" alt="group"/> <img src="https://img.shields.io/badge/Status-Done-10B981?style=for-the-badge" alt="status"/>

**BM25 formula, BM25 IDF, TF saturation (k1), length normalization (b), BM25 vs TF-IDF.**

</div>

<p align="center"><a href="../02.%20TF-IDF/README.md">Previous: 05.02 TF-IDF</a> | <a href="../../README.md">Home</a> | <a href="../README.md">Group 05: Sparse Retrieval</a> | <a href="notes/03.%20BM25.md">Notes</a> | <a href="../04.%20BM25%20Implementation%20in%20Practice/README.md">Next: 05.04 BM25 Implementation in Practice</a></p>


## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/03.%20BM25.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Jupyter notebook</b></td><td>Original notebook with full code and outputs</td><td align="center"><a href="notebooks/03.%20BM25.ipynb">Open</a></td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Result charts from the notebook (2 used in the notes)</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Chapter datasets (the notebook builds its corpus inline)</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks (last section of the notes)</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Syllabus coverage

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="50%">Syllabus subtopic</th><th width="30%">Covered in</th><th width="12%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td>What is BM25?</td><td align="center"><a href="notes/03.%20BM25.md#3-bm25-intuition">Section 3</a> · <a href="notes/03.%20BM25.md#4-the-bm25-formula">Section 4</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>Why BM25 replaced TF-IDF</td><td align="center"><a href="notes/03.%20BM25.md#2-why-do-we-need-bm25">Section 2</a> · <a href="notes/03.%20BM25.md#17-bm25-vs-tf-idf">Section 17</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>BM25 formula</td><td align="center"><a href="notes/03.%20BM25.md#4-the-bm25-formula">Section 4</a> · <a href="notes/03.%20BM25.md#28-one-page-revision-map">Section 28</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>Term frequency saturation</td><td align="center"><a href="notes/03.%20BM25.md#7-term-frequency-saturation">Section 7</a> · <a href="notes/03.%20BM25.md#14-experiment--tf-saturation-with-real-documents">Section 14</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>Document length normalization</td><td align="center"><a href="notes/03.%20BM25.md#9-document-length-normalization">Section 9</a> · <a href="notes/03.%20BM25.md#15-experiment--short-vs-long-documents">Section 15</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>k1</td><td align="center"><a href="notes/03.%20BM25.md#8-the-k1-parameter">Section 8</a> · <a href="notes/03.%20BM25.md#19-tune-k1">Section 19</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>b</td><td align="center"><a href="notes/03.%20BM25.md#10-the-b-parameter">Section 10</a> · <a href="notes/03.%20BM25.md#16-experiment--what-happens-when-b--0">Section 16</a> · <a href="notes/03.%20BM25.md#20-tune-b">Section 20</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>IDF</td><td align="center"><a href="notes/03.%20BM25.md#6-document-frequency-and-bm25-idf">Section 6</a></td><td align="center">Done</td></tr>
<tr><td align="center">09</td><td>BM25 scoring walkthrough</td><td align="center"><a href="notes/03.%20BM25.md#11-manual-bm25-calculation">Section 11</a> · <a href="notes/03.%20BM25.md#12-multi-term-query">Section 12</a> · <a href="notes/03.%20BM25.md#13-bm25-from-scratch">Section 13</a></td><td align="center">Done</td></tr>
<tr><td align="center">10</td><td>BM25 vs TF-IDF</td><td align="center"><a href="notes/03.%20BM25.md#17-bm25-vs-tf-idf">Section 17</a> · <a href="notes/03.%20BM25.md#18-compare-rankings-on-the-same-corpus">Section 18</a></td><td align="center">Done</td></tr>
<tr><td align="center">11</td><td>BM25 limitations</td><td align="center"><a href="notes/03.%20BM25.md#22-bm25-limitation--vocabulary-mismatch">Section 22</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/03.%20BM25.md#1-simple-corpus"><b>1. Simple Corpus</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">02</td><td><a href="notes/03.%20BM25.md#2-why-do-we-need-bm25"><b>2. Why Do We Need BM25?</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/03.%20BM25.md#3-bm25-intuition"><b>3. BM25 Intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/03.%20BM25.md#4-the-bm25-formula"><b>4. The BM25 Formula</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">05</td><td><a href="notes/03.%20BM25.md#5-corpus-statistics"><b>5. Corpus Statistics</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">06</td><td><a href="notes/03.%20BM25.md#6-document-frequency-and-bm25-idf"><b>6. Document Frequency and BM25 IDF</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">07</td><td><a href="notes/03.%20BM25.md#checkpoint-1"><b>CHECKPOINT 1</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">08</td><td><a href="notes/03.%20BM25.md#7-term-frequency-saturation"><b>7. Term-Frequency Saturation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">09</td><td><a href="notes/03.%20BM25.md#8-the-k1-parameter"><b>8. The k1 Parameter</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">10</td><td><a href="notes/03.%20BM25.md#9-document-length-normalization"><b>9. Document-Length Normalization</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">11</td><td><a href="notes/03.%20BM25.md#10-the-b-parameter"><b>10. The b Parameter</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">12</td><td><a href="notes/03.%20BM25.md#checkpoint-2"><b>CHECKPOINT 2</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">13</td><td><a href="notes/03.%20BM25.md#11-manual-bm25-calculation"><b>11. Manual BM25 Calculation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">14</td><td><a href="notes/03.%20BM25.md#12-multi-term-query"><b>12. Multi-Term Query</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">15</td><td><a href="notes/03.%20BM25.md#13-bm25-from-scratch"><b>13. BM25 From Scratch</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">16</td><td><a href="notes/03.%20BM25.md#14-experiment--tf-saturation-with-real-documents"><b>14. Experiment — TF Saturation With Real Documents</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">17</td><td><a href="notes/03.%20BM25.md#15-experiment--short-vs-long-documents"><b>15. Experiment — Short vs Long Documents</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">18</td><td><a href="notes/03.%20BM25.md#16-experiment--what-happens-when-b--0"><b>16. Experiment — What Happens When b = 0?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">19</td><td><a href="notes/03.%20BM25.md#checkpoint-3"><b>CHECKPOINT 3</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">20</td><td><a href="notes/03.%20BM25.md#17-bm25-vs-tf-idf"><b>17. BM25 vs TF-IDF</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">21</td><td><a href="notes/03.%20BM25.md#18-compare-rankings-on-the-same-corpus"><b>18. Compare Rankings on the Same Corpus</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">22</td><td><a href="notes/03.%20BM25.md#19-tune-k1"><b>19. Tune k1</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">23</td><td><a href="notes/03.%20BM25.md#20-tune-b"><b>20. Tune b</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">24</td><td><a href="notes/03.%20BM25.md#21-optional-rank_bm25-library"><b>21. Optional: rank_bm25 Library</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">-</td></tr>
<tr><td align="center">25</td><td><a href="notes/03.%20BM25.md#22-bm25-limitation--vocabulary-mismatch"><b>22. BM25 Limitation — Vocabulary Mismatch</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">26</td><td><a href="notes/03.%20BM25.md#23-bm25-strength--exact-terms"><b>23. BM25 Strength — Exact Terms</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">27</td><td><a href="notes/03.%20BM25.md#24-why-bm25-is-excellent-for-hybrid-search"><b>24. Why BM25 Is Excellent for Hybrid Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">28</td><td><a href="notes/03.%20BM25.md#checkpoint-4"><b>CHECKPOINT 4</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">29</td><td><a href="notes/03.%20BM25.md#25-bm25-debugging-framework"><b>25. BM25 Debugging Framework</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">30</td><td><a href="notes/03.%20BM25.md#end-to-end-example--bm25-search-from-scratch-and-with-rank_bm25"><b>End-to-End Example — BM25 Search From Scratch and With rank_bm25</b></a></td><td align="center">12</td><td align="center">11</td><td align="center">2</td></tr>
<tr><td align="center">31</td><td><a href="notes/03.%20BM25.md#26-interview-questions"><b>26. Interview Questions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">32</td><td><a href="notes/03.%20BM25.md#27-interview-scenarios"><b>27. Interview Scenarios</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">33</td><td><a href="notes/03.%20BM25.md#28-one-page-revision-map"><b>28. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">34</td><td><a href="notes/03.%20BM25.md#29-practice-tasks"><b>29. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">35</td><td><a href="notes/03.%20BM25.md#30-final-takeaways"><b>30. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">36</td><td><a href="notes/03.%20BM25.md#next-chapter--chapter-6-dense-retrieval"><b>Next Chapter — Chapter 6: Dense Retrieval</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
</tbody>
</table>
