---
id: "23033a3e00ff08a2"
title: "Google just gave Gemini the run of your Mac — three days after Apple tightened the rules"
url: "https://thenewstack.io/gemini-mac-computer-use"
link: "https://thenewstack.io/gemini-mac-computer-use"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T21:35:09Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Google is adding computer use to its Gemini app for macOS. The assistant can now work across desktop applications and websites in a separate background window without taking over the user’s screen. Gemini handles tasks in the background while users continue working. \n\n The feature includes a live preview in the chat so users can monitor the agent’s activity, pause execution, and approve actions…"
tags: ["AI Agents", "Emerging technologies", "Security"]
orgs: ["Google", "Apple"]
topics: ["agents & coding", "products & launches", "safety & ethics"]
content_source: "summary"
word_count: 534
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google just gave Gemini the run of your Mac — three days after Apple tightened the rules

The New Stack · Amanda Caswell · 2026-11-19

Google is adding computer use to its Gemini app for macOS. The assistant can now work across desktop applications and websites in a separate background window without taking over the user’s screen. Gemini handles tasks in the background while users continue working. 

 The feature includes a live preview in the chat so users can monitor the agent’s activity, pause execution, and approve actions when necessary. 

 The company’s announcement Thursday comes just three days after Apple introduced tighter permission controls for macOS automation. 

 The company’s announcement Thursday comes just three days after Apple introduced tighter permission controls for macOS automation. Google hasn’t explained how Gemini will operate under the new restrictions. 

 Apple tightens agent permissions 

 The macOS 27.3 beta 2 changes split Device Control and Data Access permissions into two categories; System & App Protection Override and Accessibility. 

 Apps requesting broad system access will face more explicit permission prompts, and users can approve individual requests instead of granting ongoing access. 

 Developers building desktop agents will also need to account for least-privilege access , since users can restrict or revoke permissions while an agent is running. 

 Gemini’s new Mac powers 

 Google says Gemini can extract shipping details from local PDFs, gather dashboard metrics for presentations, edit batches of photos, and work with 3D design software. 

 The company hasn’t detailed how the background environment is isolated from macOS, how it maintains state across applications, or which actions require user approval. 

 Google’s existing computer-use API 

 Google introduced computer use with Gemini 2.5 in October 2025 and later integrated it directly into Gemini 3.5 Flash. 

 According to the developer documentation , the model works from screenshots and returns actions for client-side execution. Developers manage the execution environment, while the API provides configurable safety policies, and optional screenshot scanning for prompt injection. 

 The new Mac feature is part of the consumer Gemini app, not a separate developer API. 

 The new Mac feature is part of the consumer Gemini app, not a separate developer API. It’s unclear whether the app uses the same execution architecture or whether Google plans to open its background environment to third-party developers. 

 Where Google stays silent 

 The company has documented prompt-injection safeguards for its developer-facing computer-use tools but hasn’t said which protections are built into the Mac app. Agents with access to local files and privileged applications also risk untrusted input reaching the agent harness , and influencing the actions it executes. 

 Reliability questions remain unanswered since the company has not shared any performance figures for the Mac app or explained what happens when an action fails, or an application behaves unexpectedly. 

 Reliability questions remain unanswered since the company has not shared any performance figures for the Mac app or explained what happens when an action fails, or an application behaves unexpectedly. 

 Rollout, requirements and tiers 

 Gemini computer use is rolling out in English in the United States for personal Google accounts belonging to users 18 and older. The feature requires an Apple Silicon Mac running macOS Sequoia 15.0 or later and a Google AI Plus, Pro, or Ultra subscription. 
 The post Google just gave Gemini the run of your Mac — three days after Apple tightened the rules appeared first on The New Stack .
