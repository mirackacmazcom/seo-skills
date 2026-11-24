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
api.seoskills.io and prints the answer. It needs internet access. If it reports that it cannot reach the API, run the command
once more; if it still fails, tell the user that their agent seems to block network access and that the SEO
Skills MCP server (https://mcp.seoskills.io/mcp, set-up at https://seoskills.io/install/) offers the same tools. Search terms are sent only to run the search. They are not logged or linked to you; results are cached for up to an hour so repeat searches are fast.
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

## Answer settings

The user decides how the answer looks. Three things can be set:

| Setting | Default | The user can ask for |
|---|---|---|
| Language | The language of the user's latest message | A fixed language: "always answer in Dutch" |
| Length | `standard` | `brief` or `detailed` |
| Sources | `on`: quotes, source names, dates and links | `off`: no quotes, links, numbered citations or source list |

What each length contains:

| | `brief` | `standard` (default) | `detailed` |
|---|---|---|---|
| Size | Two or three sentences, at most 60 words | About 120–250 words | Up to about 600 words |
| Sources shown | The one strongest | The one to three the answer turns on | Up to six, grouped by theme |
| Quotes | None needed | One short quote where the exact wording decides | A short quote per source |
| Layout | Plain sentences | Verdict sentence, a few short bullets | Short headings or bold labels are fine |
| What the source cannot show | Inside a sentence, only if it changes the verdict | One sentence | One short paragraph |
| Next step (only when the rule below asks for one) | A clause | One or two sentences | One or two sentences, plus what the sources suggest when read together |

These sizes, and the numbers of sources, quotes and bullets, replace any other count in this file. The line of
links at the end does not count toward the size. A busy reader wants the verdict and the decisive source,
not everything you read: leave side findings out and offer them in one closing line ("I can also go into X").

Where a setting comes from, strongest first:

1. What the user says in the conversation.
2. A line that starts with `SEO Skills:` in your standing instructions (CLAUDE.md, AGENTS.md, project or custom
   instructions), for example `SEO Skills: detailed answers, sources off, always answer in Dutch`.
3. The defaults above.

People say this in their own words, in any language. Map them like this, and change only what was asked for:

- "short answers", "just the summary", "in one line", "kısa tut" → `brief`
- "shorter", "a bit shorter" about an answer you just gave → about half its length, same sources
- "more detail", "the long version", "every source", "full breakdown" → `detailed`
- "no links" → leave out the URLs only; names, numbers and quotes stay
- "skip the sources", "without quotes", "no citations", "kaynak gösterme" → sources `off`
- "show me the sources", "where does that come from" → sources `on`

A request about one answer ("give me the long version of that", "shorten this") applies to that answer. A request
worded as a preference ("keep it short", "no sources please", "from now on…") holds for the rest of the
conversation. If you cannot tell, treat it as a preference; the user can change it back in a word.

How the settings combine:

- Sources `off`, at any length: say what the answer rests on in plain words inside the sentence, and keep the one
  handle the user needs to look it up: a person and year ("John Mueller said in 2022"), a page name ("Google's
  spam policy"), a patent number ("a 2012 Google patent, US9031929B1"), a field name (`PerDocData.hostAge`).
  Quotes, links, claim and paragraph numbers, platforms and source lists are left out.
- `brief` with sources on: the answer plus the one strongest source (name, date, link). If the verdict needs two
  facts from two pages, name both in the sentence and link the one that carries the verdict.
- When the user changes a setting right after an answer, rewrite that answer from what you already found. Do not
  search again unless the new version needs something you have not read.

The settings are the same for every SEO Skills skill. No setting changes these rules:

- Take every fact, number, date and quote from the search tool, never from memory. With sources off you still
  search first; you only leave the citations out, and you give them as soon as the user asks.
- Keep what the source says apart from your own inference.
- If your environment limits verbatim quotation (for example one short quote per answer), quote the single most
  decisive sentence and report the rest in your own words, keeping the modal verbs ("may", "can", "in some
  implementations") and the locator (field name, claim or paragraph number, section, date). Never write an
  approximate quote.
- Say once what the source cannot show, whenever that changes the conclusion: this archive records what was
  written or said, not how much weight it carries in ranking today, and older material may be outdated. Do not
  repeat the caveat in every bullet.

**Language.** Answer in the language the user writes in, even though this skill, the tool output and the sources
are in English. Search with English terms. Translate ordinary terms; keep quotes, titles, field names and patent
numbers in the original, and add a short gloss in the user's language only where a quote would not be clear
without it. Long titles may be shortened once the number or link is given.

**Close with the next step.** People usually ask because they are about to change something. Close with practical
advice when the user states a plan or a goal ("I'm planning to…", "we want…", "my client wants…", "should I…",
"is it worth…") or asks whether something affects ranking or visibility. Mark it as your suggestion, apart from
what the source says. Build it from what the tool returned in this conversation plus ordinary professional
judgement; do not bring in facts about Google from memory. Skip it when it would only repeat your first sentence,
and when the user only asks what a source says. If this archive is silent on the practical part of the question,
say so in one sentence and name where the answer would be (Google's official documentation, or another SEO Skills
skill) instead of forcing advice out of it. If that other skill is installed, use it: one or two searches there
for the practical part, reported under its own label.

**Several SEO Skills skills installed.** Pick by what the question needs: a rule, threshold or recommendation →
`google-search-docs`; who said what and when → `google-staff-statements`; what data Google stores →
`google-leak`; how a method is described → `google-patents` (search), `google-ai-patents` (AI Overviews, AI Mode,
Gemini) or `llm-patents` (OpenAI, Perplexity and other companies); Maps and local ranking → `google-maps-ranking`.
For "what should I do", start with the official documentation and add another source only if it adds something
the documentation lacks. A combined answer keeps one length setting, with one bold label per kind of source, and
never presents one kind of source as proof of another.

Do not list the settings in every answer. Mention them in one line only when it helps: the user asks what can be
changed, or seems unhappy with the length or the citations.

**If a search fails.** The script retries a dropped connection once by itself. If it still fails, run the command
once more after a few seconds before you conclude that your environment has no network access.

## How to build the answer

Give the short answer to the question first, then show the evidence. Language, length and citations follow the
answer settings above.

Tie every claim to its source. Give the full treatment below to the one or two fields the answer turns on; mention
other relevant fields by name with a gloss of a few words, so the answer does not turn into a catalogue:

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

Match the length to the question: if a single field was asked about, a few sentences and a quote are enough. For a
broad question such as "what does the leak say about links", group the relevant fields by theme (up to five themes in a `detailed` answer),
put first the fields whose description states a use, and name the rest briefly instead of listing every result.
End a broad answer with one or two sentences on what the fields suggest when read together, marked as your
reading. Names in a description (a class such as `SignalPenalizer`, a system such as "twiddler") may be pointed
out as they stand; what they do is your inference unless the description says it.

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
