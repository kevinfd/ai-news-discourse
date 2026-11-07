---
id: "b544e779aaaecb26"
title: "model: add Kimi-K3.1-Pro text model by usrlocalben · Pull Request #31779 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/31779"
link: "https://github.com/ggml-org/llama.cpp/pull/31779"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T22:49:45Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["jacek2023"]
language: "en"
summary: "now you can run Kimi K3.1 Pro locally (good luck!) ;) https://huggingface.co/moonshotai/Kimi-K3.1-Pro"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 618
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpqm0b/model_add_kimik31pro_text_model_by_usrlocalben/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# model: add Kimi-K3.1-Pro text model by usrlocalben · Pull Request #31779 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-11-06

Repository navigation
model: add Kimi-K3.1-Pro text model - #31779
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
      Nov 6, 2026 
    
        
  
    Contributor
        
    
              
                    CISC
    
              
              reviewed
              
                  
                    Nov 6, 2026 
                  
              
              
            
85cf1ab    to
    1fcebb8      
    Compare
  
          
              
                    CISC
    
              
              reviewed
              
                  
                    Nov 6, 2026 
                  
              
              
            
K3 with the full-attention MLA layers replaced by DSA: on this checkpoint 24
of the 93 layers carry a lightning indexer (32 heads x 128, top_k 2048, no
rope). The KDA (linear-attention) layers and the rest of the K3 skeleton -
cross-layer residuals, latent MoE, situ, MLA output gate, full-rank KDA gate -
are unchanged, so this reuses the K3 graph and converter and adds the indexer.
Indexer:
  - the selection is an additive mask over the whole cache, not a gather of
    the top-k rows, so it reuses the existing sparse flash attention path;
    off that path the mask stays correct but still costs a kq over the cache
  - the indexer key LayerNorm takes its eps from the model's rms_norm_eps,
    because dsa_config declares no eps of its own
Graph and cache:
  - new arch with four indexer tensors per DSA layer, and a hybrid memory
    that keeps a K-only MLA cache for those layers, recurrent state for the
    KDA layers, and the indexer key cache
  - the graph node budget shares the K3 entry
Conversion:
  - KimiK31Model(KimiK3Model), picked by KimiK31ForConditionalGeneration
  - dsa_config becomes attention.indexer.{head_count,key_length,top_k,types}
    plus the indexer LayerNorm eps; the layer list is 1-indexed like
    linear_attn_config's, and the converter asserts that it covers exactly
    the full-attention layers
  - the routed experts stay MXFP4 and are repacked as in K3, not dequantized
  - the vision tower and mm_projector are skipped: text only for now
  - the arch key follows the checkpoint's own model_type ("kimi_k31") and the
    loader registers KimiK31ForConditionalGeneration; the release name carries
    a -Pro suffix that nothing in the config or the tensor names uses
Quantisation: the indexer's q_b, k and proj are kept out of the quant
overrides, since the top-k selection is sensitive to their precision.
Verified on an 8-layer slice against the HF checkpoint: 38 tensors checked
exactly, the indexer metadata against the config, and the selection against
full attention - identical PPL at top_k beyond the context length, divergent
once top_k is forced below it. Arch test fixture and the full arch suite pass.
    b04cf49    to
    bd0235f      
    Compare
  
          
              
                    CISC
    
              
              approved these changes
              
                  
                    Nov 6, 2026 
                  
              
              
            
      
          
CISC
          added
  the 
  merge ready
  A maintainer can use this label to indicate that they consider the changes final and ready to merge. 
 label
      Nov 6, 2026 
    
              
                    ngxson
    
              
              approved these changes
              
                  
                    Nov 6, 2026 
                  
              
              
            
      
      
  
    3 of 6 tasks
  
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
