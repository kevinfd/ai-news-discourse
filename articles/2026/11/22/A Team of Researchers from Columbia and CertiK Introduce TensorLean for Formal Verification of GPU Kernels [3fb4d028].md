---
id: "3fb4d028a772c544"
title: "A Team of Researchers from Columbia and CertiK Introduce TensorLean for Formal Verification of GPU Kernels"
url: "https://marktechpost.com/2026/11/21/columbia-certik-tensorlean-formal-verification-gpu-kernels"
link: "https://marktechpost.com/2026/11/21/columbia-certik-tensorlean-formal-verification-gpu-kernels"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-22T01:51:43Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Researchers from Columbia University and CertiK have introduced TensorLean , a framework for formal verification of GPU kernels at the PTX level. TensorLean is a Lean-based verifier that proves compiled kernels match a tensor-level math spec. The research team checked 149 kernel instances , including every kernel of FlashAttention-2, -3 and -4 plus DeepGEMM. It proved 83 correct. The remaining…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Language Model", "Machine Learning", "New Releases", "Software Engineering", "Staff", "Tech News"]
orgs: ["Hugging Face"]
topics: ["chips & infrastructure", "models & research", "safety & ethics", "agents & coding"]
content_source: "summary"
word_count: 745
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# A Team of Researchers from Columbia and CertiK Introduce TensorLean for Formal Verification of GPU Kernels

MarkTechPost · Michal Sutter · 2026-11-22

Researchers from Columbia University and CertiK have introduced TensorLean , a framework for formal verification of GPU kernels at the PTX level. TensorLean is a Lean-based verifier that proves compiled kernels match a tensor-level math spec. The research team checked 149 kernel instances , including every kernel of FlashAttention-2, -3 and -4 plus DeepGEMM. It proved 83 correct. The remaining 66 led to 38 correctness bugs. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 TL;DR 

 Size: 1.8K-line PTX parser. Specs total 10,278 lines against 151,285 lines of kernel source, a ratio near 15:1. 

 Runs on: A 16-core workstation. It checks PTX compiled for A100, H100 and B200 kernels. 

 Performance: 83 of 149 kernel instances proved correct, 38 bugs found across 6 projects. 

 Best: Caught a FlashAttention-4 data race that never appeared in 17,760 test runs. 

 What is TensorLean? 

 TensorLean is a formal verification framework for GPU kernels at the PTX level. 

 It starts from unmodified source code. A developer writes a tensor-level spec in Lean. TensorLean then proves 4 properties: no data races, termination, correct output within tolerance, and untouched memory elsewhere. 

 How does TensorLean verify a GPU kernel? 

 Specs build on Lean’s Mathlib. Tensor operators follow PyTorch names, so @ means torch.matmul . Each spec has 5 parts: spec_math , spec_mut , spec_layout , spec_tol and requires . The math stays separate from the memory layout. 

 The pipeline runs in 7 steps: 

 Start from unmodified source. 

 Write the tensor-level spec. 

 Compile to PTX and load a PTX semantics. 

 Build a happens-before graph to check races and termination. 

 Symbolically execute to get final memory, identical across schedules. 

 Lower the spec to PTX-memory level. 

 Discharge proofs with Lean’s kernel, Z3 and cvc5. 

 Which techniques make it scale? 

 Concurrency to sequential: Race-freedom proofs on the happens-before graph cover all CTAs, threads and loop iterations symbolically. 

 Loop invariants over semirings: Closed forms for tiled, accumulating loops, such as online softmax, need 1 SMT query per loop. 

 Tolerance proofs: Algebraic error is proved zero. Round-off error is bounded separately, then combined. 

 Assertions as hints: Developers add tensorlean_assert in source. Each is proved once, then reused. 

 What bugs did TensorLean find? 

 The GitHub README lists 38 bugs, all reported upstream. FlashAttention accounts for 23. Liger Kernel has 7, TileOPs 3, TileLang 2, DeepGEMM 2 and Triton 1. 

 By category, the site reports 19 memory access errors and 13 numerical bugs. It also counts 7 data races, 5 uninitialized memory reads and 5 undefined behaviors. There are 3 algorithm errors, 2 miscompilations and 1 deadlock. One bug can sit in several categories. 

 Of 102 FlashAttention instances, 56 passed all 4 properties. The other 46 each failed a proof goal on a source bug. 

&

 How does it compare with other GPU kernel verifiers? 

 Feature TensorLean Volta ProofWright PTX in Lean (Koska et al.) Builders Columbia, CertiK MSR India, Stanford Not disclosed SF Tensor Code level PTX PTX CUDA PTX Checks against Lean tensor spec Reference kernel Safety + equivalence Lean proofs Kernels verified 149 instances, FA-2/3/4, DeepGEMM, Liger Tutorial reductions, SGEMM, FA-style, TileLang KernelBench L1, safety for 74% 3 simple kernels Async ops (wgmma, TMA) Yes, FA-3 and FA-4 Out of scope Not disclosed Yes New bugs reported 38 Races, OOB reads Not disclosed Not disclosed Check time ~10 min median, 50 min max 0.007 s to ~570 s ~3 min per kernel Not disclosed 

 The key gap versus Volta is configuration coverage. TensorLean says equivalence checkers unroll loops for one concrete setup at a time. It uses symbolic parameters instead. 

 Key Takeaways 

 TensorLean proves GPU kernels correct at the PTX level using Lean, Z3 and cvc5. 

 83 of 149 kernel instances proved correct; 38 bugs found. 

 23 bugs sit in FlashAttention-2, -3 and -4. 

 Specs run about 15x smaller than the kernel source. 

 Check out the project page , GitHub repo and announcement on X . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post A Team of Researchers from Columbia and CertiK Introduce TensorLean for Formal Verification of GPU Kernels appeared first on MarkTechPost .
