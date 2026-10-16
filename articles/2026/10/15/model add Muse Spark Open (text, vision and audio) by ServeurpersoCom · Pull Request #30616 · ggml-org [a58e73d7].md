---
id: "a58e73d7d5cb580d"
title: "model: add Muse Spark Open (text, vision and audio) by ServeurpersoCom · Pull Request #30616 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30616"
link: "https://github.com/ggml-org/llama.cpp/pull/30616"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T21:51:31Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["jacek2023"]
language: "en"
summary: "https://huggingface.co/ggml-org/Muse-Spark-Open-816B-A42B-GGUF merged after 4h"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 972
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6youd/model_add_muse_spark_open_text_vision_and_audio/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# model: add Muse Spark Open (text, vision and audio) by ServeurpersoCom · Pull Request #30616 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-10-15

Repository navigation
model: add Muse Spark Open (text, vision and audio) - #30616
Merged
ServeurpersoCom merged 9 commits intoOct 15, 2026 
Merged
Conversation
Muse Spark Open is a latent space MoE: the residual stream stays at 8192
while the 256 experts live in 4096, with a projection down and up around
them, top-8 sigmoid routing with a correction bias. Attention interleaves
three sliding layers at a 2048 window with rope for one global layer
without rope, with a sigmoid output gate and a weightless QK-norm.
Residuals are norm preserving, their gate is folded at conversion time.
Vision reuses the Muse Glimmer tower. Audio is a causal convolutional
pyramid with no attention and no spectrogram, four stages folding 16, 6,
5 and 4 samples into the channel dim, one embedding per 80 ms of 24 kHz.
The quantizer keeps the latent projections and the attention gate at
Q8_0, a little over 1% of the weights, since the whole residual stream
passes through them and the low-bit types turned the output into a
repeating loop. The model saver writes the post norm epsilon, and the
arch is registered in test-llama-archs.
Co-authored-by: Xuan Son Nguyen <son@huggingface.co>
Co-authored-by: Pedro Cuenca <pedro@huggingface.co>
      
          
github-actions
Bot
            added
      
  model
  Model specific 
      
  testing
  Everything test related 
      
  mtmd
  Related to multimodal functionality (video/image/audio) 
      
  conversion
  labels
      Oct 15, 2026 
    
              
                    ggerganov
    
              
              approved these changes
              
                  
                    Oct 15, 2026 
                  
              
              
            
        
  
    Contributor
        
  Author
    
              
                    CISC
    
              
              approved these changes
              
                  
                    Oct 15, 2026 
                  
              
              
            
        
  
    Contributor
        
    
    
  danielhanchen 
      added a commit
        to unslothai/unsloth
      that referenced
      this pull request
    
      Oct 15, 2026 
    
    
      
  
    
      ## Summary
Studio support for the Muse Spark Open GGUFs
(`unsloth/Muse-Spark-Open-816B-A42B-GGUF`, llama.cpp arch `muse-spark`,
loaded through the prebuilt llama.cpp that carries
ggml-org/llama.cpp#30616).
- **Sampling defaults.** A new `muse-spark` family uses the model card
settings: temperature 1.0, top_p 1.0, top_k disabled, and min_p 0.0. The
Hugging Face generation_config.json lists top_k 64, but the model card
recommends top_k disabled and its benchmarks use that, so the card wins.
Before this, every Muse Spark id fell through to `default.yaml` (0.7 /
0.95 / min_p 0.01).
- top_k is stored as -1, Studio's "disabled" value. The llama-server
payload sends it as 0, which llama.cpp reads as no top-k cutoff.
- The pattern sits next to `muse-glimmer`, so Glimmer keeps its own 0.95
/ 64.
- **Reasoning effort.** The Muse Spark chat template accepts
`reasoning_effort` low, medium, high or xhigh (default xhigh). Any other
value hits `raise_exception`, and the render fails.
- Before this change, the request builder forwarded the OpenAI `none`
sentinel as-is, and the default-effort path forwarded `none`, `minimal`
and `max`. All of them failed.
- Muse Spark cannot turn reasoning off. So for the `muse-spark`
architecture only, `none` and `minimal` now map to `low` and `max` maps
to `xhigh`. Inkling's numeric mapping and every other architecture are
unchanged.
## Already handled by main (verified, no change needed)
- **Variant menu.** On the real repo listing, the menu shows exactly the
eight quants: UD-IQ1_S, UD-IQ1_M, UD-IQ2_XXS, UD-IQ2_S, UD-IQ3_XXS,
UD-Q2_K_XL, UD-Q3_K_XL and UD-Q4_K_XL.
  - Each quant resolves to shard 1 plus its remaining shards.
- The root `imatrix_unsloth.gguf` is never offered as a variant and
never picked as the model.
- **Reasoning detection.** Detection publishes the four effort levels
and tool support.
- The template opens reasoning with `<|start|>assistant
to=self<|message|>`, so the existing recipient-channel parser handles
the output: `self` is reasoning, `user` is the reply.
- **Memory planner.** Tested on the real UD-IQ1_S metadata (62 blocks:
16 full-attention and 46 sliding-window layers; 163.6 GiB of weights).
The planner fits 134144 tokens of context on a single B200. Larger
context requests and smaller cards spread across 2 or 3 GPUs without
errors.
## Testing
- **New tests:** `tests/test_muse_spark.py`, 38 tests. 12 fail on main
and all pass on this branch.
- Sampling for the repo, repo:quant, cache snapshot, local .gguf and org
variants.
  - The variant menu and shard resolution for every quant.
  - The imatrix exclusion.
  - Reasoning detection.
- Every reasoning kwarg Studio can produce, rendered against the
template's effort handling.
- **Full backend suite** (`studio/backend/tests`, `-n 24`): main vs this
branch comparison of failing test IDs is in progress; I will update
here.
- **Live check:** Studio's planned argv for UD-IQ1_S (`-c 134144`, flash
attention on), run on a ggml-org/llama.cpp#30616 llama-server build on
two B200s.
- Effort high: 511 tokens, reasoning split into `reasoning_content`,
answer `17 x 23 = 391`.
- Effort low: 114 tokens, answer `391`; the system prompt renders
`Reasoning strength: 8.`
- Rendering with `reasoning_effort: "none"` fails with HTTP 500
`Unsupported reasoning_effort`. That is the failure the coercion
prevents.
              
                    CISC
    
              
              reviewed
              
                  
                    Oct 15, 2026 
                  
              
              
            
Co-authored-by: Sigbjørn Skjæret <sigbjorn.skjaeret@huggingface.co>
              
                    CISC
    
              
              approved these changes
              
                  
                    Oct 15, 2026 
                  
              
              
            
              
                    ggerganov
    
              
              approved these changes
              
                  
                    Oct 15, 2026 
                  
              
              
            
              
                    ngxson
    
              
              approved these changes
              
                  
                    Oct 15, 2026 
                  
              
              
            
        
  
    Collaborator
        
    
        
  
    Contributor
        
  Author
    
        
  
  Member
        
    
        
  
    Contributor
        
  Author
    
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
