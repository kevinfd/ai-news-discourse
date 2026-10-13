---
id: "a0839e2334709927"
title: "Normalizing Trajectory Models"
url: "https://machinelearning.apple.com/research/normalizing-trajectory-models"
source: "Apple Machine Learning Research"
domain: "machinelearning.apple.com"
source_type: "research"
collector: "rss"
date: "2026-10-08T00:00:00Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: []
language: "en"
summary: "Diffusion-based models decompose sampling into many small Gaussian denoising steps, an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which…"
tags: []
orgs: ["Apple"]
topics: ["models & research", "jobs & society"]
content_source: "fulltext"
word_count: 353
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Normalizing Trajectory Models

Apple Machine Learning Research · 2026-10-08

Normalizing Trajectory Models
AuthorsJiatao Gu†, Tianrong Chen, Ying Shen‡**, David Berthelot, Shuangfei Zhai, Josh Susskind
content type paperpublished October 2026
Diffusion-based models decompose sampling into many small Gaussian denoising steps, an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the score function induced by the model itself produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
- † University of Pennsylvania
- ‡ UIUC
- ** Work done while at Apple
Trajectory as the Teacher: Few-Step Discrete Flow Matching via Energy-Navigated Distillation
September 16, 2026research area Methods and Algorithms, research area Speech and Natural Language Processing
Discrete flow matching generates text by iteratively transforming noise tokens into coherent language, but may require hundreds of forward passes. Distillation uses the multi-step trajectory to train a student to reproduce the process in a few steps. When the student underperforms, the usual explanation is insufficient capacity. We argue the opposite: the trajectory is the bottleneck, not the student. Each training trajectory is built through a…
Normalizing Flows with Iterative Denoising
May 6, 2026research area Computer Vision, research area Methods and Algorithmsconference ICML
Normalizing Flows (NFs) are a classical family of likelihood-based methods that have received revived attention. Recent efforts such as TARFlow have shown that NFs are capable of achieving promising performance on image modeling tasks, making them viable alternatives to other methods such as diffusion models. In this work, we further advance the state of Normalizing Flow generative models by introducing iterative TARFlow (iTARFlow). Unlike…
