# Synthesis: what do the sources say together?

*Report date: 19 November 2026.*

**The official framework.** Google explains local ranking (hotel results included) with three factors: **relevance**, **distance** and **prominence**. This explanation appears at support.google.com/business/answer/7091 and on Maps Help pages. Google also says the following:
- Prominence also includes links on the web, review count and rating.
- Categories affect ranking.
- Ranking cannot be bought; payment does not affect Maps results.
- The Places API documentation associates prominence with "ranking in Google's index, global popularity".

**The patent counterparts.** Patents describe each of these three factors with concrete methods:
- **Prominence:** `US7822751B2` gives local results a query-independent "location prominence" score. The example inputs in the description are: the business's official document, the number of documents reviewing the business, and the directory sites that mention the business.
  - `US8122013B1` measures the prominence of the business name on the web.
  - `US8312010B1` uses a weighted count of user actions; among these, the call/contact action is the most heavily weighted.
  - `US8538973B1` uses the number of directions requests.
  - `US9558210B1` measures the quality of a place by how much farther than expected people travel to reach it.
  - `US10366422B2` derives a "quality visit" measure from actual visits.
- **Distance:** `US7606798B2` adjusts the weight of distance according to the topic of the query. `US9262541B2` demotes distant results in ranking. `US7792883B2` scores results by proximity to the map viewport. `US8898173B1` ranks results with multiple distance measures. `US8949013B2` uses distance, opening hours and likelihood of a visit together.
- **Relevance:** `US8407211B1` keeps category-location relevance scores. `US9348925B2` works out whether a query carries local intent from the share of its submissions that come from the map. `US9194716B1` and `US9507801B2` deal with category density and diversity.
- **Reviews:**
  - `US10394830B1` uses the sentiment in reviews as a ranking signal.
  - `US9792330B1` gives more weight to local expert reviewers.
  - `US9817907B1` favors the reviews of reviewers who stayed at the same hotel.
- **Spam:**
  - `US8473491B1` detects keyword-stuffed business names.
  - `US8694489B1` flags businesses appearing at residentially zoned addresses as map spam.
  - `US9195987B2` verifies the listing with Street View imagery and detects closed businesses.

- **Personalization and AI:** The `US20190340537A1` application, "Personalized Match Score For Places", can be read as the patent counterpart of the "Your match" score in Maps (interpretation). `US20250054045A1` generates a user-specific business profile with AI.

**Statements by Google employees.**
- The November 2019 local update was explained as "neural matching" (Danny Sullivan): conceptual matching beyond the words in the business name and description.
- For the December 2021 update Google said only "rebalancing of various factors"; the industry named it "Vicinity".
- In December 2023 a business **being open** (openness) became a stronger signal for non-navigational queries (Search Liaison).
- According to John Mueller, reviews are not a factor in web search, but may be taken into account more on the Business Profile side. Mueller also said that local/Maps results are separate from organic search.
- Google does not recommend listing on local directory sites as an SEO tool (Alan Kent).

**An important limit.** A patent shows that Google **described a method and sought protection for it**; it does not show that the method is used today or with what weight. Official pages name the factors but give no weights. In this report, patents, official documents and employee statements were kept in separate sections; the sentences that connect them to one another are my interpretation.
