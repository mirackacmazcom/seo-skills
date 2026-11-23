# Google Research publications (24 items)

This section covers papers written by Google employees and Google Research blog posts. For entries marked (s), the page could not be opened or the information could not be verified.

There is very little published research by Google that directly explains how places are ranked in Maps. Only two works are directly relevant: #1 and #2. The others deal with the inputs to ranking: data quality, fake listings, place attributes, busyness and place embeddings.

### 1. Local search ranking and business recommendation
1. **Hyper-local, directions-based ranking of places** — Venetis, Gonzalez, Halevy, Jensen (Google and academia), PVLDB 2011 — https://research.google/pubs/hyper-local-directions-based-ranking-of-places/
   - Ranks nearby places by how often they appear in directions queries.
   - Patent counterpart: US8538973B1.
2. **Category-Driven Approach for Local Related Business Recommendations** — Perez, Schueppert, Lawlor, Kishore (Google), CIKM 2015 — https://research.google/pubs/pub44857
   - Balances substitute and complementary businesses in the related-businesses list.
   - It does this with association rules mined from Maps directions queries.
3. **Orienteering Algorithms for Generating Travel Itineraries** — Friggstad, Gollapudi, Kollias, Sarlós, Swamy, Tomkins (mostly Google), WSDM 2018 — https://research.google/pubs/orienteering-algorithms-for-generating-travel-itineraries/
   - The utility of places is determined from anonymous visit data and a travel itinerary is selected.

### 2. Fake listings and abuse
4. **Pinning Down Abuse on Google Maps** — Huang, Grundman, Thomas, Kumar, Bursztein (Google) and UCSD, WWW 2017 — https://research.google/pubs/pub45976
   - Examines more than 100 thousand fake listings suspended for abuse.
   - These listings were created to divert local search traffic to deceptive services.
5. **Keeping fake listings off Google Maps** (blog, 2017-04-06) — Grundman, Thomas — https://research.google/blog/keeping-fake-listings-off-google-maps/
   - "We detect and disable 85% of fake listings before they even appear on Google Maps."

### 3. Business listing quality and place attributes
6. **Large Scale Business Discovery from Street Level Imagery** — Yu, Szegedy et al. (Google), arXiv 2015 — https://research.google/pubs/pub44629/
7. **Attention-based Extraction of Structured Information from Street View Imagery** — Wojna et al. (Google), ICDAR 2017 — https://research.google/pubs/pub46686/
8. **Updating Google Maps with Deep Learning and Street View** (blog, 2017-05-03) — https://research.google/blog/updating-google-maps-with-deep-learning-and-street-view/
9. **Job Type Extraction for Service Businesses** — Li, Najork et al. (Google), WWW Companion 2023 — https://research.google/pubs/job-type-extraction-for-service-businesses/
   - Extracts service types from business websites; this information is used in Search and Maps (s).
10. **Shopping Sense** (HCOMP 2021) and **Addressing Label Sparsity with Class-Level Common Sense for Google Maps** (Frontiers in AI 2022) — Welty, Aroyo et al. (Google)
    - https://research.google/pubs/shopping-sense-rapid-instance-level-knowledge-acquisition-for-google-maps-from-class-level-common-sense/
    - https://research.google/pubs/addressing-label-sparsity-with-class-level-common-sense-for-google-maps/
    - Place–product relations that make product- and dish-based local search (such as where to buy milk) possible.
11. **STEPS: Predicting place attributes via spatio-temporal analysis** — Nie, Gabrilovich et al., arXiv 2016 — https://arxiv.org/abs/1610.07090
    - Infers place attributes from visit patterns. The authors' Google affiliation could not be verified (s).
12. **Mobility-Embedded POIs (ME-POIs)** — Siampou, Choudhury, Arora (Google) and USC, arXiv 2026 — https://arxiv.org/abs/2601.21149
    - Blog post (2026-08-21): https://research.google/blog/how-mobility-gives-language-models-a-deeper-understanding-of-place/
    - Combines visit patterns with a text embedding to improve prediction of opening hours, price level, permanent closure and busyness.
13. **Extracting Patterns from Location History** — Kirmse et al. (Google), SIGSPATIAL 2011 — https://research.google/pubs/pub37522/

### 4. Busyness and privacy
14. **New Insights into Human Mobility with Privacy Preserving Aggregation** (blog, 2019-11-12) — https://research.google/blog/new-insights-into-human-mobility-with-privacy-preserving-aggregation/
15. **COVID-19 Community Mobility Reports: Anonymization Process** — Aktay et al. (Google), arXiv 2020 — https://arxiv.org/abs/2004.04145
16. **Plume: Differential Privacy at Scale** — Amin et al. (Google), arXiv 2022 (2201.11603)
    - A general system; it does not mention popular times.
17. **EV charging port availability prediction** (blog, 2025-11-21) — https://research.google/blog/reducing-ev-range-anxiety-how-a-simple-ai-model-predicts-port-availability/

### 5. Place embeddings and geospatial models
18. **Population Dynamics Foundation Model** — Agarwal et al. (Google), arXiv 2024 (2411.07207)
    - Blog: https://research.google/blog/insights-into-population-dynamics-a-foundation-model-for-geospatial-inference/
    - Inputs include maps, busyness and aggregated search trends.
19. **S2Vec** (blog, 2026-03-24) — https://research.google/blog/mapping-the-modern-world-how-s2vec-learns-the-language-of-our-cities/
20. **Geospatial Reasoning** (blog, 2025-04-08) — https://research.google/blog/geospatial-reasoning-unlocking-insights-with-generative-ai-and-multiple-foundation-models/
21. **Earth AI** (arXiv 2510.18318) and **Earth AI Geospatial Reasoning Agent** (arXiv 2610.15750) — That they include a comparison with Maps grounding was seen only in the search snippet (s).

### 6. Query and location context
22. **Sparse Non-negative Matrix Language Modeling for Geo-annotated Query Session Data** — Chelba, Shazeer (Google), ASRU 2015
    - Perplexity drops by 51% when location context is used for local queries.
23. **A Tale of Two (Similar) Cities** — Seth, Baluja et al. (Google), KDIR 2011
24. **Google Research at I/O 2026** (blog, 2026-05-28) — https://research.google/blog/a-new-era-of-innovation-google-research-at-io-2026/
    - The "map helpfulness" metric was redefined together with the Ask Maps team; no detail about ranking.

### Additional product blogs (not covered in the sections above)
- **Address Descriptors** (Maps Platform): ranks landmarks by "proximity, prominence, and visibility" (s).
- **Popular times**: according to the post, data from the last 4–6 weeks is weighted more heavily and differential privacy is used: https://blog.google/products/maps/maps101-popular-times-and-live-busyness-information/

**Searched for but not found (no Google-authored paper):**
- Learning-to-rank or a click model for Maps
- Maps autocomplete
- POI deduplication
- Which POIs are shown on the base map
- Explore and "Your match" recommendations
- A paper specific to popular times
- Fake review detection
- Review summarization with Gemini
- Ranking in Ask Maps
