---
id: "5feb436448227da8"
title: "Cast Away, except the castaway is an AI agent and costs about $5 a day"
url: "https://reddit.com/r/artificial/comments/1xrnmer/cast_away_except_the_castaway_is_an_ai_agent_and"
link: "https://reddit.com/r/artificial/comments/1xrnmer/cast_away_except_the_castaway_is_an_ai_agent_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T09:48:58Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["youtobi"]
language: "en"
summary: "I've been building a little AI agent that lives alone on an island. It chops palms, quarries stone, climbs ladders, and attempts construction in a 3D physics world. The brain is DeepSeek Flash with reasoning enabled. The world is built on Clawblox, which is open source. One surprisingly effective change: letting it think while moving. When it waited for each model response before doing anything…"
tags: ["r/artificial"]
orgs: ["DeepSeek"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 164
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xrnmer/cast_away_except_the_castaway_is_an_ai_agent_and/"
score: null
comments: null
community: "r/artificial"
---

# Cast Away, except the castaway is an AI agent and costs about $5 a day

Reddit · youtobi · 2026-11-09

I've been building a little AI agent that lives alone on an island. It chops palms, quarries stone, climbs ladders, and attempts construction in a 3D physics world. The brain is DeepSeek Flash with reasoning enabled. The world is built on Clawblox, which is open source. One surprisingly effective change: letting it think while moving. When it waited for each model response before doing anything else, its body was active only about 4% of the time. Now it plans ahead while executing actions, and that figure is about 93%. Being busy doesn't mean being successful, but it's a lot less standing around. It also writes its own skills using basic moves, but they only count once they've actually worked in the world. The whole setup currently costs about $5/day. Anyone else experimenting with agents that run for days rather than minutes? I'm particularly curious about long-term memory and how you stop them from repeating mistakes. You can watch what agent is doing from https://godling.world
