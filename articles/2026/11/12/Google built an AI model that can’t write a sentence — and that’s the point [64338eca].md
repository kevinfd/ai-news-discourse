---
id: "64338ecad904c5f5"
title: "Google built an AI model that can’t write a sentence — and that’s the point"
url: "https://thenewstack.io/google-gemini-decisions-api"
link: "https://thenewstack.io/google-gemini-decisions-api"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-12T17:02:36Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Google’s new Gemini Decisions API, introduced Wednesday, is designed to handle the routine decisions that AI applications make thousands of times a day, with lower costs, and faster response times than traditional generative models. \n\n …the routine decisions that AI applications make thousands of times a day, with lower costs and faster response times than traditional generative models. \n\n…"
tags: ["AI Engineering", "AI Models", "Developer tools"]
orgs: ["Google", "OpenAI", "Microsoft"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 595
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google built an AI model that can’t write a sentence — and that’s the point

The New Stack · Amanda Caswell · 2026-11-12

Google’s new Gemini Decisions API, introduced Wednesday, is designed to handle the routine decisions that AI applications make thousands of times a day, with lower costs, and faster response times than traditional generative models. 

 …the routine decisions that AI applications make thousands of times a day, with lower costs and faster response times than traditional generative models. 

 Instead of using a generative model to work through each decision and produce a text response, the API uses a new model, Gemini Decision 1, to evaluate predefined options in a single pass. 

 According to Google, response times range from 150 to 250 milliseconds for tested workloads, while pricing starts at $0.10 per million input tokens with no output-token charges. 

 The release comes just weeks after OpenAI launched its own Decisions API , joining TypeSafe AI and Microsoft in a growing market for models built to make specific decisions without generating text. 

 One pass, no generated text 

 The API supports a 256,000-token context window and can evaluate up to 1,000 independent questions against a single input, including multimodal content. Its responses include probabilities and confidence scores that developers can use to select between predefined options, evaluate information against specific criteria and decide how an application should proceed. 

 Google CEO Sundar Pichai described the model in a post on X as “built for closed-set choices,” while Google DeepMind product manager Min Choi and principal scientist Felix Yu characterized the API as providing “purpose-built primitives for bounded choices” in the launch announcement. 

 Where Google already uses it 

 Google is already using the model internally, including in Gemini Notebook, where real-time model and reasoning-level routing has reportedly reduced latency by up to 40%. Google Search also uses it to detect potentially adversarial behavior involving MCP tools. 

 Benchmarks come from Google 

 Google’s benchmark results show Gemini Decision 1 outperforming OpenAI’s GPT-6 Luna, although the competition with TypeSafe’s Jev 1.14 is closer. 

 Logan Kilpatrick , who leads product for Google AI Studio and the Gemini API, described it on X as “our new frontier decision model in the Gemini API.” On JevBench, Google’s model scored 92.2%, compared with 90.9% for Luna and 90% for Jev. 

 But Jev came out ahead on two of the seven shared tests and was cheaper to run, costing $0.68 for the full benchmark suite compared with $0.88 for Gemini Decision 1. Google’s model also recorded the lowest calibration error among those tested. 

 All of the benchmark figures come from Google’s own testing, and independent evaluations have yet to establish how the models compare in production. SiliconANGLE also noted that Jev is cheaper than Google’s model on a per-token basis. 

 All of the benchmark figures come from Google’s own testing, and independent evaluations have yet to establish how the models compare in production. 

 What developers actually pay 

 Developers only pay to send the shared context once, even when they’re asking multiple questions about it, although the questions themselves still count toward token usage. The API evaluates each question separately, so a workflow that needs to use one answer to decide what to ask next requires another call. 

 Gemini Decision 1 is available through Google AI Studio , with a free prototyping tier and integrations through OpenRouter , LangChain, Vercel, and LiteLLM. Support for Gemini on Google Cloud is also planned, although Google has not announced a release date. 

 Developers only pay to send the shared context once, even when they’re asking multiple questions about it… 
 
 The post Google built an AI model that can’t write a sentence — and that’s the point appeared first on The New Stack .
