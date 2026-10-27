---
id: "5bb7d69278b7b5fc"
title: "What's your go-to strategy for ensuring geometrical adherence to level design with local LLMs?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xg5qx4/whats_your_goto_strategy_for_ensuring_geometrical"
link: "https://reddit.com/r/LocalLLaMA/comments/1xg5qx4/whats_your_goto_strategy_for_ensuring_geometrical"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T18:56:36Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["swagonflyyyy"]
language: "en"
summary: "I'm using Q3.8-FN-NVFP4 on a fork of Ninfer-v3 to help me design the first vibe-forged Halo Infinite Forge map, a feat previously thought impossible due to AI agents' inability to directly interact with the game (no MCPs, publicly-available APIs, EAC blocks a lot, etc.). Let me give you a little background for my experiment: Halo Infinite is dead, but the Forge game mode (level design and…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 754
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xg5qx4/whats_your_goto_strategy_for_ensuring_geometrical/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# What's your go-to strategy for ensuring geometrical adherence to level design with local LLMs?

Reddit · swagonflyyyy · 2026-10-26

I'm using Q3.8-FN-NVFP4 on a fork of Ninfer-v3 to help me design the first vibe-forged Halo Infinite Forge map, a feat previously thought impossible due to AI agents' inability to directly interact with the game (no MCPs, publicly-available APIs, EAC blocks a lot, etc.). Let me give you a little background for my experiment: Halo Infinite is dead, but the Forge game mode (level design and in-game scripting mode) community is very much alive and we're still making Halo maps to this day. I wanted to see how I could harness local LLMs for making blockouts to speed up development so I can focus on scripting, lighting and gameplay design. Keep in mind the only way you can script maps in Halo Infinite is to manipulate nodes on a nodegraph, akin to UE5's blueprints but on a simpler level. No code input is possible in this mode. Halo Infinite's forge maps are also composed of MVAR files, which contain all the data regarding your map ranging from object placement and their transforms to all the scripts included in your map's nodegraph. While you can extract these MVAR files with some cool hax tools developed by modders, you can't push modified MVAR files to halo infinite directly because EAC blocks it and you can catch a ban. This means you have to do things manually during development inside Halo Infinite. To ease the level design process, I came up with an idea to use a harness, any harness (Opencode v1 in my case) and created dedicated project folders for my maps in which the agent in question would use a combination of open source tools dedicated to interacting with Halo Infinite programmatically to extract assets, understand their default properties and structures, and get the agent to create DCjson files which are run by a Python script to automatically and systematically place these assets on the map via the agent-generated coordinates that determine their 3D position, scale and rotation. I also made sure to get the agent to obsessively create or update a series of nested AGENTS.md files tied to each map's rooms, i.e. each map's rooms get their own folders and each folder gets a series of DCjson files that cover a single layer of that room (walls, floor, ceiling, doorway, etc.) before concatenating them together in a single DCjson file. That consolidated DCjson file gets concatenated to a root-level DCjson file that puts the entire map together in one file, which is ultimately rendered in blender. Each subdir has its own AGENTS.md file describing the room, its purpose, its dimensions, room-specific guidelines and explains how that room connects to other rooms in the map. Aside from that, I also managed to take these DCjson objects and convert them to .blend files so I can visualize them in Blender (and the bot can view it as well via Blender's MCP) before running the python script in Forge, like in the attached images in this post. So what's the problem? The layouts in blender look identical to the ones in Halo Infinite, right? True, but there's a couple of issues with my approach: It takes a lot of trial-and-error to get right, but each new attempt gets better than the last. For smaller models you have to go room-by-room. Local LLMs aren't trustworthy enough for long-horizon, multi-room development. Parallel subagents can only be trusted in short bursts, such as rooms with multiple adjacent rooms and doorways. Since the first and second bullet points seem to work with my current approach, it raises the question of whether it is even worth it to entrust the bot to design these rooms since I still have to sort of micromanage it. The rooms' layouts are relatively simple to do since the bot was instructed to only use a handful of primitive objects from the pool of +800 assets to choose from because it would be easier for it to develop the layouts. That's fine, but I feel like I don't really understand the bottleneck here. Is it the model's capabilities? My approach to agentic level design? Are my instructions and constraints not clear enough? Is it lacking momentum? Am I giving FN too much credit? I feel like it can do better, or maybe I should make the agent think in mathematical terms instead of spatial terms. I really wish I could find an easier way to explain it to the agent. So I ask my question: What would YOU do if you were in charge of this agent?
