---
id: "d6421e349b9bb9a2"
title: "ChatGPT for SNES"
url: "https://bxfoundry.com/chatgpt_snes"
link: "https://bxfoundry.com/chatgpt_snes"
source: "bxfoundry.com"
domain: "bxfoundry.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-20T00:25:59Z"
published_date: "2026-11-20"
collected_at: "2026-11-20T13:03:52Z"
authors: ["evan_"]
language: "en"
summary: "Download the v0.7 ROM (1.5 MB zip: one .sfc file). Requires a flash cart with Super FX support, such as an FXPak Pro or an sd2snes with current firmware. Leave Chip Options › SuperFX speed at Normal. The build with the fact book (17 MB zip: the .sfc and its .msu file) also needs MSU-1 support: put both files in the same folder with their names unchanged.\n- ChatGPT for SNES is an unofficial…"
tags: []
orgs: ["OpenAI"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 321
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50568548"
score: 103
comments: 27
community: "Hacker News"
---

# ChatGPT for SNES

bxfoundry.com · evan_ · 2026-11-20

Download the v0.7 ROM (1.5 MB zip: one .sfc file). Requires a flash cart with Super FX support, such as an FXPak Pro or an sd2snes with current firmware. Leave Chip Options › SuperFX speed at Normal. The build with the fact book (17 MB zip: the .sfc and its .msu file) also needs MSU-1 support: put both files in the same folder with their names unchanged.
- ChatGPT for SNES is an unofficial experiment designed by Benj Edwards and coded by AI agents: a ChatGPT-style chat program for the Super Nintendo. Its training conversations were written by gpt-oss-120b, OpenAI's open-weight model. Not made or endorsed by OpenAI.
- This is version 0.7 (2 November 2026).
- A small language model with about 2.2 million parameters runs on the cartridge's Super FX 2 chip and writes its answers one word at a time.
- In the main build every word it writes comes from the language model. A second build adds a fact book (the opening sentences of 150,000 Simple English Wikipedia articles, stored in the cartridge's MSU-1 data file): like ChatGPT searching the web, its model can decide to look something up and print what the book says.
- Here it runs in the Snes9x emulator in your browser; the first visit loads about 4 MB (19 MB with the fact book).
- Press Start (Enter) on the title screen, then type on your keyboard and press Enter to send. Each letter takes a moment to appear, because the page moves the cursor on the game's own on-screen keyboard.
- It is not a useful assistant: the model is millions of times smaller than the models behind ChatGPT, knows about 8,000 words, and often gets things wrong, sometimes confidently. The fact book can carry mistakes too.
On a real Super NES
If you liked this, you might enjoy Séance, which runs a tiny AI language model on a real NES.
