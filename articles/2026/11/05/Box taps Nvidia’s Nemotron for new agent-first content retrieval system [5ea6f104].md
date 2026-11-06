---
id: "5ea6f104b1e8466c"
title: "Box taps Nvidia’s Nemotron for new agent-first content retrieval system"
url: "https://techcrunch.com/2026/11/05/box-taps-nvidias-nemotron-for-new-agent-first-content-retrieval-system"
link: "https://techcrunch.com/2026/11/05/box-taps-nvidias-nemotron-for-new-agent-first-content-retrieval-system"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T14:00:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Russell Brandom"]
language: "en"
summary: "The system can supposedly answer queries four times faster, with 20% fewer errors and 90% fewer tokens used."
tags: ["AI", "Box", "nvidia"]
orgs: ["Nvidia"]
topics: ["agents & coding", "chips & infrastructure", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 336
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Box taps Nvidia’s Nemotron for new agent-first content retrieval system

TechCrunch · Russell Brandom · 2026-11-05

At its developer conference on Thursday, Box showed off a new feature that will build Nvidia’s Nemotron embedding system into the core of its product.
Called Box Content Retrieval, the new feature allows agents to answer queries far more effectively by relying on the embedded metadata created by Nemotron.
Box says the upshot for users is faster, more accurate, and less expensive queries. Nvidia’s VP of generative AI software, Kari Briski, told TechCrunch that she expects queries to be answered four times faster, with 20% fewer errors and 90% fewer tokens used.
The system will be available to all of Box’s Enterprise Advance customers, rolling out early next year.
“This dramatically boosts both the relevance of our search technology for agents,” Box CEO Aaron Levie said. “Instead of an agent having to kind of read through each document, we can send back chunks from the documents that are most relevant to the user’s query or whatever the task is that the agent is doing.”
The feature is an implementation of Nvidia’s Nemotron Embed project, which offers open-weight embedding models to improve automated retrieval systems. Major labs have often overlooked such models, which use LLMs to pre-process data so it can be better used by agents. The sector has been a focus for Nvidia’s open source model project, with its recent Nemotron release in July topping the RTEB benchmark, which measures retrieval quality.
The system will be most useful when paired with active agents, Box says, giving the example of lawyers, who will ostensibly be able to find relevant clauses and precedents more easily under the new system. Because Nemotron’s embeddings go beyond simple keywords to map underlying concepts, a search tool can surface related legal themes even when different wording or language is used.
While the Nemotron models are freely available, the system also relies heavily on Box’s pre-existing metadata and permission controls, which will make it challenging to recreate from scratch. “We’re probably packing in five different technologies into one simple API,” Levie told TechCrunch.
