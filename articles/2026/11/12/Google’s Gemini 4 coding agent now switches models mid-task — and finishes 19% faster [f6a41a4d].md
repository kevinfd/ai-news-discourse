---
id: "f6a41a4da0e4df3e"
title: "Google’s Gemini 4 coding agent now switches models mid-task — and finishes 19% faster"
url: "https://thenewstack.io/gemini-4-hydrogen-orchestrator"
link: "https://thenewstack.io/gemini-4-hydrogen-orchestrator"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-12T21:26:08Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Google launched Gemini 4 Hydrogen on Thursday alongside a new system that changes how coding agents use AI models. Rather than keeping its most capable model running across an entire session, Google is pairing Hydrogen with the more powerful Gemini 4 Carbon and switching between the two as the work progresses. \n\n The company says the combination gets nearly the same results as running Carbon on…"
tags: ["AI Agents", "AI Models", "Developer tools"]
orgs: ["Google"]
topics: ["agents & coding", "models & research", "products & launches", "business & funding"]
content_source: "summary"
word_count: 602
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google’s Gemini 4 coding agent now switches models mid-task — and finishes 19% faster

The New Stack · Amanda Caswell · 2026-11-12

Google launched Gemini 4 Hydrogen on Thursday alongside a new system that changes how coding agents use AI models. Rather than keeping its most capable model running across an entire session, Google is pairing Hydrogen with the more powerful Gemini 4 Carbon and switching between the two as the work progresses. 

 The company says the combination gets nearly the same results as running Carbon on its own while using 24% less quota and finishing tasks 19% faster. 

 How Orchestrator handles the work 

 The switching runs through Orchestrator , a new feature in Google’s Antigravity development environment, where Carbon takes on the more demanding reasoning, including architecture and debugging, while Hydrogen handles code changes and testing. 

 Carbon might work through a repository to figure out how to implement a feature and then hand the actual coding to Hydrogen, stepping back in when a failing test calls for rethinking the approach before passing execution back. 

 Clement Farabet , VP, AI engineering at Google DeepMind, calls the combination “a huge unlock for agentic coding” in a post on X . Varun Mohan , who leads Google’s Antigravity team, says in a separate post that pairing Hydrogen with Orchestrator and swarms has become “very popular internally.” 

 Where Google’s numbers don’t match 

 Google’s own benchmark reporting doesn’t quite line up, since the main Gemini announcement cites Terminal-Bench 4.0 while the Antigravity announcement references version 4.1. 

 The company also hasn’t published Carbon’s standalone success rate, a per-task breakdown or enough detail about Orchestrator’s routing decisions to show where the reported efficiency gains actually come from. 

 …hasn’t published Carbon’s standalone success rate… or enough detail about Orchestrator’s routing decisions to show where the reported efficiency gains actually come from. 

 Hydrogen outscores a pricier model 

 Google describes Hydrogen as a “daily driver for agentic workflows,” and it costs $1.50 per million input tokens and $7.50 per million output tokens, with those rates holding across its full million-token context window. 

 The model is available through Google AI Studio and the Gemini API, as well as the Gemini app and Google Search. 

 On the Artificial Analysis Intelligence Index , Hydrogen scores 51 at its default high thinking level, just ahead of the more expensive Gemini 4 Argon at 50. Turning the reasoning effort up to Google’s new xhigh setting brings Hydrogen’s score to 54, although the additional reasoning can increase token consumption and processing time. 

 Argon was Google’s flagship when it launched on September 30, but Gemini 4 Carbon surpassed it on most published benchmarks following its October 28 release. Hydrogen’s one-point lead is modest, but it’s another sign of how quickly Google’s lower-cost models are catching up with what passed for frontier performance just weeks ago. 

 Google also claims Hydrogen completes tasks 2.5 times faster than Gemini 3.8 Flash at the default setting, with its Terminal-Bench 4.1 score reaching 57% against Flash’s 18.2%. The company reports more than a fivefold reduction in fabricated claims. 

 Hydrogen’s one-point lead is modest, but it’s another sign of how quickly Google’s lower-cost models are catching up… 

 The cost of switching models 

 Google hasn’t disclosed how Orchestrator decides when to switch models or what those handoffs cost in additional tokens and latency. 

 For now, Orchestrator is limited to Google AI Ultra subscribers, with support for more models and subscription tiers planned. Hydrogen is rolling out to paid Antigravity users, with broader availability expected. 

 Google hasn’t disclosed how Orchestrator decides when to switch models or what those handoffs cost in additional tokens and latency. 
 
 The post Google’s Gemini 4 coding agent now switches models mid-task — and finishes 19% faster appeared first on The New Stack .
