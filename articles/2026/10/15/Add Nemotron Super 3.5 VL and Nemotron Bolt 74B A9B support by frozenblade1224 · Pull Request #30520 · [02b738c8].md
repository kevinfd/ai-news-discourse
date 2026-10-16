---
id: "02b738c859780c52"
title: "Add Nemotron Super 3.5 VL and Nemotron Bolt 74B A9B support by frozenblade1224 · Pull Request #30520 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30520"
link: "https://github.com/ggml-org/llama.cpp/pull/30520"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T14:06:37Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["jacek2023"]
language: "en"
summary: "day 0 support for two new Nemotrons minutes later new Nemotron 3.5 Super VL was released: https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 906
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6mlby/add_nemotron_super_35_vl_and_nemotron_bolt_74b/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Add Nemotron Super 3.5 VL and Nemotron Bolt 74B A9B support by frozenblade1224 · Pull Request #30520 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-10-15

Repository navigation
Add Nemotron Super 3.5 VL and Nemotron Bolt 74B A9B support - #30520
Merged
ggerganov merged 9 commits intoOct 15, 2026 
Merged
Conversation
              
                    danbev
    
              
              reviewed
              
                  
                    Oct 14, 2026 
                  
              
              
            
              
                    danbev
    
              
              reviewed
              
                  
                    Oct 14, 2026 
                  
              
              
            
              
                    ngxson
    
              
              reviewed
              
                  
                    Oct 14, 2026 
                  
              
              
            
              
                    danbev
    
              
              approved these changes
              
                  
                    Oct 14, 2026 
                  
              
              
            
      
          
github-actions
Bot
            added
      
  model
  Model specific 
      
  mtmd
  Related to multimodal functionality (video/image/audio) 
      
  conversion
  labels
      Oct 14, 2026 
    
              
                    CISC
    
              
              approved these changes
              
                  
                    Oct 14, 2026 
                  
              
              
            
              
                    ruixiang63
    
              
              reviewed
              
                  
                    Oct 15, 2026 
                  
              
              
            
              
                    danbev
    
              
              approved these changes
              
                  
                    Oct 15, 2026 
                  
              
              
            
        
  
  Member
        
    
        
  
  Member
        
    
    
  danielhanchen 
      added a commit
        to unslothai/unsloth
      that referenced
      this pull request
    
      Oct 15, 2026 
    
    
      
  
    
      Adds Studio support for the NVIDIA Nemotron 3.5 Bolt and Super GGUFs:
[unsloth/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-GGUF)
and
[unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF).
Both are `nemotron_h_moe` (hybrid Mamba2 + a few attention layers +
latent MoE), supported in llama.cpp by ggml-org/llama.cpp#30520.
## Variant picker and drafters
- **`NVFP4` is a quant token.** Only `MXFP*` was known, so Super's
`NVFP4` variant resolved to `LiLiCorr/lilicorr-...-NVFP4.gguf`, a 1.3 GB
drafter, and loaded it as the main model. The quant regex now accepts
`(?:MX|NV)FP[0-9]+` in all of its copies (backend and
`model-identity.ts`).
- **`lilicorr-*.gguf` is a drafter kind.** Super's LiLiCorr drafter was
listed as a selectable quant. Super uses its embedded MTP head, which
measured faster, so LiLiCorr is now excluded from variant menus and
quant lookups and is never launched. Added to `_DRAFTER_KINDS` in its
three mirrors.
- **NVFP4-suffixed sidecars pair with their weights on local loads.**
`dspark-<model>-NVFP4.gguf` / `dflash-<model>-NVFP4.gguf` kept `-nvfp4`
in the pairing stem, so a local folder load attached no drafter. Bolt
ships its LiLiCorr drafter as
`dflash-NVIDIA-Nemotron-3.5-Bolt-74B-A9B-NVFP4.gguf` (GGUF architecture
`dflash`).
With this, Auto mode launches:
| Model | Drafter | Flags |
|---|---|---|
| Super | embedded MTP head | `--spec-type draft-mtp`, no
`--model-draft` |
| Bolt | LiLiCorr (`dflash-...gguf`) | `--model-draft dflash-...
--spec-type draft-dflash` |
## Sampling defaults
New `nemotron-3.5` family in `inference_defaults.json`: temperature 1.0,
top_p 0.95 (NVIDIA's recommendation for both models). It matches every
id shape (repo, `repo:quant`, cache snapshot path, local `.gguf`) and
sits before `nemotron`, so older Nemotrons keep 1.0 / 1.0.
## Memory planner
Measured against llama-server allocations for Bolt IQ2_XXS and Super
UD-IQ2_XXS, the default path was safe but mis-priced the fixed costs:
- **Embedded MTP head counted when MTP is off.** The context fit charged
Super about 3 GB for the nextn block, which llama.cpp does not load
without `--spec-type draft-mtp`, so Super got a much shorter auto
context on tight cards. It is now excluded unless MTP is engaged
(`nemotron_h_moe` only, the arch measured).
- **Latent MoE width.** The routed-expert compute term now uses
`moe_latent_size` when present, and per-layer `expert_used_count` /
`expert_feed_forward_length` arrays are read as their max (Bolt stores
them per layer; they were read as missing).
- **DFlash / DSpark drafter compute floor.** The drafter context
re-reserves to a flat buffer once the dflash implementation initialises;
the reserve was up to 332 MiB short. Floored at the measured
draft-plus-verify graph minus the reserve Studio already charges beside
it, for dflash-architecture drafters only. On a 24 GB card Bolt's DFlash
drafter does not fit the fit budget at any context (measured 23.4 GB
minimum), so Auto keeps it off there; from 32 GB it keeps `draft-dflash`
at full context (measured 26.4 GiB peak, 0.917 acceptance).
- **Smart-offload layout** (`UNSLOTH_SMART_OFFLOAD=1`): per-layer
`head_count_kv` raised a `TypeError`, and would otherwise have counted
every layer as attention with no recurrent state. KV is now charged to
the attention layers only and Mamba state to the recurrent ones, for
`nemotron_h` / `nemotron_h_moe` only. Bolt's layout now matches the
measured resident size exactly.
| MiB | Measured | Before | After |
|---|---|---|---|
| Super weights, MTP off | 45757 | 48752 | 45765 |
| Super compute 32k / 262k | 224 / 448 | 840 / 1064 | 550 / 774 |
| Bolt compute 32k / 262k | 148 / 372 | 143 / 367 | 260 / 484 |
| Bolt DSpark drafter reserve 32k / 262k | 2540 / 3884 | 2208 / 3707 |
2548 / 3892 |
| Bolt DFlash (LiLiCorr) drafter, any context | 1750 | 2085 | 1862 |
| Super MTP reserve 32k / 262k | 590 / 1038 | 1366 / 1814 | 1075 / 1523
|
Every component now estimates at or above the measured allocation. Other
architectures are unchanged; the new tests pin that for a hybrid with
`full_attention_interval` and for a dense model.
## Tests
- `tests/test_nemotron35_bolt_super.py` and
`tests/test_nemotron35_planner.py`: 39 tests, all pass. On `main` 13 of
the picker/sampling tests fail, as expected.
- The related existing suites (GGUF, variants, drafters, MTP, DSpark,
DFlash, sampling, offload, fit, context, memory, layout): identical
failing test ids on `main` and on this branch, all pre-existing
(diffusion offload, training offload layers, one TTS test).
- Live llama-server runs of the published files on llama.cpp with
#30520: Super UD-Q4_K_XL with the Auto-mode MTP flags, draft acceptance
0.897; Bolt IQ2_XXS with the LiLiCorr drafter, acceptance 0.836 and
128.7 to 224.2 tok/s versus no drafter.
## Not covered
- Studio's pinned `gguf==0.19.0` cannot read the `Q2_0` type that Super
UD-IQ1_M through UD-Q3_K_XL use. Only the opt-in smart-offload layout
reads tensor types this way; the default path sizes from offsets and is
unaffected.
- The 24 / 48 / 80 GB fit decisions were checked by calling the planner
with simulated card sizes, not on those cards.
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
