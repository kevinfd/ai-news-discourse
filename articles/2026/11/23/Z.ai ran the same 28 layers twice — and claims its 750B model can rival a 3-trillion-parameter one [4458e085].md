---
id: "4458e08548329593"
title: "Z.ai ran the same 28 layers twice — and claims its 750B model can rival a 3-trillion-parameter one"
url: "https://thenewstack.io/zai-glm54-loop-transformer"
link: "https://thenewstack.io/zai-glm54-loop-transformer"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-23T18:46:42Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Z.ai released GLM-5.4 on Monday , introducing a Loop Transformer architecture that executes the same layers multiple times to increase computational depth without adding parameters. \n\n The company claims its 750-billion-parameter model can match the reasoning performance of models with 2 trillion to 3 trillion parameters… \n\n The company claims its 750-billion-parameter model can match the…"
tags: ["AI Engineering", "AI Models", "Large Language Models"]
orgs: []
topics: ["models & research", "business & funding", "agents & coding", "chips & infrastructure"]
content_source: "summary"
word_count: 570
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Z.ai ran the same 28 layers twice — and claims its 750B model can rival a 3-trillion-parameter one

The New Stack · Amanda Caswell · 2026-11-23

Z.ai released GLM-5.4 on Monday , introducing a Loop Transformer architecture that executes the same layers multiple times to increase computational depth without adding parameters. 

 The company claims its 750-billion-parameter model can match the reasoning performance of models with 2 trillion to 3 trillion parameters… 

 The company claims its 750-billion-parameter model can match the reasoning performance of models with 2 trillion to 3 trillion parameters, although it has not published full-scale benchmarks to support that comparison. 

 Built by continuing to train GLM-5 , the model runs a shared block of 28 layers twice during inference. Z.ai developed the architecture for demanding coding and agentic workloads . 

 Depth without more parameters 

 Z.ai chose to modify a pretrained model after earlier experiments showed that looped Transformers trained from scratch performed worse than conventional models given the same pretraining compute. 

 Repeating layers at this scale created problems with activation stability and attention caching. Z.ai introduced per-token gates to regulate updates to the residual stream and prevent activation norms from growing across iterations. 

 GLM-5.4 shares the first iteration’s KV cache and maintains a separate sliding window for the second pass, avoiding the memory cost of duplicating the entire attention history at context lengths of up to one million tokens. The model also reuses sparse attention indices between iterations, which Z.ai says had negligible impact on performance in its testing. 

 Z.ai developed fused inference kernels to reduce intermediate memory reads and writes during repeated layer execution. 

 Z.ai developed fused inference kernels to reduce intermediate memory reads and writes during repeated layer execution. 

 What the 30B benchmarks show 

 Z.ai tested the architecture at 1 billion, 4 billion, 30 billion, and 750 billion parameters, but the detailed benchmark results come from the 30-billion-parameter model. 

 In those tests, the looped model outperformed a conventional Transformer of the same size on math, scientific reasoning, and long-context tasks, despite requiring about 10% more training compute. 

 The model also generated 10% to 14% fewer output tokens on benchmarks including MMLU-Pro and GPQA-Diamond. Z.ai attributes the shorter responses to reasoning handled within the repeated layers rather than through additional generated tokens. 

 From code to robot arms 

 Z.ai calls its approach Generalized Coding. Its GLM-5.4 demonstrations include building games with physics and combat systems, creating 3D environments with GLSL shaders, and designing a six-axis robotic arm in FreeCAD. 

 In a post on X , Z.ai head Zixuan Li reported improvements over GLM-5.3 in test writing, code QA, feature development, bug fixes, and terminal-based tasks, although the company has not published the underlying evaluations. 

 Performance has varied since launch. Z.ai claims throughput of up to 200 tokens per second during off-peak hours, dropping to 70 to 80 during peak traffic. 

 One developer reported speeds of 150 to 170 tokens per second initially, followed by reports of 40 to 50 tokens per second and traffic errors later in the day. Controlled comparisons of inference latency and cost remain unavailable. 

 Z.ai also acknowledges that GLM-5.4 can spend excessive time reasoning through tasks. 

 Z.ai also acknowledges that GLM-5.4 can spend excessive time reasoning through tasks. The company is exploring adaptive computation to limit additional iterations to tokens that need them. 

 GLM-5.4 is available through the GLM Coding Plan, ZCode, and Z.ai Chat, with vision support and a one-million-token context window. 
 The post Z.ai ran the same 28 layers twice — and claims its 750B model can rival a 3-trillion-parameter one appeared first on The New Stack .
