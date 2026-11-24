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
api.seoskills.io and prints the answer. It needs internet access. If it reports that it cannot reach the API, run the command
once more; if it still fails, tell the user that their agent seems to block network access and that the SEO
Skills MCP server (https://mcp.seoskills.io/mcp, set-up at https://seoskills.io/install/) offers the same tools. Search terms are sent only to run the search. They are not logged or linked to you; results are cached for up to an hour so repeat searches are fast.
If the tool says there were too many searches, wait a minute before the next one.

## Key properties of the archive (always take these into account in the answer)

- **The scope is broad and there is noise.** A publication is included because an LLM term occurs anywhere in its
  text. If the term occurs only in the description (the LLM is mentioned in passing), or if before 2018 there is
  only the abbreviation "LLM"/"大模型" (mostly another meaning, or OCR noise in old scans), the publication is
  labelled `weak-match`. **Use `--core` for general questions**; then only families that deal with LLMs in their
  title/abstract/claims remain.
- **Full text is mostly US.** US publications (and the WO/EP publications collected company by company) have
  claims and description; China (82 thousand), Japan, Korea and the others have an English title + abstract only
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
python3 scripts/patent.py search search engine --company perplexity
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
  `tencent`, `bytedance`, `huawei`, `samsung`, `iflytek`, `inspur` and others (counts for the 40 largest groups: `stats`).
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

## Answer settings

The user decides how the answer looks. Three things can be set:

| Setting | Default | The user can ask for |
|---|---|---|
| Language | The language of the user's latest message | A fixed language: "always answer in Dutch" |
| Length | `standard` | `brief` or `detailed` |
| Sources | `on`: quotes, source names, dates and links | `off`: no quotes, links, numbered citations or source list |

What each length contains:

| | `brief` | `standard` (default) | `detailed` |
|---|---|---|---|
| Size | Two or three sentences, at most 60 words | About 120–250 words | Up to about 600 words |
| Sources shown | The one strongest | The one to three the answer turns on | Up to six, grouped by theme |
| Quotes | None needed | One short quote where the exact wording decides | A short quote per source |
| Layout | Plain sentences | Verdict sentence, a few short bullets | Short headings or bold labels are fine |
| What the source cannot show | Inside a sentence, only if it changes the verdict | One sentence | One short paragraph |
| Next step (only when the rule below asks for one) | A clause | One or two sentences | One or two sentences, plus what the sources suggest when read together |

These sizes, and the numbers of sources, quotes and bullets, replace any other count in this file. The line of
links at the end does not count toward the size. A busy reader wants the verdict and the decisive source,
not everything you read: leave side findings out and offer them in one closing line ("I can also go into X").

Where a setting comes from, strongest first:

1. What the user says in the conversation.
2. A line that starts with `SEO Skills:` in your standing instructions (CLAUDE.md, AGENTS.md, project or custom
   instructions), for example `SEO Skills: detailed answers, sources off, always answer in Dutch`.
3. The defaults above.

People say this in their own words, in any language. Map them like this, and change only what was asked for:

- "short answers", "just the summary", "in one line", "kısa tut" → `brief`
- "shorter", "a bit shorter" about an answer you just gave → about half its length, same sources
- "more detail", "the long version", "every source", "full breakdown" → `detailed`
- "no links" → leave out the URLs only; names, numbers and quotes stay
- "skip the sources", "without quotes", "no citations", "kaynak gösterme" → sources `off`
- "show me the sources", "where does that come from" → sources `on`

A request about one answer ("give me the long version of that", "shorten this") applies to that answer. A request
worded as a preference ("keep it short", "no sources please", "from now on…") holds for the rest of the
conversation. If you cannot tell, treat it as a preference; the user can change it back in a word.

How the settings combine:

- Sources `off`, at any length: say what the answer rests on in plain words inside the sentence, and keep the one
  handle the user needs to look it up: a person and year ("John Mueller said in 2022"), a page name ("Google's
  spam policy"), a patent number ("a 2012 Google patent, US9031929B1"), a field name (`PerDocData.hostAge`).
  Quotes, links, claim and paragraph numbers, platforms and source lists are left out.
- `brief` with sources on: the answer plus the one strongest source (name, date, link). If the verdict needs two
  facts from two pages, name both in the sentence and link the one that carries the verdict.
- When the user changes a setting right after an answer, rewrite that answer from what you already found. Do not
  search again unless the new version needs something you have not read.

The settings are the same for every SEO Skills skill. No setting changes these rules:

- Take every fact, number, date and quote from the search tool, never from memory. With sources off you still
  search first; you only leave the citations out, and you give them as soon as the user asks.
- Keep what the source says apart from your own inference.
- If your environment limits verbatim quotation (for example one short quote per answer), quote the single most
  decisive sentence and report the rest in your own words, keeping the modal verbs ("may", "can", "in some
  implementations") and the locator (field name, claim or paragraph number, section, date). Never write an
  approximate quote.
- Say once what the source cannot show, whenever that changes the conclusion: this archive records what was
  written or said, not how much weight it carries in ranking today, and older material may be outdated. Do not
  repeat the caveat in every bullet.

**Language.** Answer in the language the user writes in, even though this skill, the tool output and the sources
are in English. Search with English terms. Translate ordinary terms; keep quotes, titles, field names and patent
numbers in the original, and add a short gloss in the user's language only where a quote would not be clear
without it. Long titles may be shortened once the number or link is given.

**Close with the next step.** People usually ask because they are about to change something. Close with practical
advice when the user states a plan or a goal ("I'm planning to…", "we want…", "my client wants…", "should I…",
"is it worth…") or asks whether something affects ranking or visibility. Mark it as your suggestion, apart from
what the source says. Build it from what the tool returned in this conversation plus ordinary professional
judgement; do not bring in facts about Google from memory. Skip it when it would only repeat your first sentence,
and when the user only asks what a source says. If this archive is silent on the practical part of the question,
say so in one sentence and name where the answer would be (Google's official documentation, or another SEO Skills
skill) instead of forcing advice out of it. If that other skill is installed, use it: one or two searches there
for the practical part, reported under its own label.

**Several SEO Skills skills installed.** Pick by what the question needs: a rule, threshold or recommendation →
`google-search-docs`; who said what and when → `google-staff-statements`; what data Google stores →
`google-leak`; how a method is described → `google-patents` (search), `google-ai-patents` (AI Overviews, AI Mode,
Gemini) or `llm-patents` (OpenAI, Perplexity and other companies); Maps and local ranking → `google-maps-ranking`.
For "what should I do", start with the official documentation and add another source only if it adds something
the documentation lacks. A combined answer keeps one length setting, with one bold label per kind of source, and
never presents one kind of source as proof of another.

Do not list the settings in every answer. Mention them in one line only when it helps: the user asks what can be
changed, or seems unhappy with the length or the citations.

**If a search fails.** The script retries a dropped connection once by itself. If it still fails, run the command
once more after a few seconds before you conclude that your environment has no network access.

## How to work and how to build the answer

1. **Translate the concept into patent language.** Patents say "generative response engine", "language model
   program" or "retrieval" where the user says "ChatGPT search" or "RAG". `references/topic-map.md` lists the terms.
2. **Search broadly, then go deep.** `search` finds candidates; base the answer on `claims`, `passages` or `show`
   output for the two or three most relevant patents, not on the search snippet.
3. **Distinguish claims from description.** Claims are what is protected; the description is full of examples and
   options ("in some implementations"). Say which one you are quoting.
4. **Check the date and status.** An application (A1) is a filing, not a granted patent. Give the priority year.
5. **Say so if you found nothing.** List the terms you tried. Absence from the archive does not prove no patent exists.

Give the short answer first, then the evidence: one bullet per patent with number + title + priority year, what it
says, and where (`Claim n` or `[¶n]`), then the Google Patents links. Quote exactly and keep quotes short. When
the whole answer rests on one patent family, say so. A phrase with punctuation (`"llms.txt"`) is split into words
by the search, so check a "this term never occurs" finding with `find <publication> "<phrase>"` on the patents you
cite and limit the claim to what you checked. Separate what the patent says from
your own interpretation: do not say "OpenAI does X in ChatGPT"; say "OpenAI has a patent application describing
X; it describes it as follows". Matching a patent to a product name (e.g. "this is the ChatGPT plugins patent") is
your inference unless the text says so; present it as such.

For SEO/GEO questions (do LLMs choose sources, how do they cite, how do they use search) look especially at
Perplexity's search patent and at OpenAI's "generative response engine" patent (`US12619603B2`); OpenAI's "file
search" applications are about files a user uploads, not web sources. If
a comparison with Google's AI Overview patents is requested, also use the `google-ai-patents` skill and state
separately which information comes from which archive.

## Reference files

- `references/topic-map.md` — topic → patents and suggested search terms. Look at the relevant section before you
  start searching; open and verify the listed patents with the tool.
- `references/catalog.md` — every patent family by company (representative number, priority year, grant /
  acquisition status). For questions like "which patents does company X have", look here first.
- `references/background.md` — how the archive was compiled, its scope and its limits.
