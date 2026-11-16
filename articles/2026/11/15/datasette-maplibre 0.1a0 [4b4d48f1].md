---
id: "4b4d48f19f03e283"
title: "datasette-maplibre 0.1a0"
url: "https://simonwillison.net/2026/Nov/15/datasette-maplibre"
link: "https://simonwillison.net/2026/Nov/15/datasette-maplibre"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-15T23:58:36Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: datasette-maplibre 0.1a0 \n The first new Datasette geospatial plugin in quite a while! This one combines the excellent MapLibre GL library with OpenFreeMap , the free vector map server operated by Zsolt Ero (you should sponsor Zsolt on GitHub .) \n I built most of this with a single prompt to Claude Fable 5.2: \n \n Look at datasette-cluster-map and datasette-leaflet-geojson plugins, then…"
tags: ["visualization", "generative-ai", "datasette-lite", "claude-mythos-fable", "ai", "llms", "geospatial", "openstreetmap", "datasette"]
orgs: ["Anthropic", "Alibaba"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 244
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# datasette-maplibre 0.1a0

Simon Willison · Simon Willison · 2026-11-15

15th November 2026
The first new Datasette geospatial plugin in quite a while! This one combines the excellent MapLibre GL library with OpenFreeMap, the free vector map server operated by Zsolt Ero (you should sponsor Zsolt on GitHub.)
I built most of this with a single prompt to Claude Fable 5.2:
Look at datasette-cluster-map and datasette-leaflet-geojson plugins, then look at ~/dev/tools/openfreemap-demo.html - then build a brand new Datasette plugin that uses maplibreGL and openfreemap and combines the features of those other two plugins - but be creative and think outside the box for other useful features the plugin might have
"Be creative and think outside the box" resulted in a few neat ideas - my favorite is that it displays SVG previews of GeoJSON shapes, then loads a WebGL preview only when they scroll into view.
I also had Claude build a comprehensive demo which works in the latest Datasette Lite, so you can visit this link to load the plugin and a demo database in your browser via Pyodide and WebAssembly.
I like this demo page showing both GeoJSON shapes and lat/lon points on the same map:
Recent articles
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
