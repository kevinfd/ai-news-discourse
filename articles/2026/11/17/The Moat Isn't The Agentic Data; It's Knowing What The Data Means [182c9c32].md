---
id: "182c9c32fd9aecac"
title: "The Moat Isn't The Agentic Data; It's Knowing What The Data Means"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/17/the-moat-isnt-the-agentic-data-its-knowing-what-the-data-means"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/17/the-moat-isnt-the-agentic-data-its-knowing-what-the-data-means"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-17T11:15:00Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Siddhartha Rao, Forbes Councils Member"]
language: "en"
summary: "Before you sign with any vendor, put these six problems on the table. Their answers will tell you more than their demos."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Oracle"]
topics: ["models & research", "agents & coding", "business & funding", "safety & ethics"]
content_source: "fulltext"
word_count: 832
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6afb41fd4e1abceae73ade64/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# The Moat Isn't The Agentic Data; It's Knowing What The Data Means

Forbes · Siddhartha Rao, Forbes Councils Member · 2026-11-17

Siddhartha Rao is a VP & Distinguished Engineer at Oracle. He has been working on AI and machine learning for the last decade.
Nearly every serious conversation about enterprise AI now includes the same four words: “Context is the moat.” Then everyone nods.
But ask what context actually is, and the room goes quiet. That silence is expensive. Companies are funding agents to “chat with their data” without being able to say what those agents need to know.
I lead generative AI services for Oracle’s AI Data Platform, so I’m not a neutral observer. Still, I’ve watched enough pilots stall to have opinions about why. Here are six of those opinions:
Proximity Is Not Comprehension
The fashionable answer to the question of context is data gravity. Bring the models to where the data already lives.
Fine. Do it. But a model sitting next to a petabyte it doesn’t understand is like a tourist outside of a library in a language they can’t read.
The advantage belongs to whomever understands the data (like which of three revenue tables finance actually trusts) and knows which instrument fits which question, whether that means forecasting for demand, Bayesian estimates for risk or deterministic rules for eligibility.
The language model’s job, working out what the data means, is narrower than the hype suggests.
Stop Calling Everything Context
Context includes metadata, the workflows a business actually runs, an ontology of the concepts it reasons in, and an understanding of how its structured and unstructured data relate.
Context is not raw rows stuffed into a prompt. Size is not meaning, and we should stop pretending otherwise.
The piece most teams miss is the tool description. An agent never reads your data model. It reads the descriptions of the tools it’s allowed to call. A generic “run SQL” tool tells it nothing. A tool described in the business’s own language, scoped to what that agent should see, tells it how to think.
Prompt engineering was about how you ask. Context engineering is about what the model is told the world contains.
Federate The Data And Consolidate The Meaning.
Should context live in one platform or stay spread across lakehouses, databases and applications? It’s a false choice. No CIO wants yet another copy of everything, with permissions that drift from the source. Leave the data where it lives and query it in place.
What has to consolidate is meaning; one semantic layer that bounds the model, orchestrates its tools and decides what each user may touch. That layer, not storage, is the control point.
Budget For Access, Not Intelligence
Gartner predicted in June 2025 that over 40% of agentic AI projects will be canceled by the end of 2027, citing costs, unclear value and inadequate risk controls. But read that list again. Nowhere does it say the model wasn’t smart enough.
Pilots run on curated data for a few users who can see everything. Production runs on thousands of users with row-level, column-level and role-based permissions. Agents make it harder by creating data the access model never anticipated, such as summaries, memories or knowledge graphs.
If an agent tells one user what it learned from another’s query, then all you’ve done is build a very polite data leak.
Don’t Wait For Smarter Models
Will better reasoning models make proprietary context obsolete? No. The frontier has moved from capability to cost. A model that rediscovers your schema on every question burns tokens, takes a different path each time and returns an answer nobody can trace. That’s a brilliant new hire with amnesia, billing by the hour.
Context is amortized reasoning. You pay once to understand the business, and every later question inherits it. That math changes only when inference is nearly free, reproducible and able to audit itself back to source rows. I wouldn’t bet the roadmap on all three.
Make Every Answer Carry Its Receipts
When an agent acts on stale or over-permissioned context, who owns the failure? Juvenal asked the governance question nearly 2,000 years ago: Who watches the watchmen? If you can’t reconstruct what the agent saw, how old it was and whose permissions applied, the answer is the CIO.
So, build governance in. Citations should trace to the business concept the agent thought it was answering and to the exact rows it used. Memory should point back to source data with a freshness timestamp. A stale finding presented as current is the most dangerous kind of wrong, because it’s plausibly right.
Fund The Map, Not Another Model
If you fund one thing on Monday morning, make it the expertise, in-house or through a partner, to build an ontology, semantic models and progressive disclosure. Give the model the map first, then reveal detail only as each question demands. It’s cheaper, more accurate and easier to govern because every disclosure becomes a checkpoint for permissions, freshness and lineage.
Before you sign with any vendor, put these six problems on the table. Their answers will tell you more than their demos.
