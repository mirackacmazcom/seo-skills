# Background: the archive's scope and limits

The archive is made of two layers (17 November 2026):

1. **BigQuery layer (broad scope).** Every publication in the `patents-public-data.patents.publications` table
   whose title, abstract, claims or description contains this regular expression:
   `large[ -]language[ -]models?|\bllms?\b|大语言模型|大型语言模型|大模型|大規模言語モデル|대규모 언어 모델|거대 언어 모델|대형 언어 모델|große[ns]? sprachmodell|grands? modèles? de langage`
   → 116,732 publications (90,338 families). Then the non-matching members of the same families (bibliographic
   data + abstract) → 21,947 publications.
   **Second query (synonyms, same day):** publications not found by the first query that contain one of these
   terms: generative / large-scale / pre-trained language model, foundation model, generative pre-trained
   transformer, ChatGPT, GPT-3/3.5/4/4o/5, transformer-based language model; traditional Chinese 大型語言模型 /
   大語言模型, 生成式语言模型, 预训练语言模型; Japanese 事前学習済み言語モデル; Korean 초거대 모델 / 초대규모 언어 모델 /
   생성형 언어 모델; and the Spanish, Portuguese and Russian equivalents of "large language model"
   → 13,286 publications (8,871 families; 7,214 US) + 5,236 family-member publications. "foundation model" and
   "pre-trained language model" are broad terms; publications that match only these with a priority before 2018,
   or that use the term only in the description, are weak.
   Deliberately left out: "chatbot", "conversational AI", "generative AI" (not specific to LLMs, very noisy), and
   bare "GPT" (confused with the GUID Partition Table).
2. **Company layer (the section further below).** 553 publications collected from the Google Patents pages of ten
   LLM companies; the company label, the acquisition information and the full text of non-US publications such
   as WO/EP/JP come from here. If the same publication is also in BigQuery, the page record is used.

Totals: `python3 scripts/patent.py stats` (both queries + the company layer).

The archive is hosted on seoskills.io and searched through its API (see "How searches run" in `SKILL.md`). The
patent texts are stored compressed inside the database and are read with `patent.py show/claims/passages`.

## Weak-match rule

A family counts as `weak-match` if no matching member of the family has the term in its title/abstract/claims
(it occurs only in the description), or if its priority is before 2018 and it matched only on the abbreviation
"LLM"/"大模型". About 22 thousand families fall into this group; hundreds of old US patents with priorities from
1890–1975 are OCR noise and are always weak. `--core` removes them.

## Company label

In the BigQuery records the company is derived from the `assignee_harmonized` name with regular expressions; if
one member of a family is labelled, the other members get the same label. The BigQuery records carry no
acquisition information (`acquired` comes only from the company layer).

---

# Company layer (first compilation)

## How it was compiled (17 November 2026)

1. Search on Google Patents by assignee: `assignee=OpenAI`, `Anthropic`, `Perplexity`, `Mistral AI`,
   `Cohere Inc`, `AI21 Labs`, `Character Technologies`, `Stability AI`, `深度求索` (DeepSeek), `Hugging Face`.
   Unrelated companies with the same name were removed by hand (NEC, the Italian "Openai Srl", the wireless
   communications company Cohere Technologies, General Electric, etc.). Result: 175 seed publications.
2. The Google Patents page of each publication was downloaded; family members (continuations, WO/EP/JP/KR/CN/GB
   counterparts) were added from the page's "Family" and "Also Published As" sections. "Family Cites Families"
   (other companies citing the family) was deliberately left out.
3. The pages were converted to text and loaded into the same SQLite/FTS5 database format as the `google-patents`
   skill.

Total: 553 publications, 163 families, 521 publications with full text. The full text comes from the Google
Patents page.

## Limits

- **It is a lower bound.** Unpublished applications (secret for the first ~18 months), applications filed under a
  different legal entity name, and records in which Google Patents spells the assignee differently may be missing.
- No records were found for xAI or Inflection in the company layer. Big tech companies are in the BigQuery layer.
- **Ownership and legal status are Google's estimate.** For the definitive status use USPTO Assignment / Patent
  Center.
- For AI21 Labs and Anthropic, some EP/GB publications have bibliographic data only (`abstract-only`).

## Labels

- `granted` / `application`: a US granted patent (B1/B2) or application (A1) publication.
- `acquired`: the original applicant is not the company itself. The main ones: IBM → Anthropic (2025), Rain
  Neuromorphics → OpenAI, Rockset → OpenAI. Misspellings and transliterations (Openal, Ouai, 오픈에이아이,
  アンソロピック, Anselponi) were counted as the company itself.
- `company:<name>`: whose record it is (filter with `--company`).
- `AI`: a term such as language model, generative model or neural network occurs in the title/abstract/claims.

## Notes on reading patents

The same reading rules as in the `google-patents` skill apply: the priority date is the time of the invention;
continuation patents share the description but have different claims; the claims are the legal scope, while the
description is full of examples.
