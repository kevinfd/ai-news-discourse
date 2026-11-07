---
id: "aa836517ab14e86f"
title: "Claude Code driving a robot arm I built over MCP"
url: "https://youtu.be/kQVQd28h4DM?feature=shared"
link: "https://youtu.be/kQVQd28h4DM?feature=shared"
source: "Youtu"
domain: "youtu.be"
source_type: "community"
collector: "reddit"
date: "2026-11-07T10:39:11Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["funpicoprojects1"]
language: "en"
summary: "I attached a LeRobot arm on an RC car, runs on a single Raspberry Pi Pico W / Pico 2 W. The board has its own MCP server so Claude Code talks to it directly. All I typed was \"pick up object on your left, throw it to your right and say bye bye\". Claude did the rest: picks up a fluffy toy, throws it, does a 360, says bye, goes to sleep. How it works: - Added the board as an MCP server in Claude…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "summary"
word_count: 120
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xq3fsf/claude_code_driving_a_robot_arm_i_built_over_mcp/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code driving a robot arm I built over MCP

Youtu · funpicoprojects1 · 2026-11-07

I attached a LeRobot arm on an RC car, runs on a single Raspberry Pi Pico W / Pico 2 W. The board has its own MCP server so Claude Code talks to it directly. All I typed was "pick up object on your left, throw it to your right and say bye bye". Claude did the rest: picks up a fluffy toy, throws it, does a 360, says bye, goes to sleep. How it works: - Added the board as an MCP server in Claude Code - Board commands (move, drive, poses, status, stop...) are exposed as MCP tools, Claude figures out the sequence based on calibration data - The firmware also has a CLAUDE.md + skills so Claude…
