---
id: "4167e50599dead0e"
title: "2-bit copy in VRAM + exact residual in system RAM as the verifier: speculative decoding for models that don't fit your GPU"
url: "https://reddit.com/r/LocalLLaMA/comments/1xc55z3/2bit_copy_in_vram_exact_residual_in_system_ram_as"
link: "https://reddit.com/r/LocalLLaMA/comments/1xc55z3/2bit_copy_in_vram_exact_residual_in_system_ram_as"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T01:18:28Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Happy_Guitar3521"]
language: "en"
summary: "Hi Guys!, Recently I was making a research and development, but I do not have time to go further with this idea (kids, work, etc.). But maybe it will be interesting for someone. I do not think it would be something big, but maybe interesting approach that can be used in some of the cases. I believe that it is not AI slop, you can use those information's and try by yourself using Claude or Astra.…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Google"]
topics: ["models & research", "chips & infrastructure", "products & launches"]
content_source: "post"
word_count: 386
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xc55z3/2bit_copy_in_vram_exact_residual_in_system_ram_as/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 2-bit copy in VRAM + exact residual in system RAM as the verifier: speculative decoding for models that don't fit your GPU

Reddit · Happy_Guitar3521 · 2026-10-22

Hi Guys!, Recently I was making a research and development, but I do not have time to go further with this idea (kids, work, etc.). But maybe it will be interesting for someone. I do not think it would be something big, but maybe interesting approach that can be used in some of the cases. I believe that it is not AI slop, you can use those information's and try by yourself using Claude or Astra. The idea was my own and I am using it in my production app, it saved me a lot of money (project is not related to LLM's). Not sure if it is outdated or not, it can work also with MTP. Please, just don’t be unkind. I’m sharing my idea with you, and anyone is welcome to experiment with it. TLDR: Keep a 2-bit version of the model on the GPU and the rest of the weights (the residual, 6-8 bit) in system RAM. The 2-bit copy drafts tokens, then the full model checks them: the GPU does the 2-bit part, the CPU does the residual part, and only activations go over PCIe. So the draft costs no extra memory, it's literally half of the verifier. What I measured (real weights, but dequantized and run in PyTorch, so no tok/s yet): - 2-bit + 8-bit residual is closer to bf16 than Q8_0, about half the KL - with a 6-bit residual you get Q8_0-level quality while reading ~28% fewer bytes from RAM - the 2-bit draft that reuses the verifier's KV cache gets 25-30% more accepted tokens per check than Google's official Gemma 4 drafter (31B, 16 node tree: 5.23 vs 4.20) - my CPU kernel checks 16 tokens in about the same time as 1, because it's memory bound Closest thing I found is SubSpec, but it uses a separate 4-bit copy and streams weights over PCIe instead of splitting the model by bits. It only makes sense when Q8 doesn't fit in your VRAM. If it fits, just use llama.cpp. Here is a link to public repo, I hope that it would help someone with his research https://huggingface.co/HappyGuitar123/twobit-residual-spec I suggest also to use some frontier llm with high effort to analyze it, so you will have more insight. I believe that this idea has some potential. Best regards
