---
id: "5b2792c7cc46f8d1"
title: "“We are not querying like humans anymore”: OpenSearch’s Bianca Lewis on why AI agent mistakes look like successes"
url: "https://thenewstack.io/opensearch-ai-agent-observability"
link: "https://thenewstack.io/opensearch-ai-agent-observability"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-20T19:37:08Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Chris J. Preimesberger"]
language: "en"
summary: "This situation is more common than one might think: An AI agent calls the wrong API, gets a perfectly good response, and carries on as if everything went according to plan. Somewhere a dashboard is still green. For developers used to troubleshooting applications by looking for failed requests, that’s an awkward kind of success. \n\n “In the agentic AI era, we are not querying like humans anymore,”…"
tags: ["AI Agents", "AI Models", "AI Strategy", "Podcast", "sponsor-cncf", "Sponsored", "sponsored-podcast", "Video"]
orgs: []
topics: ["agents & coding", "search & media"]
content_source: "summary"
word_count: 749
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “We are not querying like humans anymore”: OpenSearch’s Bianca Lewis on why AI agent mistakes look like successes

The New Stack · Chris J. Preimesberger · 2026-11-20

This situation is more common than one might think: An AI agent calls the wrong API, gets a perfectly good response, and carries on as if everything went according to plan. Somewhere a dashboard is still green. For developers used to troubleshooting applications by looking for failed requests, that’s an awkward kind of success. 

 “In the agentic AI era, we are not querying like humans anymore,” said Bianca Lewis , executive director of the OpenSearch Software Foundation . 

 In a conversation with The New Stack senior editor for AI Frederic Lardinois at AGNTCon + MCPCon North America 2026 in San Jose, Lewis explained what that shift means for OpenSearch , the open-source project many developers already know from application search or log analytics.  

 Lewis sees a role for it on both sides of an agent’s work, helping it find the information it needs while enabling developers to see what it did with that same information. 

 Follow the agent’s trail 

 Lewis remembers when a failure at least had the decency to announce itself. 

 “Error 500 queries used to be the best thing that could ever happen because we would know that [something] went wrong,” she told TNS. “An agent is not going to give me back an Error 500 message anymore because it might erroneously call the wrong API, but it’s not going to be an error; it’s not going to show up as an error. It’s changed how we need think about our applications and how we need to observe them.” 

 A search application might give an agent access to several services. Each call can succeed on its own terms, even when the sequence takes the agent further from the user’s request. 

 Lewis describes using OpenSearch with OpenTelemetry to trace which services and APIs the agent called. Add cost data, and developers can see where a run got expensive alongside where it took a wrong turn. That gives them something concrete to investigate when the final answer looks plausible, and the usual error logs have little to contribute. 

 Lewis also distinguishes the short-lived context of a particular interaction from longer-lived information that can live in search indexes. The distinction matters when a team is deciding what to change after a bad run. The trace shows what the agent actually did. Developers can use that evidence to revisit the context the application made available to the agent in the first place. 

 The appeal of putting search and observability on a common platform is easiest to see if you already use OpenSearch for one of them. Lewis describes teams starting with observability and then using the same technology to build a search application. They can draw on existing skills and reconsider how many places they keep copies of the same business data.  

 Lardinois raises the issue of data gravity, and Lewis argues that the cost of changing platforms belongs in the total cost of ownership conversation alongside the bill for running them. 

 Who builds the next version? 

 Consolidation still takes time. Teams have applications in production for years, contracts that haven’t expired yet, and skills they’ll need to develop. Lewis and Lardinois discuss how a commercial ecosystem gives teams options for hosting and support along the way, and how an open project gives them a say in the features they’ll depend on. 

 “I think that contribution into OpenSearch can take many forms,” Lewis said. She points to pull requests, community Slack discussions, and user groups as ways to get involved. For early-career developers, she sees a chance to build a public record of how they work on a real system. 

 For experienced engineers, the systems thinking they bring to a production incident is especially valuable when an agent’s confident answer is the first clue something went sideways. 

 Lewis has a name for this shift. “I always joke — and I can say this because of my age — is that it’s sort of like revenge of the dinosaurs. We have now come to the stage where the person who understands the system-level context of what you’re trying to achieve with agentic AI becomes extremely important.” 

 Watch the full interview on The New Stack ’s YouTube channel for more on what teams are building with OpenSearch, what the community is prioritizing, and how Lewis thinks about keeping control of your data as agent workloads grow. 
 The post “We are not querying like humans anymore”: OpenSearch’s Bianca Lewis on why AI agent mistakes look like successes appeared first on The New Stack .
