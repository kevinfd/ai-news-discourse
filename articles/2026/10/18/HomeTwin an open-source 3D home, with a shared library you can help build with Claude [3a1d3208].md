---
id: "3a1d3208de0ef37d"
title: "HomeTwin: an open-source 3D home, with a shared library you can help build with Claude"
url: "https://reddit.com/r/ClaudeAI/comments/1x95rze/hometwin_an_opensource_3d_home_with_a_shared"
link: "https://reddit.com/r/ClaudeAI/comments/1x95rze/hometwin_an_opensource_3d_home_with_a_shared"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T15:19:08Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["SquareForeign"]
language: "en"
summary: "I've wanted a 3D view of my home on a wall display for years. Tap a light where it actually is, see what's happening in a room, control it from there. So I built HomeTwin. Claude built most of HomeTwin: the initial architecture, the editor, the user-facing UI, and the asset contribution skill. I guided the development, reviewed the results, and tested it in my own Home Assistant setup. I've been…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 266
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x95rze/hometwin_an_opensource_3d_home_with_a_shared/"
score: null
comments: null
community: "r/ClaudeAI"
---

# HomeTwin: an open-source 3D home, with a shared library you can help build with Claude

Reddit · SquareForeign · 2026-10-18

I've wanted a 3D view of my home on a wall display for years. Tap a light where it actually is, see what's happening in a room, control it from there. So I built HomeTwin. Claude built most of HomeTwin: the initial architecture, the editor, the user-facing UI, and the asset contribution skill. I guided the development, reviewed the results, and tested it in my own Home Assistant setup. I've been a software developer for 25 years, but modelling my whole house by hand still looked like weeks of work. The useful part of AI here is getting a starting point: upload a floor plan, get rooms, doors and windows, then check the dimensions and correct it in the editor. It's still a public beta, and that review step matters. The community part is what I care about most. The repo includes an asset contribution skill: give Claude a photo and dimensions, have it create a procedural recipe, validate it and render previews for review. We recommend Opus 5.5 or a comparable model. Take a photo of something in your house, answer a couple of questions, and in around five minutes you could have an object ready to submit. Once merged, everyone gets it through the shared library, rather than having to generate the same object again. Got a few tokens left? Help us add something from your home 🙂 Free, MIT-licensed, English and German UI. The interactive demo needs no installation. Optional AI features use your configured provider and may incur API costs. Demo: https://knaackee.github.io/hometwin/ Repo and contribution skill: https://github.com/Knaackee/hometwin Original post and discussion: https://www.reddit.com/r/homeassistant/comments/1x8xe2g/i_built_hometwin_a_3d_home_assistant_panel_with/
