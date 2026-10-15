---
id: "4b65e97be1cb3023"
title: "I built a daily pixel-creature game with Claude Code. Here's how the work was split, now that ~20 people play it daily"
url: "https://reddit.com/r/ClaudeAI/comments/1x5q63z/i_built_a_daily_pixelcreature_game_with_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T12:40:46Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["KurusuDesu"]
language: "en"
summary: "What I built: Blobvarium, a free browser game. One pixel creature is born each day, drawn entirely by code from a seed. You bid for one of its 24 copies with free in-game coins and it lives in your nursery, sings, and farms or explores in a small town!!!. How Claude Code helped: • The creature generator: Claude Code wrote the Python that turns a seed into a genome (body, limbs, horns, an Inca…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Meta"]
topics: ["models & research", "jobs & society"]
content_source: "post"
word_count: 278
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x5q63z/i_built_a_daily_pixelcreature_game_with_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a daily pixel-creature game with Claude Code. Here's how the work was split, now that ~20 people play it daily

Reddit · KurusuDesu · 2026-10-14

What I built: Blobvarium, a free browser game. One pixel creature is born each day, drawn entirely by code from a seed. You bid for one of its 24 copies with free in-game coins and it lives in your nursery, sings, and farms or explores in a small town!!!. How Claude Code helped: • The creature generator: Claude Code wrote the Python that turns a seed into a genome (body, limbs, horns, an Inca motif) and renders it as distance-field shapes into 96px pixel art, plus its hatch, walk and idle animations. No image model. • The game: a Next.js front end and a Supabase back end. Every rule about coins and bids lives in Postgres functions, with SQL tests that run on PGlite (138 of them) and 216 web tests. • The workflow: three slash commands. One session works through a task board in a loop, one commit per task. Another closes it (runs the checks, writes a report, pushes). A third Claude reviews it and sends back what isn't right. When something is unclear it writes the question down with the option it chose and keeps going, so I answer later. About 540 commits since mid-September. • This week: it found that Google blocks sign-in inside app browsers (X, LINE, Instagram), so it added sign-in by email code and a no-account look-around mode. It also rendered the attached trailer frame by frame from the game's own drawing code. Free to try: https://blobvarium.com . Open it in a browser and tap "Look around without an account", or sign in with Google or an email code. About 20 people now come back every day, which I'm happy about.😊
