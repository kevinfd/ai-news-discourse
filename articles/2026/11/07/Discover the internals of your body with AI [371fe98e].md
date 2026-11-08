---
id: "371fe98ec6f19d2c"
title: "Discover the internals of /your/ body with AI"
url: "https://reddit.com/r/ClaudeAI/comments/1xqd5f3/discover_the_internals_of_your_body_with_ai"
link: "https://reddit.com/r/ClaudeAI/comments/1xqd5f3/discover_the_internals_of_your_body_with_ai"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T18:22:55Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["samewakefulinsomnia"]
language: "en"
summary: "Short backstory, Opus 5.5 appeared to be so great at 3D modeling that I had no choice but to make something fun with it I was always interested in anatomy and wondered how things actually work, as biology lessons with 2D pictures are the least clear stuff out there, so I built Bodylang, an open-source app that lets you chat/model/track your own body throughout the day and through the wide…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches", "health & science"]
content_source: "post"
word_count: 234
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqd5f3/discover_the_internals_of_your_body_with_ai/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Discover the internals of /your/ body with AI

Reddit · samewakefulinsomnia · 2026-11-07

Short backstory, Opus 5.5 appeared to be so great at 3D modeling that I had no choice but to make something fun with it I was always interested in anatomy and wondered how things actually work, as biology lessons with 2D pictures are the least clear stuff out there, so I built Bodylang, an open-source app that lets you chat/model/track your own body throughout the day and through the wide variety of all the situations that could happen to you: https://reddit.com/link/1xqd5f3/video/cf2pzjpvf80i1/player It's a bit early and not all the systems are present, but I find it truly insightful and fun to play with. I actually used another app to make Bodylang a desktop image (interactive, called Splash) on my second monitor, so I'm constantly interacting with it in the background My beloved Opus5.5 did almost all the 3D work and coding. It wrote the Blender pipeline that takes the organs, muscles and vessels from Z-Anatomy and warps them into a separate human body model, both male and female. On top it built a Three.js scene and shaders that light up whatever is being explained, and an animated close-up drawing for each organ, which makes the overall vibe very illustrative The LLM underneath works via your existing Claude Code subscription and its generally very cheap, mostly on Haiku/Sonnet Quick demo: https://bodylang.vercel.app Code: https://github.com/yahorbarkouski/bodylang Let me know if you liked it and how you'd customize it
