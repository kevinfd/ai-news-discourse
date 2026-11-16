---
id: "0a707070c2bf4205"
title: "Fable 5.2 just solved a problem I've been struggling with for months"
url: "https://reddit.com/r/ClaudeAI/comments/1xx19zt/fable_52_just_solved_a_problem_ive_been"
link: "https://reddit.com/r/ClaudeAI/comments/1xx19zt/fable_52_just_solved_a_problem_ive_been"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T17:27:29Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["PhillyArbuckle"]
language: "en"
summary: "I've been trying for months and months to build a system that recreates real Premier League matches as animated simulations using match data. It's part of a sports website I've been building called AllSports Radio. The challenge was getting the simulation to actually follow what happened in the real match. I had managed to recreate individual sequences, sort of like a highlights reel, but…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 256
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xx19zt/fable_52_just_solved_a_problem_ive_been/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Fable 5.2 just solved a problem I've been struggling with for months

Reddit · PhillyArbuckle · 2026-11-15

I've been trying for months and months to build a system that recreates real Premier League matches as animated simulations using match data. It's part of a sports website I've been building called AllSports Radio. The challenge was getting the simulation to actually follow what happened in the real match. I had managed to recreate individual sequences, sort of like a highlights reel, but getting an entire 90-minute match to work continuously was a different beast. Then 5.2 dropped, and I decided to throw a pretty ambitious waterfall prompt to see what would happen. The big breakthrough was moving away from trying to steer a free-running simulation toward historical events. Instead, Claude helped build a system that treats the recorded match actions, their timestamps and positions as fixed constraints, then reconstructs the movement and football between them. It built a continuous reconstruction across both halves, with the players and ball moving through the entire match instead of resetting for each highlight. It also made the result scrubbable, so you can jump to any point in the game rather than watching a collection of separate clips. And my god, it actually worked! It's still a work in progress. The match events come from real data, but a lot of the movement between them has to be inferred, so it's not a perfect historical recreation. But this was the golden objective of the entire soccer project, and something I'd been banging my head against for months. Pretty incredible to see it suddenly become possible. Check it out: https://allsportsradio.site/epl/98/wrap
