---
id: "478792a41500f9b2"
title: "Claude to collect and monitor all Global Laws in Git"
url: "https://reddit.com/r/ClaudeAI/comments/1xuuy2o/claude_to_collect_and_monitor_all_global_laws_in"
link: "https://reddit.com/r/ClaudeAI/comments/1xuuy2o/claude_to_collect_and_monitor_all_global_laws_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T01:35:56Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["SnooPeripherals5313"]
language: "en"
summary: "Follow-up to this post which hit #1 on HN a while back (you can read lots of discussion at https://news.ycombinator.com/item?id=50268380 ). Surprisingly, we've had support from legal libraries around the world. But why? The idea is make all law versioned, easily attributable and searchable by agents (with 1 common set of tools for every legislation). I also believe this information should be…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["policy & regulation", "agents & coding", "search & media"]
content_source: "post"
word_count: 307
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xuuy2o/claude_to_collect_and_monitor_all_global_laws_in/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude to collect and monitor all Global Laws in Git

Reddit · SnooPeripherals5313 · 2026-11-13

Follow-up to this post which hit #1 on HN a while back (you can read lots of discussion at https://news.ycombinator.com/item?id=50268380 ). Surprisingly, we've had support from legal libraries around the world. But why? The idea is make all law versioned, easily attributable and searchable by agents (with 1 common set of tools for every legislation). I also believe this information should be freely available so CC0 license (do whatever you want with it). If interested, repo linked below, I'd welcome all comments and advice. Thanks! https://github.com/lexifina/global-law I built this project with Claude Code. It's completely free to use/try. The approach is pretty simple: use Claude to make legislation attributable (git blame, versioning with timelines). Claude Code (Claude Opus 5.5) wrote nearly all the code. I set the goals, chose the sources and made the design decisions. Specifically: I ran separate Claude Code sessions, one per country or group of countries. Each one read the official publisher's site or API, checked robots.txt and the terms of use, and wrote a script that downloads every version of each law. The script then writes them out as a git history, one commit per change on its in-force date. When a source only publishes amending Acts, the script rebuilds past versions by applying each amendment in turn. I also worked on how the countries combine into one tree, with each country as a git submodule and all their histories interleaved by in-force date. Claude wrote the build script to ensure two independent builds come out hash-for-hash identical (usually i'd consider this overkill, but you want a good VCS for this). Since last time, i've set up an automated legislative monitoring system, set this up as a free hosted mcp/api, and formalised some law. Recently, we also formalise all open US case law (you can read about that here if interested): https://lexifina.com/blog/formalizing-all-us-case-law-in-lean
