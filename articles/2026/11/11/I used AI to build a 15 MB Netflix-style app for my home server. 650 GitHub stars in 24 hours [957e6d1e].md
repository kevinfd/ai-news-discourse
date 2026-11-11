---
id: "957e6d1e9c8e2c7b"
title: "I used AI to build a 15 MB Netflix-style app for my home server. 650 GitHub stars in 24 hours"
url: "https://reddit.com/r/ChatGPT/comments/1xtdqs9/i_used_ai_to_build_a_15_mb_netflixstyle_app_for"
link: "https://reddit.com/r/ChatGPT/comments/1xtdqs9/i_used_ai_to_build_a_15_mb_netflixstyle_app_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T09:47:22Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["CoderLuii"]
language: "en"
summary: "if you run a home media server you probably have a stack of apps like sonarr, radarr and seerr just to find and get a movie onto it. none of them look like anything the rest of the house wants to use i wanted one app that does all of it and feels like netflix, so i built holyarrs with ai. you browse it like netflix, tap a movie or show, and it gets downloaded and shows up in plex or jellyfin. it…"
tags: ["r/ChatGPT"]
orgs: []
topics: ["products & launches", "agents & coding", "search & media"]
content_source: "post"
word_count: 519
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1xtdqs9/i_used_ai_to_build_a_15_mb_netflixstyle_app_for/"
score: null
comments: null
community: "r/ChatGPT"
---

# I used AI to build a 15 MB Netflix-style app for my home server. 650 GitHub stars in 24 hours

Reddit · CoderLuii · 2026-11-11

if you run a home media server you probably have a stack of apps like sonarr, radarr and seerr just to find and get a movie onto it. none of them look like anything the rest of the house wants to use i wanted one app that does all of it and feels like netflix, so i built holyarrs with ai. you browse it like netflix, tap a movie or show, and it gets downloaded and shows up in plex or jellyfin. it doesnt play anything itself, it's the part before you press play. it's about 15 MB to download. i open sourced it yesterday and it's already at 650 stars on github, way more than i expected https://reddit.com/link/1xtdqs9/video/1l26ajdpfy0i1/player what it does: rows built from your own library, netflix style: top picks for you, "because you have…", "finish the collection", and what's on the services you pay for hover any poster and it grows and plays the trailer right there anyone in the house can request something with one tap, and you approve it top 10s, new & popular and coming soon, so finding something to watch is easy https://preview.redd.it/5jtt7a1sfy0i1.jpeg?width=1920&format=pjpg&auto=webp&s=03f138ccaa906b22bc3e03bec158401a12859354 i designed it and used ai to write most of the code. one thing i learned fast is the ai doesnt care about size at all. if you let it, everything slowly gets heavier. so here's what i did: tested instead of guessing. the ai can write two versions of something fast, but it cant tell you which one is lighter. i had the home page built both ways and measured. one was about 3x lighter, so that's the one that shipped checks that fail if it gets heavy. the tests fail if the app uses more than 250 MB of memory sitting idle. the ai kept creeping past that until the check was there, now it sits around 70 launch night was the best part. people jumped into discord and tested it hard, some even sent the exact file and line to fix. i had 3 updates out within 4 hours, and it's at 18 updates and 5,000+ docker pulls since https://preview.redd.it/y4frnkgtfy0i1.jpeg?width=1920&format=pjpg&auto=webp&s=c863d6fba85f094c387e5a88c9e915232a43af00 my workflow is simple. i design it and write the spec, ai writes most of the code, a second agent reviews it, and then i review it myself and test it on my own server. i've been in security for 10+ years, so anything touching keys, sign-in or the network gets read line by line, and it got a full pentest before launch later on the roadmap, not started yet: letting chatgpt and other ai apps talk to your library, so you can ask "what should we watch tonight" and have it request it for you it's called HolyArrs and it's free. it's still a beta with bugs i want to fix, so don't make it your main app yet. if you try it, i'd love to hear what breaks. i'm in the comments and happy to go deep on the workflow if you build with ai too, whats the one rule that keeps your project from getting heavier and messier? GitHub Docker Hub HolyArrs.com Docs
