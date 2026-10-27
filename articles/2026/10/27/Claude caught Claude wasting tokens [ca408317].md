---
id: "ca408317c60d12dd"
title: "Claude caught Claude wasting tokens"
url: "https://reddit.com/r/ClaudeAI/comments/1xghc4s/claude_caught_claude_wasting_tokens"
link: "https://reddit.com/r/ClaudeAI/comments/1xghc4s/claude_caught_claude_wasting_tokens"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T02:58:49Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["OpenlyPolite"]
language: "en"
summary: "I created a voice-activated helper tool for myself. The tool works great, but it caught an agent burning tokens for no reason. Setup Fable came up with a typical voice-activated CLI tool (STT->server->Claude Code->TTS ). Opus implemented it. All local, except Claude Code acting as an agent that responds to my voice messages. Issue After one weird test session Fable read the transcript and came…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 211
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xghc4s/claude_caught_claude_wasting_tokens/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude caught Claude wasting tokens

Reddit · OpenlyPolite · 2026-10-27

I created a voice-activated helper tool for myself. The tool works great, but it caught an agent burning tokens for no reason. Setup Fable came up with a typical voice-activated CLI tool (STT->server->Claude Code->TTS ). Opus implemented it. All local, except Claude Code acting as an agent that responds to my voice messages. Issue After one weird test session Fable read the transcript and came back with this: The model misbehaved, not the harness. After your question, Claude’s first turn ran for 72 seconds and produced about 8,000 output tokens of plain text consisting almost entirely of zero-width Unicode characters (U+200B, U+200C, U+200D), the invisible kind used for joining or breaking words. No tool call, no say, just a long invisible string, then a final “(silent)”. The harness logs plain text and speaks only \ say`, so you heard nothing, the “waiting” indicator cleared when the turn ended [...]` The log line for that turn records 8,002 output tokens and an estimated cost of about $0.24 [...] That's a first for me. I never caught Claude producing gabage and outputting it myself. And I've never had another Claude session catch that, point fingers and put a price tag on it. Cool stuff and all, bnd I want my $0.24 back! ;)
