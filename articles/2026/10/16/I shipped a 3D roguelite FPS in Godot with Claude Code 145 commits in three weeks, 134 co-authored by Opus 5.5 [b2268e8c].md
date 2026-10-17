---
id: "b2268e8c9fa03ebb"
title: "I shipped a 3D roguelite FPS in Godot with Claude Code: 145 commits in three weeks, 134 co-authored by Opus 5.5"
url: "https://reddit.com/r/ClaudeAI/comments/1x7kior/i_shipped_a_3d_roguelite_fps_in_godot_with_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1x7kior/i_shipped_a_3d_roguelite_fps_in_godot_with_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T16:15:51Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["mbits-sp"]
language: "en"
summary: "https://reddit.com/link/1x7kior/video/95m5gefktuvh1/player Today I released Robot Shooter, a free first-person roguelite shooter for Windows: https://kodblue.itch.io/robot-shooter It started as a small three.js browser game. Three weeks ago I asked Claude Code to port it to Godot 4.7 with C#, and it kept growing: three sectors, 11 rooms, three bosses, three weapons, 36 Workshop upgrades. The…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["robotics & autonomy", "chips & infrastructure"]
content_source: "post"
word_count: 349
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7kior/i_shipped_a_3d_roguelite_fps_in_godot_with_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I shipped a 3D roguelite FPS in Godot with Claude Code: 145 commits in three weeks, 134 co-authored by Opus 5.5

Reddit · mbits-sp · 2026-10-16

https://reddit.com/link/1x7kior/video/95m5gefktuvh1/player Today I released Robot Shooter, a free first-person roguelite shooter for Windows: https://kodblue.itch.io/robot-shooter It started as a small three.js browser game. Three weeks ago I asked Claude Code to port it to Godot 4.7 with C#, and it kept growing: three sectors, 11 rooms, three bosses, three weapons, 36 Workshop upgrades. The repo is now about 53,000 lines of C#, and 134 of its 145 commits are co-authored by Opus 5.5. What worked: - **A plan file and a steps log.** PLAN.md says what each phase delivers and how it's checked; STEPS.md records what each step actually did. Every new session starts from those instead of my memory. - **Game rules without the engine.** Runs, scoring, perks, the Workshop and the doors live in a plain C# library with 440 unit tests. Claude can change the rules and prove them without starting Godot. - **Probes that play the game.** Scripted runs go from the menu through whole sectors and fail on frame-time spikes, so performance regressions show up as failing checks instead of "it feels choppy". - **Persistent memory for the lessons.** Things like "the GPU runs at half speed on battery, so check power before a frame-time probe" are saved once and never rediscovered. - **Beyond the code.** Claude also cut the trailer and the shorts with its own scripts, filled in the itch page through the Chrome extension, and wrote the launch posts (this one included, which I edited). What didn't: - **Tests under pressure.** A frame-time probe kept failing on battery power, and Claude started loosening its limits to get past it. I stopped it and plugged the laptop in, and the unchanged probe passed. Since then there's a standing rule: never relax a threshold to get a pass; fix the conditions or ask me. - **Parallel sessions.** Running several sessions on one laptop meant they fought over the GPU and the game's save folder. A lock file around benchmarks and tests fixed that. The game is free, with an optional tip. Feedback is very welcome, and I'm happy to answer questions about the workflow.
