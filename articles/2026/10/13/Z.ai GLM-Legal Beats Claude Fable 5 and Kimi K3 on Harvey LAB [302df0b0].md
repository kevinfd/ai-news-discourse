---
id: "302df0b0c08b99b5"
title: "Z.ai GLM-Legal Beats Claude Fable 5 and Kimi K3 on Harvey LAB"
url: "https://marktechpost.com/2026/10/13/zai-glm-legal-harvey-lab-legal-ai-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-13T08:19:54Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Z.ai just released GLM-Legal . GLM-Legal is a legal AI model from Z.ai, built on GLM-5.3-Flash and trained for agentic legal work. It targets contract review, evidence analysis and compliance research. The key result is a 19.2% all-pass rate on Harvey’s Legal Agent Benchmark (LAB) . That is nearly 3x its base model’s 6.7%. For developers, the catch is access: the API is application-only for now.…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Software Engineering"]
orgs: ["Anthropic", "OpenAI", "Hugging Face", "Google", "Meta", "China"]
topics: ["models & research", "agents & coding", "products & launches", "policy & regulation"]
content_source: "summary"
word_count: 914
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Z.ai GLM-Legal Beats Claude Fable 5 and Kimi K3 on Harvey LAB

MarkTechPost · Michal Sutter · 2026-10-13

Z.ai just released GLM-Legal . GLM-Legal is a legal AI model from Z.ai, built on GLM-5.3-Flash and trained for agentic legal work. It targets contract review, evidence analysis and compliance research. The key result is a 19.2% all-pass rate on Harvey’s Legal Agent Benchmark (LAB) . That is nearly 3x its base model’s 6.7%. For developers, the catch is access: the API is application-only for now. 

 TL;DR 

 Size: Built on GLM-5.3-Flash, a 320B-total, 18B-active MoE with a 1M-token context and 128K max output. Z.ai lists no separate GLM-Legal parameter count. 

 Runs on: Z.ai’s hosted API only, by application. No public weights. The base model self-hosts on multi-GPU servers via vLLM or SGLang, with FP8 weights. 

 Performance: Top-10 on Harvey LAB at a fraction of frontier cost. Within 2.3 points of the LegalBench leader. 

 Best: 19.17% Harvey LAB task pass rate, #7 of 79 on Vals AI, at $0.15 per test. 

 Worst: 41.83% on Vals AI’s Legal Research Bench, below its own base model (45.19%). 

 Bottom line: 
 
 Best: frontier-class legal agent scores at about 1/128 the cost of Claude Fable 5. 

 Worst: gated beta with no price, no weights and slow runs (1h12m per task). 

 What is GLM-Legal? 

 GLM-Legal is a domain-specialized version of GLM-5.3-Flash for law firms, in-house counsel and compliance teams. The base is Z.ai’s first natively multimodal GLM-5 model . It has 320B total parameters with 18B active. It mixes sparse and linear attention to cut long-context serving cost. It reads text, images, video and files, and outputs text. 

 How was GLM-Legal trained? 

 Training ran in 2 stages: 

 Mid-training on expanded legal corpora, to strengthen reasoning from facts to rules to conclusions. 

 Post-training with reinforcement learning across tens of thousands of legal task environments . 

 The Z.ai team also describes the agent harness co-evolving with the model during post-training. Edge cases in training exposed harness bottlenecks. Harness fixes then exposed the model to more realistic constraints. 

 How does GLM-Legal score on Harvey’s Legal Agent Benchmark? 

 Harvey LAB is an open-source benchmark of 1,250 tasks across 24 practice areas . Over 75,000 expert-written rubric criteria grade the work. A task passes only if every criterion passes. Harvey calls this all-pass grading. 

 Vals AI runs the held-out set with 2 LLM judges and internet disabled . Agents get file tools plus docx , pptx and xlsx skills. 

 On that leaderboard, GLM-Legal scores 19.17% and ranks #7 of 79. Its base, GLM-5.3-Flash, scores 6.67%. The 12.5-point lift is the core claim, and an independent evaluator reproduced it. 

 Z.ai’s launch chart shows GLM-Legal ahead of Kimi K3 (12.92%), Claude Fable 5 (11.25%) and GPT-6 Astra (5.42%). Those figures match Vals AI. The chart omits 6 models ranked higher, led by Muse Spark 1.2 at 25.42%. 

 GLM-Legal also passes 92.5% of individual criteria. Top models sit near 90% to 95% on that measure. 

 Does GLM-Legal match frontier models on LegalBench? 

 Roughly. Z.ai claims parity on LegalBench and the Chinese-focused PLawBench without publishing numbers. Vals AI scores GLM-Legal at 86.23% on LegalBench . Claude Fable 5 leads at 88.56% . Kimi K3 scores 86.21% . 

&&&

 How does GLM-Legal compare with Kimi K3, Claude Fable 5 and GPT-6 Astra? 

 GLM-Legal GLM-5.3-Flash (base) Kimi K3 Claude Fable 5 GPT-6 Astra Developer Z.ai Z.ai Moonshot AI Anthropic OpenAI Total / active params Built on 320B / 18B base 320B / 18B 2.8T / 104B Not disclosed Not disclosed Context window 1M 1M 1M 1M 1M Weights / license No public weights Open, MIT Open, Kimi K3 License Proprietary Proprietary Harvey LAB (task pass) 19.17% 6.67% 12.92% 11.25% 5.42% LegalBench 86.23% 83.93% 86.21% 88.56% Not listed by Vals Legal Research Bench 41.83% 45.19% 46.15% 49.52% 39.42% Cost per Harvey LAB test $0.15 $0.57 $3.83 $19.23 $26.16 Avg Harvey LAB duration 1h12m 52m17s 13m58s 26m53s 24m49s API price (in / out, per 1M tokens) Not published $0.15 / $0.50 $3 / $15 $10 / $50 $10 / $50 Access API by application API, Hugging Face API, Hugging Face API API 

 All benchmark scores, costs and durations are from Vals AI’s runs as of October 12, 2026. Vals ran both GLM models at $0.075 / $0.25 per 1M tokens. 

 How can developers access GLM-Legal? 

 Law firms, legal-tech companies and in-house teams can apply for API access . Z.ai has published no price. No GLM-Legal repository exists on Hugging Face as of October 13, 2026. Z.ai says GLM-Legal will come to AutoClaw , its desktop agent app, but gave no date. 

 The base model is available today at $0.15 / $0.50 per 1M tokens . Teams can prototype pipelines on it, then swap the model ID later. 

 Key Takeaways 

 GLM-Legal scores 19.17% on Harvey LAB, up from 6.67% for its base. 

 It ranks #7 of 79 on Vals AI, behind 6 Meta and Google models. 

 It costs $0.15 per Harvey LAB test, versus $19.23 for Claude Fable 5. 

 Legal Research Bench dropped 3.36 points versus GLM-5.3-Flash. 

 Access is application-only, with no published price or weights. 

 Check out the Z.ai tech blog , the Vals AI Harvey LAB leaderboard and the GLM-5.3-Flash model card . Apply for API access here .. All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Z.ai GLM-Legal Beats Claude Fable 5 and Kimi K3 on Harvey LAB appeared first on MarkTechPost .
