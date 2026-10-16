---
id: "e429541e453f7de2"
title: "i used codex's image generation tool and minimax to make animated rts sprites"
url: "https://reddit.com/r/ChatGPT/comments/1x5v3av/i_used_codexs_image_generation_tool_and_minimax"
link: "https://reddit.com/r/ChatGPT/comments/1x5v3av/i_used_codexs_image_generation_tool_and_minimax"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T16:00:48Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["emersoftware"]
language: "en"
summary: "hello everyone, i'm building a simple rts game for ai agents with codex and claude code. something like age of empires or starcraft for agents, but much simpler. the players are harnesses like codex, claude code and opencode. they connect to the game through cli, api or mcp, read the battlefield as text and give orders. they can also upload javascript scripts to control their units while they…"
tags: ["r/ChatGPT"]
orgs: []
topics: ["agents & coding"]
content_source: "post"
word_count: 375
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1x5v3av/i_used_codexs_image_generation_tool_and_minimax/"
score: null
comments: null
community: "r/ChatGPT"
---

# i used codex's image generation tool and minimax to make animated rts sprites

Reddit · emersoftware · 2026-10-14

hello everyone, i'm building a simple rts game for ai agents with codex and claude code. something like age of empires or starcraft for agents, but much simpler. the players are harnesses like codex, claude code and opencode. they connect to the game through cli, api or mcp, read the battlefield as text and give orders. they can also upload javascript scripts to control their units while they think. the world keeps moving, so taking too long to decide can cost them the match. i'm doing it mostly out of curiosity, because it's fun to watch them play, see what strategies emerge and compare how different models and harnesses handle it. one part of building it that i thought might be interesting to share was making the art and animations. i used the image generation tool inside codex to make the characters and buildings. for the units, we made reference sheets showing the same character facing different directions, keeping the camera, lighting and proportions consistent. a plain magenta background made it easier to remove later. then codex used terminal scripts to send those images to minimax on hugging face and generate short videos for walking, attacking, mining and dying. we used the hugging face cli for authentication and the space's api for generation. codex then extracted the frames, removed the background and packed them into sprite sheets. the game applies team colors and dithering when rendering them. we also used this process for collapsing buildings. there was quite a bit of iteration. some clips changed the weapons or cut off feet. walking animations also paused between loops. one thing that helped was taking a frame from the middle of a step and using it as the start and end reference for a new clip. codex and claude code also helped build and refine the engine and replay viewer. the replays let you switch between the agents' perspectives and click a unit to inspect the scripts it uploaded. it was interesting to have codex work across the whole process: generating images, calling another model, processing the videos and integrating the animations into the game. has anyone tried something similar? how do you keep characters consistent across different animations? age of agents is the name for now.
