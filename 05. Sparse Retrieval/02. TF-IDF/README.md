<div align="center">

# 05.02 · TF-IDF

<img src="https://img.shields.io/badge/05%20%C2%B7%20Sparse%20Retrieval-6366F1?style=for-the-badge" alt="group"/> <img src="https://img.shields.io/badge/Status-Done-10B981?style=for-the-badge" alt="status"/>

**TF variants, DF, IDF, TF-IDF formula, sparse matrix, cosine ranking, OOV and synonym limits.**

</div>

<p align="center"><a href="../01.%20Inverted%20Index%20Fundamentals/README.md">Previous: 05.01 Inverted Index Fundamentals</a> | <a href="../../README.md">Home</a> | <a href="../README.md">Group 05: Sparse Retrieval</a> | <a href="notes/02.%20TF-IDF.md">Notes</a> | <a href="../03.%20BM25/README.md">Next: 05.03 BM25</a></p>


## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="22%">Resource</th><th width="52%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Short interview-focused notes with diagrams and clean code</td><td align="center"><a href="notes/02.%20TF-IDF.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Jupyter notebook</b></td><td>Original notebook with full code and outputs</td><td align="center"><a href="notebooks/02.%20TF-IDF.ipynb">Open</a></td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Result charts from the notebook (0 used in the notes)</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Chapter datasets (the notebook builds its corpus inline)</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks (last section of the notes)</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Syllabus coverage

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="50%">Syllabus subtopic</th><th width="30%">Covered in</th><th width="12%">Status</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td>Term Frequency</td><td align="center"><a href="notes/02.%20TF-IDF.md#5-term-frequency-tf">Section 5</a> · <a href="notes/02.%20TF-IDF.md#6-visualize-tf">Section 6</a> · <a href="notes/02.%20TF-IDF.md#7-raw-tf-limitation--repetition-keeps-increasing-the-score">Section 7</a> · <a href="notes/02.%20TF-IDF.md#8-normalized-tf">Section 8</a> · <a href="notes/02.%20TF-IDF.md#9-log-scaled-tf">Section 9</a></td><td align="center">Done</td></tr>
<tr><td align="center">02</td><td>Document Frequency</td><td align="center"><a href="notes/02.%20TF-IDF.md#10-document-frequency-df">Section 10</a> · <a href="notes/02.%20TF-IDF.md#11-df-for-the-entire-vocabulary">Section 11</a></td><td align="center">Done</td></tr>
<tr><td align="center">03</td><td>Inverse Document Frequency</td><td align="center"><a href="notes/02.%20TF-IDF.md#12-inverse-document-frequency-idf">Section 12</a> · <a href="notes/02.%20TF-IDF.md#13-visual--idf-falls-as-df-increases">Section 13</a> · <a href="notes/02.%20TF-IDF.md#14-build-an-idf-table">Section 14</a> · <a href="notes/02.%20TF-IDF.md#15-common-word-vs-rare-word-example">Section 15</a></td><td align="center">Done</td></tr>
<tr><td align="center">04</td><td>TF-IDF formula</td><td align="center"><a href="notes/02.%20TF-IDF.md#16-tf-idf-formula">Section 16</a> · <a href="notes/02.%20TF-IDF.md#17-manual-tf-idf-calculation">Section 17</a> · <a href="notes/02.%20TF-IDF.md#18-compare-two-terms-in-the-same-document">Section 18</a></td><td align="center">Done</td></tr>
<tr><td align="center">05</td><td>Intuition</td><td align="center"><a href="notes/02.%20TF-IDF.md#3-visual-intuition--tf-and-idf-answer-different-questions">Section 3</a> · <a href="notes/02.%20TF-IDF.md#21-why-tf-idf-is-sparse">Section 21</a></td><td align="center">Done</td></tr>
<tr><td align="center">06</td><td>Advantages</td><td align="center"><a href="notes/02.%20TF-IDF.md#34-tf-idf-strengths-and-weaknesses">Section 34</a></td><td align="center">Done</td></tr>
<tr><td align="center">07</td><td>Limitations</td><td align="center"><a href="notes/02.%20TF-IDF.md#27-out-of-vocabulary-oov-query-terms">Section 27</a> · <a href="notes/02.%20TF-IDF.md#28-synonym-failure">Section 28</a> · <a href="notes/02.%20TF-IDF.md#29-long-document-limitation">Section 29</a> · <a href="notes/02.%20TF-IDF.md#30-repeated-term-limitation">Section 30</a> · <a href="notes/02.%20TF-IDF.md#34-tf-idf-strengths-and-weaknesses">Section 34</a></td><td align="center">Done</td></tr>
<tr><td align="center">08</td><td>Implementation from scratch using Python</td><td align="center"><a href="notes/02.%20TF-IDF.md#19-build-a-complete-tf-idf-matrix-from-scratch">Section 19</a> · <a href="notes/02.%20TF-IDF.md#22-query-tf-idf-vector">Section 22</a> · <a href="notes/02.%20TF-IDF.md#23-cosine-similarity-for-ranking">Section 23</a> · <a href="notes/02.%20TF-IDF.md#24-end-to-end-tf-idf-search-from-scratch">Section 24</a> · <a href="notes/02.%20TF-IDF.md#25-scikit-learn-tf-idf">Section 25</a></td><td align="center">Done</td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/02.%20TF-IDF.md#what-you-will-learn"><b>What You Will Learn</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">02</td><td><a href="notes/02.%20TF-IDF.md#core-mental-model"><b>Core Mental Model</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">03</td><td><a href="notes/02.%20TF-IDF.md#2-why-is-simple-word-counting-not-enough"><b>2. Why Is Simple Word Counting Not Enough?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/02.%20TF-IDF.md#3-visual-intuition--tf-and-idf-answer-different-questions"><b>3. Visual Intuition — TF and IDF Answer Different Questions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">05</td><td><a href="notes/02.%20TF-IDF.md#4-first-step--tokenization"><b>4. First Step — Tokenization</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">06</td><td><a href="notes/02.%20TF-IDF.md#5-term-frequency-tf"><b>5. Term Frequency (TF)</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">07</td><td><a href="notes/02.%20TF-IDF.md#6-visualize-tf"><b>6. Visualize TF</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">08</td><td><a href="notes/02.%20TF-IDF.md#7-raw-tf-limitation--repetition-keeps-increasing-the-score"><b>7. Raw TF Limitation — Repetition Keeps Increasing the Score</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">09</td><td><a href="notes/02.%20TF-IDF.md#8-normalized-tf"><b>8. Normalized TF</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">10</td><td><a href="notes/02.%20TF-IDF.md#9-log-scaled-tf"><b>9. Log-Scaled TF</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/02.%20TF-IDF.md#checkpoint-1"><b>CHECKPOINT 1</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">12</td><td><a href="notes/02.%20TF-IDF.md#10-document-frequency-df"><b>10. Document Frequency (DF)</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">13</td><td><a href="notes/02.%20TF-IDF.md#11-df-for-the-entire-vocabulary"><b>11. DF for the Entire Vocabulary</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">14</td><td><a href="notes/02.%20TF-IDF.md#12-inverse-document-frequency-idf"><b>12. Inverse Document Frequency (IDF)</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">15</td><td><a href="notes/02.%20TF-IDF.md#13-visual--idf-falls-as-df-increases"><b>13. Visual — IDF Falls as DF Increases</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">16</td><td><a href="notes/02.%20TF-IDF.md#14-build-an-idf-table"><b>14. Build an IDF Table</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">17</td><td><a href="notes/02.%20TF-IDF.md#15-common-word-vs-rare-word-example"><b>15. Common Word vs Rare Word Example</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">18</td><td><a href="notes/02.%20TF-IDF.md#checkpoint-2"><b>CHECKPOINT 2</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">19</td><td><a href="notes/02.%20TF-IDF.md#16-tf-idf-formula"><b>16. TF-IDF Formula</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">20</td><td><a href="notes/02.%20TF-IDF.md#17-manual-tf-idf-calculation"><b>17. Manual TF-IDF Calculation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">21</td><td><a href="notes/02.%20TF-IDF.md#18-compare-two-terms-in-the-same-document"><b>18. Compare Two Terms in the Same Document</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">22</td><td><a href="notes/02.%20TF-IDF.md#19-build-a-complete-tf-idf-matrix-from-scratch"><b>19. Build a Complete TF-IDF Matrix From Scratch</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">23</td><td><a href="notes/02.%20TF-IDF.md#20-visualize-the-tf-idf-matrix"><b>20. Visualize the TF-IDF Matrix</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">24</td><td><a href="notes/02.%20TF-IDF.md#21-why-tf-idf-is-sparse"><b>21. Why TF-IDF Is Sparse</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">25</td><td><a href="notes/02.%20TF-IDF.md#checkpoint-3"><b>CHECKPOINT 3</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">26</td><td><a href="notes/02.%20TF-IDF.md#22-query-tf-idf-vector"><b>22. Query TF-IDF Vector</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">27</td><td><a href="notes/02.%20TF-IDF.md#23-cosine-similarity-for-ranking"><b>23. Cosine Similarity for Ranking</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">28</td><td><a href="notes/02.%20TF-IDF.md#24-end-to-end-tf-idf-search-from-scratch"><b>24. End-to-End TF-IDF Search From Scratch</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">29</td><td><a href="notes/02.%20TF-IDF.md#25-scikit-learn-tf-idf"><b>25. Scikit-Learn TF-IDF</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">-</td></tr>
<tr><td align="center">30</td><td><a href="notes/02.%20TF-IDF.md#26-important-fit_transform-vs-transform"><b>26. Important: fit_transform() vs transform()</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">1</td></tr>
<tr><td align="center">31</td><td><a href="notes/02.%20TF-IDF.md#27-out-of-vocabulary-oov-query-terms"><b>27. Out-of-Vocabulary (OOV) Query Terms</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">32</td><td><a href="notes/02.%20TF-IDF.md#28-synonym-failure"><b>28. Synonym Failure</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">33</td><td><a href="notes/02.%20TF-IDF.md#29-long-document-limitation"><b>29. Long-Document Limitation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">34</td><td><a href="notes/02.%20TF-IDF.md#30-repeated-term-limitation"><b>30. Repeated-Term Limitation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">35</td><td><a href="notes/02.%20TF-IDF.md#31-binary-match-vs-tf-idf"><b>31. Binary Match vs TF-IDF</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">36</td><td><a href="notes/02.%20TF-IDF.md#32-tf-idf-end-to-end-visual"><b>32. TF-IDF End-to-End Visual</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">37</td><td><a href="notes/02.%20TF-IDF.md#checkpoint-4"><b>CHECKPOINT 4</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">38</td><td><a href="notes/02.%20TF-IDF.md#33-why-bm25-improves-on-tf-idf"><b>33. Why BM25 Improves on TF-IDF</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">39</td><td><a href="notes/02.%20TF-IDF.md#34-tf-idf-strengths-and-weaknesses"><b>34. TF-IDF Strengths and Weaknesses</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">40</td><td><a href="notes/02.%20TF-IDF.md#35-tf-idf-debugging-framework"><b>35. TF-IDF Debugging Framework</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">41</td><td><a href="notes/02.%20TF-IDF.md#end-to-end-example--tf-idf-search-from-scratch-and-with-scikit-learn"><b>End-to-End Example — TF-IDF Search From Scratch and With scikit-learn</b></a></td><td align="center">9</td><td align="center">8</td><td align="center">2</td></tr>
<tr><td align="center">42</td><td><a href="notes/02.%20TF-IDF.md#36-interview-questions"><b>36. Interview Questions</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">43</td><td><a href="notes/02.%20TF-IDF.md#37-interview-scenarios"><b>37. Interview Scenarios</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">44</td><td><a href="notes/02.%20TF-IDF.md#38-one-page-revision-map"><b>38. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">45</td><td><a href="notes/02.%20TF-IDF.md#39-practice-tasks"><b>39. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">46</td><td><a href="notes/02.%20TF-IDF.md#40-final-takeaways"><b>40. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">47</td><td><a href="notes/02.%20TF-IDF.md#next-chapter--chapter-5-bm25"><b>Next Chapter — Chapter 5: BM25</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
</tbody>
</table>
