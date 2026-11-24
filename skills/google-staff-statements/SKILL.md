---
name: google-staff-statements
description: Searches an archive of the public statements of eight current members of Google's Search team (John Mueller, Gary Illyes, Martin Splitt, Danny Sullivan / Search Liaison, Daniel Waisberg, Cherry Prommawin, Lizzi Sassman, Rajan Patel) — 47,000+ items from X, Bluesky, Mastodon, LinkedIn, Threads, Reddit, Stack Exchange, Hacker News, GitHub, Google+, Search Central YouTube videos and office hours, the Search Off the Record podcast, external podcast/video interviews, press interviews and personal sites — and answers questions from the person's own words, with the question they were answering, the date and the link. Use it when the user asks "what did Mueller say about X", "did Gary Illyes say this", "what has Search Liaison said about this", "what do Google employees say about canonical / noindex / crawl budget / core updates / E-E-A-T / AI content / backlinks / disavow", "who said this and when", "has Google changed its position on this", or whenever an SEO claim needs checking against what a Google employee actually said, even if no person is named. Do not quote statements from memory; take them from this skill's database. For official documentation use google-search-docs, for the leak google-leak, for patents google-patents or google-ai-patents.
---

# Statements by Google Search staff

This skill gathers everything eight current members of Google's Search team have publicly written and said over
the years into one searchable database: social media posts and replies, forum answers, video and podcast
transcripts, and interviews. For most replies it also stores **what the person was answering**: who asked, the
text of the question, and the root of the thread. The archive was collected in November 2026.

The goal: show claims of the "a Google employee said X" kind **at the source**. Much of what gets quoted in the SEO
world has been taken out of context, misremembered or attributed to the wrong person. A reply can only be read
correctly together with the question it answers. So take statements from this tool every time, not from memory,
and read the message that was being answered as well.

## How searches run

The archive lives on seoskills.io, so nothing is downloaded. The search tool sends its arguments to
api.seoskills.io and prints the answer. It needs internet access. If it reports that it cannot reach the API, run the command
once more; if it still fails, tell the user that their agent seems to block network access and that the SEO
Skills MCP server (https://mcp.seoskills.io/mcp, set-up at https://seoskills.io/install/) offers the same tools. Search terms are sent only to run the search. They are not logged or linked to you; results are cached for up to an hour so repeat searches are fast.
If the tool says there were too many searches, wait a minute before the next one.

## Search tool

The only tool is `scripts/statements.py` (Python 3, no extra packages needed). Run it from inside the skill folder
or by its full path:

```bash
python3 scripts/statements.py search canonical hreflang                    # full text; per item, with the best-matching unit
python3 scripts/statements.py search '"crawl budget"' -k illyes            # exact phrase; Gary Illyes only
python3 scripts/statements.py search disavow -k mueller --from 2023 --sort date   # 2023 and later, newest first
python3 scripts/statements.py search "core update" -k sullivan -p x,bluesky       # platform filter
python3 scripts/statements.py search "AI content" --in-question            # also search the text the person was ASKED
python3 scripts/statements.py search "domain authority" --question-only -k mueller  # questions only: who asked what
python3 scripts/statements.py show 2258                                    # header + thread + the full reply
python3 scripts/statements.py show 31270 --at 26:40                        # a moment in a transcript (60 s before to 120 s after); --unit N also works
python3 scripts/statements.py find "isn't a ranking factor" -k mueller     # does the phrase occur verbatim, who, where
python3 scripts/statements.py timeline "subdomain" -k mueller -n 30        # statements on a topic in date order (default first 60)
python3 scripts/statements.py people                                       # people, platforms, date ranges
python3 scripts/statements.py stats                                        # database summary
```

What you need to know:

- **Person filter (`--person`, `-k`)**: a surname, first name or handle is enough: `mueller`/`johnmu`,
  `illyes`/`gary`, `splitt`, `sullivan`/`searchliaison`, `waisberg`, `prommawin`, `sassman`/`lizzi`, `patel`.
- **Search works with English terms** (almost all content is in English; there are also German and Japanese video
  transcripts). Words are stemmed (`index`, `indexing`, `indexed` are the same). For an exact phrase wrap the double
  quotes in single quotes: `'"site reputation abuse"'`. Hyphenated/dotted terms (`E-E-A-T`, `robots.txt`) become
  phrases automatically. `OR` and `NOT` can be used. Words next to each other are joined first, so
  `subdomain subdirectory OR subfolder` finds "subdomain and subdirectory" or anything with "subfolder", which is
  rarely what you want: run one search per alternative. Search for two or three distinctive terms, not a sentence.
- **Cut the noise.** These people also joke and post about other things. For "what do they say" questions start
  with `--sort date --strict`, and leave press reports out (`-p social,forum,video,podcast`) unless you need them:
  a press item is the journalist's text. On video, `show <id> --unit N` and `--at` print a window of about three
  minutes around the moment, so expect an unrelated answer before and after the one you want.
- **Social media language:** these people write briefly and casually. Next to "ranking factor" also try phrases such
  as `"ranking signal"`, `"rank better"`, `"doesn't matter"`, `"not a thing"`. If the user's term returns nothing,
  search again with a synonym.
- **`--in-question`** adds the text of the message being answered to the search. The person may have answered
  "No, that's fine" without naming the topic in their own reply; such replies can only be found by searching the
  question. For important questions run both searches.
- **Result line:** `[item-id] date · platform type · person`, then `↳ replying to (author): …` and the matching
  excerpt `» …`. The excerpt is shortened; before quoting, read the full text and the thread with `show <id>`.
- **`show`** prints the thread in order from the root to the person's reply (`[root]` → `[mid]` → `[parent]`), then
  the reply itself. If these people have other messages in the same thread, it lists them at the end. For long
  items (video, podcast, office hours, blog) do not print everything; use the unit number from the result line
  (`#12`) with `show <id> --unit 12`, or `show <id> --search "disavow toxic"` (the best-matching unit within the
  item), and for video `--at MIN:SEC` (from 60 s before to 120 s after that moment, with a timestamped watch link; widen with `--around SECONDS`). `--full` prints
  everything.
- **Speaker identity (very important):**
  - Social media, site and LinkedIn items come from the person's **own account**; the words are theirs.
  - When speaker names are written in the transcript (Search Off the Record, most Search Central videos, written
    office hours transcripts), the header shows `(speaker-labelled)` or `speaker-labelled transcript` and each unit
    is tied to the named speaker; the `-k` filter does not attribute guests' words to that person. The labels come
    from the source and occasionally slip: if a unit contains a question followed by a long answer (e.g. the host's
    question followed immediately by the guest's story), the label may be missing. If the content does not fit the
    person, read the surrounding transcript with `show <unit> --at MIN:SEC` or the whole unit with `--full`.
  - In transcripts without speaker labels (external videos, external podcasts, some older videos) the header shows
    `participants: … — no speaker separation`. This shows the person took part in the recording, but **not** that
    they said the matching sentence: the host, a guest or another Google employee may have said it. Before
    attributing it, read the surrounding text with `show --at`: does the speaker introduce themselves, who asks the
    question, who answers. When the text itself names the speaker ("JOHN MUELLER:") or the person is the only
    participant, attribute it plainly, without a hedge. On a video, always call `show` with `--at` or `--unit`; a
    bare `show <id>` prints only the list of units. If it is still unclear, say "it is said in a video X took part in; the speaker is not
    certain from the transcript". For text tied to the person with certainty only, use `--strict`.
  - Press interviews (`interview/report`) are the journalist's text; even words in quotation marks may not be
    verbatim. Present them as "according to what X told Search Engine Land". Help Community thread pages (`forum`)
    can contain answers from several Google employees; work out who wrote what from the name on the page.
- **Platform groups (`-p`):** `social`, `forum`, `video`, `audio`, `transcript`, `written`, `external`, or
  individually `x`, `bluesky`, `mastodon`, `linkedin`, `threads`, `googleplus`, `reddit`, `stackexchange`,
  `hackernews`, `github`, `youtube` (Search Central channel, office hours included), `youtube-ext`, `podcast`
  (Search Off the Record), `podcast-ext`, `google-blog` (official blog posts written by these people), `site`,
  `press`. Item types (`--type`): `post`, `reply`, `comment`, `quote`, `video`, `podcast`, `blog`, `office-hours`,
  `interview`, `forum`.
- **Date filter:** `--from 2020`, `--to 2022-06`. A person's view can change over time; do not present an old
  statement as the current position.
- **Warnings in the header:** `DELETED` (the person later deleted it; taken from a Wayback copy),
  `captions: may be automatic` (names and terms may be wrong; suggest checking the quote against the video),
  `automatic transcript from audio`, `archive copy`, `title not verified`, `date known only to the month` (the 1st
  of the month is shown; do not give a day), `Search Liaison role account` (posts by @searchliaison after 1 August
  2025 may not be Danny Sullivan's).
- **If the message being answered is missing:** `↳ replying to a message: no text` means a reply to a deleted or
  protected message. Who it was addressed to can be seen from the @name at the start of the reply; do not guess
  the question, say "the text of the question is not in the archive".
- **Jokes:** these people are often ironic (e.g. the "result" of Mueller's 2018 "subdomain is better than
  subdirectory" poll). If a statement contradicts their established views, check its context and their other
  statements on the same topic.

## How to work

1. **Identify the person and the topic.** If the person is not clear, search without a filter and look at the
   distribution at the top of the results (`[John Mueller 47, Gary Illyes 12, …]`). For topic terms see
   `references/topic-terms.md`.
2. **Search from both sides:** in the person's own text (`search`) and, if needed, in the questions
   (`--in-question`). If you are looking for one specific quote, use `find` to see whether it occurs verbatim.
3. **Read the thread.** For every reply run `show <id>`: who asked, what they asked, what the person said "yes" or
   "no" to. Short replies ("Yes", "That's fine", "Depends") only make sense together with the question. Work out
   jokes and irony from the context too; these people (especially Illyes and Mueller) joke a lot.
4. **Check the timing.** Use `timeline` or `--sort date` to compare older and newer statements on the same topic. If
   the view has changed, give both with their dates and put the newest first. Remember that a statement describes
   Google's policy at the time it was made.
5. **If you cannot find it, say so.** List the terms and filters you tried. Absence from the archive does not prove
   the person never said it (conference talks, closed Slack/Discord groups, most deleted tweets and emails are not in
   the archive; see `references/background.md`). But do not attribute to anyone a statement that is not in the
   archive.

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

Language, length and citations follow the answer settings above. Short answer first, then the evidence. Shape it
by the kind of question:

- **"What do they say about X?"** Lead with where they agree, in one sentence. Then two or three statements, the
  newest substantive one first.
- **"Has Google changed its mind?"** Go in time order: the earlier position, the change, what has been said since.
- **"Did X say Y?"** Yes or no, then the one statement, with what it was a reply to.
- **Sources off:** the people and the years stay ("Mueller said in 2022…"); quotes, links and platforms go, and
  "in reply to what" shrinks to a clause.

For every statement:

- **Who, where, when:** "John Mueller, Reddit r/TechSEO, 2022-03-11". For video/podcast, the timestamp:
  "Search Off the Record, 2022-08-25, 26:40". Use the date in the item's header line, the same one for every item.
- **Official posts written by these people** (Search Central blog articles) are Google's published position, not a
  personal remark: present them as "the Search Central blog, by Sullivan and Illyes, 2019-09-10".
- **In reply to what:** summarise the question or the message being answered in one sentence ("to a user asking
  about parameterised URLs being indexed"). This is the real value of this skill; do not skip it.
- **Verbatim quote:** without changing the words, the short part relevant to the question. Skip irrelevant parts of a
  long reply with `[...]`; do not make a cut that changes the meaning. If the setting limits verbatim quoting, quote
  the most decisive statement and paraphrase the others, keeping their hedges.
- **Link:** the URL from the `show` output (for video, the timestamped URL). If a URL is several lines long (some
  LinkedIn comment links), link the post it belongs to or name the platform and date instead.

**Keep the person's statement separate from Google's official policy:**

- These people speak for Google, but their statements are not official documentation. They often say so themselves:
  "I'm generalising", "I can't say for sure", "systems change". Keep hedges such as "may", "usually",
  "I don't think", "generally"; do not turn "usually" into "always".
- Do not present personal chat, jokes or statements on non-Google topics (e.g. experiments on a personal website) as
  SEO rules.
- If a topic is also covered in official documentation and the user has `google-search-docs`, show the documentation
  and the employee's statement separately; if they contradict each other, say so with dates.
- If you are drawing an inference ("in practice this means …"), say that it is your inference.

**Keep it short.** Default format: the direct answer in the first sentence; then one bullet per statement (who,
where, when, in reply to what; a quote where the wording decides), as many as the length setting allows; a
changed-mind timeline may use one more bullet than usual; a one-sentence note on timing/context if needed; source
links. Length follows the answer settings. Most questions are answered with 5–10 commands: run `show` only for
the two or three statements you will quote; a statement you mention in passing may be paraphrased from the search
excerpt.

### Example

Question: "Does Mueller recommend noindex or robots.txt for internal search pages?"

> Either one; he says using both together makes no sense.
>
> - **Reddit r/TechSEO, 2022-03-11.** A user says URLs with `search?` and `sort?` parameters keep getting indexed
>   despite a sitemap and canonicals, and asks whether to use the URL parameter tool or noindex. Mueller: "With
>   robots.txt or noindex (both together don't make sense) at least you [...]". He calls the parameter tool
>   "scary". https://www.reddit.com/r/TechSEO/comments/tbrwol/_/i09uofq/
> - **Bluesky, 2025-06-02.** "you can also just block internal search from indexing with robots.txt or noindex".
>   In the same post he also says empty internal search results should return a 404.
>
> Note: both are short replies giving a personal view; for the rule in the official documentation, google-search-docs
> can be consulted.

## Reference files

- `references/people.md`: the eight people, their roles, accounts, how much content there is on each platform,
  speaker labels and name confusions (e.g. Lizzi Sassman's former surname Harvey).
- `references/topic-terms.md`: search terms these people use for common SEO topics.
- `references/background.md`: the scope of the archive, sources and collection method, known gaps.
  Read it when the user asks about the archive itself, its coverage or the reliability of a source.

If the user also has `google-search-docs`, `google-leak` and `google-patents`, the four complement each other: the
official documentation shows Google's **written policy**, this archive shows **what employees said in Q&A**, the
leak shows **which data is stored**, and the patents show **how a method is described**. State which information
comes from which source; do not present one as evidence for another.
