---
id: "f81906995cbfcc7e"
title: "Screenshots of the custom TV launchers I mentioned: built with Claude Code for our guests and backyard"
url: "https://reddit.com/r/ClaudeAI/comments/1xdw1gd/screenshots_of_the_custom_tv_launchers_i"
link: "https://reddit.com/r/ClaudeAI/comments/1xdw1gd/screenshots_of_the_custom_tv_launchers_i"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-24T01:38:52Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["rephlektiv"]
language: "en"
summary: "I don't post here much, but a few of you asked for screenshots after my comment a couple of days ago, and the replies were really kind, so here goes. I've been running these for about six months. They're very much a hobby project, built around our house, so take it as inspiration rather than a how-to. The thing that got me started: on Android TV / Google TV, the home screen is just an app.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["products & launches", "search & media"]
content_source: "post"
word_count: 494
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdw1gd/screenshots_of_the_custom_tv_launchers_i/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Screenshots of the custom TV launchers I mentioned: built with Claude Code for our guests and backyard

Reddit · rephlektiv · 2026-10-24

I don't post here much, but a few of you asked for screenshots after my comment a couple of days ago, and the replies were really kind, so here goes. I've been running these for about six months. They're very much a hobby project, built around our house, so take it as inspiration rather than a how-to. The thing that got me started: on Android TV / Google TV, the home screen is just an app. Claude Code can build you a new one, and it can talk to Home Assistant, Plex, or anything else on your network. I ended up with three, and each image caption says which one you're looking at. 1. Guest room "hotel mode" (images 1–8) Before a visit, guests fill out a short intake form: drinks, snacks, wake-up time, how they take their coffee, favorite movie genres, and whether they'd like the cats to keep them company 🐈. The TV then: greets them by name ("Good evening… a glass of champagne, perhaps?") shows their coffee order in the morning greeting builds the Plex rows from their genres goes dim and quiet overnight until their wake-up time Music, theme and TV channels I set per guest from a small control panel. There's also a local guide with places to go and drive times, and at 5 PM a little champagne button appears. Press it and Home Assistant lets us know. 🥂 2. My father-in-law's TV (images 9–12) He's a news and markets guy, so his version puts live news and stock numbers up front. His channels cover the major news networks from around the world. He also loves to test me on whether I have some random sporting event, so every live sport we can find is in there. Claude wrote the IPTV player and Plex client from scratch, so changing channels with up/down feels like a real TV. 3. Outdoor pool + hot tub TVs (images 13–20) Pool, spa, lights, fans, misters and music from the remote, through Home Assistant. Our pool controller wasn't supported by the built-in Home Assistant integration, so Claude helped me write a custom one. There's also paging to the speakers inside ("Snacks!"), a camera view, and a doorbell pop-up, left out for privacy. What helped most, if you want to try something similar: Start with who uses that TV and what they actually want. Claude is great at turning that into a UI. Let Claude test its own work. It runs an Android TV emulator, drives it with the remote over adb, and checks the screenshots. Becoming the home screen on Google TV takes some adb steps to switch off the built-in launcher. Have a way back (Settings reachable from your app, adb access) before you do it. Route device control through Home Assistant, so the TV app stays simple. Thanks for the encouragement on the last thread. Happy to answer questions, and I'd love to see what others have built for their TVs.
