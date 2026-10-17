---
id: "cb5cc3a81182cabb"
title: "model : add Kolibri-1 (Aleph-Alpha) support by riteme · Pull Request #30673 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30673"
link: "https://github.com/ggml-org/llama.cpp/pull/30673"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T11:07:59Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["jacek2023"]
language: "en"
summary: "European 78B A3.4B model is now supported by llama.cpp, I am waiting for some GGUFs https://huggingface.co/Aleph-Alpha/Kolibri-1 Kolibri is Aleph Alpha's mixture-of-experts (MoE) reasoning model, with a focus on German and English. The model supports an explicit reasoning mode and tool calling. It is optimized for long-context and inference efficiency. Model overview Model Kolibri 1 Model…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 517
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x87kgj/model_add_kolibri1_alephalpha_support_by_riteme/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# model : add Kolibri-1 (Aleph-Alpha) support by riteme · Pull Request #30673 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-10-17

Repository navigation
model : add Kolibri-1 (Aleph-Alpha) support - #30673
Merged
Merged
Conversation
      
          
github-actions
Bot
            added
      
  model
  Model specific 
      
  testing
  Everything test related 
      
  conversion
  labels
      Oct 16, 2026 
    
              
                    CISC
    
              
              approved these changes
              
                  
                    Oct 16, 2026 
                  
              
              
            
      
          
CISC
          added
  the 
  merge ready
  A maintainer can use this label to indicate that they consider the changes final and ready to merge. 
 label
      Oct 16, 2026 
    
3b9b5dd    to
    193c9eb      
    Compare
  
          Kolibri-1 is a bilingual German/English MoE reasoning model with 78B
parameters and 3.46B active per token: 50 layers, 384 routed experts plus
one shared expert.
Attention interleaves four sliding layers at a 513 window with one full
layer. The sliding layers rotate with NeoX RoPE, the full layers are NoPE.
GQA runs 48 query heads against 4 KV heads at head_dim 128 with a
QK-RMSNorm, and every block carries four RMSNorms, so the attention and the
MLP output are normalized before they rejoin the residual stream. Routing
picks the experts from logits + expert_bias and weights them with the
sigmoid of the unbiased logits, without renorm.
The converter reuses AfmoeModel for the per-expert checkpoint layout and
the expert selection bias, and writes the shared expert and the per layer
sliding window pattern. The released FP8 checkpoint needs no special code,
it goes through the generic weight_scale_inv path. Three tensor names are
added to the mapping (post_attn_norm, post_ffn_norm,
moe.router.expert_bias) and the 128k vocabulary registers the qwen2
pre-tokenizer by hash. The arch is registered in test-llama-archs, with GQA
and the sliding window pattern.
Assisted-by: DeepSeek Harness (DeepSeek V4.1 Flash)
Co-authored-by: Sigbjørn Skjæret <sigbjorn.skjaeret@huggingface.co>
        
  
    Contributor
        
  Author
    
      
          
CISC
          removed
  the 
  merge ready
  A maintainer can use this label to indicate that they consider the changes final and ready to merge. 
 label
      Oct 17, 2026 
    
        
  
  Member
        
    
              
                    CISC
    
              
              reviewed
              
                  
                    Oct 17, 2026 
                  
              
              
            
Co-authored-by: Sigbjørn Skjæret <sigbjorn.skjaeret@huggingface.co>
      
          
CISC
          added
  the 
  merge ready
  A maintainer can use this label to indicate that they consider the changes final and ready to merge. 
 label
      Oct 17, 2026 
    
              
                    ngxson
    
              
              approved these changes
              
                  
                    Oct 17, 2026 
                  
              
              
            
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
