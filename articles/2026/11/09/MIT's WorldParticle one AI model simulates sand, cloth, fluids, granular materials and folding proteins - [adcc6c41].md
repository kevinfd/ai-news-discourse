---
id: "adcc6c41598f9c14"
title: "MIT's WorldParticle: one AI model simulates sand, cloth, fluids, granular materials and folding proteins - about 100x faster than numerical simulators on protein motion"
url: "https://reddit.com/r/artificial/comments/1xs1ggg/mits_worldparticle_one_ai_model_simulates_sand"
link: "https://reddit.com/r/artificial/comments/1xs1ggg/mits_worldparticle_one_ai_model_simulates_sand"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T19:39:06Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["winer666"]
language: "en"
summary: "Researchers at MIT, the University of British Columbia and partner institutions have built WorldParticle, a single transformer-based model that simulates six kinds of physical behaviour - cloth, elastic solids, fluids, granular materials, molecular dynamics and more - where each used to need its own dedicated solver. Instead of being programmed with each governing equation, it treats everything…"
tags: ["r/artificial"]
orgs: ["UK"]
topics: ["models & research", "health & science", "robotics & autonomy", "search & media"]
content_source: "post"
word_count: 188
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xs1ggg/mits_worldparticle_one_ai_model_simulates_sand/"
score: null
comments: null
community: "r/artificial"
---

# MIT's WorldParticle: one AI model simulates sand, cloth, fluids, granular materials and folding proteins - about 100x faster than numerical simulators on protein motion

Reddit · winer666 · 2026-11-09

Researchers at MIT, the University of British Columbia and partner institutions have built WorldParticle, a single transformer-based model that simulates six kinds of physical behaviour - cloth, elastic solids, fluids, granular materials, molecular dynamics and more - where each used to need its own dedicated solver. Instead of being programmed with each governing equation, it treats everything as particles and learns the dynamics from data, predicting how they move one step at a time. The same architecture beat existing neural simulators on accuracy across all six categories, and modelled protein motion about 100x faster than numerical simulators. The paper is published in ACM Transactions on Graphics and will be presented at SIGGRAPH Asia. MIT News covered it today: https://news.mit.edu/2026/single-ai-model-simulates-many-substances-behavior-1109 One honest caveat from the coverage: the model trades some per-phenomenon accuracy against specialist solvers, and one parameter set is trained per category - a single shared model across everything is still future work. Simulation is the bottleneck for designing everything from soft robots to new drugs. If one model can cover many materials, what changes first - the pace of drug discovery, robotics simulation, or something else entirely?
