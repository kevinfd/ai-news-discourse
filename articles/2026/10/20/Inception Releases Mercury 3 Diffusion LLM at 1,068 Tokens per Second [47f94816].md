---
id: "47f948160e431d3f"
title: "Inception Releases Mercury 3 Diffusion LLM at 1,068 Tokens per Second"
url: "https://marktechpost.com/2026/10/19/inception-mercury-3-diffusion-llm"
link: "https://marktechpost.com/2026/10/19/inception-mercury-3-diffusion-llm"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T03:32:43Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Jean-marc Mommessin"]
language: "en"
summary: "Inception has released Mercury 3 , the newest version of its diffusion language model. Mercury 3 is a diffusion LLM from Inception that writes answers in parallel, not token by token. Inception reports 1,068 tokens per second on NVIDIA GPUs and a 1M-token context window. On Inception’s own benchmark table, it leads GPT-6 Luna and Claude Haiku 5.5 on 8 of 12 tests. For developers building agents,…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Staff", "Technology"]
orgs: ["OpenAI", "Anthropic", "Nvidia"]
topics: ["models & research", "agents & coding", "products & launches", "chips & infrastructure"]
content_source: "summary"
word_count: 925
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Inception Releases Mercury 3 Diffusion LLM at 1,068 Tokens per Second

MarkTechPost · Jean-marc Mommessin · 2026-10-20

Inception has released Mercury 3 , the newest version of its diffusion language model. Mercury 3 is a diffusion LLM from Inception that writes answers in parallel, not token by token. Inception reports 1,068 tokens per second on NVIDIA GPUs and a 1M-token context window. On Inception’s own benchmark table, it leads GPT-6 Luna and Claude Haiku 5.5 on 8 of 12 tests. For developers building agents, voice bots and search tools, this is a speed-first model with competitive scores. 

 TL;DR 

 Size: Parameters not disclosed. Inception says it is more than 40x larger than Mercury 1. Context is 1M tokens. 

 Runs on: Inception-served NVIDIA GPUs (exact GPU not disclosed). API only, no open weights or quantized builds. 

 Performance: Leads 8 of 12 benchmarks vs GPT-6 Luna and Haiku 5.5 (self-reported, medium settings). 

 Best: SWE-Bench Atlas 51.08, about 18 points ahead of both rivals. 

 Worst: DeepSWE v1 46.31, 5.31 points behind Haiku 5.5 (51.62). 

 What is Mercury 3? 

 Mercury 3 is Inception’s fourth Mercury release, after Mercury 1, Mercury 2 and Mercury 2.5. Mercury 1 launched in 2025. Mercury 2.5 added tunable reasoning and a 260K context window, per Inception’s launch announcement . 

 1/4 Today, we’re releasing Mercury 3. Mercury 3 is by far our most powerful model and the most intelligent diffusion LLM ever released. It outperforms GPT-6 Luna and Haiku 5.5 on quality while running at 1000+ tok/sec. pic.twitter.com/TYevDl43Lm — Stefano Ermon (@StefanoErmon) October 19, 2026 

 How does a diffusion LLM work? 

 Autoregressive models write one token after another. Each new token waits for the previous one. A diffusion LLM starts from a rough draft of the full answer. It then refines every position over a few passes in parallel. 

 Fewer sequential steps means faster output on the same GPUs. The open question was whether this approach holds up as models grow larger. 

 Does diffusion scale? 

 Here Inception’s answer is yes. Mercury 3 has more than 40x the total parameters of Mercury 1 (mini). Average quality across standard benchmarks rose about 3x between those 2 models. Speed stayed above 1,000 tokens per second. 

 Inception team plots this as a quality vs size curve across 5 Mercury generations. 

 How does Mercury 3 perform on benchmarks? 

 All scores below come from Inception’s table . Every model ran at medium settings. 

 Mercury 3 posts its largest gains on instruction following and agentic coding. IFBench reaches 76.84, 15 points above GPT-6 Luna. SWE-Bench Atlas reaches 51.08, against 33.33 for Luna and 32.26 for Haiku 5.5. GPQA Diamond lands at 89.23. 

 The losses matter too. Haiku 5.5 wins DeepSWE v1 (51.62 vs 46.31) and MRCR v2 (78.40 vs 75.50). GPT-6 Luna edges ahead on AA-Omniscience-Public (46.94 vs 46.44) and AA-LCR v1.1 (78.30 vs 77.67). Long-context retrieval and longer coding tasks remain the weak spots. 

&&&

 Mercury 3 vs GPT-6 Luna vs Claude Haiku 5.5 

 Feature Mercury 3 GPT-6 Luna Claude Haiku 5.5 Developer Inception OpenAI Anthropic Generation method Diffusion (parallel refinement) Not disclosed Not disclosed Parameters Not disclosed Not disclosed Not disclosed Context window 1M 1.05M 1M Max output Not disclosed 128K 128K Input modalities Not disclosed Text, image Text, image Open weights No (API) No (API) No (API) Output speed (Inception’s measure) 1,068 tok/s ~130 tok/s ~240 tok/s Price, $/1M in / out $0.20 / $0.70 list ($0.10 / $0.35 launch) $0.10 / $0.50 (short context) $0.10 / $0.50 (prompts up to 100K) GPQA Diamond 89.23 86.36 84.51 IFBench 76.84 61.82 54.65 SWE-Bench Atlas 51.08 33.33 32.26 DeepSWE v1 46.31 37.76 51.62 MRCR v2 75.50 62.72 78.40 

 Speed and benchmark rows: Inception’s table, medium settings. Specs and prices: each vendor’s own docs. 

 What do early users report? 

 Inception quotes 4 early-access partners. These are customer statements, not independent evals. 

 TinyFish ran 50 live Mind2Web web-navigation tasks. Mercury 3 completed 50% of them. Inception says that beat GPT-6.1-Sol but gives no Sol number. 

 Octen AI reports 0.9 seconds median generation and 2.2 seconds end to end for smart-glasses search. 

 RevisionDojo says hints and marked answers return in about a second. 

 Lorikeet says Mercury 3 beat other models on latency and evals for support agents. 

 How can developers use Mercury 3? 

 Mercury 3 is live on the Inception API Platform , OpenRouter , Baseten and Vercel. The API is OpenAI compatible. The docs use the model string mercury-3 and a reasoning_effort parameter. 

 List pricing is $0.20 per 1M input and $0.70 per 1M output tokens. At launch it is 50% off: $0.10 and $0.35. Cached input is 90% off. New accounts get 100M free tokens. Enterprise plans add dedicated capacity, autoscaling and configurable data retention. 

 Inception also ships 2 siblings : 

 Mercury Voice targets time to first answer token in voice agents. 

 Mercury Decide is a classification model. 

 Key Takeaways 

 Mercury 3 is a diffusion LLM claiming 1,068 tok/s and 1M context. 

 It leads 8 of 12 vendor-run benchmarks vs GPT-6 Luna and Haiku 5.5. 

 Biggest wins: SWE-Bench Atlas 51.08 and IFBench 76.84. 

 Haiku 5.5 still wins DeepSWE v1 and MRCR v2. 

 Launch price is $0.10 / $0.35, rising to $0.20 / $0.70. 

 Check out the official launch blog , the API docs and the OpenRouter listing . Also read our earlier coverage of Drex 1.5 . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Inception Releases Mercury 3 Diffusion LLM at 1,068 Tokens per Second appeared first on MarkTechPost .
