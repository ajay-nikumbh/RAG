<div align="center">

# 01.01 · Text Preprocessing for Retrieval

<img src="https://img.shields.io/badge/01%20%C2%B7%20NLP%20Basics%20for%20RAG-6366F1?style=for-the-badge" alt="group"/> <img src="https://img.shields.io/badge/Status-Done-10B981?style=for-the-badge" alt="status"/>

**Normalization, stop words, stemming vs lemmatization, n-grams, why the same preprocessing must run on documents and queries.**

</div>

<p align="center"><a href="../../README.md">Home</a> | <a href="../README.md">Group 01: NLP Basics for RAG</a> | <a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md">Notes</a> | <a href="../02.%20Tokens%20and%20Tokenization/README.md">Next: 01.02 Tokens and Tokenization</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="20%">Resource</th><th width="54%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Markdown notes with diagrams and clean code</td><td align="center"><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Notebook</b></td><td>Runnable notebook with code and outputs</td><td align="center"><a href="notebooks/01.%20Text%20Preprocessing%20for%20Retrieval.ipynb">Open</a></td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Figures used by the notes and notebook</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Data used by this chapter</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#basic-definitions-in-simple-words"><b>Basic Definitions in Simple Words</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">02</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#1-where-preprocessing-fits-in-rag"><b>1. Where Preprocessing Fits in RAG</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#2-why-preprocessing-matters-for-retrieval"><b>2. Why Preprocessing Matters for Retrieval</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#3-the-golden-rule-same-pipeline-on-both-sides"><b>3. The Golden Rule: Same Pipeline on Both Sides</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">05</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#4-unicode-normalization"><b>4. Unicode Normalization</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">06</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#5-case-folding"><b>5. Case Folding</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">07</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#6-accent-folding"><b>6. Accent Folding</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">08</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#7-whitespace-line-breaks-and-hyphenation"><b>7. Whitespace, Line Breaks and Hyphenation</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">09</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#8-tokenization-for-retrieval"><b>8. Tokenization for Retrieval</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">10</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#9-stop-words"><b>9. Stop Words</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#10-stemming-vs-lemmatization"><b>10. Stemming vs Lemmatization</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">12</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#11-n-grams-for-phrases-and-typos"><b>11. N-grams for Phrases and Typos</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">13</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#12-protecting-special-tokens"><b>12. Protecting Special Tokens</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">14</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#13-a-configurable-preprocessing-pipeline"><b>13. A Configurable Preprocessing Pipeline</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">15</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#14-preprocessing-for-sparse-vs-dense-retrieval"><b>14. Preprocessing for Sparse vs Dense Retrieval</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">16</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#15-end-to-end-example-does-preprocessing-change-bm25-results"><b>15. End-to-End Example: Does Preprocessing Change BM25 Results?</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">17</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#16-over-processing-failures"><b>16. Over-Processing Failures</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">18</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#17-checkpoints-with-answers"><b>17. Checkpoints With Answers</b></a></td><td align="center">3</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">19</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#18-interview-questions"><b>18. Interview Questions</b></a></td><td align="center">6</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">20</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#19-interview-scenarios"><b>19. Interview Scenarios</b></a></td><td align="center">4</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">21</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#20-one-page-revision-map"><b>20. One-Page Revision Map</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">22</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#21-practice-tasks"><b>21. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">23</td><td><a href="notes/01.%20Text%20Preprocessing%20for%20Retrieval.md#22-final-takeaways"><b>22. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
