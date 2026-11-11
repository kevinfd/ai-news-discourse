---
id: "5da81b4ba195afa0"
title: "llama.cpp: Add FP8 KV-cache"
url: "https://github.com/ggml-org/llama.cpp/pull/28392"
link: "https://github.com/ggml-org/llama.cpp/pull/28392"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T05:36:19Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Kahvana"]
language: "en"
summary: "Repository navigation\nAdd FP8 KV-cache support - #28392\nMerged\nMerged\nAdd FP8 KV-cache support#28392\nConversation\n460bbd8    to\n    b6ccff9      \n    Compare\n  \n          b6ccff9    to\n    e8b60dd      \n    Compare\n  \n          55a7e53    to\n    b99e4ce      \n    Compare\n  \n          b99e4ce    to\n    f711e8c      \n    Compare\n  \n          f711e8c    to\n    d6c8682      \n    Compare\n  \n         …"
tags: ["r/LocalLLaMA"]
orgs: []
topics: []
content_source: "fulltext"
word_count: 312
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xt9o3t/llamacpp_add_fp8_kvcache/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# llama.cpp: Add FP8 KV-cache

GitHub · Kahvana · 2026-11-11

Repository navigation
Add FP8 KV-cache support - #28392
Merged
Merged
Add FP8 KV-cache support#28392
Conversation
460bbd8    to
    b6ccff9      
    Compare
  
          b6ccff9    to
    e8b60dd      
    Compare
  
          55a7e53    to
    b99e4ce      
    Compare
  
          b99e4ce    to
    f711e8c      
    Compare
  
          f711e8c    to
    d6c8682      
    Compare
  
          51f6a0f    to
    b5f3dfd      
    Compare
  
          c802335    to
    4602e64      
    Compare
  
          4602e64    to
    10e80e6      
    Compare
  
          
              ORippler
              marked this pull request as ready for review
          October 13, 2026 15:35           
        
              
                    pwilkin
    
              
              reviewed
              
                  
                    Oct 13, 2026 
                  
              
              
            
153b077    to
    f800827      
    Compare
  
          
        
  
    Collaborator
        
  Author
    
              
                    ggerganov
    
              
              reviewed
              
                  
                    Nov 9, 2026 
                  
              
              
            
While fused KQV is currently impractival for non-shared scales, this is
an improvement for future use regardless
They belong there as they are not just a test for ggml's backend ops
              
                    ggerganov
    
              
              approved these changes
              
                  
                    Nov 10, 2026 
                  
              
              
            
              
                    am17an
    
              
              approved these changes
              
                  
                    Nov 10, 2026 
                  
              
              
            
      
      
  
    3 of 6 tasks
  
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
