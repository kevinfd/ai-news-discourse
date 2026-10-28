---
id: "dd93e1b8b3768bbf"
title: "Mirendil Launches Fern 0.1, Its First Model, With 10M-Token Context"
url: "https://marktechpost.com/2026/10/27/mirendil-fern-10m-token-context-model"
link: "https://marktechpost.com/2026/10/27/mirendil-fern-10m-token-context-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T12:57:46Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Mirendil has released Fern , its first AI model. Mirendil Fern is a from-scratch coding model with a context window of up to 10M tokens. Mirendil explains how that equals about 23 MB of code, or roughly half a million lines. That is a codebase on the scale of Megatron-LM, held in context at once. Fern 0.1 is the first version, built from Mirendil-Base after a short round of post-training. For…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Staff", "Tech News"]
orgs: ["Anthropic", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches", "business & funding"]
content_source: "summary"
word_count: 906
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Mirendil Launches Fern 0.1, Its First Model, With 10M-Token Context

MarkTechPost · Michal Sutter · 2026-10-27

Mirendil has released Fern , its first AI model. Mirendil Fern is a from-scratch coding model with a context window of up to 10M tokens. Mirendil explains how that equals about 23 MB of code, or roughly half a million lines. That is a codebase on the scale of Megatron-LM, held in context at once. Fern 0.1 is the first version, built from Mirendil-Base after a short round of post-training. For developers, its like, you load a whole repo, a full training log or days of agent traces at once. 

 TL;DR 

 Size: 0.1 to 0.5T parameters (exact count and active params not disclosed); context up to 10M tokens. 

 Runs on: Hosted early access only; no open weights or quantized builds announced. 

 Performance: Strong long-context retrieval, mid-pack agentic coding versus open-weight models, well behind frontier models. 

 Best: 100% on RULER single-needle retrieval at every length from 32K to 10M tokens (base model). 

 Worst: 6.1% on Terminal Bench 4.0, versus 66.4% for Claude Opus 5.5 in Mirendil’s own table. 

 What is Mirendil Fern? 

 Fern is a language model from Mirendil , an AI R&D lab. 

 Fern is aimed at AI R&D work, not general chat. Mirendil lists 6 target uses: 

 Working across larger codebases 

 Agentic coding that runs commands until tests pass 

 Research code: training loops, data pipelines and evaluations 

 Debugging training runs from long logs and stack traces 

 Reading full agent or training traces end to end 

 Auditing pretraining shards for duplicates, contamination and junk 

 How was Fern built? 

 Fern sits on Mirendil-Base , which Mirendil says one researcher pretrained in 3.5 months. Total compute was under $10M, including experiments, agent token spend and data processing. AI agents wrote over 99% of the code. The researcher chose what to try and when to intervene. 

 Training data came only from public sources: GitHub, public code, web pages and public datasets. Mirendil says it used no distillation, no synthetic data and no licensed data. The code was written from scratch on PyTorch and JAX. 

 Fern is the smallest of 3 planned models. Mirendil-Base-Large (0.5 to 2T parameters) is over 80% through pretraining. Mirendil-Base-XL (2 to 10T) is over 20% through. 

 Does longer context actually help? 

 Mirendil tested next-token prediction on its own repositories, concatenated into a 42.9 MB stream. It measured cross-entropy in bits per byte, where lower is better. Window sizes here are measured in bytes, not tokens. 

 Fern’s loss fell from 0.246 at a 32K-byte window to 0.155 at 16M and 23M bytes. The other models were scored up to about 1M tokens, their advertised limit. At a 1M-byte window, Kimi-K3 scored 0.140 and Fern 0.165. So Fern is not the best predictor at equal context. Its advantage is that the curve keeps going past where others stop. 

 How does Fern score on RULER? 

 RULER is a standard long-context benchmark. Mirendil ran 5 RULER tasks on Mirendil-Base, the pre-post-training model. It used greedy decoding, thinking off and exact string matching. 

 RULER task 32K 1M 4M 10M Single needle 100 100 100 100 Multi-key retrieval 100 98 98 90 Multi-key, all needles 100 100 100 100 Variable tracking 100 95 75 100 Multi-hop QA (HotpotQA) 65 65 60 45 

 Retrieval holds up well. Multi-hop reasoning drops to 45% at 10M. Each 10M cell uses only 20 examples, versus 100 elsewhere. Mirendil says broader long-context results are coming. 

&&

 How does Fern 0.1 do on agentic benchmarks? 

 Mirendil compared Fern 0.1 with open-weight and frontier models. Scores for other models come from model cards, leaderboards or Mirendil’s own runs. 

 Benchmark (pass %) Fern 0.1 Kimi-K3 GLM-5.3 Claude Opus 5.5 DeepSWE v1.1 44.2 67.3 66.9 74.2 Terminal Bench 4.0 6.1 12.6 41.9 66.4 SWE Atlas QnA 53.2 66.1 59.4 66.4 SWE-Pro v2 Hard 76.5 88.2 84.3 100.0 SWE-Bench Verified 73.4 93.4 95.4 98.2 

 Fern 0.1 beats Inkling and Nemotron 3 Ultra on 4 of 5 tests. It ties Beam on SWE-Pro v2 Hard at 76.5. It trails Beam on SWE-Bench Verified, 73.4 versus 81.6. Every frontier and large open model in the table leads it. 

 How does Fern compare with similar models? 

 Feature Fern 0.1 Kimi-K3 GLM-5.3 Developer Mirendil Moonshot AI Z.ai Total params 0.1 to 0.5T 2.8T 753B Active params Not disclosed 104B ~40B Context Up to 10M tokens 1,048,576 tokens 1,048,576 tokens Input Text, code Text, image, video Text License Not disclosed Kimi K3 License GLM-5.3 License Weights Not released Open Open Access Early access request Open weights, APIs Open weights, APIs SWE-Bench Verified* 73.4 93.4 95.4 Bits per byte at 1M bytes* 0.165 0.140 0.170 

 *Figures from Mirendil’s announcement charts. 

 Key Takeaways 

 Fern 0.1 supports up to 10M tokens, about 23 MB of code. 

 Bits per byte keeps falling to 0.155 at a 23M-byte window. 

 RULER single needle stays at 100% from 32K to 10M tokens. 

 Agentic coding lags: 6.1% on Terminal Bench 4.0. 

 Base model built by 1 researcher plus agents for under $10M. 

 Check out the Fern announcement , the Mirendil-Base pretraining post , and request early access . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Mirendil Launches Fern 0.1, Its First Model, With 10M-Token Context appeared first on MarkTechPost .
