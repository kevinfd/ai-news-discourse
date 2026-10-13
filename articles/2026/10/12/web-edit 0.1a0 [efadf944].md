---
id: "efadf9441346330c"
title: "web-edit 0.1a0"
url: "https://simonwillison.net/2026/Oct/12/web-edit"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-12T15:54:36Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: web-edit 0.1a0 \n I was working on a project from my phone using Codex Remote when I found myself wanting to edit a credentials file without round-tripping those credentials through the LLM itself. \n So... I had Codex and GPT-6 Astra Extra High build this Python web app which provides a web UI for viewing and editing files in a folder. It's intended to be run over Tailscale, so I can…"
tags: ["projects", "python", "ai", "tailscale", "generative-ai", "llms", "codex"]
orgs: ["OpenAI", "Anthropic"]
topics: ["products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 176
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# web-edit 0.1a0

Simon Willison · Simon Willison · 2026-10-12

12th October 2026
I was working on a project from my phone using Codex Remote when I found myself wanting to edit a credentials file without round-tripping those credentials through the LLM itself.
So... I had Codex and GPT-6 Astra Extra High build this Python web app which provides a web UI for viewing and editing files in a folder. It's intended to be run over Tailscale, so I can have an agent start this running and then edit files via my Tailscale network directly from my phone.
Here's the interface for browsing files in a folder:
Editing uses CodeMirror 6 - I was going to use Monaco but that still doesn't have a great mobile experience yet.
Recent articles
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
