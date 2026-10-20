---
id: "d01f8527ed4e777c"
title: "Spent 4 months building a multiplayer bird game and Claude Playtest Bots 🦚"
url: "https://reddit.com/r/ClaudeAI/comments/1xa4jp8/spent_4_months_building_a_multiplayer_bird_game"
link: "https://reddit.com/r/ClaudeAI/comments/1xa4jp8/spent_4_months_building_a_multiplayer_bird_game"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T18:18:00Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["monkeydance26"]
language: "en"
summary: "I built a small multiplayer game to replace a traditional CV on my website. You play together as up to four birds and explore a world inspired by Diablo 2 - it doesn't at first look like it but wait and see 🤣. I’m a game designer by trade and it started from an older game I never finished; I picked it up again and built my own engine on three.js so it runs straight in the browser. The part that…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 256
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xa4jp8/spent_4_months_building_a_multiplayer_bird_game/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Spent 4 months building a multiplayer bird game and Claude Playtest Bots 🦚

Reddit · monkeydance26 · 2026-10-19

I built a small multiplayer game to replace a traditional CV on my website. You play together as up to four birds and explore a world inspired by Diablo 2 - it doesn't at first look like it but wait and see 🤣. I’m a game designer by trade and it started from an older game I never finished; I picked it up again and built my own engine on three.js so it runs straight in the browser. The part that blew my mind was building a playtesting agent for the game that connects to my Claude Code subscription. I got the idea from rmalde/minecraft-agent on GitHub: a smart (Opus) model plans, a small fast classifier (Jev) picks the moves. Claude looks at a screenshot about every second and sets a goal with a few steps. jev (a decision model on OpenRouter) never sees the screen but just gets options in words like “walk to the silver feather 6m west, path clear” and picks one about 3 times a second, and an emulator presses the actual keys. You can run with 4 birds at the same time, and the AI's have different personalities: impatient, competitive, explorative, etc. It actually found bugs for me, like getting stuck in walls, or being annoyed they can't reach something easily. I can gladly share more about this :-) Still a work in progress. Would love to hear where you get stuck or what feels off. If you want to try it out: www.georgluif.at (it plays directly in your web browser)
