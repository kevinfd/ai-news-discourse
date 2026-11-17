---
id: "ccdce806419cebd8"
title: "Cloudflare open-sourced its browser for AI agents - it runs without Chromium"
url: "https://reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents"
link: "https://reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T03:43:43Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["shoumikgoswami"]
language: "en"
summary: "Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under…"
tags: ["r/artificial"]
orgs: []
topics: ["agents & coding", "products & launches", "jobs & society"]
content_source: "post"
word_count: 111
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/"
score: null
comments: null
community: "r/artificial"
---

# Cloudflare open-sourced its browser for AI agents - it runs without Chromium

Reddit · shoumikgoswami · 2026-11-17

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?
