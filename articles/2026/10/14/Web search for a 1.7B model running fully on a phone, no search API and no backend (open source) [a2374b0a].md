---
id: "a2374b0a7fba5346"
title: "Web search for a 1.7B model running fully on a phone, no search API and no backend (open source)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5oqiy/web_search_for_a_17b_model_running_fully_on_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T11:28:43Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["K4anan"]
language: "en"
summary: "We just shipped web search in Private Mind, our open source app for running LLMs locally on iOS and Android. The video is the whole pitch: Qwen 3 1.7B with web off makes up Apple's September event, with web on it gets it right and cites 5 pages. The fun constraint is that a 1.7B model with a short context can't just read 5 web pages. So most of the work is picking the few hundred words it…"
tags: ["r/LocalLLaMA"]
orgs: ["Apple", "Alibaba"]
topics: ["models & research", "search & media", "products & launches"]
content_source: "post"
word_count: 208
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5oqiy/web_search_for_a_17b_model_running_fully_on_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Web search for a 1.7B model running fully on a phone, no search API and no backend (open source)

Reddit · K4anan · 2026-10-14

We just shipped web search in Private Mind, our open source app for running LLMs locally on iOS and Android. The video is the whole pitch: Qwen 3 1.7B with web off makes up Apple's September event, with web on it gets it right and cites 5 pages. The fun constraint is that a 1.7B model with a short context can't just read 5 web pages. So most of the work is picking the few hundred words it actually gets to see. Roughly how it works: There's no search API. A hidden WebView on the phone opens DuckDuckGo (Brave and Mojeek as fallbacks) and we parse the results page It opens the top pages and cuts them into ~500 character chunks An on-device embedding model (LFM2.5, ~415MB) plus some keyword matching picks the best 6 chunks, max 3 from one page If only one site claims something, it counts for less than something two sites agree on The model answers from those chunks and links every source Web search is a per-chat toggle and off by default. When it's on, the phone makes the same requests a browser would. The chat itself stays on the device. Everything runs on react-native-executorch, both the LLM and the embeddings. Repo: https://github.com/software-mansion-labs/private-mind
