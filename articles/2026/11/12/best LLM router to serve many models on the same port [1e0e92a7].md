---
id: "1e0e92a7166b14a3"
title: "best LLM router to serve many models on the same port?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xujdb3/best_llm_router_to_serve_many_models_on_the_same"
link: "https://reddit.com/r/LocalLLaMA/comments/1xujdb3/best_llm_router_to_serve_many_models_on_the_same"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T17:45:20Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["andreabarbato"]
language: "en"
summary: "I'm working on a router that wraps many LLMs serving from different ips and ports and exposes them all as a single port, since i have 2 machines serving many slots of Qwen 3.8 FN but i wanted to ensure speed is always fast (one machine is faster and can hold more slots, but too many slots busy and then it's better to call the other machine, also i gotta avoid evicting from the cache active…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["agents & coding"]
content_source: "post"
word_count: 118
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xujdb3/best_llm_router_to_serve_many_models_on_the_same/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# best LLM router to serve many models on the same port?

Reddit · andreabarbato · 2026-11-12

I'm working on a router that wraps many LLMs serving from different ips and ports and exposes them all as a single port, since i have 2 machines serving many slots of Qwen 3.8 FN but i wanted to ensure speed is always fast (one machine is faster and can hold more slots, but too many slots busy and then it's better to call the other machine, also i gotta avoid evicting from the cache active conversations, that kind of workflow) I might be reinventing the wheel tho so: how do you guys solve for this kind of situation? edit: thanks a lot for all the answers i had no idea there was so much stuff around lol
