---
id: "491d929082574790"
title: "Z AI Releases GLM-5.4: A 750B Loop Transformer That Runs 28 Layers Twice"
url: "https://marktechpost.com/2026/11/23/zai-glm-5-4-loop-transformer"
link: "https://marktechpost.com/2026/11/23/zai-glm-5-4-loop-transformer"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-23T19:11:40Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Z.ai has released GLM-5.4 , its first flagship model built on a Loop Transformer architecture. The GLM-5.4 Loop Transformer runs 28 layers of the GLM-5 base model for 2 iterations. Z.ai says the model reaches intelligence comparable to 2T-3T parameter models. For developers, the pitch is ‘Generalized Coding’: code as the tool for video, games, 3D shaders and CAD. \n\n TL;DR \n\n Size: 750B-scale…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Staff"]
orgs: ["DeepSeek", "Nvidia"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "summary"
word_count: 1091
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Z AI Releases GLM-5.4: A 750B Loop Transformer That Runs 28 Layers Twice

MarkTechPost · Asif Razzaq · 2026-11-23

Z.ai has released GLM-5.4 , its first flagship model built on a Loop Transformer architecture. The GLM-5.4 Loop Transformer runs 28 layers of the GLM-5 base model for 2 iterations. Z.ai says the model reaches intelligence comparable to 2T-3T parameter models. For developers, the pitch is ‘Generalized Coding’: code as the tool for video, games, 3D shaders and CAD. 

 TL;DR 

 Size: 750B-scale base. Active parameters not disclosed. Context window not officially listed (the blog discusses deployment at 1M context). 

 Runs on: Z.ai-hosted only for now (GLM Coding Plan, ZCode, Z.ai Chat). Self-hosting hardware not disclosed until weights ship. 

 Performance: No flagship benchmark table yet. Z.ai claims parity with 2T-3T parameter models. 

 Best: +11.3 points on AIME25 (19.17 to 30.42) in Z.ai’s 30B looped ablation. 

 Worst: +3.3 points on IFBench (50.20 to 53.47), the smallest gain. Z.ai also flags “marathon thinking” loops. 

 What is GLM-5.4? 

 GLM-5.4 is a 750B-scale Loop Transformer from Z.ai that runs shared layers twice per pass. It ships first inside Z.ai’s own products: the GLM Coding Plan , the ZCode desktop app and Z.ai Chat . 

 Z.ai did not pre-train a looped model from scratch. It adapted the pre-trained GLM-5 base through continued training. The technical post states that looped models trained from scratch still trail unshared models at equal compute. Adapting an existing base raises the ceiling with a relatively small compute overhead. 

 How does the Loop Transformer work? 

 In a standard Transformer, each layer runs once per forward pass. In GLM-5.4, a group of 28 weight-shared layers runs for 2 iterations. Z.ai made 3 changes to keep this practical at 750B scale. 

 Gated progressive updates 

 Overwriting hidden states across loops made activation norms blow up. GLM-5.4 adds independent per-token gates for each iteration. The first pass writes small updates and builds global context. The second pass opens the gates to refine the output. On harder tokens, the first pass writes more aggressively. 

 Hybrid KV cache 

 A naive design keeps a full KV cache for every loop. GLM-5.4’s second loop reuses the sparse KV selected in pass 1. It keeps its own new KV only inside a local sliding window. So the extra loop costs 1 sliding window of KV cache, not a full context cache. Z.ai says this keeps the cost increase over GLM-5.3 under control at 1M context. 

 Sparse attention index reuse 

 The second loop reuses the indices from the first loop’s indexer. That adds zero indexing overhead. Z.ai reports near-identical results versus recomputing indices on every pass. 

&&&&

 How does GLM-5.4 perform on benchmarks? 

 Z.ai has not published benchmark scores for the 750B GLM-5.4 model. A Z.ai team member said scores will come later, per DataCamp . The evidence in the blog is an iso-parameter ablation on a 30B model. It shares the 750B base’s architecture. The looped version used about 10% more total training compute. Scores were measured after 200K long-context SFT with thinking mode on. 

 Benchmark (30B ablation) Baseline + Loop Gain Avg. output length change AIME25 19.17 30.42 +11.3 -635 tokens (-2%) GPQA-Diamond 47.58 56.26 +8.7 -2,473 tokens (-11.7%) AA-LCR 40.33 47.67 +7.3 -539 tokens (-9.7%) MMLU-Pro 71.65 75.05 +3.4 -863 tokens (-14.9%) IFBench 50.20 53.47 +3.3 -763 tokens (-13.0%) 

 Source: Z.ai GLM-5.4 blog . Self-reported, 30B model, not the 750B flagship. 

 Two patterns stand out. The largest gains come in math, science reasoning and long context. Output length also falls on most tasks. MMLU-Pro answers got 14.9% shorter and GPQA-Diamond answers 11.7% shorter. Z.ai says part of the reasoning moves into the loop’s implicit depth. AIME25 is the exception: output length dropped only 2%. 

 Z.ai validated the design on 1B, 4B, 30B and 750B bases. The ‘2T-3T parameter’ claim has no flagship table behind it yet. 

 What can GLM-5.4 do beyond traditional coding? 

 Z.ai calls this direction Generalized Coding. It credits gains in both coding and vision. The technical sections shows four demos: 

 Video: a self-narrated music video called “Hello World”. 

 Engineering: a 6-axis robotic arm built through CAD modeling in FreeCAD. 

 Games: a complete game with movement, physics, maps, combat and art assets. 

 3D: an interactive bird-watching scene built with math geometry and custom GLSL shaders. 

 These are vendor demos, not benchmarks. 

 How fast is GLM-5.4 and where can developers use it? 

 Z.ai reports up to 200 tokens/s off-peak and 70-80 tokens/s at peak load. It fused core kernels to cut intermediate memory traffic. 

 Access today runs through the GLM Coding Plan, ZCode and Z.ai Chat. ZCode is Z.ai’s desktop agent harness for GLM-5.4. It runs on macOS, Windows and Linux (Beta). The Coding Plan lists Lite at $12.6/month, Pro at $56 and Max at $117.6. Z.ai says prices may change. 

 How does GLM-5.4 compare with other open frontier models? 

 Feature GLM-5.4 ( Z.ai ) GLM-5.3 ( Z.ai docs ) Kimi K3.1 Pro ( HF ) DeepSeek-V4.1-Flash ( HF ) Architecture Loop Transformer: 28 GLM-5 layers x 2 passes Same base as GLM-5.2, new post-training MoE MoE Total params 750B scale Not disclosed 2.8T 552B backbone + 196B Engram memory Active params Not disclosed Not disclosed 104B 8B prefill / 16B decode Context Not officially listed (blog cites 1M deployment) 1M (128K max output) 1,048,576 Up to 1M Input Not disclosed (vision gains claimed) Text Text, image Text, image License / weights Weights planned after safety hardening Not stated on docs page Kimi K3.1 Pro License, weights on HF MIT, weights on HF Access Coding Plan, ZCode, Z.ai Chat; API soon API, Coding Plan Kimi API and apps HF weights, DeepSeek API Published scores 30B ablation only Terminal-Bench 3.0: 28.3 On model card DeepSWE v1.1: 74.2 ( NVIDIA card ) 

 Key Takeaways 

 GLM-5.4 loops 28 GLM-5 layers twice at 750B scale. 

 30B ablation: +11.3 on AIME25 for ~10% more training compute. 

 The extra loop costs 1 sliding window of KV cache, not a full cache. 

 Up to 200 tok/s off-peak, 70-80 tok/s at peak. 

 No flagship scores, public API or weights yet. 

 Check out the official GLM-5.4 tech blog and try it in ZCode . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Z AI Releases GLM-5.4: A 750B Loop Transformer That Runs 28 Layers Twice appeared first on MarkTechPost .
