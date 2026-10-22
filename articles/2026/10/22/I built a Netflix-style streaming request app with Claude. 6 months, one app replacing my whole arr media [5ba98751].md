---
id: "5ba987511ccaadf7"
title: "I built a Netflix-style streaming request app with Claude. 6 months, one app replacing my whole *arr media stack"
url: "https://reddit.com/r/ClaudeAI/comments/1xcaoox/i_built_a_netflixstyle_streaming_request_app_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xcaoox/i_built_a_netflixstyle_streaming_request_app_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T06:06:31Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["CoderLuii"]
language: "en"
summary: "Hi, I'm developing an alternative to the *arr stack with Claude that I called HolyArrs. It's one self-hosted app that replaces Sonarr, Radarr, Lidarr, Bazarr, Prowlarr, Seerr, SABnzbd and qBittorrent, with a Netflix-style page for browsing and requesting. Why you might want to use HolyArrs: movies, tv shows and music in one app a Netflix and Apple TV style browse page: hover a title and the…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches", "search & media", "models & research"]
content_source: "post"
word_count: 431
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xcaoox/i_built_a_netflixstyle_streaming_request_app_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Netflix-style streaming request app with Claude. 6 months, one app replacing my whole *arr media stack

Reddit · CoderLuii · 2026-10-22

Hi, I'm developing an alternative to the *arr stack with Claude that I called HolyArrs. It's one self-hosted app that replaces Sonarr, Radarr, Lidarr, Bazarr, Prowlarr, Seerr, SABnzbd and qBittorrent, with a Netflix-style page for browsing and requesting. Why you might want to use HolyArrs: movies, tv shows and music in one app a Netflix and Apple TV style browse page: hover a title and the trailer plays, browse by mood, follow an actor request a movie, a whole show or a single episode in one tap multiple versions of the same title (4K and 1080p, theatrical and director's cut, two languages) without a second instance built-in metadata service that needs no API key, or switch to TMDB or TVDB and pick the episode order per show migration wizard that imports your current library, settings and preferences without renaming or moving files compatibility API so tools like nzb360, Helmarr, Homarr widgets and Seerr keep working indexers, subtitles, Usenet and torrents in the same app modular: switch off what you don't use and restart one part without stopping the rest its own recommendation rows, worked out on your server sign-in on by default, API keys never shown or sent anywhere, fake and malware releases caught before they reach your library one Go process, about 110 MB of RAM at idle on my server optional AI search with a local or cloud model, plus an MCP server, off by default HolyArrs also doesn't send anything about your library to us. Recommendations and metadata matching happen on your server. How Claude helped: before any code, Claude studied 36 of the apps we all run in a lab and wrote manuals in our own words, and the build only works from those manuals every change gets checked against the real apps running side by side what Claude missed: it will happily ship a feature that works and looks great, but it doesn't notice cost. My last build quietly went from about 76 MB to 110 MB of idle RAM. Nothing was broken, so nothing flagged it, only measuring every build caught it. Now that number is a gate, not an afterthought You might not want to use HolyArrs yet if you need it today. It isn't public yet, and I've been running it on my own server every day first. I've been in software and security for 10+ years, so I'd rather release something you can trust with your library than something rushed. It'll be free and open source. I'm looking for a few beta testers if you run a home media server. Website: holyarrs.coderluii.dev
