---
id: "624250e69ef1b987"
title: "Inspired by the Abyssal Garden post, I gave Fable 5.2 the same kind of prompt and a critic subagent: a drivable Fiat Uno with a ladder on the roof, in one HTML file"
url: "https://reddit.com/r/ClaudeAI/comments/1xy28dk/inspired_by_the_abyssal_garden_post_i_gave_fable"
link: "https://reddit.com/r/ClaudeAI/comments/1xy28dk/inspired_by_the_abyssal_garden_post_i_gave_fable"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T21:43:47Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Viktorkav"]
language: "en"
summary: "Drive it in your browser · Source and prompts on GitHub Free to play, nothing to install. It needs Chrome or Edge on a desktop, with WebGPU. Two days ago u/Any-Reputation8118 shared Abyssal Garden , the swimmable ocean in a 97 KB HTML file. What stuck with me was the prompt.txt in their repo: besides describing the scene, it tells Claude how to check its own work. I wanted to see if that…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 556
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xy28dk/inspired_by_the_abyssal_garden_post_i_gave_fable/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Inspired by the Abyssal Garden post, I gave Fable 5.2 the same kind of prompt and a critic subagent: a drivable Fiat Uno with a ladder on the roof, in one HTML file

Reddit · Viktorkav · 2026-11-16

Drive it in your browser · Source and prompts on GitHub Free to play, nothing to install. It needs Chrome or Edge on a desktop, with WebGPU. Two days ago u/Any-Reputation8118 shared Abyssal Garden , the swimmable ocean in a 97 KB HTML file. What stuck with me was the prompt.txt in their repo: besides describing the scene, it tells Claude how to check its own work. I wanted to see if that structure still holds when the subject is something people know by heart, so I wrote my own prompt on the same skeleton and gave it to Fable 5.2. The car: a 1996 Fiat Uno Mille EP, two doors, light blue, with an aluminium ladder strapped to the roof. In Brazil the "Uno with a ladder" is a running joke: the beat-up work car that somehow passes everyone on the highway. So it got its own race track. What the prompt asked for Priorities in a fixed order for when they conflict: visual quality, matching the real car (I attached photos), stable frame rate, file size. No engine and no 3D or physics library. WebGPU, and everything procedural: car, track, forest, sky and materials come from code, with no textures, models or HDRIs. A frame budget on my machine (M4 Max, 2560×1440): 11 ms average GPU time and no frame over 16.7 ms during a scripted 60-second lap. Three checks, and "done" only when all three pass: a visual critic: a fresh subagent every round that gets six fixed camera shots, frames and 8-frame bursts from the lap, and the reference photos. It never sees the code or Claude's reasoning, and it sorts defects into major, medium and minor. The loop runs until nothing above minor is left; GPU timing on the 60-second lap; an automated test that presses every key and checks that the car reacts. How it went Fable 5.2 on high effort ran for 7 h 12 min and 8 critic rounds. The output is a single 603 KB index.html, assembled by a small Node script from JS and WGSL source files. It never reached its own finish line: the critic still flagged 4 major defects in round 8, which is where I stopped it. At API prices that run would have cost about $348. A second prompt added what makes it a game: start screen, gamepad support, a dashboard with speedometer, rev counter, gear and lap times, a benchmark button that replays the scripted lap and reports frame times, and sound. All of it is Web Audio synthesis: a 1.0 four-cylinder engine that follows the revs, tyre squeal, wind, birds in the forest and a crowd as you pass the grandstand. The video is that scripted lap, captured frame by frame with the game's own audio. I also gave the same prompt to Opus 5.5 to compare, and its version is in the repo too: 5 hours, 11 rounds, 341 KB, about $88, and it stopped on its own saying the job wasn't done. Controls: W/S throttle and brake (S reverses), A/D to turn, Space handbrake, C camera, hold V to look back, R puts you back on track, Esc menu, B benchmark, M mute. The menus are in Portuguese, the keys aren't. The prompts are in the repo unedited (also in Portuguese). The code is free for non-commercial use.
