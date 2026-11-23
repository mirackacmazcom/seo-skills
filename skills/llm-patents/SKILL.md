---
name: llm-patents
description: Searches an archive of every patent publication in the world whose text mentions large language models (LLM / large language model / 大模型 / 大規模言語モデル) — 157 thousand publications, 100 thousand families; full text for the US, title + abstract for other countries — and answers questions from the patent text. Filterable by company label - OpenAI, Anthropic, Perplexity, Mistral, Google, Microsoft, Meta, Amazon, Apple, NVIDIA, IBM, Baidu, Alibaba, Tencent, ByteDance, Huawei, Samsung and others. Use this skill when the user talks about LLM patents, asks "does OpenAI / Microsoft / Perplexity / Anthropic have a patent for X", asks how a feature of products such as ChatGPT, Claude, Copilot, Gemini or Perplexity is described (plugins, function calling, memory, prompt caching, agents, RAG, citations and source attribution, LLM-generated search results), or asks about the patent basis of LLM-based search or GEO / AI visibility, even if the word "patent" is never used. For Google's classic search/ranking patents use the google-patents skill. Do not write patent numbers, dates or quotes from memory; take them from this skill's database.
---

# LLM patent archive

This skill gathers every patent publication in the world whose text contains an LLM term (BigQuery, Google
Patents Public Data), together with records collected company by company for the LLM companies, into a single
searchable database: 157,165 publications in 99,911 families (November 2026 compilation). For the current counts
and the distribution by company run `python3 scripts/patent.py stats`; details are in `references/background.md`.

The goal is the same as in the `google-patents` skill: answer the user's question based on **what the patent
actually says**. A patent only shows that the company **described a method and sought protection for it**; it
does not show that the product works that way today. Take patent numbers, dates and quotes from the tool every
time.

## How searches run

The archive lives on seoskills.io, so nothing is downloaded. The search tool sends its arguments to
api.seoskills.io and prints the answer. It needs internet access; if it reports that it cannot reach the API,
tell the user that their agent blocks network access and that the SEO Skills MCP server
(https://mcp.seoskills.io/mcp) offers the same tools. Search terms are sent to run the search and are not stored.
If the tool says there were too many searches, wait a minute before the next one.

## Key properties of the archive (always take these into account in the answer)

- **The scope is broad and there is noise.** A publication is included because an LLM term occurs anywhere in its
  text. If the term occurs only in the description (the LLM is mentioned in passing), or if before 2018 there is
  only the abbreviation "LLM"/"大模型" (mostly another meaning, or OCR noise in old scans), the publication is
  labelled `weak-match`. **Use `--core` for general questions**; then only families that deal with LLMs in their
  title/abstract/claims remain.
- **Full text is mostly US.** US publications (and the WO/EP publications collected company by company) have
  claims and description; China (76 thousand), Japan, Korea and the others have an English title + abstract only
  (`abstract-only`). A Chinese patent that mentions LLMs only in its description is not in the archive.
- **The company label is derived from the applicant name** (`--company`, full list in `stats`). Unlabelled
  publications are `(other)`; universities and small companies are here. Subsidiary names may have been missed.
- **Anthropic has almost no inventions of its own.** For the large majority of publications in Anthropic's record
  the original applicant is IBM; IBM assigned them to Anthropic in 2025. They are labelled `acquired` and do not
  describe how Claude works. Say this clearly in any answer about Claude.
- **Part of OpenAI's record is chip patents acquired from Rain Neuromorphics (Rain AI)** (in-memory computing,
  memristors). These are also labelled `acquired`. OpenAI's own product patents start in 2023.
- **Most publications are applications, not grants.** These companies are young; many publications are at the
  `application` stage and their claims may change. Unpublished applications (secret for the first 18 months) do
  not appear at all, so the archive is a lower bound.
- `catalog.md` and `topic-map.md` cover only the company layer (10 LLM companies); for big tech and other
  applicants use `search --company`.

## Search tool

The only tool is `scripts/patent.py` (Python 3, no extra packages needed). Run it from inside the skill folder:

```bash
python3 scripts/patent.py stats                                   # counts and distribution by company
python3 scripts/patent.py search language model plugin api --core # --core: drop weak matches and acquired ones
python3 scripts/patent.py search search results summary --company microsoft --core --granted
python3 scripts/patent.py search search engine citation --company perplexity
python3 scripts/patent.py search prompt cache --company openai --core
python3 scripts/patent.py search '"generative response engine"' --in claims --granted
python3 scripts/patent.py show US11922144B1                       # bibliographic data + abstract + first independent claim
python3 scripts/patent.py claims US11922144B1 --independent       # independent claims
python3 scripts/patent.py passages US11922144B1 manifest web api  # relevant description paragraphs, numbered [¶n]
python3 scripts/patent.py find US11922144B1 plugin                # does the phrase occur in this patent
python3 scripts/patent.py family US11922144B1                     # other publications in the same family
python3 scripts/patent.py inventor Andrey Mishchenko              # by inventor
python3 scripts/patent.py topics                                  # topic labels derived from CPC
```

What you need to know:

- **`--company`** values: LLM companies `openai`, `anthropic`, `perplexity`, `mistral`, `cohere`, `ai21`,
  `character`, `stability`, `deepseek`, `huggingface`, `zhipu`, `moonshot`; big tech `google`, `microsoft`,
  `meta`, `amazon`, `apple`, `nvidia`, `ibm`, `salesforce`, `adobe`, `oracle`, `sap`, `baidu`, `alibaba`,
  `tencent`, `bytedance`, `huawei`, `samsung`, `iflytek`, `inspur` and others (full list and counts: `stats`).
  **`--core`** drops weak matches and acquired publications; use it in general searches and for questions like
  "what has company X patented around LLMs".
- **`search` works with English terms**, and words are reduced to their stems. Search with two or three
  distinctive terms, not with a sentence. Patents almost never name products: instead of "ChatGPT" use
  "generative response engine", "conversational interface"; instead of "plugin" use "external API ... manifest";
  "Claude" never appears. See `references/topic-map.md` for suitable terms.
- The default scope is title + abstract + claims; when there are few results the tool widens to the description,
  then to OR, and says so. The options `--in title | abstract | claims | description | all`, `--strict`,
  `--granted`, `--from YEAR`, `--to YEAR`, `--topic label`, `--ai`, `--limit N` and `--width 0` work as in
  `google-patents`.
- **Results are per family.** Continuations share the description but have different claims; for claim-level
  evidence list the members with `family <publication>` and run `claims` on the relevant member.
- `passages` and `show --section description` use the same `[¶n]` numbers; give that number when quoting.
- Before saying that something does not occur, verify with `find` or `search <term> --in all --strict`.
- Labels: `granted` / `application` (US), `AI`, `acquired`, `weak-match`, `abstract-only`, `company:<name>`.

## How to work and how to build the answer

The rules of the `google-patents` skill apply as they are: first translate the concept into patent language,
search broadly and then go deep, distinguish claims from description, check the date and grant status, and say so
if you found nothing. Answer in the user's language, briefly (150–300 words), with every claim sourced by number +
title + priority year + `Claim n` or `[¶n]`, and with a Google Patents link. Separate what the patent says from
your own interpretation: do not say "OpenAI does X in ChatGPT"; say "OpenAI has a patent application describing
X; it describes it as follows". Matching a patent to a product name (e.g. "this is the ChatGPT plugins patent") is
your inference unless the text says so; present it as such.

For SEO/GEO questions (do LLMs choose sources, how do they cite, how do they use search) look especially at
Perplexity's search patents and at OpenAI's "generative response engine" / search / file search applications. If
a comparison with Google's AI Overview patents is requested, also use the `google-patents` skill and state
separately which information comes from which archive.

## Reference files

- `references/topic-map.md` — topic → patents and suggested search terms. Look at the relevant section before you
  start searching; open and verify the listed patents with the tool.
- `references/catalog.md` — every patent family by company (representative number, priority year, grant /
  acquisition status). For questions like "which patents does company X have", look here first.
- `references/background.md` — how the archive was compiled, its scope and its limits.
