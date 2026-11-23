# Background: the archive's scope, source types and limits

Read this file when the user asks about the archive itself, how binding a source is, how current a page is, or what
is missing. For current numbers run `python3 scripts/gdocs.py stats`; the numbers below reflect the day the database
was built.

## Contents

1. What the archive is
2. Collections and how much weight each carries
3. How to read the dates
4. Languages and translations
5. Source types (official Markdown, HTML conversion, Internet Archive copy, PDF)
6. Known gaps
7. What the official documentation does and does not say
8. Where the database comes from

## 1. What the archive is

An offline copy, captured on 11 November 2026, of the pages Google **itself has published** on search, SEO, ranking,
technical SEO, performance and AI: 3,630 documents, about 3.3 million words of English text, Google's own Turkish
versions of 1,086 pages, and 471 blog posts published only in another language.

The starting point is Search Central (`developers.google.com/search`). The whole of that site was captured, along with
the crawling documentation, PageSpeed Insights, the Search Console API, web.dev, Lighthouse/CrUX, How Search Works and
the Search Console Help Center; Google pages linked from the documentation (blogs, help pages of other products,
Cloud, Android, Firebase, PDFs) were added as well. Non-Google sites (schema.org, MDN, Wikipedia…) are not in the
archive.

This archive is **not a leak or a patent collection**: everything in it is Google's public, official account.

## 2. Collections and how much weight each carries

| Code | Content | How to treat it |
|---|---|---|
| `docs` | Search Central documentation (164 pages) | Google's **current, authoritative** guidance. If a rule is asked about, look here first. |
| `crawling` | Crawling infrastructure documentation | Current; the definitive reference for Googlebot and robots.txt. |
| `search-misc` | Updates list, FAQs, Indexing API, case studies, events, status dashboard | The updates list and FAQs are current. |
| `office-hours` | SEO office hours transcripts (2022–2024) | Spoken answers by Google staff to individual questions. They describe the situation at the time; not part of the `core` group. |
| `sc-help` | Search Console Help Center | Definitions of reports and tools. Google gives no date on most pages. |
| `hsw` | How Search Works | Plain explanation written for a general audience; little technical detail. |
| `pdf` | Search Quality Rater Guidelines and other PDFs | The guidelines are a handbook for raters; they do not describe the ranking algorithm (§7). |
| `blog` | Search Central blog, 2005–2026 (more than 1,600 posts) | An announcement **as of the day it was published**. Old posts may no longer hold; always give the date. |
| `webdev`, `chrome`, `psi` | web.dev, Chrome for Developers, PageSpeed Insights | The primary source for performance metrics and tools. These are Chrome team documents; `docs` makes the link to search ranking. |
| `sc-api` | Search Console API reference | Technical reference. |
| `gblog` | The Keyword, Official Google Blog, Security Blog… | Corporate announcements; marketing language may dominate. |
| `help-other` | Help pages of other products (Merchant Center, Web Search, News, Tag Manager…) | Only pages linked from the Search documentation; the primary source for that product's rules. |
| `other` | Other cited Google pages (Cloud, Android, Firebase…) | A side source; not the main documentation for the topic. |

By default `search` puts current documentation ahead of old blog posts. Use `--flat` to rank by text match only, and
`--in docs` or `--in core` (the official guidance without the blog) to narrow the scope.

If two sources contradict each other: the current `docs` page overrides the old blog post. To find when a rule
changed, search the `search/updates` page (`passages search/updates <term>`).

## 3. How to read the dates

The dates line in `show` output can show three different things:

- **published**: the day a blog post was published (read from its address and text).
- **last updated**: the last-updated date Google states on the page. Documentation pages have this; they have no
  publication date.
- **archived**: the day the page was copied into this archive (2026-11-11). Changes Google made after this date are
  not in the archive.

In the answer, give the publication year for blog posts and "as of the archive date" for documentation pages. If the
user asks about "right now" and the topic changes quickly (AI features, structured data types, spam policies), state
the archive date explicitly.

## 4. Languages and translations

- The main text is English, and search runs on the English text by default. Base quotes on the English text.
- Google's own Turkish versions of 1,086 pages are included (`show <doc> --translation`). About a third are human
  translations and the rest Google's machine translations; `show` says which. Terms can be inconsistent in machine
  translations; if the translated text and the English text differ, the English text applies. All of the Search
  Central documentation, most Search Console Help pages and about a quarter of the blog posts have a Turkish version.
  web.dev, Chrome and How Search Works pages have none.
- To search the translated text use `--lang tr`. This index is accent-insensitive and matches substrings: typing
  `yonlendirme` also finds "yönlendirmeleri". Terms shorter than three letters cannot be searched.
- 471 blog posts were published only in another language (German 160, Spanish 128, Japanese 102, Chinese 45,
  French 15, Indonesian 12 and others). Their English page is a one-sentence note; the text is stored in the original
  language and searched with `--lang de` (or `--lang all`). Most are announcements of local events.

## 5. Source types

The "source" line in `show` output says where the text comes from:

- **Google's official Markdown version** (the large majority of documents): the Markdown output Google serves for the
  page. The cleanest text.
- **Text converted from HTML** (help pages, Google blogs and the translated versions): the page's HTML was converted
  to Markdown. The content is the same; table and list formatting may be imperfect.
- **Internet Archive copy**: when a page cannot be fetched from the live site, its copy on web.archive.org is used,
  and the copy date appears in `show` output. The current database has no pages of this type (all help pages were
  fetched from the live site); they may appear if the archive is updated later. If you see one, give the copy date in
  your citation.
- **PDF text extract** (7 files): plain text extracted from the PDF. The Search Quality Rater Guidelines are split by
  their numbered sections, and each section's page range is recorded; give the section number and page when quoting
  (e.g. "§2.3, p. 11"). Tables and example screenshots can look messy because they were flattened into plain text;
  there are no images.

## 6. Known gaps

- **The Search Console Help Center is extensive but not guaranteed to be complete.** Only pages reachable by links were
  captured. If the help page you are looking for is missing, say so; do not say "Google publishes no such page".
- **Help centers of other products are incomplete.** For products such as Merchant Center, Web Search, News and Tag
  Manager, only pages linked from the Search documentation are included (`list help-other`). The rest of those help
  centers is not in the archive.
- **No help forum threads.** The content of `support.google.com/…/thread/…` addresses is loaded later in the browser,
  so it could not be captured; forum announcements linked from the documentation are empty in the archive.
- **No images or videos.** Their captions or links appear in the text.
- **No tools that require sign-in** (the Search Console reports themselves, testing tools), YouTube videos or non-Google
  sites.
- **No removed pages.** Old documentation Google has deleted (e.g. structured data types that are no longer supported)
  is not in the archive; traces of it remain on the `search/updates` page and in old blog posts. If you give an old
  address, the tool follows it to the new one or says the address no longer exists on Google.

Something not being in the archive does not prove that Google has said nothing on the topic; it only shows that it
does not appear in the official pages in this archive.

## 7. What the official documentation does and does not say

- The documentation says **what Google recommends, what it supports and what it treats as a policy violation**. It does
  not give the weights, thresholds or a complete list of ranking signals. A question like "does it affect ranking" can
  usually be answered at the level of "Google says the following".
- The language is deliberately cautious: "may", "can", "we recommend", "is not a ranking factor". Do not lose this
  nuance when paraphrasing or translating; "recommends" and "requires", "can use" and "uses" are not the same thing.
- **The Search Quality Rater Guidelines** describe how human raters should score search results. In Google's own words
  these ratings do not directly change the ranking of individual pages; they are used to measure whether the systems
  work well. Do not present a criterion from the guidelines as a "ranking factor".
- **Blog posts** are announcements and describe the situation on the day they were written; later changes are not
  corrected in the post.
- **Office hours transcripts** are spoken answers by Google staff to individual questions; they are not as binding as
  official policy text, but they are valuable for practical detail.
- **web.dev and Lighthouse** describe good engineering practice. A Lighthouse audit or a PageSpeed score is not, on its
  own, a ranking signal; only `docs/appearance/page-experience` and `docs/appearance/core-web-vitals` make the link to
  ranking.

If the user also has the `google-leak` and `google-patents` skills, the three sources complement each other:

- **Official documentation** (this skill): what Google tells the public and what it recommends.
- **The leak** (`google-leak`): what data Google's internal systems store, and under which names.
- **Patents** (`google-patents`): how a method is described.

The three can say different things on the same topic; in the answer, state which information comes from which source
and do not present one as evidence for another.

## 8. Where the database comes from

The database (about 67 MB) is hosted on seoskills.io and searched through its API; nothing is downloaded (see "How searches run" in `SKILL.md`).
