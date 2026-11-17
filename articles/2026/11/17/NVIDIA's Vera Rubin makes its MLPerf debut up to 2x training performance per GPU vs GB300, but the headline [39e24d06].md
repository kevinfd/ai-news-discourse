---
id: "39e24d064fd38ff2"
title: "NVIDIA's Vera Rubin makes its MLPerf debut: up to 2x training performance per GPU vs GB300, but the headline 10x agentic figure is still provisional"
url: "https://reddit.com/r/artificial/comments/1xy8wb5/nvidias_vera_rubin_makes_its_mlperf_debut_up_to"
link: "https://reddit.com/r/artificial/comments/1xy8wb5/nvidias_vera_rubin_makes_its_mlperf_debut_up_to"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T02:39:04Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["winer666"]
language: "en"
summary: "NVIDIA released its first MLPerf results for the Vera Rubin platform today (MLPerf Training v6.1 and MLPerf Endpoints v1.0). The numbers, from NVIDIA's blog post: - Vera Rubin NVL72 swept all seven MLPerf Training v6.1 benchmarks, with up to 2x more performance per GPU than a highly optimized GB300 NVL72 baseline. On DeepSeek-V3 671B it trained in 4.14 minutes on 1,024 GPUs, vs 8.03 minutes for…"
tags: ["r/artificial"]
orgs: ["Nvidia", "DeepSeek"]
topics: ["chips & infrastructure", "models & research", "agents & coding"]
content_source: "post"
word_count: 218
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xy8wb5/nvidias_vera_rubin_makes_its_mlperf_debut_up_to/"
score: null
comments: null
community: "r/artificial"
---

# NVIDIA's Vera Rubin makes its MLPerf debut: up to 2x training performance per GPU vs GB300, but the headline 10x agentic figure is still provisional

Reddit · winer666 · 2026-11-17

NVIDIA released its first MLPerf results for the Vera Rubin platform today (MLPerf Training v6.1 and MLPerf Endpoints v1.0). The numbers, from NVIDIA's blog post: - Vera Rubin NVL72 swept all seven MLPerf Training v6.1 benchmarks, with up to 2x more performance per GPU than a highly optimized GB300 NVL72 baseline. On DeepSeek-V3 671B it trained in 4.14 minutes on 1,024 GPUs, vs 8.03 minutes for GB300 at the same scale, with about 97% scaling efficiency going from 256 to 1,024 GPUs. - On MLPerf Endpoints, NVIDIA claims more than 10x the throughput per watt on agentic inference (Kimi K3) vs GB300 at the same response speed. The caveat worth flagging: the 10x Endpoints figure is provisional, pending MLCommons verification, and it comes from one specific configuration pairing - 32 Vera Rubin accelerators at 1,024 concurrent queries vs 48 GB300 accelerators at 48 queries. Time to first token was actually slower on Vera Rubin in that run (4,673.9 ms vs 2,305.1 ms at P90). The training sweep is the more solid part of the story, and it's the first independent-style benchmark showing of the Rubin generation. What do you make of it - does the training result alone move the needle on the hardware race, or is agentic inference throughput the number that actually matters now? Source: https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin/
