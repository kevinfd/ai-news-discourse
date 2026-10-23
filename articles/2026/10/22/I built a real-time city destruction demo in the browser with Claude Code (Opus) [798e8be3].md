---
id: "798e8be3b7252b4e"
title: "I built a real-time city destruction demo in the browser with Claude Code (Opus)."
url: "https://reddit.com/r/ClaudeAI/comments/1xclevr/i_built_a_realtime_city_destruction_demo_in_the"
link: "https://reddit.com/r/ClaudeAI/comments/1xclevr/i_built_a_realtime_city_destruction_demo_in_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T15:17:52Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["smith2008"]
language: "en"
summary: "I've been experimenting with Claude Code on a project called Breakable.js. It's an open-source destruction library for Three.js/WebGPU, with a playable demo featuring six different worlds you can blow apart. It has GPU physics, buildings that actually collapse when you destroy their supports, destructible cars, terrain, and pretty much everything else in the scene. I guided the development and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "post"
word_count: 166
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xclevr/i_built_a_realtime_city_destruction_demo_in_the/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a real-time city destruction demo in the browser with Claude Code (Opus).

Reddit · smith2008 · 2026-10-22

I've been experimenting with Claude Code on a project called Breakable.js. It's an open-source destruction library for Three.js/WebGPU, with a playable demo featuring six different worlds you can blow apart. It has GPU physics, buildings that actually collapse when you destroy their supports, destructible cars, terrain, and pretty much everything else in the scene. I guided the development and reviewed the results, but Claude Code did most of the actual work. What impressed me most was how well it handled testing. It wrote 240 unit tests and even ran the game in Chrome, taking screenshots, checking performance, and inspecting the results of explosions. For bigger features, it used multiple agents working in parallel, with other agents reviewing the work. It also built the whole asset pipeline using GPT Image, Stable Audio, image-to-3D models, and Blender scripts. Still plenty of room for improvement, but I'm pretty happy with how far it got. Code (MIT): https://github.com/kchernev/breakable.js To run it needs WebGPU, so desktop Chrome or Edge is recommended.
