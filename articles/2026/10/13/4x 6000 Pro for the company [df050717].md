---
id: "df050717a1adb49f"
title: "4x 6000 Pro for the company"
url: "https://reddit.com/r/LocalLLaMA/comments/1x4yoqm/4x_6000_pro_for_the_company"
link: "https://reddit.com/r/LocalLLaMA/comments/1x4yoqm/4x_6000_pro_for_the_company"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T14:49:31Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["q-admin007"]
language: "en"
summary: "Here is how i serve 40 people (10 of them developers) with local AI services. n8n for automatisation whisper and Vexa AI, a bot joins Teams and makes transcripts, n8n later extracts decisions and todos OpenWebUI, ChatGPT-like webinterface for everyone, most agentic features are disabled, websearches via Tavily are possible Every developer has an API key to use via BiFrost (OpenAI compatible API…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "AMD", "Alibaba"]
topics: ["agents & coding"]
content_source: "post"
word_count: 194
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x4yoqm/4x_6000_pro_for_the_company/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 4x 6000 Pro for the company

Reddit · q-admin007 · 2026-10-13

Here is how i serve 40 people (10 of them developers) with local AI services. n8n for automatisation whisper and Vexa AI, a bot joins Teams and makes transcripts, n8n later extracts decisions and todos OpenWebUI, ChatGPT-like webinterface for everyone, most agentic features are disabled, websearches via Tavily are possible Every developer has an API key to use via BiFrost (OpenAI compatible API router) for what they find useful Every developer has a local Linux VM where agents can be installed. A 4U server that contains 4 6000 Blackwell MaxQ and 384GB DDR5 and one AMD EPYC 9275F 24-Core CPU. The server runs Proxmox, every model or application runs inside LXC with Cuda 13.3 and Debian 13, Driver 595. mainmodel is Deepseek V4 Flash with vLLM, GPU utilization 0.55, TP4, 1M context. fallbackmodel is Qwen 3.8 27B Q8 with llama.cpp, 265K context in Q8. minimodel is K2-Horizon 7B Q6 with llama.cpp, with 64K context in Q8. ComfyUI to generate pics and videos for marketing. Embedding/Reranking with Geofront/BGE-M3-GGUF:BF16 and sinjab/bge-reranker-v2-m3-F16-GGUF with llama.cpp Overall cost of the server was around 55k€. Backup server with two 6000 Blackwell MaxQ is planned https://preview.redd.it/eribrlg7z8vh1.png?width=1913&format=png&auto=webp&s=33c7044412273dec45e9c251c879d4b2a1dd6e53 Ask if you have questions.
