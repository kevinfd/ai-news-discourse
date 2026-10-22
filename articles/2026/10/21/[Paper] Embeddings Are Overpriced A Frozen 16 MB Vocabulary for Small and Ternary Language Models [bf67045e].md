---
id: "bf67045e32e4d431"
title: "[Paper] Embeddings Are Overpriced? A Frozen 16 MB Vocabulary for Small and Ternary Language Models"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbnpiu/paper_embeddings_are_overpriced_a_frozen_16_mb"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbnpiu/paper_embeddings_are_overpriced_a_frozen_16_mb"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T13:50:09Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["pmttyji"]
language: "en"
summary: "In a small language model the vocabulary is the single largest part. In Gemma 3 270M the embedding table holds 168M of 268M parameters, and because quantisation methods leave the embedding in 16-bit, it is also most of the file once the rest of the model is compressed. We ask what that table actually buys. We replace it with one frozen table of 512-bit codes, 16 MB, with no trainable parameters,…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 253
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbnpiu/paper_embeddings_are_overpriced_a_frozen_16_mb/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] Embeddings Are Overpriced? A Frozen 16 MB Vocabulary for Small and Ternary Language Models

Reddit · pmttyji · 2026-10-21

In a small language model the vocabulary is the single largest part. In Gemma 3 270M the embedding table holds 168M of 268M parameters, and because quantisation methods leave the embedding in 16-bit, it is also most of the file once the rest of the model is compressed. We ask what that table actually buys. We replace it with one frozen table of 512-bit codes, 16 MB, with no trainable parameters, derived once from a pretrained embedding by principal-component projection and sign binarisation, and we train the same Gemma-shaped body from scratch on the same 2.05B tokens with and without it. The learned table buys 0.20 nats of validation loss for 2.6 times the trainable parameters, but on LAMBADA, HellaSwag and PIQA the frozen-table model is better or tied; only ARC-Easy favours the learned table. With a ternary BitNet b1.58 body the whole model is a 46 MB file, still ties the float model on LAMBADA and PIQA, and on a laptop CPU generates 615 to 740 tokens per second in 62 MB of memory, five to six times the speed of the float model's 8-bit GGUF in this http URL at a seventh of the memory. The frozen table wins by 1.7 to 2.3 nats on rare words, accepts 10,000 new words after training with a 3% cost where the learned table collapses by 43%, and all of it is released with the weights, the data and every evaluation answer. arXiv : https://arxiv.org/abs/2610.22428 PDF : https://arxiv.org/pdf/2610.22428 GitHub : https://github.com/QLNI HuggingFace : https://huggingface.co/QLNI/embeddings-are-overpriced
