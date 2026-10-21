---
id: "1fbe753b698fb41a"
title: "I used Claude Code to turn 44 real cities into Cities: Skylines 2 zoning maps. 41 players asked for their city on GitHub."
url: "https://reddit.com/r/ClaudeAI/comments/1xazs8l/i_used_claude_code_to_turn_44_real_cities_into"
link: "https://reddit.com/r/ClaudeAI/comments/1xazs8l/i_used_claude_code_to_turn_44_real_cities_into"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T18:17:52Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Kingleyend"]
language: "en"
summary: "Players who rebuild real cities in Cities: Skylines 2 need to know what goes where, so I made a map that takes OpenStreetMap data and colours every building with the zone type the game would use (low density housing, offices, industry and so on). It started with Minneapolis six months ago. Now there are 44 cities in 20 countries, many of them because someone opened an issue asking for theirs.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 331
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xazs8l/i_used_claude_code_to_turn_44_real_cities_into/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Claude Code to turn 44 real cities into Cities: Skylines 2 zoning maps. 41 players asked for their city on GitHub.

Reddit · Kingleyend · 2026-10-20

Players who rebuild real cities in Cities: Skylines 2 need to know what goes where, so I made a map that takes OpenStreetMap data and colours every building with the zone type the game would use (low density housing, offices, industry and so on). It started with Minneapolis six months ago. Now there are 44 cities in 20 countries, many of them because someone opened an issue asking for theirs. You can drag the game's playable area (the 23x23 tile square) over any city and export it as a PNG for the Image Overlay mod. It's not only for the game, though. If you like maps, it's a quick way to see how land use is laid out in 44 cities. Minneapolis has a Compare mode that puts the zoning inferred from OSM next to the city's official 2040 plan and shows where they match and where they don't. Cartographers, urban planners and GIS people may find that part more interesting than the game. **How I built it with Claude Code** - A CLAUDE.md with the project rules, and a written plan for each bigger feature before any code (they live in docs/plans). - For the map viewer layout I had Claude and Codex argue. Each proposed three layouts, then each critiqued the other's and checked the claims against the code, and they agreed on one. The before and after is in the video. - 694 tests, some of them Playwright checks that open the map in a real browser. - City requests come in as GitHub issues with a bounding box. Claude Code runs the extractor for that area, rebuilds the map tiles and opens a PR. So far: 411 commits and 19 releases, one person. The zoning is inferred from OSM tags, building height and shape, so it's a reference, not a city's official zoning. Map: https://osyanne.github.io/CitiesSkylines2-osm-toolkit/ Code (MIT, no API keys): https://github.com/Osyanne/CitiesSkylines2-osm-toolkit If your city is missing, open an issue with the bounding box and I'll add it.
