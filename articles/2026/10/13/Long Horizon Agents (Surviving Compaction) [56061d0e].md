---
id: "56061d0ea30ca58d"
title: "Long Horizon Agents (Surviving Compaction)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x4wf9k/long_horizon_agents_surviving_compaction"
link: "https://reddit.com/r/LocalLLaMA/comments/1x4wf9k/long_horizon_agents_surviving_compaction"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T13:19:09Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["cryowastakenbycryo"]
language: "en"
summary: "I struggled w/ context windows and compaction limits for a while. Post compaction stupidity and loss of context would have agents hallucinating wildly after about the third compaction. Pi's context plugin helps, but adding a small proxy in front of my agents that let's them edit their system prompt has nearly stopped hallucination while adding a source of truth that the agent sees each turn. To…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["agents & coding"]
content_source: "post"
word_count: 259
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x4wf9k/long_horizon_agents_surviving_compaction/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Long Horizon Agents (Surviving Compaction)

Reddit · cryowastakenbycryo · 2026-10-13

I struggled w/ context windows and compaction limits for a while. Post compaction stupidity and loss of context would have agents hallucinating wildly after about the third compaction. Pi's context plugin helps, but adding a small proxy in front of my agents that let's them edit their system prompt has nearly stopped hallucination while adding a source of truth that the agent sees each turn. To clarify: they don't directly edit their system prompt. They edit a file that the proxy appends to the system prompt. They see this text every turn as if it is their system prompt and it's cache stable between edits. They can swap these files in and out, add more than one, etc. I don't claim to have solved the memory issue - my agents still forget things and have to figure them out all over again when they forget to take notes. But they are staying sane. They've been able to maintain state and continue working on the same project indefinitely. The first agent to use the proxy as working memory has compacted 62 times on a budget of 128k. It's seen about 232M input tokens and generated 3.8M (i have nfc how this maths). It started out as a coder building a harness. It is now the project manager for the harnessed agents and managing a couple of production jobs. The code it wrote is the asset I wanted; the agent behind the code is the asset I need to protect. How are you keeping your agents sane for the next decade?
