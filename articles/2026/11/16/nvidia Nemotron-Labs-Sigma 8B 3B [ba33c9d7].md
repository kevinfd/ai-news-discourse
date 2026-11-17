---
id: "ba33c9d72629ae8a"
title: "nvidia/Nemotron-Labs-Sigma 8B/3B"
url: "https://reddit.com/r/LocalLLaMA/comments/1xxwg6w/nvidianemotronlabssigma_8b3b"
link: "https://reddit.com/r/LocalLLaMA/comments/1xxwg6w/nvidianemotronlabssigma_8b3b"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T18:06:03Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["jacek2023"]
language: "en"
summary: "Nemotron-Labs-Sigma-8B-instruct is a 8-billion-parameter continuous diffusion language model. Instead of generating text one token at a time, it denoises Gaussian noise in a low-dimensional (16-D) continuous token-embedding space, where the denoiser network and the token embeddings are learned jointly by likelihood optimization. Text is decoded in parallel blocks: each block of tokens is refined…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "chips & infrastructure", "business & funding"]
content_source: "post"
word_count: 372
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xxwg6w/nvidianemotronlabssigma_8b3b/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# nvidia/Nemotron-Labs-Sigma 8B/3B

Reddit · jacek2023 · 2026-11-16

Nemotron-Labs-Sigma-8B-instruct is a 8-billion-parameter continuous diffusion language model. Instead of generating text one token at a time, it denoises Gaussian noise in a low-dimensional (16-D) continuous token-embedding space, where the denoiser network and the token embeddings are learned jointly by likelihood optimization. Text is decoded in parallel blocks: each block of tokens is refined over a configurable number of denoising steps (Denoising Diffusion Probabilistic Model (DDPM) or Denoising Diffusion Implicit Model (DDIM) samplers) with self-conditioning, while previously committed tokens are reused through a standard key-value (KV) cache. Fewer steps trade a little quality for large speedups, and the smooth continuous representation makes the model amenable to few-step distillation and trajectory steering. This is the SFT (supervised fine-tuned) variant, fine-tuned for instruction following on top of the corresponding Base model . Use the bundled chat template to format conversations. This model is ready for commercial or non-commercial use. Highlights Continuous-space diffusion language modeling at 8B scale with reasoning accuracy competitive with state-of-the-art masked (discrete) diffusion LMs. Block-parallel decoding: whole blocks of tokens are denoised together; sampling quality holds up well down to few denoising steps per block. Efficient DDPM/DDIM-based samplers with self-conditioning and optional classifier-free guidance, implemented in plain PyTorch in this repository. Standard transformers loading via trust_remote_code ; no custom kernels, flash-attention, or training framework required for inference. Model Architecture Architecture Type: Transformer Network Architecture: Other: Ministral-style decoder-only Transformer (grouped-query attention, SwiGLU, rotary position embeddings) with a continuous-diffusion generation head (16-D continuous token-embedding space, learned jointly with the denoiser). Number of model parameters: 8 billion (8B) This model was developed based on: Nemotron-Labs-Sigma-8B Input Input Type(s): Text Input Format(s): String Input Parameters: One-Dimensional (1D): Sequences Other Properties Related to Input: Maximum context length of 8,192 tokens (prompt plus generated tokens). Conversations should be formatted with the bundled chat template (chat_template.jinja). Supported language: English. Output Output Type(s): Text Output Format: String Output Parameters: One-Dimensional (1D): Sequences Other Properties Related to Output: Up to 8,192 tokens total (prompt plus generation). Text is generated in parallel blocks (default 64 tokens per block) with a configurable number of denoising steps per block (Number of Function Evaluations (NFE) = steps + 1 per block); fewer steps give faster generation at some quality cost. https://huggingface.co/nvidia/Nemotron-Labs-Sigma-8B https://huggingface.co/nvidia/Nemotron-Labs-Sigma-8B-instruct https://huggingface.co/nvidia/Nemotron-Labs-Sigma-3B https://huggingface.co/nvidia/Nemotron-Labs-Sigma-3B-instruct
