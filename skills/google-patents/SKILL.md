---
name: google-patents
description: Searches an archive of Google's patents on search, ranking, crawling, indexing, site quality, links/PageRank, user behaviour, query understanding, web performance and AI/generative search — 54,101 publications in 10,491 families, full text — and answers questions from the patent text itself. Use this skill when the user mentions Google patents, a patent number (US…), an inventor (e.g. Navneet Panda), or concepts such as PageRank, Reasonable Surfer, Panda, site quality score, Navboost, TrustRank, Agent Rank, historical data, answer passages, knowledge panels or generative summaries. Also use it for questions like "does Google have a patent for X", "how does Google calculate X", "what does the patent say", "is there a patent behind this SEO claim", and whenever an SEO claim needs to be checked against a primary source, even if the user never uses the word "patent". Do not write patent numbers, dates or quotes from memory; always take them from this skill's database. For Google's AI patents (AI Overviews, AI Mode, Gemini, DeepMind, query fan-out) use google-ai-patents; for other companies' LLM patents use llm-patents.
---

# Google search patents archive

This skill gathers Google's search-related patent publications (including those assigned to Google or held by
affiliated companies) into a single searchable database: 54,101 publications in 10,491 patent families; the claims
and description of 26,776 publications are stored as full text. Priority dates run from 1961 to 2026; most families are from the 2000s onwards.

The goal: answer the user's question based on **what the patent actually says**. In the SEO world patents are very
often passed on as "Google does this", whereas a patent only shows that Google **described a method and sought
protection for it**. The value of this skill is that it can verify a claim at its primary source, with the number
and the paragraph. So take patent numbers, dates and quotes from the search tool every time, not from memory:
patent numbers recalled from memory are often wrong.

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
python3 scripts/patent.py search site quality score            # full-text search, one result per family
python3 scripts/patent.py search '"anchor text"' link --in claims --granted   # claims only, granted patents
python3 scripts/patent.py search generative summary --ai --from 2022          # AI-flagged, priority 2022+
python3 scripts/patent.py show US9031929B1                     # bibliographic data + abstract + first independent claim + section headings
python3 scripts/patent.py claims US9031929B1 --independent     # independent claims (the protected core)
python3 scripts/patent.py passages US8661029B1 click viewing time   # the most relevant description paragraphs, numbered [¶n]
python3 scripts/patent.py find US7346839B2 sandbox              # does the phrase occur in this patent; in which claims and paragraphs
python3 scripts/patent.py show US9031929B1 --section description --full   # the whole description, numbered [¶n]
python3 scripts/patent.py family US6285999                     # other publications in the same family (continuations)
python3 scripts/patent.py inventor Navneet Panda               # an inventor's patents
python3 scripts/patent.py topics                               # topic tags; topics <tag> lists the patents in that topic
python3 scripts/patent.py stats                                # database summary
```

What you need to know:

- **`search` works with English terms** (the patent texts are in English). Words are reduced to their stem
  (`rank`, `ranking`, `ranked` count as the same), so wildcards (`*`) are not needed; if you use one, wrap it in
  single quotes so the shell does not complain (`'prerender*'`). For an exact phrase, wrap double quotes in single
  quotes: `'"search result"'`. Write `OR` / `NOT` to build your own logic.
- **Search with two or three distinctive terms, not a sentence.** `search click duration ranking` works well;
  `search how google uses click-through dwell time for ranking` does not. Patents do not use SEO jargon ("viewing
  time" / "click duration" instead of "dwell time", "answer passage" instead of "featured snippet"); check the topic
  map first for the right terms.
- **The default scope is title + abstract + claims.** Long descriptions mention almost every term somewhere, so
  full-text search is noisy. If the narrow scope finds fewer than five families, the tool first widens to the
  description text, and if there are still few, joins the terms with OR, and says so at the top of the output;
  exact matches are always on top. To choose the scope yourself use `--in title | abstract | claims | description |
  all`; to turn widening off use `--strict`.
- **Filters:** `--granted` (granted US patents), `--from YEAR` / `--to YEAR` (priority year), `--topic tag`,
  `--ai`, `--perf`, `--core`, `--limit N`. `--width 0` hides snippets. `--topic` tags are derived from the patent
  class (CPC); they can miss related patents with a different class, so do not rely on them alone.
- **`--core` reduces noise.** The archive was kept inclusive, so it also contains publications only loosely related
  to search (they appear in the output with tags such as `weak-match` and `affiliate:waymo`). Use `--core` for
  general SEO questions; remove it if you find nothing. `--core` does not drop advertising or database patents;
  tell those apart by their title.
- **Results are per family.** An invention's application, grant and continuations are collapsed into one line; the
  publication shown is the family's representative (the first granted US publication). Continuation patents in the
  same family **share the same description but have different claims**; each continuation protects another aspect
  of the invention. If you need claim-level evidence, list the members with `family <publication>` and run
  `claims <member>` with the relevant member's number. `family` also shows publications that carry the same title
  but are recorded under a separate family number.
- **`show` is short by default** (a description can be 30–200 thousand characters). Instead of loading the whole
  description into context, pull the relevant paragraphs with `passages <publication> <terms>`. `passages` options:
  `--limit N` (how many paragraphs, default 6), `--max N` (characters per paragraph; `--max 0` for no limit),
  `--around N` (also show neighbouring paragraphs). If you give a quoted phrase, only paragraphs containing that
  phrase are returned.
- **Paragraph numbers are consistent.** `passages` and `show --section description` use the same `[¶n]` numbers;
  give this number when you quote. `show --section` values: `abstract`, `claims`, `description`, `all`; add `--full`
  for the whole description. For a single claim use `claims <publication> --no N`.
- **The text can be imperfect.** The text of older patents comes from scanned documents and can contain OCR errors
  (such as `coffesponding`); some non-US publications are machine translations. Quote the text as it is, and point
  out a defect if it affects the meaning; do not silently correct it.
- **Verify before saying something is not in a patent.** `find <publication> <phrase>` reports how many times and
  where the phrase occurs in the title, abstract, claims and description, and says explicitly if it does not occur
  at all. Base a statement such as "the word sandbox does not appear in the patent" on this. To say that a term
  occurs nowhere in the archive, use `search <term> --in all --strict`.
- Publication numbers can be written flexibly: `US9031929B1`, `US-9031929-B1`, `9031929`.
- Tags: `granted` / `application` (US), `AI`, `performance`, `acquired` (the original owner was not Google),
  `abstract-only` (no full text), `weak-match`, `affiliate:<group>`.

## How to work

1. **Translate the concept into patent language.** The user asks in SEO terms such as "clicks", "authority",
   "sandbox" or "AI Overview"; patents use phrases like "implicit user feedback", "document inception date" or
   "natural language based summary" and almost never name products (Panda, Penguin, Navboost, AI Overview). Look at
   `references/topic-map.md` first: it shows which patents and which search terms common SEO concepts correspond to.
   The file is long; find the relevant heading in its table of contents and read only that section.
2. **Search broadly, then go deep.** Find candidates with `search` (try several different terms and the `--in`
   option), open the two or three most relevant patents with `show`, then read the part relevant to the question
   with `claims` and `passages`. Do not generalise from a single patent; patents that address the same topic in
   different years often complement each other.
3. **Tell claims and description apart.** The claims are the legally protected definition of the invention and are
   written in precise language. The description is full of examples, options and possibilities beginning with "in
   some implementations"; an example there is not a required part of the invention. When you say something "is in
   the patent", say which of the two it is in.
4. **Check the date and status.** The priority date shows when the invention was made; a patent with a 2004
   priority describes 2004 thinking. A publication tagged `application` has not been granted yet and its claims may
   change. An `acquired` patent was not developed at Google.
5. **If you cannot find it, say so and state what you searched for.** List the terms you tried and show the closest
   real patents, if any. Something not being in the archive does not prove that Google has no patent on the topic
   (see `references/background.md` for the limits of the coverage); but attributing to a patent something that is
   not in the archive misleads the user.

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

Language, length and citations follow the answer settings above. Give the short answer to the question first, then show the
evidence.

Tie every claim to its source:

- Cite the patent with its number, title and priority year: `US9031929B1` "Site quality score" (priority 2012).
- Give the location of the quote: `Claim 1` for a claim, and the paragraph number the tool shows, `[¶42]`, for the
  description.
- Quote the patent text in quotation marks without changing its words; keep quotes short and relevant to the
  question. Keep modal verbs ("may", "can", "in some implementations") as they are; they are part of the meaning.
  You may skip an irrelevant part of a long sentence with `[...]`; do not make a cut that changes the meaning.
- Add the Google Patents link the tool gives, so the user can open the source themselves.
- If the publication is an `application`, `acquired`, `abstract-only` or comes from a machine translation, say so.

**Separate what the patent says from your own interpretation.** This is the most important rule of this skill:

- A patent shows that Google **described a method and sought protection for it**. It does **not** show that the
  method is used in search, is still used, or what weight it has; companies patent many ideas they never use.
  Instead of "Google uses X", say "Google has a patent that describes X; it explains it as follows".
- If the patent contains a formula, threshold or example number, convey it exactly, but say whether it is an example
  (description) or part of a claim. Numbers in the description are mostly given "for example".
- If the patent does not name a product (most do not), a mapping such as "this is the Panda patent" is your
  interpretation or the SEO community's; present it as such.
- If you are making an inference, say clearly that it is an inference.
- A patent cannot diagnose the user's own site; for questions like "why did my site drop", say what the patent
  describes and do not attribute the cause to the patent.

**Write briefly.** The user calls this skill to get a fast, well-sourced answer, not a long review. Default format:

- The first sentence directly answers the question (yes / no / partly, with a one-sentence reason).
- Then short bullets or a short paragraph, as many as the length setting allows: each one a patent, what that
  patent says, and where (`Claim 1` or `[¶42]`). At most one short quote per patent; summarise the rest in your
  own words.
- A one-sentence limitation note (the patent describes this; it does not show it is used) and the source links.
- Length and the number of patents follow the answer settings; give each patent only a sentence or two. Do not add a "what I searched" list.

Do not write up everything you read: leave out side patents found while searching, family member listings and
method notes. Pick the two or three findings most useful to the user; for the rest, say in one sentence on the last
line "I can also go into X if you like". The same measure applies to the research: most questions are answered with
6–10 commands (one or two `search`, one or two `show`, a few `claims` / `passages`). Read in full only the patents
you will cite; do not spend time on extra searches that will not change the answer.

### Example

Question: "Does Google have a patent for a site quality score, and how is it calculated?"

> Yes: `US9031929B1` "Site quality score" (priority 2012, granted; inventors April Lehman and Navneet Panda).
>
> - Claim 1 defines the score as a ratio: the number of unique queries that refer to the site by name ("unique
>   queries [...] categorized as referring to a particular site") divided by the number of unique queries for which
>   users clicked through from the results to that site.
> - Roughly: how often people search for the site by name, against how many clicks the site gets from general
>   queries.
>
> The patent describes this calculation; it does not say whether the score is used in ranking today. The name
> "Panda" does not appear in the text; that mapping is the SEO community's interpretation.
>
> Source: https://patents.google.com/patent/US9031929B1/en

## Reference files

- `references/topic-map.md` — SEO concept → patents and suggested search terms (18 topics). Look at the relevant
  section before you start searching. The patents listed are starting points; open and verify each one with the
  tool.
- `references/background.md` — the coverage and limits of the archive, what the tags mean, how to read a patent
  (priority/application/grant, families, types of claims). Read it when the user asks about the archive itself, its
  reliability or a patent's legal status.

A patent answers "what method did Google describe". If the question is really about what Google recommends or
requires today (a rule, a threshold, a policy), say that this is the patent view only and that Google's official
documentation is the place for the rule; use the `google-search-docs` skill if it is installed. For AI Overviews,
AI Mode and Gemini patents, prefer `google-ai-patents` if it is installed; this archive holds only the search
patents that overlap.

If the user also has the `google-leak` skill, the two complement each other: the leak shows **what data** Google
stores (field names), while the patents show **how a method is described**. When you use both, state separately
which information comes from which source.
