---
id: "7ece378d343df19a"
title: "Anthropic shipped message threads (beta): Claude Code now sends only new messages per turn, about 35% lower time to first token on 500k to 1M token requests"
url: "https://reddit.com/r/ClaudeAI/comments/1xnc4ew/anthropic_shipped_message_threads_beta_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xnc4ew/anthropic_shipped_message_threads_beta_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T02:07:50Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["emarkosov"]
language: "en"
summary: "Published Nov 2 on claude.com, so two days old, but I haven't seen it discussed much. Details: - New `thread` parameter on the Messages API, beta header `message-threads-2026-08-12`. The first request sends the full conversation and starts a thread. Later requests send only the new messages plus the ID of the previous response. - Already on by default for most Claude Code users. You probably…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Microsoft", "Amazon"]
topics: ["agents & coding"]
content_source: "post"
word_count: 274
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xnc4ew/anthropic_shipped_message_threads_beta_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Anthropic shipped message threads (beta): Claude Code now sends only new messages per turn, about 35% lower time to first token on 500k to 1M token requests

Reddit · emarkosov · 2026-11-04

Published Nov 2 on claude.com, so two days old, but I haven't seen it discussed much. Details: - New `thread` parameter on the Messages API, beta header `message-threads-2026-08-12`. The first request sends the full conversation and starts a thread. Later requests send only the new messages plus the ID of the previous response. - Already on by default for most Claude Code users. You probably have it without changing anything. - Median time to first token drops about 35% for requests between 500k and 1M tokens. Smaller payloads over the wire too, which matters for computer-use agents sending screenshots every turn. - Token usage and pricing do not change. Claude still reads the full conversation every turn. Same rate limits. - Threads live in memory, encrypted, not written to disk. A thread expires 5 minutes after its last request and is deleted no more than an hour after. Then the client resends the full conversation and starts a new one. - Limits: max 4 cache_control breakpoints per thread request, continue requests can't include system or tools (you get a 400), no Message Batches, token counting or compaction on a thread. Not ZDR or HIPAA eligible, so check that if it applies to you. - Available on the Claude API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed) and Microsoft Foundry. The 5 minute expiry is the part I'd watch. If you leave a session idle, the next turn pays the full resend. If you're working with 1M context, have you noticed the first token coming back faster this week, or is the gap too small to feel in practice? Source: https://claude.com/resources/articles/message-threads
