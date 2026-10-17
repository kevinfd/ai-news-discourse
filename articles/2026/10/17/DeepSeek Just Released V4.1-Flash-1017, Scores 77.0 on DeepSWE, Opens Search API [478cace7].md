---
id: "478cace71257002b"
title: "DeepSeek Just Released V4.1-Flash-1017, Scores 77.0 on DeepSWE, Opens Search API"
url: "https://marktechpost.com/2026/10/17/deepseek-just-released-v4-1-flash-1017-scores-77-0-on-deepswe-opens-search-api"
link: "https://marktechpost.com/2026/10/17/deepseek-just-released-v4-1-flash-1017-scores-77-0-on-deepswe-opens-search-api"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-17T08:53:58Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "DeepSeek has just released DeepSeek-V4.1-Flash-1017 , a new checkpoint of its V4.1-Flash model. It is live on the DeepSeek website, app and API . DeepSeek claims stronger scores, faster task completion and shorter outputs than the September V4.1-Flash release . The company calls it a Pareto improvement in performance and cost. Alongside it, DeepSeek opened its Search and Fetch APIs to every…"
tags: ["Agentic AI", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Staff"]
orgs: ["DeepSeek", "Anthropic", "OpenAI", "Hugging Face"]
topics: ["models & research", "agents & coding", "search & media", "products & launches"]
content_source: "summary"
word_count: 880
paywalled: false
image: "http://www.bing.com/th?id=ONUT.ebC504qZH19gfwPk6PGwiQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# DeepSeek Just Released V4.1-Flash-1017, Scores 77.0 on DeepSWE, Opens Search API

MarkTechPost · Asif Razzaq · 2026-10-17

DeepSeek has just released DeepSeek-V4.1-Flash-1017 , a new checkpoint of its V4.1-Flash model. It is live on the DeepSeek website, app and API . DeepSeek claims stronger scores, faster task completion and shorter outputs than the September V4.1-Flash release . The company calls it a Pareto improvement in performance and cost. Alongside it, DeepSeek opened its Search and Fetch APIs to every developer. For agent builders, that means a cheaper coding model plus a first-party web layer behind one API key. 

 TL;aDR 

 Size: 552B backbone parameters plus 196B Engram parameters. It activates 8B parameters per token in prefill and 16B in decode. Context is 1M tokens, with up to 384K output tokens. 

 Runs on: DeepSeek API as deepseek-flash . September V4.1-Flash weights (763B parameters, FP8) are MIT-licensed on Hugging Face. Hardware requirements and 1017 weights: Not disclosed. 

 Performance: Beats the previous V4.1-Flash on all 11 benchmarks DeepSeek reported, by 2.0 to 11.1 points. 

 Best: 77.0 on DeepSWE v1.1, above Claude Opus 5 (74.0) in DeepSeek’s table. 

 Worst: 42.6 on HLE without tools, versus 56.3 for Claude Opus 5. 

 What is DeepSeek-V4.1-Flash-1017? 

 DeepSeek-V4.1-Flash-1017 is an updated post-training checkpoint of DeepSeek-V4.1-Flash, served through the deepseek-flash model name. The architecture details below come from the V4.1-Flash technical report . 

 DeepSeek team states that DeepSeek-V4.1-Flash-1017 uses reinforcement learning with self-feedback for end-to-end project work. Its examples run from game creation to 3D modeling. It is tuned for DeepSeek Harness , Tencent CodeBuddy and WorkBuddy. DeepSeek recommends DeepSeek Harness v0.2.1-rc.1 or later. 

 How does the V4.1-Flash architecture work? 

 V4.1-Flash is a multimodal Mixture-of-Experts model with 40 Transformer layers. They split into a 20-layer causal encoder and a 20-layer decoder. 

 Causal Encoder-Decoder (CED): Decoder global KV is projected from the final encoder hidden states. This nearly halves prefill compute. 

 Compressed Sparse Attention 2 (CSA2): Layers run in Full, Reindex or Reuse mode. They share main KV and indexer keys across layers. 

 FP4 main KV cache: Global KV drops to 890 bytes per token, about 1/4 of V4-Flash. 

 SWA Bounded Replay: Persistent KV cache shrinks to roughly 1/8 of V4-Flash. 

 Reasoning effort: A 1 to 100 scalar. The API tiers low, high and max map to 50, 75 and 100. 

 DeepSeek-V4.1-Flash-1017 benchmarks 

 All scores below are DeepSeek’s own figures . DeepSeek ran Terminal-Bench 4.0 in Claude Code and DeepSWE in Mini-SWE-V2. ZeroBench-main uses Pass@5. 

 Benchmark V4.1-Flash-1017 V4.1-Flash Kimi K3 GLM 5.3 GPT 5.6-Sol Claude Opus 5 DeepSWE v1.1 77.0 74.2 67.5 66.9 73.0 74.0 Terminal-Bench 4.0 42.3 31.2 12.6 37.9 39.9 51.8 Automation-Bench v1.0.6 60.5 54.8 46.7 48.8 45.8 50.3 Agents’ Last Exam 35.4 31.8 27.6 28.5 26.7 28.6 Apex Bench v1.1 72.1 64.6 47.8 56.6 54.3 65.8 ProgramBench 29.1 20.3 17.5 19.0 23.0 37.0 NL2Repo-Bench 68.2 65.4 58.0 58.0 56.8 75.3 HLE (no tools) 42.6 / 44.0* 36.8 / 39.1* 43.5 42.0* 44.5 56.3 BabyVision (w/ tools) 92.5 89.6 85.7 Not disclosed 88.9 94.1 

 *Text-only HLE subset. 

 The 1017 checkpoint leads on DeepSWE, Automation-Bench, Agents’ Last Exam and Apex Bench. Claude Opus 5 still leads on Terminal-Bench 4.0, ProgramBench, NL2Repo and HLE. 

&&
 -->

 How does it compare with open-weight rivals? 

 Feature DeepSeek-V4.1-Flash-1017 Kimi K3 GLM-5.3 Total parameters 552B backbone + 196B Engram 2.8T 753B Active parameters 8B prefill / 16B decode 104B Not disclosed Context 1M 1,048,576 Not disclosed License MIT (V4.1-Flash); 1017 weights Not disclosed Kimi K3 License GLM-5.3 license Modality Text, image in; text out Text, image Text DeepSWE v1.1 77.0 67.5 66.9 Agents’ Last Exam 35.4 28.3 28.5 API price (1M input miss / output, peak) $0.30 / $1.20 Not disclosed Not disclosed 

 What are DeepSeek’s Search and Fetch APIs? 

 The Search API returns ranked web results for a query. The Fetch API returns a single page as Markdown. DeepSeek says its in-house engine serves hundreds of millions of requests daily. 

 Endpoints: POST /v1/tools/search and POST /v1/tools/fetch on api.deepseek.com . 

 Search options: 1 to 50 results, optional page content, and operators like site: , lang: , after: and before: . 

 Result fields: Each result has a 0 to 3 rerank score and a 0 to 4 authority tier. 

 Price: $0.75 per 1,000 successful requests for each endpoint. Empty results and failures are free. 

 Rate limit: 5 QPS per account for each API. 

 Free window: Server-side calls via DeepSeek Harness, Claude Code or Codex stay free until November 1, 2026. 

 Deployment and pricing 

 Call the model with deepseek-flash through OpenAI or Anthropic-format endpoints. Peak pricing is $0.30 per 1M cache-miss input tokens and $1.20 per 1M output tokens. Off-peak rates are half. 

 Key Takeaways 

 1017 scores 77.0 on DeepSWE v1.1, up from 74.2. 

 It leads Automation-Bench (60.5) and Agents’ Last Exam (35.4). 

 Claude Opus 5 still wins on HLE and Terminal-Bench 4.0. 

 Search and Fetch cost $0.75 per 1,000 calls each. 

 Agent harness calls stay free until November 1, 2026. 

 Check out the DeepSeek announcement , the Search and Fetch docs , the technical report and the model card . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post DeepSeek Just Released V4.1-Flash-1017, Scores 77.0 on DeepSWE, Opens Search API appeared first on MarkTechPost .
