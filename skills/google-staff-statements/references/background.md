# Background of the archive

## Scope and sources

The archive was collected in November 2026 from the eight people's verified accounts and from published records
about them. It is hosted on seoskills.io and searched through its API (see "How searches run" in `SKILL.md`).

| Source | How it was collected | Note |
|---|---|---|
| X | Apify (full search in monthly slices) | The tweets that replies answer were fetched separately. Some deleted tweets come from Wayback (marked DELETED in the header). |
| Bluesky, Mastodon | Public API | Thread from the root onwards. |
| LinkedIn | Apify (cross-checked with two independent scrapers) | Posts, comments, the comment being replied to and earlier replies in the thread. |
| Threads | Apify | @searchliaison only. |
| Reddit | Arctic Shift archive | Comments and the post/comment being replied to. |
| Stack Exchange, Hacker News, GitHub | Public APIs | With the question/thread text. |
| Google+ | Archive copies | The platform closed in 2019; most of the content is lost and there are no dates. |
| YouTube (Google Search Central) | yt-dlp and Apify | Office hours, SEO Mythbusting, Search Central Lightning Talks, etc. Human-made captions where available, otherwise automatic captions. |
| Search Off the Record | Transcripts published by Google (PDF) + Whisper transcription for unpublished ones | Most are speaker-labelled. |
| External videos and podcasts | Discovery + classification; Apify captions or Whisper transcription | Only those in which the person was confirmed to speak. No speaker separation. |
| Press interviews | Page text (Internet Archive copy for dead pages) | The interviewer's account; not verbatim (see below). |
| Official blog posts | From the google-search-docs archive, posts the person authored | |
| Personal sites | Sitemap/feed | johnmu.com, splitti.online, okaylizzi.com, danielwaisberg.com. |

## Known gaps

- **Deleted content:** most tweets the people later deleted on X, and about 2,500 tweets they replied to (deleted or
  protected accounts), are missing. For these replies the header shows "replying to a message: no text"; who the
  reply was addressed to can be seen from the @username at the start of the reply.
- **Old forums:** the old Google Webmaster Central Help Forum, Google Groups and most Google+ content have been
  removed from the internet.
- **Conference talks:** stage talks whose recordings were not published (SMX, Pubcon, BrightonSEO, etc.) exist only
  through press reports.
- **Closed channels:** Discord/Slack communities, email and private messages are not included.
- **Automatic captions:** a small number of YouTube videos have only automatic captions (shown in the header).
- **LinkedIn:** posts with images or video and image comments have no text.

## Reliability of source types

1. Text the person wrote from their own account: verbatim.
2. Speaker-labelled podcast transcript: verbatim (the transcript may contain small spelling errors).
3. Video/podcast transcript without speaker separation: said in the recording, but who said it must be worked out
   from the surrounding text.
4. Press interviews and summary articles: the journalist's account. Present them as "according to X"; do not treat
   even words given in quotation marks as verbatim.
