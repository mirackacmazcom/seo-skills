# Background: the archive's coverage, its limits, and how to read a patent

## Contents

1. What the archive is and where it came from
2. What is in it and what is not
3. What the tags mean
4. How to read a patent
5. Common mistakes

## 1. What the archive is and where it came from

The archive was compiled in November 2026. Sources:

- **Google Patents Public Data (BigQuery)**: bibliographic data, abstracts, and the full text of US publications
  (26,410 publications).
- **Google Patents pages**: the full text of 331 families with no US equivalent (50 of them English machine
  translations).
- **European Patent Office publication server**: the full text of 35 EP publications.

In total: 54,101 publications, 10,491 patent families, 26,776 publications with full text. The remaining 27,325
publications (countries other than the US) contain only the title, abstract and bibliographic data; their content
is read in the full-text member of the same family.

The archive is hosted on seoskills.io and searched through its API (see "How searches run" in `SKILL.md`).

## 2. What is in it and what is not

**Included** (among publications whose applicant is Google or that were assigned to Google):

- All publications in the information-retrieval class (CPC G06F16 and the older G06F17/30): search, ranking,
  crawling, indexing, query processing, result presentation, website management, image/video/audio search, database
  querying.
- Those with search, ranking, crawling or web page terms in their title or abstract.
- Those in which AI terms occur together with search/query/summary terms (generative search).
- Those with web performance terms (page loading, prerender, prefetch).
- Those that use these terms heavily in the claims or description text (marked `weak-match`).
- The PageRank family registered to Stanford University.
- Publications in the information-retrieval class from DeepMind, Motorola Mobility, Waymo, X/Verily and some
  acquired companies.
- The family members of all these publications in other countries.

**Excluded, and limits:**

- Google patents that meet none of the criteria above (hardware, most advertising technology, Android, maps and so
  on). The archive is not all of Google's patents.
- Patents assigned to Google after February 2017 that do not match these keywords may be missing.
- The full text of 6 families was not available from any source.
- Patents published after November 2026 are not included. Patent applications are published about 18 months after
  filing, so the most recent work (roughly after mid-2025) does not appear in the archive.
- A topic not being in the archive does not show that Google has no patent on it, or that it does not use the
  method.

## 3. What the tags mean

| Tag | Meaning |
|---|---|
| `granted` | A patent granted in the US (kind code B1/B2). The claims have been through examination. |
| `application` | A published US application (A1). It may not be granted; the claims may change or be rejected. |
| `AI` | AI terms occur together with search terms in the title/abstract or the text. |
| `performance` | Web performance terms occur. |
| `acquired` | The original applicant was not Google (IBM, Motorola, Hitachi and so on); Google acquired it later. It does not reflect Google's own engineering. |
| `affiliate:<group>` | `stanford_pagerank`, `deepmind`, `motorola_mobility`, `waymo`, `x_verily`, `acquired_company`. |
| `weak-match` | Not in the information-retrieval class; included only through a text or interface keyword match. It may be off topic (speech recognition, graphics processing, ad bidding and the like). |
| `abstract-only` | No full text. Where possible the tool switches to the family's full-text member and says so. |

`search --core` leaves out the noise in the last three groups (except the PageRank family).

## 4. How to read a patent

**Dates.** The *priority date* is the date the invention was first filed and shows the age of the idea. The *filing
date* is the date that particular publication was filed; for continuations it can be years after the priority date.
The *grant date* is the date the patent was granted. US patents expire roughly 20 years after filing; most patents
with a 2004 priority have expired. Being expired or abandoned does not affect the historical value of the content.

**Family.** Publications based on the same priority form a family: the first application (A1), the grant (B1/B2),
continuations, divisional applications and the equivalents in other countries. Continuation patents share the same
description but have different claims; Google keeps obtaining patents with new claims from the same description for
years. Keeping a family going for a long time shows that Google considered the idea worth protecting; it does not
prove that Google uses it.

**Sections.**

- *Abstract*: a short introduction; it has no legal weight.
- *Claims*: the part that draws the boundaries of protection. **Independent claims** (those that do not refer to
  another claim) are the broadest definition of the invention; they are usually repeated three times, as the
  method, system and computer-medium forms of the same idea. **Dependent claims** ("The method of claim 1,
  wherein...") add further detail; a feature mentioned there is an option, not a required part of the invention.
- *Description*: background, summary, description of the drawings and the detailed description. Phrases such as "In
  some implementations", "for example" and "may" express possibilities. Numbers and thresholds here are almost
  always examples.

**Language.** Patents are deliberately written in general terms: "resource" (page), "document", "search system",
"selection" (click), "entity", "score". Product and algorithm names (Panda, Penguin, Hummingbird, Navboost, AI
Overview) very rarely appear.

## 5. Common mistakes

- **"There is a patent, so they use it."** A patent describes a method; it does not show that it is used.
- **Presenting an example from the description as a rule.** "A short click can be [...] given a low weight (e.g.,
  −0.1)" is an example, not the weight Google uses.
- **Presenting an application as a grant.** In publications tagged `application` the claims may not have been
  examined yet.
- **Presenting an acquired patent as Google's method.** A patent acquired from IBM does not describe Google's
  engineering.
- **Ignoring the date.** A patent with a 2003 priority describes the web of that time.
- **Mapping a patent to a product name and presenting it as fact.** These mappings are interpretation; say so.
- **Generalising from one patent.** Several patents on the same topic usually describe different approaches.
