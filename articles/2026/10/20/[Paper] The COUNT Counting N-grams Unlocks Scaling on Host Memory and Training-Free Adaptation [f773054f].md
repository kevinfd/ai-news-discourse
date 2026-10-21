---
id: "f773054fd1668509"
title: "[Paper] The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free Adaptation"
url: "https://reddit.com/r/LocalLLaMA/comments/1xat6o7/paper_the_count_counting_ngrams_unlocks_scaling"
link: "https://reddit.com/r/LocalLLaMA/comments/1xat6o7/paper_the_count_counting_ngrams_unlocks_scaling"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T14:10:33Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["pmttyji"]
language: "en"
summary: "The scaling relationship of compute and performance for language models (LMs) has been extensively studied; more recently, models are being designed to scale memory use, as well. In particular, adding embeddings for n-grams scales memory separately from compute use, because each pass only processes individual embedding rows, which are much smaller than the storage used for the whole embedding…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 243
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xat6o7/paper_the_count_counting_ngrams_unlocks_scaling/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free Adaptation

Reddit · pmttyji · 2026-10-20

The scaling relationship of compute and performance for language models (LMs) has been extensively studied; more recently, models are being designed to scale memory use, as well. In particular, adding embeddings for n-grams scales memory separately from compute use, because each pass only processes individual embedding rows, which are much smaller than the storage used for the whole embedding table. However, existing methods train embeddings from scratch, which needs expensive GPU memory for fast reading and writing. Meanwhile, the ordinary memory of the host system is cheap and underutilized by these training methods. To scale on host memory, we introduce COUNT (Counting Offline Unlocks N-gram Transformers), which builds n-gram embeddings without adding learned parameters by storing precomputed n-gram counts on host. We use the corpus frequencies to weight together the LM's own unembeddings of the next tokens most often following the current n-gram history. At a fixed compute budget, COUNT can be added as an additional input embedding for pretraining 1B-parameter LMs to improve validation loss as much as an LM with 57% more compute. If GPU memory is limited, using COUNT to let backbone parameters fill GPU memory gives better performance than splitting memory with additional learned n-gram embeddings. Beyond efficiency, COUNT allows switching in a different table of n-gram counts from a domain-specific corpus at inference time to adapt to a new task without any training. arXiv : https://arxiv.org/abs/2610.20456 PDF : https://arxiv.org/pdf/2610.20456 GitHub : https://github.com/IanMagnusson/COUNT HuggingFace : https://huggingface.co/IanMagnusson tweet : https://x.com/IanMagnusson/status/2110718235507318868
