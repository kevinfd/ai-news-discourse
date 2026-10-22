---
id: "d1bb8b23a5d566d8"
title: "I gave Claude Code my parents' TV model number. It found the TV on Wi-Fi and cleaned out the ads. The interesting part: the prompt is mostly a list of things it must NOT do"
url: "https://reddit.com/r/ClaudeAI/comments/1xbrzo0/i_gave_claude_code_my_parents_tv_model_number_it"
link: "https://reddit.com/r/ClaudeAI/comments/1xbrzo0/i_gave_claude_code_my_parents_tv_model_number_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T16:31:35Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Gathin23"]
language: "en"
summary: "Last Saturday my parents' TV played a sponsored ad before Netflix. I gave Claude Code the model number and let it work over ADB. It found the TV on the network, disabled 25 Xiaomi ad and tracking packages, and wrote them a simple home screen. What made it work wasn't the clever part, it was the guardrails: Back up the full package list before touching anything Disable, never uninstall, so…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["models & research", "safety & ethics"]
content_source: "post"
word_count: 170
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbrzo0/i_gave_claude_code_my_parents_tv_model_number_it/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I gave Claude Code my parents' TV model number. It found the TV on Wi-Fi and cleaned out the ads. The interesting part: the prompt is mostly a list of things it must NOT do

Reddit · Gathin23 · 2026-10-21

Last Saturday my parents' TV played a sponsored ad before Netflix. I gave Claude Code the model number and let it work over ADB. It found the TV on the network, disabled 25 Xiaomi ad and tracking packages, and wrote them a simple home screen. What made it work wasn't the clever part, it was the guardrails: Back up the full package list before touching anything Disable, never uninstall, so everything is reversible in one line A list of packages it must never touch (setup, Wi-Fi, input, and on Google TV the one that breaks casting) Ask before disabling anything the family might actually use I posted the before/after, and it got a bit out of hand: over 4 days about 200 people sent PRs with lists for their own TVs, and it's now around 150 models from 50 brands. Most of the prompt's rules came from people's TVs breaking in new ways. If you've used Claude Code on hardware like this, I'm curious what guardrails you ended up adding.
