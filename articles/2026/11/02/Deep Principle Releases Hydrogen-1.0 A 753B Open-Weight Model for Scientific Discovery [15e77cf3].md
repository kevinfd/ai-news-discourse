---
id: "15e77cf34f39a760"
title: "Deep Principle Releases Hydrogen-1.0: A 753B Open-Weight Model for Scientific Discovery"
url: "https://marktechpost.com/2026/11/02/deep-principle-hydrogen-1-0-open-weight-scientific-model"
link: "https://marktechpost.com/2026/11/02/deep-principle-hydrogen-1-0-open-weight-scientific-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-02T18:41:41Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Deep Principle has released Hydrogen-1.0 , an open-weight scientific model for chemistry, materials science and life sciences. It is built by post-training Z.ai’s GLM-5.3 on domain data, laboratory records and agent discovery trajectories. For developers, it offers open weights that report a FrontierScience-Research win over GPT-6-Astra. The weights ship under the MIT License. \n\n TL;DR \n\n Size:…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Open Source", "Staff"]
orgs: ["OpenAI", "Nvidia", "AMD", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "agents & coding", "health & science"]
content_source: "summary"
word_count: 845
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Deep Principle Releases Hydrogen-1.0: A 753B Open-Weight Model for Scientific Discovery

MarkTechPost · Asif Razzaq · 2026-11-02

Deep Principle has released Hydrogen-1.0 , an open-weight scientific model for chemistry, materials science and life sciences. It is built by post-training Z.ai’s GLM-5.3 on domain data, laboratory records and agent discovery trajectories. For developers, it offers open weights that report a FrontierScience-Research win over GPT-6-Astra. The weights ship under the MIT License. 

 TL;DR 

 Size: 753B parameters (MoE, ~40B active per the GLM-5.3 base), 1M-token context, 128K max output. 

 Runs on: 8 GPUs with SGLang (tested); NVFP4 for NVIDIA B200/B300, MXFP4 for AMD MI350X/MI355X. 

 Performance: Beats GPT-6-Astra on FrontierScience-Research; roughly matches Kimi-K3 on GPQA-Diamond. 

 Best: 38.3% on FrontierScience-Research vs 33.3% for GPT-6-Astra (self-reported). 

 Worst: Trails GPT-6-Astra (max thinking) by 3.33 points on NMR structure elucidation. 

 What is Hydrogen-1.0? 

 Hydrogen-1.0 is a scientific research assistant model from Deep Principle, a Hangzhou-based AI-for-materials company. The model card describes it as a GLM-5.3 derivative for scientific problem solving. It targets question framing, experiment planning, results analysis and open-ended discovery. Deep Principle team states that proprietary models produced recent AI science results, but their discovery capabilities are not open. Hydrogen-1.0 is its attempt at a reproducible, inspectable alternative. 

 How was Hydrogen-1.0 trained? 

 The pipeline combines supervised fine-tuning (SFT) with reinforcement learning (RL). Data comes from 4 sources: 

 Domain knowledge: chemistry, materials science and life sciences data. 

 Research scenarios: task-specific feedback from Deep Principle scientists. 

 Laboratory records: full-cycle electronic lab notebook records captured through Mira . 

 Discovery trajectories: sequences of choices and feedback, including failed attempts. 

 Infrastructure builds on Megatron and SGLang across NVIDIA CUDA and AMD ROCm. The team keeps dynamic sparse attention causal across context-parallel shards. Muon optimizer state is moved between CPU, GPU and disk per backend. RL uses resumable rollouts, and each token keeps its original behavior log-probability for importance correction. A layout adapter converts training checkpoints into BF16 and 128×128 blockwise FP8 inference weights. Full datasets and recipes are not released. 

 How does Hydrogen-1.0 perform on benchmarks? 

 On public benchmarks, Deep Principle reports Hydrogen-1.0 outperforms GPT-6-Astra on FrontierScience-Research. The tweet thread from one of the founders’ report 93.0% on GPQA-Diamond. That improves on GLM-5.3 and roughly matches Kimi-K3, per the blog. 

 Internal research-task evals compare it with GPT-6-Astra at maximum thinking: 

 Scientific computing: Hydrogen-1.0 leads by 5.13 percentage points. 

 Forward reaction prediction: Hydrogen-1.0 leads by 4.76 percentage points. 

 NMR structure elucidation: GPT-6-Astra leads by 3.33 points. 

 In transition metal complex design, models chased a larger HOMO-LUMO gap over 5 rounds. By round 5, Hydrogen-1.0 reached a mean best-so-far gap of 4.318 eV. GPT-6-Astra reached 3.689 eV and Kimi-K3 reached 3.353 eV. On 117 experiment-planning questions, Hydrogen-1.0 scored above Kimi-K3. GPT-6-Astra and Opus-5.5 were excluded after refusing more than 50% of requests. 

&

 What can it do in a real lab workflow? 

 The technical post shows 4 demos . Hydrogen-1.0 writes Python to build a polyethylene melt and runs GROMACS. It detects a topology error, repairs it, and analyzes the corrected 40 ns trajectory. It grows an Ireland-Claisen reaction network of 27 structures through 30 plausible reactions. It ranks 7 candidate monoformylation products of 2-bromonaphthalene from a 1H NMR trace. It also writes a JSON protocol for a 12-vial Suzuki coupling study. A virtual lab compilation step catches an aspiration without a fresh tip before execution. 

 How do you deploy Hydrogen-1.0? 

 Weights are on Hugging Face and ModelScope . Deep Principle team tested BF16 serving with SGLang on 8 GPUs using tensor parallelism of 8. NVFP4 targets NVIDIA B200 and B300. MXFP4 targets AMD Instinct MI350X and MI355X. The server exposes an OpenAI-compatible API with a reasoning_effort setting. 

 Hydrogen-1.0 vs GLM-5.3, Kimi K3 and GPT-6-Astra 

 Feature Hydrogen-1.0 GLM-5.3 Kimi K3 GPT-6-Astra Developer Deep Principle Z.ai Moonshot AI OpenAI Total params 753B 753B ( HF ) 2.8T Not disclosed Active params ~40B (inherited) 40B ( LM Studio ) 16 of 896 experts Not disclosed Context 1M 1M 1M 1.05M Weights / license Open, MIT Open, GLM-5.3 License Open Proprietary Modality Text Text Text + vision Not disclosed here Science focus Chemistry, materials, life sciences Coding, agents General General FrontierScience-Research 38.3% Not disclosed Not disclosed 33.3% (per Deep Principle) GPQA-Diamond 93.0% Not disclosed Not disclosed 96.0% (OpenAI-reported) API price (in/out per 1M) NeuroSpark: Not disclosed $1.40 / $4.40 ( Z.ai ) $3.00 / $15.00 $10.00 / $50.00 ( OpenAI ) 

 Key Takeaways 

 Hydrogen-1.0 is an MIT-licensed, 753B GLM-5.3 post-train for science. 

 It reports 38.3% on FrontierScience-Research, above GPT-6-Astra’s 33.3%. 

 Training adds lab records and discovery trajectories, not just papers. 

 It still trails GPT-6-Astra on NMR structure elucidation. 

 NVFP4 and MXFP4 builds target Blackwell and MI350-class GPUs. 

 Check out the Technical blog , Model weights on Hugging Face and Usage notes . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Deep Principle Releases Hydrogen-1.0: A 753B Open-Weight Model for Scientific Discovery appeared first on MarkTechPost .
