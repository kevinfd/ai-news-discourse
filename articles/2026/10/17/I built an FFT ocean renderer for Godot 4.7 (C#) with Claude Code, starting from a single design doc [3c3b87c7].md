---
id: "3c3b87c72ac474e8"
title: "I built an FFT ocean renderer for Godot 4.7 (C#) with Claude Code, starting from a single design doc"
url: "https://reddit.com/r/ClaudeAI/comments/1x8emfc/i_built_an_fft_ocean_renderer_for_godot_47_c_with"
link: "https://reddit.com/r/ClaudeAI/comments/1x8emfc/i_built_an_fft_ocean_renderer_for_godot_47_c_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T16:32:38Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["Zionn13"]
language: "en"
summary: "What I built: an open-source, drop-in ocean renderer for Godot 4.7 C#. It simulates waves with three FFT cascades on the GPU, generates foam that forms on crests and dissolves into trails, and shades everything to a soft, painterly, sky-driven look. It runs at 1000+ fps at 1080p on my machine. How Claude Code helped: I didn’t write this iteration of the code by hand. While working on my own…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 328
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8emfc/i_built_an_fft_ocean_renderer_for_godot_47_c_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an FFT ocean renderer for Godot 4.7 (C#) with Claude Code, starting from a single design doc

Reddit · Zionn13 · 2026-10-17

What I built: an open-source, drop-in ocean renderer for Godot 4.7 C#. It simulates waves with three FFT cascades on the GPU, generates foam that forms on crests and dissolves into trails, and shades everything to a soft, painterly, sky-driven look. It runs at 1000+ fps at 1080p on my machine. How Claude Code helped: I didn’t write this iteration of the code by hand. While working on my own project, I wrote OCEAN_GUIDE.md, a single brief covering every technical choice, value, engine gotcha, verification step and dead end I’d found. I gave it to Claude Code in an empty Godot project, and it built the renderer, tests, demo scene and dev tooling from that guide, checking its own work with in-engine screenshots and benchmarks. Then we iterated: I pointed out what looked wrong (seams in the foam, foam that looked embossed, far waves that swam as the camera moved), and Claude found the causes, fixed them and wrote each finding back into the guide. The guide, not the code, is the real artifact: hand it to Claude Code with an empty Godot 4.7 C# project and it should rebuild this ocean. Build stats: Claude Code with Opus 5.5 (medium effort) on the $20 Pro plan. The initial build took ~1 hour, about 40% of one 5-hour session and 5% of my weekly limit. The usage readout puts the whole project, refinement rounds included, at about $58.70 in API-equivalent terms (~$18 for the initial build). On the subscription, it just came out of my limits. Free to try: it’s MIT-licensed and free. Clone the repo, open it in Godot 4.7 (.NET edition), and press Play. The demo opens with live tweak panels and a fly camera (WASD, hold right mouse to look). To use it in your own project, copy the ocean/ folder and instance one scene. Inspired by, and using techniques from, Tessendorf, Sea of Thieves, Atlas, Acerola, 2Retr0’s GodotOceanWaves and Crest (the foam texture). Repo: https://github.com/alozionn/ocean-renderer-godot-csharp
