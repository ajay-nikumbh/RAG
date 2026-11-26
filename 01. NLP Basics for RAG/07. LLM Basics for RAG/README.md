<div align="center">

# 01.07 · LLM Basics for RAG

<img src="https://img.shields.io/badge/01%20%C2%B7%20NLP%20Basics%20for%20RAG-6366F1?style=for-the-badge" alt="group"/> <img src="https://img.shields.io/badge/Status-Done-10B981?style=for-the-badge" alt="status"/>

**What an LLM does, context window, token cost, temperature, why LLMs hallucinate and why retrieval helps.**

</div>

<p align="center"><a href="../06.%20Similarity%20Metrics%20for%20Dense%20Search/README.md">Previous: 01.06 Similarity Metrics for Dense Search</a> | <a href="../../README.md">Home</a> | <a href="../README.md">Group 01: NLP Basics for RAG</a> | <a href="notes/07.%20LLM%20Basics%20for%20RAG.md">Notes</a> | <a href="../../02.%20RAG%20Introduction/01.%20RAG%20Fundamentals/README.md">Next: 02.01 RAG Fundamentals</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="20%">Resource</th><th width="54%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Markdown notes with diagrams and clean code</td><td align="center"><a href="notes/07.%20LLM%20Basics%20for%20RAG.md">Open</a></td></tr>
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
<tr><td align="center">01</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#basic-definitions-in-simple-words"><b>Basic Definitions in Simple Words</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">02</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#1-what-exactly-is-an-llm"><b>1. What exactly is an LLM?</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#2-autoregressive-generation"><b>2. Autoregressive generation</b></a></td><td align="center">-</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">04</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#3-what-goes-into-an-llm-in-rag"><b>3. What goes into an LLM in RAG?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">05</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#4-rag-prompt-anatomy"><b>4. RAG prompt anatomy</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">06</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#5-parametric-knowledge"><b>5. Parametric knowledge</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">07</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#6-parametric-knowledge-is-different-from-a-database"><b>6. Parametric knowledge is different from a database</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">08</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#7-why-parametric-knowledge-creates-problems-for-enterprise-rag"><b>7. Why parametric knowledge creates problems for enterprise RAG</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">09</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#8-parametric-vs-non-parametric-knowledge"><b>8. Parametric vs non-parametric knowledge</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">10</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#9-without-rag"><b>9. Without RAG</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">11</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#10-with-rag"><b>10. With RAG</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">12</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#11-why-retrieval-helps"><b>11. Why retrieval helps</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">13</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#12-why-retrieval-does-not-eliminate-hallucination"><b>12. Why retrieval does NOT eliminate hallucination</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">14</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#13-why-llms-hallucinate"><b>13. Why LLMs hallucinate</b></a></td><td align="center">7</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">15</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#14-hallucination-flow"><b>14. Hallucination flow</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">16</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#15-context-window"><b>15. Context window</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">17</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#16-what-consumes-context"><b>16. What consumes context?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">18</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#17-example-token-budget-calculation"><b>17. Example token-budget calculation</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">19</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#18-context-budget-architecture"><b>18. Context-budget architecture</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">20</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#19-why-larger-context-window-does-not-remove-retrieval"><b>19. Why larger context window does not remove retrieval</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">21</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#20-retrieval-as-information-bottleneck"><b>20. Retrieval as information bottleneck</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">22</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#21-more-context-is-not-always-better"><b>21. More context is not always better</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">23</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#22-lost-in-the-middle-intuition"><b>22. Lost-in-the-middle intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">24</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#23-why-reranking-matters-to-llms"><b>23. Why reranking matters to LLMs</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">25</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#24-temperature"><b>24. Temperature</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">26</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#25-low-temperature"><b>25. Low temperature</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">27</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#26-higher-temperature"><b>26. Higher temperature</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">28</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#27-temperature-visualization"><b>27. Temperature visualization</b></a></td><td align="center">2</td><td align="center">2</td><td align="center">2</td></tr>
<tr><td align="center">29</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#28-important-temperature-misconception"><b>28. Important temperature misconception</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">30</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#29-greedy-decoding-intuition"><b>29. Greedy decoding intuition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">31</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#30-top-k--top-p-awareness"><b>30. Top-k / top-p awareness</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">32</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#31-prompting-in-rag"><b>31. Prompting in RAG</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">33</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#32-grounded-generation"><b>32. Grounded generation</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">34</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#33-retrieval-changes-the-llm-task"><b>33. Retrieval changes the LLM task</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">35</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#34-but-retrieval-can-also-hurt-generation"><b>34. But retrieval can also hurt generation</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">1</td></tr>
<tr><td align="center">36</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#35-garbage-in-garbage-out"><b>35. Garbage-in-garbage-out</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">37</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#36-llm-vs-embedding-model"><b>36. LLM vs embedding model</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">38</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#37-mermaid-comparison"><b>37. Mermaid comparison</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">39</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#38-llm-context-vs-vector-database"><b>38. LLM context vs vector database</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">40</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#39-three-knowledge-locations-in-rag"><b>39. Three knowledge locations in RAG</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">41</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#40-conversation-history-also-competes-with-retrieval"><b>40. Conversation history also competes with retrieval</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">42</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#41-context-budgeting-formula"><b>41. Context budgeting formula</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">43</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#42-dynamic-context-construction"><b>42. Dynamic context construction</b></a></td><td align="center">1</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">44</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#43-why-rag-can-improve-factuality"><b>43. Why RAG can improve factuality</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">45</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#44-why-rag-improves-auditability"><b>44. Why RAG improves auditability</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">46</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#45-why-rag-vs-fine-tuning-for-knowledge-updates"><b>45. Why RAG vs fine-tuning for knowledge updates</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">47</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#46-rag-vs-long-context-prompting"><b>46. RAG vs long-context prompting</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">48</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#47-rag-failure-decomposition"><b>47. RAG failure decomposition</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">49</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#48-example-end-to-end"><b>48. Example end-to-end</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">50</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#49-interview-question--what-does-an-llm-actually-do"><b>49. Interview question — What does an LLM actually do?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">51</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#50-interview-question--what-is-parametric-knowledge"><b>50. Interview question — What is parametric knowledge?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">52</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#51-interview-question--why-do-llms-hallucinate"><b>51. Interview question — Why do LLMs hallucinate?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">53</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#52-interview-question--how-does-rag-reduce-hallucination"><b>52. Interview question — How does RAG reduce hallucination?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">54</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#53-interview-question--why-doesnt-rag-eliminate-hallucination"><b>53. Interview question — Why doesn't RAG eliminate hallucination?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">55</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#54-interview-question--what-is-a-context-window"><b>54. Interview question — What is a context window?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">56</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#55-interview-question--how-do-you-calculate-rag-context-budget"><b>55. Interview question — How do you calculate RAG context budget?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">57</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#56-interview-question--why-not-put-the-entire-corpus-into-a-large-context-window"><b>56. Interview question — Why not put the entire corpus into a large context window?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">58</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#57-interview-question--what-does-temperature-do"><b>57. Interview question — What does temperature do?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">59</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#58-interview-question--does-temperature-solve-hallucination"><b>58. Interview question — Does temperature solve hallucination?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">60</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#59-interview-question--embedding-model-vs-llm"><b>59. Interview question — Embedding model vs LLM?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">61</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#60-interview-question--rag-vs-fine-tuning"><b>60. Interview question — RAG vs fine-tuning?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">62</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#61-interview-question--rag-vs-long-context"><b>61. Interview question — RAG vs long context?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">63</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#62-common-interview-traps"><b>62. Common interview traps</b></a></td><td align="center">8</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">64</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#63-complete-rag-mental-model"><b>63. Complete RAG mental model</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">65</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#64-final-revision-sheet"><b>64. Final revision sheet</b></a></td><td align="center">10</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">66</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#65-practice-tasks"><b>65. Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">67</td><td><a href="notes/07.%20LLM%20Basics%20for%20RAG.md#66-final-takeaways"><b>66. Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
