---
id: "f2c40ed7856de8e9"
title: "One game without AI ($50k, a studio) and one with Claude Code ($700). It’s been… fun :)"
url: "https://reddit.com/r/ClaudeAI/comments/1xwzqi2/one_game_without_ai_50k_a_studio_and_one_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xwzqi2/one_game_without_ai_50k_a_studio_and_one_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T16:27:42Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["noteasytobecheesy"]
language: "en"
summary: "Hey everyone. Thought I'd share my experience with 'made with AI' :) I’m not a developer and never will be though it hasn't been for a lack of trying. I would LOVE to learn to code. I started learning react.js then node js then Python then C++ then html then product design then project management then had an idea for a movie so am 1/3rds through the script (no AI help there, lol) then had an…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 608
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xwzqi2/one_game_without_ai_50k_a_studio_and_one_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# One game without AI ($50k, a studio) and one with Claude Code ($700). It’s been… fun :)

Reddit · noteasytobecheesy · 2026-11-15

Hey everyone. Thought I'd share my experience with 'made with AI' :) I’m not a developer and never will be though it hasn't been for a lack of trying. I would LOVE to learn to code. I started learning react.js then node js then Python then C++ then html then product design then project management then had an idea for a movie so am 1/3rds through the script (no AI help there, lol) then had an idea for a game (that one is shipped) then got sidetracked then had an idea for another game (this one). Never underestimate the power of interests and unfinished business an ADHD person is capable of 😁 Anywho, between three jobs, a family, and doing my best to adult, I had an idea for a game 2 years ago. I paid a studio ~$50k to build from my design the first time. Got torn to shreds on Reddit how 'it's not really my game if I pay developers' and posts got pulled left and right for 'the visuals being sloppy and unprofessional'. Fair enough. For my second game, I didn't have the money to work with a studio again so I decided to give "vibe coding" a try and was honestly blown away by the process. Was fun and challenging and in a few weeks with Claude Code I was able to build a fully playable game with a live Steam page, for under $700. Reddit has been more receptive but when I posted on LinkedIn I was told to ‘learn to code’ and that I was ‘a disgrace’. So I’ve been torn apart from both sides now, which at least feels balanced, lol. The stack Claude Code (Opus 5.5) with the Unity MCP wrote essentially all the C#. Higgsfield for music, voice-over (rendered from my own voice) and the 3D turntable renders I post daily (Building of the Day) Unity 6. A plain design doc + CLAUDE. md before the first prompt - the most valuable hour of the project. What the agents ended up doing that I didn’t plan OBS lagged on my laptop, so Claude built an in-engine replay recorder: frame-stepped capture, re-rendered audio, cursor drawn in. Every gameplay clip I post comes from it. Later it built a scripted version - a shot script in, a finished clip out, so the marketing footage films itself. I had no playtesters. So Claude built a playtest harness (a local API into the built game) and I wrote eight player profiles - the Impatient, the Economist, the First-timer, a Japanese player… Eight agents each play the full 60-day demo and fill in an evaluation sheet. Reading eight sheets side by side found a soft-lock, a wrong-reason bug in 7 of 8 runs, and an economy exploit before any human saw it. 14 languages, with an automated test that catches translated text overflowing its buttons at three screen sizes, including the Steam Deck’s. 360 automated tests, because the least fun part by far was: playtest, find bug, describe it, fix, repeat. ~300 times. What I still did: the idea, the economy, every design and balance decision, every “no, that’s not it”, and all the playing. AI didn’t decide what the game was. My take: “made without AI” isn’t the badge of honour people think, and “made with AI” isn’t a scarlet letter. There are sloppy games on both sides. What vibe-coding changes is who gets to try - people with ideas and very limited budgets. Let players judge the result. Steam page is live, demo 2 December: https://store.steampowered.com/app/5485070 Happy to share the CLAUDE. md, the player profiles, or the prompts - ask away.
