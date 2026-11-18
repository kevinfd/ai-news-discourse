---
id: "6658057fd23d3b59"
title: "Latent Lattice Language Models"
url: "https://shivamduggal4.github.io/latent-lattice-language-models"
link: "https://shivamduggal4.github.io/latent-lattice-language-models"
source: "shivamduggal4.github.io"
domain: "shivamduggal4.github.io"
source_type: "community"
collector: "hackernews"
date: "2026-11-17T22:17:18Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["E-Reverance"]
language: "en"
summary: "1MIT2Adobe\n    Paper\n    Code (coming soon)\n  \nAbstract\nLanguage models typically increase per-token computation through deeper or looped layers and latent reasoning steps, while richer residual connections improve information flow across layers. We instead increase computational capacity: the number of active computational states a model maintains. We introduce the Lattice of Latents, a set of…"
tags: []
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 582
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50539039"
score: 53
comments: 5
community: "Hacker News"
---

# Latent Lattice Language Models

shivamduggal4.github.io · E-Reverance · 2026-11-17

1MIT2Adobe
    Paper
    Code (coming soon)
  
Abstract
Language models typically increase per-token computation through deeper or looped layers and latent reasoning steps, while richer residual connections improve information flow across layers. We instead increase computational capacity: the number of active computational states a model maintains. We introduce the Lattice of Latents, a set of per-layer horizontal latent streams that run recurrently along time, alongside the vertical residual stream that flows through depth. Like hyper-connections, mHC, and attention or value residuals, the Lattice enhances the residual stream, but rather than adding or rerouting residual pathways through depth, it provides companion computational states that persist across tokens. Unlike hybrid Transformer–SSM architectures, whose recurrent states primarily serve as internal memory for sequence mixing, these latents directly condition the vertical stream’s attention, KV-cache writes, MLP computation, and decoding. On Transformers trained on 20B FineWeb-Edu tokens, a 406M-parameter Lattice model lowers validation perplexity from 15.41 to 14.40 over a parameter-matched Transformer. These gains extend across architectural variants. The Lattice composes with prior residual-stream enhancements: with hyper-connections and input residuals, it lowers validation perplexity from 15.41 (base Transformer) and 14.22 (Transformer with same enhancements) to 13.61. On Gated DeltaNet, Mamba-2, Triadic GDN, and GDN–Mamba-2 hybrids, it improves perplexity at every tested native state size, with Lattice-GDN & Lattice-Triadic-GDN variants outperforming pure baselines with 4× larger native states. These results identify persistent per-layer state as a complementary axis for scaling language-model computation.
Vertical residual streams flow through depth; horizontal latents persist across tokens. Switch between training and inference, and compare models.
      Input injectionablation
    
    Paused · click to play
Click the figure to pause. Input injection can be switched on or off at any moment; the animation continues from the same point.
Interactive versions of the main results. Hover over any bar or point for details.
LLLM (dmodel, dr) has a vertical residual-stream width dmodel and horizontal-latent width dr.
      Eval set
      
    
      View
      
        
        
        
      
    
      Transformer
      LLLM (single pass)
      LLLM + Jacobi refiner (J3)
    
GFLOP/token: floating-point operations per token, excluding attention scores (which add only ≈ 0.1 GFLOP/token) and the embedding lookup.
J3 runs three sweeps; its sequential rollout uses a single pass at inference (click Show full table for results).
FineWeb-Edu validation perplexity as training continues. Circle area is proportional to parameter count.
Both LLLMs use only 22 layers vs. 40 for the Transformer 40L, so with the same attention width (1024) they keep a 45% smaller KV cache.
400M models, 20B FineWeb-Edu tokens. Lattice models narrow the vertical width from 1024 to 932 to stay iso-parameter. The Transformer and its single enhancements appear first, then the Lattice and its single enhancements, then two-enhancement combinations.
      Transformer variants
      Lattice variants (ours)
    
HC: hyper-connections; mHC: manifold-constrained HC; value: value residual (ResFormer; learned weights for the single +value runs, fixed 0.5 in x0 + value); x0: nanochat-style input residual.
A hard regime: the vertical residual stream is squeezed to 256 dimensions. Press play to add the horizontal-update enhancements one at a time and watch them recover most of the gap to a full-width Transformer. 10B-token pretraining.
+ adds a component; ↻ replaces one. Parameter counts are shown under each bar.
Pure vs. Lattice recurrent models (∼405M parameters, 10B FineWeb-Edu tokens) across native-state sizes per mixer. Each Lattice model is iso-parameter with its pure counterpart. Bars appear from highest to lowest perplexity, each at its state-size position.
      Pure backbone
      + Lattice (ours)
    
Native-state size counts recurrent-memory entries per mixer (1K = 1024 scalars), excluding the horizontal latents and convolution states. Lattice models use input injection + vstream.
