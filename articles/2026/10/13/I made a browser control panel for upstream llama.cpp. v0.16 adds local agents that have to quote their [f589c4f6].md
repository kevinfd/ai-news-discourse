---
id: "f589c4f61fee7636"
title: "I made a browser control panel for upstream llama.cpp. v0.16 adds local agents that have to quote their sources, and code checks the quotes"
url: "https://reddit.com/r/ArtificialInteligence/comments/1x55mh1/i_made_a_browser_control_panel_for_upstream"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T19:05:43Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Sleepybear2611"]
language: "en"
summary: "I built LlamaForge, a free, MIT-licensed browser control panel for llama.cpp. It isn't a fork: it drives the real upstream llama-server, so when llama.cpp adds a model you update from the panel and have it that day. Almost all of the code was written by Claude Code (Opus) while I made the decisions and tested on my own hardware. What it does - Before you load a model it shows, to scale, where it…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic", "Nvidia"]
topics: ["chips & infrastructure", "models & research", "products & launches", "agents & coding"]
content_source: "post"
word_count: 509
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1x55mh1/i_made_a_browser_control_panel_for_upstream/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# I made a browser control panel for upstream llama.cpp. v0.16 adds local agents that have to quote their sources, and code checks the quotes

Reddit · Sleepybear2611 · 2026-10-13

I built LlamaForge, a free, MIT-licensed browser control panel for llama.cpp. It isn't a fork: it drives the real upstream llama-server, so when llama.cpp adds a model you update from the panel and have it that day. Almost all of the code was written by Claude Code (Opus) while I made the decisions and tested on my own hardware. What it does - Before you load a model it shows, to scale, where it will land on each GPU using sizes measured on your machine, and tells you if it won't fit. - Runs several models at once. The main one goes on the fastest GPU that fits. - v0.16 adds Embers: small local agents that read sources you point them at overnight and write you a brief. Every claim has to quote its source word for word, and plain code (not the model) checks the quote against the saved snapshot. If the quote isn't there, the claim is dropped. - Also a Voice tab. The voiceover in the video is Qwen3-TTS running locally. How Claude was used - Plan, then subagents. For bigger features I have Claude write a spec, then a task-by-task plan. Then it runs each task with a fresh subagent, followed by a spec-compliance review and a separate code-quality review. Reviews catch real stuff: on the last feature the final review found several bugs that had to be fixed before merge. - Probe before building. When a feature depends on llama.cpp behaving a certain way, Claude writes a small throwaway script against a sandbox server first to check that it really does. That happened with keeping a conversation's cache across a reload with a different GPU layer count. Building on an untested assumption is where most of the wasted time used to go. - Tests first for backend logic. The backend is Python stdlib only, the frontend vanilla JS, no build step. That's a constraint I gave Claude on purpose, so the codebase stays small enough for it (and me) to reason about. - A CLAUDE.md of past mistakes. Every time something bit us, it went into the file so the next session doesn't repeat it. One example: a shallow copy of the config defaults leaked changes process-wide. Another: the browser pane silently answers "cancel" to confirm() , so the panel now uses its own dialogs and a test fails if anyone adds a native one back. - Where it went wrong: Claude once spent an hour chasing a "bug" that was really its own test script feeding the model a fake earlier answer. Lesson: make it verify the test harness before the code. - What I do myself: pick what to build, run it on real GPUs, and say no a lot. Try it (free, MIT) irm https://raw.githubusercontent.com/dadwritestech/llamaforge/master/install.ps1 | iex # windows curl -fsSL https://raw.githubusercontent.com/dadwritestech/llamaforge/master/install.sh | sh # linux / macos My box is Windows + NVIDIA (5080 + 5060 Ti on a PCIe x4 slot). Linux and macOS pass CI but have had little real-hardware use, so bug reports are very welcome. https://github.com/dadwritestech/llamaforge
