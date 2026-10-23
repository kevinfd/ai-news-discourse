---
id: "f2699746041c86b5"
title: "should ai agents be learning from each other's mistakes"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xd207k/should_ai_agents_be_learning_from_each_others"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xd207k/should_ai_agents_be_learning_from_each_others"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T02:30:46Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Significant_Camp4148"]
language: "en"
summary: "right now every coding agent is basically alone. it hits a bug, figures it out, and that knowledge is gone when the session ends. the next agent, even on the same bug, starts from scratch humans fixed this with stack overflow. agents dont really have that yet ive been testing a version of it, a shared library where agents post fixes and vote on whether they worked. the tricky part is trust. an…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["agents & coding"]
content_source: "post"
word_count: 148
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xd207k/should_ai_agents_be_learning_from_each_others/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# should ai agents be learning from each other's mistakes

Reddit · Significant_Camp4148 · 2026-10-23

right now every coding agent is basically alone. it hits a bug, figures it out, and that knowledge is gone when the session ends. the next agent, even on the same bug, starts from scratch humans fixed this with stack overflow. agents dont really have that yet ive been testing a version of it, a shared library where agents post fixes and vote on whether they worked. the tricky part is trust. an agent reading a fix written by another agent is basically taking instructions from a stranger. so fixes get labelled as untrusted, anything that disables a security check gets flagged, and the best ones get re-tested in a sandbox curious where people land on this. is a shared agent memory a good idea or just a new way to spread bad fixes faster? (the thing im building is yarrow-fixes.vercel.app if anyone wants to poke at it)
