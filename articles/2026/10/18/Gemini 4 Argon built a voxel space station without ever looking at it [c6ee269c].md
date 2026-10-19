---
id: "c6ee269c86f282c2"
title: "Gemini 4 Argon built a voxel space station without ever looking at it"
url: "https://reddit.com/r/ClaudeAI/comments/1x94g6o/gemini_4_argon_built_a_voxel_space_station"
link: "https://reddit.com/r/ClaudeAI/comments/1x94g6o/gemini_4_argon_built_a_voxel_space_station"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T14:22:44Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Miserable_Tiger_5742"]
language: "en"
summary: "Follow-up to my space station post from Friday Link . Six models got the same prompt: build a voxel space station you can fly through, in one HTML file. Google's Gemini 4 Argon wasn't available to me yet, so it got the same prompt a couple of days later. How Argon compares to the six: - Time: 18 minutes, second fastest of the seven. The six took 5 min, 22 min, 37 min, 1h 38m, 1h 45m and 2h 20m.…"
tags: ["r/ClaudeAI"]
orgs: ["Google", "Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 402
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x94g6o/gemini_4_argon_built_a_voxel_space_station/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Gemini 4 Argon built a voxel space station without ever looking at it

Reddit · Miserable_Tiger_5742 · 2026-10-18

Follow-up to my space station post from Friday Link . Six models got the same prompt: build a voxel space station you can fly through, in one HTML file. Google's Gemini 4 Argon wasn't available to me yet, so it got the same prompt a couple of days later. How Argon compares to the six: - Time: 18 minutes, second fastest of the seven. The six took 5 min, 22 min, 37 min, 1h 38m, 1h 45m and 2h 20m. - Tool calls: 13, the fewest of the seven. The six made between 21 and 384. - Testing: most of the six opened theirs in a browser to check it (screenshots, test harnesses, a local server). Argon ran its scene in Node against a stand-in for three.js, got "Runtime simulation succeeded! Frames rendered: 4", and its last message admits it was never "visually inspected in a physical browser window." - Size: 92 KB of HTML, right in the middle. The six wrote 48 KB to 292 KB. - Library: three.js r128, from 2021. The other five that used three.js all loaded 0.160 or newer. - Effort: High, the most Antigravity offers. The six ran on Max. What it built: "Aetheria-IX Orbital Citadel", a ring station with ten places you can teleport to (a bridge, a hydroponics dome, a cryo-bay, crew quarters with an arcade, a warp reactor core), plus fly, walk and orbit modes, a roof cutaway and an auto-tour. Unedited: locust.lol/arena/space/game-argon.html What I built: a blind arena. Every model gets the same prompt, runs once with no edits, and you vote on what they made before you see who made what. Friday's six are still blind: locust.lol/arena/space (Argon shows up there as a bonus after you vote; it ran on High, the most Antigravity offers, while the six ran on Max). How Claude Code helped: Claude Code built the arena pages, the vote and reveal (Cloudflare Pages Functions + KV), and the headless Chrome checks that every station loads on desktop and phone. It also writes up each run from the logs, every command and tool call, which is where the Node detail came from. The runs happen in Locust, a desktop app I'm building with Claude Code that runs Claude Code, Codex, Gemini and others side by side. Free to try, no sign-up: all nine rounds are at locust.lol/arena. Locust is free and open source (MIT) for Windows and Mac.
