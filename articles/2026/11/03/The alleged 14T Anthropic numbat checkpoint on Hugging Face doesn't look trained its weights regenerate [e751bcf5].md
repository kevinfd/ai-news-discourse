---
id: "e751bcf5c1962201"
title: "The alleged 14T Anthropic \"numbat\" checkpoint on Hugging Face doesn't look trained: its weights regenerate exactly from name seeded random noise"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xmmns8/the_alleged_14t_anthropic_numbat_checkpoint_on"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xmmns8/the_alleged_14t_anthropic_numbat_checkpoint_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T07:30:12Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["djcroman"]
language: "en"
summary: "Primary source (Hugging Face audit thread): https://huggingface.co/burner22/numbat/discussions/13 The burner22/numbat repo that went around X and HN this weekend as a leaked mid training \"Mythos class\" checkpoint (7.72 TB, 772 shards, about 14T params claimed) falls apart under a pretty simple test. Hash a tensor's name with SHA256, use the first 8 bytes as a NumPy PCG64 seed, draw normals,…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic", "Hugging Face", "DeepSeek"]
topics: ["models & research"]
content_source: "post"
word_count: 233
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xmmns8/the_alleged_14t_anthropic_numbat_checkpoint_on/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# The alleged 14T Anthropic "numbat" checkpoint on Hugging Face doesn't look trained: its weights regenerate exactly from name seeded random noise

Reddit · djcroman · 2026-11-03

Primary source (Hugging Face audit thread): https://huggingface.co/burner22/numbat/discussions/13 The burner22/numbat repo that went around X and HN this weekend as a leaked mid training "Mythos class" checkpoint (7.72 TB, 772 shards, about 14T params claimed) falls apart under a pretty simple test. Hash a tensor's name with SHA256, use the first 8 bytes as a NumPy PCG64 seed, draw normals, apply a small transform and round to bf16, and you get the stored weights bit for bit. The first audit matched 43 full tensors and also predicted 21 tensors before reading them. A follow up thread extended it to the 4 bit expert matrices: 162,246,496 of 162,246,496 sign bits matched across 770 of the 772 shards. I reran the small tensor check myself with HTTP range reads on shard 1, without running any repo code: 369,408 of 369,408 values matched, and a wrong seed control matched about 0.6%. The norm layers also look nothing like a trained model (kurtosis about 3 at every depth vs roughly 20 to 150 in Qwen3 and DeepSeek V3). The codename itself is real from the March Claude Code leak, which is probably why it spread. Anthropic hasn't commented. The practical bit: the README asks you to load it with trust_remote_code=True. Has anyone seen a tool or HF check that flags "this is seeded noise" automatically? My longer write up with charts and the reproduction (my own site): https://go.djcroman.com/fake-mythos-leak?p=reddit
