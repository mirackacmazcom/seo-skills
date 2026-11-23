# Topic map: product/concept → patents and search terms

Patents almost never name products. This table translates common concepts into patent language. The numbers
listed are starting points; open and verify each one with `show` / `claims` / `passages`. For the full list see
`catalog.md`.

## Contents

1. LLM-based search and citations (GEO / AI visibility)
2. The ChatGPT chat interface and the "generative response engine"
3. Plugins, function calling, APIs, structured output
4. Memory, personalisation, custom instructions, context summarisation
5. Agents and computer use
6. Reasoning (chain-of-thought) and alignment
7. Code (Codex, Code Interpreter, Canvas)
8. Image, video, audio (DALL·E, Sora, Whisper, Stability)
9. Efficiency: prompt caching, distillation, KV cache
10. Privacy and security
11. Hardware and data centres (OpenAI chips, Rain AI)
12. Anthropic

## 1. LLM-based search and citations

Terms: `augmented search`, `search engine`, `retrieval augmented`, `citation`, `source`, `file search`,
`document intelligence`, `embedding`.

- Perplexity `US20250291863A1` Augmented search engine; `US20250363097A1` Compact search client for augmented search.
- Mistral `US12645742B1` RAG-based product assistant; `US12651113B1` Document intelligence system.
- OpenAI `US20260236435A1` File search tool integrated with virtual assistant; `US12073299B2` text/code embeddings
  with contrastive pre-training (the basis of semantic search).
- Cohere `US20260228531A1` dataset filtering.

## 2. The ChatGPT chat interface

Terms: `generative response engine` (the phrase OpenAI uses for ChatGPT), `assistant message`,
`conversational interface`, `overlay application`.

- `US12164548B1` Adaptive UI for rich output rendering of assistant messages
- `US20250348183A1` / `US20250348196A1` Overlay application (the desktop app)
- `US12699964B1` Project management for generative response engine contexts (Projects)
- `US12706918B1` Seamless consumer integration of access to a generative response engine
- `US20260093899A1` Collaboration on an asset (Canvas-like co-editing)
- `US20250274411A1` User and model reactions

## 3. Plugins, function calling, APIs

Terms: `external API manifest`, `schema`, `function call`, `structured output`, `assistants API`.

- `US11922144B1`, `US12124823B2`, `US12547480B2` Schema-based integration of external APIs (plugins)
- `US12554519B2` Virtual assistants API; `US12591766B1` API with state management
- `US20260127368A1` Enforcing structured output
- Mistral `US12670045B1` Code implemented tool calls

## 4. Memory and personalisation

Terms: `personalized responses`, `selective learning`, `custom instructions`, `summarizing context`.

- `US20250200361A1` Selective learning of information for personalized responses (memory)
- `US12430518B2` Custom model instructions
- `US12675519B1` Summarizing context and conditioning a LLM
- `US12400074B1` Stateful pretrained transformers
- Character.AI `US12481835B1` Character turn summaries

## 5. Agents

Terms: `agent`, `long running task`, `shared workspace`, `computer using agent`, `automatic interface actions`.

- `US20260203082A1` Computer using agent with hybrid human control (Operator)
- `US12346664B1` Interactions during a long running task; `US12405822B1` Multi-agent shared workspace
- `US20250373574A1` Interactions between assistant-type agents; `US12518109B1` Language model automations
- `US11887367B1` Automatic interface actions
- Anthropic `US12387036B1` Multimodal agent for image-text interface automation (Anthropic's only family of its own)
- Perplexity `US20260219957A1` General agent orchestration

## 6. Reasoning and alignment

- `US20260073295A1` Generative response engine using chain-of-thought reasoning (o1)
- `US20260161958A1` Deliberative alignment of language models to comply with policies
- `US12671713B1` Agent reinforcement fine-tuning, multi-layer security
- `US20240362421A1` Language model-based content classification (moderation)

## 7. Code

- `US12008341B2`, `US20240402999A1` Code generation with models trained on code (Codex)
- `US12498947B2` Interpreting computer code with a multimodal model (Code Interpreter)
- `US12675262B1` Online development environment

## 8. Image, video, audio

- `US11922550B1` Hierarchical text-conditional image generation (DALL·E 2); `US11983806B1` image generation
- `US20250259423A1` Model image generation using recaptioned images (DALL·E 3)
- `WO2025174789A1` Generative video engine; `US20250259362A1` prompt editor; `US20250259361A1` storyboard GUI (Sora)
- `US12079587B1` Multi-task automatic speech recognition (Whisper)
- Stability AI: 3D, video, audio and clothing generation (see the catalog)

## 9. Efficiency

- `US12596764B1` Prompt caching; `US12619603B2` Distilled generative response engine
- Character.AI `US12682211B2` Optimizing key value cache for LLM inference

## 10. Privacy and security

- `US12712833B1` Private inference (encrypted chat); `US12387007B2` PII scrubber

## 11. Hardware

Terms: `compute-in-memory`, `matrix multiplication`, `accelerator`, `cooling`, `chiplet`.
OpenAI's own applications (2024+) are mixed with those acquired from Rain Neuromorphics (`acquired`);
separate them with `--core`.

## 12. Anthropic

Its own family is only `US12387036B1` (and the family members `US20260195524A1` and the JP/KR/CN/WO
counterparts). The other 17 families were acquired from IBM in 2025: transformer inference acceleration, speech
recognition, adversarial attack detection, document extraction, bias mitigation. They do not describe how Claude
works.
