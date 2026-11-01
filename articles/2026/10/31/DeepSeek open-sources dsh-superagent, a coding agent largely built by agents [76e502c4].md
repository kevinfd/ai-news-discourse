---
id: "76e502c4ebad39b1"
title: "DeepSeek open-sources dsh-superagent, a coding agent largely built by agents"
url: "https://github.com/deepseek-ai/dsh-superagent-prototype"
link: "https://github.com/deepseek-ai/dsh-superagent-prototype"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-31T13:41:11Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["wondersky"]
language: "en"
summary: "Research prototype for reference only, not an official DeepSeek product. This code grew out of our team's day-to-day development work, with much of the engineering done by coding agents. Treat it as research code, not production-ready software. It may still contain bugs, and its coding style and engineering practices may be inconsistent. Review and adapt it before using it in your own…"
tags: ["r/singularity"]
orgs: ["DeepSeek"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 366
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50316116"
score: 10
comments: 0
community: "Hacker News"
---

# DeepSeek open-sources dsh-superagent, a coding agent largely built by agents

GitHub · wondersky · 2026-10-31

Research prototype for reference only, not an official DeepSeek product. This code grew out of our team's day-to-day development work, with much of the engineering done by coding agents. Treat it as research code, not production-ready software. It may still contain bugs, and its coding style and engineering practices may be inconsistent. Review and adapt it before using it in your own environment.
We have adapted it for publication, so it is not identical to our internal version or the implementation described in Exploring Super-agent Design: Towards a More Autonomous Agent System. Some designs discussed in the article are directions for future development and are not implemented in this prototype.
dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. It listens to GitHub and, optionally, Feishu. When someone allowed asks the agent for work, it opens a work item, works on it in its own agent session and directory, and answers in the original conversation, for example with a pull request. A web panel shows what needs a person.
It is also a way of working with an agent: take as little human attention as possible, and give as much value as possible. An agent that can act for a whole team can also waste a whole team's attention, so it acts only when asked or when a rule the team wrote allows it, and speaks only when someone must act or can use a result. docs/000-philosophy.md explains the principle and what it asks of the operator.
Setup has many steps, so an agent does it with you. Ask your coding agent:
Read SETUP.md in this repository and set up dsh-superagent with me.
It asks one short question at a time, shows the full plan once, and then installs and configures everything. SETUP.md is what it follows.
Read the numbered documents in order; each builds only on the ones before it.
- 000 Philosophy
- 001 Domain model
- 002 Authorization
- 003 Execution
- 004 Prompts
- 005 Panel
- 006 Deployment: manual setup, configuration, upgrades and troubleshooting
- 007 Architecture
- 008 Cookbook: adding a Source
pnpm check runs the typecheck, the tests and the build.
