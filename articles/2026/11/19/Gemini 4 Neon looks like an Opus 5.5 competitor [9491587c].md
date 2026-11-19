---
id: "9491587c1875ac6b"
title: "Gemini 4 Neon looks like an Opus 5.5 competitor"
url: "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model"
link: "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model"
source: "Micjm"
domain: "micjm.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-19T00:29:45Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["seizethecheese"]
language: "en"
summary: "Gemini 4 Neon looks like an Opus 5.5 competitor\nTLDR: we project Gemini 4 Neon’s performance based on what a faster Gemini 4 Carbon might score and find it equivalent to Opus 5.5\nGemini 4 Carbon is the best model on the Agent Duel leaderboard if you exclude early voting. Carbon’s main problem is that it is slooooow.\nToday, Gemini 4 Neon was released, and looks to be an incremental benchmark…"
tags: []
orgs: ["Google"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 270
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50554374"
score: 236
comments: 73
community: "Hacker News"
---

# Gemini 4 Neon looks like an Opus 5.5 competitor

Micjm · seizethecheese · 2026-11-19

Gemini 4 Neon looks like an Opus 5.5 competitor
TLDR: we project Gemini 4 Neon’s performance based on what a faster Gemini 4 Carbon might score and find it equivalent to Opus 5.5
Gemini 4 Carbon is the best model on the Agent Duel leaderboard if you exclude early voting. Carbon’s main problem is that it is slooooow.
Today, Gemini 4 Neon was released, and looks to be an incremental benchmark improvement with a very large speed improvement. Earlier today, it was being served extremely fast via OpenRouter: 127 tokens per second. This is way faster than Carbon at 46 tokens per second.
This got me wondering, could Neon be not just a good model but the best model?
Modeling our leaderboard
To investigate, I modeled the win rate in our leaderboard. The best model has three components, model identity, speed and whether the user voted early. My initial modeling did poorly, so I added an interaction between speed and early voting. This ended up working well.
And surprisingly, speed seems to be pretty much as important as model identity (another blog on that soon).
Projecting Gemini 4 Neon performance
If you assume the same performance as Gemini 4 Carbon (which is reasonable given even better benchmark scores), and 127 tps, we would project an Elo on the Agent Duel leaderboard of 1,066, just below Opus 5.5 at 1,078 in our later analysis snapshot.
The 90% interval for the projected Elo difference between Gemini 4 Neon and Opus 5.5 is -94 to +68, with Neon projected to win 48.3% of the time against Opus (counting ties as half a win).
