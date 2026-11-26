<div align="center">

# 01.03 · From Bag of Words to Embeddings

<img src="https://img.shields.io/badge/01%20%C2%B7%20NLP%20Basics%20for%20RAG-6366F1?style=for-the-badge" alt="group"/> <img src="https://img.shields.io/badge/Status-Done-10B981?style=for-the-badge" alt="status"/>

**One-hot and bag-of-words vectors, word2vec intuition, contextual embeddings, why meaning needs dense vectors.**

</div>

<p align="center"><a href="../02.%20Tokens%20and%20Tokenization/README.md">Previous: 01.02 Tokens and Tokenization</a> | <a href="../../README.md">Home</a> | <a href="../README.md">Group 01: NLP Basics for RAG</a> | <a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md">Notes</a> | <a href="../04.%20Embeddings%20Fundamentals/README.md">Next: 01.04 Embeddings Fundamentals</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="20%">Resource</th><th width="54%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Markdown notes with diagrams and clean code</td><td align="center"><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Notebook</b></td><td>Runnable notebook with code and outputs</td><td align="center">Not yet</td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Figures used by the notes and notebook</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Data used by this chapter</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#basic-definitions-in-simple-words"><b>Basic Definitions in Simple Words</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">02</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#1-why-do-we-need-numerical-text-representations"><b>1. Why do we need numerical text representations?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">03</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#2-one-hot-encoding"><b>2. One-Hot Encoding</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">04</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#3-mathematical-representation"><b>3. Mathematical representation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">05</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#4-major-problem-with-one-hot-vectors"><b>4. Major problem with one-hot vectors</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">06</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#5-one-hot-has-no-semantic-geometry"><b>5. One-hot has no semantic geometry</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">07</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#6-another-problem-dimensionality"><b>6. Another problem: dimensionality</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">08</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#7-sparse-vs-dense-vectors"><b>7. Sparse vs dense vectors</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">09</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#8-from-words-to-documents--bag-of-words"><b>8. From words to documents — Bag of Words</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">10</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#9-bag-of-words-example"><b>9. Bag-of-Words example</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#10-why-is-it-called-a-bag"><b>10. Why is it called a "bag"?</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">12</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#11-bow-architecture"><b>11. BoW architecture</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">13</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#12-why-bow-was-useful"><b>12. Why BoW was useful</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">14</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#13-problem-all-words-arent-equally-useful"><b>13. Problem: all words aren't equally useful</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">15</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#14-tf-idf--important-bridge"><b>14. TF-IDF — important bridge</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">16</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#15-term-frequency"><b>15. Term Frequency</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">17</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#16-inverse-document-frequency"><b>16. Inverse Document Frequency</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">18</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#17-tf-idf"><b>17. TF-IDF</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">19</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#18-tf-idf-representation"><b>18. TF-IDF representation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">20</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#19-the-synonym-problem"><b>19. The synonym problem</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">21</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#20-another-example"><b>20. Another example</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">22</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#21-the-key-conceptual-shift"><b>21. The key conceptual shift</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">23</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#22-distributional-hypothesis"><b>22. Distributional hypothesis</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">24</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#23-word2vec"><b>23. Word2Vec</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">25</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#24-word2vec-training-intuition"><b>24. Word2Vec training intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">26</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#25-cbow--continuous-bag-of-words"><b>25. CBOW — Continuous Bag of Words</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">27</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#26-cbow-mermaid"><b>26. CBOW Mermaid</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">28</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#27-skip-gram"><b>27. Skip-gram</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">29</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#28-skip-gram-mermaid"><b>28. Skip-gram Mermaid</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">30</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#29-why-word2vec-was-revolutionary"><b>29. Why Word2Vec was revolutionary</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">31</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#30-dense-semantic-geometry"><b>30. Dense semantic geometry</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">32</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#31-famous-vector-arithmetic-intuition"><b>31. Famous vector arithmetic intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">33</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#32-static-embeddings"><b>32. Static embeddings</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">34</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#33-static-embedding-problem"><b>33. Static embedding problem</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">35</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#34-contextual-embeddings"><b>34. Contextual embeddings</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">36</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#35-static-vs-contextual"><b>35. Static vs contextual</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">37</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#36-transformer-contextual-representations"><b>36. Transformer contextual representations</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">38</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#37-from-token-embeddings-to-sentence-embeddings"><b>37. From token embeddings to sentence embeddings</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">39</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#38-sentence-embedding-intuition"><b>38. Sentence embedding intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">40</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#39-why-fixed-size-dense-vectors-are-powerful"><b>39. Why fixed-size dense vectors are powerful</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">41</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#40-sparse-vs-dense-retrieval"><b>40. Sparse vs dense retrieval</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">42</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#41-comparison"><b>41. Comparison</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">43</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#42-why-dense-vectors-are-called-embeddings"><b>42. Why dense vectors are called embeddings</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">44</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#43-why-meaning-needs-learned-dense-representations"><b>43. Why meaning needs learned dense representations</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">45</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#44-important-nuance--dense-does-not-understand-perfectly"><b>44. Important nuance — dense does not "understand" perfectly</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">46</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#45-bag-of-words-python"><b>45. Bag of Words Python</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">47</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#46-create-bow-manually"><b>46. Create BoW manually</b></a></td><td align="center">-</td><td align="center">2</td><td align="center">-</td></tr>
<tr><td align="center">48</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#47-the-semantic-failure-in-code"><b>47. The semantic failure in code</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">49</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#48-one-hot--bow--embeddings"><b>48. One-hot → BoW → embeddings</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">50</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#49-why-did-we-not-simply-abandon-sparse-retrieval"><b>49. Why did we not simply abandon sparse retrieval?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">51</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#50-lexical-vs-semantic-retrieval-example"><b>50. Lexical vs semantic retrieval example</b></a></td><td align="center">3</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">52</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#51-interview-question--why-is-one-hot-encoding-poor-for-semantics"><b>51. Interview question — Why is one-hot encoding poor for semantics?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">53</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#52-interview-question--what-is-bag-of-words"><b>52. Interview question — What is Bag of Words?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">54</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#53-interview-question--main-limitation-of-bow"><b>53. Interview question — Main limitation of BoW?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">55</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#54-interview-question--why-tf-idf-over-raw-bow"><b>54. Interview question — Why TF-IDF over raw BoW?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">56</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#55-interview-question--what-is-the-core-idea-behind-word2vec"><b>55. Interview question — What is the core idea behind Word2Vec?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">57</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#56-interview-question--cbow-vs-skip-gram"><b>56. Interview question — CBOW vs Skip-gram?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">58</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#57-interview-question--why-are-word2vec-embeddings-called-static"><b>57. Interview question — Why are Word2Vec embeddings called static?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">59</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#58-interview-question--what-are-contextual-embeddings"><b>58. Interview question — What are contextual embeddings?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">60</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#59-interview-question--sparse-vs-dense-vectors"><b>59. Interview question — Sparse vs dense vectors?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">61</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#60-interview-question--why-not-use-dense-retrieval-only"><b>60. Interview question — Why not use dense retrieval only?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">62</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#61-important-interview-progression"><b>61. Important interview progression</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">63</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#62-common-traps"><b>62. Common traps</b></a></td><td align="center">8</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">64</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#63-mental-model"><b>63. Mental model</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">65</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#64-final-comparison-table"><b>64. Final comparison table</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">66</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#65-final-revision"><b>65. Final revision</b></a></td><td align="center">6</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">67</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#66-practice-tasks"><b>66. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">68</td><td><a href="notes/03.%20From%20Bag%20of%20Words%20to%20Embeddings.md#67-final-takeaways"><b>67. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
