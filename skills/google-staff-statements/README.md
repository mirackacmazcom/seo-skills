# Google Staff Statements skill for Claude and AI agents

<p align="center"><img src="../../assets/cards/google-staff-statements.png" alt="Google Staff Statements skill for Claude and AI agents" width="560"></p>

Search 47,388 public statements by Google's search team, with the date, the question being answered and a link to the source.

Part of [SEO Skills](../../README.md), free skills that answer from primary sources. Full page with an example answer: [seoskills.io/skills/google-staff-statements](https://seoskills.io/skills/google-staff-statements/).

## Ask it

- "What has John Mueller said about disavowing links?"
- "Did Gary Illyes really say that about crawl budget?"
- "Has Google's advice on this changed over the years?"

The agent uses the skill when your question calls for it. To call it by name in Claude Code: `/google-staff-statements` (or `/seo-skills:google-staff-statements` when installed as a plugin).

## See it answer

<img src="../../assets/demos/google-staff-statements.png" alt="Example answer from the google-staff-statements skill, with the search it ran" width="100%">

## Install

All seven skills as a Claude Code plugin:

```text
/plugin marketplace add mirackacmazcom/seo-skills
/plugin install seo-skills@seo-skills
```

Or only this skill:

```bash
mkdir -p ~/.claude/skills
curl -L https://seoskills.io/downloads/google-staff-statements.zip -o /tmp/google-staff-statements.zip
unzip -o /tmp/google-staff-statements.zip -d ~/.claude/skills/
```

Other agents (Codex, Cursor, Gemini CLI, Copilot, OpenCode): see the [install section](../../README.md#install).

## Answer settings

Answers come in the language you write in, short and with sources. Ask for a brief or detailed answer, a fixed language, or no sources: see [answer settings](../../README.md#answer-settings).

## What is in this folder

- `SKILL.md`: when the agent should use the skill, the search commands and the rules for quoting sources
- `references/`: topic map and background notes the agent can read
- `scripts/statements.py`: sends the search to api.seoskills.io and prints the result, for example `python3 scripts/statements.py search disavow --person mueller --from 2023`

The archive itself stays on seoskills.io. Search terms are sent only to run the search. They are not logged or linked to you; results are cached for up to an hour so repeat searches are fast.
