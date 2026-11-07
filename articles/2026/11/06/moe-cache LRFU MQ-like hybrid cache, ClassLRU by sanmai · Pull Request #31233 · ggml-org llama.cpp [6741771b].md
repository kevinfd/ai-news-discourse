---
id: "6741771ba842685e"
title: "moe-cache : LRFU/MQ-like hybrid cache, ClassLRU by sanmai · Pull Request #31233 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/31233"
link: "https://github.com/ggml-org/llama.cpp/pull/31233"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T15:39:09Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["pmttyji"]
language: "en"
summary: "Replace SLRU with a cache that prioritizes frequently used experts in classes, ranked using decaying usage history. With a warm cache, I measured +6% decode on QFN and +7% on GLM versus SLRU, with 8% fewer uploads. Enables the auto mode for llama_moe_cache with promising benchmarks Waiting for 30966 to be merged."
tags: ["r/LocalLLaMA"]
orgs: []
topics: []
content_source: "fulltext"
word_count: 531
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpfvfz/moecache_lrfumqlike_hybrid_cache_classlru_by/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# moe-cache : LRFU/MQ-like hybrid cache, ClassLRU by sanmai · Pull Request #31233 · ggml-org/llama.cpp

GitHub · pmttyji · 2026-11-06

Repository navigation
moe-cache : LRFU/MQ-like hybrid cache, ClassLRU - #31233
Merged
Merged
Conversation
              
                    sanmai
    
              
              commented
              
                  
                    Oct 27, 2026 
                  
              
              
            
              sanmai
              marked this pull request as ready for review
          October 27, 2026 10:17           
        
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
    
              sanmai
              marked this pull request as draft
          October 27, 2026 12:02           
        
…s always 1, ids have n_expert_used entries per token)
      
      
  
    1 task done
  
        
  
    Contributor
        
  Author
    
…e[1] is the count
        
  
    Contributor
        
    
        
  
    Collaborator
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
        
  
    Collaborator
        
    
        
  
    Contributor
        
  Author
    
        
  
    Collaborator
        
    
        
  
    Contributor
        
    
              
                    sanmai
    
              
              commented
              
                  
                    Oct 29, 2026 
                  
              
              
            
              
                    sanmai
    
              
              commented
              
                  
                    Oct 29, 2026 
                  
              
              
            
      
          
sanmai
        changed the title
moe-cache : LRFU/MQ-inspired hybrid cache, ClassLRU
moe-cache : LRFU/MQ-like hybrid cache, ClassLRU
      Oct 29, 2026 
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
        
  
    Collaborator
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
        
  
    Collaborator
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
    
  imaami 
      pushed a commit
        to imaami/llama.cpp
      that referenced
      this pull request
    
      Nov 2, 2026 
    
    
      
  
    
      Picked from ggml-org#31233 (open at the time of picking),
head 8be980f, net diff against its merge base 7aca0d2:
  6a8bf8e moe-cache : LRFU/MQ-inspired hybrid cache
  5dd386c make the clock advance by N tokens: use the real token count (ne[1] is always 1, ids have
  9ac703c sel is a RESHAPE node, the orig input is in src[0], so sel->src[0]->ne[1] is the count
  9f4c30d c for the class index, last_use for last use time
  c09c6f5 explain the roles of these
  e05f14e compute the key once
  b7c08c5 use the key directly instead of re-reading
  231bc3e show how the score is computed from the age
  98ce01e remove the branch and clarify exp2 and log2 relationship
  cfea435 reword the header comment and elaborate on unused slots and sorting
  82466a9 not a copy, not just skip
  7649b1f std::array maybe
  1ba27ea Revert "std::array maybe"
  5e2fe31 half life it is
  2797967 add key and iteration helpers
  a00d1bc extract decayed_crf
  8be980f bump classes to 8, document the formula, display the cache size in token worth count
        
  
    Contributor
        
  Author
    
              
                    am17an
    
              
              approved these changes
              
                  
                    Nov 6, 2026 
                  
              
              
            
        
  
    Contributor
        
  Author
    
      
          
sanmai
          added
  the 
  merge ready
  A maintainer can use this label to indicate that they consider the changes final and ready to merge. 
 label
      Nov 6, 2026 
    
        
  
    Collaborator
        
    
        
  
    Contributor
        
  Author
    
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
