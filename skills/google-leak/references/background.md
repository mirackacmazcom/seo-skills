# Background: what the leak is, where the data comes from, what its limits are

Use this file when the user asks about the leak itself, its reliability, its history, or the scope of this
database. For current numbers, run `python3 scripts/leak.py stats --revisions`.

## What leaked

The discovery document of Google's **Content Warehouse API** (the API of the Document AI Warehouse product on
Google Cloud) was published in a form that contained not only the schemas belonging to that product but also
thousands of data structure definitions belonging to Google's internal systems. Because Google's client libraries
are generated automatically from this document, the same content also ended up in the Go, Python, Ruby, PHP, Java,
Node and Elixir libraries.

The document is **not source code**. What it contains is data structure definitions: schema names, field names,
their types, and the description notes engineers wrote for the fields.

## Timeline

The dates below were verified from the repository history this database was built from:

- **2022-10-17** — The first revision containing internal schemas (`20220920`) was published in the
  `googleapis/google-api-go-client` repository. Even that revision had 2,411 schemas; in other words, the content
  was public for about 19 months.
- **2023-10-18** — The most extensive single revision (`20231011`, 2,619 schemas).
- **2024-03-13** — The Elixir client was generated for the first time; readable documentation pages appeared on
  hexdocs (v0.2.0 and v0.3.0 → revision `20231106`; v0.4.0, 2024-03-28 → revision `20240321`).
- **2024-04-16** — The last leaked revision (`20240412`, 2,595 schemas).
- **2024-05-07** — Cleanup: with revision `20240506` the internal schemas were removed, leaving 174 official
  schemas.

Public disclosure (according to press sources; this cannot be verified from this database): the documents were
announced at the end of May 2024 by Rand Fishkin (SparkToro) and Michael King (iPullRank); the source was stated
to be Erfan Azimi. Google confirmed that the documents were real, but warned against making assumptions about
Search based on out-of-context, outdated or incomplete information. The figures often quoted in the press,
"2,596 modules, 14,014 attributes", belong to hexdocs version v0.4.0.

## Scope of this database

- The union of 51 discovery document revisions (`20220920` – `20241204`): 2,756 schemas, 15,050 fields.
- For every schema and field the **most recent** description is stored; the `first` / `last` values are the
  first and last revision in which it was seen.
- 188 schemas are "official API" (Document AI Warehouse schemas that remained after the cleanup:
  `GoogleCloudContentwarehouse…`, `GoogleCloudDocumentai…`, `GoogleIam…` etc.). The remaining 2,568 schemas are
  leaked internal schemas.
- 163 schemas are not in hexdocs v0.4.0; they appear only in older revisions. The `show` output states this.
- No revision was published between `20231106` and `20240321`.
- Out of scope: changes to description text in older revisions (only the most recent description is kept) and
  the API's endpoints (methods/resources).

## Limits of the document

Keep these in mind when answering, and tell the user when relevant:

1. **Existing does not mean being used.** A field being defined does not show that it is used in ranking. It may
   be for storage, debugging, an experiment, or an entirely different product.
2. **No weights.** The document does not contain the ranking weight, threshold or formula of any field.
3. **Currency is uncertain.** The newest leaked revision is from April 2024. Many fields are marked
   `[deprecated]`, and some say in their description that they have been abandoned. The state of today's systems
   cannot be known.
4. **Most schemas are outside Search.** The most populous prefixes belong to Assistant, People, Knowledge Graph
   (Webref), NLP, video and Maps (Geostore). The ones most relevant to web search are around `PerDocData`,
   `CompositeDoc`, `CompressedQualitySignals`, `QualityNsr…`, `QualityNavboost…`, `Anchors…`,
   `IndexingDocjoiner…`.
5. **The descriptions are written in internal jargon.** `go/…` links and `google3/…` file paths belong to
   Google's internal network and cannot be opened from outside. When talking about the meaning of an abbreviation
   that the document does not explain (e.g. NSR, Qstar, Craps, Keto, Rhubarb, Tofu), state that this is community
   interpretation and that the document does not give the expansion. To see how a term is used in the document,
   run `leak.py search <term> --width 0`.

## Source links

- Schema page (hexdocs v0.4.0): `https://hexdocs.pm/google_api_content_warehouse/0.4.0/GoogleApi.ContentWarehouse.V1.Model.<SchemaName>.html`
- History of the raw discovery document: the history of the file `contentwarehouse/v1/contentwarehouse-api.json`
  in the `github.com/googleapis/google-api-go-client` repository.
