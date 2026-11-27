---
id: "82a13b62ffcbeb2a"
title: "OpenAI may be in cost control mode"
url: "https://micjm.com/blog/openai-is-in-cost-control-mode"
link: "https://micjm.com/blog/openai-is-in-cost-control-mode"
source: "Micjm"
domain: "micjm.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-26T07:33:12Z"
published_date: "2026-11-26"
collected_at: "2026-11-27T13:04:05Z"
authors: ["seizethecheese"]
language: "en"
summary: "OpenAI may be in cost control mode\nOpenAI’s recent release of Astra 6.2 and Sol 6.2 was widely panned. What happened?\nBased on our data, it looks like they’ve been tuned for cost savings. Specifically output tokens per task and reasoning tokens per task have dropped.\nHere is a chart of high-level cost change from the GPT-6 to GPT 6.2:\nThe X axis in the above chart is the ratio of spending of the…"
tags: []
orgs: ["OpenAI"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 237
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50652527"
score: 338
comments: 348
community: "Hacker News"
---

# OpenAI may be in cost control mode

Micjm · seizethecheese · 2026-11-26

OpenAI may be in cost control mode
OpenAI’s recent release of Astra 6.2 and Sol 6.2 was widely panned. What happened?
Based on our data, it looks like they’ve been tuned for cost savings. Specifically output tokens per task and reasoning tokens per task have dropped.
Here is a chart of high-level cost change from the GPT-6 to GPT 6.2:
The X axis in the above chart is the ratio of spending of the GPT model compared to opponents in our battle system for real work. The Y axis on the above chart is Elo from our leaderboard.
The moves in the chart are significant, here’s the same chart with confidence intervals:
What changed
Compared to opponents, Astra and Sol seem to be reasoning a lot less. Here is a chart of how much models reason compared to opponents in the same battle. Above the line means more reasoning and below means less.
You can see that both Astra 6 and Sol 6.1 were pretty normal models, but Astra 6.2 and Sol 6.2 become outliers.
We can see the same effect with output tokens:
Are these changes significant? The p-value on output dropping is 0.0055 for Sol and 0.022 for Astra. The p-value on reasoning dropping is 0.00013 for Sol and 0.0064 for Astra.
In conclusion, Astra and Sol appear to be cost tuned compared to their predecessors, and to a degree that makes them underthinking outliers.
