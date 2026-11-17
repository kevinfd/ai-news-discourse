---
id: "c59e5988cb86eddb"
title: "Would you let an AI agent keep retrying while you're asleep?"
url: "https://reddit.com/r/artificial/comments/1xxt4yh/would_you_let_an_ai_agent_keep_retrying_while"
link: "https://reddit.com/r/artificial/comments/1xxt4yh/would_you_let_an_ai_agent_keep_retrying_while"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T16:02:29Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["shoumikgoswami"]
language: "en"
summary: "An agent can fail at a task and still successfully make the next API call. That's an uncomfortable combination if nobody is watching the bill. Andrey Altrouter wrote up a simulation of a loop that keeps appending tool results and trying again. With full history sent each time and no prompt caching, later attempts cost more because they carry all the earlier attempts with them. A harness that…"
tags: ["r/artificial"]
orgs: []
topics: ["agents & coding", "policy & regulation"]
content_source: "post"
word_count: 127
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xxt4yh/would_you_let_an_ai_agent_keep_retrying_while/"
score: null
comments: null
community: "r/artificial"
---

# Would you let an AI agent keep retrying while you're asleep?

Reddit · shoumikgoswami · 2026-11-16

An agent can fail at a task and still successfully make the next API call. That's an uncomfortable combination if nobody is watching the bill. Andrey Altrouter wrote up a simulation of a loop that keeps appending tool results and trying again. With full history sent each time and no prompt caching, later attempts cost more because they carry all the earlier attempts with them. A harness that summarizes history can keep going instead of hitting the context limit. I'd want a run to stop visibly when it hits a step or spending limit, and tell me what remains unfinished. Quietly handing back a partial answer would hide the problem. What's the longest you'd leave your agent running unattended? More on the simulation's assumptions on my profile.
