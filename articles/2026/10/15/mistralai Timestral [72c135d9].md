---
id: "72c135d9166275d5"
title: "mistralai/Timestral"
url: "https://reddit.com/r/LocalLLaMA/comments/1x6ouoy/mistralaitimestral"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6ouoy/mistralaitimestral"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T15:32:45Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["jacek2023"]
language: "en"
summary: "https://preview.redd.it/zyoo32u7hnvh1.png?width=1400&format=png&auto=webp&s=f0dc824a831d10abc6b824afabb98c64e7fa9d40 from Mistral: Timestral is a family of time series foundation models for zero-shot forecasting, available in 5M , 28M , 123M , and 209M parameter versions. This repository contains the 209M checkpoint. Timestral supports univariate and multivariate forecasting, past-only and…"
tags: ["r/LocalLLaMA"]
orgs: ["Mistral"]
topics: ["models & research"]
content_source: "post"
word_count: 212
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6ouoy/mistralaitimestral/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# mistralai/Timestral

Reddit · jacek2023 · 2026-10-15

https://preview.redd.it/zyoo32u7hnvh1.png?width=1400&format=png&auto=webp&s=f0dc824a831d10abc6b824afabb98c64e7fa9d40 from Mistral: Timestral is a family of time series foundation models for zero-shot forecasting, available in 5M , 28M , 123M , and 209M parameter versions. This repository contains the 209M checkpoint. Timestral supports univariate and multivariate forecasting, past-only and known-future covariates, and probabilistic predictions across 21 quantiles. It accepts up to 32,768 historical time steps and forecasts up to 1,024 steps in a single forward pass. We’re releasing the source code in our GitHub repository to make it easy to run Timestral and reproduce our benchmark results. Model Details Size: 209M parameters. Architecture: patch-based transformer with time attention and variate attention, 24 layers, embedding dimension 768. Patching: 32 time steps per patch. Each patch is embedded from its values together with their missing-value indicators. Context length: up to 32,768 time steps (1,024 patches). Forecast horizon : Up to 1,024 time steps (32 patches) in a single forward pass. Longer horizons are forecast block by block, with each block's median forecast appended to the context. Outputs: 21 quantiles (0.01, 0.05, 0.1, 0.15, …, 0.85, 0.9, 0.95, 0.99). Inputs: univariate or multivariate target variates, plus past-only and known-future covariates, numeric or categorical (categorical covariates are target-encoded). Missing values are marked as NaN. Inference: PyTorch on CPU or GPU. https://huggingface.co/mistralai/Timestral-209M https://huggingface.co/mistralai/Timestral-123M https://huggingface.co/mistralai/Timestral-28M https://huggingface.co/mistralai/Timestral-5M
