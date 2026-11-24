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
api.seoskills.io and prints the answer. It needs internet access; if it reports that it cannot reach the API,
tell the user that their agent blocks network access and that the SEO Skills MCP server
(https://mcp.seoskills.io/mcp) offers the same tools. Search terms are sent to run the search and are not stored.
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
  phrases automatically. `OR` and `NOT` can be used. Search for two or three distinctive terms, not a sentence.
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
    question, who answers. If it is still unclear, say "it is said in a video X took part in; the speaker is not
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

## How to build the answer

Answer in the user's language. Give statements in their original English in quotation marks; if needed, add a
short explanation in the user's language next to them. Short answer first, then the evidence.

For every statement:

- **Who, where, when:** "John Mueller, Reddit r/TechSEO, 2022-03-11". For video/podcast, the timestamp:
  "Search Off the Record, 2022-08-25, 26:40".
- **In reply to what:** summarise the question or the message being answered in one sentence ("to a user asking
  about parameterised URLs being indexed"). This is the real value of this skill; do not skip it.
- **Verbatim quote:** without changing the words, the short part relevant to the question. Skip irrelevant parts of a
  long reply with `[...]`; do not make a cut that changes the meaning. If the setting limits verbatim quoting, quote
  the most decisive statement and paraphrase the others, keeping their hedges.
- **Link:** the URL from the `show` output (for video, the timestamped URL).

**Keep the person's statement separate from Google's official policy:**

- These people speak for Google, but their statements are not official documentation. They often say so themselves:
  "I'm generalising", "I can't say for sure", "systems change". Keep hedges such as "may", "usually",
  "I don't think", "generally"; do not turn "usually" into "always".
- Do not present personal chat, jokes or statements on non-Google topics (e.g. experiments on a personal website) as
  SEO rules.
- If a topic is also covered in official documentation and the user has `google-search-docs`, show the documentation
  and the employee's statement separately; if they contradict each other, say so with dates.
- If you are drawing an inference ("in practice this means …"), say that it is your inference.

**Keep it short.** Default format: the direct answer in the first sentence; then two to five bullets, each one
statement (who, where, when, in reply to what, short quote); a one-sentence note on timing/context if needed; source
links. A single-question answer is 150–350 words. Go longer if the user asks for a full list, a chronology or a
comparison. Most questions are answered with 5–10 commands.

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
