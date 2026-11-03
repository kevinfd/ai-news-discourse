---
id: "1b1caed4cc40e7c8"
title: "What I log separately when LLM agents can talk and act in the same game"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xmcdhl/what_i_log_separately_when_llm_agents_can_talk"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xmcdhl/what_i_log_separately_when_llm_agents_can_talk"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T22:59:43Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["ViceGodIm"]
language: "en"
summary: "I built a Godot escape room for Gemini, Qwen and Nemotron. One key opens a shared exit, and players can free a trapped teammate or leave. I keep the public radio message separate from the selected button in each reply. That lets me check an offer to help against what the agent actually does, instead of treating its explanation as evidence that it performed the action. The world pauses while all…"
tags: ["r/ArtificialInteligence"]
orgs: ["Google", "Alibaba"]
topics: ["agents & coding"]
content_source: "post"
word_count: 148
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xmcdhl/what_i_log_separately_when_llm_agents_can_talk/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# What I log separately when LLM agents can talk and act in the same game

Reddit · ViceGodIm · 2026-11-02

I built a Godot escape room for Gemini, Qwen and Nemotron. One key opens a shared exit, and players can free a trapped teammate or leave. I keep the public radio message separate from the selected button in each reply. That lets me check an offer to help against what the agent actually does, instead of treating its explanation as evidence that it performed the action. The world pauses while all three choose from legal controls using the same simulation snapshot. After collecting replies, it advances three game seconds. The engine handles navigation and physics; the models receive text state and recent messages, without images. My 2:27 recording, with settings in the description: https://youtu.be/ej0GjJyqq2c I also keep raw replies and replay frames. The video contains an early collision bug and a new attempt after fixing it. Some settings changed too, so those attempts don't isolate model ability. https://preview.redd.it/79v4fpo35azh1.jpeg?width=3840&format=pjpg&auto=webp&s=91a41ba16c76e1aa174a1f310ba48ce70f87c7ba
