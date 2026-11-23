---
name: google-leak
description: Searches the 2,756 schemas and 15,050 fields of the Google Content Warehouse API leak (the 2024 "Google leak" / Google Search documentation leak) and answers questions directly from those documents. Use this skill when the user mentions the Google leak, the leaked documents, Content Warehouse, or systems and field names that appear in the leak such as NavBoost, siteAuthority, PerDocData, CompressedQualitySignals, NSR, Twiddler, pandaDemotion, anchor/link signals, click signals, Chrome data or hostAge. Also use it for SEO questions like "does Google store / measure / keep X as a signal", "what is in the leak about X" or "what does the Google leak say", and whenever an SEO claim needs to be verified or refuted against the leaked documents, even if the user never uses the word "leak". Do not answer from memory; always take field names and descriptions from this skill's database.
---

# Google Content Warehouse API leak

This skill gathers **51 revisions** of the Content Warehouse API discovery document, which Google accidentally
published in its own open source repositories between 2022 and 2024, into a single searchable database: 2,756
schemas (2,568 leaked, 188 from the official Document AI Warehouse API) and 15,050 fields. For every field it
records the name, the type, the original description written by Google engineers, and the revisions in which the
field exists.

The goal: answer the user's question based on **what the document actually says**. A great deal of exaggerated
and incorrect commentary on this topic circulates online; the value of this skill is that it can verify a claim
at the source. So take field names and descriptions from the search tool every time, not from memory.

## How searches run

The archive lives on seoskills.io, so nothing is downloaded. The search tool sends its arguments to
api.seoskills.io and prints the answer. It needs internet access; if it reports that it cannot reach the API,
tell the user that their agent blocks network access and that the SEO Skills MCP server
(https://mcp.seoskills.io/mcp) offers the same tools. Search terms are sent to run the search and are not stored.
If the tool says there were too many searches, wait a minute before the next one.

## Search tool

The only tool is `scripts/leak.py` (Python 3, no extra packages needed). Run it from inside the skill folder:

```bash
python3 scripts/leak.py search navboost              # search names and descriptions (all terms must occur together)
python3 scripts/leak.py search click --name-only     # search schema/field names only
python3 scripts/leak.py field siteAuthority          # which schemas contain a field with this name
python3 scripts/leak.py show CompressedQualitySignals          # the whole schema, with full descriptions
python3 scripts/leak.py show PerDocData --brief                # field names and types only
python3 scripts/leak.py show PerDocData --match spam --match scam   # filter fields in a large schema
python3 scripts/leak.py refs QualityNsrNsrData       # who uses this schema, and what it uses
python3 scripts/leak.py history PerDocData --match hostAge   # in which revision a field was added / removed
python3 scripts/leak.py list QualityNavboost         # list schemas by prefix
python3 scripts/leak.py stats --revisions            # database summary and revision list
```

What you need to know:

- **`search` matches substrings** and ignores term order. A search for `author` also returns `authority` and
  `authorized`. If you want whole words, add `--word` (camelCase parts count as words: `hostAge` → `host`, `age`).
  Terms of three letters or fewer (`age`, `ctr`, `nsr`) are matched as whole words automatically. For finer
  filtering use `--regex`.
- **`search` truncates descriptions** (`--width 0` gives the full text); **`show` and `field` always give the
  full text.** Before quoting a description, view its full text with `show <Schema> --match <field>`.
- `search` options: `--limit N`, `--name-only`, `--fields-only`, `--schemas-only`, `--leaked-only` (excludes the
  official API schemas). `show --match` searches both the field name and the description; `show --enum` shows
  all enum values.
- **The status line** describes the schema's place in the leak, not that Google has stopped using the field. All
  leaked internal schemas were removed from the document in the May 2024 cleanup; the phrase "removed it from the
  document after revision …" means the schema had already been removed before the cleanup. Only the
  `[deprecated]` tag or the description itself says that a field has been abandoned.

## How to work

1. **Translate the concept into the document's language.** The documents are in English and use Google's internal
   jargon, while the user asks in SEO terms such as "clicks", "authority" or "sandbox". Look at
   `references/topic-map.md` first: it shows which schemas and fields common SEO concepts correspond to and which
   terms to search for. The file is long; find the relevant heading in its table of contents and read only that
   section.
2. **Search broadly, then go deep.** Find candidate fields with `search`; open the relevant schema with `show` and
   read the surrounding fields too. The meaning of a field usually becomes clear from the schema's own description
   and from neighbouring fields; statements that say something about usage ("used in preliminary scoring",
   "applied in Qstar") are mostly found there. Use `refs` to see where the schema connects (e.g.
   `CompressedQualitySignals` → `PerDocData`).
3. **Check which system the field belongs to.** Most of the schemas in the database belong to systems outside
   Search (Assistant, YouTube, Maps, People, Document AI), and even within Search there are different subsystems
   (index selection, sitelinks, image search). The prefix of the schema name and the schema description tell you
   this. For example, `QualitySitemapScoringSignals` belongs to sitelink scoring; presenting a field from it as a
   general web ranking signal would be wrong.
4. **If you cannot find it, say so and state what you searched for.** Abbreviations (e.g. E-E-A-T) usually do not
   appear in the document; also try the spelled-out form and related concepts (`expertise`, `trust`,
   `authority`). If there is still nothing, say "I could not find a field with this name in the leak", list the
   terms you tried, and show the closest real fields if there are any. Something not appearing in the document
   does not prove that Google does not use it; but attributing to the document something that is not in it
   misleads the user.

## How to build the answer

Answer in the user's language. Leave field and schema names, and the descriptions you quote, in their original
English; if needed, add a short explanation in the user's language next to them. Give the short answer to the
question first, then show the evidence.

Tie every claim to its source:

- Write the field in `Schema.field` form with the type the tool shows: `CompressedQualitySignals.siteAuthority` (`integer(uint32)`).
- Quote the description from the document in quotation marks, without changing its words. You may skip the part
  of a long description that is irrelevant to the question with `[...]`; do not make a cut that changes the
  meaning. If there is no description, say "no description in the document".
- Give the schema's hexdocs link so the user can open the source themselves. The link is printed in the `show`
  output; its pattern is
  `https://hexdocs.pm/google_api_content_warehouse/0.4.0/GoogleApi.ContentWarehouse.V1.Model.<SchemaName>.html`.
  If `show` says "no page in v0.4.0", do not give a link for that schema; just state in which revisions it was
  seen.
- If the field is marked `[deprecated]`, or was added/removed in a particular revision, say so.

**Separate what the document says from your own interpretation.** This is the most important rule of this skill,
because the document only defines data structures:

- The document shows that a field **exists** and how the engineer described it. It does **not** show whether the
  field is used in ranking, what its weight is, or whether it is still active today. Instead of "Google uses X as
  a ranking factor", say "Google has a field named X; its description is as follows".
- If the description states the usage explicitly, convey it as is; this is the document's own statement and the
  most valuable part of the answer.
- If you are making an inference ("this probably means …"), say clearly that it is an inference.
- The document cannot diagnose the user's own site; for questions like "why did my site drop", explain what the
  document shows and do not attribute the cause to the document.

Match the length to the question: if a single field was asked about, a few sentences and a quote are enough; for a
broad question such as "what does the leak say about links", group the relevant fields by theme and put the most
important ones first rather than dumping every result.

### Example

Question: "Does Google keep something called site authority?"

> Yes, there is a field with this name in the leak: `CompressedQualitySignals.siteAuthority` (`integer(uint32)`).
> Its description in the document: "site_authority: converted from quality_nsr.SiteAuthority, applied in Qstar."
> This schema is attached to every document through `PerDocData.compressedQualitySignals`.
>
> That is all the document says: the field exists, it is derived from the `quality_nsr` system, and it is applied
> in "Qstar". How it is computed and its weight in ranking are not stated in the document.
>
> Source: https://hexdocs.pm/google_api_content_warehouse/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals.html

## Reference files

- `references/topic-map.md` — SEO concept → schema/field mapping and suggested search terms (15 topics). Look at
  the relevant section before you start searching.
- `references/background.md` — what the leak is, the timeline, the revisions, Google's statement, and the limits
  of the document. Read it when the user asks about the leak itself, its reliability or its history.
- `data/schemas.jsonl` — the database itself (one schema per line). Normally you do not need to read it directly;
  if the tool is not enough, it can also be searched with `grep`.
