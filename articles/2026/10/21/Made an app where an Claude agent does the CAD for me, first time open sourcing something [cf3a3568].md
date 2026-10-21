---
id: "cf3a3568ab759416"
title: "Made an app where an Claude agent does the CAD for me, first time open sourcing something"
url: "https://reddit.com/r/ClaudeAI/comments/1xbke4m/made_an_app_where_an_claude_agent_does_the_cad"
link: "https://reddit.com/r/ClaudeAI/comments/1xbke4m/made_an_app_where_an_claude_agent_does_the_cad"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T11:17:29Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Lazar988"]
language: "en"
summary: "Been using Claude Code for a while and at some point I wondered if it could do my CAD too. Turns out yes, way better than I expected. So I built an app around it, it's called SOMA and it's open source. The idea: Claude Code writes the model as Python code with CadQuery, SOMA builds it on every save and shows it in 3D. Claude runs in a normal terminal inside the app, so it's your own Claude Code…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "post"
word_count: 318
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbke4m/made_an_app_where_an_claude_agent_does_the_cad/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Made an app where an Claude agent does the CAD for me, first time open sourcing something

Reddit · Lazar988 · 2026-10-21

Been using Claude Code for a while and at some point I wondered if it could do my CAD too. Turns out yes, way better than I expected. So I built an app around it, it's called SOMA and it's open source. The idea: Claude Code writes the model as Python code with CadQuery, SOMA builds it on every save and shows it in 3D. Claude runs in a normal terminal inside the app, so it's your own Claude Code with your own subscription and settings. No wrapper, no extra API key. Works with Codex, OpenCode and Gemini CLI too. What makes it work well is that Claude can check its own results. SOMA gives it a CLI, so it can build the model, measure distances, check for collisions, run FEM and render images to actually look at what it made. There's an AGENTS.md with the project rules and skills for 3D printing, CNC, sheet metal etc that you can switch on per model. From your side you can click on a part or just draw on the 3D view and send that to Claude as a screenshot, like "this hole is too small" with a circle around it. Every step Claude makes is saved in a history, so if it messes something up you just go back. You can do pretty complex stuff with it. Assemblies with a lot of parts, start from a hand drawn sketch, or load an existing STEP file and build around it. The CNC mill in the video has 118 parts. Funny side note, most of SOMA itself was also written with Claude Code. Free, GPL, builds for Windows, Mac and Linux. I mainly tested on Windows, so Mac and Linux feedback would be great. Website: SOMA – Open-source AI CAD for Claude Code, Codex and CadQuery GitHub: https://github.com/Kai-Jungsthoefel/SOMA Curious how it works with your setups and what you end up building.
