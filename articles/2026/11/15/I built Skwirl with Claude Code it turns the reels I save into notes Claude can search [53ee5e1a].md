---
id: "53ee5e1a1baae485"
title: "I built Skwirl with Claude Code: it turns the reels I save into notes Claude can search"
url: "https://reddit.com/r/ClaudeAI/comments/1xx30g3/i_built_skwirl_with_claude_code_it_turns_the"
link: "https://reddit.com/r/ClaudeAI/comments/1xx30g3/i_built_skwirl_with_claude_code_it_turns_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T18:35:01Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["PaRtHuS"]
language: "en"
summary: "I built this myself, almost entirely with Claude Code. What it does I save a lot of dev tutorials on Instagram and YouTube and never open them again. Skwirl takes a reel or post you save, transcribes the audio, reads the text on screen, and writes a short note you can search. It also has an MCP server, so Claude can search those notes. How Claude Code helped build it - Claude Code wrote the…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Meta"]
topics: ["search & media", "agents & coding", "jobs & society"]
content_source: "post"
word_count: 261
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xx30g3/i_built_skwirl_with_claude_code_it_turns_the/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built Skwirl with Claude Code: it turns the reels I save into notes Claude can search

Reddit · PaRtHuS · 2026-11-15

I built this myself, almost entirely with Claude Code. What it does I save a lot of dev tutorials on Instagram and YouTube and never open them again. Skwirl takes a reel or post you save, transcribes the audio, reads the text on screen, and writes a short note you can search. It also has an MCP server, so Claude can search those notes. How Claude Code helped build it - Claude Code wrote the backend: a Cloudflare Worker with a D1 database, the queue that processes saves, and sign-in by email code. - It wrote the pipeline that downloads a reel, transcribes it, pulls the on-screen text from frames, and turns that into a structured note. - It built the MCP server and the OAuth flow, so Claude and other MCP clients can connect. - I ran several Claude Code sessions in parallel, each in its own git worktree, with one session reviewing and merging the others' work. - It also wrote the test suite, which is how I catch regressions before each deploy. My part was the product decisions, the design, and a lot of "no, not like that". How I use it with Claude With the Claude Code plugin, Claude searches my saves at the start of a task without being asked. Last week I asked for a scroll-driven parallax hero, and it pulled up a "4 Web Animation Patterns" reel I'd saved weeks earlier and used it as the reference. Free to try Go to https://skwirl.app , sign up with your email, and paste a reel link.
