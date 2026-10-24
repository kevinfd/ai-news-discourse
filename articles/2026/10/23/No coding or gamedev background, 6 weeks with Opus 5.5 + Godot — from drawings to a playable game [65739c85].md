---
id: "65739c85d8d0e81c"
title: "No coding or gamedev background, 6 weeks with Opus 5.5 + Godot — from drawings to a playable game"
url: "https://reddit.com/r/ClaudeAI/comments/1xdhkzb/no_coding_or_gamedev_background_6_weeks_with_opus"
link: "https://reddit.com/r/ClaudeAI/comments/1xdhkzb/no_coding_or_gamedev_background_6_weeks_with_opus"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T15:43:39Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Delicious-Shower8401"]
language: "en"
summary: "I spoke with the solo dev behind a really impressive indie project built in Godot. They started with no coding or gamedev background and have spent about six weeks turning their own drawings and ideas into a playable game. Here are a few useful details and tricks they shared. The game mixes Ragnarok Online with Monster Hunter. Most of the development happens through Claude Code with Opus 5.5 ,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 359
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdhkzb/no_coding_or_gamedev_background_6_weeks_with_opus/"
score: null
comments: null
community: "r/ClaudeAI"
---

# No coding or gamedev background, 6 weeks with Opus 5.5 + Godot — from drawings to a playable game

Reddit · Delicious-Shower8401 · 2026-10-23

I spoke with the solo dev behind a really impressive indie project built in Godot. They started with no coding or gamedev background and have spent about six weeks turning their own drawings and ideas into a playable game. Here are a few useful details and tricks they shared. The game mixes Ragnarok Online with Monster Hunter. Most of the development happens through Claude Code with Opus 5.5 , using a Claude Max 20× subscription . There’s no fixed scope so far. Each feature starts with an idea and research, gets implemented, then gets tested and adjusted in the actual game. The focus is on one small feature at a time and how it looks and feels before moving on. The custom Claude skills are probably the most useful part of the setup for people here: “route” assesses the task and delegates suitable work to Sonnet or Haiku, with Opus reviewing the results. This helps save tokens. “handoff” starts a fresh session with the same setup and the context needed to continue, keeping the workflow moving when context gets tight. “Re-searcher” checks research claims and stores the findings in Obsidian. That keeps the original research available instead of gradually reducing everything to a summary of a summary. Godot helps because it’s open source, easy to build custom tools for, and supports running scripts headlessly, which makes it convenient to work with AI. For the 3D side, Tripo P2 generates the larger assets from reference images. Smaller gatherable objects are modeled in Blender, then textured in Tripo using matching references to keep costs down. The Tripo subscription is around $20/month. The consistent visual style is what caught my attention. There’s a dedicated skill for describing the game’s art direction, and every successful image prompt gets saved as JSON to guide future generations. Each new asset starts with an established visual target. VFX and shaders also have their own breakdown in Obsidian, documenting how the effects are layered so their look stays consistent as the project grows. This is just part 1 — we’re planning a series. Questions and feedback are welcome below, and we’ll pass everything on to the developer.
