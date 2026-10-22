---
id: "a637fa6c047ab047"
title: "Perplexity and NVIDIA Researchers Introduce JOLT: a Joint Teacher-Student Reinforcement Learning Method"
url: "https://marktechpost.com/2026/10/21/perplexity-jolt-joint-on-policy-learning-teaching"
link: "https://marktechpost.com/2026/10/21/perplexity-jolt-joint-on-policy-learning-teaching"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T04:56:31Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Perplexity , along with NVIDIA team, has introduced JOLT, a new post-training method for language models. JOLT stands for Joint On-policy Learning and Teaching . It trains a single model in 2 roles. The teacher sees privileged information; the student does not. The key change is that the teacher is trained too, so its feedback stays usable. On MATH, JOLT matched GRPO’s accuracy with 6.5x fewer…"
tags: ["Agentic AI", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Reinforcement Learning"]
orgs: ["Perplexity", "Nvidia", "DeepSeek", "Hugging Face"]
topics: ["jobs & society", "models & research", "policy & regulation", "chips & infrastructure"]
content_source: "summary"
word_count: 943
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Perplexity and NVIDIA Researchers Introduce JOLT: a Joint Teacher-Student Reinforcement Learning Method

MarkTechPost · Asif Razzaq · 2026-10-22

Perplexity , along with NVIDIA team, has introduced JOLT, a new post-training method for language models. JOLT stands for Joint On-policy Learning and Teaching . It trains a single model in 2 roles. The teacher sees privileged information; the student does not. The key change is that the teacher is trained too, so its feedback stays usable. On MATH, JOLT matched GRPO’s accuracy with 6.5x fewer processed training tokens. For teams running RL post-training, that is a direct compute question. 

 TL;DR 

 What it is: a post-training method. 

 Size: tested on Qwen3-0.6B, Qwen3-4B-Instruct, Qwen3-8B, Qwen3-30B-A3B-Instruct and DeepSeek-V2-Lite. 

 Runs on: 1 shared model plays both roles, so no separate teacher model. Training hardware: Not disclosed. 

 Performance: JOLT+ posts the highest mean score in every setting tested against GRPO, OPSD and π-Distill. 

 Best: AppWorld state-test pass rate of 72.09% with JOLT+, vs 62.20% for GRPO (+9.9 points). 

 Worst: JOLT without student reward scores 51.92% on AppWorld, below GRPO. 

 What is Perplexity JOLT? 

 JOLT is a self-distillation method from Perplexity and NVIDIA that trains one model as teacher and student. It builds on On-Policy Self-Distillation (OPSD) . 

 Why does RL post-training need a better teacher? 

 Outcome-reward RL, such as GRPO , gives one reward per attempt. That signal is sparse. It does not say which tokens helped. On long agentic tasks, successes are rare, so learning is slow. 

 On-Policy Distillation fixes sparsity by having a stronger teacher score each student token. OPSD removes the separate teacher. The same model becomes the teacher when given privileged context, such as a verified solution. 

 The research team argues this is not enough. A teacher holding the answer can take shortcuts the student cannot follow. Its guidance may sit beyond the student’s reach. In the paper, OPSD’s teacher-student disagreement grows during MATH training. 

 How does JOLT work? 

 JOLT trains both roles of one shared model at the same time: 

 Teacher: gets privileged information. It learns from outcome rewards, plus a KL penalty that keeps it close to the student. 

 Student: sees only the task. It learns from the teacher’s token-level distillation signal on its own attempts. 

 On-policy: each role learns from trajectories generated under its own context. 

 JOLT+: adds the student’s own outcome reward to the student update. 

 The research stands in the center on a ‘reward-consistent’ teacher. Its distillation update should point the same way as the student’s reward gradient. The ideal teacher favors high-advantage actions while staying near the student’s policy. 

&&

 How does JOLT perform on benchmarks? 

 The research team tested 5 settings, each with a different base model and type of privileged information: 

 GSM8K: DeepSeek-V2-Lite; teacher gets the verified answer. 

 MATH: Qwen3-0.6B; teacher gets worked reference solutions. 

 LiveCodeBench v6: Qwen3-8B on 131 problems; teacher gets a passing sibling solution or execution feedback. 

 AppWorld: Qwen3-4B-Instruct; teacher gets summaries of past attempts. 

 Terminal-Bench 2.1: Qwen3-30B-A3B-Instruct trained on TMax ; teacher gets private verifier files. 

 JOLT+ had the highest mean score in every setting. Against GRPO, the strongest baseline, it gained 1.5 points on GSM8K. It also gained 4.2 on MATH, 3.0 on LCBv6 and 9.9 on AppWorld. On Terminal-Bench 2.1 , JOLT+ reached 10.96% pass@1 and 34.83% pass@32. GRPO scored 8.25% and 30.34%. 

 Even plain JOLT, with no student reward, beat GRPO on MATH: 72.14% versus 68.36%. 

 How much training compute does JOLT save? 

 On MATH, the research team fit accuracy curves against training-token budgets. At 63.44% accuracy, GRPO’s checkpoint used 8.40M processed training tokens. JOLT’s fitted curve needed 1.30M, a 6.5x reduction. Counting completion tokens only, the gap widens to about 13x. Across 55% to 65% accuracy targets, savings range from 4.3x to 7.4x on processed tokens. 

 JOLT also levels off higher. It plateaus near 72%, against about 70% for GRPO and 62% for OPSD. 

 How does JOLT compare with GRPO, OPSD and π-Distill? 

 All scores below come from Perplexity’s own runs in the JOLT paper , with hyperparameters tuned per method. Method descriptions link to each method’s own paper. 

 Feature JOLT JOLT+ GRPO OPSD π-Distill Separate teacher model No No No teacher No (self-teacher) No (shared model) Teacher is trained Yes (reward + KL to student) Yes (reward + KL to student) Not applicable No Yes (KL-regularized) Student signal Dense distillation, on-policy Distillation + outcome reward Group-relative outcome reward Dense distillation, on-policy Off-policy, teacher trajectories MATH, Qwen3-0.6B (%) 72.14 ± 0.90 72.59 ± 1.17 68.36 ± 3.73 61.20 ± 2.10 42.25 ± 1.10 LCBv6, Qwen3-8B (%) 47.64 ± 1.10 49.08 ± 0.41 46.13 ± 1.83 45.34 ± 1.50 38.23 ± 1.72 AppWorld, Qwen3-4B (%) 51.92 ± 5.30 72.09 ± 6.01 62.20 ± 2.83 29.49 ± 2.48 59.85 ± 2.97 Terminal-Bench 2.1 pass@1 (%) 6.56 10.96 8.25 2.82 4.99 Terminal-Bench 2.1 pass@32 (%) 25.69 34.83 30.34 16.90 22.31 Code Not yet released Not yet released Not disclosed GitHub Not disclosed 

 Terminal-Bench base model: 5.18% pass@1, 22.81% pass@32. 

 Key Takeaways 

 1 model plays teacher and student, and the teacher is trained too. 

 6.5x fewer processed tokens than GRPO at matched MATH accuracy. 

 JOLT+ beats GRPO by 9.9 points on AppWorld. 

 Plain JOLT still trails GRPO on AppWorld and Terminal-Bench. 

 Check out the paper on arXiv and the Perplexity research blog post . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Perplexity and NVIDIA Researchers Introduce JOLT: a Joint Teacher-Student Reinforcement Learning Method appeared first on MarkTechPost .
