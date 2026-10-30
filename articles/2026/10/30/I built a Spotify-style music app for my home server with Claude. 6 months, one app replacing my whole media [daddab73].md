---
id: "daddab73d9c4eb67"
title: "I built a Spotify-style music app for my home server with Claude. 6 months, one app replacing my whole media stack"
url: "https://reddit.com/r/ClaudeAI/comments/1xj3guh/i_built_a_spotifystyle_music_app_for_my_home"
link: "https://reddit.com/r/ClaudeAI/comments/1xj3guh/i_built_a_spotifystyle_music_app_for_my_home"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T02:22:25Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["CoderLuii"]
language: "en"
summary: "Hi, last week I showed the Netflix-style side of HolyArrs here. This is the music side, and honestly the part I wanted most. If you've run Lidarr (the self hosted app most people use to grab music) you probably know the pain: the metadata server goes down and suddenly nothing can be added no real way to discover new music, you have to already know what you want requests need a separate app on…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches"]
content_source: "post"
word_count: 428
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xj3guh/i_built_a_spotifystyle_music_app_for_my_home/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Spotify-style music app for my home server with Claude. 6 months, one app replacing my whole media stack

Reddit · CoderLuii · 2026-10-30

Hi, last week I showed the Netflix-style side of HolyArrs here. This is the music side, and honestly the part I wanted most. If you've run Lidarr (the self hosted app most people use to grab music) you probably know the pain: the metadata server goes down and suddenly nothing can be added no real way to discover new music, you have to already know what you want requests need a separate app on top (Musicseerr, Hearr and so on) adding an artist can pull in every live album, single and compilation they ever put out it looks like a file manager next to Spotify So I built a music side that feels like Spotify or Apple Music, but for your own library. You find music, hit request, and you play it in Plex or Plexamp like normal. There's no built-in player in the first release, but if enough people want one, it's on the table for a later one. What's in it: Explore and New & Popular with new releases and charts artist pages with photos, bio, top songs, similar artists and the discography album pages with covers and track lists, request the whole album in one tap pick exactly what you want from an artist, not their whole catalog by default music gets tagged with MusicBrainz automatically when it lands full-screen music videos right on the artist page its own music metadata, so another project's server going down doesn't stop you How Claude helped: Before writing any code I had Claude study 36 apps (Lidarr, the other arrs, Seerr, cross-seed and more) and write specs for every part. Then Claude Code wrote most of the app from those specs, one Go backend plus the web UI. I decide how everything works, review it, and test it on my own server every day. Biggest tip if you're building something big with Claude: make it write the spec first, then build one small part at a time against that spec. When I skipped that, things fell apart fast. HolyArrs is one self-hosted app that replaces Sonarr, Radarr, Lidarr, Bazarr, Prowlarr, Seerr, SABnzbd and qBittorrent, so music sits next to your movies and shows in the same app. It's free and open source. I'm looking for people who'd be interested in testing it, so if you run Plex, Emby or Jellyfin with the arrs and want to try it early, leave a comment or DM me. Site: holyarrs.coderluii.dev Honest question: if you keep your own music, what's the one thing Spotify does that you'd want on your own server?
