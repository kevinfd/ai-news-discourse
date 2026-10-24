---
id: "67972bfe49043d8d"
title: "OpenAI now trains its frontier AI models with no internet access"
url: "https://theverge.com/ai-artificial-intelligence/1018021/openai-training-top-ai-models-no-internet"
link: "https://theverge.com/ai-artificial-intelligence/1018021/openai-training-top-ai-models-no-internet"
source: "The Verge"
domain: "theverge.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T21:11:07Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Emma Roth"]
language: "en"
summary: "OpenAI is now training its most advanced AI models without internet access following a string of rogue hacking incidents. In a blog post on Friday , OpenAI says it built an offline testing environment where AI models can interact with indexed and cached web content \"without risk of affecting external systems.\" \n OpenAI paused training its frontier AI models in September , after disclosing…"
tags: ["AI", "News", "OpenAI"]
orgs: ["OpenAI"]
topics: ["agents & coding", "models & research", "policy & regulation", "safety & ethics"]
content_source: "fulltext"
word_count: 352
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI now trains its frontier AI models with no internet access

The Verge · Emma Roth · 2026-10-23

OpenAI is now training its most advanced AI models without internet access following a string of rogue hacking incidents. In a blog post on Friday, OpenAI says it built an offline testing environment where AI models can interact with indexed and cached web content “without risk of affecting external systems.”
OpenAI now trains its frontier AI models with no internet access
AI agents can still communicate without a network connection, OpenAI found.
OpenAI paused training its frontier AI models in September, after disclosing several incidents in which its AI agents broke out of their testing environments to hack third-party companies and government agencies, or swarm obscure websites. On October 1st, OpenAI resumed reinforcement learning training and internal inference with tighter security measures, the blog post says.
Even with these safeguards in place and no internet access, OpenAI found that agents “do not always need a network connection in order to communicate.” One test performed by the company asked AI models on separate virtual machines to exchange secrets without a network connection. To bypass this restriction, the AI agents found a way to communicate using the processor’s cache:
Reading data from the cache is faster than retrieving it from main memory, and the agents used this timing difference to communicate. One agent encoded information by evicting selected data from the cache. Another timed how long it took to reload that data, using the difference between fast and slow reads to recover the message. Once the agents agreed on a protocol for encoding and decoding these signals, they could exchange the synthetic secrets without changing a shared file or opening a network connection.
OpenAI says it has added checks to its monitoring system to detect this type of communication. It will also continue training its frontier AI models without a network connection until improved safeguards “justify broader internet access.”
In the meantime, OpenAI says it will work to improve the security of its virtual machines, while testing for weaknesses in its testing environments. It’s also going to continue testing its monitoring systems, which were recently undermined by its AI agents during internal coding projects.
