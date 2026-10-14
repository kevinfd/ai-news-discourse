---
id: "1e5b8b0dfbafde85"
title: "common : add --spec-draft-n-ubatch by ggerganov · Pull Request #30459 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30459"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T11:08:21Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["jacek2023"]
language: "en"
summary: "a new option to optimize your VRAM"
tags: ["r/LocalLLaMA"]
orgs: []
topics: []
content_source: "fulltext"
word_count: 312
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5odh2/common_add_specdraftnubatch_by_ggerganov_pull/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# common : add --spec-draft-n-ubatch by ggerganov · Pull Request #30459 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-10-14

Repository navigation
common : add --spec-draft-n-ubatch - #30459
Merged
Merged
Conversation
Allow configuring the physical batch size of the draft context. The
drafters feed it at most the drafted tokens per sequence and chunk larger
batches by its own n_ubatch, so it does not need the ubatch of the target.
A smaller value shrinks the draft compute buffer and leaves more VRAM for
the target KV cache (the draft is fitted together with the target).
The default 0 keeps the current behavior of following --n-ubatch.
Assisted-by: pi:llama.cpp/Qwen3.8-Flash-Next
              
                    ggerganov
    
              
              commented
              
                  
                    Oct 13, 2026 
                  
              
              
            
      
          
github-actions
Bot
            added
      
  documentation
  Improvements or additions to documentation 
      
  testing
  Everything test related 
      
  server
  labels
      Oct 13, 2026 
    
            ggerganov
            marked this pull request as ready for review
        October 13, 2026 18:51         
        
      
[no ci]
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
