---
id: "242f625fdf1eee1c"
title: "First 6-step LoRA adapters with no upsampling step, ~5x faster [N]"
url: "https://reddit.com/r/MachineLearning/comments/1xgye14/first_6step_lora_adapters_with_no_upsampling_step"
link: "https://reddit.com/r/MachineLearning/comments/1xgye14/first_6step_lora_adapters_with_no_upsampling_step"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T17:09:28Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["sdiazlor"]
language: "en"
summary: "Hey! We published a set of 6-step LoRAs, one without the upsampling step: https://huggingface.co/PrunaAI/P-Q-Image-2.1 - Generate or edit images in just 6 steps instead of 40. Use 6-steps for preserving inputs when editing and 6-steps-upsampled for improved visual quality and shorter end-to-end generation. - 6-step distillation provides improved quality with few generation steps.…"
tags: ["r/MachineLearning"]
orgs: ["Alibaba"]
topics: []
content_source: "post"
word_count: 112
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xgye14/first_6step_lora_adapters_with_no_upsampling_step/"
score: null
comments: null
community: "r/MachineLearning"
---

# First 6-step LoRA adapters with no upsampling step, ~5x faster [N]

Reddit · sdiazlor · 2026-10-27

Hey! We published a set of 6-step LoRAs, one without the upsampling step: https://huggingface.co/PrunaAI/P-Q-Image-2.1 - Generate or edit images in just 6 steps instead of 40. Use 6-steps for preserving inputs when editing and 6-steps-upsampled for improved visual quality and shorter end-to-end generation. - 6-step distillation provides improved quality with few generation steps. 6-steps-upsampled is the first distillation that removes the need for a separate prompt-upsampling step. This means 41 to 80 seconds saved, depending on your prompt style. - The LoRA adapters load directly on top of Qwen-Image-2.1, so the pipeline stays unchanged. Few-step distillation cuts the diffusion cost, and the upsampled adapter also removes the prompt-upsampling step before image generation.
