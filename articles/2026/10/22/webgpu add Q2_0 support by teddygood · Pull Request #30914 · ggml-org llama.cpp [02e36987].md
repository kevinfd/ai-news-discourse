---
id: "02e369879a379a41"
title: "webgpu : add Q2_0 support by teddygood · Pull Request #30914 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30914"
link: "https://github.com/ggml-org/llama.cpp/pull/30914"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T09:17:46Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["pmttyji"]
language: "en"
summary: "Tested on an RTX 3060 with native Dawn WebGPU . llama-bench -m MODEL -p 512 -n 128 -r 5 -ngl 99 -dev WebGPU -t 2 -fa off Model Test master (t/s) PR (t/s) Ternary Bonsai 1.7B Q2_0 pp512 35.03 ± 0.46 1915.91 ± 3.36 Ternary Bonsai 1.7B Q2_0 tg128 14.02 ± 0.16 94.75 ± 0.20 Bonsai 2 2B Q2_0 pp512 36.40 ± 0.46 2039.89 ± 10.03 Bonsai 2 2B Q2_0 tg128 12.57 ± 0.20 71.72 ± 0.24"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 245
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xcdpks/webgpu_add_q2_0_support_by_teddygood_pull_request/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# webgpu : add Q2_0 support by teddygood · Pull Request #30914 · ggml-org/llama.cpp

GitHub · pmttyji · 2026-10-22

Repository navigation
webgpu : add Q2_0 support - #30914
Merged
Merged
Conversation
      
          
github-actions
Bot
            added
      
  ggml
  changes relating to the ggml tensor library for machine learning 
      
  WebGPU
  labels
      Oct 21, 2026 
    
      
          
yomaytk
          added
  the 
  merge ready
  A maintainer can use this label to indicate that they consider the changes final and ready to merge. 
 label
      Oct 22, 2026 
    
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
