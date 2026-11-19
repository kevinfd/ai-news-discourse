---
id: "630b41be4a2bc539"
title: "datasette-arrows 0.1a0"
url: "https://simonwillison.net/2026/Nov/18/datasette-arrows"
link: "https://simonwillison.net/2026/Nov/18/datasette-arrows"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-18T17:09:59Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: datasette-arrows 0.1a0 \n Datasette 1.0a43 added the ability for plugins to implement streaming export formats. Datasette core supports streaming CSV and TSV - you can export millions of lines of data from a table without needing to load it all into memory, because those two file formats support streaming data in chunks. The register_output_renderer() plugin hook can now be used to…"
tags: ["datasette", "projects"]
orgs: ["Anthropic", "Alibaba"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 230
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# datasette-arrows 0.1a0

Simon Willison · Simon Willison · 2026-11-18

18th November 2026
Datasette 1.0a43 added the ability for plugins to implement streaming export formats. Datasette core supports streaming CSV and TSV - you can export millions of lines of data from a table without needing to load it all into memory, because those two file formats support streaming data in chunks. The register_output_renderer() plugin hook can now be used to implement the same pattern for other formats.
I've learned never to release a new plugin feature without accompanying it with a plugin that uses it.
Claude Fable 5.2 suggested the Apache Arrow streaming format as a good option, and built this plugin in almost a single shot.
Add the plugin to Datasette (datasette install datasette-arrows) and the export dialog gains this new Arrow option:
This screenshot is from Datasette's main branch - the most recent release doesn't yet group streaming formats such as Arrow with the TSV and CSV in the "All rows in this table" section, but that's coming in the next alpha release.
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
