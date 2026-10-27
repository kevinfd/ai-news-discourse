---
id: "b17eb9dbde5d2705"
title: "Tensor Split Over PCIe 3.0 x1 — Good Results"
url: "https://reddit.com/r/LocalLLaMA/comments/1xgojqz/tensor_split_over_pcie_30_x1_good_results"
link: "https://reddit.com/r/LocalLLaMA/comments/1xgojqz/tensor_split_over_pcie_30_x1_good_results"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T10:10:09Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Introvertosaurus"]
language: "en"
summary: "When I was considering adding a second GPU, quite a few people told me PCIe 3.0 x1 would be a massive bottleneck and that upgrading my motherboard should be my first priority. I went ahead with the x1 riser anyway, and the results have been better than expected. Sharing as this likely have value to other planning machines. My home setup: Intel i5-14400F 2× RTX 3060 12GB (24GB total) One GPU on…"
tags: ["r/LocalLLaMA"]
orgs: ["Intel"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 724
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xgojqz/tensor_split_over_pcie_30_x1_good_results/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Tensor Split Over PCIe 3.0 x1 — Good Results

Reddit · Introvertosaurus · 2026-10-27

When I was considering adding a second GPU, quite a few people told me PCIe 3.0 x1 would be a massive bottleneck and that upgrading my motherboard should be my first priority. I went ahead with the x1 riser anyway, and the results have been better than expected. Sharing as this likely have value to other planning machines. My home setup: Intel i5-14400F 2× RTX 3060 12GB (24GB total) One GPU on PCIe x16, the other on PCIe 3.0 x1 llama.cpp, running Gemma 4 31b Q5 (tight fit, tight context) Switching from layer splitting to tensor splitting increased +42% t/s (14 -> 20), even with one GPU connected over PCIe 3.0 x1. I did not do extensive testing yet though on this exact setup as I am waiting for a PSU upgrade before running those cards too hard. Based on what everyone said I expected it to crawl and was just planning on testing memory allocation... But then got the surprised positive result. Testing on I rented a machine with 2× RTX 5060 Ti 16GB (32GB total) to do some testing on some 70b models but decided to check PCIe traffic during tensor split before I shut it down. I was wondering how much bandwidth tensor splitting actually needed over PCIe. Test configuration: Model: L3.1 Nemotron Sunfall 71B IQ3_XS Context: 2k Flash Attention enabled llama.cpp PCIe Gen 3 capable links, running at x8 width Layer vs. tensor splitting: Test Layer Tensor prompt generation 11.7 t/s 20.7 t/s prompt processing 591.8 t/s 464.4 t/s +77% t/s with tensor splitting. PCIe bandwidth measurements I monitored PCIe traffic during tensor-split inference using: nvidia-smi dmon -s t -d 1 Here are some actual samples during generation (MB/s): GPU RX TX 0 92 102 1 96 105 0 94 108 1 107 108 0 92 100 1 94 99 0 98 107 1 105 111 0 93 103 1 95 101 0 92 99 1 94 98 Both GPUs consistently transferred approximately 90–110 MB/s in each direction during decode. PCIe 3.0 x1 has a theoretical bandwidth of approximately 985 MB/s per direction, this very likely not going to be a bottle neck issue for tensor split for low-mid range GPUs. Model loading would be slightly slower of course, on model loading I saw a spikes exceeding 4,000 MB/s. Obviously, x1 would slow that down adding several seconds to model load time. I am not switching models often though so a few extra seconds on load isn’t an issue. These results don't prove PCIe x1 has no performance penalty. The Vast cards weren't running over x1, and average throughput doesn't capture latency, synchronization overhead, or short transfer bursts. However, it looks very promising that upgrading my motherboard or sacrificing a nvme slot is probably unnecessary. UPDATE: As many have mentioned the prompt processing is the part that slows down the most. I did a fast test on my local 2x3060. Bandwidth usage was higher, but still well below its max. The penalty for tensor split is real, but its not conclusive that it would be any faster with a higher links speed. Looks like I do have a heavy penalty for tensor parallel on prompt processing: Prompt Layer prefill Tensor prefill Tensor penalty 512 313.5 t/s 184.9 t/s −41.0% 2,048 341.6 205.4 −39.9% 4,096 358.4 220.3 −38.5% 6,144 359.5 225.2 −37.4% 7,600 358.7 226.5 −36.9% Below are the PCIe bandwidth on my setup, much higher than the 5060 ti interestingly... however, the majority of the time they still remained well below the max link of GPU 1. This snapshot was captured starting at the prompt processing of the 7600 context size. # gpu rxpci txpci # Idx MB/s MB/s 0 0 691 1 0 813 0 3188 450 1 141 133 0 4065 446 1 143 136 0 4061 409 1 168 136 0 3880 441 1 142 138 0 4021 446 1 142 136 0 4004 421 1 170 136 0 0 0 1 0 0 0 459 407 1 369 363 0 469 394 1 347 378 0 461 393 1 358 380 0 467 387 1 347 369 0 456 406 1 350 376 0 466 387 1 347 366 0 456 387 1 355 207 0 466 388 1 352 214 0 468 387 1 451 284 0 467 387 1 425 365 0 458 374
