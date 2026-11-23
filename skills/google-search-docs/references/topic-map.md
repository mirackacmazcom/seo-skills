# Topic map: SEO concept → official page and search terms

This file shows which pages in the archive cover frequently asked topics and which English terms to search for. The
pages listed are starting points; open each one with `show` and read the relevant section, do not pass on content
from here. Keys can be given to the `show` command as they are (e.g. `show search/docs/essentials/spam-policies`).

Short forms: `docs/…` = `search/docs/…` (Search Central documentation), `blog/…` = `search/blog/…`,
`help/N` = `support.google.com/webmasters/answer/N`, `SQRG` = Search Quality Rater Guidelines (`show sqrg`).

## Contents

1. Core principles and spam policies
2. Helpful content, E-E-A-T, YMYL, Search Quality Rater Guidelines
3. Ranking systems and updates
4. How Search works
5. Crawling: Googlebot, crawl budget, robots.txt, status codes
6. Indexing controls: noindex, robots meta, removals
7. Canonical URLs and duplicate content
8. Redirects and site moves
9. Sitemaps
10. JavaScript, mobile-first indexing, AMP
11. URL structure and links
12. Appearance in search results: title, snippet, site name, date
13. Structured data and rich results
14. Images, video, Discover, News, Web Stories
15. AI: AI features, generative AI content, controls
16. Page experience, Core Web Vitals, PageSpeed Insights, Lighthouse, CrUX
17. International and multilingual sites
18. E-commerce
19. Search Console reports and tools
20. Traffic drops, manual actions, security issues
21. Myths, things Google says "don't focus on", hiring an SEO
22. History: landmark blog posts
23. Tracking recent changes

---

## 1. Core principles and spam policies

Questions: "what are Google's rules", "does X count as spam", "cloaking / doorway / keyword stuffing", "parasite SEO",
"renting out a subfolder or subdomain", "coupon section", "white-label content", "expired domain",
"scaled content".

- `docs/essentials` — Search Essentials: technical requirements, spam policies, key best practices
- `docs/essentials/technical` — the minimum technical requirements for a page to be indexable
- `docs/essentials/spam-policies` — all the spam policies; each policy is its own section (cloaking, doorway abuse,
  expired domain abuse, hidden text, keyword stuffing, link spam, scaled content abuse, scraping, site reputation
  policy, sneaky redirects, thin affiliation, user-generated spam)
- `docs/appearance/spam-updates` — spam updates and SpamBrain
- `blog/2024/03/core-update-spam-policies`, `blog/2024/11/site-reputation-abuse`,
  `blog/2026/08/update-site-reputation-policy` — announcements of the policies
- `help/9044175` — Manual actions report: the consequence of each policy violation and the steps to fix it

Terms: `cloaking`, `doorway`, `"scaled content abuse"`, `"site reputation"`, `"expired domain"`,
`"keyword stuffing"`, `"thin affiliate"`, `"link spam"`, `"manual action"`.

Note: the name and content of the site reputation policy have changed. The 2024 announcements use the name "site
reputation abuse" and say that the host site's involvement does not change the outcome; the current documentation
(August 2026) uses the name "site reputation policy", looks at the host site's contribution and editorial oversight,
and contains a separate provision for the EEA. Base the answer on the current documentation; use the blog posts only
for history.

## 2. Helpful content, E-E-A-T, YMYL, Search Quality Rater Guidelines

Questions: "is E-E-A-T a ranking factor", "what is YMYL", "is author information required", "how is quality content
defined", "do raters affect rankings".

- `docs/fundamentals/creating-helpful-content` — self-assessment questions, the E-E-A-T section, Who/How/Why
- `sqrg` — Search Quality Evaluator Guidelines (PDF, numbered sections). Key sections: 2.3 YMYL, 3.1 Page
  Quality Rating Considerations, 3.4 E-E-A-T, 4.x Lowest Quality, 5.x Low Quality, 7.x High, 8.x Highest,
  the Needs Met sections. Search with `passages sqrg <terms>`.
- `sqrg-overview` — a short overview PDF describing the raters' role
- `www.google.com/search/howsearchworks/how-search-works/rigorous-testing` — how the ratings are used
- `blog/2022/12/google-raters-guidelines-e-e-a-t` — the addition of "Experience"
- `docs/fundamentals/seo-starter-guide` — the "Things we believe you shouldn't focus on" section (including E-E-A-T)

Terms: `E-E-A-T`, `YMYL`, `"people-first"`, `"quality rater"`, `trust`, `"main content"`, `"reputation"`.

Note: the SQRG is a handbook given to raters; it is not a description of the ranking algorithm. You can verify Google's
own wording with `find "E-E-A-T itself isn't a specific ranking factor"`.

## 3. Ranking systems and updates

Questions: "which ranking systems are there", "what to do after a core update", "does the helpful content system still
exist", "reviews system", "is PageRank still used".

- `docs/appearance/ranking-systems-guide` — the list of named systems (BERT, PageRank, RankBrain, reviews,
  site diversity, spam detection…) and the retired ones
- `docs/appearance/core-updates` — core updates and recovery
- `docs/appearance/reviews-system` — the reviews system; `docs/specialty/ecommerce/write-high-quality-reviews`
- `www.google.com/search/howsearchworks/how-search-works/ranking-results` — the factors considered in ranking (meaning,
  relevance, quality, usability, context)
- `search/help/site-position-in-search-faq` — ranking position FAQ
- Blog: `blog/2019/08/core-updates`, `blog/2022/08/helpful-content-update`, `blog/2024/08/august-2024-core-update`

Terms: `"core update"`, `"ranking systems"`, `"helpful content system"`, `"reviews system"`, `PageRank`,
`"site diversity"`, `freshness`.

## 4. How Search works

- `docs/fundamentals/how-search-works` — crawling, indexing, serving results (technical account)
- `www.google.com/search/howsearchworks/how-search-works` and its subpages (`organizing-information`,
  `ranking-results`, `detecting-spam`, `rigorous-testing`)
- `docs/fundamentals/seo-starter-guide`, `docs/fundamentals/get-started`, `docs/fundamentals/get-started-developers`

## 5. Crawling: Googlebot, crawl budget, robots.txt, status codes

Questions: "crawl budget", "verifying Googlebot IPs", "robots.txt rule", "how are 5xx / 429 / 404 handled",
"reducing the crawl rate", "faceted navigation".

- `crawling/docs/about-crawling`, `crawling/docs/myths-about-crawling`
- `crawling/docs/crawl-budget` — crawl budget for large sites
- `crawling/docs/faceted-navigation` — filtered navigation URLs
- `crawling/docs/crawlers-fetchers/overview-google-crawlers`, `…/google-common-crawlers`,
  `…/google-special-case-crawlers`, `…/google-user-triggered-fetchers`, `…/verify-google-requests`,
  `…/reduce-crawl-rate`
- `docs/crawling-indexing/googlebot`
- robots.txt: `crawling/docs/robots-txt/robots-txt-spec` (exact syntax), `…/create-robots-txt`,
  `…/useful-robots-txt-rules`, `docs/crawling-indexing/robots/intro`
- `crawling/docs/troubleshooting/http-status-codes`, `…/dns-network-errors`,
  `docs/crawling-indexing/troubleshoot-crawling-errors`
- Help: `help/9679690` (Crawl Stats report), `help/6062598` (robots.txt report)

Terms: `"crawl budget"`, `"crawl rate"`, `Googlebot`, `"user agent"`, `disallow`, `robots.txt`, `429`, `503`.

## 6. Indexing controls: noindex, robots meta, removals

- `docs/crawling-indexing/block-indexing` — noindex
- `docs/crawling-indexing/robots-meta-tag` — robots meta, `data-nosnippet`, `X-Robots-Tag`, all the `max-snippet`,
  `nosnippet`, `notranslate`, `unavailable_after` rules
- `docs/crawling-indexing/special-tags` — the meta tags Google supports
- `docs/crawling-indexing/control-what-you-share`, `…/remove-information`, `…/prevent-images-on-your-page`,
  `…/keep-redacted-information-out`, `…/ask-google-to-recrawl`, `…/indexable-file-types`
- `search/help/crawling-index-faq`
- Help: `help/7440203` (Page indexing report and what the statuses mean), `help/9012289` (URL Inspection),
  `help/9689846` (Removals tool), `help/7474347` (why is my page missing)

Terms: `noindex`, `nosnippet`, `"X-Robots-Tag"`, `"crawled currently not indexed"`, `"discovered currently not
indexed"`, `"removal"`.

## 7. Canonical URLs and duplicate content

- `docs/crawling-indexing/canonicalization` — how Google chooses the canonical
- `docs/crawling-indexing/consolidate-duplicate-urls` — rel="canonical", redirect and sitemap methods
- `docs/crawling-indexing/canonicalization-troubleshooting`
- Help: `help/10347851` (glossary: canonical)

Terms: `canonical`, `duplicate`, `"rel=canonical"`, `syndicated`.

## 8. Redirects and site moves

- `docs/crawling-indexing/301-redirects` — permanent/temporary, server-side, meta refresh, JavaScript redirects
- `docs/crawling-indexing/site-move-with-url-changes`, `…/site-move-no-url-changes`
- `docs/crawling-indexing/pause-online-business`, `…/website-testing` (A/B testing)
- Help: `help/9370220` (Change of Address tool)

Terms: `redirect`, `301`, `302`, `"site move"`, `migration`, `"change of address"`.

## 9. Sitemaps

- `docs/crawling-indexing/sitemaps/overview`, `…/build-sitemap`, `…/large-sitemaps`, `…/image-sitemaps`,
  `…/video-sitemaps`, `…/news-sitemap`, `…/combine-sitemap-extensions`
- Help: `help/7451001` (Sitemaps report)

Terms: `sitemap`, `lastmod`, `"sitemap index"`, `changefreq`, `priority`.

## 10. JavaScript, mobile-first indexing, AMP

- `docs/crawling-indexing/javascript/javascript-seo-basics`, `…/fix-search-javascript`, `…/dynamic-rendering`,
  `…/lazy-loading`
- `docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing`
- `docs/crawling-indexing/amp` and its subpages
- Blog: `blog/2019/05/the-new-evergreen-googlebot`, `blog/2016/11/mobile-first-indexing`,
  `blog/2020/03/announcing-mobile-first-indexing-for`

Terms: `rendering`, `"JavaScript SEO"`, `"dynamic rendering"`, `"lazy loading"`, `"mobile-first indexing"`.

## 11. URL structure and links

- `docs/crawling-indexing/url-structure`
- `docs/crawling-indexing/links-crawlable` — crawlable links, anchor text, internal links
- `docs/crawling-indexing/qualify-outbound-links` — `nofollow`, `sponsored`, `ugc`
- `docs/essentials/spam-policies` → the "Link spam" section
- Blog: `blog/2019/09/evolving-nofollow-new-ways-to-identify`, `blog/2021/07/link-tagging-and-link-spam-update`,
  `blog/2022/12/december-22-link-spam-update`, `blog/2016/09/penguin-is-now-part-of-our-core`
- Help: `help/9049606` (Links report), `help/2648487` (disavowing links)

Terms: `"anchor text"`, `nofollow`, `sponsored`, `"link spam"`, `disavow`, `"internal links"`.

## 12. Appearance in search results: title, snippet, site name, date

- `docs/appearance/title-link`, `docs/appearance/snippet` (including meta description),
  `docs/appearance/featured-snippets`, `docs/appearance/sitelinks`, `docs/appearance/site-names`,
  `docs/appearance/favicon-in-search`, `docs/appearance/publication-dates`
- `docs/appearance/visual-elements-gallery` — the names of the elements on the results page
- `docs/appearance/avoid-intrusive-interstitials`, `docs/appearance/translated-results`,
  `docs/appearance/preferred-sources`
- `search/help/site-appearance-faq`
- Blog: `blog/2021/08/update-to-generating-page-titles`, `blog/2021/09/more-info-about-titles`

Terms: `"title link"`, `"meta description"`, `snippet`, `"site name"`, `favicon`, `"featured snippet"`, `byline`.

## 13. Structured data and rich results

- `docs/appearance/structured-data/intro-structured-data`, `…/sd-policies` (general rules),
  `…/search-gallery` (list of supported types)
- Type pages `docs/appearance/structured-data/<type>`: `article`, `breadcrumb`, `product`, `product-snippet`,
  `merchant-listing`, `product-variants`, `review-snippet`, `local-business`, `organization`, `event`, `recipe`,
  `video`, `job-posting`, `qapage`, `profile-page`, `discussion-forum`, `dataset`, `course`, `software-app`,
  `return-policy`, `shipping-policy`, `loyalty-program`, `paywalled-content`, `speakable`, `carousel`…
  Full list: `list docs --path structured-data --limit 0`.
- `…/generate-structured-data-with-javascript`
- Help: `help/7552505` (rich result reports), `help/9166415` (unparsable data), `help/7445569`
  (Rich Results Test)

Terms: type name + `required` / `recommended` / `"JSON-LD"`; for removed types `deprecated`, `"no longer"`.

Note: read whether a property is required or recommended from the table on the type page; do not write it from memory,
these tables change often. A type with no page in the archive is either not supported or its support has been
removed; look up when and why it was removed in the updates list in §23.

## 14. Images, video, Discover, News, Web Stories

- `docs/appearance/google-images`, `docs/appearance/structured-data/image-license-metadata`
- `docs/appearance/video`, `docs/appearance/structured-data/video`; help: `help/9495631` (Video indexing)
- `docs/appearance/google-discover`; help: `help/9216516`
- `www.google.com/search/howsearchworks/how-news-works`, `docs/crawling-indexing/sitemaps/news-sitemap`,
  `docs/appearance/flexible-sampling`; help: `help/10083653` (Google News performance report)
- `docs/appearance/enable-web-stories`, `…/web-stories-content-policy`, `…/web-stories-creation-best-practices`

## 15. AI: AI features, generative AI content, controls

Questions: "what should I do to appear in AI Overviews", "is AI content banned", "can I opt out of AI Overviews",
"what is Google-Extended for", "is llms.txt needed", "GEO / AEO".

- `docs/appearance/ai-features` — AI Overviews and AI Mode: how they work, site owner controls, measurement
- `docs/fundamentals/ai-optimization-guide` — optimization guide for generative AI features
- `docs/fundamentals/using-gen-ai-content` — using generative AI content on a site
- `docs/essentials/spam-policies` → "Scaled content abuse"
- `docs/crawling-indexing/robots-meta-tag` — the effect of the `nosnippet`, `max-snippet` and `data-nosnippet` rules
  on AI features
- `help/16908024` — Search generative AI control: excluding a site from Search's generative AI features
- `docs/crawling-indexing/control-what-you-share` — all the methods for keeping content from Google; the current
  developer documentation that also mentions the generative AI control. `docs/appearance/ai-features` does not
  mention this control (it is dated earlier); for opt-out questions, rely on this page and the help page.
- `crawling/docs/crawlers-fetchers/google-common-crawlers` — Google-Extended and other tokens
- `developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt` — Lighthouse's llms.txt audit. This is a Chrome
  team page about AI agents and does not mention Google Search; whether Search uses this file is stated in
  `docs/fundamentals/ai-optimization-guide`. Do not confuse the two.
- Blog: `blog/2023/02/google-search-and-ai-content` (approach to AI-generated content),
  `blog/2025/05/succeeding-in-ai-search` (recommendations for visibility in AI experiences),
  `blog/2026/06/gen-ai-performance-reports` (generative AI performance reports in Search Console),
  `blog/2026/10/ai-training-control` (a control for AI training; not related to visibility in Search)
- `www.gstatic.com/gumdrop/files/hsw-mum-v5.pdf` — introduction to MUM

Note: opting out of AI features in Search, snippet controls and Google-Extended are separate things and are covered on
three separate pages (`help/16908024`, `docs/crawling-indexing/robots-meta-tag`,
`crawling/docs/crawlers-fetchers/google-common-crawlers`). Read from each page itself what it affects.

Terms: `"AI Overviews"`, `"AI Mode"`, `"generative AI"`, `"Google-Extended"`, `"scaled content"`, `nosnippet`,
`"query fan-out"`, `"llms.txt"`.

## 16. Page experience, Core Web Vitals, PageSpeed Insights, Lighthouse, CrUX

Questions: "is CWV a ranking factor", "LCP/INP/CLS thresholds", "difference between the PSI score and field data",
"does the Lighthouse score affect rankings".

- Relation to ranking: `docs/appearance/page-experience`, `docs/appearance/core-web-vitals`,
  `blog/2023/04/page-experience-in-search`, `blog/2020/05/evaluating-page-experience`
- Metrics: `web.dev/articles/vitals`, `web.dev/articles/lcp`, `web.dev/articles/inp`, `web.dev/articles/cls`,
  `web.dev/articles/ttfb`, `web.dev/articles/fcp`, `web.dev/articles/defining-core-web-vitals-thresholds`
- Improvement: `web.dev/articles/optimize-lcp`, `web.dev/articles/optimize-inp`, `web.dev/articles/optimize-cls`,
  `web.dev/articles/top-cwv`, `web.dev/articles/bfcache`, `web.dev/learn/performance`
- Lab and field data: `web.dev/articles/lab-and-field-data-differences`,
  `web.dev/articles/vitals-measurement-getting-started`
- PageSpeed Insights: `developers.google.com/speed/docs/insights/v5/about`
- CrUX: `developer.chrome.com/docs/crux`, `developer.chrome.com/docs/crux/methodology`,
  `developer.chrome.com/docs/crux/api`, `developer.chrome.com/docs/crux/history-api`
- Lighthouse: `developer.chrome.com/docs/lighthouse/overview`,
  `developer.chrome.com/docs/lighthouse/performance/performance-scoring`; SEO audits
  `list chrome --path lighthouse/seo`
- Help: `help/9205520` (Core Web Vitals report), `help/11396518` (HTTPS report)
- History: `blog/2010/04/using-site-speed-in-web-search-ranking`, `blog/2018/01/using-page-speed-in-mobile-search`,
  `blog/2023/05/introducing-inp`

Terms: `LCP`, `INP`, `CLS`, `"75th percentile"`, `"field data"`, `"lab data"`, `"page experience"`. Narrow performance
searches with `--in perf`.

Note: the defining source for the thresholds is the metric pages on web.dev. `docs/appearance/core-web-vitals` and
Search Console's Core Web Vitals report write the same thresholds in slightly different words; if they differ, give
each with its source. For the relation to ranking, read the relevant sections of `docs/appearance/page-experience`.

## 17. International and multilingual sites

- `docs/specialty/international/localized-versions` — hreflang (HTML, HTTP header, sitemap)
- `docs/specialty/international/managing-multi-regional-sites`, `…/locale-adaptive-pages`

Terms: `hreflang`, `"x-default"`, `ccTLD`, `"locale-adaptive"`, `geotargeting`.

## 18. E-commerce

- `docs/specialty/ecommerce` and its subpages: `designing-a-url-structure-for-ecommerce-sites`,
  `help-google-understand-your-ecommerce-site-structure`, `pagination-and-incremental-page-loading`,
  `share-your-product-data-with-google`, `include-structured-data-relevant-to-ecommerce`,
  `where-ecommerce-data-can-appear-on-google`, `how-to-launch-an-ecommerce-website`
- Product structured data: §13 (`product`, `merchant-listing`, `product-variants`, `return-policy`,
  `shipping-policy`)

Terms: `pagination`, `"load more"`, `"infinite scroll"`, `"product variants"`, `"Merchant Center"`.

## 19. Search Console reports and tools

- Getting started: `docs/monitor-debug/search-console-start`, `help/9128668`, `help/10267942`, `help/9133276`
- Performance: `help/7576553`, `help/7042828` (definitions of impressions, position, clicks), `help/17011165`,
  `help/17011259`; `docs/monitor-debug/google-analytics-search-console`, `docs/monitor-debug/bubble-chart-analysis`
- Index: `help/7440203`, `help/9012289`, `help/12482179`, `help/7451001`, `help/9689846`
- Experience and enhancements: `help/9205520`, `help/11396518`, `help/7552505`, `help/9495631`
- Site management: `help/34592` (adding a property), `help/9008080` (verification), `help/7687615` (users),
  `help/9370220`, `help/12919198` (bulk data export)
- API: `developers.google.com/webmaster-tools`, `…/webmaster-tools/v1/searchanalytics/query`,
  `…/webmaster-tools/v1/urlInspection.index/inspect`; Indexing API: `search/apis/indexing-api/v3/using-api`
- All of them: `list sc-help --limit 0`

Note: most Search Console Help pages carry no date from Google; the header shows only the date the page was archived.
For help pages of other products use `list help-other` (Merchant Center, Web Search, News, Tag Manager and others;
only pages linked from the documentation).

## 20. Traffic drops, manual actions, security issues

- `docs/monitor-debug/debugging-search-traffic-drops`, `help/9079473`
- `help/9044175` (Manual actions report: each action type and its fix), `help/9044101` (Security issues)
- `docs/monitor-debug/security/malware`, `…/social-engineering`, `…/prevent-malware`,
  `docs/monitor-debug/prevent-abuse`, `help/6347750`
- `search/help/report-quality-issues`, `search/help/debug`
- Explicit content and SafeSearch: `docs/specialty/explicit/guidelines`, `docs/specialty/explicit/troubleshooting`

Note: the archive cannot diagnose the user's site; report the possible causes the document lists.

## 21. Myths, things Google says "don't focus on", hiring an SEO

- `docs/fundamentals/seo-starter-guide` → "Things we believe you shouldn't focus on" (meta keywords, keyword
  stuffing, keywords in the domain name or URL, content length, subdomains / subdirectories, PageRank,
  duplicate content, number and order of headings, E-E-A-T)
- `crawling/docs/myths-about-crawling`
- `docs/fundamentals/do-i-need-seo`, `docs/fundamentals/third-party-seo`
- SEO office hours transcripts (2022–2024, Q&A): `list office-hours`; to search inside them
  `search <terms> --in office-hours`. The answers describe the situation at the time; if they contradict the current
  documentation, the documentation applies.

Terms: `myth`, `"word count"`, `"duplicate content penalty"`, `"domain age"`, `"bounce rate"`, `"LSI"`,
`"keyword density"`. Verify with `find` whether a claim appears in the official text.

## 22. History: landmark blog posts

These describe the situation on the date they were published; for the current situation look at the relevant current
documentation.

| Topic | Post |
|---|---|
| Panda (2011) | `googleblog.blogspot.com/2011/02/finding-more-high-quality-sites-in.html`, `blog/2011/05/more-guidance-on-building-high-quality` |
| Penguin (2012, 2016) | `blog/2012/04/another-step-to-reward-high-quality`, `blog/2016/09/penguin-is-now-part-of-our-core` |
| Site speed (2010, 2018) | `blog/2010/04/using-site-speed-in-web-search-ranking`, `blog/2018/01/using-page-speed-in-mobile-search` |
| HTTPS (2014) | `blog/2014/08/https-as-ranking-signal` |
| Mobile-friendliness (2015) | `blog/2015/02/finding-more-mobile-friendly-search`, `blog/2015/04/rolling-out-mobile-friendly-update` |
| Mobile-first indexing (2016–2020) | `blog/2016/11/mobile-first-indexing`, `blog/2020/03/announcing-mobile-first-indexing-for` |
| Crawl budget (2017) | `blog/2017/01/what-crawl-budget-means-for-googlebot` |
| nofollow change (2019) | `blog/2019/09/evolving-nofollow-new-ways-to-identify` |
| BERT (2019) | `blog.google/products-and-platforms/products/search/search-language-understanding-bert` |
| Page experience (2020–2023) | `blog/2020/05/evaluating-page-experience`, `blog/2023/04/page-experience-in-search` |
| Product reviews (2021) | `blog/2021/04/product-reviews-update` |
| Helpful content (2022) | `blog/2022/08/helpful-content-update` |
| E-E-A-T (2022) | `blog/2022/12/google-raters-guidelines-e-e-a-t` |
| AI content (2023) | `blog/2023/02/google-search-and-ai-content` |
| March 2024 core update + spam policies | `blog/2024/03/core-update-spam-policies` |
| Site reputation abuse (2024, 2026) | `blog/2024/11/site-reputation-abuse`, `blog/2026/08/update-site-reputation-policy` |

To go through a particular year: `search <terms> --in blog --from 2011 --to 2012` or
`list blog --from 2024 --sort date`.

## 23. Tracking recent changes

- `search/updates` — "Latest documentation updates": a dated list of every change made to the documentation (long
  page; search it with `passages search/updates <term>`). The fastest way to find when a rule changed or when a
  feature was removed.
- `crawling/docs/changelog` — changelog of the crawling documentation
- `status.search.google.com/summary`, `search/help/status-dashboard` — update and incident records
- Newest blog posts: `list blog --sort date --limit 20`; most recently updated documentation:
  `list docs --sort updated --limit 20`
