---
id: "76f9c54918a11783"
title: "[Paper] Specter: Fast MoE Inference via Quantization-Enabled Multi-Step Speculative Offloading"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbj6an/paper_specter_fast_moe_inference_via"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbj6an/paper_specter_fast_moe_inference_via"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T10:09:24Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["pmttyji"]
language: "en"
summary: "Mixture-of-experts (MoE) models often exceed a single accelerator's memory capacity. Offloading experts to host memory creates a severe PCIe I/O bottleneck because data-dependent routing keeps transfers on the critical path. We present Specter, an inference system that uses quantization to combine speculative decoding with expert offloading. Its lightweight quantized draft model runs efficiently…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 141
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbj6an/paper_specter_fast_moe_inference_via/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] Specter: Fast MoE Inference via Quantization-Enabled Multi-Step Speculative Offloading

Reddit · pmttyji · 2026-10-21

Mixture-of-experts (MoE) models often exceed a single accelerator's memory capacity. Offloading experts to host memory creates a severe PCIe I/O bottleneck because data-dependent routing keeps transfers on the critical path. We present Specter, an inference system that uses quantization to combine speculative decoding with expert offloading. Its lightweight quantized draft model runs efficiently on device while preserving high-fidelity expert activation patterns. This provides accurate multi-step lookahead over future expert usage, allowing the runtime to organize expert movement and execution ahead of verification and improve both communication and execution efficiency. Under single-request inference, Specter achieves an average 1.50x (up to 1.88x) speedup in time per output token (TPOT) over the state-of-the-art system. Specter makes memory-constrained, single-GPU MoE inference more practical on commodity hardware . Our code is available at this https URL . arXiv : https://arxiv.org/abs/2511.14102 PDF : https://arxiv.org/pdf/2511.14102 GitHub : https://github.com/wwwwwf/specter_asplos
