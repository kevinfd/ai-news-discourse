---
id: "a0338e84289c7545"
title: "qwen4exp : build the QSA selection without the kq_mask by sanmai · Pull Request #30965 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30965"
link: "https://github.com/ggml-org/llama.cpp/pull/30965"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T18:43:46Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["jacek2023"]
language: "en"
summary: "gigabytes of VRAM saved (Qwen Flash Next) \"This is one of the things Strata does to squeeze the most juice from the experts' cache.\""
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 353
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdmek0/qwen4exp_build_the_qsa_selection_without_the_kq/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# qwen4exp : build the QSA selection without the kq_mask by sanmai · Pull Request #30965 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-10-23

Repository navigation
qwen4exp : build the QSA selection without the kq_mask - #30965
Merged
Merged
Conversation
      
          
sanmai
        changed the title
Feat/qsa no kq mask
qwen4exp : build the QSA selection without the kq_mask
      Oct 22, 2026 
    
      
          
github-actions
Bot
            added
      
  model
  Model specific 
      
  testing
  Everything test related 
      
  ggml
  changes relating to the ggml tensor library for machine learning 
      
  CUDA
  Related to the CUDA backend 
  labels
      Oct 22, 2026 
    
3ff573e    to
    7d0ea51      
    Compare
  
          
        
  
    Contributor
        
    
ggml_top_k_mask with a single keep row returns [n_kv, n_tokens], while
build_attn_qsa expects the kq_mask layout [n_kv, n_tokens/n_stream, 1, n_stream].
With several streams the shape assert failed at graph reserve.
              
                    sanmai
    
              
              commented
              
                  
                    Oct 22, 2026 
                  
              
              
            
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
              sanmai
              marked this pull request as ready for review
          October 22, 2026 09:14           
        
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
              
                    am17an
    
              
              approved these changes
              
                  
                    Oct 23, 2026 
                  
              
              
            
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
    
              
                    ServeurpersoCom
    
              
              approved these changes
              
                  
                    Oct 23, 2026 
                  
              
              
            
    
  edwardyoon 
      pushed a commit
        to edwardyoon/focus-llama
      that referenced
      this pull request
    
      Oct 24, 2026 
    
    
      
  
    
      …without the kq_mask
      
        
      
      
    6 tasks
  
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
