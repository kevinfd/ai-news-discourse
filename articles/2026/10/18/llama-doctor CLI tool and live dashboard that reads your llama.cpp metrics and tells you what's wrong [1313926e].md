---
id: "1313926e9f87b5d5"
title: "llama-doctor: CLI tool and live dashboard that reads your llama.cpp metrics and tells you what's wrong"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9aq2i/llamadoctor_cli_tool_and_live_dashboard_that"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9aq2i/llamadoctor_cli_tool_and_live_dashboard_that"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T18:38:01Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["msalsas"]
language: "en"
summary: "https://preview.redd.it/93o5gjyuq9wh1.png?width=2800&format=png&auto=webp&s=86528bbbcee68e37ca775af011c1c16ec87eddd1 Points at a running llama.cpp or Unsloth Studio server, pulls /metrics, /props and /slots, and gives you severity-graded findings: prefill vs decode, queue pressure, prefix cache reuse, memory headroom. Exit codes map to severity, so cron can gate on it. Read-only, stdlib only,…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: []
content_source: "post"
word_count: 60
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9aq2i/llamadoctor_cli_tool_and_live_dashboard_that/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# llama-doctor: CLI tool and live dashboard that reads your llama.cpp metrics and tells you what's wrong

Reddit · msalsas · 2026-10-18

https://preview.redd.it/93o5gjyuq9wh1.png?width=2800&format=png&auto=webp&s=86528bbbcee68e37ca775af011c1c16ec87eddd1 Points at a running llama.cpp or Unsloth Studio server, pulls /metrics, /props and /slots, and gives you severity-graded findings: prefill vs decode, queue pressure, prefix cache reuse, memory headroom. Exit codes map to severity, so cron can gate on it. Read-only, stdlib only, Python 3.10+. https://github.com/msalsas/llama-doctor Open to PRs, especially from anyone with a server that makes it crash.
