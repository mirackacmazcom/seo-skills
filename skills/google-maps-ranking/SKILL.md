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
api.seoskills.io and prints the answer. It needs internet access; if it reports that it cannot reach the API,
tell the user that their agent blocks network access and that the SEO Skills MCP server
(https://mcp.seoskills.io/mcp) offers the same tools. Search terms are sent to run the search and are not stored.
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
- Search with two or three distinctive words, not a sentence. If the first search comes back weak, try again with a synonym.
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
2. **Follow the hierarchy.** Build the answer by strength of evidence:
   - Official document first (Google's own statement).
   - Then employee statement (give context and date).
   - Then patent (only "describes").

   If a patent appears to contradict an official statement, say so; do not put the patent ahead of the statement.
3. **Check dates.** Employee statements and help pages change. For example, Google's core local ranking page was shortened in July 2025 and the sentence saying that web ranking is also a factor was removed. Always give the date of a statement. Do not present an old statement as today's rule.
4. **Report absence too.** The archive records that on some topics Google has never spoken: the effect of posts, photos, citations, click signals and review replies on ranking, and learning-to-rank for Maps. If the user asks about these, say "Google has made no official statement on this" and, where there are any, show the related patents as descriptions. Do not present third-party tests (Sterling Sky, Whitespark, etc.) as a Google source.
5. **Say so if you cannot find it.** List the terms you tried. The archive is dated November 2026; if the question is about a more recent development, point that out.

## Answer format

Answer in the user's language. Leave document titles and quotes in their original English.

- **Make the first sentence the direct answer** (yes / no / partly + a one-sentence reason).
- Follow with short bullets by source type. Each bullet should include:
  - The source (page name, person + date, or patent number + title + priority year)
  - What it says
  - The link
- Keep quotes short and verbatim. For patents, state whether it is a claim or the description.
- **Separate what the patent says from interpretation.** Do not say "Google uses X". Say instead "Google has a patent that describes X (US…, priority 20xx)". Matching a patent to a product feature (e.g. US20190340537A1 ↔ "Your match") is interpretation; present it as such.
- **Flag secondary sources.** Some of the employee statements are relayed only via Search Engine Roundtable; in the archive they are labeled "SER+original" or "secondary". State this in the answer as well.
- When a practical question comes up ("what should I do?"), give Google's official recommendation first. Present ideas drawn from patents separately, as "possible signal, not a proven factor".
- Length: 150–300 words for single-topic questions. Go longer if the user asks for a full breakdown, a comparison or a report.

### Example

Question: "Does review count affect Google Maps ranking?"

> Yes. Google says so officially. Review count and rating are part of the "prominence" factor.
>
> - **Official:** The "Tips to improve your local ranking on Google" page says "More reviews and positive ratings can help your business's local ranking." (support.google.com/business/answer/7091).
> - **Employee:** In August 2021 John Mueller said reviews are not used in web search, but that on the Business Profile side "maybe that's taken into account more". This statement comes from a secondary source (SEJ).
> - **Patent:** US7822751B2 (priority 2005) gives local results a query-independent "location prominence" score. In the description, the number of documents reviewing the business is given as an example of one of the inputs to this score [¶59]. US10394830B1, in turn, describes the sentiment in reviews as a ranking signal.
>
> Patents describe these methods; they do not show with what weight they are used today. Google has made no official statement about the effect of review replies or of keywords in reviews on ranking.
