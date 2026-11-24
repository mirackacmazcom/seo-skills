---
name: google-ai-patents
description: Searches an archive of the AI patents of Google and the Alphabet companies (DeepMind/GDM, Waymo, Verily, X, Intrinsic, Isomorphic, Fitbit…) — 82,806 publications, 14,495 families, all countries, full text for 99.9% of families — and answers questions from the patent text. Use it for AI Overviews and generative search, AI Mode / conversational search, query fan-out (splitting a query into sub-queries), source and passage selection in generative answers, citations, factuality / hallucination, training LLMs with search results, embeddings and dense retrieval, model architectures such as Gemini / Transformer / MoE, Lens and multimodal search, assistants and agents, SynthID watermarking, and speech and image recognition. Use it when the user asks things like "how does Google build AI Overviews", "which sources does Google pick for a generative answer", "is there a patent for AI Mode / query fan-out", "Gemini's or DeepMind's patent on X", or "what do Google patents say about GEO / AI visibility", even if the word "patent" never comes up. For classic search / ranking / PageRank / site quality patents use the google-patents skill; for LLM companies other than Google use the llm-patents skill. Do not write patent numbers, dates or quotes from memory; take them from this skill's database.
---

# Google AI patent archive

This skill gathers the AI-related patent publications of Google and the Alphabet companies into a single searchable
database: 82,806 publications, 14,495 patent families, all countries. Claims and description are stored in full for
14,488 families (US publications from BigQuery; ~1,000 families without a US member from Google Patents pages, 75 of
them Google's English machine translation). Priority dates run from 1986 to 2026; the newest publication is from
17 September 2026.

The scope is deliberately broad: besides machine learning, neural networks, language and speech, image recognition,
robotics, autonomous vehicles, quantum and health AI, it also contains **~2,750 search-related families** and **~170
families related to AI Overviews / generative search**. SEO and AI-visibility questions mostly fall into these last two
groups; you can narrow a search to them with `--search` or `--ai`.

The goal: answer the user's question based on **what the patent actually says**. A patent only shows that Google
**described a method and asked for protection** for it; it does not show that the method is used in products. Take
patent numbers, dates and quotes from the tool every time, not from memory.

## How searches run

The archive lives on seoskills.io, so nothing is downloaded. The search tool sends its arguments to
api.seoskills.io and prints the answer. It needs internet access. If it reports that it cannot reach the API, run the command
once more; if it still fails, tell the user that their agent seems to block network access and that the SEO
Skills MCP server (https://mcp.seoskills.io/mcp, set-up at https://seoskills.io/install/) offers the same tools. Search terms are sent only to run the search. They are not logged or linked to you; results are cached for up to an hour so repeat searches are fast.
If the tool says there were too many searches, wait a minute before the next one. If it says the daily limit is
reached (2,000 searches a day), tell the user; it resets at 00:00 UTC.

## Search tool

The only tool is `scripts/patent.py` (Python 3, no extra packages needed). Run it from inside the skill folder:

```bash
python3 scripts/patent.py search generative summary search results --ai     # flagged AI Overview / generative search
python3 scripts/patent.py search sub-queries decomposition --search --from 2023   # search-related, priority 2023+
python3 scripts/patent.py search mixture of experts --group deepmind          # by company group (google, deepmind, waymo …)
python3 scripts/patent.py search '"synthetic queries"' --in claims --granted  # claims only, granted US patents
python3 scripts/patent.py show US11769017B1                    # bibliographic data + abstract + first independent claim + section headings
python3 scripts/patent.py claims US11769017B1 --independent    # independent claims (the protected core)
python3 scripts/patent.py passages US11769017B1 linkify verification   # most relevant description paragraphs, numbered [¶n]
python3 scripts/patent.py find US11769017B1 "search result"    # does the phrase occur in this patent; in which claims and paragraphs
python3 scripts/patent.py family US11769017B1                  # publications in the same family (continuations, WO/EP)
python3 scripts/patent.py inventor Noam Shazeer                # an inventor's patents
python3 scripts/patent.py topics                               # topic labels; topics <label> lists families in that topic
python3 scripts/patent.py groups                               # company groups and family counts
python3 scripts/patent.py stats                                # database summary
```

What you need to know:

- **`search` works with English terms.** Words are stemmed (`summary` and `summaries` are the same). For an exact
  phrase, wrap the double quotes in single quotes: `'"search result documents"'`. You can write `OR` / `NOT`; since the
  precedence is NOT > AND > OR, group alternatives with parentheses: `'(hallucination OR uncertainty) "language model"'`.
- **Search with two or three distinctive terms, not a sentence.** Patents do not use product names: instead of
  "AI Overview" use "natural language based summary" / "generative summary", instead of "fan-out" use "sub-queries" /
  "synthetic queries", instead of "AI Mode" use "stateful chat" / "search session", instead of "Lens" use
  "multimodal query" / "visual search". Check `references/topic-map.md` first for the right terms.
- **The default scope is title + abstract + claims.** If there are few results, the tool first widens to the
  description text, then joins the terms with OR, and says so; widened results come after a divider line and are often
  noise. If you choose the scope yourself (`--in title|abstract|claims|description|all`) no widening happens; to turn
  widening off in the default scope, use `--strict`. (`--core` has nothing to do with widening; it only removes weak
  matches.)
- **Filters:** `--search` (search-related families), `--ai` (flagged AI Overview / generative search), `--group <name>`
  (`google` = the applicant is Google itself; `deepmind`, `waymo`, `verily`, `x-development`, `intrinsic`, `fitbit`,
  `isomorphic-labs` …), `--granted`, `--from YEAR` / `--to YEAR` (priority), `--topic <label>`, `--core` (remove weak
  matches), `--limit N`, `--width 0` (no snippets).
- **The archive also covers general AI.** For an SEO/search question, if you do not use `--search`, robotics, speech
  recognition or chip patents may also come up; tell them apart by title.
- **Results are per family.** The application, grant, continuations and WO/EP/CN publications of the same invention
  are collected in one line. Continuations have **the same description but different claims**; for claim-level
  evidence, list the members with `family` and run `claims` on the relevant member. Example: the AI Overview family has
  four separate US grants (`US11769017B1`, `US11886828B1`, `US11900068B1`, `US12118325B2`); `family` also shows the
  separately recorded families with the same title (`US20250005303A1`, `WO2024145537A1`).
- **`show` is short.** Do not load the whole description; pull the relevant paragraphs with `passages <pub> <terms>`
  (`--limit`, `--max 0`, `--around N`). Paragraph numbers are consistent between `passages` and
  `show --section description`, but **only within that publication**: the same paragraph can shift by a number or two
  across family members. When you cite `[¶n]`, also name the publication.
- **Give the number of the family member whose claim you quote.** Continuations have different claims; do not
  attribute the representative's claim to another member.
- **Texts from Google Patents pages** (`stats`: "Google Patents page") sometimes come in split: in a few machine
  translations the claims are unnumbered and `claims` may show 0 claims; then read them with `show --section claims`.
- **Before saying something does not occur in a patent, verify it with `find <pub> <phrase>`.**
- When chaining several commands, use `echo '---'` as a separator (zsh treats an `echo ===` line as a command).
- Publication numbers can be written flexibly: `US11769017B1`, `US-11769017-B1`, `11769017`.
- Labels: `granted` / `application` (US), `generative-search`, `acquired`, company group (`deepmind`, `waymo` …),
  `weak-match`, `abstract-only`, `machine-translation`.

## How to work

1. **Translate the concept into patent language.** `references/topic-map.md` maps AI search and SEO concepts to patent
   terms and verified starting patents. The file is long; find the relevant heading in its table of contents and read
   only that section.
2. **Search broadly, then go deep.** Find candidates with `search`, open the two or three most relevant patents with
   `show`, and read the part relevant to the question with `claims` and `passages`. Re-verify the patents in the map
   with the tool.
3. **Tell the claims from the description.** The claims are the legally protected definition; the description is full
   of options that begin with "in some implementations". When you say something "is in the patent", say which of the
   two it is in.
4. **Check the context.** Some titles are misleading: for example, "Providing generative answers including citations to
   source documents" (`US12346366B2`) is about documents in cloud storage (Drive), not web search. Before tying a patent
   to web search, check that phrases such as "search result documents", "search engine" or "web" occur in the claim.
5. **Date and status.** The priority date shows how old the idea is. A publication labelled `application` has not been
   granted, and its claims can change. `acquired` and subsidiary patents may not come from Google's own search team.
   Most applications filed after 2025 have not been published yet, so they are not in the archive.
6. **If you cannot find it, say so.** List the terms you tried and show the closest real patents. Something missing
   from the archive does not prove that Google has no patent on it (`references/background.md`).

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

## How to build the answer

Answer in the user's language. Leave patent titles and quotes in their original English; if needed, add a short
explanation in the user's language next to them. Give the short answer first, then show the evidence.

- Cite the patent by number, title and priority year: `US11769017B1` "Generative summaries for search results"
  (priority 2022).
- Give the location of the quote: `Claim 1` or `[¶42]`.
- Quote exactly, without changing the words, and keep it short; skip the irrelevant part with `[...]`. Keep the modal
  verbs ("can", "may", "in some implementations") as they are; they mark an option, not a rule.
- Add the Google Patents link.
- State if the patent is an `application`, `acquired`, from a subsidiary, a `machine-translation` or a `weak-match`.

**Separate what the patent says from your own interpretation.** This is the most important rule of this skill:

- Do not say "Google uses X"; say "Google has a patent that describes X; it explains it like this".
- Product names almost never appear in patents. Matching "this is the AI Overview / AI Mode patent" is your
  interpretation or the SEO community's; present it as such.
- If SEO/GEO advice is asked for, first state the mechanism the patent describes, then give the advice in a
  separate closing sentence marked as your suggestion (see "Close with the next step" above).
- Numbers and thresholds in the description are almost always examples; say whether they are part of a claim or not.
- A patent cannot diagnose the user's own site.

**Keep it short.** Default format: the direct answer in the first sentence; then short bullets, as many as the length setting allows
(each one a patent, what it says and where); a one-sentence note on limits; the links. Length follows the answer
settings. Most questions are answered with 6–10 commands; read in full only the patents you will cite. Paragraphs in
these patents are long: `passages --max 1200` is usually enough, and paragraph numbers differ between members of a
family, so cite the number together with the publication you read it in.

### Example

Question: "Is there a patent showing that Google splits the query into sub-queries in AI Overviews?"

> Yes, there are several; the most direct is `US20250348485A1` "Generative model based decomposition of input query into
> sub-queries and generation of comprehensive response based on responses to sub-queries" (priority 2024, application).
>
> - Claim 1: a generative model processes the input query and determines "a plurality of sub-queries" and the tools to
>   use for each sub-query; a comprehensive response is generated from the responses to the sub-queries, then checked
>   with a "critique response" and refined if it does not satisfy the query.
> - `US20240289407A1` "Search with stateful chat" (priority 2023): generates "synthetic queries" from the query and the
>   user context, and selects search result documents responsive to both the original and the synthetic queries
>   (Claim 1).
>
> The patents describe this method; they do not say it is used this way in AI Overviews or AI Mode. The "fan-out"
> match is an interpretation. Sources: https://patents.google.com/patent/US20250348485A1/en ·
> https://patents.google.com/patent/US20240289407A1/en

## Reference files

- `references/topic-map.md` — AI search and SEO concept → patent terms → verified patents (14 topics).
- `references/background.md` — the archive's scope, sources and limits, labels, company groups, and how to read a
  patent.

Related skills: `google-patents` for classic search/ranking patents; `google-leak` for the data fields in the Google
leak; `google-search-docs` for Google's official documentation; `llm-patents` for other LLM companies such as OpenAI,
Anthropic and Perplexity. When using them together, say separately which information comes from which source.
