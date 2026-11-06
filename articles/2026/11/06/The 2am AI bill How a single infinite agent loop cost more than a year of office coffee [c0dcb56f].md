---
id: "c0dcb56f656cff3a"
title: "The 2am AI bill: How a single infinite agent loop cost more than a year of office coffee"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xp4zgr/the_2am_ai_bill_how_a_single_infinite_agent_loop"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xp4zgr/the_2am_ai_bill_how_a_single_infinite_agent_loop"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T05:35:58Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["longtriproad"]
language: "en"
summary: "I keep thinking about the 2am problem. A tool goes down. Your agent doesn't know that, so it retries. The retry fails, so it retries again. Each one of those is a paid model call, and it will happily do this for six hours because nothing told it to stop. You find out in the morning, usually from the provider's spend alert, which is a strange kind of alert since by the time it arrives the money…"
tags: ["r/ArtificialInteligence"]
orgs: ["OpenAI", "Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 226
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xp4zgr/the_2am_ai_bill_how_a_single_infinite_agent_loop/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# The 2am AI bill: How a single infinite agent loop cost more than a year of office coffee

Reddit · longtriproad · 2026-11-06

I keep thinking about the 2am problem. A tool goes down. Your agent doesn't know that, so it retries. The retry fails, so it retries again. Each one of those is a paid model call, and it will happily do this for six hours because nothing told it to stop. You find out in the morning, usually from the provider's spend alert, which is a strange kind of alert since by the time it arrives the money has already left. I've heard a few versions of this story now. The amounts vary. The feeling doesn't. One person told me a single agent on one bad night cost more than their office spends on coffee in a year, and I'm honestly not sure that was an exaggeration. I’ve been working on a solution for this called ACPPotamia. It sits between your agents and OpenAI or Anthropic. Before any call goes out it checks that call will cost against a budget you set, and if an agent is just repeating itself it cuts it off. Setup is changing one URL in your existing SDK, which took longer to write in this post than to actually do. You can check it out here: acp.examopotamia.com I'd like to hear how your team found out, if it's happened to you. Was it the invoice? A dashboard? Someone's gut feeling at 3am?
