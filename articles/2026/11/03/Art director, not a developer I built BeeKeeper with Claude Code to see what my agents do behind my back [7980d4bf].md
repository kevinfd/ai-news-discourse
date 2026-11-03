---
id: "7980d4bf7207e567"
title: "Art director, not a developer: I built BeeKeeper with Claude Code to see what my agents do behind my back"
url: "https://reddit.com/r/ClaudeAI/comments/1xmrcr1/art_director_not_a_developer_i_built_beekeeper"
link: "https://reddit.com/r/ClaudeAI/comments/1xmrcr1/art_director_not_a_developer_i_built_beekeeper"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T12:12:53Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["RanAviv"]
language: "en"
summary: "I run a lot of Claude Code sessions at once and kept losing track of them. Which one is working, which one is waiting for me, which one quietly stopped an hour ago. So I built BeeKeeper, a pixel-art hive. Every project is a room. Every Claude Code chat and every agent is a little character that walks into its room, works with a speech bubble showing what it's doing right now, waits for me, and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["agents & coding", "jobs & society", "models & research"]
content_source: "post"
word_count: 282
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmrcr1/art_director_not_a_developer_i_built_beekeeper/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Art director, not a developer: I built BeeKeeper with Claude Code to see what my agents do behind my back

Reddit · RanAviv · 2026-11-03

I run a lot of Claude Code sessions at once and kept losing track of them. Which one is working, which one is waiting for me, which one quietly stopped an hour ago. So I built BeeKeeper, a pixel-art hive. Every project is a room. Every Claude Code chat and every agent is a little character that walks into its room, works with a speech bubble showing what it's doing right now, waits for me, and falls asleep when it's idle. When Claude calls a subagent, you see it step into the room. How Claude helped: I'm an art director, not a developer, so Claude Code wrote basically all of it from my direction. It's React + Vite with a small Node server that reads the session logs and agent files Claude Code already keeps in ~/.claude and your project folders. I did the art direction, rooms and characters. One thing I changed along the way: I realised most people won't pay to generate their own rooms and characters, so I spent a few more dollars building a bigger free library. It ships with 20 ready rooms and 17 characters. Drawing your own room is optional (about 10 cents with your own Gemini key). Also, the short promo video took 3 times longer than I expected. Classic. - 100% free, open source, MIT licence - Runs locally, only reads your Claude Code folders, nothing is uploaded (the only exception is if you choose to generate a custom room, then your description goes to Google's image model) - Also has tabs for your agents' records and how often you use each skill https://github.com/ranucho/beekeeper Happy to answer anything about how it reads the sessions.
