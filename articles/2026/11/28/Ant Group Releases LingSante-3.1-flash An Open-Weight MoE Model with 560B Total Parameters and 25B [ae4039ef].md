---
id: "ae4039eff4967e39"
title: "Ant Group Releases LingSante-3.1-flash: An Open-Weight MoE Model with 560B Total Parameters and 25B Activations per Token"
url: "https://marktechpost.com/2026/11/28/ant-group-lingsante-3-1-flash-open-source-medical-ai"
link: "https://marktechpost.com/2026/11/28/ant-group-lingsante-3-1-flash-open-source-medical-ai"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-28T09:45:33Z"
published_date: "2026-11-28"
collected_at: "2026-11-28T13:03:39Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Ant Group has open-sourced LingSante , a family of medical and health AI models behind health app Afu. The flagship, LingSante-3.1-flash , is an open-weight medical AI model with 560B total parameters and 25B active per token. It ships under the MIT license with a 1M-token context window. On the new InclusionMed evaluation, it scores highest among open models. It is a self-hostable model trained…"
tags: ["Agentic AI", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Open Source", "Promote"]
orgs: ["OpenAI", "Anthropic", "Google", "Hugging Face", "DeepSeek"]
topics: ["models & research", "health & science", "agents & coding", "search & media"]
content_source: "summary"
word_count: 922
paywalled: false
image: "https://www.marktechpost.com/wp-content/uploads/2026/11/image.jpeg"
discussion_url: null
score: null
comments: null
community: null
---

# Ant Group Releases LingSante-3.1-flash: An Open-Weight MoE Model with 560B Total Parameters and 25B Activations per Token

MarkTechPost · Asif Razzaq · 2026-11-28

Ant Group has open-sourced LingSante , a family of medical and health AI models behind health app Afu. The flagship, LingSante-3.1-flash , is an open-weight medical AI model with 560B total parameters and 25B active per token. It ships under the MIT license with a 1M-token context window. On the new InclusionMed evaluation, it scores highest among open models. It is a self-hostable model trained for clinical reasoning, medical search and tool-using agents. 

 TL;DR 

 What? :It is a self-hostable model trained for clinical reasoning, medical search and tool-using agents. 

 Size: 560B total, ~25B active per token (MoE), 1M-token context. 

 Runs on: Multi-GPU servers. The reference SGLang setup uses 8x H200 or 4x GB300. An MXFP4 quantized checkpoint is available. 

 Performance: Strong on medical reasoning and medical agents. Weaker on general coding and CLI agent tasks. 

 Best: 65.72 on HealthBench Professional,the top score in the model card’s 9-model comparison 

 What is LingSante-3.1-flash? 

 LingSante-3.1-flash is a medical deep-reasoning model from Ant Group, built on the Ling-3.1-flash base model. It targets complex case analysis and professional medical agents. 

 According to Ant’s official release, Afu serves 150 million users and handles nearly 20 million health consultations daily. LingSante is the model family behind that app. 

 What is in the LingSante family? 

 Ant group opened two models first, with more weights promised in phases: 

 LingSante-3.1-flash: 560B total, ~25B active, 1M context, text-only deep reasoning. 

 LingSante-3.1-air-VL : 124B total, 5.5B active, 256K context, built on Ling-3.0-flash-VL, MIT license. 

 The research team also names 3 models not yet open. LingSante-Pulse predicts risk for more than 150 conditions. LingSante-MedGuard screens for medical safety, compliance and bioethics risks. LingSante-Live is a real-time video consultation agent already inside Afu. 

 How does the architecture work? 

 The model card describes a hybrid-linear MoE design: 

 63 KDA (linear attention) layers and 9 gated MLA layers, a 7:1 ratio 

 512 routed experts plus 1 shared expert, 8 routed experts active per token 

 Hidden size 4096, 64 attention heads, vocabulary of 157,184 

 BF16, F32 and F8_E4M3 tensor types 

 The linear-heavy attention stack is what makes a 1M-token window practical at this size. 

 How was it trained? 

 Medical and general data were mixed through pretraining, mid-training and SFT. Post-training used RL for medical reasoning, tool use, search and professional behavior. The final stage was multi-teacher on-policy distillation. 

 The research team adds 3 details: 

 Agent environments: real MCP services, mock MCP tools and world models for rare edge cases. 

 Deep search: Contribution-aware Joint RL rewards each agent by its contribution. Ant reports over 20% fewer search steps than accuracy-only multi-agent RL. 

 Professional behavior: physicians annotated reward data with a reported 99.62% agreement rate. 

 How does it perform on benchmarks? 

 All scores below are from the model card’s comparison table .  

 Where it leads the full 9-model field: 

 HealthBench Professional: 65.72 (GPT-6 Astra 64.18, Claude Opus 5.5 61.19) 

 EHR-Complex: 74.40 (GPT-6 Astra 74.20) 

 BrowseComp with context: 94.10 (Kimi-K3.1-Pro 92.10) 

 HLE text-only with tools: 72.22 single-agent, 74.87 multi-agent 

 Where it trails: 

 MedQA-USMLE: 94.50, versus 97.33 for GPT-6 Astra and Gemini 4 Argon 

 InclusionMed-DxFiles: 56.09, versus 73.40 for Gemini 4 Argon 

 On the InclusionMed Index , the model card reports an overall 45.064. That places it 5th of 23 configurations. The 4 models above it are all closed. They are Gemini 4 Argon (49.1), Claude Opus 5.5 (48.9), Claude Fable 5.1 (48.9) and GPT-6 Astra (45.1). That is the basis for the “number 1 open-source” claim. 

 How does it compare with other open models? 

 Feature LingSante-3.1-flash DeepSeek-V4.1-Flash GLM-5.3 Kimi-K3.1-Pro Total params 560B 552B backbone 753B (HF metadata) 2.8T Active params ~25B 16B decode, 8B prefill Not disclosed on card 104B Context 1M 1M 1,048,576 (config) 1M License MIT MIT GLM-5.3 license Kimi K3.1 Pro license Modality Text Text + image Text Text + image Medical tuning Yes No No No HealthBench Professional* 65.72 52.04 51.18 55.87 MedQA-USMLE* 94.50 95.13 93.09 96.15 InclusionMed-DxFiles* 56.09 53.85 52.56 59.94 BrowseComp (w. context)* 94.10 89.49 68.33 92.10 Terminal-Bench 4.0* 26.5 33.8 41.9 67.2 

 *Scores measured by Ant Group and published on the LingSante-3.1-flash model card . Specs for rivals come from each rival’s own model card. 

&&

 How do you deploy LingSante-3.1-flash? 

 Weights are on Hugging Face and ModelScope . A MXFP4 checkpoint cuts memory needs. Hosted API access runs through Computrix . 

 SGLang (recommended): image lmsysorg/sglang:dev-ling-3.1-flash, MTP speculative decoding, TP8 and EP8 on 8x H200. Use parallelism 4 on 4x GB300. See the SGLang cookbook . 

 vLLM: TP8, expert parallelism, prefix caching, 3-token MTP and ling3 parsers. 

 Sampling: temperature 1.0, top_p 0.95, top_k 20, thinking enabled. 

 Key Takeaways 

 560B MoE, ~25B active, 1M context, MIT license. 

 45.064 on InclusionMed: top open model, 5th overall. 

 Leads all 9 models on HealthBench Professional (65.72). 

 Specialized for medical tasks; trails general models on coding benchmarks. 

 Check out the model weights , technical blog , Medium post and InclusionMed paper .  You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 

 Thanks to the Ant Research team for the thought leadership / resources for this article. This article is sponsored . 
 The post Ant Group Releases LingSante-3.1-flash: An Open-Weight MoE Model with 560B Total Parameters and 25B Activations per Token appeared first on MarkTechPost .
