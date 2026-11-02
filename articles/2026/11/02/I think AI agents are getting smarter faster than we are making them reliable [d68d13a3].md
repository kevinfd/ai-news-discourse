---
id: "d68d13a397a6938d"
title: "I think AI agents are getting smarter faster than we are making them reliable"
url: "https://reddit.com/r/singularity/comments/1xlolhr/i_think_ai_agents_are_getting_smarter_faster_than"
link: "https://reddit.com/r/singularity/comments/1xlolhr/i_think_ai_agents_are_getting_smarter_faster_than"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T05:11:53Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Swimming_Ask3859"]
language: "en"
summary: "I keep seeing people ask how much smarter models need to get before agents become genuinely useful on their own. I am starting to think that is only half the problem. The model can reason correctly and still fail because the thing connecting it to the real world gives it bad information. Browser agents made this really obvious to me. Imagine an agent clicks a button and the request times out.…"
tags: ["r/singularity"]
orgs: ["Anthropic", "Google"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 537
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xlolhr/i_think_ai_agents_are_getting_smarter_faster_than/"
score: null
comments: null
community: "r/singularity"
---

# I think AI agents are getting smarter faster than we are making them reliable

Reddit · Swimming_Ask3859 · 2026-11-02

I keep seeing people ask how much smarter models need to get before agents become genuinely useful on their own. I am starting to think that is only half the problem. The model can reason correctly and still fail because the thing connecting it to the real world gives it bad information. Browser agents made this really obvious to me. Imagine an agent clicks a button and the request times out. Did the click happen Did it fail Should the agent click again That sounds like a tiny technical problem until the button says Send, Submit, Delete, or Purchase. A stronger model does not magically know what happened. The same thing happens when a website rerenders and the element the model saw no longer exists in the same state. Or the agent navigates somewhere else and keeps reasoning from an old page. Or it starts typing while the interface is still changing. The model can make a perfectly reasonable decision based on information that is already wrong. I got interested enough in this problem that I started building an open source project called Chrome Controlla. It is basically a browser control layer for AI agents that tries to make actions easier to verify. It keeps track of the exact Chrome tab and document the agent is working with. If an element changes in a way that can safely be recovered, it can try to find it again. If something moves off screen, it can scroll and check again. If part of a page is still changing, it can wait until that part actually settles before continuing. The part I care about most is what happens when an action has an unknown result. It does not just repeat the action. It tells the agent that it does not actually know whether the first one happened. I have been testing it with coding agents like Codex and Claude Code and measuring the boring parts too. A ranked page snapshot currently takes about 32 ms in my local tests. A full snapshot of a page with 4,103 nodes took 103 ms. I also had it type a 3,973 character document into Google Docs and then checked the resulting document separately instead of letting the same action that wrote it decide whether it succeeded. It is open source under Apache 2.0. You can download it here https://github.com/Praket7/chrome-controlla I am obviously biased because I built it, but the project has changed my view of where agent development is heading. We spend a huge amount of time comparing model intelligence. I think the systems around the model are going to matter more and more as the models get better. If an AI can reason for hours but cannot reliably tell whether the action it just took actually happened, that seems like a pretty serious ceiling on useful autonomy. Maybe the jump from good agents to agents we actually trust will come partly from better models. But I think a lot of it will come from making their eyes, hands, and feedback loops much harder to fool. Do you think better models eventually reason their way around problems like this, or does reliable autonomy need a much better control layer around the model too
