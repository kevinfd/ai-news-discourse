---
id: "5d4bdf4656aab275"
title: "Compiling web applications into verified operations for AI agents"
url: "https://protocolis.co/paper"
link: "https://protocolis.co/paper"
source: "Protocolis"
domain: "protocolis.co"
source_type: "community"
collector: "hackernews"
date: "2026-11-24T19:12:02Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["vahagnb"]
language: "en"
summary: "Solid-State Web Execution: Compiling Web Applications into Verified Operations for AI Agents\nAbstract\nSuppose a hotel search calls for a $200 price cap. On its first visit to the site, Protocolis identifies the price control and gives the agent an operation it can call with that amount. The model chooses the action. The engine runs it and checks the page for evidence of the limit that took…"
tags: []
orgs: []
topics: ["models & research", "agents & coding", "business & funding"]
content_source: "fulltext"
word_count: 428
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50632998"
score: 34
comments: 12
community: "Hacker News"
---

# Compiling web applications into verified operations for AI agents

Protocolis · vahagnb · 2026-11-24

Solid-State Web Execution: Compiling Web Applications into Verified Operations for AI Agents
Abstract
Suppose a hotel search calls for a $200 price cap. On its first visit to the site, Protocolis identifies the price control and gives the agent an operation it can call with that amount. The model chooses the action. The engine runs it and checks the page for evidence of the limit that took effect. We call this solid-state web execution. The compiler derives operations from the live interface without a model call, a site-specific adapter or changes by the site owner. To our knowledge it is the first such compiler in operation. We tested it against the browser tools and agents in common use, as shipped, across three model sizes and three task lengths, with its memory and learning switched off. On long tasks that every system attempted, its default mode completed 76 percent (80 of 105); the best alternative in each comparison completed 46 percent. It was the most stable system tested: it never fell below 55 percent in any condition, while every alternative fell to 28 percent or lower. The cheapest alternative on the same model cost 1.9 to 26 times as much per completed task. On a small model it cost less than every alternative on a frontier model, in 30 of 30 pairings, and matched or exceeded its completion rate in 24. When it reported a long task finished, the judge disagreed less than half as often as with the alternatives (22 against 56 percent). Every result is a first visit, the least favourable setting for the design. We publish the tasks, the judging rules and the outcome of all 3,443 counted runs.
Headline results
- On long tasks that every system attempted, its default mode completed 76 percent (80 of 105); the best alternative in each comparison completed 46 percent.
- It was the most stable system tested: it never fell below 55 percent in any condition, while every alternative fell to 28 percent or lower.
- The cheapest alternative on the same model cost 1.9 to 26 times as much per completed task.
- On a small model it cost less than every alternative on a frontier model, in 30 of 30 pairings, and matched or exceeded its completion rate in 24.
Coming soon to arXivAuthor’s copy until it is announced there.
Replication kit · Offered for acquisition · Get in touch
Recompute every figure from the replication kit · download (.zip)
Patent-pending, in production with paying customers, offered for acquisition. Evaluation access on request: get in touch.
