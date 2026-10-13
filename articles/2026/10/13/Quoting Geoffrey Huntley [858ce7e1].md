---
id: "858ce7e14d9130e5"
title: "Quoting Geoffrey Huntley"
url: "https://simonwillison.net/2026/Oct/13/geoffrey-huntley"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-13T13:32:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Simon Willison"]
language: "en"
summary: "If the agent isn't using my diagnostics library, I could introspect and update AGENTS.md, but there's still a delta, and it'll drift. Instead, I write a pre-commit hook that checks the git diff for direct calls to observability modules that bypass my diagnostics module. Boom: fail the commit, inject a prompt telling the agent to use the diagnostics library. All of a sudden it's ten out of ten. \n…"
tags: ["coding-agents", "generative-ai", "git", "agentic-engineering", "ai", "geoffrey-huntley", "llms"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 142
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Quoting Geoffrey Huntley

Simon Willison · Simon Willison · 2026-10-13

13th October 2026
If the agent isn't using my diagnostics library, I could introspect and update AGENTS.md, but there's still a delta, and it'll drift. Instead, I write a pre-commit hook that checks the git diff for direct calls to observability modules that bypass my diagnostics module. Boom: fail the commit, inject a prompt telling the agent to use the diagnostics library. All of a sudden it's ten out of ten.
— Geoffrey Huntley, nobody should type code by hand anymore. here's what's left.
Recent articles
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
