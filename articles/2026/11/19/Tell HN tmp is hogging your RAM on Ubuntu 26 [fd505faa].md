---
id: "fd505faa8c59cd4e"
title: "Tell HN: /tmp is hogging your RAM on Ubuntu 26"
url: "https://news.ycombinator.com/item?id=50554756"
link: "https://news.ycombinator.com/item?id=50554756"
source: "Hacker News"
domain: "news.ycombinator.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-19T01:13:06Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["boldi"]
language: "en"
summary: "As a Ubuntu user, it was just brought to my attention that /tmp is now mounted on tmpfs (aka your RAM). Coding agents, like Claude Code, use /tmp as a scratchpad for files, model weights, etc. Therefore, if you have RAM constraints, consider setting CLAUDE_CODE_TMPDIR to e.g. ~/.claude/tmp"
tags: []
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 48
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50554756"
score: 10
comments: 4
community: "Hacker News"
---

# Tell HN: /tmp is hogging your RAM on Ubuntu 26

Hacker News · boldi · 2026-11-19

As a Ubuntu user, it was just brought to my attention that /tmp is now mounted on tmpfs (aka your RAM). Coding agents, like Claude Code, use /tmp as a scratchpad for files, model weights, etc. Therefore, if you have RAM constraints, consider setting CLAUDE_CODE_TMPDIR to e.g. ~/.claude/tmp
