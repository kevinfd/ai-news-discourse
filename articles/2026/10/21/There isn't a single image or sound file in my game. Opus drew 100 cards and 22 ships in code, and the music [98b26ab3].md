---
id: "98b26ab3d79d72a7"
title: "There isn't a single image or sound file in my game. Opus drew 100 cards and 22 ships in code, and the music is composed live by your flight"
url: "https://reddit.com/r/ClaudeAI/comments/1xbirxe/there_isnt_a_single_image_or_sound_file_in_my"
link: "https://reddit.com/r/ClaudeAI/comments/1xbirxe/there_isnt_a_single_image_or_sound_file_in_my"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T09:45:41Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["jaboos91"]
language: "en"
summary: "Star Hop is a one-tap space game: your ship orbits a planet, you tap to launch and try to land in the next planet's orbit. Free in the browser, no sign-up: https://www.star-hop.app/?utm_source=reddit&utm_medium=post&utm_campaign=claudeai-code There isn't a single image or sound file in it. Every picture and every sound is code Claude wrote: 100 collectible pilot cards. Opus first wrote a small…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 339
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbirxe/there_isnt_a_single_image_or_sound_file_in_my/"
score: null
comments: null
community: "r/ClaudeAI"
---

# There isn't a single image or sound file in my game. Opus drew 100 cards and 22 ships in code, and the music is composed live by your flight

Reddit · jaboos91 · 2026-10-21

Star Hop is a one-tap space game: your ship orbits a planet, you tap to launch and try to land in the next planet's orbit. Free in the browser, no sign-up: https://www.star-hop.app/?utm_source=reddit&utm_medium=post&utm_campaign=claudeai-code There isn't a single image or sound file in it. Every picture and every sound is code Claude wrote: 100 collectible pilot cards. Opus first wrote a small SVG kit (stars, skies, planets, ships, engine trails, sparks), then composed each card from three parallax layers plus a hero that breaks out over the frame. All 100 are 152 kB of code. 22 ships drawn with canvas paths, and 19 paint jobs that recolour them. Two generative music scores, synthesized live in the browser. In the upbeat one your combo adds layers (kick, bass, claps, arpeggio, then the lead), hyperdrive brings in the full arrangement, a crash muffles the music and the band drops out for two bars, and the tempo climbs with each sector. The whole game is about 0.5 MB gzipped, plus fonts. The prompt behind the music (I wrote it in Czech, this is a translation): I'm wondering if we should improve the music in the game. Make it more dynamic, more fun, right now it's pretty gloomy. We could put a switch in settings between the original and something upbeat. I'm imagining something like Beat Saber: the music reacts to the game, speeding up, bonuses, crashes. Get what I mean? What options do we have to make it? Maybe ElevenLabs? Claude laid out the options, I said "let's just do it in code", and half an hour later it was in production. What didn't work at first: the cards used SVG filters (turbulence clouds, blurs), and phones re-rendered them on every tilt. Now each layer is painted once into a canvas. The starry backdrop had a similar problem on Firefox for Android and moved to WebGL there. Solo project, built with Claude Code. Happy to answer questions about how it's made. And if you play, turn the sound on: can you hear your combo?
