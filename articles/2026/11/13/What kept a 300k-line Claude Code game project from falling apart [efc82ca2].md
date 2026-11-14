---
id: "efc82ca2011bead7"
title: "What kept a 300k-line Claude Code game project from falling apart"
url: "https://reddit.com/r/ClaudeAI/comments/1xv9g4y/what_kept_a_300kline_claude_code_game_project"
link: "https://reddit.com/r/ClaudeAI/comments/1xv9g4y/what_kept_a_300kline_claude_code_game_project"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T14:33:45Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Tommyruin"]
language: "en"
summary: "The game is now about 172k lines of code and 135k lines of tests, and 943 of its 1,644 commits carry a Claude co-author line. Aita: The Dark Domain , is a roguelite played with a normal deck of playing cards in the Etruscan underworld. Every card you attack with is a card you no longer have when the enemy hits back. Solo or online co-op for 1–4 players. Out 1 December on Steam, Google Play and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["products & launches"]
content_source: "post"
word_count: 428
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xv9g4y/what_kept_a_300kline_claude_code_game_project/"
score: null
comments: null
community: "r/ClaudeAI"
---

# What kept a 300k-line Claude Code game project from falling apart

Reddit · Tommyruin · 2026-11-13

The game is now about 172k lines of code and 135k lines of tests, and 943 of its 1,644 commits carry a Claude co-author line. Aita: The Dark Domain , is a roguelite played with a normal deck of playing cards in the Etruscan underworld. Every card you attack with is a card you no longer have when the enemy hits back. Solo or online co-op for 1–4 players. Out 1 December on Steam, Google Play and the App Store for £1.99 / $1.99, with a free demo on Steam now . Here's what I found made it work: - One rules engine. Every card, Blessing and boss rule lives in one shared core that solo, co-op, the game server and the test player all run. A rule written anywhere else counts as a bug, and parity tests check that solo, co-op and the server reach the same result. - A good .md file that every session reads first (naming, architecture, what "done" means), plus handoff notes so the next session starts where the last one ended. - Gates before every push: lint, tests, a build, a docs check and a translation check. The game is in 14 languages, and the check fails if one is out of date. - The headless AI player as previously mentioned. Building this was huge, and i'm consistently iterating on it to ensure a good power curve and difficulty level Early on, rules lived inside the each mode separately, so solo and co-op could drift apart. In Feb I pulled every rule into one shared core (or at least thought so, I kept finding small bits that lived outside the core until October!). Additionally, the games were built two different ways until I moved every one of them onto a single pixel canvas in October - this was a huge visual upgrade. I feel like with a coding background, these mistakes would have been removed from the word go, but unfortunately it was a lesson I had to learn along the way. At least I wont make it in my next projects!! Numbers: 1,644 commits since 5 January, 943 with a Claude co-author line (57%), about 172k lines of game code (not counting my marketing tools) and 135k lines of tests. I switched around based on what was flavour of the month subscription wise, and I got married in June, hence the slow down! I'm sure a few hundred more to go before the 1st December! Please Try the demo here and give it a Wishlist!!! Happy to answer any questions! :)
