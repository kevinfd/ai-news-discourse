---
id: "520dec5497dfa689"
title: "Samaya AI Releases Sterling: A 3B-Active Finance Research Agent Model that Beats Claude Fable 5.1 on FrontierFinance at 11x Lower Cost"
url: "https://marktechpost.com/2026/10/30/samaya-sterling-post-trained-finance-research-model-frontierfinance"
link: "https://marktechpost.com/2026/10/30/samaya-sterling-post-trained-finance-research-model-frontierfinance"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-30T07:26:12Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Samaya AI has released Samaya Sterling , a post-trained model for agentic financial research. Sterling is built on NVIDIA’s Nemotron 3.5 Lightning , a 30B mixture-of-experts model with 3B active parameters. On Samaya’s FrontierFinance benchmark , it scores 58.9%. Claude Fable 5.1 scores 55.9%. Each Sterling question costs $0.61, against $6.89 for Fable 5.1. For developers, the takeaway is a…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Guardrail", "Harness", "Language Model", "Large Language Model", "Machine Learning"]
orgs: ["Anthropic", "Nvidia", "Hugging Face", "Thinking Machines"]
topics: ["models & research", "agents & coding", "jobs & society", "products & launches"]
content_source: "summary"
word_count: 833
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Samaya AI Releases Sterling: A 3B-Active Finance Research Agent Model that Beats Claude Fable 5.1 on FrontierFinance at 11x Lower Cost

MarkTechPost · Asif Razzaq · 2026-10-30

Samaya AI has released Samaya Sterling , a post-trained model for agentic financial research. Sterling is built on NVIDIA’s Nemotron 3.5 Lightning , a 30B mixture-of-experts model with 3B active parameters. On Samaya’s FrontierFinance benchmark , it scores 58.9%. Claude Fable 5.1 scores 55.9%. Each Sterling question costs $0.61, against $6.89 for Fable 5.1. For developers, the takeaway is a concrete recipe: co-train a small model with its harness, and it can win in a narrow domain. 

 TL;DR 

 Size: 30B total, 3B active (MoE). Base model context: up to 1M tokens. Sterling’s serving context: not disclosed. 

 Runs on: the base model fits a single H100 80GB in BF16 (256K context). Sterling’s serving hardware: not disclosed. 

 Performance: beats every high-quality system on the FrontierFinance leaderboard on quality per dollar (self-reported). 

 Best: 58.9% on FrontierFinance (60.6% in high-effort mode), vs 55.9% for Claude Fable 5.1. 

 Worst: 45.2% on the hardest third of FrontierFinance questions. 

 What is Samaya Sterling? 

 Samaya Sterling is a LoRA post-trained version of Nemotron 3.5 Lightning, tuned to work as a financial research agent. It plans research, calls finance tools, gathers evidence and hands findings to a separate report writer. According to Maithra Raghu’s X announcement , it started as a 2-person effort on agentic orchestration efficiency. 

 How does the harness support a 3B-active model? 

 Samaya team adapted its production finance harness for a small model. Detailed guidance was stripped from the system prompt and tool descriptions. Tools were merged to shorten the prompt. Two helper models manage context. A condenser shortens long tool results. A compactor summarizes the trace as it grows. A research budget caps how long the agent works. After that, the report writer answers from what was found. 

 How was Sterling trained? 

 Training used LoRA on Tinker , Thinking Machines Lab’s training API. It ran in 4 stages: 

 SFT on synthetic traces : Samaya generated 968 synthetic analyst questions. The teacher, Kimi K3, answered each twice, and an LLM judge picked the better answer. The model learned to call 37 tools with valid arguments. 

 SFT on the best of 8 strategies : Kimi K3 answered 1,819 expert-written questions using 8 research strategies. The best-graded answer per question became training data. Best-of-8 met 80% of essential rubric items, against about 66% for the single best strategy. After filtering, 1,157 questions remained. 

 Offline GRPO : GRPO scored all 8 teacher answers against each other. No new generation was needed, so each step was cheap. 

 Online GRPO : The model answered each question 8 times and learned from graded attempts. Truncated importance sampling corrected a known MoE sampler mismatch. 

 How does Sterling score on FrontierFinance? 

 FrontierFinance has 220 public queries scored against expert-written rubrics. The grader uses a 3-model judge panel. Samaya team states that no benchmark question was used in training. Checkpoints were chosen on 100 internal validation questions. 

 Sterling scores 58.9% at $0.61 and 282 s per question. Fable 5.1 scores 55.9% at $6.89 and 268 s. Samaya’s own high-effort system scores 2.9 points lower at $1.81. 

 Every stage added quality: 42.5% (base), 51.4%, 54.8%, 57.5%, then 58.9%. Median tool calls rose from 3 to 17. In high-effort mode, Sterling reaches 60.6% at $1.83 and 372 s. On the hardest third, it rose from 31.8% to 45.2%. 

 The model itself costs $0.04 per question. Tools and helper models make up the rest of the $0.61. 

 &&

 How does Sterling compare? 

 Feature Samaya Sterling Claude Fable 5.1 Samaya System, high effort Nemotron 3.5 Lightning base Total / active params 30B / 3B Not disclosed Not disclosed 30B / 3B Context Not disclosed 1M Not disclosed Up to 1M License / access No public weights or API announced Proprietary API Samaya platform OpenMDW-1.1, open weights FrontierFinance score 58.9% (60.6% high effort) 55.9% 56.0% (58.9 minus 2.9 pp) 42.5% Cost per question $0.61 ($1.83 high effort) $6.89 $1.81 Not disclosed Latency per question 282 s (372 s high effort) 268 s 278 s Not disclosed Token pricing Not disclosed $10 / $50 per MTok Not disclosed Not disclosed 

 FrontierFinance figures for all columns come from the Samaya blog and are self-reported. 

 Key Takeaways 

 Sterling scores 58.9% on FrontierFinance, 3.0 points above Claude Fable 5.1. 

 Cost per question drops 11x: $0.61 vs $6.89. 

 3B active parameters, trained with 2 SFT and 2 GRPO stages. 

 Harness and model co-training drive the gains. 

 All results are self-reported on Samaya’s own benchmark. 

 Check out the technical blog , the FrontierFinance benchmark , the dataset and the grader repo . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Samaya AI Releases Sterling: A 3B-Active Finance Research Agent Model that Beats Claude Fable 5.1 on FrontierFinance at 11x Lower Cost appeared first on MarkTechPost .
