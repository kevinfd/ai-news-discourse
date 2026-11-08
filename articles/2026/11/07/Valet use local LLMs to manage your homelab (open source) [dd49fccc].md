---
id: "dd49fccc8f7e4709"
title: "Valet: use local LLMs to manage your homelab (open source)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xq7qi4/valet_use_local_llms_to_manage_your_homelab_open"
link: "https://reddit.com/r/LocalLLaMA/comments/1xq7qi4/valet_use_local_llms_to_manage_your_homelab_open"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T14:32:04Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["egfwivbwwruigwrhfbsr"]
language: "en"
summary: "My favourite use case for local LLMs is running my homelab, because everything stays private (and it helps me justify the GPU lol) I wanted one dashboard to help me manage all of my services, so I made Valet. Live demo: https://demo.askvalet.dev Valet has a chat agent that works with any local or hosted model. It integrates with 185+ services and supports custom plugins. You can ask it to pause…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Anthropic"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 411
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xq7qi4/valet_use_local_llms_to_manage_your_homelab_open/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Valet: use local LLMs to manage your homelab (open source)

Reddit · egfwivbwwruigwrhfbsr · 2026-11-07

My favourite use case for local LLMs is running my homelab, because everything stays private (and it helps me justify the GPU lol) I wanted one dashboard to help me manage all of my services, so I made Valet. Live demo: https://demo.askvalet.dev Valet has a chat agent that works with any local or hosted model. It integrates with 185+ services and supports custom plugins. You can ask it to pause pi-hole, investigate crash logs, request a movie, etc It also knows its own docs, so it can configure itself. Tell it what you want changed on your dashboard and it edits the config (with your approval). I was already addicted to tweaking my homepage but this made it way more fun haha What I run it on Qwen 3.8 27B on a 5090, about 230 tok/s. Most responses take 2–5 seconds Qwen passes about 90% of a small eval set I wrote. Where it struggles is open ended digging (like "why isn’t this timer running?”) where it can burn through tons of tool calls Managing context is tricky because I run a lot of services, so tool definitions were ~90% of the prompt before some optimizations What helped: Hiding tools from unused integrations that aren't needed in chat Turning thinking off makes it 2–3x faster, but it starts making up answers to follow ups Lazy load tools (starts with a short list of tools and loads more only when a question needs them) Those cut tokens per answer by 30-50%. Obviously every model and setup is different so everything is configurable from the config file AI involvement I’m a SWE and used Claude for almost all of the coding, but I designed + reviewed everything and made the architecture decisions. I was very conscious of slop, security, and performance as I wanted to build something high quality. But it’s early so there may be rough edges I haven’t caught Security and privacy: Runs on your own hardware with no account or telemetry Read only by default, nothing can be changed from the page until you turn on auth (local accounts, OIDC, or your proxy’s auth) Keys stay on the server and API keys live in .env. The browser only gets the finished cards The AI never sees your keys. Anything that changes something waits for your approval and with a local model nothing leaves your network Docker access is read-only through a socket proxy Docs (completely free + open source): https://askvalet.dev
