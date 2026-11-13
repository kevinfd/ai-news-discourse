---
id: "b008f8cf5a503ee3"
title: "My game got removed from gamedev subs for using AI, so here’s exactly how I made it with Claude"
url: "https://reddit.com/r/ClaudeAI/comments/1xul18m/my_game_got_removed_from_gamedev_subs_for_using"
link: "https://reddit.com/r/ClaudeAI/comments/1xul18m/my_game_got_removed_from_gamedev_subs_for_using"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T18:46:30Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["SirKnighty"]
language: "en"
summary: "I’ve been making games for 19 years. Over the last few years it had turned into a job, and I stopped enjoying it. A few weeks ago I set myself a challenge, take one small game through the entire pipeline on my own with AI. That meant development, art, marketing, the Steam page, and getting it onto the platform. It took about 5 weeks. For the first time in years I was actually having fun making a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["jobs & society", "agents & coding"]
content_source: "post"
word_count: 426
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xul18m/my_game_got_removed_from_gamedev_subs_for_using/"
score: null
comments: null
community: "r/ClaudeAI"
---

# My game got removed from gamedev subs for using AI, so here’s exactly how I made it with Claude

Reddit · SirKnighty · 2026-11-12

I’ve been making games for 19 years. Over the last few years it had turned into a job, and I stopped enjoying it. A few weeks ago I set myself a challenge, take one small game through the entire pipeline on my own with AI. That meant development, art, marketing, the Steam page, and getting it onto the platform. It took about 5 weeks. For the first time in years I was actually having fun making a game again. In the game, you drive a machine into a dense field, clear it, and use what you earned to buy the next field. It's a chill, unrealistic farming game. A couple of gamedev subs removed my posts as I disclosed AI use, so I’m sharing the process here instead, for anyone curious how it actually works. The stack Claude (Opus 5.5) in Claude Code wrote basically all of the C#. I worked with it like a small team of agents. Funplay MCP + Unity 6 let Claude drive the Unity editor directly. It can inspect scenes, change values, take screenshots and play the game, so it can see what it built instead of guessing. Having tested several MCPs: Funplay is the best one IMO Magnific for concept art, textures and material maps. Tripo to turn picked concepts into 3D models. Blender + MCP , driven by scripts, to clean up, split, rescale and fix those models before they go into the game. The automated part This is the part I find most interesting. I ended up with a backlog of cards by writing out plans, design ideas and feedback. A runner script takes one card at a time while I’m away (like sleeping), with a hard time and money budget per card. It works in its own branch, builds the game headlessly, runs tests, drives the built game to measure handling, takes screenshots, and only lands the change if everything passes. The marketing side runs the same way. Scripted camera takes are automatically filmed inside the game, cut into shorts, and queued on a posting schedule. I still made every taste call: how it feels, how it looks, what’s fun. AI didn’t decide what the game was. It still took a lot of manual game design work and feedback to iterate on cutting mechanics and crops, camera, tractor structure and it's movement, and level/environment setup. If anyone wants details on any part of this, ask away. I’m happy to share what worked and what didn’t. And if you’re curious about the game itself, here it is: https://store.steampowered.com/app/5341880
