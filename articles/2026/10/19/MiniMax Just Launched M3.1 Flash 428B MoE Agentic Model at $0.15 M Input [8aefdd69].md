---
id: "8aefdd69c39f65a7"
title: "MiniMax Just Launched M3.1 Flash: 428B MoE Agentic Model at $0.15/M Input"
url: "https://marktechpost.com/2026/10/19/minimax-m3-1-flash-release"
link: "https://marktechpost.com/2026/10/19/minimax-m3-1-flash-release"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-19T12:37:58Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "MiniMax has just released MiniMax M3.1 Flash on its API, priced at $0.15 per 1M input tokens . MiniMax also confirmed that Space Bunny was an earlier M3.1 Flash build. That stealth model processed over 200T tokens. For developers, the message is near-frontier agentic scores at Flash-tier cost. Model weights are due in late October, 2026. \n\n TL;DR \n\n Size: 428B total parameters, about 23B active…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Software Engineering"]
orgs: ["DeepSeek", "OpenAI", "Anthropic", "Nvidia"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 979
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# MiniMax Just Launched M3.1 Flash: 428B MoE Agentic Model at $0.15/M Input

MarkTechPost · Asif Razzaq · 2026-10-19

MiniMax has just released MiniMax M3.1 Flash on its API, priced at $0.15 per 1M input tokens . MiniMax also confirmed that Space Bunny was an earlier M3.1 Flash build. That stealth model processed over 200T tokens. For developers, the message is near-frontier agentic scores at Flash-tier cost. Model weights are due in late October, 2026. 

 TL;DR 

 Size: 428B total parameters, about 23B active (MoE); 1,000,000-token context 

 Runs on: MiniMax API, M Plan and MiniMax Code today. Self-hosting hardware not disclosed; weights arrive Oct 23 

 Performance: Near-frontier on agentic office work, mid-pack on hard coding, all MiniMax-reported 

 Best: Automation-Bench v1.0.6 at 62.2, the top score in MiniMax’s table 

 Worst: Terminal Bench 4.0 at 38.1, versus 51.8 for Opus 5 

 What is MiniMax M3.1 Flash? 

 MiniMax M3.1 Flash is a multimodal mixture-of-experts model from MiniMax. It targets coding, agentic office work and visual reasoning. MiniMax’s product page lists 428B total parameters and about 23B active. It also mentions sparse attention and a native visual encoder. 

 The model accepts text, image and video input and returns text. The context window is 1,000,000 tokens. Those parameter totals match MiniMax M3 , which ships at ~428B total and ~23B active. MiniMax has not published a technical report on what changed in the Flash variant. 

 How does reasoning work in M3.1 Flash? 

 Reasoning is always on and cannot be disabled. Developers choose from 5 effort levels: Low, Medium, High, Xhigh and Max. MiniMax recommends Max as the default. 

 Migration matters here. Requests sending thinking.type=disabled or effort=none return an error. Reasoning arrives in a separate reasoning_content field, which may be absent. Integrations that parse inline <think> tags from M3 need updating. 

 How does M3.1 Flash perform on benchmarks? 

 All scores below are MiniMax-reported. No independent replication exists yet. 

 On the CoWork set, M3.1 Flash leads Automation-Bench v1.0.6 at 62.2 . Opus 5 scores 50.3 and GPT-5.6 Sol 45.8. It ties Opus 5 on BankerToolBench at 76.2. It also tops LOCA-Bench 256K at 60.3. Agents’ Last Exam lands at 29.6. 

 Coding results are mixed. DeepSWE v1.1 scores 73.7, just above GPT-5.6 Sol at 73.0. DeepSeek-V4.1-Flash-1017 scores higher at 77.0. Terminal Bench 4.0 is the weakest result at 38.1. SWE Refactor Bench sits at 23.0, versus 31.0 for Opus 5. 

 On vision, BabyVision with tools reaches 91.0 and CharXiv RQ reaches 82.5. HLE without tools scores 43.4. 

 Spot checks hold up. The Kimi K3 model card reports DeepSWE 67.5 and BabyVision 85.7, matching MiniMax’s table. One inconsistency: MiniMax’s cost chart plots Automation-Bench max effort at 62.8, while its table says 62.2. 

 What does M3.1 Flash cost per task? 

 MiniMax frames value as cost per task, not per token. On its Automation-Bench chart, all 5 effort levels sit below $0.05 per task. Scores range from 52.8 at low effort to 62.8 at max. A full 152-task Agents’ Last Exam run cost about $111 at 29.6. On DeepSWE, DeepSeek V4.1 Flash-1017 plots both higher and cheaper at max effort. 

&

 How do you deploy MiniMax M3.1 Flash? 

 The model is live on platform.minimax.io as MiniMax-M3.1-Flash . MiniMax supports Anthropic-compatible and OpenAI-compatible access, including Chat Completions and Responses. It is also available through M Plan and the MiniMax Code desktop app . 

 Pricing is a flat $0.15 input and $0.60 output per 1M tokens. Cache reads cost $0.015 per 1M. There is no long-context surcharge. MiniMax M3 costs $0.30/$1.20 up to 512K input and doubles above that. Per token, Flash is half of M3’s standard rate. MiniMax claims 1/3 the cost of M3 but has not detailed the calculation. 

 On speed, MiniMax’s product page lists about 150 tokens per second. The announcement claims 3x the speed of M3. Weights arrive October 23; the license is not yet disclosed. For scale, M3’s MXFP8 build is about 440 GB . 

 How does M3.1 Flash compare with DeepSeek, Kimi and GLM? 

 Feature MiniMax M3.1 Flash DeepSeek V4.1 Flash Kimi K3 GLM-5.3 Total / active params 428B / ~23B ( MiniMax ) 552B / 8B prefill, 16B decode ( NVIDIA card ) 2.8T / 104B ( HF ) ~744B / ~40B, shared GLM-5 base Context 1M 1M ( DeepSeek docs ) 1,048,576 1,048,576 ( Cloudflare ) Inputs Text, image, video Text, image Text, image Text Weights / license Due Oct 23; license not disclosed Open, MIT Open, Kimi K3 License Open weights API price in / out (1M) $0.15 / $0.60 flat $0.30 / $1.20 peak; half off-peak $3.00 / $15.00 $1.40 / $4.40 Self-host hardware Not disclosed Not disclosed MXFP4 weights; vLLM, SGLang Not disclosed Automation-Bench v1.0.6* 62.2 54.8 46.7 48.8 DeepSWE v1.1* 73.7 74.2 67.5 66.9 Terminal Bench 4.0* 38.1 31.2 12.6 37.9 BabyVision (w/ tools)* 91.0 89.6 85.7 Not reported 

 *Scores from MiniMax’s comparison table . Kimi K3 DeepSWE and BabyVision match its own card. 

 What are the limitations? 

 Every benchmark is vendor-reported, and harness choice shifts results. Automation-Bench numbers do not transfer across sources. Kimi K3’s card reports 30.8 on a 600-task public subset, while MiniMax lists 46.7. 

 Opus 5 leads by 13.7 points on Terminal Bench 4.0 and 14.1 on NL2Repo-Bench. Always-on reasoning also sets a token and latency floor for simple calls. Self-hosting details remain unknown until October 23. 

 Key Takeaways 

 428B MoE with ~23B active and a 1M context. 

 $0.15/$0.60 per 1M tokens, half of M3’s per-token rate. 

 Leads Automation-Bench v1.0.6 at 62.2, MiniMax-reported. 

 Trails Opus 5 by 13.7 points on Terminal Bench 4.0. 

 Weights land Oct 23; reasoning cannot be disabled. 

 Check out the announcement , product page and API docs . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post MiniMax Just Launched M3.1 Flash: 428B MoE Agentic Model at $0.15/M Input appeared first on MarkTechPost .
