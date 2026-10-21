---
id: "42448fcef2e3554b"
title: "Singapore's air hit PSI 230 this week. I built a live haze map with Claude Code that shows where that air came from, and what tomorrow brings"
url: "https://reddit.com/r/ClaudeAI/comments/1xbgkdf/singapores_air_hit_psi_230_this_week_i_built_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xbgkdf/singapores_air_hit_psi_230_this_week_i_built_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T07:25:33Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["teyou"]
language: "en"
summary: "Since August, smoke from fires in Sumatra and Kalimantan has been drifting over Singapore; the 24-hour PSI peaked at 230 on 18 Oct. I wanted one place to see the fires, the smoke and the wind together, so I built it with Claude Code: https://sea-haze.teyou.dev/ (free, no login, works on phones). What it shows Every satellite fire detection since 1 Aug, replayed day by day (13,012 in Indonesia on…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "China"]
topics: ["models & research"]
content_source: "post"
word_count: 312
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbgkdf/singapores_air_hit_psi_230_this_week_i_built_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Singapore's air hit PSI 230 this week. I built a live haze map with Claude Code that shows where that air came from, and what tomorrow brings

Reddit · teyou · 2026-10-21

Since August, smoke from fires in Sumatra and Kalimantan has been drifting over Singapore; the 24-hour PSI peaked at 230 on 18 Oct. I wanted one place to see the fires, the smoke and the wind together, so I built it with Claude Code: https://sea-haze.teyou.dev/ (free, no login, works on phones). What it shows Every satellite fire detection since 1 Aug, replayed day by day (13,012 in Indonesia on 8 Oct alone) The smoke plume from Copernicus's CAMS model, including the next two days Where Singapore's air had been over the previous 5 days, from a small particle model on NOAA GFS winds Tomorrow's outlook: 31 NOAA GEFS forecasts drawn as a fan, plus a forecast PSI range (both labelled as forecasts) A 10-scene story mode, in English, Chinese, Malay and Indonesian How Claude was used Claude Code wrote the code: the Python data pipeline, the map (MapLibre, no framework), the particle model and the CI. My part was deciding what to build and what the map is allowed to claim. I ran it like a small team: several Claude Code sessions in parallel, each in its own git worktree. Every change starts as a GitHub issue and lands as a pull request with before/after screenshots, and one lead session reviews and merges. The surprise was data cleaning. Raw satellite fire data includes gas flares, factories, volcanoes, sun glint and reflections over water. We wrote a rule for each and removed 51,922 false detections before the map was honest. It now runs by itself: GitHub Actions refreshes the data twice a day, Cloudflare serves the site, and a small Cloudflare Worker warns me if the data goes stale. Happy to answer questions about the workflow or the data. What would make it more useful to you? Data: NASA FIRMS, NEA (data.gov.sg), NOAA GFS and GEFS. Contains modified Copernicus Atmosphere Monitoring Service information.
