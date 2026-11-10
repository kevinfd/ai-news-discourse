---
id: "d21117f0d25dac9e"
title: "My 15 MB Netflix-style media app got way more love here than I expected, so I shipped it. Built with Claude 🤯"
url: "https://reddit.com/r/ClaudeAI/comments/1xsg8bv/my_15_mb_netflixstyle_media_app_got_way_more_love"
link: "https://reddit.com/r/ClaudeAI/comments/1xsg8bv/my_15_mb_netflixstyle_media_app_got_way_more_love"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T06:57:38Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["CoderLuii"]
language: "en"
summary: "last week i shared the netflix-style app i built for my media server with claude code, the 15 MB one. it got way more love than i expected, over 1,000 people joined the subreddit waiting for it. so i shipped it quick recap: a home media server usually means six apps (sonarr, radarr, lidarr, bazarr, prowlarr, seerr) just to find and get a movie. holyarrs does all of it in one app that feels like…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "search & media", "agents & coding"]
content_source: "post"
word_count: 534
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xsg8bv/my_15_mb_netflixstyle_media_app_got_way_more_love/"
score: null
comments: null
community: "r/ClaudeAI"
---

# My 15 MB Netflix-style media app got way more love here than I expected, so I shipped it. Built with Claude 🤯

Reddit · CoderLuii · 2026-11-10

last week i shared the netflix-style app i built for my media server with claude code, the 15 MB one. it got way more love than i expected, over 1,000 people joined the subreddit waiting for it. so i shipped it quick recap: a home media server usually means six apps (sonarr, radarr, lidarr, bazarr, prowlarr, seerr) just to find and get a movie. holyarrs does all of it in one app that feels like netflix, and plugs into what you already run: qbittorrent or sabnzbd to download, plex, jellyfin or emby to watch https://reddit.com/link/1xsg8bv/video/l3fhsh9seq0i1/player here's what's in it on day one: rows built from your own library, netflix style: top picks for you, "because you have…", "popular in your household", "finish the collection", and what's on the services you pay for hover any poster and it grows and plays the trailer right there, no youtube tab top 10s, new & popular and coming soon for shows, movies and music, all in one app. anyone in the house can request something with one tap moves your sonarr and radarr over in a few minutes. your files never move talks like sonarr and radarr, so the tools you already use keep working HD and 4K of the same movie side by side no api keys. posters and search come from a metadata server i run and pay for still about 15 MB, no operating system inside, signed images https://preview.redd.it/xytofjqueq0i1.jpeg?width=1920&format=pjpg&auto=webp&s=8c134f6321ce83bb1cb12a7013db9d6752cc9b88 the part i didnt expect was launch night. people started using it and reporting bugs in discord, some with the exact file and line where it broke. 1.0.1, 1.0.2 and 1.0.3 went out within 4 hours. someone asked for ukrainian, and the site and docs had it within the hour https://preview.redd.it/ku22eg7weq0i1.jpeg?width=1920&format=pjpg&auto=webp&s=4c74d20ae8e1e2eeeb7688f30653be341f4eacb9 my workflow is still simple. i design it and write the spec, claude code writes most of the code, a second agent reviews it, and then i review it myself and test it on my own server. i've been in security for 10+ years, so anything touching keys, sign-in or the network gets read line by line, and it got a full pentest before launch. the size rule from last time stayed: if a change makes it heavier, it doesnt ship what's next, mostly straight from your requests: trash guides sync for your quality rules the app itself in 11 more languages trakt lists and plex watchlists turning into requests one click to go back a version plugins, so people can add what they want without waiting on me and the bigger stuff on the roadmap for later: an mcp server, so claude and other ai apps can talk to your library asking claude things like "what should we watch tonight" and having it request it for you apps for your phone and your tv (samsung, google tv, roku, apple tv) https://preview.redd.it/54his3xxeq0i1.jpeg?width=1920&format=pjpg&auto=webp&s=828ecc28a0bf85d5abeca8c1434a4d9d4a6725b6 it's called HolyArrs and it's free. it's still a beta with bugs i want to fix, so don't make it your main app yet. if you try it, i'd love to hear what breaks. i'm in the comments and happy to go deep on the workflow whats the one thing holyarrs has to get right before you'd switch? GitHub Docker Hub HolyArrs.com Docs
