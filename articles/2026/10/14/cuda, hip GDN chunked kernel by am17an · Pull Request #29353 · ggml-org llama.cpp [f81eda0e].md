---
id: "f81eda0e2caeaae4"
title: "cuda, hip: GDN chunked kernel by am17an · Pull Request #29353 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/29353"
link: "https://github.com/ggml-org/llama.cpp/pull/29353"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T14:23:13Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["jacek2023"]
language: "en"
summary: "Performance on Model Prompt tokens master tok/s pr tok/s Change RTX PRO 6000 Blackwell Qwen3.5-35B-A3B-Q8_0 2048 13,653.58 16,459.56 +20.6% RTX PRO 6000 Blackwell Qwen3.5-35B-A3B-Q8_0 4096 14,090.26 16,595.47 +17.8% RTX PRO 6000 Blackwell Qwen3.8-27B-Q8_0 2048 4,470.39 4,757.20 +6.4% RTX PRO 6000 Blackwell Qwen3.8-27B-Q8_0 4096 4,442.45 4,699.08 +5.8% Spark GB10 Qwen3.6-35B-A3B-UD-Q4_K_M 2048…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic"]
topics: []
content_source: "fulltext"
word_count: 790
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5skta/cuda_hip_gdn_chunked_kernel_by_am17an_pull/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# cuda, hip: GDN chunked kernel by am17an · Pull Request #29353 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-10-14

Repository navigation
cuda, hip: GDN chunked kernel - #29353
Merged
Merged
Conversation
Ported-from: tetherto#257
Source-commit: 53f0027
Co-authored-by: Aman Gupta <aman.gupta@tether.io>
      
          
github-actions
Bot
            added
      
  testing
  Everything test related 
      
  ggml
  changes relating to the ggml tensor library for machine learning 
      
  CUDA
  Related to the CUDA backend 
  labels
      Sep 24, 2026 
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
              
                    IMbackK
    
              
              previously requested changes
              
                  
                    Sep 24, 2026 
                  
              
              
            
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
Enable SM86 and SM89 after RTX 3090 and RTX 4090 correctness and prefill benchmarks. Keep other untested architectures on the existing fallback.
Assisted-by: Codex
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
    
        
  
    Contributor
        
    
        
  
    Contributor
        
    
              
                    ORippler
    
              
              reviewed
              
                  
                    Sep 28, 2026 
                  
              
              
            
      Comment on lines
    
      +307
     to 
      +314
    
  
        
  
    Collaborator
        
    
        
  
    Contributor
        
    
    
  baykalokandemir 
      added a commit
        to baykalokandemir/llama.cpp-bells-tortured
      that referenced
      this pull request
    
      Sep 28, 2026 
    
    
      
  
    
      …s K == 1, we run K = 3); prefill unchanged
Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_018co7fcJoEQXMxLezg7HpMU
    
  sourenaraya 
      added a commit
        to sourenaraya/llama.cpp
      that referenced
      this pull request
    
      Oct 7, 2026 
    
    
  
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
        
  
  Member
        
    
        
  
    Contributor
        
  Author
    
        
  
  Member
        
    
        
  
  Member
        
    
# Conflicts:
#	ggml/src/ggml-cuda/gated_delta_net.cu
#	ggml/src/ggml-cuda/mma.cuh
        
  
    Contributor
        
  Author
    
  This was referenced Oct 13, 2026 
    
  professorpalmer 
      added a commit
        to professorpalmer/llama.cpp-ada-ternary
      that referenced
      this pull request
    
      Oct 13, 2026 
    
    
      
  
    
      Prefill-sized GATED_DELTA_NET ops run a chunked tensor-core kernel instead of
the per-token recurrent kernel. The raw gates are activated into temporaries
first. With K > 1 state snapshots (one sequence), the MMA kernel runs the first
n - K tokens and the recurrent kernel the last K, which write the snapshot
slots. The fused state gather is supported: the live state rows are copied to
a contiguous s0 first. One WARN line when the chunked path first engages, and
one when a prefill-sized op skips it.
BF16 MMA on Ampere GA10x / Ada and newer. Other cards are checked before any
temporaries are allocated and keep the recurrent kernel (one WARN line with the
device cc). GGML_CUDA_GDN_MMA_DISABLE=1 turns it off. Tests in the 27B shape.
RTX 4070: prefill +3 to +6 % (drafting on); perplexity 8.0714 -> 8.0733
(+0.024 %, -c 2048, 32 chunks); exact copies and needles unchanged.
RTX 2060 SUPER (sm_75): not taken; 32k prefill and decode unchanged.
    
  professorpalmer 
      added a commit
        to professorpalmer/bonsai-ada-surgery
      that referenced
      this pull request
    
      Oct 13, 2026 
    
    
      
  
    
      …lama.cpp#29353) (#40)
* patches: 0054 chunked gated-delta-net MMA prefill (port of ggml-org/llama.cpp#29353); README: rows 0050 and 0054, patch counts 54
* patches: 0054 checks the device before the GDN MMA temporaries (RTX 20: clean skip line, no allocations)
---------
Co-authored-by: Cary Palmer <24235924+professorpalmer@users.noreply.github.com>
    
  edwardyoon 
      pushed a commit
        to edwardyoon/focus-llama
      that referenced
      this pull request
    
      Oct 14, 2026 
    
    
  
              
                    ORippler
    
              
              approved these changes
              
                  
                    Oct 14, 2026 
                  
              
              
            
      
      
  
    3 of 5 tasks
  
    
  professorpalmer 
      added a commit
        to professorpalmer/llama.cpp-ada-mirai
      that referenced
      this pull request
    
      Oct 15, 2026 
    
    
      
  
    
      …#29353)
Prefill-sized GATED_DELTA_NET ops run a chunked tensor-core kernel instead of
the per-token recurrent kernel. The raw gates are activated into temporaries
first. With K > 1 state snapshots (one sequence), the MMA kernel runs the first
n - K tokens and the recurrent kernel the last K, which write the snapshot
slots. The fused state gather is supported: the live state rows are copied to
a contiguous s0 first. One WARN line when the chunked path first engages, and
one when a prefill-sized op skips it.
BF16 MMA on Ampere GA10x / Ada and newer. Other cards are checked before any
temporaries are allocated and keep the recurrent kernel (one WARN line with the
device cc). GGML_CUDA_GDN_MMA_DISABLE=1 turns it off. Tests in the 27B shape.
RTX 4070: prefill +3 to +6 % (drafting on); perplexity 8.0714 -> 8.0733
(+0.024 %, -c 2048, 32 chunks); exact copies and needles unchanged.
RTX 2060 SUPER (sm_75): not taken; 32k prefill and decode unchanged.
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
