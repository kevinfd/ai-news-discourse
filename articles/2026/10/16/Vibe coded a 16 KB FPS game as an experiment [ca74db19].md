---
id: "ca74db192ab62357"
title: "Vibe coded a 16 KB FPS game as an experiment"
url: "https://reddit.com/r/ClaudeAI/comments/1x78955/vibe_coded_a_16_kb_fps_game_as_an_experiment"
link: "https://reddit.com/r/ClaudeAI/comments/1x78955/vibe_coded_a_16_kb_fps_game_as_an_experiment"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T05:54:46Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["zTrojan"]
language: "en"
summary: "I wanted to see how far I could get by vibe coding something that normally takes deep demoscene knowledge. Ended up with a small FPS that fits in 16 KB I used Fable 5 High for the initial planning and Opus 5.5 High for implementation, polishing and optimization The game: You’re blind, underground. Your scanner fires sonar pulses at three frequencies. A pulse briefly lights up walls and enemies,…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["agents & coding"]
content_source: "post"
word_count: 290
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x78955/vibe_coded_a_16_kb_fps_game_as_an_experiment/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Vibe coded a 16 KB FPS game as an experiment

Reddit · zTrojan · 2026-10-16

I wanted to see how far I could get by vibe coding something that normally takes deep demoscene knowledge. Ended up with a small FPS that fits in 16 KB I used Fable 5 High for the initial planning and Opus 5.5 High for implementation, polishing and optimization The game: You’re blind, underground. Your scanner fires sonar pulses at three frequencies. A pulse briefly lights up walls and enemies, then the map fades back to a faint trace. Every pulse is also noise, and everything down there hunts by sound. 3 levels, 3 enemy types plus a boss, pits and bridges, generative music Optimization techniques: The level is a 64×64 cell grid, ray-cast in the fragment shader (2D DDA). That freed ~430 bytes, which then paid for pulse shadows, fake AO and procedural wall patterns Every frame the CPU rewrites one float texture (64×90 RGBA32F). It holds the cells, the enemy list, the pulses, the lamps, the HUD text and even the font bits. The camera’s yaw, pitch and aspect ratio ride in on the texture coordinate of a single glRects . Zero uniforms, zero matrices, one draw call Enemies are signed distance fields built from parts (rounded boxes and “limb” segments, 7 bytes per part), smoothly unioned and sphere-traced. The crawler has six jointed legs that actually walk. Close-ups were slow, so each part got a bounding sphere the shader can skip x87 instead of SSE2, stdcall instead of cdecl, inlining turned off, and a 300 MB Crinkler hash table instead of 100 MB Music is generative. Every bar a tiny LCG picks a chord from a diatonic progression, then pad, bass and arpeggio play it through the same synth as the sound effects Source code and executable: https://github.com/zTrojan/blind-sector
