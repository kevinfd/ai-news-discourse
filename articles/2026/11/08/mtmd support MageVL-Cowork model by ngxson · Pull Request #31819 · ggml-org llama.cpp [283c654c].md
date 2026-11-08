---
id: "283c654c46db522b"
title: "mtmd: support MageVL-Cowork model by ngxson · Pull Request #31819 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/31819"
link: "https://github.com/ggml-org/llama.cpp/pull/31819"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T04:04:59Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["pmttyji"]
language: "en"
summary: "GGUF to use : https://huggingface.co/ggml-org/Mage-VL-Cowork-GGUF"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 363
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xqpc7u/mtmd_support_magevlcowork_model_by_ngxson_pull/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# mtmd: support MageVL-Cowork model by ngxson · Pull Request #31819 · ggml-org/llama.cpp

GitHub · pmttyji · 2026-11-08

Repository navigation
mtmd: support MageVL-Cowork model - #31819
Merged
Merged
Conversation
      
          
github-actions
Bot
            added
      
  mtmd
  Related to multimodal functionality (video/image/audio) 
      
  conversion
  labels
      Nov 6, 2026 
    
              
                    CISC
    
              
              approved these changes
              
                  
                    Nov 6, 2026 
                  
              
              
            
        
  
    Collaborator
        
  Author
    
The rope factors are shared by every layer, so they live in clip_model
instead of a pointer copied into each clip_layer. The loader now checks
that v.rope_freqs is F32 with d_head elements and that d_head splits
into the 4:6:6 pairs the graph expects.
        
  
    Contributor
        
    
    
  ServeurpersoCom 
      added a commit
        to ServeurpersoCom/llama.cpp
      that referenced
      this pull request
    
      Nov 7, 2026 
    
    
  
    
  neurall 
      pushed a commit
        to neurall/llama.cpp
      that referenced
      this pull request
    
      Nov 8, 2026 
    
    
      
  
    
      * mtmd: support MageVL-Cowork model
* mtmd: keep magevl rope_freqs at model level and check its shape
The rope factors are shared by every layer, so they live in clip_model
instead of a pointer copied into each clip_layer. The loader now checks
that v.rope_freqs is F32 with d_head elements and that d_head splits
into the 4:6:6 pairs the graph expects.
---------
(cherry picked from commit 9f0e509)
      
      
  
    3 of 6 tasks
  
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
