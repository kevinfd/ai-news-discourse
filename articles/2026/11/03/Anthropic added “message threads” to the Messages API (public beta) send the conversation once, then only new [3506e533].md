---
id: "3506e533ac2d8179"
title: "Anthropic added “message threads” to the Messages API (public beta): send the conversation once, then only new messages. Already on by default in Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xmh012/anthropic_added_message_threads_to_the_messages"
link: "https://reddit.com/r/ClaudeAI/comments/1xmh012/anthropic_added_message_threads_to_the_messages"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T02:27:09Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["emarkosov"]
language: "en"
summary: "Published yesterday (Nov 2) on claude.com. Short version of what it is: - You send the full conversation once. Every later request carries only the new messages plus the previous response ID, so you stop re-sending the whole history every turn. - Anthropic's number: for requests with 500k to 1M tokens, median time to first token drops by about 35%. That is where the long-context pain is, so this…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Microsoft", "Amazon"]
topics: ["agents & coding"]
content_source: "post"
word_count: 201
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmh012/anthropic_added_message_threads_to_the_messages/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Anthropic added “message threads” to the Messages API (public beta): send the conversation once, then only new messages. Already on by default in Claude Code

Reddit · emarkosov · 2026-11-03

Published yesterday (Nov 2) on claude.com. Short version of what it is: - You send the full conversation once. Every later request carries only the new messages plus the previous response ID, so you stop re-sending the whole history every turn. - Anthropic's number: for requests with 500k to 1M tokens, median time to first token drops by about 35%. That is where the long-context pain is, so this is aimed at long-running agents. - A thread expires 5 minutes after its last request. After that your client resends the full conversation and starts a new thread. - Token usage does not change. Standard token rates and existing rate limits apply, so this is about latency, not cost. - Status: public beta on the Claude Platform, plus Claude on AWS, Microsoft Foundry and Google Cloud. - It is already on by default for most Claude Code users, which is where the 35% figure comes from. I want to try this on my own agent loop and see if the number holds outside Claude Code. Has anyone on a 500k+ context agent measured the difference yet, and does the 5 minute expiry get in the way for slow tool calls? Source: https://claude.com/resources/articles/message-threads
