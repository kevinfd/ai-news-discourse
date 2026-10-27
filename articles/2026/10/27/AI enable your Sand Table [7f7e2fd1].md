---
id: "7f7e2fd136f33677"
title: "AI enable your Sand Table"
url: "https://reddit.com/r/ClaudeAI/comments/1xghtnl/ai_enable_your_sand_table"
link: "https://reddit.com/r/ClaudeAI/comments/1xghtnl/ai_enable_your_sand_table"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T03:22:34Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Jlannin"]
language: "en"
summary: "I can now say \"Claude, draw today's weather\" and a steel ball starts carving it into my HoMedics Drift sand table from my Claude desktop app. \"Turn this photo of the dog into a sand portrait.\" \"Redraw that fractal I like.\" Claude plans the path, checks it, and sends it to the table, and then you get to sit there and watch it happen. It's called Drifted . I built it in a day for my Drift (the 16\"…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 408
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xghtnl/ai_enable_your_sand_table/"
score: null
comments: null
community: "r/ClaudeAI"
---

# AI enable your Sand Table

Reddit · Jlannin · 2026-10-27

I can now say "Claude, draw today's weather" and a steel ball starts carving it into my HoMedics Drift sand table from my Claude desktop app. "Turn this photo of the dog into a sand portrait." "Redraw that fractal I like." Claude plans the path, checks it, and sends it to the table, and then you get to sit there and watch it happen. It's called Drifted . I built it in a day for my Drift (the 16" Bluetooth one). Free, open source, runs on a Mac or can be ported to any OS. Far more than what I could do with the out of the box app, which was running pre-built patterns. The digital twin Sand carries memory - the ball never lifts, so every move gets drawn , even the jumps between shapes. Grooves are as wide as the ball, so fine detail turns to mush. And a drawing takes 15–20 minutes, so you find out it's wrong a long time after you hit go. So there's a simulation of the table that comes with this. Claude previews every drawing in it first, sees the stray lines and mushy bits, fixes them, and only then sends it to the real thing. It takes seconds instead of twenty minutes, tells you how long the real drawing will take, and can animate the ball drawing it. I built the twin with a webcam pointed at the table. Draw something, photograph it, compare with what the sim predicted, fix the sim, repeat. Claude ran most of that loop itself: drawing test patterns, tracking the ball in the video, scoring each guess against the photo, tuning how far the ball shoves sand and what angle the piles settle at. The GIF and pics 3 and 4 are sim vs real. Real sand makes crisper ridges than the sim does, but it's close enough to catch the stuff that matters. You don't need a camera to use it. Want to build your own thing instead? There's a local API, a Swift library for Mac and iOS apps, and the Bluetooth protocol is documented, so you can write a client in whatever you like. The ideas carry over to other ball-and-magnet tables too. So far it's drawn fractals, a weather display, a clock, and portraits of people and our dog. Unofficial, not affiliated with HoMedics, and if you don't have a Drift, go get one. Free and MIT licensed. 👉 https://github.com/joshlannin/drifted
