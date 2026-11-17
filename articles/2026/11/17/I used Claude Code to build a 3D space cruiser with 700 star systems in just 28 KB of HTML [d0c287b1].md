---
id: "d0c287b15c67e22c"
title: "I used Claude Code to build a 3D space cruiser with 700 star systems in just 28 KB of HTML"
url: "https://reddit.com/r/ClaudeAI/comments/1xygtrv/i_used_claude_code_to_build_a_3d_space_cruiser"
link: "https://reddit.com/r/ClaudeAI/comments/1xygtrv/i_used_claude_code_to_build_a_3d_space_cruiser"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T10:15:01Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["lighght"]
language: "en"
summary: "Try it in your browser | Source code on GitHub Free to play, nothing to install. Runs in the browser on desktop and mobile. After seeing the 97 KB underwater world posted here recently, I wondered whether the same technical approach could work for a little 3D space exploration demo. So I prompted Claude Code to build one. The result is Post Apocalyptic Space Cruise , a procedurally generated…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 310
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xygtrv/i_used_claude_code_to_build_a_3d_space_cruiser/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Claude Code to build a 3D space cruiser with 700 star systems in just 28 KB of HTML

Reddit · lighght · 2026-11-17

Try it in your browser | Source code on GitHub Free to play, nothing to install. Runs in the browser on desktop and mobile. After seeing the 97 KB underwater world posted here recently, I wondered whether the same technical approach could work for a little 3D space exploration demo. So I prompted Claude Code to build one. The result is Post Apocalyptic Space Cruise , a procedurally generated galaxy with 700 star systems that you can freely explore. You'll encounter red dwarfs, sun-like stars, white dwarfs, neutron stars, supergiants, black holes, gas giants, rocky planets, and moons. As deep space contains a whole lot of nothing, you can travel relatively fast between stars, but slow down automatically when approaching celestial bodies. You can also adjust your ship's speed manually. The star and planet distributions are based on the generation formulas from WHERE ARE THEY?, a little 2D space exploration roguelike I've been developing. How I built it with Claude Code: My initial prompt described the technical approach and the kind of space exploration experience I had in mind. Claude Code generated the WebGL2 rendering code, procedural planets and textures, and synthesized audio. It took a few follow-up prompts to get the star/planet distributions closer to my existing game and to improve the travel speed and controls. The initial HTML file was about 26 KB. After adding some metadata and other little adjustments, the final file is around 28 KB . All the 3D visuals and sounds are generated directly in your browser, without pre-made 3D models, texture files, or audio files. The start screen does load a separate GIF and font. The demo still has some glitches, and the mobile controls are a bit fiddly. Older phones might also struggle with the higher graphics settings. Anyway, it was a fun little experiment, and I'm curious what you think! :)
