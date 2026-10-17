---
id: "13231fcaa0ba5483"
title: "This is 61 KB HTML file 🤯"
url: "https://reddit.com/r/ClaudeAI/comments/1x7v7gj/this_is_61_kb_html_file"
link: "https://reddit.com/r/ClaudeAI/comments/1x7v7gj/this_is_61_kb_html_file"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T23:24:42Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Any-Reputation8118"]
language: "en"
summary: "I built a real-time ocean simulation with Claude Code (Opus 5.5) What it is: a single 61 KB HTML file that renders a sunset ocean in your browser with WebGPU. It has an FFT wave simulation, whitecaps, a physically based sky with clouds, and sun glitter. You fly around with WASD and the mouse. How I used Claude Code: I gave it one prompt: make the most realistic water scene it could, in WebGPU,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 188
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7v7gj/this_is_61_kb_html_file/"
score: null
comments: null
community: "r/ClaudeAI"
---

# This is 61 KB HTML file 🤯

Reddit · Any-Reputation8118 · 2026-10-16

I built a real-time ocean simulation with Claude Code (Opus 5.5) What it is: a single 61 KB HTML file that renders a sunset ocean in your browser with WebGPU. It has an FFT wave simulation, whitecaps, a physically based sky with clouds, and sun glitter. You fly around with WASD and the mouse. How I used Claude Code: I gave it one prompt: make the most realistic water scene it could, in WebGPU, with a floating camera. It wrote the renderer from scratch with no engine or libraries. It took screenshots of its own output and had separate subagents critique the screenshots, so it wasn't judging its own work. The whole thing took about 30 minutes. Free to try: ocean-noniv.vercel.app , preferably in Chrome. It needs a WebGPU-capable GPU, and on laptops you have to force Chrome onto the dedicated GPU. Otherwise the performance might be bad or it might not run at all. On RTX 5070 Ti I get ~260 FPS at 2560×1440 resolution. Click the canvas to look around, WASD to move, H for a settings panel. Repo with unminified and more organised version: github.com/Noniv/web-ocean
