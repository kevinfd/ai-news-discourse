---
id: "5708842e035554ac"
title: "Title: CUDA: few-row MMQ for BS 2-24 by anujj · Pull Request #31533 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/31533"
link: "https://github.com/ggml-org/llama.cpp/pull/31533"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T14:10:23Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["pmttyji"]
language: "en"
summary: "Speculative decoding (SPEED-Bench) llama-server -m Qwen3.8-27B-UD-Q4_K_M.gguf --mmproj mmproj-F16.gguf -ngl 999 --parallel 1 --batch-size 4096 --ubatch-size 1024 --ctx-size 180224 \\ --spec-type draft-dflash --spec-draft-n-max 7 --spec-draft-model Qwen3.8-27B-DFlash2-Q4_K_M.gguf --spec-draft-backend-sampling \\ --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 --presence-penalty 0.0 --repeat-penalty…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "AMD"]
topics: ["chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 1335
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xudqle/title_cuda_fewrow_mmq_for_bs_224_by_anujj_pull/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Title: CUDA: few-row MMQ for BS 2-24 by anujj · Pull Request #31533 · ggml-org/llama.cpp

GitHub · pmttyji · 2026-11-12

Repository navigation
Title: CUDA: few-row MMQ for BS 2-24 - #31533
Merged
Merged
Conversation
New int8 MMA kernel for quantized mat-muls with 2-24 src1 columns, e.g. speculative decoding verify passes.
Supports Q8_0, Q3_K, Q4_K, Q5_K, Q6_K, IQ3_S, IQ4_NL and IQ4_XS on NVIDIA GPUs from Ampere on.
      
          
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
      Nov 2, 2026 
    
              anujj
              marked this pull request as ready for review
          November 2, 2026 13:10           
        
    
  vvsotnikov 
      added a commit
        to vvsotnikov/llama.cpp
      that referenced
      this pull request
    
      Nov 4, 2026 
    
    
      
  
    
      Keep the new async-copy and scale helpers local to the few-row path.
Retain the existing Ada small-projection route and the original MMVQ/MMQ
implementations outside that path. Based on upstream PR ggml-org#31533.
Assisted-by: Codex
        
  
    Contributor
        
  Author
    
              
                    ORippler
    
              
              reviewed
              
                  
                    Nov 6, 2026 
                  
              
              
            
      Comment on lines
    
      +29
     to 
      +34
    
  
        
  
    Collaborator
        
    
        
  
    Contributor
        
    
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
# Conflicts:
#	tests/test-backend-ops.cpp
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
    
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
    
  pratiknarola-t 
      added a commit
        to tetherto/qvac-fabric-llm.cpp
      that referenced
      this pull request
    
      Nov 11, 2026 
    
    
      
  
    
      Port of ggml-org#31533 (head ffce469). At 2..24 src1
columns MMVQ repeats its multiply work for every column, and MMQ gets
too few 128-row tiles, so stream-k splits K and needs its fixup
kernel. The few-row kernel reads each weight once, decodes it once into
int8 MMA fragments and multiplies it with all columns. The 4 warps of
a block split K, each with its own cp.async ring, and src1 is quantized
straight into the fragment layout. It covers Q8_0, Q3_K, Q4_K, Q5_K,
Q6_K, IQ3_S, IQ4_NL and IQ4_XS on NVIDIA Ampere to Blackwell, from a
per-type minimum column count tuned on the RTX 5090 (DGX Spark has its
own row). Results are deterministic.
Differences from the upstream diff:
- ggml-cuda.cu: fabric has no upstream MMQ fusion, so only the include
  and the dispatch in ggml_cuda_mul_mat_canonical (after MMF, before
  MMVQ) apply.
- cp-async.cuh: fabric already has cp_async_commit_group and
  cp_async_wait_group with the same PTX.
- mmvq.cu: fabric's DGX Spark prefetch uses the shared
  ggml_cuda_prefetch_l2 (GB10 SASS unchanged).
- test-backend-ops: the PR's cases, plus cases at 4, 6, 7 and 17
  columns with K >= 2048, where per-type column ranges start.
Decode step at B columns, paired runs (llama-batched-bench) against
the base:
- RTX 3080: Qwen3.5-9B Q4_K_M -9.5/-14.9/-23.6/-30.0/-36.0% at B4..8
  (B8 19.65 to 12.57 ms), B1..2 unchanged, +1.2% at B3: the RTX 5090
  table starts Q5_K at 3 columns, where the kernel is 7% slower per op
  than MMVQ on this GPU. Qwen3-8B Q8_0 -2.3/-7.8/-13.4% at B6..8,
  B1..5 unchanged.
- GB10: Qwen3.5-9B Q4_K_M -7.5..-9.0% at B2..8, B1 unchanged.
  Qwen3.8-27B Q8_0 -4.9..-5.2% at B2..4, -7.0..-7.4% at B6..8.
Logits stay within the spread of the existing paths: against batch-512
(MMQ) logits, KLD at 4 and 8 columns matches the base's.
    
  pratiknarola-t 
      added a commit
        to tetherto/qvac-fabric-llm.cpp
      that referenced
      this pull request
    
      Nov 11, 2026 
    
    
      
  
    
      Port of ggml-org/llama.cpp commit 6ad15f4 ("HIP: RDNA3 WMMA path for
few-row MMQ"), posted on ggml-org#31533. It adds a 16x16x16
int8 WMMA form of the few-row kernel for Q4_K, Q5_K, Q6_K, Q8_0 and
IQ4_NL on RDNA3 and RDNA3.5, with its own src1 fragment layout and
per-type column ranges tuned on a Radeon 8060S. The lanes decode the
weights straight from global memory.
The file guard becomes !GGML_USE_MUSA. The device code stays behind
CP_ASYNC_AVAILABLE (NVIDIA) and __GFX11__ (RDNA3), and the host takes
the WMMA path only for GGML_CUDA_CC_IS_RDNA3, so other AMD GPUs keep
MMVQ and MMQ. The quantize kernel computes the head's sum of the
quantized values before the WMMA layout branch.
Decode step at B columns on a Radeon 8060S (ROCm 7.2.2, gfx1151),
paired runs (llama-batched-bench) against the base:
- Qwen3.5-9B Q4_K_M: -6.5/-14.8/-21.7/-28.9% at B5..8 (B8 48.04 to
  34.15 ms), B1..2 and B4 unchanged, +3.3% at B3 (next commit).
- Qwen3.5-9B Q8_0: unchanged at B1..8 (Q8_0 uses it from 17 columns).
        
  
    Collaborator
        
    
              
                    ORippler
    
              
              reviewed
              
                  
                    Nov 11, 2026 
                  
              
              
            
      Comment on lines
    
      +2312
     to 
      +2316
    
  
        
  
    Collaborator
        
    
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
      
      
  
    1 task done
  
      
      
  
    3 of 6 tasks
  
    
  JenySadadia 
      pushed a commit
        to tetherto/qvac-fabric-llm.cpp
      that referenced
      this pull request
    
      Nov 13, 2026 
    
    
      
  
    
      Port of ggml-org#31533 (head ffce469). At 2..24 src1
columns MMVQ repeats its multiply work for every column, and MMQ gets
too few 128-row tiles, so stream-k splits K and needs its fixup
kernel. The few-row kernel reads each weight once, decodes it once into
int8 MMA fragments and multiplies it with all columns. The 4 warps of
a block split K, each with its own cp.async ring, and src1 is quantized
straight into the fragment layout. It covers Q8_0, Q3_K, Q4_K, Q5_K,
Q6_K, IQ3_S, IQ4_NL and IQ4_XS on NVIDIA Ampere to Blackwell, from a
per-type minimum column count tuned on the RTX 5090 (DGX Spark has its
own row). Results are deterministic.
Differences from the upstream diff:
- ggml-cuda.cu: fabric has no upstream MMQ fusion, so only the include
  and the dispatch in ggml_cuda_mul_mat_canonical (after MMF, before
  MMVQ) apply.
- cp-async.cuh: fabric already has cp_async_commit_group and
  cp_async_wait_group with the same PTX.
- mmvq.cu: fabric's DGX Spark prefetch uses the shared
  ggml_cuda_prefetch_l2 (GB10 SASS unchanged).
- test-backend-ops: the PR's cases, plus cases at 4, 6, 7 and 17
  columns with K >= 2048, where per-type column ranges start.
Decode step at B columns, paired runs (llama-batched-bench) against
the base:
- RTX 3080: Qwen3.5-9B Q4_K_M -9.5/-14.9/-23.6/-30.0/-36.0% at B4..8
  (B8 19.65 to 12.57 ms), B1..2 unchanged, +1.2% at B3: the RTX 5090
  table starts Q5_K at 3 columns, where the kernel is 7% slower per op
  than MMVQ on this GPU. Qwen3-8B Q8_0 -2.3/-7.8/-13.4% at B6..8,
  B1..5 unchanged.
- GB10: Qwen3.5-9B Q4_K_M -7.5..-9.0% at B2..8, B1 unchanged.
  Qwen3.8-27B Q8_0 -4.9..-5.2% at B2..4, -7.0..-7.4% at B6..8.
Logits stay within the spread of the existing paths: against batch-512
(MMQ) logits, KLD at 4 and 8 columns matches the base's.
(cherry picked from commit 1d94f50)
    
  JenySadadia 
      pushed a commit
        to tetherto/qvac-fabric-llm.cpp
      that referenced
      this pull request
    
      Nov 13, 2026 
    
    
      
  
    
      Port of ggml-org/llama.cpp commit 6ad15f4 ("HIP: RDNA3 WMMA path for
few-row MMQ"), posted on ggml-org#31533. It adds a 16x16x16
int8 WMMA form of the few-row kernel for Q4_K, Q5_K, Q6_K, Q8_0 and
IQ4_NL on RDNA3 and RDNA3.5, with its own src1 fragment layout and
per-type column ranges tuned on a Radeon 8060S. The lanes decode the
weights straight from global memory.
The file guard becomes !GGML_USE_MUSA. The device code stays behind
CP_ASYNC_AVAILABLE (NVIDIA) and __GFX11__ (RDNA3), and the host takes
the WMMA path only for GGML_CUDA_CC_IS_RDNA3, so other AMD GPUs keep
MMVQ and MMQ. The quantize kernel computes the head's sum of the
quantized values before the WMMA layout branch.
Decode step at B columns on a Radeon 8060S (ROCm 7.2.2, gfx1151),
paired runs (llama-batched-bench) against the base:
- Qwen3.5-9B Q4_K_M: -6.5/-14.8/-21.7/-28.9% at B5..8 (B8 48.04 to
  34.15 ms), B1..2 and B4 unchanged, +3.3% at B3 (next commit).
- Qwen3.5-9B Q8_0: unchanged at B1..8 (Q8_0 uses it from 17 columns).
(cherry picked from commit c40a907)
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
