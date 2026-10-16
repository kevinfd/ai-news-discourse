---
id: "7bb5688cda75bfec"
title: "Train LoRA directly on Quantized GGUFs, no PyTorch, no Parent(FP16) needed, just your GGUF and the data"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5j48s/train_lora_directly_on_quantized_ggufs_no_pytorch"
link: "https://reddit.com/r/LocalLLaMA/comments/1x5j48s/train_lora_directly_on_quantized_ggufs_no_pytorch"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T05:34:47Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["ZenZombie117"]
language: "en"
summary: "I've seen this one floating around quite a bit now and since this is something that can be done without the parent and or other dependencies i thought i'd share something. Usually when you fine-tune a model you can't: - train against the quantized GGUF file itself - do it without PyTorch, transformers or a separate Python setup - use the exact same GGUF for inference afterwards, without…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 345
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5j48s/train_lora_directly_on_quantized_ggufs_no_pytorch/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Train LoRA directly on Quantized GGUFs, no PyTorch, no Parent(FP16) needed, just your GGUF and the data

Reddit · ZenZombie117 · 2026-10-14

I've seen this one floating around quite a bit now and since this is something that can be done without the parent and or other dependencies i thought i'd share something. Usually when you fine-tune a model you can't: - train against the quantized GGUF file itself - do it without PyTorch, transformers or a separate Python setup - use the exact same GGUF for inference afterwards, without converting the model (QLoRA does train through a 4-bit base, but in PyTorch and on its own NF4 format, not on the GGUF you serve.) With Runner, the CPU training forward pass is the CPU serving forward pass, so the adapter is trained on the exact weights it will run on. CUDA/Metal serving uses the GPU's own arithmetic, within a measured tolerance but not bit-identical. There is no FP16 copy to keep, and no framework to install. With runner the 16-bit nor the PyTorch package is needed, this is done through "freezing" the weights of the current X-bit GGUF, only a "small" LoRA adapter is trained on top. Quick-Guide: # train through the quantized base you will serve ./runner -m base-Q4_K_M.gguf --train data.jsonl --train-steps 200 \ --lora-rank 8 --train-out adapter.gguf # adapter.gguf.train.json now records base/data/adapter sha256, seed, config, binary # serve the adapter beside the frozen base (the exact form) ./runner -m base-Q4_K_M.gguf --lora adapter.gguf --serve # fold it into a standalone file for any GGUF runtime: 8-bit or better ./runner -m base-Q4_K_M.gguf --lora adapter.gguf \ --merge-lora merged-Q8_0.gguf --quant q8_0 # teacher-forced logprobs for evals and rewards ./runner -m base-Q4_K_M.gguf --lora adapter.gguf -f eval.txt --score on thing to note though, when Training 4-bits, the adapter seems to disappear when merging it into the weights, runner refuses such a merge just for that reason unless overridden. Held-out exact tool-call score before training, with the adapter served beside the base, and after merging the adapter into three output types. One base (Qwen3-4B Q4_K_M) and one task, measured 2026-08-22, so not a promise for other models. Source: docs/adaptation-engine.md. You can find the repo with the binaries here: https://github.com/Joakimpalm-Zen/xyntetik-runner Happy Training!
