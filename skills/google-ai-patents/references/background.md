# Background: the archive's scope, sources, limits, and how to read a patent

## Contents

1. What the archive is and where it came from
2. Scope: what is in and what is out
3. Labels and company groups
4. How to read a patent
5. Common mistakes

## 1. What the archive is and where it came from

Compiled on 17 November 2026. Sources:

- **Google Patents Public Data (BigQuery, `patents-public-data.patents.publications`)**: bibliographic data, abstract,
  CPC and the full text of US publications (36,403 publications). The data covers publications up to 17 September 2026.
- **USPTO assignment records (`uspto_oce_assignment`)**: US patents assigned to Google/DeepMind/Waymo/X/Verily (the
  dataset ends in early 2017).
- **The Google Patents interface**: US publications in AI classes whose current owner is Google were crawled in
  half-year slices; acquired/subsidiary publications missing from BigQuery were added.
- **Google Patents pages**: the full text of 995 families without a US member (mostly 2023–2025 WO applications; 75 of
  them Google's English machine translation of CN/JP/KR/DE/FR publications).

Total: 82,806 publications, 14,495 families; 14,488 families have full text. The archive is a single SQLite database
hosted on seoskills.io and searched through its API (see "How searches run" in `SKILL.md`); `python3 scripts/patent.py stats` summarises it.

## 2. Scope

**What is in** (among publications whose applicant is Google or an Alphabet company, or that were assigned to Google,
**the whole family** if any publication in it matches one of these):

- AI classes (CPC): G06N (machine learning, neural networks, knowledge-based AI, probabilistic models, quantum),
  Y10S706; language and speech (G06F40, G06F17/27–28, G10L13/15/17/21/25, G06F3/167); image and pattern recognition
  (G06V, G06K9, G06T7, G06F18); robotics, autonomous vehicles/drones, health/bio/chemistry AI, learning control (B25J9/16,
  G05D1, B60W60, G16H50, G16B40, G16C20/70, G05B13, G06Q10/04).
- An AI term in the title/abstract (machine learning, neural network, language model, LLM, generative, transformer,
  speech recognition, computer vision, assistant, classifier …).
- At least one AI term in the claims.
- At least five AI terms in the description (families that entered only this way are labelled `weak-match`).

**Limits:**

- Patent applications stay unpublished for ~18 months; most applications filed after mid-2025 are not in the archive.
- 7 families have no full text on Google Patents either.
- Acquisitions after 2017 were checked through the interface only in AI classes; an acquired patent outside the AI
  classes may have been missed.
- The "broadest" definition is inclusive; under labels such as `weak-match`, `security` or `advertising-and-marketing`
  AI may be a side topic.
- Most classic ranking/crawling/PageRank patents outside search are not in this archive but in the `google-patents`
  skill.
- A topic missing from the archive does not show that Google has no patent on it or does not use the method.

## 3. Labels and company groups

| Label | Meaning |
|---|---|
| `granted` / `application` | US grant (B1/B2) / US application (A1; the claims may change). |
| `generative-search` | Generative model terms occur together with search/query/answer terms in the title/abstract (AI Overviews, generative search). |
| `acquired` | The first applicant was not Google/Alphabet; assigned later, or the current owner on Google Patents is Google. |
| `<group>` | The applicant is not Google itself but an Alphabet company or an acquired company (see below). |
| `weak-match` | Entered only through AI terms in the description. |
| `abstract-only` | No full text; the tool switches to a full-text member of the family where possible. |
| `machine-translation` | The full text is Google's English machine translation. Say so when quoting. |

Company groups (the `groups` command gives the counts): `deepmind` (DeepMind Technologies, GDM Holding LLC), `waymo`,
`verily`, `x-development`, `intrinsic`, `isomorphic-labs`, `calico`, `wing`, `mineral` (part of it later went to Deere),
`sidewalk-labs`, `jigsaw`, `fitbit`, `mandiant`, `loon`, `north-thalmic`, `lytro`, `schaft`, `redwood-robotics`,
`speaktoit-api-ai`, `phiar`, `tenor`, `nest`, `atlantic-quantum`, `adhawk` (AdHawk Microsystems), `other-acquired`
(Chronicle, Looker, Kaggle …). An empty group = the applicant is Google itself (`--group google`).

Topic labels (`topics`): `ai-overview-and-generative-search`, `generative-ai-and-llm`,
`search-and-information-retrieval`, `assistants-and-dialogue`, `neural-networks`, `machine-learning`,
`natural-language-processing`, `machine-translation`, `speech-recognition`, `speech-synthesis`,
`image-and-video-recognition`, `image-analysis`, `pattern-recognition`, `model-training-and-efficiency`,
`reinforcement-learning`, `recommender-systems`, `federated-learning-and-privacy`, `autonomous-vehicles-and-drones`,
`robotics`, `health-ai`, `quantum-computing`, `security`, `advertising-and-marketing` and others. They are derived from
the CPC and the title/abstract; do not rely on them alone.

## 4. How to read a patent

- **Dates:** priority (when the idea was first filed), filing, publication, grant. US patents expire roughly 20 years
  after filing.
- **Family:** publications based on the same priority (A1, B1/B2, continuations, WO/EP/CN counterparts). Continuations
  have the same description but different claims. In Google AI patents one invention often produces several US grants
  and a WO publication.
- **Sections:** abstract (no legal weight); claims (the boundary of protection; independent claims are the broadest
  definition); description (examples and options; "in some implementations", "for example" signal a possibility).
- **Language:** "generative model (GM)", "large language model (LLM)", "search result document (SRD)", "natural
  language (NL) based output", "client device", "automated assistant". Product names (Gemini, AI Overview, AI Mode,
  Lens, Bard) almost never appear.

## 5. Common mistakes

- **"It has a patent, so it uses it."** A patent describes a method; it does not show that the method is used.
- **Interpreting by title.** `US12346366B2` "…citations to source documents" is about Drive documents, not web search.
  Read the claim.
- **Presenting an example from the description as a rule.**
- **Presenting an application as a grant.**
- **Presenting a subsidiary's or an acquired patent as Google Search's method.** Waymo, Fitbit and Mandiant patents do
  not come from the search team.
- **Quoting a machine translation as if it were the original text.**
- **Generalising from a single patent.** Several patents on the same topic (e.g. fan-out) describe different approaches.
