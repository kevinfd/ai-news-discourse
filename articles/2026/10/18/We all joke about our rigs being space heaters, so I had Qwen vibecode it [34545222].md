---
id: "34545222509ff75c"
title: "We all joke about our rigs being space heaters, so I had Qwen vibecode it"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8v97a/we_all_joke_about_our_rigs_being_space_heaters_so"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8v97a/we_all_joke_about_our_rigs_being_space_heaters_so"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T05:40:13Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["PraxisOG"]
language: "en"
summary: "With winter coming up where I'm at, I wanted to see if this could actually work. Running my 4x V620 server flat out made my apartment too hot anyway, so the problem really was control. I settled on using a motherboard temperature sensor with an offset cause cases get hot. It works well enough but I want an esp32 based thermostat eventually. This project is based around the vLLM backend I use,…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: []
content_source: "post"
word_count: 140
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8v97a/we_all_joke_about_our_rigs_being_space_heaters_so/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# We all joke about our rigs being space heaters, so I had Qwen vibecode it

Reddit · PraxisOG · 2026-10-18

With winter coming up where I'm at, I wanted to see if this could actually work. Running my 4x V620 server flat out made my apartment too hot anyway, so the problem really was control. I settled on using a motherboard temperature sensor with an offset cause cases get hot. It works well enough but I want an esp32 based thermostat eventually. This project is based around the vLLM backend I use, and pauses heating when inference is needed. It also has a token gated localhost webpage for controlling target temperature so my partner can use it too. I had the project sanitized and forked for a public repo but is more of a tech demo than anything else. This project started as a meme but is good enough I'm probably going to use it lol. Heres the repo: https://github.com/PraxisOG/gpu-furnace-v2
