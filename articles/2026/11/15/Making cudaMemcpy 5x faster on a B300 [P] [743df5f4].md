---
id: "743df5f4d175f14c"
title: "Making cudaMemcpy 5x faster on a B300 [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p"
link: "https://reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T18:20:27Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["makneeee"]
language: "en"
summary: "https://preview.redd.it/cjz9xy3rht1i1.png?width=1600&format=png&auto=webp&s=0eea8a5d9e53d5ea4593ce1a629bc7342a049ffa Hi everyone, I made a tool that can speed up pageable transfers for cudaMemcpy. For example: # B300, copying a 1 GB tensor to the GPU and back: import time, torch x = torch.ones(1 << 30, dtype=torch.uint8) y = x.to(\"cuda\"); y.cpu() for name, copy in [(\"CPU -> GPU\", lambda:…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 94
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/"
score: null
comments: null
community: "r/MachineLearning"
---

# Making cudaMemcpy 5x faster on a B300 [P]

Reddit · makneeee · 2026-11-15

https://preview.redd.it/cjz9xy3rht1i1.png?width=1600&format=png&auto=webp&s=0eea8a5d9e53d5ea4593ce1a629bc7342a049ffa Hi everyone, I made a tool that can speed up pageable transfers for cudaMemcpy. For example: # B300, copying a 1 GB tensor to the GPU and back: import time, torch x = torch.ones(1 << 30, dtype=torch.uint8) y = x.to("cuda"); y.cpu() for name, copy in [("CPU -> GPU", lambda: (x.to("cuda"), torch.cuda.synchronize()))]: t = time.perf_counter() for _ in range(5): copy() print(f"{name}: {5 * x.nbytes / (time.perf_counter() - t) / 1e9:.1f} GB/s") $ python bench.py CPU -> GPU: 10.2 GB/s $ cmt tune -- python bench.py CPU -> GPU: 51.5 GB/s blog: https://maknee.github.io/blog/2026/CudaMemcpy/ code: https://github.com/Maknee/cudamemcpy-tuner
