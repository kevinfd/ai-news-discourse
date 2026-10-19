---
id: "793a84a2fbd588c0"
title: "I built a free Pixel Art converter that also works on mobile (Open Source)"
url: "https://reddit.com/r/ClaudeAI/comments/1x93r3x/i_built_a_free_pixel_art_converter_that_also"
link: "https://reddit.com/r/ClaudeAI/comments/1x93r3x/i_built_a_free_pixel_art_converter_that_also"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T13:52:08Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Rafilondon"]
language: "en"
summary: "I needed pixel art for another project and built this with Claude Code. After a load-bearing amount of testing, I’m quite happy with it, so why not share it? It runs on device in your browser (desktop, mobile) and supports custom presets. Use it: https://pixelpass.iromoto.dev Free and open source . https://github.com/iromoto-dev/pixelpass Pixel Pass turns a painting or a photo into pixel art: a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["jobs & society", "models & research"]
content_source: "post"
word_count: 208
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x93r3x/i_built_a_free_pixel_art_converter_that_also/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a free Pixel Art converter that also works on mobile (Open Source)

Reddit · Rafilondon · 2026-10-18

I needed pixel art for another project and built this with Claude Code. After a load-bearing amount of testing, I’m quite happy with it, so why not share it? It runs on device in your browser (desktop, mobile) and supports custom presets. Use it: https://pixelpass.iromoto.dev Free and open source . https://github.com/iromoto-dev/pixelpass Pixel Pass turns a painting or a photo into pixel art: a real low-res grid, a small palette (picked from your picture, or PICO-8, Game Boy and others), dither only where the picture is smooth. How Claude Code helped: It started as a Python script in my game’s art pipeline that Claude Code wrote with me. For this, it ported that to a single HTML file in plain JavaScript and checked in Node that both versions gave pixel-identical results. Most of the work was back and forth: I tested and described what looked wrong (dark portraits lost their colours, faces in shadow went flat, the pixel art once showed on both sides of the slider), and Claude Code found the cause and fixed it. It also tested the page itself, in its own browser and on my Android emulator for phone and tablet, and made the preview image with a script that runs the same pixel engine.
