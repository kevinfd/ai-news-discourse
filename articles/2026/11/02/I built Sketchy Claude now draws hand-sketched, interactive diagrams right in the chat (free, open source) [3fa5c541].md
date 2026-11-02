---
id: "3fa5c541e54b0b7e"
title: "I built Sketchy: Claude now draws hand-sketched, interactive diagrams right in the chat (free, open source)"
url: "https://reddit.com/r/ClaudeAI/comments/1xlrc5h/i_built_sketchy_claude_now_draws_handsketched"
link: "https://reddit.com/r/ClaudeAI/comments/1xlrc5h/i_built_sketchy_claude_now_draws_handsketched"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T07:59:00Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Nkgsporty"]
language: "en"
summary: "github.com/ddkbs/sketchy Sketchy is a free open source tool which lets claude draw & explain directly in the chat. The drawing is in a hand-drawn style with hover details and a step by step mode. Claude only says what’s in the drawing (boxes, arrows, groups). The positions come from a layout engine, so it doesn’t end up with the overlapping boxes you usually get when an LLM writes SVG. It works…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 239
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlrc5h/i_built_sketchy_claude_now_draws_handsketched/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built Sketchy: Claude now draws hand-sketched, interactive diagrams right in the chat (free, open source)

Reddit · Nkgsporty · 2026-11-02

github.com/ddkbs/sketchy Sketchy is a free open source tool which lets claude draw & explain directly in the chat. The drawing is in a hand-drawn style with hover details and a step by step mode. Claude only says what’s in the drawing (boxes, arrows, groups). The positions come from a layout engine, so it doesn’t end up with the overlapping boxes you usually get when an LLM writes SVG. It works in the normal chat as a skill (upload a zip, done) and in Claude Code as an MCP extension. The extension can also label real photos with a small local vision model and draw e.g. Arduino wiring. How I built it with Claude: I built Sketchy almost entirely with Claude Code. I planned the architecture with it first (scene JSON → layout engine → hand-drawn renderer), then built it piece by piece. After each step I had Claude explain what it did so I actually understood the code instead of just copying it. Claude Code wrote most of the layout and rendering code, the MCP server and the packaging as a .mcpb extension. The hardest part was getting LLM-generated diagrams to look clean, so I had Claude describe only what to draw and let the layout engine handle positions. I tested that by having Claude draw lots of different diagrams and fixing whatever broke. It’s completely free and open source: download the skill zip or the .mcpb from GitHub
