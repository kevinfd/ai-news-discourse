---
id: "7df196a39c2a4d8d"
title: "A free map that shows what every building in a city is used for, inferred from OpenStreetMap. Built with Claude Code, rendered in 3D for this post"
url: "https://reddit.com/r/ClaudeAI/comments/1xmi6yr/a_free_map_that_shows_what_every_building_in_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xmi6yr/a_free_map_that_shows_what_every_building_in_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T03:23:38Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Kingleyend"]
language: "en"
summary: "I built a free map that shows what every building in a city is used for: homes by density, shops, offices, industry and parking. It infers all of it from OpenStreetMap, so it works even where a city publishes no zoning data at all. It covers 77 cities in 31 countries so far. It's free to use in the browser: open the map, pick a city and click any building. You can see how a whole city is laid…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 376
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmi6yr/a_free_map_that_shows_what_every_building_in_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# A free map that shows what every building in a city is used for, inferred from OpenStreetMap. Built with Claude Code, rendered in 3D for this post

Reddit · Kingleyend · 2026-11-03

I built a free map that shows what every building in a city is used for: homes by density, shops, offices, industry and parking. It infers all of it from OpenStreetMap, so it works even where a city publishes no zoning data at all. It covers 77 cities in 31 countries so far. It's free to use in the browser: open the map, pick a city and click any building. You can see how a whole city is laid out, building by building: where it's dense, where it's all parking, where the offices cluster. Some cities publish official plans for what can be built where. In Minneapolis you can lay the map over the 2040 plan and see where reality and the plan disagree (the red buildings in the video). Minneapolis also has parks, schools, hospitals, every road and the transit lines. It started as a tool for Cities: Skylines 2: export any area as an image and trace a real city in the game. It's inferred by rules, so it's a reference, not official zoning. Checked against property records, the zone fits for 81% of homes in Philadelphia and 67% in New York. How Claude Code helped The zoning rules. Claude Code wrote the Python extractors that read OpenStreetMap extracts and turn tags, land use, height and building shape into zones. When a rule gets a case wrong, I describe it, and Claude fixes the rule and adds a test (728 so far). While making this video it found that tall buildings without a use tag were zoned as industry, the Stock Exchange among them, and fixed it. The process. A CLAUDE.md holds the project rules, bigger features start as a written plan in docs/plans before any code, and Codex reviews the changes as a second opinion. The 3D in this video. Claude Code pulled the building heights from Overpass, wrote the Three.js scene and rendered every frame with Playwright in headless Chrome. When I pointed out glitches (flickering flat lots, bridge towers standing in the river), it traced them to depth precision and to how OSM tags bridges, and fixed them. Try it: https://osyanne.github.io/CitiesSkylines2-osm-toolkit/ Code (MIT): https://github.com/Osyanne/CitiesSkylines2-osm-toolkit What would you use a map like this for? Map data © OpenStreetMap contributors, tiles © Esri.
