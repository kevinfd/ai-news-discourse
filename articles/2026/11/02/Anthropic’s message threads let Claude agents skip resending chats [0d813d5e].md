---
id: "0d813d5ec8df2a18"
title: "Anthropic’s message threads let Claude agents skip resending chats"
url: "https://thenextweb.com/news/anthropic-message-threads-beta-claude-api-agents"
link: "https://thenextweb.com/news/anthropic-message-threads-beta-claude-api-agents"
source: "The Next Web"
domain: "thenextweb.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-02T12:14:00Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Ana Maria Constantin"]
language: "en"
summary: "Anthropic's message threads beta lets agents send only new messages to Claude instead of the whole conversation, cutting wait times on long sessions."
tags: []
orgs: ["Anthropic", "Google", "Microsoft", "Amazon"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 314
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic’s message threads let Claude agents skip resending chats

The Next Web · Ana Maria Constantin · 2026-11-02

Anthropic launched message threads in public beta for its API. Agents send the full conversation once, then only new messages, which Anthropic says cuts the wait before Claude replies by about 35% on very long sessions. Prices and rate limits stay the same.
Anthropic has launched message threads, a beta feature for developers building AI agents on Claude, the company said on Monday. Agents no longer have to resend the whole conversation every time they make a request.
A coding agent can make hundreds of requests in one session, and each one normally carries every earlier message and tool result. Once that history runs to hundreds of thousands of tokens, sending it all again adds a delay before Claude starts to reply.
With threads, an agent sends the full conversation once. After that, it sends only what is new, plus the ID of Claude’s last reply.
Anthropic has already switched threads on for most users of Claude Code, its coding agent. On requests of 500,000 to 1M tokens, it says the typical wait before Claude starts answering fell by about 35%.
The feature saves time, not money. Claude still reads the whole conversation on every turn, and Anthropic says prices and rate limits are unchanged. On cost, Anthropic instead cut cache prices by 75% in September, as long agent sessions push up AI bills.
Threads are held in memory, encrypted and never written to disk. They expire five minutes after the last request, so developers must keep their own copy of each conversation. Anthropic says threads are not eligible for its zero data retention or HIPAA health-data setups.
The beta works on all Claude models, on Anthropic’s own platform as well as through AWS, Microsoft Foundry and Google Cloud. It follows Anthropic’s cheaper Opus 5.5 model, released in September.
Get the TNW newsletter
Get the most important tech news in your inbox each week.
