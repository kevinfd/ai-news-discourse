---
id: "d5b580da604ed34e"
title: "How I gave my coding agents human-like memory"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xu3smf/how_i_gave_my_coding_agents_humanlike_memory"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xu3smf/how_i_gave_my_coding_agents_humanlike_memory"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T04:51:31Z"
published_date: "2026-11-12"
collected_at: "2026-11-12T13:04:19Z"
authors: ["karatyma_dev"]
language: "en"
summary: "(not written with ai..?) Basically, a few months ago, I hated the fact that memory.md files & claude.md took up a huuuuge chunk of my context window during model switching/effort switching (& during cache refreshes). Didn't really find any definitive solutions outside of relatively complex LangChain, Mem0, and Supermemory implementations (where you have to install unnecessary SDKs and all), so…"
tags: ["r/ArtificialInteligence"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 159
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xu3smf/how_i_gave_my_coding_agents_humanlike_memory/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# How I gave my coding agents human-like memory

Reddit · karatyma_dev · 2026-11-12

(not written with ai..?) Basically, a few months ago, I hated the fact that memory.md files & claude.md took up a huuuuge chunk of my context window during model switching/effort switching (& during cache refreshes). Didn't really find any definitive solutions outside of relatively complex LangChain, Mem0, and Supermemory implementations (where you have to install unnecessary SDKs and all), so my goal was to make a simple, one-shot memory solution where you can have your agent recall basically anything. It's called Slaunt and it uses vector embeddings over a simple MCP server that connects instantly (one-click) to all of your agents, and it enables your agents to see what happens across multiple sources too (eg. Vercel, Supabase, AWS, Railway, Linear, Notion, etc.)! Slaunt can enable your agents to recall literally anything, from failed deployments from three months ago, to what a subagent said last week. We're free right now, ask me anything. Sign up at slaunt.ai , thanks guys!
