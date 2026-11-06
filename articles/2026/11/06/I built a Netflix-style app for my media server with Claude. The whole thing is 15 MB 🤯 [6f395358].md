---
id: "6f395358bb26b913"
title: "I built a Netflix-style app for my media server with Claude. The whole thing is 15 MB 🤯"
url: "https://reddit.com/r/ClaudeAI/comments/1xp76q1/i_built_a_netflixstyle_app_for_my_media_server"
link: "https://reddit.com/r/ClaudeAI/comments/1xp76q1/i_built_a_netflixstyle_app_for_my_media_server"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T07:53:59Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["CoderLuii"]
language: "en"
summary: "if you run a home media server you probably have sonarr, radarr, lidarr, bazarr, prowlarr and seerr. thats six apps, and each one ships with its own little operating system inside just to run. sonarr and radarr each sit around 110-140 MB of ram doing nothing i wanted one app that does all of it and feels like netflix, so i built holyarrs. its about 15 MB to download and idles around 70 MB of ram…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "search & media"]
content_source: "post"
word_count: 318
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xp76q1/i_built_a_netflixstyle_app_for_my_media_server/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Netflix-style app for my media server with Claude. The whole thing is 15 MB 🤯

Reddit · CoderLuii · 2026-11-06

if you run a home media server you probably have sonarr, radarr, lidarr, bazarr, prowlarr and seerr. thats six apps, and each one ships with its own little operating system inside just to run. sonarr and radarr each sit around 110-140 MB of ram doing nothing i wanted one app that does all of it and feels like netflix, so i built holyarrs. its about 15 MB to download and idles around 70 MB of ram with 12,800 movies and shows in it https://reddit.com/link/1xp76q1/video/qv0lumey4yzh1/player i designed it and used claude to help write the code. one thing i learned fast is claude doesnt care about size at all. if you let it, everything slowly gets heavier. so here's what i did to keep it small: set limits before writing anything. how much memory it can use idle, how fast it starts, how big it can be. every feature had to fit inside those tested instead of guessing. i had the same home page (10,000 posters) built two different ways and measured both. one was about 3x lighter and drew the screen in half the time, so i went with that no operating system in the box. it's one program with the web app built into it and nothing else. thats most of the size difference, and it also means theres nothing in there for an attacker to use checks that fail if it gets heavy. it runs with a 12,800 item library and fails if idle memory goes over 250 MB. claude kept creeping past that until the check was there, now it holds around 70. theres also one that kills it mid-job and fails if it isnt back in 2 seconds. it comes back in about half a second the memory check stays in as features get added, so if something makes it heavier, it doesnt ship https://preview.redd.it/rflwbbzx6yzh1.png?width=2560&format=png&auto=webp&s=3981802bb283bb8f6d93437fea8a6b3a0177dddc videos of it running and the full roadmap: holyarrs.coderluii.dev
