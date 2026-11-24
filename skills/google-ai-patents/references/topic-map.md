# Topic map: AI search and SEO concepts → patent language → patents

Under each heading: the concept the user uses, the terms the patents use (search with these), and starting patents
verified with the tool. The lists are starting points; before answering, reopen the relevant patent with `show`,
`claims` and `passages`. The numbers were verified with the tool on 17 November 2026.

## Contents

1. AI Overviews / generative summaries
2. Query fan-out: splitting the query into sub-queries and synthetic queries
3. Source and passage selection for the generative answer, diversity
4. Citations, verification, factuality and hallucination
5. Conversational search and session state (AI Mode-like)
6. Proactive suggestions and "change event" summaries
7. Training and augmenting LLMs with the search engine
8. Generative search interface and formats
9. Speed and cost: model selection, latency
10. Dense retrieval, embeddings and LLM query expansion
11. Query intent and query rewriting
12. Multimodal and visual search (Lens, Circle to Search-like)
13. Foundation model architectures (Transformer, MoE, word2vec)
14. Marking AI content and verifying provenance (SynthID-like)

---

## 1. AI Overviews / generative summaries

- **Patent language:** "natural language (NL) based summary", "generative summary", "large language model (LLM) output",
  "search result documents (SRDs)", "linkifying", "verification".
- **Search:** `search generative summary search results --ai`, `search '"NL based summary"' --in claims`
- `US11769017B1` "Generative summaries for search results" (priority 2022, granted). Claim 1: generating LLM output from
  the query and/or the content of search result documents and showing the NL based summary together with links to the
  responsive documents; updating the summary when the user interacts with a document. In the same family, with
  different claims: `US11886828B1`, `US11900068B1`, `US12118325B2` (granted) and `US20240220735A1`; recorded separately
  with the same title: `US20250005303A1`, `WO2024145537A1`, `EP4627452A1`. For claim-level evidence, read each member's
  claims separately.
- `US20250139105A1` "Query-aware extractive hierarchical summarization" (priority 2023, application).
- `US12566796B1` "Query-dependent generative descriptions for videos provided via a search result" (priority 2024).

## 2. Query fan-out: sub-queries and synthetic queries

- **Patent language:** "sub-queries", "decomposing the input query", "synthetic queries", "related queries",
  "query variants", "comprehensive response".
- **Search:** `search query decomposition sub-queries --search`, `search '"synthetic queries"'`
- `US20250348485A1` (and `WO2025240274A1`) "Generative model based decomposition of input query into sub-queries and
  generation of comprehensive response based on responses to sub-queries" (priority 2024, application). Claim 1: a
  generative model decomposes the query into sub-queries and the tools to use for each sub-query; a comprehensive
  response is generated from the sub-responses, checked with a "critique response" and refined if it falls short.
- `US20240289407A1` "Search with stateful chat" (priority 2023, application). Claim 1: synthetic queries are generated
  from the query + user/device context; the document set is selected from documents responsive to both the original
  query and the synthetic queries.
- `US20260072965A1` "Controlled content diversity in retrieval for generative search" (priority 2024, application): a
  group of related queries (see section 3).
- `US11663201B2` "Generating query variants using a trained generative model" (priority 2017, granted): an early
  example of generating query variants with a generative model.
- `US12730818B2` "Adaptive deadline bounded query execution using generative model(s)" (priority 2024, granted).

## 3. Source and passage selection, diversity

- **Patent language:** "portions from highest-ranked resources", "relevance to … and diversity from", "context passages",
  "long-form response", "retrieval-augmented generation".
- **Search:** `search content diversity retrieval generative --search`, `search '"highest-ranked resources"' --in claims`,
  `search retrieval augmented generation passages --search --from 2023`
- `US20260072965A1` "Controlled content diversity in retrieval for generative search" (priority 2024, application).
  Claim 1: related queries are determined for the query based on relevance and diversity; for the original query and
  each related query, portions are selected **from the highest-ranked resources** based on relevance and on difference
  from one another; these are given to the generative model to generate a long-form response. One of the most direct
  patents from an SEO perspective.
- `US20260147768A1` "System For Extracting Relevant Passages As Context For Multimodal Queries" (priority 2024,
  application).
- `US20260252576A1` "Refining Ambiguous Retrieval-Augmented Generation Queries Through User Feedback" (GDM, priority 2025).
- `US20260147631A1` "Systemic Performance Improvement for Retrieval-Augmented Generation Serving" (priority 2024).

## 4. Citations, verification, factuality, hallucination

- **Patent language:** "citations", "verification", "factuality", "hallucination", "confabulation", "grounding",
  "uncertainty", "abstention", "encoded context passages".
- **Search:** `search citation generative response`, `search factuality generated responses`,
  `search '(hallucination OR uncertainty OR abstention) "language model"'`, for DeepMind `--group deepmind`
- `US20240289395A1` "Factuality of generated responses" (priority 2023, application). Claim 1: the query-generating part
  of the LLM generates a search query; the response-generating part is trained to decide whether to use the retrieved
  passages.
- `US12277635B1` "User verification of a generative response to a multimodal query" (priority 2023, granted).
- `US12530398B2` "Visual citations for information provided in response to multimodal queries" (priority 2023, granted).
- `US12346366B2` "Providing generative answers including citations to source documents" (priority 2023, granted).
  **Caution:** its claims are about documents on a cloud storage platform (Drive), not web search.
- `US20250225337A1` "Detection of hallucinations in large language model responses" (priority 2024, application);
  `US20260154578A1` "Real-time hallucination detection and correction for large language model(s)" (priority 2024);
  `WO2025245362A1` "Detecting neural network hallucinations using in-context learning" (GDM, priority 2024).
- DeepMind's approach of measuring uncertainty and abstaining when needed: `WO2025165950A1` "Conformal abstention for
  neural networks" (priority 2024; no answer is given if the similarity score between candidates does not meet a
  threshold), `US20260220391A1` "Summarizing LLM Predictive Distributions from Embeddings" (GDM, priority 2025;
  "hallucinating" occurs in the description).
- `US12008473B2` (section 7) selects among candidate responses conditioned on search results; the word "hallucination"
  does not occur.

## 5. Conversational search and session state

- **Patent language:** "stateful chat", "search session", "state data", "multi-turn", "follow-up query", "conversational".
- **Search:** `search stateful chat search --search`, `search multi-turn dialog generative --search`
- `US20240289407A1` "Search with stateful chat" (see section 2): generative search that keeps state data throughout the
  session.
- `US12651122B2` "Preservation of visual content across multi-turn dialogs with generative model(s)" (priority 2024,
  granted).
- `US20250173519A1` "Query Intent Understanding and Search Result Generation" (priority 2023, application).
- `US10026398B2` "Follow-up voice query prediction" (priority 2016, granted).
- `US12450464B2` "Guided dialogue using language generation neural networks and search" (GDM, priority 2022, granted).
- `US20250173519A1` Claim 1: the new query is processed together with earlier inputs in the same multi-turn session to
  generate a "contextually aware query". In `US20240289407A1` follow-up questions are described not in the claims but
  in the description ([¶218]).
- `US20260178846A1` "Using llms to automatically create follow-up links in llm response" (priority 2024, application).

## 6. Proactive suggestions and change event summaries

- **Patent language:** "proactive query and content suggestion", "change event", "web data", "change event summary".
- `US12079292B1` "Proactive query and content suggestion with generative model generated question and answer"
  (priority 2023, granted). Claim 1: a change event on a topic is detected from web data; the generative model
  generates query suggestions and a change summary from the related web resources. (Matching it to Discover / "what
  changed" style surfaces is an interpretation.)
- `US12730848B2` "Content snippet generation and storage with generative model content grouping" (priority 2024, granted).

## 7. Training and augmenting LLMs with the search engine

- **Patent language:** "search engine conditioned", "supervision signal", "reinforcement learning", "augmenting … using
  search engine results".
- `US12437016B2` "Fine-tuning large language model(s) using reinforcement learning with search engine feedback"
  (priority 2023, granted). Claim 1: a supervision signal is generated by comparing the raw LLM output with output
  conditioned on search engine results, and the LLM is fine-tuned.
- `US12008473B2` "Augmenting machine learning language models using search engine results" (DeepMind, priority 2022,
  granted).
- `WO2024207009A1` / `US20260277967A1` "Efficient use of tools by language models" (priority 2023).

## 8. Generative search interface and formats

- `US20260003902A1` "Generative ai search formats" (priority 2024, application).
- `US20250348504A1` "Search System for Providing Categorical Search Results Via Generative Models" (priority 2024,
  application): search results organised by topic.
- `WO2025085135A1` "Contextualized and optimal content load and placement in a web search environment using generative
  models" (priority 2023).
- `US20260161721A1` "Prompt Element Generation for use as Input in Generative Models in a Web Search Environment"
  (priority 2023).
- `US12158907B1` "Thematic search" (priority 2023, granted).

## 9. Speed and cost

- `US12664187B2` "Dynamic selection from among multiple candidate generative models with differing computational
  efficiencies" (priority 2023, granted).
- `US12499144B2` "LLM latency reduction via bridging multiple LLMS of differing sizes" (priority 2023, granted).
- `US20260161639A1` "Reducing latency, in generating output response to a user query, based on processing the user
  query using generative model(s)" (priority 2024).
- `US12730818B2` "Adaptive deadline bounded query execution using generative model(s)" (priority 2024, granted).

## 10. Dense retrieval, embeddings, LLM query expansion

- **Patent language:** "dual encoder", "embedding", "differentiable search index", "query expansion", "negative sampling",
  "reranking".
- `WO2024229375A1` "Query expansion by prompting large language models" (priority 2023).
- `US20260064743A1` "Systems and Methods for Prompt-Based Query Generation for Diverse Retrieval" (priority 2022).
- `US20250355948A1` "Instruction-based dual encoder retrieval system" (priority 2024).
- `US20250165469A1` "Machine Learning Models as a Differentiable Search Index for Directly Predicting Resource
  Retrieval Results" (priority 2022).
- `US12619922B2` "Training embedding models using a stale embedding cache for negative sampling" (priority 2021, granted).
- `US12511325B2` "Reranking documents based on graph representations of the documents" (priority 2024, granted).

## 11. Query intent and query rewriting

- `US20250173519A1` "Query Intent Understanding and Search Result Generation" (priority 2023).
- `US9684693B1` "On-device query rewriting" (priority 2016, granted).
- `US20240135187A1` "Method for Training Large Language Models to Perform Query Intent Classification" (priority 2022).
- `US9147154B2` "Classifying resources using a deep network" (priority 2013, granted): classifying resources with a deep
  network.

## 12. Multimodal and visual search

- **Patent language:** "multimodal query", "visual search", "image query", "search refinement".
- `US12380157B2` "Visual search interface in an operating system" (priority 2023, granted).
- `US12681982B2` "Systems and methods for efficient multimodal search refinement" (priority 2022, granted).
- `US12602429B2` "Video and audio multimodal searching system" (priority 2023, granted);
  `US12346386B2` "Visual and audio multimodal searching system".
- `US12596744B2` "Multimodal search on wearable smart devices" (priority 2024, granted).
- `US12277635B1`, `US12530398B2` (section 4).

## 13. Foundation model architectures

- `US10452978B2` "Attention-based sequence transduction neural networks" (priority 2017, granted): the Transformer; 14+
  members in the family. `US11556786B2` "Attention-based decoder-only sequence transduction neural networks"
  (priority 2017).
- `US10719761B2` "Mixture of experts neural networks" (priority 2016, granted); `US12518135B2` "Sparse and differentiable
  mixture of experts neural networks"; `US12242948B2` "routing within multitask mixture-of-experts models".
- `US9037464B1` "Computing numeric representations of words in a high-dimensional space" (priority 2013, granted):
  word2vec.
- By inventor: `inventor Noam Shazeer`, `inventor Jeffrey Dean`, `inventor Quoc Le`.

## 14. Marking AI content and verifying provenance

- `US12738282B2` "Verifying the provenance of a digital object using watermarking and embeddings" (GDM, priority 2023,
  granted).
- `US20240320529A1` "Multi-stage watermarking of a digital object generated by a machine learning model" (DeepMind,
  priority 2023).
- The name SynthID does not occur in the patents; this match is an interpretation. Verify with `find <pub> SynthID`.
