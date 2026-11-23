# Scope, method and limits

**Patents (326 families)**

The list was swept with four separate methods, and the results of each method were compared against the others.

1. **Local archives.** Full-text search was run in two archives: search patents (54,101 publications) and AI patents (82,806 publications). Topic tags and more than 60 targeted searches yielded 1,522 candidate families. In addition, the titles of all families in both archives were scanned.
2. **Google Patents keyword search.** 24 queries were run with the "assignee Google" filter, and 2,478 results (2,185 + 293) were reviewed.
3. **Google Patents classification (CPC) sweep.** This sweep is independent of keywords. All Google patents in the following classes were scanned page by page:
   - G06F16/9537: location-dependent search
   - G06F16/29: geographic databases
   - G01C21/3679 and G01C21/3682: POI search and display
   - G06Q30/0282: business rating and reviews
   - G06Q50/12 and G06Q50/14: hotels, restaurants, travel
   - Intersected with local terms: G06Q30/0201, G06F16/24578 (result ranking), G06F16/9535 (personalization), H04W4/021 and H04W4/029 (location services)
   
   About 2,700 results were reviewed. The result counts split by year range added up exactly to the overall total; the sweep was done without gaps.
4. **Acquired companies.** Mapping and local search companies that Google acquired, and whose patents may have stayed under their own names, were swept separately: Waze, Zagat, Where2, Keyhole, Zipdash, Endoxon, Urban Engines, Dealmap and Google Technology Holdings (Motorola).
   - The patents of Waze, Zagat and Urban Engines are about navigation, parking, map building and payments. None is about ranking.
   - No patent registered to Zipdash or Endoxon was found. Where2's patent and the only Google-originated patent that came out of the Keyhole search concern geographic data and event information; they do not touch ranking.
   - Motorola's location patents are on the device side.
   - 2 ranking-related patents from Dealmap were added and marked as "acquired".
5. **Repeat check.** In each round, titles not yet on the list were assessed by hand. The number of newly found relevant families changed from round to round as follows: 50 → 50 → 16 → 25. The last round was the keyword-independent sweep covering the classes in full; it produced 25 new relevant families out of 2,700 results.

Reading depth and coverage:
- The independent claims of the core patents were read.
- Patents without a note carry only an excerpt from the abstract.
- The abstracts of patents not found in the local archive were not read.
- Map tile, rendering, navigation, ad bidding and image processing patents are not in the main list; they are kept in the supplementary CSV.
- The ads side appears only for context, in category 10.

**Official documents, employee statements and research publications**

Sources were collected from the local archive of official documentation and from web search. A separate gap check was then carried out, and Google Research publications were swept separately. X/Twitter posts could not be opened because they require a login; those quotes are given via Search Engine Roundtable, with the original link.

**Link check (19 November 2026)**

- **First round:** 365 of 368 links opened.
- **Document and research links added later:** 52 of 52 links opened.
- **Patent links added later:** 121 of 122 links were opened in a browser and verified by title.

Links that did not open, and why:
- **US20260267829A1:** Published in September 2026; it does not yet have a page on Google Patents.
- **2 articles on Search Engine Journal:** The site blocks automated access (HTTP 403).
- **The 3rd link in the first round:** This is US20260267829A1 itself.
