---
id: "c8b22a872311479d"
title: "I built a cozy puzzle game with Claude Code, and a solver that makes every level fair (free, open source)"
url: "https://reddit.com/r/ClaudeAI/comments/1x9r4kc/i_built_a_cozy_puzzle_game_with_claude_code_and_a"
link: "https://reddit.com/r/ClaudeAI/comments/1x9r4kc/i_built_a_cozy_puzzle_game_with_claude_code_and_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T08:16:43Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["betta_fan"]
language: "en"
summary: "Free to play, no account needed: https://klarbase.dev https://reddit.com/link/1x9r4kc/video/0oay9s4wudwh1/player I built Klarbase, a small browser puzzle game: you guide a little sprout called Pip across floating isles, one move per key. Push crates into water to make a path, slide on ice, pull levers that flip bridges, step through arches that teleport you. 24 levels across 5 themes, plus a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["jobs & society", "models & research"]
content_source: "post"
word_count: 374
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9r4kc/i_built_a_cozy_puzzle_game_with_claude_code_and_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a cozy puzzle game with Claude Code, and a solver that makes every level fair (free, open source)

Reddit · betta_fan · 2026-10-19

Free to play, no account needed: https://klarbase.dev https://reddit.com/link/1x9r4kc/video/0oay9s4wudwh1/player I built Klarbase, a small browser puzzle game: you guide a little sprout called Pip across floating isles, one move per key. Push crates into water to make a path, slide on ice, pull levers that flip bridges, step through arches that teleport you. 24 levels across 5 themes, plus a builder to make your own. Code (MIT): https://github.com/TanmoyP/klarbase How Claude Code helped Almost all of the code was written by Claude Code (Opus). My job was direction, decisions and playtesting. The parts that taught me the most: It talked me out of my first design. v1 was a camera-angle illusion puzzle and it felt wonky. When I asked for a revamp, Claude argued the illusion itself was the cause and proposed turn-based grid puzzles instead. That was the right call. Levels are designed with a solver in the loop. Claude wrote the rules engine plus a breadth-first solver, then designed the 24 levels against it. If a level had no solution, or a shortcut skipped the mechanic it was meant to teach, the solver caught it and Claude redesigned it. Every level's "par" is the true shortest solution, and the game can replay it. One source of truth. The rules live in one small dependency-free package that the game, the builder, the solver, the server and CI all import, so they can't disagree about whether a level works. Open-source contributions that are safe to accept. Anyone can add a level by PR. CI checks it's solvable, the par is honest, it's not a copy, and the author only touched their own folder. It never runs contributor code, and Claude simulated 11 hostile PRs to test that. No art files. Islands, the character, clouds and sound are all generated in code (three.js + Web Audio), so a level is a few KB of text. What didn't work first time: early levels it designed by eye were often trivial or unsolvable until the solver became the judge. Claude is a lot better at "write a checker, then design against it" than at designing blind. Feedback welcome Which level got you stuck in a bad way? Does the builder make sense without instructions? Anything broken on your phone?
