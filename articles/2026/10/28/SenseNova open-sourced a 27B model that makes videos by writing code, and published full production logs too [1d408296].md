---
id: "1d408296bc89087f"
title: "SenseNova open-sourced a 27B model that makes videos by writing code, and published full production logs too"
url: "https://reddit.com/r/artificial/comments/1xhv6bq/sensenova_opensourced_a_27b_model_that_makes"
link: "https://reddit.com/r/artificial/comments/1xhv6bq/sensenova_opensourced_a_27b_model_that_makes"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T17:49:32Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["quietsam8"]
language: "en"
summary: "It's called Code2Video. Rather than generating pixels the way video models do, it writes a program for each shot, renders it, looks at the frames and revises the code. I think the reasoning holds up for a certain kind of video. If a ball bounces, the bounce comes from the physics in the code, not from what bounces usually look like. Text, formulas and chart numbers get typed in from the source,…"
tags: ["r/artificial"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 167
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xhv6bq/sensenova_opensourced_a_27b_model_that_makes/"
score: null
comments: null
community: "r/artificial"
---

# SenseNova open-sourced a 27B model that makes videos by writing code, and published full production logs too

Reddit · quietsam8 · 2026-10-28

It's called Code2Video. Rather than generating pixels the way video models do, it writes a program for each shot, renders it, looks at the frames and revises the code. I think the reasoning holds up for a certain kind of video. If a ball bounces, the bounce comes from the physics in the code, not from what bounces usually look like. Text, formulas and chart numbers get typed in from the source, so they don't come out as gibberish. And since every element is a named object, changing one thing is a small edit rather than a full regeneration that can shift the parts you liked. Besides the weights (a fine-tune of Qwen3.8-27B), the release has a skill file that walks an AI agent through the production process, a template that turns a short request into a full brief, and full production logs with the messages, tool calls and review images. It's built for motion graphics, explainers and stylized 2D or 3D scenes. Everything is at https://github.com/OpenSenseNova/SenseNova-6.8-Code2Video
