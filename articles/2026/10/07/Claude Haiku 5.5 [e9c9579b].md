---
id: "e9c9579b69181934"
title: "Claude Haiku 5.5"
url: "https://platform.claude.com/docs/en/models/haiku-5-5/overview"
link: "https://platform.claude.com/docs/en/models/haiku-5-5/overview"
source: "Claude Platform Docs"
domain: "platform.claude.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-07T17:56:14Z"
published_date: "2026-10-07"
collected_at: "2026-10-13T20:17:27Z"
authors: ["denysvitali"]
language: "en"
summary: "Claude Haiku 5.5\nFor high-volume, latency-sensitive tasks such as classification, extraction, and routing\n- 1M\n- 128K\n- From $0.10\n- From $0.50\nOverview\nClaude Haiku 5.5 is built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks. It supports adaptive thinking with the effort parameter, a 1M token context window, and up to 128k output tokens.…"
tags: []
orgs: ["Anthropic", "Amazon"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 469
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=49996358"
score: 13
comments: 1
community: "Hacker News"
---

# Claude Haiku 5.5

Claude Platform Docs · denysvitali · 2026-10-07

Claude Haiku 5.5
For high-volume, latency-sensitive tasks such as classification, extraction, and routing
- 1M
- 128K
- From $0.10
- From $0.50
Overview
Claude Haiku 5.5 is built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks. It supports adaptive thinking with the effort parameter, a 1M token context window, and up to 128k output tokens. It uses the same newer tokenizer as Claude 4.7 and later models, so the same text counts as approximately 30% more tokens than on Claude Haiku 4.5. Its thinking blocks work only in the account that produced them, or in an account linked to it.
For code changes, see the migration guide. For model IDs, pricing, and limits, see the Claude Haiku 5.5 overview. For prompting guidance, see Prompting Claude Haiku 5.5.
How it compares
Specifications
Model IDs
Pricing
- Input
- $0.10 / MTok $0.50 / MTok
- Output
- $0.50 / MTok $2.50 / MTok
- 5m cache write
- $0.125 / MTok $0.625 / MTok
- 1h cache write
- $0.20 / MTok $1 / MTok
- Cache read
- $0.01 / MTok $0.05 / MTok
- Batch API
- 50% discount on input and output
Capabilities
- Context window
- 1M tokens
- Max output
- 128K tokens
- Max output (Batch API, beta)
- 300K tokens
- Thinking
- Adaptive
- Default effort
- medium
- Comparative latency
- Fastest
- Input → output
- Text and images → text
- Reliable knowledge cutoff
- Jun 2026
- Training data cutoff
- Jun 2026
Availability
- Status
- Active (latest)
- Released
- October 7, 2026
- Retirement
- Not sooner than October 7, 2027
- Platforms
- Claude APIAmazon BedrockGoogle CloudMicrosoft FoundryClaude Platform on AWS
Good to know
- Adaptive thinking is on by default. Control thinking depth with the effort parameter.
- Omit temperature, top_p, and top_k. See Remove sampling parameters for the values that return a 400 error.
- On the Message Batches API, Claude Haiku 5.5 supports up to 300k output tokens with the output-300k-2026-03-24 beta header.
- The minimum cacheable prompt length is 512 tokens. See Prompt caching.
- Query limits and capabilities programmatically with the Models API.
Resources
Behavioral differences and prompting patterns specific to Claude Haiku 5.5.
Choose a model and effort level, shape prompts, and stream output for faster responses.
Claude Haiku 5.5 determines when and how much to think. Steer depth with effort.
How the context window is counted and managed.
Reference
The system prompt Claude Haiku 5.5 uses on claude.ai and the Claude apps.
Safety evaluations and deployment decisions for Claude Haiku 5.5.
Full price list, including batch discounts and prompt caching rates.
How model IDs, aliases, and pinned snapshots work.
Lifecycle status and retirement commitments for every Claude model.
Was this page helpful?
