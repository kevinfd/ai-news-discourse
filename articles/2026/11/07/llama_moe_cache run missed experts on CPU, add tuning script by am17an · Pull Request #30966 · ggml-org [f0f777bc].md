---
id: "f0f777bc10c205fa"
title: "llama_moe_cache: run missed experts on CPU, add tuning script by am17an · Pull Request #30966 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30966"
link: "https://github.com/ggml-org/llama.cpp/pull/30966"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T16:25:06Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["jacek2023"]
language: "en"
summary: "This is a significant speedup for MoE offloading (low VRAM people). I tried Strata once, and it had some tuning mechanism, so probably this is a similar idea."
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure", "business & funding"]
content_source: "fulltext"
word_count: 1581
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xqacka/llama_moe_cache_run_missed_experts_on_cpu_add/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# llama_moe_cache: run missed experts on CPU, add tuning script by am17an · Pull Request #30966 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-11-07

Repository navigation
llama_moe_cache: run missed experts on CPU, add tuning script - #30966
Merged
Merged
Conversation
      
          
github-actions
Bot
            added
      
  documentation
  Improvements or additions to documentation 
      
  server
      
  ggml
  changes relating to the ggml tensor library for machine learning 
  labels
      Oct 22, 2026 
    
d923838    to
    c41b895      
    Compare
  
          
    
  gouglhupf 
      pushed a commit
        to gouglhupf/llama.cpp
      that referenced
      this pull request
    
      Oct 22, 2026 
    
    
      
  
    
      squashed pick of ggml-org#30966 : compute part of the MoE cache
misses on the CPU, add moe-cache-tune.py tuning script, CODEOWNERS entry
Assisted-by: GLM-5.3-Flash
        
  
  Member
        
    
        
  
  Member
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
    
  gouglhupf 
      pushed a commit
        to gouglhupf/llama.cpp
      that referenced
      this pull request
    
      Oct 23, 2026 
    
    
      
  
    
      squashed pick of ggml-org#30966 : compute part of the MoE cache
misses on the CPU, add moe-cache-tune.py tuning script, CODEOWNERS entry
Assisted-by: GLM-5.3-Flash
              
                    eapache
    
              
              reviewed
              
                  
                    Oct 23, 2026 
                  
              
              
            
    
  gouglhupf 
      pushed a commit
        to gouglhupf/llama.cpp
      that referenced
      this pull request
    
      Oct 25, 2026 
    
    
      
  
    
      squashed pick of ggml-org#30966 : compute part of the MoE cache
misses on the CPU, add moe-cache-tune.py tuning script, CODEOWNERS entry
Assisted-by: GLM-5.3-Flash
bffc558    to
    4899779      
    Compare
  
          
        
  
    Contributor
        
  Author
    
    
  gouglhupf 
      pushed a commit
        to gouglhupf/llama.cpp
      that referenced
      this pull request
    
      Nov 4, 2026 
    
    
      
  
    
      squashed pick of ggml-org#30966 : compute part of the MoE cache
misses on the CPU, add moe-cache-tune.py tuning script, CODEOWNERS entry
Assisted-by: GPT 6.1 Sol
        
  
    Collaborator
        
    
--moe-cache-cpu-share F computes a share F of the MoE cache misses on the CPU
from the host experts instead of uploading them. The graph builds the expert
FFN twice: on the device from the cache slots, where the misses left to the CPU
read zero slots, and on the CPU from the host experts, where the experts
computed on the device have id -1. The two results are added before the down
bias.
- ggml-cpu: MUL_MAT_ID skips negative ids and writes zero rows
- sched: the copy callback is called for all the inputs of a split, and before
  the host sync when there are no events
- the slot lookup callback reads the inputs of the CPU part together with the
  selected experts, so the CPU part does not wait for the device, and its
  result is copied back asynchronously
- each token uses distinct zero slots, mul_mat_id does not support an expert
  selected twice by a token
- LLAMA_MOE_CACHE_TRACE writes the selected experts of each lookup, for a
  simulator of the cache
The script wraps a llama-server command: it starts the server at two cache
sizes and three CPU shares, fits the upload and CPU speeds of the machine, and
replays the routing of the runs through a copy of the cache logic to predict
other sizes and shares. It prints the recommended --moe-cache-mib and
--moe-cache-cpu-share.
docs/moe-cache.md describes the MoE cache arguments and the script.
With a high --moe-cache-cpu-share, few misses are uploaded, so an empty cache
fills slowly and more misses than needed go to the CPU. The CPU share now
starts once all the slots of a cache group hold an expert. moe-cache-tune.py
replays the same rule.
The graph construction no longer updates the MoE cache directly: the CPU
parts of the layers are accumulated in the graph result and applied to
the cache in llama_context::process_ubatch, after the graph inputs are
set and before the graph is computed.
Assisted-by: dsh:llama.cpp/ggml-org/GLM-5.3-Flash-GGUF (Mac Studio, M5 Ultra, 256GB)
c6eb877    to
    0290c8d      
    Compare
  
          
        
  
    Contributor
        
  Author
    
        
  
  Member
        
    
The CPU part reads the host experts, so the scheduler places it on the
CPU without set_tensor_backend. The cache gives no CPU map for batches
that a device would offload. Graphs with a CPU part look up their own
slot map, so the graph does not register the part with the cache.
ggml-backend : the inputs of the next split that are already computed
are copied to host memory before the current split runs, so a CPU split
does not wait for the device split before it. This replaces the stash
of the cache, and the copy callback is again called for host weights
only.
              
                    ggerganov
    
              
              reviewed
              
                  
                    Nov 7, 2026 
                  
              
              
            
The scheduler prefetch no longer checks that the next split runs on
another backend: the inputs of a split are never on its own backend,
so the input loop already skips that case.
              
                    ggerganov
    
              
              approved these changes
              
                  
                    Nov 7, 2026 
                  
              
              
            
    
  linellazatin 
      pushed a commit
        to linellazatin/llama.cpp
      that referenced
      this pull request
    
      Nov 7, 2026 
    
    
      
  
    
      …rg#30966)
* moe-cache : compute part of the misses on the CPU
--moe-cache-cpu-share F computes a share F of the MoE cache misses on the CPU
from the host experts instead of uploading them. The graph builds the expert
FFN twice: on the device from the cache slots, where the misses left to the CPU
read zero slots, and on the CPU from the host experts, where the experts
computed on the device have id -1. The two results are added before the down
bias.
- ggml-cpu: MUL_MAT_ID skips negative ids and writes zero rows
- sched: the copy callback is called for all the inputs of a split, and before
  the host sync when there are no events
- the slot lookup callback reads the inputs of the CPU part together with the
  selected experts, so the CPU part does not wait for the device, and its
  result is copied back asynchronously
- each token uses distinct zero slots, mul_mat_id does not support an expert
  selected twice by a token
- LLAMA_MOE_CACHE_TRACE writes the selected experts of each lookup, for a
  simulator of the cache
* scripts : add moe-cache-tune.py to pick the MoE cache arguments
The script wraps a llama-server command: it starts the server at two cache
sizes and three CPU shares, fits the upload and CPU speeds of the machine, and
replays the routing of the runs through a copy of the cache logic to predict
other sizes and shares. It prints the recommended --moe-cache-mib and
--moe-cache-cpu-share.
docs/moe-cache.md describes the MoE cache arguments and the script.
* add am17an as codeowner for MoE cache
* moe-cache : upload all the misses until the cache is full
With a high --moe-cache-cpu-share, few misses are uploaded, so an empty cache
fills slowly and more misses than needed go to the CPU. The CPU share now
starts once all the slots of a cache group hold an expert. moe-cache-tune.py
replays the same rule.
* add backend sync for async transfer queue
* moe-cache : let the scheduler copy the results of the CPU part
* Fix MSVC compilation
* remove sync change
* llama-graph : extract the CPU share condition into can_cpu_share
* llama-graph : make llm_graph_params::moe_cache const
The graph construction no longer updates the MoE cache directly: the CPU
parts of the layers are accumulated in the graph result and applied to
the cache in llama_context::process_ubatch, after the graph inputs are
set and before the graph is computed.
Assisted-by: dsh:llama.cpp/ggml-org/GLM-5.3-Flash-GGUF (Mac Studio, M5 Ultra, 256GB)
* scripts : replay the ClassLRU policy in moe-cache-tune.py
* moe-cache : pick CPU misses by CRF instead of random (ggml-org#31853)
* moe-cache : remove the backend logic of the CPU part from the graph
The CPU part reads the host experts, so the scheduler places it on the
CPU without set_tensor_backend. The cache gives no CPU map for batches
that a device would offload. Graphs with a CPU part look up their own
slot map, so the graph does not register the part with the cache.
ggml-backend : the inputs of the next split that are already computed
are copied to host memory before the current split runs, so a CPU split
does not wait for the device split before it. This replaces the stash
of the cache, and the copy callback is again called for host weights
only.
* llama-graph : return the MoE cache slots and CPU ids in a struct
The scheduler prefetch no longer checks that the next split runs on
another backend: the inputs of a split are never on its own backend,
so the input loop already skips that case.
---------
Co-authored-by: Gaurav Garg <gaugarg@nvidia.com>
Co-authored-by: Georgi Gerganov <ggerganov@gmail.com>
Co-authored-by: Alexey Kopytko <alexey@kopytko.com>
    
  linellazatin 
      added a commit
        to linellazatin/llama.cpp
      that referenced
      this pull request
    
      Nov 7, 2026 
    
    
  
    
  neurall 
      added a commit
        to neurall/llama.cpp
      that referenced
      this pull request
    
      Nov 8, 2026 
    
    
      
  
    
      …_norm, server parent slots); the MoE cache CPU share (ggml-org#30966) follows separately
    
  neurall 
      added a commit
        to neurall/llama.cpp
      that referenced
      this pull request
    
      Nov 8, 2026 
    
    
      
  
    
      …ggml-org#30966), planner two-sample rule, run history
      
      
  
    3 of 6 tasks
  
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
