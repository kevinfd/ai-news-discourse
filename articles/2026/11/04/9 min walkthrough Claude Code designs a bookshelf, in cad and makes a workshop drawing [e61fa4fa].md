---
id: "e61fa4fa101b3dd4"
title: "9 min walkthrough: Claude Code designs a bookshelf, in cad and makes a workshop drawing"
url: "https://reddit.com/r/ClaudeAI/comments/1xnmfn9/9_min_walkthrough_claude_code_designs_a_bookshelf"
link: "https://reddit.com/r/ClaudeAI/comments/1xnmfn9/9_min_walkthrough_claude_code_designs_a_bookshelf"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T12:01:17Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Lazar988"]
language: "en"
summary: "A few weeks ago I posted SOMA here, the app where Claude Code does the CAD. SOMA now has over 1000 downloads, which is way more than I ever hoped for :) People asked how it actually works in practice, so I made a proper tutorial. It's one project start to finish: one prompt for a bookshelf, then changes by drawing on the 3D view, parameters, a FEM check how much a shelf holds, a technical…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 312
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xnmfn9/9_min_walkthrough_claude_code_designs_a_bookshelf/"
score: null
comments: null
community: "r/ClaudeAI"
---

# 9 min walkthrough: Claude Code designs a bookshelf, in cad and makes a workshop drawing

Reddit · Lazar988 · 2026-11-04

A few weeks ago I posted SOMA here, the app where Claude Code does the CAD. SOMA now has over 1000 downloads, which is way more than I ever hoped for :) People asked how it actually works in practice, so I made a proper tutorial. It's one project start to finish: one prompt for a bookshelf, then changes by drawing on the 3D view, parameters, a FEM check how much a shelf holds, a technical drawing, and a phone stand with the 3D printing skill. Some parts are sped up, the drawing took Claude about 6 minutes. The thing that makes it work is that Claude checks its own work. It builds the model, measures and renders pictures it looks at before it tells you it's done. Skills can be off, on demand or always on, so it only reads the rules it needs. How I built it with Claude Most of SOMA was written by Claude Code (Opus 5.5), with me deciding what to build, reviewing and testing. It's an Electron app in TypeScript plus a Python library and CLI on top of CadQuery. What worked for me: a CLAUDE.md with the project rules, code principles and a decision log, so Claude knows why things are the way they are across sessions. The test suites start the real app and drive it, and Claude takes screenshots of the UI and looks at them after every change, the same way it checks its own CAD models in SOMA. I review the screenshots and the diffs and tell it what to fix. Even this tutorial was made with Claude Code: it scripted the app to record each scene, wrote the voice over (local AI voice) and cut the video. To try it: download it for Windows, macOS or Linux from https://somacad.app and use your own Claude Code subscription, no extra API key.
