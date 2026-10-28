---
id: "ef6ccba5230669ef"
title: "Playing around with 3d visualizations"
url: "https://reddit.com/r/ClaudeAI/comments/1xgs3tu/playing_around_with_3d_visualizations"
link: "https://reddit.com/r/ClaudeAI/comments/1xgs3tu/playing_around_with_3d_visualizations"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T13:10:16Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["levmiseri"]
language: "en"
summary: "I have been using Claude code and opus 5.5 to make detailed models of bio objects. First making and optimizing the cloud point engine and then trying a bunch of initial objects to render in it. The engine especially is something I’m happy with and will try using it for more stuff You can see these live at https://grimoire.bio Something that I’m trying to be more aware of and that worked nicely…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 200
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgs3tu/playing_around_with_3d_visualizations/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Playing around with 3d visualizations

Reddit · levmiseri · 2026-10-27

I have been using Claude code and opus 5.5 to make detailed models of bio objects. First making and optimizing the cloud point engine and then trying a bunch of initial objects to render in it. The engine especially is something I’m happy with and will try using it for more stuff You can see these live at https://grimoire.bio Something that I’m trying to be more aware of and that worked nicely here is making the work for Claude contained. Isolating the parts as much as possible so that it doesn’t need to fill its context with stuff not necessary for the task at hand. That then also enabled easy parallelization where I could fire up one orchestration agent and it would create bunch of subagents, each taking care of generating only one specific bio object. **The rendering engine** Written directly in WGSL compute shaders with no dependencies. Everything is points, but it’s not really ‘stored’ as points cloud. The GPU generated everything ok the spot with the number of points based on the structure in view, filling the memory dynamically. The points are splatted with atomics into a blur pyramid, no lit surfaces or other traditional 3d rendering stuff.
