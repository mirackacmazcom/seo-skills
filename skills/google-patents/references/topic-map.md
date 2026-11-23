# Topic map: SEO concept → patents and search terms

This file connects common SEO concepts to patents in the archive and to English search terms that work. Every
patent listed has been verified in the archive (November 2026), but it is a **starting point**: open and read it with
`show`, `claims` and `passages` before answering. Product-name mappings (Panda, Navboost and so on) are the SEO
community's interpretation; the patent texts do not mention these names.

## Contents

1. Links and PageRank
2. Anchor text
3. User behaviour and clicks
4. Site quality
5. Trust, authority and authors
6. Freshness and historical data
7. Spam and manipulation
8. Crawling and sitemaps
9. Duplicate content and canonicalisation
10. Indexing and the phrase-based system
11. Query understanding: rewriting, synonyms, autocomplete
12. Result presentation: snippets, answer boxes, answer passages
13. Entities and knowledge panels
14. Personalisation
15. Local search
16. News, image and video search
17. AI and generative search (AI Overviews)
18. Web performance and page speed

---

## 1. Links and PageRank

| Patent | Priority | Note |
|---|---|---|
| `US6285999B1` Method for node ranking in a linked database | 1997 | The original PageRank patent. Owned by Stanford University (`affiliate:stanford_pagerank`); its family has 10 publications (`family US6285999`). |
| `US7716225B1` Ranking documents based on user behavior and/or feature data | 2004 | The phrase "reasonable surfer model" appears in the description: not every link is equally likely to be clicked. |
| `US6526440B1` Ranking search results by reranking the results based on local inter-connectivity | 2001 | Reranking based on links within the result set (referred to as LocalRank). |
| `US9165040B1` Producing a ranking for pages using distances in a web-link graph | 2006 | Link distance from seed pages. |
| `US7783639B1` Determining quality of linked documents | 2004 | The score is based on the scores of the linking documents and the relationship (affiliation) between documents. |

Search: `search '"link graph"' rank`, `search inbound links weight --in claims --granted --core`,
`search '"random surfer"'`, `search '"seed"' pages distance link`.

## 2. Anchor text

| Patent | Priority | Note |
|---|---|---|
| `US7260573B1` Personalizing anchor text scores in a search engine | 2004 | |
| `US7716225B1` (above) | 2004 | Link features and anchor text appear in the claims. |
| `US7346839B2` Information retrieval based on historical data | 2003 | Changes in anchor text over time ("data relating to anchor text" in Claim 1). |

Search: `search '"anchor text"' --in claims --granted`, `search '"anchor text"' change over time`.

## 3. User behaviour and clicks

| Patent | Priority | Note |
|---|---|---|
| `US8661029B1` Modifying search result ranking based on implicit user feedback | 2006 | Weighting clicks by viewing time is also protected in dependent claims (Claims 3–7); the example weight numbers are only in the description [¶45]. In SEO circles it is associated with Navboost; that name does not appear in the patent texts. |
| `US8938463B1` Modifying search result ranking based on implicit user feedback and a model of presentation bias | 2007 | Correcting for position (presentation) bias. |
| `US7962462B1` Deriving and using document and site quality signals from search query streams | 2005 | Quality signals from query streams. |
| `US9195944B1` Scoring site quality | 2012 | A site quality score from visit durations. |
| `US9092510B1` Modifying search result ranking based on a temporal element of user feedback | 2007 | The age of click data. |
| `US8694511B1` Modifying search result ranking based on populations | 2007 | Separating by user populations such as language and country. |
| `US8868565B1` Calibrating click duration according to context | 2012 | Calibrating click duration according to context. |
| `US8694374B1` Detecting click spam | 2007 | Filtering out fake clicks. |
| `US8615514B1` Evaluating website properties by partitioning user feedback | 2010 | Site-level user feedback. |
| `US8819004B1` Ranking image search results using hover data | 2012 | Mouse hover data in image search. |

Search: `search '"implicit user feedback"'`, `search '"long click"' OR '"short click"'`,
`search '"click data"' ranking --granted`, `search click duration --in title`, `search '"presentation bias"'`.
Instead of "dwell time", patents mostly say "viewing time", "click duration" or "long click".

## 4. Site quality

| Patent | Priority | Note |
|---|---|---|
| `US9031929B1` Site quality score | 2012 | The ratio of queries referring to the site to clicks on the site. Navneet Panda is a co-inventor. |
| `US8682892B1` Ranking search results | 2012 | Navneet Panda; a group-level calculation for groups of resources, based on the number of independent incoming links. |
| `US9684697B1` Ranking search results | 2012 | Same period, same circle of inventors. |
| `US9767157B2` Predicting site quality | 2013 | Predicting the quality of new sites with a phrase model. |
| `US9002832B1` Classifying sites as low quality sites | 2012 | Classification based on the quality groups of the resources linking to the site. |

Search: `search site quality score --core`, `search '"low quality"' site classify --in abstract`,
`inventor Navneet Panda`.

## 5. Trust, authority and authors

| Patent | Priority | Note |
|---|---|---|
| `US7603350B1` Search result ranking based on trust | 2006 | Ranking based on trust in the entities that label documents (referred to as TrustRank). |
| `US7565358B2` Agent rank | 2005 | Scoring the "agents" that sign content; the source of the author authority discussions. Its family has 8 publications. |
| `US8645396B2` Reputation scoring of an author | 2007 | Author reputation score. |

E-E-A-T is not a patent term; search with `expertise`, `trust`, `authoritative`, `reputation`.
Search: `search author reputation score`, `search trust rank label --core`, `search authoritative source --in claims`.

## 6. Freshness and historical data

| Patent | Priority | Note |
|---|---|---|
| `US7346839B2` Information retrieval based on historical data | 2003 | Document inception date, content changes, link and anchor text history, traffic, domain data (listed in Claim 1). The main source of the "sandbox" and domain age discussions. |
| `US7840572B2` Document scoring based on document inception date | 2003 | A continuation in the same family. Claim 1 lists how the inception date can be determined; one of the options is the domain's registration date ("a date on which a domain associated with the document is registered"). |
| `US8521749B2` Document scoring based on document inception date | 2003 | Another continuation in the same family. Claim 1 protects the rate at which links are created since the inception date (average rate at which links [...] are created). |
| `US9002867B1` Modifying ranking data based on document changes | 2010 | Weighting a result quality statistic for different versions of a document. |

Search: `search '"inception date"'`, `search '"history data"' score document`, `search stale fresh document ranking --core`,
`search '"domain"' registered inception date --in claims`.
This family is large and each continuation protects a different type of data: list the members with
`family US7346839` and read the relevant member with `claims <member>`.

## 7. Spam and manipulation

| Patent | Priority | Note |
|---|---|---|
| `US7509344B1` Method for detecting link spam in hyperlinked databases | 2003 | |
| `US8392823B1` Systems and methods for detecting hidden text and hidden links | 2003 | |
| `US8639680B1` Hidden text detection for search result scoring | 2012 | |
| `US7302645B1` Methods and systems for identifying manipulated articles | 2003 | |
| `US8473491B1` Systems and methods of detecting keyword-stuffed business titles | 2010 | Local business names. |
| `US8612436B1` Reverse engineering circumvention of spam detection algorithms | 2011 | |

Search: `search '"link spam"' OR '"web spam"'`, `search '"keyword stuffing"' OR '"hidden text"' OR cloaking --in description`,
`search doorway pages`, `search spam score document demote`.

## 8. Crawling and sitemaps

| Patent | Priority | Note |
|---|---|---|
| `US7725452B1`, `US8042112B1` Scheduler for search engine crawler | 2003 | Crawl scheduling and priority. |
| `US8666964B1` Managing items in crawl schedule | 2005 | |
| `US8862569B2` Method and techniques for determining crawling schedule | 2012 | |
| `US7769742B1` Web crawler scheduler that utilizes sitemaps from websites | 2005 | |
| `US7801881B1` Sitemap generating client for web crawler | 2005 | |
| `US7865497B1` Sitemap generation where last modified time is not available to a network crawler | 2008 | |
| `US7653617B2` Mobile sitemaps | 2005 | |

"Crawl budget" is not a patent term; search with `crawl rate`, `crawl schedule`, `refresh`, `host load`.
Search: `search crawl schedule --in title --granted`, `search sitemap --in abstract`, `topics crawling-and-indexing`.

## 9. Duplicate content and canonicalisation

| Patent | Priority | Note |
|---|---|---|
| `US7627613B1` Duplicate document detection in a web crawler system | 2003 | |
| `US8140505B1` Near-duplicate document detection for web crawling | 2005 | |
| `US6615209B1` Detecting query-specific duplicate documents | 2000 | |
| `US7711679B2` Phrase-based detection of duplicate documents in an information retrieval system | 2004 | |
| `US8055626B1` Detecting mirrors on the web | 2005 | |

Search: `search duplicate document detection --in title`, `search canonical url select --core`, `search '"near-duplicate"'`.

## 10. Indexing and the phrase-based system

| Patent | Priority | Note |
|---|---|---|
| `US7536408B2` Phrase-based indexing in an information retrieval system | 2004 | The first of the phrase-based indexing family (Anna Patterson). |
| `US8117223B2` Integrating external related phrase information into a phrase-based indexing information retrieval system | 2007 | |
| `US7711679B2` (above) | 2004 | |

Search: `search '"phrase-based"' --in title`, `search '"inverted index"' posting list --core --granted`,
`topics text-indexing`.

## 11. Query understanding: rewriting, synonyms, autocomplete

| Patent | Priority | Note |
|---|---|---|
| `US7953746B1` Contextual query revision | 2007 | |
| `US7870147B2` Query revision using known highly-ranked queries | 2005 | |
| `US7617205B2` Estimating confidence for query revision models | 2005 | |
| `US9514743B2` Query rewrite corrections | 2014 | |
| `US7636714B1` Determining query term synonyms within query context | 2005 | |
| `US8255376B2` Augmenting queries with synonyms from synonyms map | 2006 | |
| `US8055669B1` Search queries improved based on query semantic information | 2003 | Adding alternative terms that are semantically close to the query. |
| `US8930350B1` Autocompletion using previously submitted query data | 2009 | |
| `US7487145B1` Method and system for autocompletion using ranked results | 2004 | |

Search: `search '"query revision"' OR '"query rewriting"' --in title`, `search synonym query term --in title --granted`,
`search autocomplete --in title`, `search query intent classify --core`.

## 12. Result presentation: snippets, answer boxes, answer passages

| Patent | Priority | Note |
|---|---|---|
| `US8145617B1` Generation of document snippets based on queries and search results | 2005 | |
| `US9940367B1` Scoring candidate answer passages | 2014 | The source of the featured snippet / passage discussions. |
| `US9959315B1` Context scoring adjustments for answer passages | 2014 | A context score based on the passage's heading path on the page (heading vector). |
| `US10019513B1` Weighted answer terms for scoring answer passages | 2014 | |
| `US10180964B1` Candidate answer passages | 2014 | |
| `US9355175B2` Triggering answer boxes | 2010 | |
| `US8538982B2` Framework for selecting and presenting answer boxes relevant to user input as query suggestions | 2009 | |

"Featured snippet" is not a patent term; search with `answer passage`, `answer box`, `direct answer`.
Search: `search answer passage scoring --in title`, `search snippet generating --in title`,
`search '"structured data"' OR markup search result --core`.

## 13. Entities and knowledge panels

| Patent | Priority | Note |
|---|---|---|
| `US10235423B2` Ranking search results based on entity metrics | 2012 | |
| `US9268820B2` Providing knowledge panels with search results | 2011 | |
| `US10922326B2` Triggering knowledge panels | 2012 | |
| `US9477711B2` Knowledge panel | 2012 | |
| `US10402410B2` Contextualizing knowledge panels | 2015 | |

Search: `search '"knowledge panel"' --in title`, `search entity metric rank`, `search '"knowledge graph"' --core`,
`topics knowledge-graph`.

## 14. Personalisation

| Patent | Priority | Note |
|---|---|---|
| `US9298777B2` Personalization of web search results using term, category, and link-based user profiles | 2003 | |
| `US7523096B2` Methods and systems for personalized network searching | 2003 | A large family (14 publications). |
| `US7827170B1` Systems and methods for demoting personalized search results based on personal information | 2007 | |
| `US8832132B1` Personalizing search queries based on user membership in social network communities | 2004 | |

Search: `search personalized search results user profile --in title`, `topics personalized-search`.

## 15. Local search

| Patent | Priority | Note |
|---|---|---|
| `US8626766B1` Systems and methods for ranking and importing business listings | 2011 | |
| `US7827176B2` Methods and systems for endorsing local search results | 2004 | |
| `US9792330B1` Identifying local experts for local search | 2013 | |
| `US9348925B2` Locally significant search queries | 2010 | |
| `US8473491B1` Systems and methods of detecting keyword-stuffed business titles | 2010 | |

Search: `search '"local search"' OR '"business listing"' --in title`, `search location prominence business rank`,
`topics geographic-and-local-search`.

## 16. News, image and video search

| Patent | Priority | Note |
|---|---|---|
| `US7577655B2` Systems and methods for improving the ranking of news articles | 2003 | Ranking articles by the quality of the source they belong to. |
| `US7568148B1` Methods and apparatus for clustering news content | 2002 | |
| `US8819004B1` Ranking image search results using hover data | 2012 | |
| `US7933338B1` Ranking video articles | 2004 | |

Search: `search news article source rank --in title`, `search image search rank --in abstract --core`,
`topics image-search`, `topics video-search`.

## 17. AI and generative search (AI Overviews)

"AI Overview" is a product name and does not appear in patents; patents say "natural language (NL) based summary",
"generative summary", "large language model (LLM)", "generative model".

| Patent | Priority | Note |
|---|---|---|
| `US11769017B1` Generative summaries for search results | 2022 | Generating a summary from search result documents with an LLM. Its family has five US publications (including `US11886828B1`, `US11900068B1`, `US12118325B2`); the claims of each protect a different aspect. `WO2024145537A1` and `US20250005303A1`, with the same title, are recorded under separate family numbers in the data source; the `family` command shows them under "Other families with the same title". |
| `US12437016B2` Fine-tuning large language model(s) using reinforcement learning with search engine feedback | 2023 | |
| `US12639300B2` Utilizing large language model (LLM) in responding to multifaceted queries | 2023 | |
| `US12277635B1` User verification of a generative response to a multimodal query | 2023 | |
| `US12620394B2` Query response interface with server side generative model(s) | 2024 | |
| `WO2025240274A1` Generative model based decomposition of input query into sub-queries and generation of comprehensive response based on responses to sub-queries | 2024 | Splitting a query into sub-queries (referred to as "query fan-out"). Full text taken from the Google Patents page. |
| `WO2024137088A1` Search with machine-learned model-generated queries | 2022 | Full text taken from the Google Patents page. |

Most of this area consists of filings from 2023 onwards: many are in `application` status and their claims may
change.
Search: `search generative summary search result --ai`, `search '"large language model"' search result document --ai --from 2022`,
`search LLM sub-queries --ai`, `search '"natural language based summary"'`, `search grounding OR citation LLM response source --ai`.

## 18. Web performance and page speed

| Patent | Priority | Note |
|---|---|---|
| `US9928223B1` Methods for prerendering and methods for managing and configuring prerendering operations | 2011 | Chrome prerendering. |
| `US8826153B2` Speculative actions based on user dwell time over selectable content | 2011 | |
| `US8341245B1` Content-facilitated speculative preparation and rendering | 2011 | |
| `US9330074B2` Style sheet speculative preloading | 2013 | |
| `US9203684B1` Reduction of web page load time using HTTP header compression | 2010 | |
| `US9201929B1` Ranking a search result document based on data usage to load the search result document | 2013 | A rare example that ties the cost of loading a page to ranking. |

Most patents on this topic describe browser and network engineering, not ranking. "Core Web Vitals" is not a patent
term; search with `page load time`, `latency`, `prerender`, `prefetch`, `render`.
Search: `search prerender OR prefetch --in title --perf`, `search '"page load"' time ranking --core`,
`search '"load time"' search result rank --in claims`.
