---
name: google-search-docs
description: Searches an archive of Google's OFFICIAL documentation on search and SEO (3,600+ documents; Search Central docs and blog, spam policies, crawling/robots.txt, structured data, Search Console Help, How Search Works, the Search Quality Rater Guidelines, web.dev/Core Web Vitals, Chrome and PageSpeed Insights) and answers questions from Google's own text, with quotes and links. Use it when the user asks "what does Google officially say", "what do the docs say", "is X a ranking factor", "does X count as spam" or "does Google recommend X"; and whenever a rule, threshold or recommendation needs to be checked, or an SEO claim backed by a primary source, on topics such as canonical, noindex, robots.txt, hreflang, sitemaps, redirects, JavaScript SEO, structured data/schema, snippets, core updates, E-E-A-T, YMYL, AI Overviews, AI content, spam policies, Core Web Vitals or Search Console reports, even if the user never says "documentation". Do not write rules or quotes from memory. (Not for editing Google Docs; for the leak use google-leak, for patents google-patents or google-ai-patents.)
---

# Google official documentation archive

This skill gathers the pages Google **itself has published** on search, SEO, ranking, technical SEO, performance and
AI into one searchable database: 3,630 documents, about 3.3 million words of English text, plus Google's own
translations of 1,086 pages (Turkish in this archive). The archive was captured on 11 November 2026.

The goal: answer the user's question based on **what Google actually wrote**. A large share of what gets passed
around in SEO as "Google says" is misremembered, outdated or was never said. The value of this skill is that it can
show a rule or recommendation at its source, with its section and date. So take rules, thresholds and quotes from
the search tool every time, not from memory: the documentation changes often, and the version in memory is
frequently out of date.

## How searches run

The archive lives on seoskills.io, so nothing is downloaded. The search tool sends its arguments to
api.seoskills.io and prints the answer. It needs internet access. If it reports that it cannot reach the API, run the command
once more; if it still fails, tell the user that their agent seems to block network access and that the SEO
Skills MCP server (https://mcp.seoskills.io/mcp, set-up at https://seoskills.io/install/) offers the same tools. Search terms are sent only to run the search. They are not logged or linked to you; results are cached for up to an hour so repeat searches are fast.
If the tool says there were too many searches, wait a minute before the next one. If it says the daily limit is
reached (2,000 searches a day), tell the user; it resets at 00:00 UTC.

## Search tool

The only tool is `scripts/gdocs.py` (Python 3, no extra packages needed). Run it from inside the skill folder, or call
the script by its full path; it does not depend on the working directory:

```bash
python3 scripts/gdocs.py search canonical duplicate            # full-text search; results by document, with matching sections
python3 scripts/gdocs.py search '"crawl budget"' --in core     # exact phrase; current guidance only (no blog)
python3 scripts/gdocs.py search '"core update"' --in blog --from 2024 --strict --sort date   # blog, 2024 onwards, newest first
python3 scripts/gdocs.py search INP threshold --in perf        # web.dev + Chrome + PageSpeed Insights
python3 scripts/gdocs.py show docs/essentials/spam-policies    # header + section list (whole text for short documents)
python3 scripts/gdocs.py show docs/essentials/spam-policies --section 12        # one section (3,5-7 or "heading" also work)
python3 scripts/gdocs.py show docs/crawling-indexing/301-redirects --translation   # Google's own translation
python3 scripts/gdocs.py passages sqrg YMYL harm               # most relevant paragraphs in a long document (tagged [§n ¶m])
python3 scripts/gdocs.py find "E-E-A-T itself isn't a specific ranking factor"  # does the phrase occur verbatim, and where
python3 scripts/gdocs.py list docs --path structured-data --limit 200             # documents in a collection
python3 scripts/gdocs.py refs docs/fundamentals/creating-helpful-content        # pages linking to / linked from this page
python3 scripts/gdocs.py stats                                 # database summary; list (on its own) counts the collections
```

What you need to know:

- **Search works with English terms**; the main text is English. Words are reduced to their stem (`rank`,
  `ranking` and `ranked` count as the same). For an exact phrase, wrap the double quotes in single quotes:
  `'"site reputation"'`. Hyphenated and dotted terms (`E-E-A-T`, `robots.txt`, `max-snippet`) are searched as
  phrases automatically. You can use `OR` / `NOT`.
- **Search with two or three distinctive terms, not with a sentence.** `search hreflang x-default` works well;
  `search how should I set up hreflang for my multilingual site` does not. The user's SEO jargon and Google's term
  can differ ("parasite SEO" → `"site reputation"`; "dwell time" does not appear in the docs); look at the topic map
  first for the right terms.
- **Search runs on sections and groups the results by document.** Under each result, the matching sections appear
  with their `§N` number and a short snippet. The snippet is cut; before quoting or summarising anything, read the
  section itself with `show <doc> --section N`.
- **Ranking puts current documentation ahead of old blog posts**, because the archive has more than 1,600 blog posts
  against 164 documentation pages. Turn this off with `--flat`. If few sections contain all the terms, the tool also
  adds sections that contain any of them and says so at the top of the output (full matches are marked with `*`);
  turn this off with `--strict`.
- **Filters:** `--in <collection>` (comma-separated for several): `docs`, `crawling`, `search-misc`, `sc-help`,
  `hsw`, `pdf`, `blog`, `office-hours`, `webdev`, `chrome`, `psi`, `sc-api`, `gblog`, `help-other`, `other`; ready
  groups `core` (current official guidance; no blog or office hours), `perf`, `blogs`. Also `--path <text>`
  (contained in the address), `--from YEAR` / `--to YEAR`, `--title` (titles only), `--sort date`, `--limit N`,
  `--sections N`, `--width 0` (no snippets). `office-hours` holds transcripts of spoken answers to questions from
  2022–2024; valuable for practical detail, but they describe the situation at that time.
- **Document names are flexible.** You can give the full URL, `host/path`, the end of the path
  (`essentials/spam-policies`) or a short form: `docs/…` = Search Central documentation, `blog/…` = Search Central
  blog post, `help/7440203` = Search Console Help page, `sqrg` = Search Quality Rater Guidelines, `sqrg-overview` =
  the short overview of the guidelines. If you give an old address, the tool follows it to the new one or says the
  page no longer exists on Google.
- **`show` is short by default:** header, section list and the intro (only the start of a long intro). Instead of
  loading long documents into context, pull the relevant section with `--section` or the relevant paragraphs with
  `passages <doc> <terms>`. Use `--full` for the whole document and `--links` to see link addresses.
- **`passages` returns results most relevant first.** Write a multi-word concept in quotes (`'"site reputation"'`);
  without quotes the words also match separately. Tables match row by row, so only the relevant row of a long table
  comes back. Long paragraphs are cut around the match; use `--max 0` for the whole paragraph, `--around N` for the
  surrounding paragraphs, `--limit N` for more results.
- **`find` tells you whether a phrase occurs verbatim in the archive** (case and whitespace differences are ignored),
  in how many documents and in which sections. Rely on it before saying "Google says this nowhere" or attributing a
  sentence from memory to Google. You do not need it for a quote whose section you have already read with `show`.
  Add `--loose` to count inflected forms too.
- **Translations:** the archive also holds Google's own translations of many pages (Turkish in this archive).
  `show <doc> --translation` shows that version and says whether it is a human or machine translation. To search the
  translated text use `--lang tr` (accent-insensitive, substring match: `yonlendirme` → "yönlendirmeleri"). For blog
  posts published only in another language use `--lang de|es|ja|…` or `--lang all`.
- **The date and source in the header matter.** A blog post shows its publication date, a documentation page its last
  update date. If you see the `archived copy <date>` tag, the page was taken from the Internet Archive rather than the
  live site; give the copy date in your citation. PDF sections show page numbers. Most help pages carry no date from
  Google; the header then shows only the date the page was archived.

## How to work

1. **Translate the concept into Google's language and the right page.** Look at `references/topic-map.md` first: it
   shows which official pages cover common topics and which terms to search for. The file is long; find the relevant
   heading in its table of contents and read only that section. If the topic is not in the map, start with `search`.
2. **Current documentation first, history second.** If a rule, recommendation or definition is asked about, the
   answer is almost always in `docs`, `crawling` or `sc-help`. Blog posts answer "when was this announced and what was
   said then"; find when a rule changed with `passages search/updates <term>`. For quality concepts (E-E-A-T, YMYL,
   Needs Met) use `sqrg`; for metric definitions and thresholds use `--in perf`.
3. **Read the section; do not settle for the snippet.** `search` finds candidates; base the answer on the output of
   `show --section` or `passages`. If a page refers to another page (the docs link to each other a lot), open that
   too; `refs` shows other pages on the same topic.
4. **Check the date and the source type.** A blog post from 2012 describes the situation in 2012; if there is a current
   documentation page on the same topic, that one applies. Policies change too: a statement in an announcement post
   may have been reversed in the later-updated documentation, so do not rely on the blog post alone; open the current
   page as well. If you see a contradiction, state both with their dates in one sentence at the end of the answer. A
   page simply not mentioning a newer development is not a contradiction; go with the more recent source. If two
   current pages say the same thing in different words (e.g. one writes a threshold as "below" and the other as "at
   or below"), give both with their sources. For pages that are archived copies, give the copy date.
5. **If you cannot find it, say so and state what you searched for.** List the terms you tried and show the closest
   real page if there is one. Something not appearing in the archive does not prove that Google has said nothing on
   the topic (see `references/background.md` for the gaps); but attributing to Google a statement that is not in the
   archive misleads the user.

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

Answer in the user's language. Leave page titles and quotes in their original English; if needed, add a short
explanation in the user's language next to them. If the user wants a quote in the language of one of the archived
translations, use Google's own version (`--translation`) and say if it is a machine translation; never translate a
quote yourself and put it in quotation marks. Give the short answer to the question first, then show the evidence.

Tie every claim to its source:

- Name the page with its title and date: "Spam policies for Google web search" (updated 2026-08-28). For a blog post
  give the publication date: (blog, 2019-09-10). If the page has no date, say "as of the archive date, 2026-11-11".
- Give the location of the quote: the section heading is enough (the *Scaled content abuse* section). For the
  guidelines give the section number and page: SQRG §2.3, p. 11.
- Quote Google's text in quotation marks without changing its words; keep quotes short and relevant to the question.
  You may skip an irrelevant part of a long sentence with `[...]`; do not make a cut that changes the meaning.
- If your environment limits verbatim quotation (e.g. one short quote per answer), quote the single most decisive
  sentence; report the other sources in your own words, keeping their modal verbs, and give each one's page, section
  and address. Never write an invented or approximate "quote" in place of a real one.
- Add the address from the `show` or `passages` output so the user can open the source themselves.

**Separate what Google says from your own interpretation.** This is the most important rule of this skill:

- The documentation says **what Google recommends, what it supports and what it treats as a policy violation**. It
  does not give the weights of ranking signals or a complete list of them. Only write a sentence like "Google weighs X
  this much in ranking" if the text says exactly that.
- Keep the modal verbs. "may", "can", "we recommend", "isn't a ranking factor" and "one of many signals" each say
  something different; do not turn "recommends" into "requires" or "can use" into "uses".
- The Search Quality Rater Guidelines are a handbook for human raters. Do not present a criterion from them as a
  ranking factor; say "the guidelines tell raters that …".
- web.dev and Lighthouse describe good practice; a Lighthouse audit or a PageSpeed score is not, on its own, a ranking
  signal. If a Search Central document makes the link to ranking, quote that document.
- If you are drawing an inference ("this means …", "in practice you should …"), say clearly that it is an inference.
  If you rely on general knowledge that is not in the archive (e.g. whether a country is in the EEA), say that it does
  not come from the archive.
- The documentation cannot diagnose the user's own site. For questions like "why did my site drop", report the
  possible causes Google lists and the checks it recommends; do not attribute the cause to the documentation.

**Write briefly.** The user calls this skill to get a fast, well-founded answer. Default format:

- The first sentence answers the question directly (yes / no / partly, with a one-sentence reason).
- Then a few short bullets or a short paragraph: each one a page or section, what it says there, and where. Think of
  quotes per claim: one short quote for each claim where the exact wording or modal verb is decisive, the rest in your
  own words. How many sources and quotes to show follows the answer settings.
- If needed, a one-sentence note on limits (what the documentation does not say, the date, an archived copy) and the
  source links.
- Length follows the answer settings. If the question has several parts or the answer depends on conditions, give
  each part a short answer. If space is tight, keep what the sources say and shorten your own interpretation and side
  details. Do not add a "what I searched" log.
- When two current pages give different numbers or options for different purposes (180 days on one page, a year on
  another; noindex on one, robots.txt on another), lead with the page that is most specific to the user's case and
  explain the other in one clause. That is not a contradiction; say what each number is for.
- If the tool shows that Google publishes the page in the user's language, you may add the link to that version so
  the user can read the source; quote from it only as described above.

Do not write up everything you read: leave side pages and method notes out of the answer. Most questions are answered
in 3–8 commands. When the topic map names the page, go straight to `passages <page> <terms>` or `show --section` and
skip `search`. `passages` needs every term to match, so give it one to three terms. Read in full only the sections
you will cite; do not spend time on extra searches that will not change the answer.

### Example

Question: "Is E-E-A-T a ranking factor?"

> No; Google says so explicitly on two official pages, but it does not treat E-E-A-T as unimportant either.
>
> - "Creating helpful, reliable, people-first content" (updated 2026-10-05), section *Get to know E-E-A-T and the
>   quality rater guidelines*: "While E-E-A-T itself isn't a specific ranking factor, using a mix of factors that can
>   identify content with good E-E-A-T is useful."
> - "SEO Starter Guide", section *Things we believe you shouldn't focus on*: "Thinking E-E-A-T is a ranking factor:
>   No, it's not."
>
> As Google describes it, E-E-A-T is not a single signal but the name for qualities its systems try to reward. The
> documentation does not say which signals measure it.
>
> Sources: https://developers.google.com/search/docs/fundamentals/creating-helpful-content ·
> https://developers.google.com/search/docs/fundamentals/seo-starter-guide

## Reference files

- `references/topic-map.md` — SEO topic → official pages and suggested search terms (23 topics). Look at the relevant
  section before you start searching. The pages listed are starting points; open and read each one with the tool.
- `references/background.md` — the archive's scope, how much weight each collection carries, what the dates and
  source types mean, translations, known gaps, what the official documentation does and does not say, and where the
  database comes from. Read it when the user asks about the archive itself, the reliability of a source or the gaps.

If the user also has the `google-staff-statements`, `google-leak` and `google-patents` skills, they complement each
other: the official documentation shows what Google **tells the public**, staff statements **what employees answered
in Q&A**, the leak **what data it stores**, and the patents **how a method is described**. When you use them together, state which information comes from which source; do not present one as
evidence for another.
