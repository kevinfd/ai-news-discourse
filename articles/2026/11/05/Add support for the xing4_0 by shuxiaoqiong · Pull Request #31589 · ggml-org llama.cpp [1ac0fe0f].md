---
id: "1ac0fe0fa3a5953e"
title: "Add support for the xing4_0 by shuxiaoqiong · Pull Request #31589 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/31589"
link: "https://github.com/ggml-org/llama.cpp/pull/31589"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T18:30:55Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["jacek2023"]
language: "en"
summary: "Xing4.0-29B-A4B is a next-generation large language model in the Xing series (formerly TeleChat ), developed by China Telecom Artificial Intelligence Technology Co., Ltd. With 29B total parameters and only 4B activated per token, it natively supports a 256K context length, extensible to 512K. It is the first model of this scale trained entirely on the Ascend NPU platform with the MindSpore…"
tags: ["r/LocalLLaMA"]
orgs: ["China"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 335
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xoqc59/add_support_for_the_xing4_0_by_shuxiaoqiong_pull/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Add support for the xing4_0 by shuxiaoqiong · Pull Request #31589 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-11-05

Repository navigation
Add support for the xing4_0 - #31589
Merged
Merged
Add support for the xing4_0 #31589
Conversation
      
        
              This comment was marked as off-topic.
        
              
                    CISC
    
              
              reviewed
              
                  
                    Nov 3, 2026 
                  
              
              
            
      
          
github-actions
Bot
            added
      
  model
  Model specific 
      
  testing
  Everything test related 
      
  conversion
  labels
      Nov 3, 2026 
    
              
                    CISC
    
              
              reviewed
              
                  
                    Nov 4, 2026 
                  
              
              
            
Co-authored-by: Sigbjørn Skjæret <sigbjorn.skjaeret@huggingface.co>
      
          
CISC
          added
  the 
  merge ready
  A maintainer can use this label to indicate that they consider the changes final and ready to merge. 
 label
      Nov 4, 2026 
    
      
          
CISC
          removed
  the 
  merge ready
  A maintainer can use this label to indicate that they consider the changes final and ready to merge. 
 label
      Nov 4, 2026 
    
        
  
  Member
        
    
        
  
    Contributor
        
  Author
    
              
                    CISC
    
              
              approved these changes
              
                  
                    Nov 4, 2026 
                  
              
              
            
              
                    ngxson
    
              
              reviewed
              
                  
                    Nov 4, 2026 
                  
              
              
            
      Comment on lines
    
      +455
     to 
      +467
    
  
      
      
  
    2 of 4 tasks
  
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
        
  
    Collaborator
        
    
        
  
  Member
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
      
      
  
    3 of 6 tasks
  
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
