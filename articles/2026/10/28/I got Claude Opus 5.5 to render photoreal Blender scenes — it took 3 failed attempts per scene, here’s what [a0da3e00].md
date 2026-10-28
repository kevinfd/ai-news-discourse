---
id: "a0da3e00aa060ec7"
title: "I got Claude Opus 5.5 to render photoreal Blender scenes — it took 3 failed attempts per scene, here’s what actually fixed them"
url: "https://reddit.com/r/ClaudeAI/comments/1xhi21l/i_got_claude_opus_55_to_render_photoreal_blender"
link: "https://reddit.com/r/ClaudeAI/comments/1xhi21l/i_got_claude_opus_55_to_render_photoreal_blender"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T08:02:47Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["ApartmentWest8163"]
language: "en"
summary: "I made these stills (4K, Blender Cycles) by having Claude Code write and run every Blender Python script, with me judging the renders by eye and telling it what looked fake. I built a small Claude Code workflow around this; the images are the output. The first version of every scene was bad. What I learned from watching Claude fail: Procedural noise looks like a cartoon. Fjord v1: Claude…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 406
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xhi21l/i_got_claude_opus_55_to_render_photoreal_blender/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I got Claude Opus 5.5 to render photoreal Blender scenes — it took 3 failed attempts per scene, here’s what actually fixed them

Reddit · ApartmentWest8163 · 2026-10-28

I made these stills (4K, Blender Cycles) by having Claude Code write and run every Blender Python script, with me judging the renders by eye and telling it what looked fake. I built a small Claude Code workflow around this; the images are the output. The first version of every scene was bad. What I learned from watching Claude fail: Procedural noise looks like a cartoon. Fjord v1: Claude textured the cliffs, rocks and ice with Noise/Voronoi + flat colour. My feedback: "looks like animation trying to blend into real life". Fix: scanned assets (Poly Haven, Rock Master), and noise only to hide seams. "Describe it and build it" produces mush. Rainforest v7: Claude composed from a text description plus assets and the result was sparse and repetitive, with game-ready palms I could spot instantly. It only improved when I picked ONE reference photo (first generated with Nano Banana, then a real photo) and forced Claude to put every render next to it before sending. I now make that a hard rule. Compare per object, not per frame. Whole-frame comparison hid problems: the fjord's distant peaks looked fine small and "melted like wax" at 100%. Claude now splits the reference into objects (peaks, cliff, foreground rock, water, sky), pulls real photos and measurements for each, and fixes one object per round. Real data beats scattering. For the Grand Canyon, Claude scattered rocks over the far mountains and it got worse. What worked: USGS 1 m lidar + aerial imagery detail, thinner haze, removing a periodic stripe pattern. An erosion add-on that looked great in a video did nothing on real elevation data. Let Claude check itself with scripts.A linter that scans the .blend for floating objects, constant roughness and sRGB normal maps found 87 problems on the rainforest that I'd missed by eye. A separate agent that tries to tell render crops from real photos (blind) is my stopping test. Film grain and blur did nothing while the scene was still far from real: 0 of 18 crops fooled it. \Smaller gotchas Claude logged in a mistakes file:default rock roughness 0.16 = wax look; SUBSURF on rocks froze a render for 20–50 min on one core; volume bounces made god rays too faint vs. real photos; "nothing real has perfectly cut edges" turned out to be a useful rule (bevel and break every edge). Happy to share the mistakes log or answer questions on any step.
