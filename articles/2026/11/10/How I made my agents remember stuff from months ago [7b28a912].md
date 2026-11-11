---
id: "7b28a912bec15df9"
title: "How I made my agents remember stuff from months ago"
url: "https://reddit.com/r/artificial/comments/1xsxudj/how_i_made_my_agents_remember_stuff_from_months"
link: "https://reddit.com/r/artificial/comments/1xsxudj/how_i_made_my_agents_remember_stuff_from_months"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T20:32:41Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["karatyma_dev"]
language: "en"
summary: "(not written with ai..?) (also not focused on profit: read more) Basically, a few months ago, I hated the fact that memory.md files & claude.md took up a huuuuge chunk of my context window during model switching/effort switching (& during cache refreshes). Didn't really find any definitive solutions outside of relatively complex LangChain, Mem0, and Supermemory implementations (where you have to…"
tags: ["r/artificial"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 190
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xsxudj/how_i_made_my_agents_remember_stuff_from_months/"
score: null
comments: null
community: "r/artificial"
---

# How I made my agents remember stuff from months ago

Reddit · karatyma_dev · 2026-11-10

(not written with ai..?) (also not focused on profit: read more) Basically, a few months ago, I hated the fact that memory.md files & claude.md took up a huuuuge chunk of my context window during model switching/effort switching (& during cache refreshes). Didn't really find any definitive solutions outside of relatively complex LangChain, Mem0, and Supermemory implementations (where you have to install unnecessary SDKs and all), so my goal was to make a simple, one-shot memory solution where you can have your agent recall basically anything . It's called Slaunt and it uses vector embeddings over a simple MCP server that connects instantly (one-click) to all of your agents, and it enables your agents to see what happens across multiple sources too (eg. Vercel, Supabase, AWS, Railway, Linear, Notion, etc.)! Slaunt can enable your agents to recall literally anything, from failed deployments from three months ago, to what a subagent said last week. We're free right now and I've made a promise to give the first handful of users lifetime free Pro subs. You'll see an option in settings after you sign up. Sign up at slaunt.ai , thanks guys!
