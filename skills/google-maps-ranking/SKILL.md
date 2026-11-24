---
name: google-maps-ranking
description: Answers from a primary-source archive on ranking in Google Maps, local search (local pack) and Google Business Profile, with 326 Google patent families, 111 official Google docs, 45 Google employee statements and 26 Google Research papers (Nov 2026). Use for Maps ranking, local SEO, map SEO, Business Profile (formerly Google My Business) optimization, relevance-distance-prominence, how reviews, categories, business name, distance, opening hours ("openness"), visit and location history or photos affect ranking, fake listings or review spam, Vicinity/Possum updates, the "Your match" score, Ask Maps or Gemini recommendations in Maps. Also without the words "patent" or "document", e.g. "how to rank higher on Maps", "does review count affect ranking", "do keywords in the business name help", "what did Google say". Public sources only; for the 2024 Google leak see google-leak, for full patent text google-patents. Take patent numbers, quotes and dates from this skill's data, not memory.
---

# Google Maps ranking archive

This skill gathers in one place the publicly available primary sources that explain how ranking works in Google Maps and local search. The sources are of four types, and each has a different evidentiary value:

| Type | What it shows | What it does not show |
|---|---|---|
| **Official Google document** (support.google.com, developers.google.com, blog.google) | What Google tells the public, i.e. the official framework | The weights or the detailed formula |
| **Google employee statement** (Danny Sullivan, John Mueller, etc.) | Google's side of the story on a particular signal or update | A permanent rule; statements can go out of date over time |
| **Google Research publication** | Technical work that Google teams carried out with Maps data and published | That the method is used in the product |
| **Patent** | That Google described a method and sought protection for it | That the method is used today, or with what weight |

The value of this skill is that it can tie claims of the "Google Maps ranks like this" kind back to their source. In the local SEO world, many claims rest either on an over-reading of a patent or on a misremembered statement. So take numbers, dates and quotes from the archive every time; patent numbers and quotes written from memory often turn out to be wrong.

## How searches run

The archive lives on seoskills.io, so nothing is downloaded. The search tool sends its arguments to
api.seoskills.io and prints the answer. It needs internet access. If it reports that it cannot reach the API, run the command
once more; if it still fails, tell the user that their agent seems to block network access and that the SEO
Skills MCP server (https://mcp.seoskills.io/mcp, set-up at https://seoskills.io/install/) offers the same tools. Search terms are sent to run the search and are not stored.
If the tool says there were too many searches, wait a minute before the next one.

## Tool

`scripts/search.py` (Python 3, no extra packages needed). Run it from the skill folder:

```bash
python3 scripts/search.py search review ranking signal        # searches all four source types at once
python3 scripts/search.py search distance --type statement    # employee statements only
python3 scripts/search.py search business name keyword --type doc
python3 scripts/search.py search prominence --type patent --category 1
python3 scripts/search.py show US7822751B2                    # a patent's note, abstract and link
python3 scripts/search.py category                            # the 10 patent categories
python3 scripts/search.py category 4                          # all patents in one category
python3 scripts/search.py stats
```

- `--type` values: `patent`, `doc`, `statement`, `research`.
- Common concepts expand automatically to related terms (review → rating, distance → proximity/nearby, prominence → popular, hours → open/openness, fake → spam/fraud…).
- Search with two or three distinctive words, not a sentence. Every word must match (a word also matches its listed synonyms, shown as "term groups" in the output), so an extra word can turn a good search into zero matches: drop a word or try a synonym. Common words match widely ("hours" also finds "Office Hours" transcripts); narrow with `--type`.
- **The "Note" field on patents** was written after reading the independent claims and shows its basis (Claim 1, [¶56]). Patents without a note carry only the patent's own abstract; do not claim anything about such a patent that the abstract does not say.
- **When the full text of a patent** is needed (claim detail, a specific paragraph), the `show` output says which separate skill holds the full text. Those archive skills (`google-patents`, `google-ai-patents`) are not part of this skill. If the named one is installed, use its `patent.py` script, for example:

  ```bash
  python3 <google-patents skill folder>/scripts/patent.py claims <number> --independent
  python3 <google-patents skill folder>/scripts/patent.py passages <number> <terms>
  ```

  If it is not installed, work from the note and abstract here and point to the Google Patents link.

## Reference files

When you need the context of an item you found through search, read only the relevant section of the file concerned.

- `references/synthesis.md`: A short summary of what the four source types say together. For general questions ("How does Maps ranking work?") read this first.
- `references/official-docs.md`: Official documents. Sections: A) ranking factors, B) optimization, C) policies, D) reviews, E) product and AI blogs, F) Places API, G) Quality Rater Guidelines.
- `references/employee-statements.md`: Employee statements, grouped by topic. Each entry carries a primary/secondary source label.
- `references/google-research.md`: Google Research publications.
- `references/patents.md`: The full list of the 326 patents, category by category (684 lines). Do not load all of it; use the `search` and `category` commands.
- `references/scope-and-method.md`: How the archive was compiled, what it does not cover, the link check. Read it when the user asks about the reliability or completeness of the archive.

## How to work

1. **Split the question by source type.** A question like "Do reviews affect ranking?" is searched in four places:
   - What does Google officially say? (doc)
   - What have employees said? (statement)
   - Which patents describe this? (patent)
   - Is there research? (research)

   Search without a type first, then narrow with `--type` if needed.
2. **Follow the hierarchy when sources disagree.** By strength of evidence:
   - Official document (Google's own statement).
   - Employee statement (give context and date).
   - Patent (only "describes").

   The hierarchy settles conflicts; it does not fix the order of the answer. Lead with the source that answers the
   question most directly, whatever its type. If a patent appears to contradict an official statement, say so; do
   not put the patent ahead of the statement.
3. **Check dates.** Employee statements and help pages change. For example, Google's core local ranking page was shortened in July 2025 and the sentence saying that web ranking is also a factor was removed. Always give the date of a statement. Do not present an old statement as today's rule.
4. **Report absence too.** The archive records that on some topics Google has never spoken: the effect of posts, photos, citations, click signals and review replies on ranking, and learning-to-rank for Maps. If the user asks about these, say "Google has made no official statement on this" and, where there are any, show the related patents as descriptions. Do not present third-party tests (Sterling Sky, Whitespark, etc.) as a Google source.
5. **Say so if you cannot find it.** List the terms you tried. The archive is dated November 2026; if the question is about a more recent development, point that out.

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
| Next step | A clause, only for a decision question | One or two sentences | One or two sentences, plus what the sources suggest when read together |

These sizes replace any other word count in this file. A busy reader wants the verdict and the decisive source,
not everything you read: leave side findings out and offer them in one closing line ("I can also go into X").

Where a setting comes from, strongest first:

1. What the user says in the conversation.
2. A line that starts with `SEO Skills:` in your standing instructions (CLAUDE.md, AGENTS.md, project or custom
   instructions), for example `SEO Skills: detailed answers, sources off, always answer in Dutch`.
3. The defaults above.

People say this in their own words, in any language. Map them like this, and change only what was asked for:

- "shorter", "short answers", "just the summary", "in one line", "kısa tut" → `brief`
- "more detail", "the long version", "every source", "full breakdown" → `detailed`
- "no links", "skip the sources", "without quotes", "kaynak gösterme" → sources `off`
- "show me the sources", "where does that come from" → sources `on`

A request about one answer ("give me the long version of that", "shorten this") applies to that answer. A request
worded as a preference ("keep it short", "no sources please", "from now on…") holds for the rest of the
conversation. If you cannot tell, treat it as a preference; the user can change it back in a word.

How the settings combine:

- Sources `off`, at any length: say what the answer rests on in plain words inside the sentence. Names that help
  the user look it up stay: a person and year ("John Mueller said in 2022"), a page ("Google's spam policy"), a
  patent in words ("a 2012 Google patent on site quality"), a field ("a field called hostAge"). Quotes, links,
  claim and paragraph numbers, platforms and source lists are left out.
- `brief` with sources on: the answer plus the one strongest source (name, date, link). If the verdict needs two
  facts from two pages, name both in the sentence and link the one that carries the verdict.
- When the user changes a setting right after an answer, rewrite that answer from what you already found. Do not
  search again unless the new version needs something you have not read.

The settings are the same for every SEO Skills skill. No setting changes these rules:

- Take every fact, number, date and quote from the search tool, never from memory. With sources off you still
  search first; you only leave the citations out, and you give them as soon as the user asks.
- Keep what the source says apart from your own inference.
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
skill if it is installed) instead of forcing advice out of it.

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

## Answer format

Language, length and citations follow the answer settings above.

- **Make the first sentence the direct answer**: yes, no, partly, or "Google has not said", plus a one-sentence
  reason.
- Follow with short bullets, one per source that bears directly on the question. Each bullet should include:
  - The source (page name, person + date, or patent number + title + priority year)
  - What it says
  - The link
- **Leave out a source type that adds nothing.** If there is no official page or no employee statement on the
  point, say so in one clause ("no employee statement exists") instead of filling a bullet with a loosely related
  source. An entry that the archive lists with only a title and a link, without a summary, is not evidence: do not
  cite it for a claim.
- Keep quotes short and verbatim. For patents, state whether it is a claim or the description.
- **Separate what the patent says from interpretation.** Do not say "Google uses X". Say instead "Google has a patent that describes X (US…, priority 20xx)". Matching a patent to a product feature (e.g. US20190340537A1 ↔ "Your match") is interpretation; present it as such.
- **Flag secondary sources in plain words.** The archive labels each employee statement: `primary` (Google's own page was read), `SER+original` (Search Engine Roundtable reports the quote and links to the original post) and `secondary` (only a news report). Official documents carry `✔` (page opened and checked), `✔a` (taken from the archive of official documentation) or `(s)` (seen in a search result only, not verified). Do not show these labels to the user; write "reported by Search Engine Roundtable, with a link to the original post" or "from a news report only, not verified". When the archive paraphrases a statement, paraphrase it too and do not put it in quotation marks.
- When the user has a plan, or asks whether something affects ranking, close with what to do: Google's official recommendation first, where one exists. Present ideas drawn from patents separately, as "possible signal, not a proven factor".
- A question the first search answers fully needs no further searches. An answer that says "Google has not said" should be short: the verdict, the nearest real source in one bullet, and what to do.

### Example

Question: "Does review count affect Google Maps ranking?"

> Yes. Google says so officially. Review count and rating are part of the "prominence" factor.
>
> - **Official:** The "Tips to improve your local ranking on Google" page says "More reviews and positive ratings can help your business's local ranking." (support.google.com/business/answer/7091).
> - **Employee:** In August 2021 John Mueller said reviews are not used in web search, but that on the Business Profile side "maybe that's taken into account more". This statement comes from a secondary source (SEJ).
> - **Patent:** US7822751B2 (priority 2005) gives local results a query-independent "location prominence" score. In the description, the number of documents reviewing the business is given as an example of one of the inputs to this score [¶59]. US10394830B1, in turn, describes the sentiment in reviews as a ranking signal.
>
> Patents describe these methods; they do not show with what weight they are used today. Google has made no official statement about the effect of review replies or of keywords in reviews on ranking.
