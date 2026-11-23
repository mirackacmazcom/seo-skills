# Topic map: SEO concept → schema and field

This file was generated from the database; every schema and field name here really exists in the leak, and
the descriptions are taken from the document in shortened form. It is a **starting point**, not a complete list:
before using a field in an answer, read its full description with `leak.py show <Schema> --match <field>`, and
run `search` with the suggested terms to find other fields on the same topic.

The file is long; instead of reading all of it, find the relevant section in the table of contents below and read
only that section (e.g. get the line numbers with `grep -n '^## ' references/topic-map.md`).

## Contents

1. Main container schemas
2. Clicks and user behavior (NavBoost, "Craps")
3. Chrome data
4. Site authority and site quality (NSR)
5. Page quality and content (PQ, originality, length)
6. Algorithm names and demotion fields (Panda, Penguin, etc.)
7. Links, anchor text and PageRank
8. Domain age, "sandbox" and registration info
9. Spam
10. Dates and freshness
11. Authors, entities and topical focus
12. E-E-A-T, expertise and trust
13. Mobile and page experience
14. Indexing, crawling and tiers
15. Local search

## 1. Main container schemas

Most of the fields related to web search are gathered in these few schemas. For a broad question, open these first with `show --brief`.

- `PerDocData` (133 fields) — =========================================================================== # Make sure you read the comments in the bottom before you add any new field. NB: As noted in…
- `CompositeDoc` (45 fields) — Protocol record used for collecting together all information about a document. Please consult go/dj-explorer for two basic questions about `CompositeDoc`: - Where should…
- `CompressedQualitySignals` (39 fields) — A message containing per doc signals that are compressed and included in Mustang and TeraGoogle. For TeraGoogle, this message is included in perdocdata which means it ca…
- `QualityNsrNsrData` (60 fields) — NOTE: When adding a new field to be propagated to Raffia check if NsrPatternSignalSpec needs to be updated. Next ID: 63
- `QualityNsrPQData` (20 fields) — Next id: 22
- `DocProperties` (12 fields) — NOTE: In segindexer, the docproperties of a document may be reused from a previous cycle if its content is not changed. If you add a new field to DocProperties, make sur…
- `AnchorsAnchor` (39 fields) — no description in the document
- `AnchorsAnchorSource` (25 fields) — attributes of the source document for the link
- `IndexingDocjoinerAnchorStatistics` (50 fields) — Statistics of the anchors in a docjoin. Next available tag ID: 63.
- `QualityNavboostCrapsCrapsData` (23 fields) — NEXT TAG: 28
- `SmartphonePerDocData` (10 fields) — This message is used for storing smartphone related information. Note: MobilePerDocData is a similar message, but it's for lowend mobile.
- `CompositeDocIndexingInfo` (24 fields) — Contains information *mostly* used within indexing (e.g. not used for building the production serving shards). Most of this data is generated only in Alexandria, however…
- `IndexingDocjoinerDataVersion` (709 fields) — DataVersion tracks the version of data in CompositeDoc. The notion of "data" here is loose and people can define the name of their own. For example, a signal generated b…
- `WWWDocInfo` (69 fields) — Some per-doc info is returned for all www DocInfo requests. Next id: 94
- `ImageData` (99 fields) — This defines the per-doc data which is extracted from thumbnails and propagated over to indexing. It contains all information that can be used for restricts. Next tag id…
- `VideoContentSearchVideoInfo` (28 fields) — This message holds metadata and signals of one video. It is typically used for holding debug data in tables produced by offline pipelines related to video anchors. Pleas…
- `LocalWWWInfo` (12 fields) — Next Id: 36
- `RegistrationInfo` (2 fields) — Domain registration information for the document. NEXT ID TO USE: 3

## 2. Clicks and user behavior (NavBoost, "Craps")

Search terms: `navboost`, `craps`, `click`, `impression`, `pnav`, `ctr`, `firefly`. Schema prefix: `QualityNavboost`. Most of the counter fields have no description; the statements that say something about usage are in the schema descriptions and in the last entries below.

- `QualityNavboostCrapsCrapsData.goodClicks` (`number(double)`) — no description in the document
- `QualityNavboostCrapsCrapsData.badClicks` (`number(double)`) — no description in the document
- `QualityNavboostCrapsCrapsData.lastLongestClicks` (`number(double)`) — The number of clicks that were last and longest in related user queries.
- `QualityNavboostCrapsCrapsData.clicks` (`number(double)`) — no description in the document
- `QualityNavboostCrapsCrapsData.impressions` (`number(double)`) — These fields may become legacy fields; we may retire them and use the squashed field (below) instead, to allow for some nesting.
- `QualityNavboostCrapsCrapsData.squashed` (`QualityNavboostCrapsCrapsClickSignals`) — Not used yet - we will probably move the impressions / clicks / good_clicks bad clicks / last longest clicks into here from top level, and rename those fields to legacy.
- `QualityNavboostCrapsCrapsData.unsquashed` (`QualityNavboostCrapsCrapsClickSignals`) — We will start using this one for the retuning rollout.
- `QualityNavboostCrapsCrapsData.unscaledIpPriorBadFraction` (`number(double)`) — Used to assign a prior based on IP address. See quality/navboost/craps/craps-ip-prior.h. This value is prior to the linear transformation (scaling / offset / min / max) that's applied in cr…
- `QualityNavboostCrapsCrapsData.voterTokenCount` (`integer(int32)`) — The number of distinct voter tokens (a lower bound on the number of distinct users that contributed to the entry, used for privacy-related filtering).
- `QualityNavboostCrapsCrapsData.patternLevel` (`integer(int32)`) — Level of pattern. More general patterns get higher values. For URL patterns this field = 0. For example, if we have "http://abc.def.ghi/xyz.html" level 0 pattern will be "http://abc.def.ghi…
- `QualityNavboostCrapsCrapsData.device` (`QualityNavboostCrapsCrapsDevice`) — The device interface and os slice of the CrapsData.
- `QualityNavboostCrapsCrapsClickSignals.unsquashedClicks` (`number(double)`) — This is not being populated for the current format - instead two instances of CrapsClickSignals (squashed/unsquashed) are used. We are migrating to the new format where this field will be p…
- `QualityNavboostCrapsCrapsClickSignals.unsquashedLastLongestClicks` (`number(double)`) — no description in the document
- `QualityNavboostCrapsCrapsClickSignals.absoluteImpressions` (`number(double)`) — Thus far this field is only used for host level unsquashed impressions. When compressed (e.g., in perdocdata.proto, CompressedQualitySignals), this value is represented individually and thu…
- `QualityNavboostCrapsCrapsClickSignals.unicornClicks` (`number(double)`) — The subset of clicks that are associated with an event from a Unicorn user.
- `CompressedQualitySignals.crapsNewUrlSignals` (`string(uint64)`) — For craps_[url|pattern]_signals, please avoid accessing these fields directly, even in minor ways like checking has_craps_*. Instead, please use methods from quality/navboost/craps/craps-lo…
- `CompressedQualitySignals.crapsNewHostSignals` (`string(uint64)`) — no description in the document
- `CompressedQualitySignals.crapsNewPatternSignals` (`string(uint64)`) — no description in the document
- `CompressedQualitySignals.crapsAbsoluteHostSignals` (`integer(uint32)`) — Impressions, unsquashed, host level, not to be used with compressed ratios. Not to be used in Pattern Data.
- `CompressedQualitySignals.navDemotion` (`integer(uint32)`) — nav_demotion: converted from QualityBoost.nav_demoted.boost.
- `QualityNsrNsrData.pnav` (`number(float)`) — Fractional signals.
- `QualityNsrNsrData.pnavClicks` (`number(float)`) — denominator for the pnav computation
- `QualityNsrNsrData.directFrac` (`number(float)`) — no description in the document
- `QualityNsrNsrData.impressions` (`number(float)`) — Site-level impressions.
- `IndexingSignalAggregatorAgeWeightedCoverageData.lastGoodClickDateInDays` (`integer(int32)`) — Indicates the date when this document received the last good click. Note: The date is identified in terms of number of days since Epoch. **Note:** this schema is coverage data that belongs to the index selection side; do not present it as a ranking signal.
- `CompressedQualitySignals.crapsUnscaledIpPriorBadFraction` (`integer(uint32)`) — no description in the document
- `CountryMetroNBFeature.navboost` (`number(float)`) — This is the multiplier to apply to the result for this locale & query. NOTE: This is for serving purposes only and should not be populated in the index.
- `CountryCountryAttachment.metroNavboost` (`list<CountryMetroNBFeature>`) — Metro navboost: list of (NavBoost feature V2, navboost float) pairs.
- `CompositeDocIndexingInfo.rawNavboost` (`integer(int32)`) — The raw navboost count for the canonical url without aggregating the navboost from dup urls. This field is used when building forwarding map.
- `PerDocData.onsiteProminence` (`integer(uint32)`) — Onsite prominence measures the importance of the document within its site. It is computed by propagating simulated traffic from the homepage and high craps click pages. It is a 13-bit int.
- `PerDocData.fireflySiteSignal` (`QualityCopiaFireflySiteSignal`) — Contains Site signal information for Firefly ranking change. See http://ariane/313938 for more details.
- `QualityCopiaFireflySiteSignal.dailyClicks` (`string(int64)`) — no description in the document
- `QualityCopiaFireflySiteSignal.dailyGoodClicks` (`string(int64)`) — no description in the document
- `IndexingSignalAggregatorUrlPatternSignals` (6 fields) — Contains only the signals necessary to perform per-URL click prediction. Used by Index Selection for scoring. NEXT ID TO USE: 7
- `CompressedQualitySignals` (39 fields) — A message containing per doc signals that are compressed and included in Mustang and TeraGoogle. For TeraGoogle, this message is included in perdocdata which means it can be used in preliminary scoring. CAREFUL: For TeraGoogle, this data resides in very limited serving memory (Flash storage) for a huge number of documents. Next id: 44 **Note:** the `craps*` fields are where click data is carried to the document level: looking at the `QualityNavboostCrapsCrapsData` schema with `refs` shows no direct reference from a web document, because the data is carried in packed (uint64) fields such as `crapsNewUrlSignals`.

## 3. Chrome data

Search term: `chrome` (with `--name-only`; otherwise Chromecast/ChromeOS results get mixed in).

- `QualityNsrNsrData.chromeInTotal` (`number(float)`) — Site-level Chrome views.
- `QualitySitemapScoringSignals.chromeTransCount` (`string(uint64)`) — no description in the document
- `QualitySitemapScoringSignals.chromeTransProb` (`number(float)`) — no description in the document
- `QualitySitemapScoringSignals.chromeWeight` (`number(float)`) — no description in the document
- `QualitySitemapScoringSignals` (18 fields) — Scoring signals for computing the sitelink score. This message is currently intended only for debugging. Accordingly, this is populated in CDoc but not in MDU. It is enforced by the [(exclude_from_mdu) = true] annotation of the corresponding fields in Target and TargetGroup. **Note:** this schema belongs to sitelink scoring; it is not general web ranking.
- `VideoContentSearchVideoInfo.uniqueChromeViews` (`integer(int32)`) — Number of unique visits in Chrome.
- `IndexingDocjoinerDataVersion.chromeCounts` (`IndexingDocjoinerDataVersionVersionInfo`) — LINT.ThenChange(//depot/google3/indexing/ames/spanner/schema/websearch_main.sdl)
- `IndexingDocjoinerDataVersion.instantChromeViews` (`IndexingDocjoinerDataVersionVersionInfo`) — no description in the document

## 4. Site authority and site quality (NSR)

Search terms: `nsr`, `authority`, `site quality`, `qstar`. Schema prefixes: `QualityNsr`, `QualityAuthority`.

- `CompressedQualitySignals.siteAuthority` (`integer(uint32)`) — site_authority: converted from quality_nsr.SiteAuthority, applied in Qstar.
- `CompressedQualitySignals.authorityPromotion` (`integer(uint32)`) — authority promotion: converted from QualityBoost.authority.boost
- `CompressedQualitySignals.unauthoritativeScore` (`integer(uint32)`) — Unauthoritative score. Used as one of the web page quality qstar signals.
- `CompressedQualitySignals.lowQuality` (`integer(uint32)`) — S2V low quality score: converted from quality_nsr.NsrData, applied in Qstar. See quality_nsr::util::ConvertNsrDataToLowQuality.
- `CompressedQualitySignals.vlqNsr` (`integer(uint32)`) [deprecated] — NSR for low-quality videos, converted from quality_nsr.NsrData.vlq_nsr. This field is deprecated - used the equivalent field inside nsr_data_proto instead.
- `CompressedQualitySignals.pqData` (`integer(uint32)`) — Encoded page-level PQ signals.
- `CompressedQualitySignals.nsrConfidence` (`integer(uint32)`) [deprecated] — NSR confidence score: converted from quality_nsr.NsrData. This field is deprecated - use nsr_variance inside nsr_data_proto instead.
- `CompressedQualitySignals.experimentalQstarSignal` (`number(float)`) — This field is *not* propagated to shards. It is meant to be populated at serving time using one of the versions present in the `experimental_nsr_team_wsj_data` field above (using the `Exper…
- `QualityNsrNsrData.nsr` (`number(float)`) — no description in the document
- `QualityNsrNsrData.siteQualityStddevs` (`list<QualityNsrVersionedFloatSignal>`) — Estimate of site's PQ rating stddev--spread of the page-level PQ ratings of a site. Note this is different from nsr_variance which predicts error of NSR itself from the aggregated site-leve…
- `QualityNsrNsrData.sitePr` (`number(float)`) — no description in the document
- `QualityNsrNsrData.siteLinkIn` (`number(float)`) — Average value of the site_link_in for pages in the sitechunk.
- `QualityNsrNsrData.siteLinkOut` (`number(float)`) — Aggregated value of url link out scores for this sitechunk.
- `QualityNsrNsrData.smallPersonalSite` (`number(float)`) — Score of small personal site promotion go/promoting-personal-blogs-v1
- `QualityNsrNsrData.titlematchScore` (`number(float)`) — Titlematch score of the site, a signal that tells how well titles are matching user queries.
- `QualityNsrNsrData.tofu` (`number(float)`) — Site-level tofu score: site quality predictor based on content.
- `QualityNsrNsrData.chardScoreEncoded` (`list<QualityNsrVersionedIntSignal>`) — Site-level Chard (encoded as an int).
- `QualityNsrNsrData.clutterScores` (`list<QualityNsrVersionedFloatSignal>`) — no description in the document
- `QualityNsrNsrData.ugcScore` (`number(float)`) — no description in the document
- `QualityNsrNsrData.articleScoreV2` (`number(float)`) — no description in the document
- `QualityNsrNsrData.isVideoFocusedSite` (`boolean`) — Bit to determine whether the site has mostly video content, but is not hosted on any known video-hosting domains. Site is considered to be video-focused, if it has > 50% of the URLs with wa…
- `QualityNsrNsrData.healthScore` (`number(float)`) — Categorical signals.
- `QualityNsrNsrData.ymylNewsV2Score` (`number(float)`) — no description in the document
- `QualityNsrNsrData.shoppingScore` (`number(float)`) — no description in the document
- `QualityNsrNsrData.localityScore` (`number(float)`) — Locality score of the site, i.e. the locality component of the LocalAuthority signal (see go/pq-localauthority).
- `QualityNsrNsrData.site2vecEmbeddingEncoded` (`list<QualityNsrNsrDataEncodedEmbedding>`) — Encoded site2vec embedding (to be used in superroot) since the full embeddings take too much space.
- `QualityNsrNsrData.isCovidLocalAuthority` (`boolean`) — Bit to determine whether the site has the local authority covid signal, as computed by go/covid-local-authority
- `QualityNsrNsrData.isElectionAuthority` (`boolean`) — Bit to determine whether the site has the election authority signal, as computed by go/election-authority
- `QualityNsrNsrData.spambrainLavcScores` (`list<QualityNsrVersionedFloatSignal>`) — no description in the document
- `QualityNsrNsrData.clusterUplift` (`QualityNsrNsrDataClusterUplift`) — no description in the document
- `PerDocData.hostNsr` (`integer(uint32)`) [deprecated] — Site rank computed for host-level sitechunks. This value encodes nsr, site_pr and new_nsr. See quality_nsr::util::ConvertNsrDataToHostNsr and go/nsr. This field is deprecated - used the equ…

## 5. Page quality and content (PQ, originality, length)

Search terms: `content effort`, `original`, `quality`, `tokens`, `title`.

- `QualityNsrPQData.contentEffort` (`list<QualityNsrVersionedFloatSignal>`) — LLM-based effort estimation for article pages (see landspeeder/4311817).
- `QualityNsrPQData.chardScoreEncoded` (`list<QualityNsrVersionedIntSignal>`) — URL-level Chard (encoded as an int).
- `QualityNsrPQData.keto` (`list<QualityNsrVersionedFloatSignal>`) — Keto score.
- `QualityNsrPQData.rhubarb` (`list<QualityNsrVersionedFloatSignal>`) — Site-URL delta signals based quality score computed in Goldmine via the Rhubarb model (go/rhubarb-dd).
- `QualityNsrPQData.page2vecLq` (`number(float)`) — no description in the document
- `QualityNsrPQData.linkIncoming` (`number(float)`) — no description in the document
- `QualityNsrPQData.linkOutgoing` (`number(float)`) — no description in the document
- `QualityNsrPQData.numOffdomainAnchors` (`number(float)`) — The total number of offdomain anchors seen by the NSR pipeline for this page.
- `PerDocData.OriginalContentScore` (`integer(int32)`) — The original content score is represented as a 7-bits, going from 0 to 127. Only pages with little content have this field. The actual original content score ranges from 0 to 512. It is enc…
- `PerDocData.commercialScore` (`number(float)`) — A measure of commerciality of the document Score > 0 indicates document is commercial (i.e. sells something) Computed by repository/pageclassifiers/parsehandler-commercial.cc
- `PerDocData.ymylHealthScore` (`integer(uint32)`) — Stores scores of ymyl health classifier as defined at go/ymyl-classifier-dd. To use this field, you MUST join g/pq-classifiers-announce and add your use case at http://shortn/_nfg9oAldou.
- `PerDocData.ymylNewsScore` (`integer(uint32)`) — Stores scores of ymyl news classifier as defined at go/ymyl-classifier-dd. To use this field, you MUST join g/pq-classifiers-announce and add your use case at http://shortn/_nfg9oAldou.
- `PerDocData.shingleInfo` (`ShingleInfoPerDocData`) — no description in the document
- `DocProperties.numTokens` (`integer(int32)`) — The number of tokens, tags and punctuations in the tokenized contents. This is an approximation of the number of tokens, tags and punctuations we end up with in mustang, but is inexact sinc…
- `DocProperties.avgTermWeight` (`integer(int32)`) — The average weighted font size of a term in the doc body
- `DocProperties.title` (`string`) — Extracted from the title tag of the content. This is typically extracted by TitleMetaCollector defined at google3/segindexer/title-meta-collector.h. Please see its documentation for the for…
- `DocProperties.badTitle` (`boolean`) — Missing or meaningless title
- `DocProperties.badtitleinfo` (`list<DocPropertiesBadTitleInfo>`) — no description in the document
- `BlogPerDocData.copycatScore` (`integer(int32)`) — no description in the document

## 6. Algorithm names and demotion fields (Panda, Penguin, etc.)

Search terms: `demotion`, `panda`, `penguin`, `promote`.

- `CompressedQualitySignals.pandaDemotion` (`integer(uint32)`) — This is the encoding of Panda fields in the proto SiteQualityFeatures in quality/q2/proto/site_quality_features.proto. The encoding/decoding is performed using functions from quality_coati:…
- `CompressedQualitySignals.babyPandaDemotion` (`integer(uint32)`) — baby_panda_demotion: converted from QualityBoost.rendered.boost.
- `CompressedQualitySignals.babyPandaV2Demotion` (`integer(uint32)`) — New BabyPanda demotion, applied on top of Panda. This is meant to replace |baby_panda_demotion|.
- `CompressedQualitySignals.anchorMismatchDemotion` (`integer(uint32)`) — anchor_mismatch_demotion: converted from QualityBoost.mismatched.boost.
- `CompressedQualitySignals.exactMatchDomainDemotion` (`integer(uint32)`) — Page quality signals converted from fields in proto QualityBoost in quality/q2/proto/quality-boost.proto. To save indexing space, we convert the float values in [0, 1] to integers in range…
- `CompressedQualitySignals.serpDemotion` (`integer(uint32)`) — serp demotion: applied in Qstar.
- `CompressedQualitySignals.productReviewPDemoteSite` (`integer(uint32)`) — Product review demotion/promotion confidences. (Times 1000 and floored)
- `CompressedQualitySignals.productReviewPPromoteSite` (`integer(uint32)`) [deprecated] — no description in the document
- `CompressedQualitySignals.scamness` (`integer(uint32)`) — Scam model score. Used as one of the web page quality qstar signals. Value range from 0 to 1023.
- `IndexingDocjoinerAnchorStatistics.penguinPenalty` (`number(float)`) — Page-level penguin penalty (0 = good, 1 = bad).
- `IndexingDocjoinerAnchorStatistics.penguinLastUpdate` (`integer(int32)`) — BEGIN: Penguin related fields. Timestamp when penguin scores were last updated. Measured in days since Jan. 1st 1995.
- `IndexingDocjoinerAnchorStatistics.penguinEarlyAnchorProtected` (`boolean`) — Doc is protected by goodness of early anchors.
- `IndexingDocjoinerAnchorStatistics.penguinTooManySources` (`boolean`) — Doc not scored because it has too many anchor sources. END: Penguin related fields.
- `IndexingDocjoinerAnchorStatistics.badbacklinksPenalized` (`boolean`) — Whether this doc is penalized by BadBackLinks, in which case we should not use improvanchor score in mustang ascorer.

## 7. Links, anchor text and PageRank

Search terms: `anchor`, `pagerank`, `link`, `offdomain`. Schema prefixes: `Anchors`, `IndexingDocjoinerAnchor`.

- `AnchorsAnchor.text` (`string`) — Space-delimited anchor words. Text that needs segmentation (like CJK or Thai) is unsegmented, since we set FLAGS_segment_during_lexing to false in mr-linkextractor.cc .
- `AnchorsAnchor.sourceType` (`integer(int32)`) — is to record the quality of the anchor's source page and is correlated with but not identical to the index tier of the source page. In the docjoins built by the indexing pipeline (Alexandri…
- `AnchorsAnchor.fontsize` (`integer(int32)`) — no description in the document
- `AnchorsAnchor.isLocal` (`boolean`) — The bit ~roughly~ indicates whether an anchor's source and target pages are on the same domain. Note: this plays no role in determining whether an anchor is onsite, ondomain, or offdomain i…
- `AnchorsAnchor.context2` (`integer(int32)`) — This is a hash of terms near the anchor. (This is a second-generation hash replacing the value stored in the 'context' field.)
- `AnchorsAnchor.creationDate` (`integer(int32)`) — used for history - the first and last time we have seen this anchor. creation_date also used for Freshdocs Twitter indexing, a retweet is an anchor of the original tweet. This field records…
- `AnchorsAnchor.firstseenDate` (`integer(int32)`) — # days past Dec 31, 1994, 23:00:00 UTC (Unix time @788914800) that this link was first seen. Should never occupy more than 15 bits. NOTE: this is NOT the same as creation_date; firstseen_da…
- `AnchorsAnchor.pagerankWeight` (`number(float)`) — Weight to be stored in linkmaps for pageranker
- `AnchorsAnchor.weight` (`integer(int32)`) — weights are 0-127
- `AnchorsAnchor.locality` (`integer(int32)`) — For ranking purposes, the quality of an anchor is measured by its "locality" and "bucket". See quality/anchors/definitions.h for more information.
- `AnchorsAnchor.expired` (`boolean`) — true iff exp domain
- `AnchorsAnchor.deleted` (`boolean`) — no description in the document
- `AnchorsAnchorSource.pagerank` (`integer(int32)`) — uint16 scale
- `AnchorsAnchorSource.pagerankNs` (`integer(int32)`) — unit16 scale
- `AnchorsAnchorSource.nsr` (`integer(uint32)`) — This NSR value has range [0,1000] and is the original value [0.0,1.0] multiplied by 1000 rounded to an integer.
- `AnchorsAnchorSource.spamrank` (`integer(int32)`) — uint16 scale
- `AnchorsAnchorSource.indyrank` (`integer(int32)`) — uint16 scale
- `AnchorsAnchorSource.homePageInfo` (`integer(int32)`) — Information about if the source page is a home page. It can be one of the enum values defined in PerDocData::HomePageInfo (NOT_HOMEPAGE, NOT_TRUSTED, PARTIALLY_TRUSTED, and FULLY_TRUSTED).
- `AnchorsAnchorSource.outdegree` (`integer(int32)`) — no description in the document
- `IndexingDocjoinerAnchorStatistics.anchorCount` (`integer(int32)`) — no description in the document
- `IndexingDocjoinerAnchorStatistics.offdomainAnchorCount` (`integer(int32)`) — no description in the document
- `IndexingDocjoinerAnchorStatistics.anchorSpamInfo` (`IndexingDocjoinerAnchorSpamInfo`) — This structure contains signals and penalties of AnchorSpamPenalizer. It replaces phrase_anchor_spam_info above, that is deprecated.
- `IndexingDocjoinerAnchorStatistics.linkBeforeSitechangeTaggedAnchors` (`integer(int32)`) — no description in the document
- `IndexingDocjoinerAnchorStatistics.pageFromExpiredTaggedAnchors` (`integer(int32)`) — Set in SignalPenalizer::FillInAnchorStatistics.
- `IndexingDocjoinerAnchorPhraseSpamInfo.phraseAnchorSpamDays` (`number(float)`) — Over how many days 80% of these phrases were discovered.
- `PerDocData.pagerank` (`number(float)`) — Experimental pageranks (DEPRECATED; only pagerank in MustangBasicInfo is used).
- `PerDocData.toolbarPagerank` (`integer(int32)`) — A copy of the value stored in /namespace/indexing/wwwglobal//fakepr/* for this document. A value of quality_bakery::FakeprUtils::kUnknownToolbarPagerank indicates that we don't have toolbar…
- `PerDocData.homepagePagerankNs` (`integer(int32)`) — The page-rank of the homepage of the site. Copied from the cdoc.doc().pagerank_ns() of the homepage.
- `PerDocData.crawlPagerank` (`integer(int32)`) — This field is used internally by the docjoiner to forward the crawl pageranks from original canonicals to canonicals we actually chose; outside sources should not set it, and it should not…
- `PerDocData.smearingMaxTotalOffdomainAnchors` (`integer(int32)`) — no description in the document
- `PerDocData.IsAnchorBayesSpam` (`boolean`) — Is this document considered spam by the anchor bayes classifier?

## 8. Domain age, "sandbox" and registration info

Search terms: `hostAge`, `domainAge`, `registration`, `expired`.

- `PerDocData.hostAge` (`integer(int32)`) — The earliest firstseen date of all pages in this host/domain. These data are used in twiddler to sandbox fresh spam in serving time. It is 16 bit and the time is day number after 2005-12-31, and all the previous time are set to 0. If this url's host_age == domain_age, then omit domain_age Please use //spam/content/siteage-util.h to convert the day between epoch second. Regarding usage of Sentinel values: We would like to check if a value exists in scoring bundle while using in Ranklab AST. For this having a sentin… **Note:** this is the only place in the document where the word "sandbox" appears in connection with web search, and it says it is used only for "fresh spam".
- `PerDocData.domainAge` (`integer(int32)`) — 16-bit **Note:** its description is only "16-bit"; its meaning follows from the `hostAge` description.
- `CompositeDoc.registrationinfo` (`RegistrationInfo`) — Information about the most recent creation and expiration of this domain. It's extracted from domainedge signal.
- `RegistrationInfo.createdDate` (`integer(int32)`) — This is the number of days since January 1st 1995 that this domain was last created. This should always fit in 15 bits.
- `RegistrationInfo.expiredDate` (`integer(int32)`) — This is the number of days since January 1st 1995 that this domain last expired. This should always fit in 15 bits. Jan 1st 1995 was chosen by the history project as a special epoch date. B…

## 9. Spam

Search terms: `spam`, `scam`, `gibberish`, `stuffing`. `show PerDocData --match spam` lists them all.

- `PerDocData.spamrank` (`integer(int32)`) — The spamrank measures the likelihood that this document links to known spammers. Its value is between 0 and 65535.
- `PerDocData.spambrainData` (`SpamBrainData`) — Host-v1 sitechunk level scores coming from spambrain.
- `PerDocData.spambrainTotalDocSpamScore` (`number(float)`) — The document total spam score identified by spambrain, going from 0 to 1.
- `PerDocData.spambrainDomainSitechunkData` (`SpamBrainData`) — Domain sitechunk level scores coming from spambrain.
- `PerDocData.DocLevelSpamScore` (`integer(int32)`) — The document spam score is represented as a 7-bits, going from 0 to 127.
- `PerDocData.uacSpamScore` (`integer(int32)`) — The uac spam score is represented in 7 bits, going from 0 to 127. Threshold is 64. Score >= 64 is considered as uac spam.
- `PerDocData.trendspamScore` (`integer(int32)`) — For now, the count of matching trendspam queries.
- `PerDocData.spamMuppetSignals` (`SpamMuppetjoinsMuppetSignals`) — Contains hacked site signals which will be used in query time joins. As of Oct'19, the field is stored in a separate corpus. It'll only be populated for in-flight requests between retrieve…
- `PerDocData.SpamWordScore` (`integer(int32)`) — The spamword score is represented in 7-bits, going from 0 to 127.
- `PerDocData.ScaledLinkAgeSpamScore` (`integer(int32)`) — End DEPRECATED ------------------------------------------------------------ Link age score is represented as a 7-bit integer, going from 0 to 127.
- `PerDocData.spamtokensContentScore` (`number(float)`) — For SpamTokens content scores. Used in SiteBoostTwiddler to determine whether a page is UGC Spam. See go/spamtokens-dd for details.
- `PerDocData.GibberishScore` (`integer(int32)`) — The gibberish score is represented in 7 bits, going from 0 to 127.
- `PerDocData.KeywordStuffingScore` (`integer(int32)`) — The keyword stuffing score is represented in 7 bits, going from 0 to 127.
- `PerDocData.urlPoisoningData` (`UrlPoisoningData`) — Contains url poisoning data for suppressing spam documents.

## 10. Dates and freshness

Search terms: `date`, `freshness`, `lastSignificantUpdate`, `byline`. Schema prefix: `QualityTimebased`.

- `PerDocData.semanticDate` (`integer(int32)`) — SemanticDate, estimated date of the content of a document based on the contents of the document (via parsing), anchors and related documents. Date is encoded as a 32-bits UNIX date (1970 Ja…
- `PerDocData.semanticDateInfo` (`integer(int32)`) — Info is encoded using a SemanticDate specific format. Contains confidence scores for day/month/year components as well as various meta data required by the freshness twiddlers.
- `PerDocData.datesInfo` (`string(int64)`) — Stores dates-related info (e.g. page is old based on its date annotations). Used in FreshnessTwiddler. Use encode/decode functions from quality/timebased/utils/dates-info-helper-inl.h
- `PerDocData.lastSignificantUpdate` (`string(int64)`) — Last significant update of the document. This is sourced from the quality_timebased.LastSignificantUpdate proto as computed by the LSUSelector from various signals. The value is a UNIX time…
- `PerDocData.freshboxArticleScores` (`integer(uint32)`) — Stores scores of freshness-related classifiers: freshbox article score, live blog score and host-level article score. The encoding/decoding API is in quality/freshness/freshbox/goldmine/fre…
- `PerDocData.isHotdoc` (`boolean`) — Set by the FreshDocs instant doc joiner. See //indexing/instant/hotdocs/README and http://go/freshdocs-hotdocs.
- `PerDocData.freshnessEncodedSignals` (`string(int64)`) [deprecated] — Stores freshness and aging related data, such as time-related quality metrics predicted from url-pattern level signals. Use the encoding decoding API in quality/freshness/docclassifier/agin…
- `QualityTimebasedSyntacticDate.bylineDate` (`string(int64)`) — The following field is set only when the byline date is different from the "date" field above. Currently this happens when the byline date is within the 24 hours of the crawl time, or close…
- `NlpSaftDocument.bylineDate` (`string(int64)`) — Document's byline date, if available: this is the date that will be shown in the snippets in web search results. It is stored as the number of seconds since epoch. See segindexer/composited…
- `NlpSaftDocument.syntacticDate` (`string(int64)`) — Document's syntactic date (e.g. date explicitly mentioned in the URL of the document or in the document title). It is stored as the number of seconds since epoch. See quality/timebased/synt…
- `CompositeDocIndexingInfo.urlHistory` (`CrawlerChangerateUrlHistory`) — Url change history for this doc (see crawler/changerate/changerate.proto for details). Note if a doc has more than 20 changes, we only keep the last 20 changes here to avoid adding to much…
- `CrawlerChangerateUrlHistory.latestVersion` (`CrawlerChangerateUrlVersion`) — The latest version we've seen.

## 11. Authors, entities and topical focus

Search terms: `author` (with `--word`; otherwise `authority` and `authorized` get mixed in), `entity`, `webref`, `embedding`, `topic`. Schema prefixes: `RepositoryWebref`, `QualityAuthorityTopic`. These fields **identify** the author; the database has no field that assigns a score to an author.

- `PerDocData.authorObfuscatedGaiaStr` (`list<string>`) — no description in the document
- `PerDocData.DEPRECATEDAuthorObfuscatedGaia` (`list<string(uint64)>`) [deprecated] — The obfuscated google profile gaia id(s) of the author(s) of the document. This field is deprecated, use the string version.
- `RepositoryWebrefDetailedEntityScores.isAuthor` (`boolean`) — True if the entity is the author of the document. This was mainly developed and tuned for news articles (e.g. /m/02x27qn on "www.vogue.com/article/flint-town-netflix") but is also popluated…
- `RepositoryWebrefDetailedEntityScores.profileUrl` (`string`) — Contains the link to the author's profile url on the platform.
- `RepositoryWebrefDetailedEntityScores.isPublisher` (`boolean`) — True if the entity is the publisher of the page (e.g. CNN on "http://www.cnn.com/foo/bar").
- `RepositoryWebrefWebrefMustangAttachment.isAuthorIndex` (`list<integer(int32)>`) — The indices of all the reference entities in encoded_mid that are authors of the page. Not packed as in most cases when populated, it contains 1 element.
- `IndexingDocjoinerDataVersion.qualityAuthorshipAuthorAnnotations` (`IndexingDocjoinerDataVersionVersionInfo`) — no description in the document
- `IndexingDocjoinerDataVersion.repositoryWebrefAuthorExtractionAnnotation` (`IndexingDocjoinerDataVersionVersionInfo`) — no description in the document
- `PerDocData.webrefEntities` (`RepositoryWebrefWebrefMustangAttachment`) — WebRef entities associated to the document. See go/webref for details.
- `PerDocData.queriesForWhichOfficial` (`OfficialPagesQuerySet`) — The set of (query, country, language) triples for which this document is considered to be the official page. For example, www.britneyspears.com would be official for ("britney spears", "us"…
- `PerDocData.onsiteProminence` (`integer(uint32)`) — Onsite prominence measures the importance of the document within its site. It is computed by propagating simulated traffic from the homepage and high craps click pages. It is a 13-bit int.
- `PerDocData.asteroidBeltIntents` (`QualityOrbitAsteroidBeltDocumentIntentScores`) — For indexing Asteroid Belt intent scores. See go/asteroid-belt for details.
- `QualityAuthorityTopicEmbeddingsVersionedItem.siteFocusScore` (`number(float)`) — Number denoting how much a site is focused on one topic.
- `QualityAuthorityTopicEmbeddingsVersionedItem.siteRadius` (`number(float)`) — The measure of how far page_embeddings deviate from the site_embedding.
- `QualityAuthorityTopicEmbeddingsVersionedItem.siteEmbedding` (`string(byte)`) — Compressed site/page embeddings.
- `QualityAuthorityTopicEmbeddingsVersionedItem.pageEmbedding` (`string(byte)`) — no description in the document
- `CompressedQualitySignals.topicEmbeddingsVersionedData` (`list<QualityAuthorityTopicEmbeddingsVersionedItem>`) — Versioned TopicEmbeddings data to be populated later into superroot / used directly in scorers.

## 12. E-E-A-T, expertise and trust

In the database, searches for `eeat`, `e-e-a-t`, `e-a-t` and `trustworthiness` return **0 results**; there is no field named "E-E-A-T score" or author authority score. `expertise` appears only in a field that belongs to a Maps profile. The real fields closest to these concepts are listed below; the document does not say they are part of E-E-A-T, and drawing that connection is interpretation.

- `CompressedQualitySignals.siteAuthority` (`integer(uint32)`) — site_authority: converted from quality_nsr.SiteAuthority, applied in Qstar.
- `CompressedQualitySignals.authorityPromotion` (`integer(uint32)`) — authority promotion: converted from QualityBoost.authority.boost
- `CompressedQualitySignals.unauthoritativeScore` (`integer(uint32)`) — Unauthoritative score. Used as one of the web page quality qstar signals.
- `QualityNsrNsrData.isElectionAuthority` (`boolean`) — Bit to determine whether the site has the election authority signal, as computed by go/election-authority
- `QualityNsrNsrData.isCovidLocalAuthority` (`boolean`) — Bit to determine whether the site has the local authority covid signal, as computed by go/covid-local-authority
- `PerDocData.ymylHealthScore` (`integer(uint32)`) — Stores scores of ymyl health classifier as defined at go/ymyl-classifier-dd. To use this field, you MUST join g/pq-classifiers-announce and add your use case at http://shortn/_nfg9oAldou.
- `PerDocData.ymylNewsScore` (`integer(uint32)`) — Stores scores of ymyl news classifier as defined at go/ymyl-classifier-dd. To use this field, you MUST join g/pq-classifiers-announce and add your use case at http://shortn/_nfg9oAldou.
- `QualityNsrNsrData.ymylNewsV2Score` (`number(float)`) — no description in the document
- `RepositoryWebrefDetailedEntityScores.isAuthor` (`boolean`) — True if the entity is the author of the document. This was mainly developed and tuned for news articles (e.g. /m/02x27qn on "www.vogue.com/article/flint-town-netflix") but is also popluated…
- `AppsPeopleOzExternalMergedpeopleapiMapsExtendedData.topicExpertise` (`list<string>`) — A topic that creator has expertise in. This will be in the format: emoji associated with the topic, display name of the topic, topic score **Note:** belongs to a Maps product profile; it is not related to web search.

## 13. Mobile and page experience

Search terms: `mobile`, `smartphone`, `interstitial`, `volt`.

- `SmartphonePerDocData.isSmartphoneOptimized` (`boolean`) — Indicates if the page is rendered in a friendly manner on smartphones. We use this field as tri-state: "unset" means the rendering result classification is not available, and "set as false"…
- `SmartphonePerDocData.violatesMobileInterstitialPolicy` (`boolean`) — Indicates if the page is violating mobile interstitial policy and should be demoted. See go/interstitials-ranking-dd for details.
- `SmartphonePerDocData.adsDensityInterstitialViolationStrength` (`integer(int32)`) — Indicates if the page is violating mobile ads density interstitial policy and the violation strength. See go/interstitials-for-ads and http://ariane/268642 for details. To save indexing spa…
- `SmartphonePerDocData.mobileFriendlyScore` (`integer(int32)`) — Mobile friendliness score in the range of [0, 100]. See go/modena-ranking.
- `PerDocData.voltData` (`IndexingMobileVoltVoltPerDocData`) — Contains page UX signals for VOLT ranking change. See http://ariane/4025970 for more details.
- `PerDocData.desktopInterstitials` (`IndexingMobileInterstitialsProtoDesktopInterstitials`) — Contains desktop interstitials signal for VOLT ranking change.
- `PerDocData.MobileData` (`MobilePerDocData`) — Additional metadata for lowend mobile documents in the Google index.

## 14. Indexing, crawling and tiers

Search terms: `tier`, `crawl`, `docjoiner`, `duplicate`. Schema prefixes: `Indexing`, `Crawler`, `Trawler`.

- `PerDocData.scaledSelectionTierRank` (`integer(int32)`) — Selection tier rank is a language normalized score ranging from 0-32767 over the serving tier (Base, Zeppelins, Landfills) for this document. This is converted back to fractional position w…
- `CompositeDoc.indexinginfo` (`CompositeDocIndexingInfo`) — no description in the document
- `CompositeDoc.dataVersion` (`IndexingDocjoinerDataVersion`) — Contains the tracking version of various data fields in CompositeDoc.
- `CompositeDoc.forwardingdup` (`list<CompositeDocForwardingDup>`) — no description in the document
- `CompositeDoc.extradup` (`list<CompositeDocExtraDup>`) — no description in the document
- `CompositeDoc.badSslCertificate` (`IndexingBadSSLCertificate`) — This field is present iff the page has a bad SSL certificate itself or in its redirect chain.
- `CompositeDoc.anchorStats` (`IndexingDocjoinerAnchorStatistics`) — Mark as non-personal since it's an aggregation of anchors. For more details of Search personal data, see go/dma52-search-cdoc-fields.
- `CompositeDoc.qualitysignals` (`CompositeDocQualitySignals`) — no description in the document
- `CompositeDoc.perDocData` (`PerDocData`) — no description in the document

## 15. Local search

Search terms: `local`, `geo`, `locality`. Schema prefixes: `Geostore`, `Localsearch`, `LocalWWWInfo`.

- `LocalWWWInfo.geotopicality` (`RepositoryAnnotationsGeoTopicality`) [deprecated] — Information about geo locations, rather than individual businesses.
- `QualityNsrNsrData.localityScore` (`number(float)`) — Locality score of the site, i.e. the locality component of the LocalAuthority signal (see go/pq-localauthority).
- `CompositeDoc.localinfo` (`LocalWWWInfo`) — no description in the document
