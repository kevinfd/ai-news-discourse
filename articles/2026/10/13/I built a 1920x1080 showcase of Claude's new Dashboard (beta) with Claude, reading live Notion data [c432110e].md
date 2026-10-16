---
id: "c432110ec2c865f1"
title: "I built a 1920x1080 showcase of Claude's new Dashboard (beta) with Claude, reading live Notion data"
url: "https://reddit.com/r/ClaudeAI/comments/1x534mn/i_built_a_1920x1080_showcase_of_claudes_new"
link: "https://reddit.com/r/ClaudeAI/comments/1x534mn/i_built_a_1920x1080_showcase_of_claudes_new"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T17:34:14Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["UnhappyTap9123"]
language: "en"
summary: "I built this myself, in one Claude session, to find out what the new Dashboard artifact can and cannot do. It is a sandbox with eight tabs (slides) that demo each element type, with a small caption under every object naming its type and subtypes. What it is: - A typed Dashboard artifact on a fixed 1920x1080 canvas, scaled to the viewer width. - KPI tiles with deltas and 17 chart types drawn in…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 417
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x534mn/i_built_a_1920x1080_showcase_of_claudes_new/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a 1920x1080 showcase of Claude's new Dashboard (beta) with Claude, reading live Notion data

Reddit · UnhappyTap9123 · 2026-10-13

I built this myself, in one Claude session, to find out what the new Dashboard artifact can and cannot do. It is a sandbox with eight tabs (slides) that demo each element type, with a small caption under every object naming its type and subtypes. What it is: - A typed Dashboard artifact on a fixed 1920x1080 canvas, scaled to the viewer width. - KPI tiles with deltas and 17 chart types drawn in d3 (bar, grouped, stacked, line/area/step, donut, treemap, heat map, funnel, waffle, gauge and others). - Filters and chips, a sortable and searchable table with a drilldown panel, custom buttons and switches, inline SVG icons, and a Present mode that auto-advances. - Accent colour, labels and motion can be tweaked live. How it works (the useful part): - Data comes from 3 saved Notion views, not direct database queries. Each dataset is one live query against a view, so a dashboard costs 3 queries in total. This was my fix for the quota problems I had before. - All maths lives in 17 dash.calc functions that chain on each other. The page only draws their output. - Limits I hit: Notion views return at most 100 rows, and there are no forms, iframes, inline handlers or maps. How Claude helped: - Claude read my earlier field-guide notes, created the three Notion views, and wrote the whole page (about 1,300 lines of HTML, CSS and JS). It dry-ran the calcs in node against my real data before publishing. When I sent a phone screenshot with the title and right side cut off, it found the scaling bug and fixed it in one edit. Why bother: - I wanted one page that proves what is possible before I build real dashboards, and a checklist of what needs a prompt versus what I can edit myself. Free to try: - The Dashboard is in beta (announced 8 Oct 2026) on paid plans, and an Enterprise owner has to enable it. My copy reads my private Notion, so I cannot share a working link. To rebuild it, connect Notion (or any connector) and use a prompt like: -Create a Dashboard artifact named "Demo and tools presentation", 1920x1080, with tabs for KPI tiles, bar, part-to-whole and line charts, filters, a sortable table with drilldown, and custom buttons. Use one saved view per dataset so queries stay low. Put a small caption under each object naming its type. Happy to answer questions about the calc structure or the quota workaround.
