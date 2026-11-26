<div align="center">

# 01.04 · Embeddings Fundamentals

<img src="https://img.shields.io/badge/01%20%C2%B7%20NLP%20Basics%20for%20RAG-6366F1?style=for-the-badge" alt="group"/> <img src="https://img.shields.io/badge/Status-Done-10B981?style=for-the-badge" alt="status"/>

**Dense vectors, model selection, domain-specific and multilingual embeddings.**

</div>

<p align="center"><a href="../03.%20From%20Bag%20of%20Words%20to%20Embeddings/README.md">Previous: 01.03 From Bag of Words to Embeddings</a> | <a href="../../README.md">Home</a> | <a href="../README.md">Group 01: NLP Basics for RAG</a> | <a href="notes/04.%20Embeddings%20Fundamentals.md">Notes</a> | <a href="../05.%20Embedding%20Mathematics/README.md">Next: 01.05 Embedding Mathematics</a></p>

## Chapter files

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="20%">Resource</th><th width="54%">Description</th><th width="18%">Link</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><b>Notes</b></td><td>Markdown notes with diagrams and clean code</td><td align="center"><a href="notes/04.%20Embeddings%20Fundamentals.md">Open</a></td></tr>
<tr><td align="center">02</td><td><b>Notebook</b></td><td>Runnable notebook with code and outputs</td><td align="center"><a href="notebooks/04.%20Embeddings%20Fundamentals.ipynb">Open</a></td></tr>
<tr><td align="center">03</td><td><b>Diagrams</b></td><td>Figures used by the notes and notebook</td><td align="center"><a href="diagrams">Open</a></td></tr>
<tr><td align="center">04</td><td><b>Datasets</b></td><td>Data used by this chapter</td><td align="center"><a href="datasets">Open</a></td></tr>
<tr><td align="center">05</td><td><b>Exercises</b></td><td>Practice tasks</td><td align="center"><a href="exercises">Open</a></td></tr>
</tbody>
</table>

## Subtopic index

<table width="100%">
<thead><tr><th width="8%">Sr No</th><th width="56%">Section</th><th width="12%">Subtopics</th><th width="12%">Code</th><th width="12%">Diagrams</th></tr></thead>
<tbody>
<tr><td align="center">01</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#introduction"><b>Introduction</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">02</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#basic-definitions-in-simple-words"><b>Basic Definitions in Simple Words</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">03</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-1--why-do-embeddings-exist"><b>Part 1 — Why do embeddings exist?</b></a></td><td align="center">15</td><td align="center">-</td><td align="center">10</td></tr>
<tr><td align="center">04</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-2--different-kinds-of-embeddings"><b>Part 2 — Different kinds of embeddings</b></a></td><td align="center">6</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">05</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-3--pooling"><b>Part 3 — Pooling</b></a></td><td align="center">9</td><td align="center">2</td><td align="center">-</td></tr>
<tr><td align="center">06</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-4--how-text-embeddings-are-learned"><b>Part 4 — How text embeddings are learned</b></a></td><td align="center">14</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">07</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-5--bi-encoders"><b>Part 5 — Bi-encoders</b></a></td><td align="center">12</td><td align="center">-</td><td align="center">6</td></tr>
<tr><td align="center">08</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-6--similarity-mathematics"><b>Part 6 — Similarity mathematics</b></a></td><td align="center">14</td><td align="center">3</td><td align="center">1</td></tr>
<tr><td align="center">09</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-7--building-embeddings-in-python"><b>Part 7 — Building embeddings in Python</b></a></td><td align="center">9</td><td align="center">9</td><td align="center">-</td></tr>
<tr><td align="center">10</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-8--what-does-an-embedding-actually-encode"><b>Part 8 — What does an embedding actually encode?</b></a></td><td align="center">3</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">11</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-9--query-embeddings-vs-document-embeddings"><b>Part 9 — Query embeddings vs document embeddings</b></a></td><td align="center">3</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">12</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-10--embedding-dimensionality"><b>Part 10 — Embedding dimensionality</b></a></td><td align="center">5</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">13</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-11--high-dimensional-geometry"><b>Part 11 — High-dimensional geometry</b></a></td><td align="center">4</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">14</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-12--embedding-normalization"><b>Part 12 — Embedding normalization</b></a></td><td align="center">2</td><td align="center">2</td><td align="center">-</td></tr>
<tr><td align="center">15</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-13--embedding-similarity-thresholds"><b>Part 13 — Embedding similarity thresholds</b></a></td><td align="center">3</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">16</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-14--embedding-models-and-chunk-size"><b>Part 14 — Embedding models and chunk size</b></a></td><td align="center">3</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">17</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-15--domain-specific-embeddings"><b>Part 15 — Domain-specific embeddings</b></a></td><td align="center">4</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">18</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-16--multilingual-embeddings"><b>Part 16 — Multilingual embeddings</b></a></td><td align="center">3</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">19</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-17--embeddings-for-different-content-types"><b>Part 17 — Embeddings for different content types</b></a></td><td align="center">2</td><td align="center">1</td><td align="center">-</td></tr>
<tr><td align="center">20</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-18--embedding-model-selection"><b>Part 18 — Embedding model selection</b></a></td><td align="center">13</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">21</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-19--embedding-caching"><b>Part 19 — Embedding caching</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">22</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-20--embedding-versioning"><b>Part 20 — Embedding versioning</b></a></td><td align="center">3</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">23</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-21--updating-documents"><b>Part 21 — Updating documents</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">24</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-22--embedding-batch-processing"><b>Part 22 — Embedding batch processing</b></a></td><td align="center">1</td><td align="center">2</td><td align="center">1</td></tr>
<tr><td align="center">25</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-23--common-embedding-failure-modes"><b>Part 23 — Common embedding failure modes</b></a></td><td align="center">11</td><td align="center">1</td><td align="center">2</td></tr>
<tr><td align="center">26</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-24--embeddings-are-lossy-compression"><b>Part 24 — Embeddings are lossy compression</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">27</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-25--why-vector-arithmetic-sometimes-works"><b>Part 25 — Why vector arithmetic sometimes works</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">28</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-26--word2vec-intuition"><b>Part 26 — Word2Vec intuition</b></a></td><td align="center">4</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">29</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-27--transformer-to-sentence-embedding-pipeline"><b>Part 27 — Transformer-to-sentence-embedding pipeline</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">30</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-28--self-attention-connection"><b>Part 28 — Self-attention connection</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">31</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-29--positional-information"><b>Part 29 — Positional information</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">32</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-30--similarity-is-model-dependent"><b>Part 30 — Similarity is model-dependent</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">33</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-31--similarity-score-is-not-probability"><b>Part 31 — Similarity score is not probability</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">34</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-32--what-is-a-good-cosine-score"><b>Part 32 — What is a good cosine score?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">35</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-33--embedding-retrieval-and-metadata-filters"><b>Part 33 — Embedding retrieval and metadata filters</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">36</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-34--embedding-security-considerations"><b>Part 34 — Embedding security considerations</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">37</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-35--embedding-observability"><b>Part 35 — Embedding observability</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">38</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-36--empty-chunks"><b>Part 36 — Empty chunks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">39</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-37--duplicates"><b>Part 37 — Duplicates</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">40</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-38--production-embedding-architecture"><b>Part 38 — Production embedding architecture</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">41</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-39--scaling-embedding-generation"><b>Part 39 — Scaling embedding generation</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">42</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-40--embedding-latency-online"><b>Part 40 — Embedding latency online</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">43</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-41--should-query-embeddings-be-generated-by-the-llm"><b>Part 41 — Should query embeddings be generated by the LLM?</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">44</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-42--embeddings-vs-fine-tuning"><b>Part 42 — Embeddings vs fine-tuning</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">45</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-43--evaluation"><b>Part 43 — Evaluation</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">46</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-44--error-diagnosis"><b>Part 44 — Error diagnosis</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">47</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-45--faang-interview-questions"><b>Part 45 — FAANG interview questions</b></a></td><td align="center">20</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">48</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-46--interview-traps"><b>Part 46 — Interview traps</b></a></td><td align="center">9</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">49</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-47--production-design-example"><b>Part 47 — Production design example</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">50</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-48--full-mathematical-summary"><b>Part 48 — Full mathematical summary</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">51</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-49--most-important-conceptual-diagram"><b>Part 49 — Most important conceptual diagram</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">2</td></tr>
<tr><td align="center">52</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-50--how-to-think-about-embeddings-in-one-sentence"><b>Part 50 — How to think about embeddings in one sentence</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">53</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-51--what-embeddings-are-good-at-vs-bad-at"><b>Part 51 — What embeddings are good at vs bad at</b></a></td><td align="center">2</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">54</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#part-52--revision-cheat-sheet"><b>Part 52 — Revision cheat sheet</b></a></td><td align="center">15</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">55</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#final-mental-model"><b>Final mental model</b></a></td><td align="center">1</td><td align="center">-</td><td align="center">1</td></tr>
<tr><td align="center">56</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#practice-tasks"><b>Practice Tasks</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
<tr><td align="center">57</td><td><a href="notes/04.%20Embeddings%20Fundamentals.md#final-takeaways"><b>Final Takeaways</b></a></td><td align="center">-</td><td align="center">-</td><td align="center">1</td></tr>
</tbody>
</table>
