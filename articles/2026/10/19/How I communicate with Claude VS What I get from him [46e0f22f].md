---
id: "46e0f22f769f62b5"
title: "How I communicate with Claude VS What I get from him."
url: "https://reddit.com/r/ClaudeAI/comments/1x9wt73/how_i_communicate_with_claude_vs_what_i_get_from"
link: "https://reddit.com/r/ClaudeAI/comments/1x9wt73/how_i_communicate_with_claude_vs_what_i_get_from"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T13:24:34Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["ChargeAdventurous751"]
language: "en"
summary: "Shoutout to SNOWFLOW for inspiring me. I let Claude Code do the building with no game engine this time. I feel like it gives better results than going through UE5 or Unity. It's Babylon.js with WebGPU and hand-written shaders, the same stack SNOWFLOW uses. What Claude Code did: - Turned SNOWFLOW's snow terrain into a lake. The waves are one maths function that runs on both the GPU (what you see)…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 337
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9wt73/how_i_communicate_with_claude_vs_what_i_get_from/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How I communicate with Claude VS What I get from him.

Reddit · ChargeAdventurous751 · 2026-10-19

Shoutout to SNOWFLOW for inspiring me. I let Claude Code do the building with no game engine this time. I feel like it gives better results than going through UE5 or Unity. It's Babylon.js with WebGPU and hand-written shaders, the same stack SNOWFLOW uses. What Claude Code did: - Turned SNOWFLOW's snow terrain into a lake. The waves are one maths function that runs on both the GPU (what you see) and the CPU (what the board and boat ride on), so nothing floats above or sinks into the water. - Built the towboat and its V-shaped wake, the rope (a simulated chain from the boat's tower to the handle), and the towing physics: the rope swings you out wide, the board's edge grips, and releasing as you hit the wake launches you. - Made the water react to the rider the way SNOWFLOW's snow did: a spray wall off the edge on hard carves, the board's own wake, and splashes with rings on landings. - Generated the boat, rider and board in code, with a few helper agents working in parallel on those. - Tested without a graphics card by rendering screenshots in headless Chrome and checking that the water drawn on screen matched the water the physics used. Controls: A/D or mouse to carve, hold Space to load up, release on the wake to pop. F1 opens sliders for waves, wake size, boat speed and more. Don't trash me about the life vest and shorts, I modelled them in blender. They're quick placeholders for prototyping. On a serious note, should I finish this game? XD Thinking about adding monoskis, waterskis and all sorts of obstacles and terrain. I made this prototype in 48 hours so there is only 3 tricks so far. The prototype: https://glidewater.vercel.app/ Follow along: https://groups.google.com/g/SBHMN And I'm also interested in working with anyone serious that has a background in animation, blender or game design so hit me up if you want. I have a few projects I'm already building and already finished.
