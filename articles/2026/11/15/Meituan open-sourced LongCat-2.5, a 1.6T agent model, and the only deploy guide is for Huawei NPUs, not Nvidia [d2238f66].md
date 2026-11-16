---
id: "d2238f6676c7f18f"
title: "Meituan open-sourced LongCat-2.5, a 1.6T agent model, and the only deploy guide is for Huawei NPUs, not Nvidia"
url: "https://reddit.com/r/artificial/comments/1xwx2hc/meituan_opensourced_longcat25_a_16t_agent_model"
link: "https://reddit.com/r/artificial/comments/1xwx2hc/meituan_opensourced_longcat25_a_16t_agent_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T14:37:57Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["javimbuilds"]
language: "en"
summary: "Meituan just released the LongCat-2.5 weights under MIT: 1.6T total parameters, about 48B active per token, with text, image and video input. On their own table it scores 88.4 on Terminal Bench v2.1, right next to Claude Opus 5 at 89.1. On the harder Terminal Bench v4.0 the gap opens up: 38.5 vs 53.9 for Opus 5. The catch if you want to self-host is that the model card only documents NPU…"
tags: ["r/artificial"]
orgs: ["Anthropic", "Nvidia", "OpenAI"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 130
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xwx2hc/meituan_opensourced_longcat25_a_16t_agent_model/"
score: null
comments: null
community: "r/artificial"
---

# Meituan open-sourced LongCat-2.5, a 1.6T agent model, and the only deploy guide is for Huawei NPUs, not Nvidia

Reddit · javimbuilds · 2026-11-15

Meituan just released the LongCat-2.5 weights under MIT: 1.6T total parameters, about 48B active per token, with text, image and video input. On their own table it scores 88.4 on Terminal Bench v2.1, right next to Claude Opus 5 at 89.1. On the harder Terminal Bench v4.0 the gap opens up: 38.5 vs 53.9 for Opus 5. The catch if you want to self-host is that the model card only documents NPU deployment, with no Nvidia path yet. As someone who builds small web projects, what I care about is that the API speaks both OpenAI and Anthropic formats, so testing it inside an existing agent setup is cheap. Has anyone run it in a real coding agent loop yet, and does it hold up outside the benchmarks? Source: https://huggingface.co/meituan-longcat/LongCat-2.5
