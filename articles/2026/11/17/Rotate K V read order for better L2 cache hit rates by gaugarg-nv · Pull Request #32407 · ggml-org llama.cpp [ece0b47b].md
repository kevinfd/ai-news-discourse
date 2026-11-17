---
id: "ece0b47ba33fdc3b"
title: "Rotate K/V read order for better L2 cache hit rates by gaugarg-nv · Pull Request #32407 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/32407"
link: "https://github.com/ggml-org/llama.cpp/pull/32407"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T11:34:46Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["jacek2023"]
language: "en"
summary: "Significant prompt processing speedup with long contexts gpu_info model_type n_prompt n_gen n_depth Master (t/s) PR (t/s) Speed-up NVIDIA GeForce RTX 5090 qwen35 27B Q4_K - Medium 512 0 131072 1290.10833 1822.36027 1.41 NVIDIA GeForce RTX 5090 qwen35 27B Q4_K - Medium 512 0 65536 2030.31282 2527.97409 1.25 NVIDIA GeForce RTX 5090 qwen35 27B Q4_K - Medium 512 0 32768 2931.96118 3142.20539 1.07…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure"]
content_source: "fulltext"
word_count: 228
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xyi6hj/rotate_kv_read_order_for_better_l2_cache_hit/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Rotate K/V read order for better L2 cache hit rates by gaugarg-nv · Pull Request #32407 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-11-17

Repository navigation
Rotate K/V read order for better L2 cache hit rates - #32407
Merged
Merged
Conversation
      
          
github-actions
Bot
            added
      
  ggml
  changes relating to the ggml tensor library for machine learning 
      
  CUDA
  Related to the CUDA backend 
  labels
      Nov 16, 2026 
    
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
