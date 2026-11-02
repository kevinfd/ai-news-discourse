---
id: "2ee4c43a285ab21e"
title: "Systemadministrator assist by claude"
url: "https://reddit.com/r/ClaudeAI/comments/1xls0kt/systemadministrator_assist_by_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xls0kt/systemadministrator_assist_by_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T08:43:07Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Dry_Eggplant6329"]
language: "en"
summary: "I built jolitz with Claude Code. It turns a terminal AI agent (Claude Code, OpenCode, ...) into a careful sysadmin for your servers over SSH: it asks before changing anything, knows how to undo each change, and logs every step. It’s a fork of heinzel by Stefan Wintermeyer. He moved parts into a Pro version, so I forked it to keep everything free under MIT. What I added AIX support (next to…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Oracle"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 255
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xls0kt/systemadministrator_assist_by_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Systemadministrator assist by claude

Reddit · Dry_Eggplant6329 · 2026-11-02

I built jolitz with Claude Code. It turns a terminal AI agent (Claude Code, OpenCode, ...) into a careful sysadmin for your servers over SSH: it asks before changing anything, knows how to undo each change, and logs every step. It’s a fork of heinzel by Stefan Wintermeyer. He moved parts into a Pro version, so I forked it to keep everything free under MIT. What I added AIX support (next to Linux) An overview page per fleet: EOL dates, changes per host, config drift An optional team hub. The hub never runs commands and never holds SSH keys. How Claude helped I used Claude Code as the main developer and acted as reviewer and sysadmin. I described what I needed from 20+ years of SAP/Oracle operations, Claude wrote the code, and I tested it against real Linux and AIX hosts. Claude wrote most of the AIX specific checks after I gave it the commands and outputs we use in practice (lslpp, oslevel, etc.). For the overview page, Claude designed the data model for EOL dates and config drift and built the UI. I fixed the parts where its assumptions about real servers were wrong. The safety rules (ask first, rollback plan, logging) were refined in several rounds: I let Claude run against test servers, checked where it was too bold, and tightened the rules. Free to try Everything is free and open source under MIT, no paid tier. Clone the repo and follow the README: https://github.com/superlab-by-supbrt/jolitz Feedback welcome, especially from people running mixed fleets.
