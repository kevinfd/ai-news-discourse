---
id: "e49f718bce7009f7"
title: "I built a game engine where Claude is a first-class user. Here it is building an environment from scratch"
url: "https://reddit.com/r/ClaudeAI/comments/1xdkutx/i_built_a_game_engine_where_claude_is_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xdkutx/i_built_a_game_engine_where_claude_is_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T17:45:37Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["nayti53"]
language: "en"
summary: "I built Apeiron, a game engine and editor designed from the start to be used by AI agents as well as people. The video shows the in-engine agent, running on Claude, building a small game environment: procedural world generation, texture and material graphs, AI-generated meshes, lighting and scene setup. What it does: one editor for worlds, modeling, textures, materials, animation, VFX and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 202
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdkutx/i_built_a_game_engine_where_claude_is_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a game engine where Claude is a first-class user. Here it is building an environment from scratch

Reddit · nayti53 · 2026-10-23

I built Apeiron, a game engine and editor designed from the start to be used by AI agents as well as people. The video shows the in-engine agent, running on Claude, building a small game environment: procedural world generation, texture and material graphs, AI-generated meshes, lighting and scene setup. What it does: one editor for worlds, modeling, textures, materials, animation, VFX and gameplay. It runs natively and in the browser. The agent uses the same commands a human does, so everything it builds shows up in the undo history and in graphs you can open and edit. How Claude Code helped: Claude Code wrote most of the code over the past five months, across rendering, physics, procedural graphs, the editor and the agent itself. I focused on architecture, review and product decisions. How Claude is used inside it: the built-in agent runs on Claude and can build scenes, materials, worlds and gameplay from a prompt. The engine is also an MCP server, so Claude Code or any MCP client can drive the editor directly. Free to try (early version): https://engine.apeironengine.com in Chrome or Edge (needs WebGPU). No install. Expect rough edges and missing features. Feedback is very welcome. Happy to answer questions.
