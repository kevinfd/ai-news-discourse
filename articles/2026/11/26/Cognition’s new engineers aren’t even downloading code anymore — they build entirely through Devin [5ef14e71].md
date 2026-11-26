---
id: "5ef14e71d3b61f79"
title: "Cognition’s new engineers aren’t even downloading code anymore — they build entirely through Devin"
url: "https://thenewstack.io/cognition-devin-automated-engineering"
link: "https://thenewstack.io/cognition-devin-automated-engineering"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-26T12:53:43Z"
published_date: "2026-11-26"
collected_at: "2026-11-26T13:04:05Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Some engineers joining Cognition no longer set up local development environments . Instead, Devin has become their primary interface for software development. \n\n Speaking to Patrick O’Shaughnessy on Tuesday’s episode of Invest Like the Best , Cognition co-founder and CEO Scott Wu describes how the company’s internal engineering practices have changed as coding agents have become more capable. \n\n…"
tags: ["AI Agents", "AI Engineering", "AI Operations"]
orgs: []
topics: ["agents & coding"]
content_source: "summary"
word_count: 742
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Cognition’s new engineers aren’t even downloading code anymore — they build entirely through Devin

The New Stack · Amanda Caswell · 2026-11-26

Some engineers joining Cognition no longer set up local development environments . Instead, Devin has become their primary interface for software development. 

 Speaking to Patrick O’Shaughnessy on Tuesday’s episode of Invest Like the Best , Cognition co-founder and CEO Scott Wu describes how the company’s internal engineering practices have changed as coding agents have become more capable. 

 No terminal, no download 

 “The funniest moment for me, I would say, was actually around like four or five months ago when we started to realize that new engineers that joined our team just didn’t even download the code on their computer,” Wu says. “Like they didn’t pull up a terminal. They didn’t run a command line or anything.” 

 “new engineers that joined our team just didn’t even download the code on their computer … They didn’t run a command line or anything.” 

 Over roughly a year, Cognition doubled its engineering headcount while increasing its rate of merged pull requests 20-fold, Wu says. That amounts to approximately ten times as many merged pull requests per engineer, despite the company’s already extensive use of AI coding tools a year earlier. 

 Perhaps more significant, Wu estimates, is that approximately 90% of Cognition’s internal Devin usage is now automated in some form. 

 When Devin runs itself 

 Wu cites incident response as an example of Cognition’s automated Devin workflows, where an error can trigger an investigation before an on-call engineer intervenes. 

 “It doesn’t involve a human saying, ‘Hey, Devin, I need you to go work on this thing’ to kick it off.” 

 “It doesn’t involve a human saying, ‘Hey, Devin, I need you to go work on this thing’ to kick it off,” Wu says. 

 Although Wu does not specify whether the 90% figure represents session count, token consumption, or another metric, automated execution has implications for compute provisioning and budget allocation as inference demand becomes less dependent on individual developer activity. 

 Cognition has already introduced hierarchical budgets for Devin , which give enterprises spending controls across organizational levels. 

 250,000 pull requests monthly 

 Wu says one of Cognition’s largest banking customers was on track to merge 250,000 pull requests with Devin in October. Until a few months earlier, the entire organization had been merging approximately 400,000 pull requests per month. 

 The bank has approximately 80,000 engineering personnel, according to Wu, and only a fraction of the organization had been fully onboarded to Devin at the time of the interview. 

 Separately, Citi CEO Jane Fraser says during the bank’s third-quarter earnings call that 14,000 engineers use Devin. 

 Neither Cognition’s internal figures nor the banking customer’s projected PR volume account for the complexity of individual changes. Wu does not provide corresponding data on change failure rates or review workloads , metrics that would help establish whether the rest of the SDLC has kept pace with implementation. 

 The disparity between implementation and review capacity has already prompted vendors such as CodeRabbit to expand into agentic change management . 

 Wu argues that enterprise adoption also requires engineering leaders to reconsider their roadmaps and organizational structures to accommodate additional implementation capacity. 

 Watching the agent swarms 

 The shift from individual background agents to swarms is a particular concern for Wu because monitoring becomes more difficult when multiple agents work together. 

 Cognition has been exploring this execution model with its recently introduced Devin Bots , persistent agents that manage other agents’ work. 

 Wu stresses the need to catch unintended agent behavior early and limit what agents can access, especially when workflows run without an engineer supervising them. 

 The engineering skill ceiling hasn’t changed 

 “The barrier to entry has for sure gotten a lot lower,” Wu says. “However, I think the skill ceiling and, you know, a lot of the particular skill sets that you need are still very much the same as they always have been.” 

 “I think people who can do that really well have always been valuable and now they’re just 10 times more valuable.” 

 For Wu, writing code is only one part of software engineering. Engineers still have to figure out what an incomplete or ambiguous specification actually means and make architectural decisions that could affect the business for years, even if an agent handles the implementation. 

 “I think people who can do that really well have always been valuable and now they’re just 10 times more valuable,” Wu says. 
 The post Cognition’s new engineers aren’t even downloading code anymore — they build entirely through Devin appeared first on The New Stack .
