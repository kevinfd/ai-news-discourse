---
id: "45f8bb682d722314"
title: "microsoft/UserRepGen-4B"
url: "https://reddit.com/r/LocalLLaMA/comments/1x664yt/microsoftuserrepgen4b"
link: "https://reddit.com/r/LocalLLaMA/comments/1x664yt/microsoftuserrepgen4b"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T23:16:47Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["jacek2023"]
language: "en"
summary: "https://preview.redd.it/gwb4of5vmivh1.png?width=2400&format=png&auto=webp&s=853f4cf25b4140ccf8b151b4124547788a544b33 UserRepGen-4B is a fine-tuned Qwen3.5-4B language model that generates a structured, natural-language user representation from a multi-turn user-assistant conversation. Each representation contains a task description and a behavior description for a user, and is intended to…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 114
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x664yt/microsoftuserrepgen4b/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# microsoft/UserRepGen-4B

Reddit · jacek2023 · 2026-10-14

https://preview.redd.it/gwb4of5vmivh1.png?width=2400&format=png&auto=webp&s=853f4cf25b4140ccf8b151b4124547788a544b33 UserRepGen-4B is a fine-tuned Qwen3.5-4B language model that generates a structured, natural-language user representation from a multi-turn user-assistant conversation. Each representation contains a task description and a behavior description for a user, and is intended to condition a separate LLM-based user simulator. Unlike UserLM-8b and UserLM-2.0 , which generate user utterances, UserRepGen-4B generates representations, not simulated user turns . It does not itself execute the user's task or serve as the simulator. The model was trained with online supervised fine-tuning through hindsight distillation, using feedback obtained by comparing simulated and original user behavior. At inference time, it generates a representation directly from the source conversation without requiring simulation rollouts or hindsight feedback. https://huggingface.co/microsoft/UserRepGen-4B
