---
id: "df34bee602e3bce1"
title: "I made a real time fish identification app for scuba diving and snorkelling"
url: "https://reddit.com/r/ClaudeAI/comments/1xx98ed/i_made_a_real_time_fish_identification_app_for"
link: "https://reddit.com/r/ClaudeAI/comments/1xx98ed/i_made_a_real_time_fish_identification_app_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T22:52:20Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["yayimahuman123"]
language: "en"
summary: "I recently made a real time fish identification app for scuba diving and snorkelling with the help of Claude and Codex! The app works completely offline using on-device models that I fine tuned, since reception doesn’t travel underwater. It’s called FishSnapper and is available on iPhone . I had vibe coded a lot of stuff before, but this was my first time vibe training ML models. FishSnapper…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 208
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xx98ed/i_made_a_real_time_fish_identification_app_for/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a real time fish identification app for scuba diving and snorkelling

Reddit · yayimahuman123 · 2026-11-15

I recently made a real time fish identification app for scuba diving and snorkelling with the help of Claude and Codex! The app works completely offline using on-device models that I fine tuned, since reception doesn’t travel underwater. It’s called FishSnapper and is available on iPhone . I had vibe coded a lot of stuff before, but this was my first time vibe training ML models. FishSnapper uses a pipeline of two models: a fine-tune of YOLO v9 for animal detection, and a fine-tune of BioCLIP 2.5 huge, which is a visual transformer, for classification. The data is largely from iNaturalist and includes some data I labelled for this project. Something like this would’ve taken me way more time without AI coding tools. I could focus on research and user experience, and offloaded most of the operational work to Claude and Codex: assembling datasets, building data labelling UIs, renting GPUs, training models in the cloud, iterating on the iOS app, and more. I initially had low expectations, but was quite surprised at how accurate it was. I wouldn’t bet on it getting the answer right every time, but it’s been reliable enough to make it easy to confirm and has already taught me a bunch of new species.
