---
id: "fe3249232feb1763"
title: "Baseten Releases joey-1, a 2B Decision Model at $0.01 per 1M Tokens"
url: "https://marktechpost.com/2026/10/29/baseten-joey-1-2b-decision-model"
link: "https://marktechpost.com/2026/10/29/baseten-joey-1-2b-decision-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T21:20:29Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Baseten has released joey-1 , a 2B model from its in-house research lab, Base Labs. The joey-1 decision model returns a label and a calibrated probability instead of generated text. It targets high-volume routing, classification and guardrail checks. Baseten prices it at $0.01 per million input tokens , with open weights on Hugging Face under MIT. \n\n TL;DR \n\n Size: 2B parameters, post-trained…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Decision Models", "Editors Pick", "For Devs", "Language Model", "New Releases", "Open Source", "Staff"]
orgs: ["Hugging Face", "Perplexity"]
topics: ["models & research", "chips & infrastructure", "safety & ethics", "business & funding"]
content_source: "summary"
word_count: 982
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Baseten Releases joey-1, a 2B Decision Model at $0.01 per 1M Tokens

MarkTechPost · Asif Razzaq · 2026-10-29

Baseten has released joey-1 , a 2B model from its in-house research lab, Base Labs. The joey-1 decision model returns a label and a calibrated probability instead of generated text. It targets high-volume routing, classification and guardrail checks. Baseten prices it at $0.01 per million input tokens , with open weights on Hugging Face under MIT. 

 TL;DR 

 Size: 2B parameters, post-trained from Qwen3.5-2B. 16,384-token max sequence (Baseten says 262k on dedicated deployments). 

 Runs on: Baseten Model APIs, or self-hosted on 1 CUDA GPU (VRAM not disclosed). No official quantized builds listed. 

 Performance: Top model under 4B on the Jev Decision Index 0.4 public split, per Baseten. 

 Best: 63.30 on Jev Decision Index 0.4 (public split), ranked #37 of 230 models. 

 Worst: Trails its 9B sibling elephant-1 by 8.94 points on the same split (63.30 vs 72.24). 

 Bottom line: Best: 20 ms P50 decisions for $0.01 per 1M tokens. Worst: less general knowledge than its larger siblings. 

 What is joey-1? 

 joey-1 is a 2B decision model from Baseten’s Base Labs that answers typed questions in 1 forward pass. You send a state (text or images) and 1 or more questions. The model returns a probability for every option of every question. It does not write free-form text that your application must parse. 

 It supports 3 question types: 

 choice: pick 1 named option, such as which team owns a ticket. 

 yes/no ( noul in the API): returns the probability of yes. 

 score: ordered levels, lowest first, such as urgency. 

 joey-1 is the third member of a family. Baseten shipped mammoth-1 (27B) and elephant-1 (9B) last week. All 3 share training data and the /v1/systemone API, so switching is a 1-line change. 

 How does joey-1 work? 

 Base Labs post-trained Qwen3.5-2B with a full fine-tune of the language model. The vision encoder stays frozen. Full-attention layers use a block-bidirectional mask. All questions are answered from 1 shared-prefix prefill, so extra questions add little cost. 

 Training details from the model card : 

 Data: 6.21M decision examples. Mix: 58.3% core decision skills, 16.1% safety, 16.1% judging and expert domains, 9.5% public data. 

 Objective: cross-entropy plus a Brier calibration term, with a trained “I don’t know” option. 

 Recipe: 1 epoch, 43,390 steps, peak learning rate 1e-5, bf16. 

 Hardware: 2 nodes of 8 H100 GPUs. 

 Calibration lets you set a confidence threshold. Uncertain answers can escalate to elephant-1, mammoth-1 or a human. 

&&

 How fast and cheap is joey-1? 

 Baseten reports a P50 end-to-end latency of 20 ms for an average 2,000-token request. That is about 2.5x faster than elephant-1 (49 ms). The blog’s TL;DR also claims 5x faster than comparable decision models, without naming them. 

 Model APIs charge $0.01 per 1M input tokens; output and cached input are listed at $0.00. elephant-1 costs $0.035 and mammoth-1 costs $0.10. 

 Baseten’s example: 10M support tickets a month at about 500 tokens each is 5B tokens. That is about $50 on joey-1, versus $500 on mammoth-1. 

 How does joey-1 score on benchmarks? 

 All scores below are self-reported on Baseten’s model card . 

 On the Jev Decision Index 0.4 public split, joey-1 scores 63.30. That ranks #37 of 230 models and is the top score under 4B. The Jev Decision Index is a community leaderboard on Hugging Face. 

 On the same split, Cloudflare’s 27B Clef scores 61.71 and Jev 1.14 scores 60.70. 

 joey-1 trails elephant-1 in every area. It beats Jev 1.14 in 4 of 5 areas, including language, tools and retrieval. 

 On Baseten’s replica of the Artificial Analysis Decision Index, joey-1 scores 62.9, versus 65.9 for mammoth-1. 

 joey-1 vs. other small decision models 

 Feature joey-1 elephant-1 Perplexity Decider Flash v1.2 Cloudflare Clef-Flash Developer Baseten (Base Labs) Baseten (Base Labs) Perplexity Cloudflare Parameters 2B 9B 4B 9B Base model Qwen3.5-2B Qwen3.5-9B Qwen3.5-4B Qwen3.5-9B License MIT MIT Apache-2.0 Apache-2.0 Inputs Text, images Text, images Text, images Text, JSON, images, video Max context 16,384 (Model APIs); 262k on dedicated 16k (Model APIs); 262k on dedicated 262,144 (trained to about 32k) 16,384 default API price per 1M input tokens $0.01 $0.035 $0.01 Not disclosed Jev Decision Index 0.4 (public)* 63.30 72.24 60.06 Not disclosed Reported latency** 20 ms P50 49 ms P50 Not disclosed 38.8 ms median Self-host hardware 1 CUDA GPU Not disclosed About 9 GiB BF16 weights on a CUDA GPU Tested on 1 H200 Weights access Public Public Private repo, token required Public 

 *Jev 0.4 scores for all models come from Baseten’s joey-1 model card . **Latency figures are not comparable. Baseten measures end-to-end on its platform; Cloudflare reports its own Decision Index 0.2.1 run. 

 How do you deploy joey-1? 

 Model APIs: call decision-models/baseten-joey-2b-latest at /v1/systemone . Zero data retention is on by default. 

 Dedicated deployments: Baseten says these unlock 262k context, fine-tuned weights and co-location with LLM workloads. 

 Self-hosted: download from Hugging Face and run setup.sh . It needs 1 CUDA GPU and a PyTorch 2.8 / CUDA 12.8 image. 

 You can fine-tune joey-1 on Baseten Training Jobs using the fine-tuning cookbook . joey-1 is also listed on OpenRouter at $0.01 per 1M input tokens. 

 Key Takeaways 

 joey-1 returns labels plus calibrated probabilities, not text. 

 Baseten reports 20 ms P50 latency at $0.01 per 1M input tokens. 

 63.30 on Jev Decision Index 0.4 public: top model under 4B. 

 Trails elephant-1 by 8.94 points; best as a first-line router. 

 MIT weights on Hugging Face; self-host on 1 CUDA GPU. 

 Check out the blog post , model card , model library page and fine-tuning cookbook . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Baseten Releases joey-1, a 2B Decision Model at $0.01 per 1M Tokens appeared first on MarkTechPost .
