---
id: "faa49b78e7169dc9"
title: "An LLM’s ETA got more accurate while its traffic controller lost to a queue rule"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xovib4/an_llms_eta_got_more_accurate_while_its_traffic"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xovib4/an_llms_eta_got_more_accurate_while_its_traffic"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T21:54:52Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["ViceGodIm"]
language: "en"
summary: "I tried a simple way to evaluate an LLM controller: log its forecast before advancing the sim, then score its actions against a baseline. At sim time 65s it predicted the ambulance would arrive at 100s. At 95s, after the delay was visible, it revised the prediction to 112s. The actual arrival was 112.2s, while a basic queue rule got there in 107.6s with the same arrivals, routes and safety…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["safety & ethics"]
content_source: "post"
word_count: 102
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xovib4/an_llms_eta_got_more_accurate_while_its_traffic/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# An LLM’s ETA got more accurate while its traffic controller lost to a queue rule

Reddit · ViceGodIm · 2026-11-05

I tried a simple way to evaluate an LLM controller: log its forecast before advancing the sim, then score its actions against a baseline. At sim time 65s it predicted the ambulance would arrive at 100s. At 95s, after the delay was visible, it revised the prediction to 112s. The actual arrival was 112.2s, while a basic queue rule got there in 107.6s with the same arrivals, routes and safety constraints. The late estimate was close, but the earlier estimate is the one I’d compare across controllers if the goal is planning ahead. This was one Godot run. My recorded experiment: https://www.youtube.com/watch?v=YY41_8_H-O8
