---
id: "2b5b171feda60695"
title: "ChatGPT can make GIFs now, so I turned one into a game-ready pixel art explosion (step by step)"
url: "https://reddit.com/r/ChatGPT/comments/1xtezyr/chatgpt_can_make_gifs_now_so_i_turned_one_into_a"
link: "https://reddit.com/r/ChatGPT/comments/1xtezyr/chatgpt_can_make_gifs_now_so_i_turned_one_into_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T11:04:43Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["KasperzackGames"]
language: "en"
summary: "ChatGPT can make animated GIFs now, so I tried it for game effects. Here is the full method. The video shows the explosion step by step; the lightning and the volcano in its opening are ChatGPT GIFs (Images 2.6) too, one prompt each, cleaned by the same script and played in a small Godot 4 scene. Problem: the GIF wobbles and won't line up in a game. Fix: pin it to one point in the prompt: \"The…"
tags: ["r/ChatGPT"]
orgs: ["OpenAI", "Anthropic"]
topics: ["jobs & society", "search & media", "agents & coding"]
content_source: "post"
word_count: 531
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1xtezyr/chatgpt_can_make_gifs_now_so_i_turned_one_into_a/"
score: null
comments: null
community: "r/ChatGPT"
---

# ChatGPT can make GIFs now, so I turned one into a game-ready pixel art explosion (step by step)

Reddit · KasperzackGames · 2026-11-11

ChatGPT can make animated GIFs now, so I tried it for game effects. Here is the full method. The video shows the explosion step by step; the lightning and the volcano in its opening are ChatGPT GIFs (Images 2.6) too, one prompt each, cleaned by the same script and played in a small Godot 4 scene. Problem: the GIF wobbles and won't line up in a game. Fix: pin it to one point in the prompt: "The bottom edge of the frame is the ground line, and the explosion hits the ground at the bottom centre, at the same point in every frame." Problem: chunky pixels. Fix: "Use fine pixel art: each art pixel is only 2 to 3 image pixels wide." If it still comes back coarse, re-roll. Problem: you can't cut it out. Fix: "flat solid pure magenta #FF00FF in every frame". For violet effects like lightning use pure green #00FF00, or the key eats the violet. Problem: flames cut off at the top of the frame. Fix: "The tallest flame tips reach about 85 percent of the frame height: always leave empty background above the fire and at both sides, so nothing is ever cut off by the frame edges." Problem: it isn't real pixel art. Up to 253 colours in one frame, soft edges, no shared grid. Fix: a cleanup script that keys out the background, puts every frame on one pixel grid, gives all frames one palette (26 colours for the explosion), pins the blast to the ground (frame-to-frame wobble 0.43 -> 0.30 px) and writes a sprite sheet with JSON. Problem: the effect looks pasted on. Fix: ask an image AI to repaint the background lit by a fire at the blast point, keep only the pixels that got warmer, and blend that copy in near the blast while it burns. The lightning and the cyan beam get a coded colour light with an ordered dither instead. Problem: it doesn't feel like a hit. Fix, in Godot: a 4 to 6 frame hit-stop, 1 or 2 black-and-white impact frames, a 40% flash, screen shake in whole pixels, a few rocks, a scorch mark, embers, and the smoke held for 1.8 s so it drifts away instead of popping. What ChatGPT doesn't do well: it draws "HD pixel art" (its pixels were 2.5 to 4 image pixels wide, not on one grid), it ignores size requests (I asked for at least 512 x 512 and got 316 x 301; all seven came back with about 93,000 to 96,000 pixels), and results vary. 5 of my 7 GIFs were usable; one was too coarse and one was cut off at the top. The stick figures, camera, light, background motion and small extras like rocks and sparks are code; the scripts and the Godot scene were written with an AI coding agent (I used Claude Code; Codex does the same job here). The voice in the clip and in the YouTube video is AI. The full guide and the free kit (prompts, cleanup script, Godot scene, all five effects, MIT) are on GitHub: https://github.com/kasperzackgames/chatgpt-pixel-effects The same video on YouTube, where lightning, fire and an energy beam follow: https://www.youtube.com/watch?v=Zu3a0PBJk_s
