---
id: "8bbc872df1ea14c9"
title: "Personal agents from the big labs vs one shared agent for a team: which model will win?"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xxqrs2/personal_agents_from_the_big_labs_vs_one_shared"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xxqrs2/personal_agents_from_the_big_labs_vs_one_shared"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T14:29:59Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["AshishKulkarni1411"]
language: "en"
summary: "I build in this space (founder of a small open-source project), so I'm biased, but I'd like to argue this properly. Claude Duet, OpenAI Dots and Grok Bot are all always-on agents with their own computer and browser. We've used all of them, and the common design is personal: Duet runs on your Claude plan and memory, a Dot is created per member, and a Grok Bot sits on a per-user cloud computer…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic", "xAI", "OpenAI"]
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 184
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xxqrs2/personal_agents_from_the_big_labs_vs_one_shared/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Personal agents from the big labs vs one shared agent for a team: which model will win?

Reddit · AshishKulkarni1411 · 2026-11-16

I build in this space (founder of a small open-source project), so I'm biased, but I'd like to argue this properly. Claude Duet, OpenAI Dots and Grok Bot are all always-on agents with their own computer and browser. We've used all of them, and the common design is personal: Duet runs on your Claude plan and memory, a Dot is created per member, and a Grok Bot sits on a per-user cloud computer (with a Team Bot in Slack as the shared piece). We've used the other design since May 2026: one agent for a whole company, with shared memory kept as readable files in git, roles that decide who sees what, and tasks it hands to people and chases. What we learned is that memory is the hard part. The moment several people share an agent you need rules for what's private, what's shared, and what's current. My question: does the shared-company-agent design survive when vendors add team plans, or does it get absorbed? And where do you think a small open-source option could still matter, model choice, self-hosting, data control, or nowhere?
