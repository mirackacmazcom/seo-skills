# Google Maps Ranking skill for Claude and AI agents

<p align="center"><img src="../../assets/cards/google-maps-ranking.png" alt="" width="560"></p>

Answer local SEO and Google Maps ranking questions from 326 patent families, 111 official documents, 45 staff statements and 26 Google Research papers.

Part of [SEO Skills](../../README.md), free skills that answer from primary sources. Full page with an example answer: [seoskills.io/skills/google-maps-ranking](https://seoskills.io/skills/google-maps-ranking/).

## Ask it

- "Do reviews affect local ranking?"
- "The client wants to add the city to their Business Profile name. Good idea?"
- "Which patents describe ranking local results by distance?"

The agent uses the skill when your question calls for it. To call it by name in Claude Code: `/google-maps-ranking` (or `/seo-skills:google-maps-ranking` when installed as a plugin).

## See it answer

<img src="../../assets/demos/google-maps-ranking.png" alt="Example answer from the google-maps-ranking skill, with the search it ran" width="100%">

## Install

All seven skills as a Claude Code plugin:

```text
/plugin marketplace add mirackacmazcom/seo-skills
/plugin install seo-skills@seo-skills
```

Or only this skill:

```bash
mkdir -p ~/.claude/skills
curl -L https://seoskills.io/downloads/google-maps-ranking.zip -o /tmp/google-maps-ranking.zip
unzip /tmp/google-maps-ranking.zip -d ~/.claude/skills/
```

Other agents (Codex, Cursor, Gemini CLI, Copilot, OpenCode): see the [install section](../../README.md#install).

## What is in this folder

- `SKILL.md`: when the agent should use the skill, the search commands and the rules for quoting sources
- `references/`: topic map and background notes the agent can read
- `scripts/search.py`: sends the search to api.seoskills.io and prints the result, for example `python3 scripts/search.py search business name keyword`

The archive itself stays on seoskills.io. Search terms are sent to run the search and are not stored.
