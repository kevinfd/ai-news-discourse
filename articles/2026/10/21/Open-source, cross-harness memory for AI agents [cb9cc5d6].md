---
id: "cb9cc5d643824d76"
title: "Open-source, cross-harness memory for AI agents"
url: "https://news.ycombinator.com/item?id=50182883"
link: "https://news.ycombinator.com/item?id=50182883"
source: "Hacker News"
domain: "news.ycombinator.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-21T15:42:38Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["shakshukan"]
language: "en"
summary: "Earlier this year, my co-founder and I found ourselves frequently switching between different coding agents (Claude Code, Codex, Cursor) anytime we ran out of shaky usage limits or a newer, better model came out. We became increasingly frustrated with having to re-explain our tasks, workflows, common mistake patterns, etc. anytime we switched agents. We found no good free alternatives out there,…"
tags: []
orgs: ["Anthropic", "Cursor"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 163
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50182883"
score: 16
comments: 11
community: "Hacker News"
---

# Open-source, cross-harness memory for AI agents

Hacker News · shakshukan · 2026-10-21

Earlier this year, my co-founder and I found ourselves frequently switching between different coding agents (Claude Code, Codex, Cursor) anytime we ran out of shaky usage limits or a newer, better model came out. We became increasingly frustrated with having to re-explain our tasks, workflows, common mistake patterns, etc. anytime we switched agents. We found no good free alternatives out there, so we built our own and fully open-sourced it! Beacon hooks into 20+ different agent harnesses, captures session telemetry (prompts, tool calls, command executions, etc) in one normalized format, and distills it into common patterns and repeatable workflows with a human-approval step. This compounded knowledge is then accessible to any future agent via skills / MCP. We believe your agent data is yours to own and should not be locked behind any frontier lab's ecosystem or closed memory infrastructure. We built Beacon to make working across agents way more transparent and efficient. Try it out and tell us what you think: https://github.com/Asymptote-Labs/agent-beacon
