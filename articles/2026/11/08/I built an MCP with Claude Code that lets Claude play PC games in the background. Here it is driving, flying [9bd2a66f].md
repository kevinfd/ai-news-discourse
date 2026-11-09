---
id: "9bd2a66f18f96b18"
title: "I built an MCP with Claude Code that lets Claude play PC games in the background. Here it is driving, flying a heli and walking in GTA on its own"
url: "https://reddit.com/r/ClaudeAI/comments/1xr3gbs/i_built_an_mcp_with_claude_code_that_lets_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xr3gbs/i_built_an_mcp_with_claude_code_that_lets_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T17:11:53Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Wonderful-Ad-8579"]
language: "en"
summary: "I wanted AI agents to create, test, and improve my game mods autonomously by actually playing the games, without taking over my PC while they do it. So I built an MCP server with Claude Code. It gives Claude its own keyboard, mouse, gamepad and screen capture inside a single game. The game runs in the background so I can keep using my PC uninterrupted, and several games can run at once with one…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 436
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xr3gbs/i_built_an_mcp_with_claude_code_that_lets_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an MCP with Claude Code that lets Claude play PC games in the background. Here it is driving, flying a heli and walking in GTA on its own

Reddit · Wonderful-Ad-8579 · 2026-11-08

I wanted AI agents to create, test, and improve my game mods autonomously by actually playing the games, without taking over my PC while they do it. So I built an MCP server with Claude Code. It gives Claude its own keyboard, mouse, gamepad and screen capture inside a single game. The game runs in the background so I can keep using my PC uninterrupted, and several games can run at once with one agent each. In the video Claude is driving to a map waypoint in GTA IV, flying a helicopter to a waypoint and landing it in GTA V, and walking to a marker in GTA IV. All of it is real time and unedited. After that it makes the choices in a Detroit: Become Human scene, and plays TABS, Halo Wars 2, Phantom Rose and Cities: Skylines. How Claude helped, since that's the interesting part: Claude Code set up the project, planned it and wrote most of the code: a DLL that runs inside the game for input and capture, and a TypeScript MCP server on top of it with about 100 tools. The development itself is done by Claude agents. Each agent gets one game as a test bed and one problem to solve, like "the car keeps stalling on this junction". It plays the game through the MCP, finds what the tools get wrong, fixes the code, and measures before and after on the same route. Then Claude Code reviews the change and runs the tests before it goes public. Each game is a small profile: where the minimap is, how the camera turns, what the waypoint looks like. So supporting a new game is mostly data, not code. Claude agents write most of those profiles while they play. Codex helped with some of the code too. What it can't do yet: indoors with no minimap it still struggles. In Morrowind it took a while to find the right door. Aiming in shooters is early. Full playthroughs are the goal but we're not there yet. It's free and open source (MIT) and works with any MCP client. It's Windows only for now, because the part that runs in the game is a Windows DLL. Single-player and offline games only: it won't run in games with anti-cheat. https://github.com/CorruptedAng3l/llm-game-automation-mcp Edit: GitHub's automated system suspended my account after this post blew up (no email or warning), so the GitHub link is down for now. Support ticket is in and nothing's deleted. Same repo and release on GitLab: https://gitlab.com/corruptedang3l-group/llm-game-automation-mcp Happy to answer questions, and tell me what game you'd want to see it try next.
