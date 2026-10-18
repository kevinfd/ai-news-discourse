---
id: "27d0e2fc1a87d037"
title: "how do teams catch AI chatbots giving customers wrong answers? ours promised free repairs"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8f7cc/how_do_teams_catch_ai_chatbots_giving_customers"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8f7cc/how_do_teams_catch_ai_chatbots_giving_customers"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T16:55:59Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["CommonMinimum587"]
language: "en"
summary: "so we moved our support bot onto our own self-hosted model earlier this year so customer data stays in house. It answers from our help docs with RAG and for months it was fine and just ast week a customer sent a screenshot where the bot told him accidental damage was covered under warranty and we’d repair it for free. It isn’t and we don’t. The doc it pulled was about the extended plan, which he…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["safety & ethics", "models & research"]
content_source: "post"
word_count: 292
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8f7cc/how_do_teams_catch_ai_chatbots_giving_customers/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# how do teams catch AI chatbots giving customers wrong answers? ours promised free repairs

Reddit · CommonMinimum587 · 2026-10-17

so we moved our support bot onto our own self-hosted model earlier this year so customer data stays in house. It answers from our help docs with RAG and for months it was fine and just ast week a customer sent a screenshot where the bot told him accidental damage was covered under warranty and we’d repair it for free. It isn’t and we don’t. The doc it pulled was about the extended plan, which he doesn’t have, and the bot blended the two we had to honor it cause arguing with a screenshot of your own bot is a losing game, air Canada literally lost a tribunal case over its chatbot giving misleading info about bereavement fares in 2024.haunting part is nothing in our logs looked obviously wrong. The answer was fluent and on topic, it was just built on the wrong chunk and from reading around, catching this before the customer does seems to split into two jobs one is to logging the retrieved chunks next to every answer so you can trace where things went wrong, and tools like Langfuse or Arize Phoenix help with that. The other is a check on the live answer before it gets sent, blocking anything about coverage or refunds that the retrieved evidence doesn’t actually back up then second part we’re looking at Orq AI, which runs evaluators as guardrails that block a response when a check fails, and has an on-prem install so nothing leaves our setup. The alternative is Nemo Guardrails and writing more of the checks ourselves Still not sure whether a guardrail on the way out catches more than someone reading transcripts every morning, especially when the bot mixes up two policies that are both technically in the docs
