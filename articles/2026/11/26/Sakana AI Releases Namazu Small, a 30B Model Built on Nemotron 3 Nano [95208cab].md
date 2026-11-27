---
id: "95208cab72613384"
title: "Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano"
url: "https://marktechpost.com/2026/11/26/sakana-ai-namazu-small-30b-nemotron-3-nano"
link: "https://marktechpost.com/2026/11/26/sakana-ai-namazu-small-30b-nemotron-3-nano"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-26T22:06:40Z"
published_date: "2026-11-26"
collected_at: "2026-11-27T13:04:05Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Sakana AI has announced Sakana Namazu Small , a 30-billion-parameter reasoning model built on NVIDIA Nemotron 3 Nano. The Japan-based lab ran continued pretraining and post-training in-house, starting from Nemotron 3 Nano’s pretrained base. Sakana AI team states that the result beats NVIDIA’s 120B Nemotron 3 Super on its 25-benchmark average. \n\n TL;DR \n\n Size: 30B total parameters, 3B active…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Context Engineering", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Staff", "Tech News"]
orgs: ["Nvidia", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "products & launches", "business & funding"]
content_source: "summary"
word_count: 832
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano

MarkTechPost · Michal Sutter · 2026-11-26

Sakana AI has announced Sakana Namazu Small , a 30-billion-parameter reasoning model built on NVIDIA Nemotron 3 Nano. The Japan-based lab ran continued pretraining and post-training in-house, starting from Nemotron 3 Nano’s pretrained base. Sakana AI team states that the result beats NVIDIA’s 120B Nemotron 3 Super on its 25-benchmark average. 

 TL;DR 

 Size: 30B total parameters, 3B active (labeled 30B-A3B in Sakana’s chart). Context length: Not disclosed. 

 Runs on: Hardware not disclosed. Sakana says it is small enough for your own environment. The Nemotron 3 Nano base was designed for DGX Spark, H100 and B200 GPUs. 

 Performance: 60.1 average on 25 benchmarks, ahead of Nemotron 3 Super (56.2) and Nano (50.2). Self-reported. 

 Best: BrowseComp 73.5, about 2x Nemotron 3 Super’s 36.1. 

 Worst: SimpleQA Verified 6.8, below Nemotron 3 Nano (9.1) and Super (18.1). 

 What is Sakana Namazu Small? 

 Sakana Namazu Small is a 30B-A3B reasoning model from Sakana AI, tuned for web research and long-document QA. “Sakana Namazu” names models Sakana builds on open models and finishes with its own post-training. The larger Sakana Namazu is based on Kimi K2.6. Namazu Small is the compact member of that family. 

 Sakana AI targets 3 kinds of work: everyday conversation, research with web search, and reading long documents. It was developed as a reasoning model. It organizes the information it needs and reasons step by step toward an answer. 

 How was Namazu Small trained? 

 Sakana started from the pretrained base of Nemotron 3 Nano, not NVIDIA’s post-trained release. It then applied continued pretraining and post-training techniques built for this release. These sit on top of methods Sakana developed for the original Sakana Namazu. 

 The base architecture matters for deployment. Nemotron 3 Nano is a hybrid Mamba-Transformer mixture-of-experts model. NVIDIA lists it at 30B total and 3B active parameters , with context up to 1M tokens. 

 How does Namazu Small perform on benchmarks? 

 Sakana compared it against 2 NVIDIA models, both post-trained by NVIDIA. These are Nemotron 3 Nano (30B-A3B) and Nemotron 3 Super (120B-A12B). The suite spans 25 benchmarks in 3 groups. All scores are self-reported by Sakana . 

 Benchmark group Namazu Small (30B-A3B) Nemotron 3 Super (120B-A12B) Nemotron 3 Nano (30B-A3B) Overall (25 benchmarks) 60.1 56.2 50.2 Web search (9) 59.9 54.6 49.3 Context grounding and instruction following (8) 67.1 56.4 53.9 Knowledge (8) 53.2 57.8 47.6 

 Where does it win? 

 Web research is the standout. On BrowseComp , Namazu Small scores 73.5 versus 36.1 for Super and 29.3 for Nano. On DeepSearchQA it reaches 84.3, against 65.4 for Super. 

 Grounded long-document answering also jumps. LLM-jp LongBench rises to 86.0, versus 67.0 for the Nano baseline. FaithEval reaches 78.3 versus 59.1 for Super. LongBench-Cite hits 80.2 and ALCE reaches 60.2, both citation-focused tasks. 

 Where does it fall short? 

 Closed-book knowledge is the weak spot. On SimpleQA Verified it scores 6.8, below Super (18.1) and Nano (9.1). Japanese SimpleQA lands at 8.0, versus 24.9 for Super. HealthBench drops to 40.6, under Nano’s 47.5. Sakana itself says tasks using only internal knowledge did not improve much. 

 Per benchmark, Namazu Small beats Super on 13 of 25 tests. It beats Nano on 22 of 25. 

&&

 How does it compare with Nemotron 3 Nano and Super? 

 Feature Sakana Namazu Small NVIDIA Nemotron 3 Nano NVIDIA Nemotron 3 Super Total parameters 30B 30B 120B Active parameters 3B (A3B per Sakana chart) 3B 12B Architecture Built on Nemotron 3 Nano base Hybrid Mamba-Transformer MoE LatentMoE: Mamba-2 + MoE + attention, with MTP Context length Not disclosed Up to 1M tokens Up to 1M tokens Reasoning Yes (reasoning model) Yes (reasoning and non-reasoning) Yes (configurable on/off) License Not disclosed NVIDIA Nemotron Open Model License NVIDIA Nemotron Open Model License Weights Not released; on-prem details due Dec 2026 Open on Hugging Face Open on Hugging Face Hardware Not disclosed Designed for DGX Spark, H100, B200 Min 1x B200 or 1x DGX Spark (NVFP4) Overall avg, Sakana 25-benchmark suite 60.1 50.2 56.2 BrowseComp (Sakana eval) 73.5 29.3 36.1 LLM-jp LongBench (Sakana eval) 86.0 67.0 60.0 SimpleQA Verified (Sakana eval) 6.8 9.1 18.1 Pricing Not disclosed Open weights Open weights 

 Key Takeaways 

 30B-A3B reasoning model on the Nemotron 3 Nano base, trained in-house. 

 60.1 average on 25 benchmarks, ahead of the 120B Super’s 56.2. 

 BrowseComp 73.5, about 2x Nemotron 3 Super’s 36.1. 

 Closed-book recall lags: SimpleQA Verified 6.8. 

 Check out the official announcement , the Nemotron 3 Nano technical report and the Nemotron 3 Super model card . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano appeared first on MarkTechPost .
