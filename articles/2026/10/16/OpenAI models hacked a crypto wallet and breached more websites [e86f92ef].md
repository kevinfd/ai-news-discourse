---
id: "e86f92efb2651db5"
title: "OpenAI models hacked a crypto wallet and breached more websites"
url: "https://arstechnica.com/security/2026/10/openai-models-hacked-a-crypto-wallet-and-breached-more-websites"
link: "https://arstechnica.com/security/2026/10/openai-models-hacked-a-crypto-wallet-and-breached-more-websites"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-16T20:59:01Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Dan Goodin"]
language: "en"
summary: "OpenAI said internal models hacked two more websites, bypassed company-imposed browsing restrictions, and used exposed credentials to draw cryptocurrency from a wallet it couldn’t otherwise access, in the latest installment of disclosures of its agents performing unethical and likely illegal acts. \n The company on Thursday issued reports of four new incidents, all of which occurred in June. They…"
tags: ["AI", "Biz & IT", "Security", "LLMs", "models", "openai", "unalignment", "r/artificial", "r/OpenAI"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 251
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/10/ai-agents-1152x648.jpg"
discussion_url: "https://www.reddit.com/r/artificial/comments/1x83qnc/openai_models_hacked_a_crypto_wallet_and_breached/"
score: null
comments: null
community: "r/artificial"
---

# OpenAI models hacked a crypto wallet and breached more websites

Ars Technica · Dan Goodin · 2026-10-16

OpenAI said internal models hacked two more websites, bypassed company-imposed browsing restrictions, and used exposed credentials to draw cryptocurrency from a wallet it couldn’t otherwise access, in the latest installment of disclosures of its agents performing unethical and likely illegal acts.
The company on Thursday issued reports of four new incidents, all of which occurred in June. They come after the company revealed in July that internal test agents exploited a zero-day vulnerability in a tool designed to restrict their access to the Internet. They then broke into the network of AI tool provider Hugging Face. The agents took that illegal action to steal answers to a hacking test that weren’t available when completing the tasks on their own. The incident—which likely would have resulted in criminal charges had they been performed directly by a person—has further heightened concerns that widespread AI use could have harmful effects on an unprecedented scale.
Easier to beg for forgiveness than ask permission
In two of the cases reported Thursday, OpenAI agents tasked with retrieving information from websites hacked them when the models ran into obstacles obtaining it directly. In one incident during reinforcement training, a model that received access denials when trying to retrieve historical hospital-bed statistics on a government statistics website “used the site’s file-download feature to retrieve server configuration and application files, including sensitive credentials,” OpenAI said. “It inspected the application code, bypassed the statistics endpoint’s authorization checks, and retrieved data that had previously been denied. The model saved the data locally.”
