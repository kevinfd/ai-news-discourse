---
id: "deaf100114892826"
title: "Week 13 of making fishing and exploration game - demo almost finished"
url: "https://reddit.com/r/ClaudeAI/comments/1xgoj4i/week_13_of_making_fishing_and_exploration_game"
link: "https://reddit.com/r/ClaudeAI/comments/1xgoj4i/week_13_of_making_fishing_and_exploration_game"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T10:09:06Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["RUSuper"]
language: "en"
summary: "Hello there again :) This is Week 13 of me posting this \"dev log\" so to say and explaining how I do things and talking about progress. While \"exploration\" mechanic was added one week ago, I was finally able to make it feel like a proper completely equal part to fishing segment of the game. And with \"Ship in a bottle\" collection done to 29 out of 40 total ships I'm happy how this progress. As…"
tags: ["r/ClaudeAI"]
orgs: ["OpenAI", "Anthropic", "Google"]
topics: ["agents & coding"]
content_source: "post"
word_count: 696
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgoj4i/week_13_of_making_fishing_and_exploration_game/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Week 13 of making fishing and exploration game - demo almost finished

Reddit · RUSuper · 2026-10-27

Hello there again :) This is Week 13 of me posting this "dev log" so to say and explaining how I do things and talking about progress. While "exploration" mechanic was added one week ago, I was finally able to make it feel like a proper completely equal part to fishing segment of the game. And with "Ship in a bottle" collection done to 29 out of 40 total ships I'm happy how this progress. As always weekly progress can be seen on my profile. DEMO DOWNLOAD - FREE Demo doesn't really have everything newest and most polished so you might not have ships in the bottles, that version is being kept for steam release which I will do once steam approves my ID verification (it already is exactly 1 month). Zone 1 out of 5 (demo) is almost entirely done, some smaller polish parts and bug fixes are left. What was done this week: This week I added curios, rarest ship in the bottle is actually cracking the walls of the bottle when shooting cannons and all the items in zone 1 are adjusted manually where they gonna drop or how they are earned. etc. Some zones were a bit improved as can be seen in the video to not look too boring even though there is no gameplay there. Engines with their own sounds were added and can be seen when changed. Cabinet new 3D scene with collections was fully fixed in terms of lighting and small island dioramas were made. As I mentioned before 29 of 40 ships in a bottles were created with textures and added to bottles. This time while still using Decisions.md like before that tags every decision in the game with [USER] or [PROPOSED] (By AI) And User ones have priority over proposed ones, helps with AI hallucinations in the project where AI can't gaslight you into telling you something was decided by you if it really wasn't (it has more than 350 decisions by now). I switched workflow a bit. This time I tried doing something else instead of my old "manager" session managing other sessions and sending them tasks. I created "Effort" sessions (Medium to Max) and have Jev decide which tasks goes into which effort level and then just "manager session" sending it to different effort levels and doing it this way. Though this is polish stage and not much was done it is hard to say if this is more token efficient than before, in general I feel no difference in quality or token usage than with my previous workflow, though that is just subjective feeling, somebody could test it properly I guess. Jev basically scans every task I give to my Claude sessions and just decides which effort certain tasks deserve. Models were made by TripoAI and Opus 5.5 via Blender MCP mostly for this week. It can be seen in the video. For example rarest ship that is inspired by Black Pearl and shoots cannons in the bottle was done in TripoAI then fixed a bit in Blender by Opus 5.5 . I do not use anymore any other AI other than Claude Opus 5.5 , no more Astra and didn't even try Gemini sadly, for now Opus is more than enough for my needs. People have asked me how I make textures and those are either directly done by ChatGPT using OpenAI API key provided to Opus 5.5 or in TripoAI , those done in Tripo are 1k textures as I don't need any heavier ones as they take a lot of memory. Total cost: Claude Max 200$ x 3 = 600$ Astra 100$ x 1 = 100$ ElevenLabs x 11$ = 11$ TripoAI 20$ x 2 = 40$ OpenAI API credits 70$ = 70$ Other things I forgot about 100$ = 100$ (around) Around 900-950$ Disclosure: I’ve been writing these devlogs since Week 1. Since Week 8, Tripo has been supporting them (paid collaboration + a gifted Max plan). That’s why my cost breakdown no longer includes Tripo (Except what I paid from my own pocked for first 8 weeks). If you’re doing this yourself, add their plan to the total.
