---
id: "79c331097e246f75"
title: "Claude built a time-loop choose-your-own-adventure, I could use some feedback"
url: "https://reddit.com/r/ClaudeAI/comments/1xqjguq/claude_built_a_timeloop_chooseyourownadventure_i"
link: "https://reddit.com/r/ClaudeAI/comments/1xqjguq/claude_built_a_timeloop_chooseyourownadventure_i"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T23:03:02Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["BlitzAce71"]
language: "en"
summary: "I've always wanted to write a time-loop story. It's one of my favorite genres, but my attempts at writing it as straight fiction never worked. So I built it as an interactive story with Claude instead. What it is: Second Hand is a choose-your-own-adventure heist set on the Halcyon, a flying art deco casino city. You come back for your younger brother or sister (chosen by the reader at game…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["jobs & society"]
content_source: "post"
word_count: 402
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqjguq/claude_built_a_timeloop_chooseyourownadventure_i/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude built a time-loop choose-your-own-adventure, I could use some feedback

Reddit · BlitzAce71 · 2026-11-07

I've always wanted to write a time-loop story. It's one of my favorite genres, but my attempts at writing it as straight fiction never worked. So I built it as an interactive story with Claude instead. What it is: Second Hand is a choose-your-own-adventure heist set on the Halcyon, a flying art deco casino city. You come back for your younger brother or sister (chosen by the reader at game start), who is working off your gambling debt in the engine room. At 2:17 AM the city falls out of the sky, and you're back on the dock at 9:00 PM, living the same night again. You're the only one who remembers. Everyone else repeats the night exactly, unless you change something. It has illustrated scenes, character portraits, ambient sound, a clock, a map and a journal. You don't carry items between loops, you carry what you've learned: codes, schedules, people's secrets. There are 4 chapters, about 150 scenes and 5 endings. How I built it with Claude: Design: I came up with the premise, characters, loop rules and endings. Claude helped me turn them into a story bible and chapter outlines. Writing: Claude drafted the prose to rules I set: second person, present tense, nobody but you remembers, strict cause and effect. I revised and redirected a lot. Engine: Claude wrote the game itself as a single HTML page with plain JavaScript. It covers scenes, timed events, the clock, the journal and theory system, the map, save codes, and a brother/sister option that changes every pronoun. Art: Claude wrote the image prompts, which I generated in ChatGPT. Claude then converted the images and placed them in scenes, and adjusted the prose so it matches what's in each picture. Testing: Claude built a checker that confirms every scene link is valid, scripted playthroughs that run each route in a headless browser, and phone and desktop screenshots to catch text overflow. Near the end it did a full consistency pass for plot holes. Hosting: It's published as a Claude artifact. Free to try: it's free and plays in the browser on phone or desktop, with no install or payment: https://claude.ai/artifact/EyDhuFZbWzNwtEy73kgGo3 It took about a week. I'm not claiming it's groundbreaking, and it still feels like an AI project. I'd really like some general feedback: is the story worth playing, where did you get confused or bored, and do you have any technical pointers?
