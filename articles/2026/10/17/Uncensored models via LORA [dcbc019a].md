---
id: "dcbc019ab44f672a"
title: "Uncensored models via LORA"
url: "https://reddit.com/r/LocalLLaMA/comments/1x83ign/uncensored_models_via_lora"
link: "https://reddit.com/r/LocalLLaMA/comments/1x83ign/uncensored_models_via_lora"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T06:57:03Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["vhthc"]
language: "en"
summary: "I know the heretic tool is the usual generic approach to remove refusals from a model, and a lot of research has been done to find out what parts in the LLM need to change. This gets very expensive though the larger the model is. Then for Krea2 turbo/base I saw that there are LORAs to remove censorship in the text encoder - well, image models is not something that is often discussed here, so I…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 160
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x83ign/uncensored_models_via_lora/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Uncensored models via LORA

Reddit · vhthc · 2026-10-17

I know the heretic tool is the usual generic approach to remove refusals from a model, and a lot of research has been done to find out what parts in the LLM need to change. This gets very expensive though the larger the model is. Then for Krea2 turbo/base I saw that there are LORAs to remove censorship in the text encoder - well, image models is not something that is often discussed here, so I am not surprised to not have read about that here. And now I have stumbled across this: https://github.com/msuiche/weightless - and I have not noticed previous discussions here. It seems just to reduce refusals for cyber purposes, but I think the LORA approach makes it cheaper to create and more flexible (just load/unload a lora, keep the model as-is)? Has anyone done experiments between this for eg glm 5.3 Flash and the heretic or cyber model versions of it? What are the advantages and disadvantages?
