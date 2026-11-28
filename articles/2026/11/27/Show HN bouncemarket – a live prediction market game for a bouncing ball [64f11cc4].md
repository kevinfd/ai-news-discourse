---
id: "64f11cc42feb5246"
title: "Show HN: bouncemarket – a live prediction market game for a bouncing ball"
url: "https://bouncemarket.minhanhday.com"
link: "https://bouncemarket.minhanhday.com"
source: "Minhanhday"
domain: "bouncemarket.minhanhday.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-27T15:01:50Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["mday404"]
language: "en"
summary: "a ball will fall. trade on where it lands. I made this game! Some technical details: The entire drop of the ball is simulated server-side, then streamed to each client as server-sent events with a small buffer. Every drop is deterministic from its starting position, so rounds can be replayed exactly for later analysis, but tiny variations in starting position can change the ultimate outcome.…"
tags: []
orgs: []
topics: []
content_source: "summary"
word_count: 107
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50667726"
score: 388
comments: 130
community: "Hacker News"
---

# Show HN: bouncemarket – a live prediction market game for a bouncing ball

Minhanhday · mday404 · 2026-11-27

a ball will fall. trade on where it lands. I made this game! Some technical details: The entire drop of the ball is simulated server-side, then streamed to each client as server-sent events with a small buffer. Every drop is deterministic from its starting position, so rounds can be replayed exactly for later analysis, but tiny variations in starting position can change the ultimate outcome. There's some AI traders to keep the market moving, but they drop out in any round that has more than five people. They operate using a naive set of rules that I wrote for them, so they're not too hard to b
