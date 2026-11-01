---
id: "bb44e5d4ae65dfd2"
title: "Used Claude to rebuild Transmission's Mac app in Liquid Glass"
url: "https://reddit.com/r/ClaudeAI/comments/1xko5jd/used_claude_to_rebuild_transmissions_mac_app_in"
link: "https://reddit.com/r/ClaudeAI/comments/1xko5jd/used_claude_to_rebuild_transmissions_mac_app_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T23:14:44Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Nik_116"]
language: "en"
summary: "Been doing this with VLC too but this one got out of hand. I forked Transmission and had Claude rebuild the Mac interface around Liquid Glass. It's called Nagare. The fun part was how we worked. I'd pick the direction, Claude would mock it up, and I kept pushing back until it felt right. The header is your download speed drawn as water, each transfer is a row of droplets, and seeding rises like…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 205
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xko5jd/used_claude_to_rebuild_transmissions_mac_app_in/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Used Claude to rebuild Transmission's Mac app in Liquid Glass

Reddit · Nik_116 · 2026-10-31

Been doing this with VLC too but this one got out of hand. I forked Transmission and had Claude rebuild the Mac interface around Liquid Glass. It's called Nagare. The fun part was how we worked. I'd pick the direction, Claude would mock it up, and I kept pushing back until it felt right. The header is your download speed drawn as water, each transfer is a row of droplets, and seeding rises like a tide. A few things that were harder than I expected: - Testing without taking over my screen. Claude built a separate test copy with its own profile, then ran it against real swarms of public-domain films - Liquid Glass in AppKit has quirks. Padding set on a stack view just gets ignored inside a glass view, for example - Old nibs. Most of the Details and Add windows ended up rebuilt in code What didn't work: it would sometimes call something done until I looked at the screenshot and it was clearly off. Comparing against the actual design every round is what fixed that. The engine is untouched, it's all interface. Free and open source if you want to look at it: https://github.com/Nik-code/nagare Happy to answer questions on the workflow.
