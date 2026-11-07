---
id: "d116e3633c119c23"
title: "False positive: debugging my own software flagged as reverse engineering"
url: "https://reddit.com/r/ClaudeAI/comments/1xpxotw/false_positive_debugging_my_own_software_flagged"
link: "https://reddit.com/r/ClaudeAI/comments/1xpxotw/false_positive_debugging_my_own_software_flagged"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T04:42:22Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["berkayraifov"]
language: "en"
summary: "I’m working on my own project, VSTMX, and asked an AI assistant to help debug a browser reconnect issue after a tmux crash. The request was to reproduce the bug in my development environment, inspect my application’s connection and session-selection flow, and fix the reconnect behavior. The request wasn’t about extracting a model’s hidden reasoning, reverse-engineering a model, or copying model…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 138
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpxotw/false_positive_debugging_my_own_software_flagged/"
score: null
comments: null
community: "r/ClaudeAI"
---

# False positive: debugging my own software flagged as reverse engineering

Reddit · berkayraifov · 2026-11-07

I’m working on my own project, VSTMX, and asked an AI assistant to help debug a browser reconnect issue after a tmux crash. The request was to reproduce the bug in my development environment, inspect my application’s connection and session-selection flow, and fix the reconnect behavior. The request wasn’t about extracting a model’s hidden reasoning, reverse-engineering a model, or copying model outputs. But I received this refusal: > *“This request was blocked as it seems to violate Anthropic's Terms of Service restrictions on reverse engineering or duplicating model outputs.”* It was labeled reasoning_extraction. I can’t tell which part of the prompt triggered it, and the refusal didn’t explain further. Has anyone else seen this kind of false positive on ordinary software debugging? Is there a way to report it or get more detail about what triggered the classification?
