---
id: "6af5d994aaf67f61"
title: "Use ClaudeCode with real customer data without the data ever reaching Claude"
url: "https://reddit.com/r/ClaudeAI/comments/1x8f0gm/use_claudecode_with_real_customer_data_without"
link: "https://reddit.com/r/ClaudeAI/comments/1x8f0gm/use_claudecode_with_real_customer_data_without"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T16:48:08Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["nahuel990"]
language: "en"
summary: "Baldanders is a free, open-source (MIT) CLI I built for Claude Code users who can't put personal data into Claude: support emails, contracts, HR files, anything with customers' names, IDs or bank details in it. What it does You chat with Claude through your existing Claude Code login, as normal. Before each message leaves your machine, Baldanders swaps names, emails, phone numbers, IBANs, 55+…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI", "xAI"]
topics: ["models & research"]
content_source: "post"
word_count: 273
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8f0gm/use_claudecode_with_real_customer_data_without/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Use ClaudeCode with real customer data without the data ever reaching Claude

Reddit · nahuel990 · 2026-10-17

Baldanders is a free, open-source (MIT) CLI I built for Claude Code users who can't put personal data into Claude: support emails, contracts, HR files, anything with customers' names, IDs or bank details in it. What it does You chat with Claude through your existing Claude Code login, as normal. Before each message leaves your machine, Baldanders swaps names, emails, phone numbers, IBANs, 55+ national ID formats and secrets for tokens like [PERSON_1]. Claude only ever sees the tokens. When the reply comes back, the real values are put back in on your side. The token map never leaves your laptop, and running with -v shows exactly what was sent. Claude Code runs in an empty private directory with all tools and MCP servers disabled, so it can't read your files either. How Claude Code helped build it I wrote the first version myself, then used Claude Code for the big expansion. It took detection from a handful of formats to phones from any country, IBANs for 89 countries and 55+ national ID formats with checksum validation. It also switched names and addresses to a multilingual model and fixed the Codex and Grok providers. It set up the PyPI packaging, the CI matrix (Linux, macOS and Windows on Python 3.10 to 3.13) and trusted publishing, and designed the logo. The part that took the most iteration was tuning detection so it catches real IDs without scrubbing ordinary numbers like order IDs and version strings. Use it free pip install "baldanders[all]" baldanders download baldanders It also works with ChatGPT (Codex login), Grok, and any OpenAI-compatible API. https://github.com/Nahuel990/Baldanders Issues and missed detections are very welcome.
