<div align="center">

# 05.01 · Inverted Index Fundamentals

<img src="https://img.shields.io/badge/05%20%C2%B7%20Sparse%20Retrieval-6366F1?style=for-the-badge" alt="group"/> <img src="https://img.shields.io/badge/Status-Done-10B981?style=for-the-badge" alt="status"/>

**Regulation PDFs, parsing, chunking, metadata filters, BM25 + dense, RRF, LLM reranker.; Lexical vs semantic, inverted indexes, TF-IDF, BM25 from first principles, learned sparse retrieval.**

</div>

<p align="center"><a href="../../04.%20Chunking%20and%20Metadata/04.%20Field-Aware%20Search/README.md">Previous: 04.04 Field-Aware Search</a> | <a href="../../README.md">Home</a> | <a href="../README.md">Group 05: Sparse Retrieval</a> | <a href="notes/01.%20Inverted%20Index%20Fundamentals.md">Notes</a> | <a href="../02.%20TF-IDF/README.md">Next: 05.02 TF-IDF</a></p>


## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Jupyter notebook</b></td><td>Original notebook with full code and outputs</td><td align="center"><a href="notebooks/01.%20Inverted%20Index%20Fundamentals.ipynb">Open</a></td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Result charts from the notebook (1 used in the notes)</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Chapter datasets (the notebook builds its corpus inline)</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks (last section of the notes)</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Syllabus coverage

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="50%">Syllabus subtopic</th><th width="30%">Covered in</th><th width="12%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td>Forward index</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#4-forward-index">Section 4</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>Inverted index</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#5-inverted-index">Section 5</a> · <a href="notes/01.%20Inverted%20Index%20Fundamentals.md#7-indexed-search">Section 7</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>Posting lists</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#6-vocabulary-and-posting-lists">Section 6</a> · <a href="notes/01.%20Inverted%20Index%20Fundamentals.md#10-rich-posting-lists">Section 10</a> · <a href="notes/01.%20Inverted%20Index%20Fundamentals.md#23-sorted-posting-lists">Section 23</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>Term frequency</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#9-term-frequency-tf">Section 9</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>Document frequency</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#8-document-frequency-df">Section 8</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>Tokenization</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#16-tokenization-and-normalization">Section 16</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>Stopwords</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#17-stopwords">Section 17</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>Stemming</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#18-stemming--simple-intuition">Section 18</a></td><td align="center">Done</td></tr>
<tr><td align="center">09</td><td>Lemmatization</td><td align="center"><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#19-lemmatization--intuition-only">Section 19</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#2-why-do-we-need-an-index"><b>2. Why Do We Need an Index?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">02</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#3-naive-search"><b>3. Naive Search</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#4-forward-index"><b>4. Forward Index</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#5-inverted-index"><b>5. Inverted Index</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">05</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#6-vocabulary-and-posting-lists"><b>6. Vocabulary and Posting Lists</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">06</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#7-indexed-search"><b>7. Indexed Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">07</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#checkpoint-1"><b>CHECKPOINT 1</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">08</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#8-document-frequency-df"><b>8. Document Frequency (DF)</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">09</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#9-term-frequency-tf"><b>9. Term Frequency (TF)</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">10</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#10-rich-posting-lists"><b>10. Rich Posting Lists</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#11-boolean-search"><b>11. Boolean Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">12</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#12-multi-term-and-search"><b>12. Multi-Term AND Search</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">13</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#checkpoint-2"><b>CHECKPOINT 2</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">14</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#13-positional-index"><b>13. Positional Index</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">15</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#14-exact-phrase-search"><b>14. Exact Phrase Search</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">16</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#15-general-phrase-search"><b>15. General Phrase Search</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">17</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#16-tokenization-and-normalization"><b>16. Tokenization and Normalization</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">18</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#17-stopwords"><b>17. Stopwords</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">19</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#18-stemming--simple-intuition"><b>18. Stemming — Simple Intuition</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">20</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#19-lemmatization--intuition-only"><b>19. Lemmatization — Intuition Only</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">21</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#checkpoint-3"><b>CHECKPOINT 3</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">22</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#20-full-indexing-pipeline"><b>20. Full Indexing Pipeline</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">23</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#21-query-time-pipeline"><b>21. Query-Time Pipeline</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">24</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#22-index-time-vs-query-time"><b>22. Index Time vs Query Time</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">3</td></tr>
<tr><td align="center">25</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#23-sorted-posting-lists"><b>23. Sorted Posting Lists</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">26</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#24-candidate-retrieval-vs-ranking"><b>24. Candidate Retrieval vs Ranking</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">27</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#25-why-this-matters-for-bm25"><b>25. Why This Matters for BM25</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">28</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#26-inverted-index-vs-vector-index"><b>26. Inverted Index vs Vector Index</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">29</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#27-common-misconceptions"><b>27. Common Misconceptions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">30</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#28-debugging-an-inverted-index"><b>28. Debugging an Inverted Index</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">31</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#checkpoint-4"><b>CHECKPOINT 4</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">32</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#29-interview-questions"><b>29. Interview Questions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">33</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#30-interview-scenarios"><b>30. Interview Scenarios</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">34</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#31-one-page-revision-map"><b>31. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">35</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#32-practice-tasks"><b>32. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">36</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#33-final-takeaways"><b>33. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">37</td><td><a href="notes/01.%20Inverted%20Index%20Fundamentals.md#next-chapter--chapter-4-tf-idf"><b>Next Chapter — Chapter 4: TF-IDF</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
</tbody>
</table>
