---
id: "562f8e0b6dd145c2"
title: "Giving System 1 decision models virtual gamepads: a Godot fighting experiment"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xhps40/giving_system_1_decision_models_virtual_gamepads"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xhps40/giving_system_1_decision_models_virtual_gamepads"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T14:35:23Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["ViceGodIm"]
language: "en"
summary: "I built a Godot sword-fighting tournament for eight local entrants, mostly System 1-style decision models plus a GLiNER classifier wildcard. These models pick from supplied options. I wanted quick combat decisions. The loop: structured state → legal action menu → model choice → short gamepad input. Inference runs asynchronously alongside the 60 Hz game. A held input can trigger several attacks.…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 117
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xhps40/giving_system_1_decision_models_virtual_gamepads/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Giving System 1 decision models virtual gamepads: a Godot fighting experiment

Reddit · ViceGodIm · 2026-10-28

I built a Godot sword-fighting tournament for eight local entrants, mostly System 1-style decision models plus a GLiNER classifier wildcard. These models pick from supplied options. I wanted quick combat decisions. The loop: structured state → legal action menu → model choice → short gamepad input. Inference runs asynchronously alongside the 60 Hz game. A held input can trigger several attacks. The biggest snag was action selection, OpenJev kept choosing guard with argmax. Sampling its probabilities got it moving. I reran that match, kept the first corrected take, and got the same winner. Response times differ, and there's only one fight per matchup. Repeated matches with swapped sides would make a better comparison. My tournament demo: https://youtu.be/erP5lWKykEY
