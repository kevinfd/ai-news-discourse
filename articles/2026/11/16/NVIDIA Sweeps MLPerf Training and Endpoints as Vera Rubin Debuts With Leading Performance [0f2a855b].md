---
id: "0f2a855bc6a8fcf2"
title: "NVIDIA Sweeps MLPerf Training and Endpoints as Vera Rubin Debuts With Leading Performance"
url: "https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin"
link: "https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin"
source: "NVIDIA Blog"
domain: "blogs.nvidia.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-16T16:00:25Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Shruti Koparkar"]
language: "en"
summary: "In its MLPerf benchmarks debut, with results released today, the NVIDIA Vera Rubin platform delivers leading performance across training, post-training and agentic inference.  \n NVIDIA swept every MLPerf Training v6.1 benchmark and, in its first MLPerf Endpoints submission, delivered more than 10x generational gains in throughput per watt for agentic AI — measuring how much agentic work a system…"
tags: ["AI", "AI Infrastructure", "Hardware", "Networking", "Software", "Agentic AI", "AI Training", "CUDA", "NVIDIA Vera Rubin"]
orgs: ["Nvidia", "Microsoft", "Google", "DeepSeek", "Oracle", "CoreWeave"]
topics: ["chips & infrastructure", "models & research", "agents & coding"]
content_source: "fulltext"
word_count: 698
paywalled: false
image: "https://blogs.nvidia.com/wp-content/uploads/2026/11/vera-rubin-mlperf-training-endpoints.png"
discussion_url: null
score: null
comments: null
community: null
---

# NVIDIA Sweeps MLPerf Training and Endpoints as Vera Rubin Debuts With Leading Performance

NVIDIA Blog · Shruti Koparkar · 2026-11-16

In its MLPerf benchmarks debut, with results released today, the NVIDIA Vera Rubin platform delivers leading performance across training, post-training and agentic inference.
NVIDIA swept every MLPerf Training v6.1 benchmark and, in its first MLPerf Endpoints submission, delivered more than 10x generational gains in throughput per watt for agentic AI — measuring how much agentic work a system delivers with each watt of power.
These results are just the beginning. Vera Rubin performance will keep climbing through continuous optimization of NVIDIA’s CUDA-powered software stack, so the infrastructure that customers invest in today delivers more value over time.
NVIDIA Sweeps MLPerf Training v6.1
AI agents are now everywhere, writing code, running business workflows, answering customer questions and, as this week’s SC26 conference highlights, advancing scientific research.
Faster training means smarter agents can reach users sooner, drug discovery models can keep pace with new lab data and fraud-detection models can adapt to new threats faster.
MLPerf Training measures how fast a system can train a range of AI models to a target level of accuracy.
The NVIDIA platform was the only one with results on every benchmark this round, spanning large language models, image generation, recommender systems and reinforcement learning post-training. In its debut, Vera Rubin NVL72 delivered up to 2x more performance per GPU than the highly optimized NVIDIA GB300 NVL72 system — early results that show the pace of generation-over-generation innovation.
NVIDIA also demonstrated performance at scale. On the DeepSeek-V3 benchmark, Vera Rubin NVL72 scaled from 256 to 1,024 GPUs with about 97% efficiency: quadrupling the GPUs cut time to train from 16 minutes to about four.
NVIDIA also ran the benchmark on 10,240 GPUs with GB300 systems, representing the largest scale in this round. Microsoft Azure matched that scale with 10,240 NVIDIA GPUs with GB200 systems.
Results at this scale matter because adding GPUs only speeds up training if they can work together efficiently. NVIDIA NVLink scale-up networking connects the GPUs within each system so they act as one, while NVIDIA Quantum-X800 InfiniBand and Spectrum-X Ethernet scale-out networking link those systems across the data center. Combined with optimized software, this keeps thousands of GPUs working in concert, helping developers build more intelligent models while cutting training times.
NVIDIA Vera Rubin Leads Agentic Inference on MLPerf Endpoints
An AI agent for travel that plans and books a whole trip — or an IT agent that finds and fixes a problem before anyone files a ticket — may reason, call tools and check its work many times to finish a single task.
Each of those steps generates tokens. Because AI data centers are limited by power, the more tokens a system can generate each second for every watt of power, the more agents it can serve and the more value it creates.
MLPerf Endpoints tests systems on real agentic coding and enterprise workflows, and checks that the agents still complete their tasks correctly. NVIDIA Vera Rubin leads across all of its agentic benchmarks.
For example, in a provisional result for Kimi K3, a large open model built for agentic workflows, Vera Rubin NVL72 systems deliver more than 10x the throughput per watt of NVIDIA GB300 NVL72 at the same response speed.
Every AI service has to balance serving many users at once against responding quickly to each one. Vera Rubin shifts that entire curve, serving more users while responding faster.
Leadership Across Benchmarks and Workloads
NVIDIA partners participated extensively in MLPerf Training, with submissions from 20 organizations: ASUS, Azure, Cisco, CoreWeave, Crusoe, Dell Technologies, Firmus, Giga Computing, Google Cloud, HPE, Inventec, Krai, Lambda, Nebius, Oracle, Quanta Cloud Technology (QCT), Supermicro, TTA and the University of Florida.
Their submissions show how NVIDIA’s programmable platform, with open source libraries and frameworks, lets a vast ecosystem of partners innovate and optimize AI training performance.
The lead extends beyond MLPerf.
Vera Rubin also delivers leading performance on independent benchmarks including SemiAnalysis AgentX and Artificial Analysis AgentPerf, showcasing how the same NVIDIA infrastructure can productively run everything from pretraining and post-training to agentic inference, as well as workloads beyond AI, such as the high-performance computing showcased at SC26 this week.
Dive deeper into the results in the MLPerf Training and MLPerf Endpoints technical blogs.
