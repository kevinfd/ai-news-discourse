---
id: "7df12f50b67e3bc4"
title: "Zyphra ZYFA: FP8 FlashAttention for AMD MI355X, Up to 1.76x Faster"
url: "https://marktechpost.com/2026/11/06/zyphra-zyfa-fp8-flashattention-amd-mi355x"
link: "https://marktechpost.com/2026/11/06/zyphra-zyfa-fp8-flashattention-amd-mi355x"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-06T17:28:04Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Zyphra has released ZYFA (Zyphra FlashAttention on AMD) , a set of FP8 and BF16 prefill attention kernels for AMD Instinct MI355X GPUs. ZYFA is Zyphra’s FP8 attention engine for long-context prefill, and the code is open source under Apache 2.0 . On real model activations, its FP8 kernels run 1.16-1.76x faster than AITER , AMD’s default kernel library. At head dimension 128, ZYFA’s FP8 error is…"
tags: ["AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Staff", "Tech News"]
orgs: ["AMD", "Mistral", "Nvidia", "DeepSeek", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "products & launches"]
content_source: "summary"
word_count: 957
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Zyphra ZYFA: FP8 FlashAttention for AMD MI355X, Up to 1.76x Faster

MarkTechPost · Michal Sutter · 2026-11-06

Zyphra has released ZYFA (Zyphra FlashAttention on AMD) , a set of FP8 and BF16 prefill attention kernels for AMD Instinct MI355X GPUs. ZYFA is Zyphra’s FP8 attention engine for long-context prefill, and the code is open source under Apache 2.0 . On real model activations, its FP8 kernels run 1.16-1.76x faster than AITER , AMD’s default kernel library. At head dimension 128, ZYFA’s FP8 error is 62-78% lower than AITER’s. 

 TL;DR 

 Framework: It is a kernel library. Causal forward (prefill) attention in FP8 e4m3 and BF16, head dim 128 and MLA shape (192/128). 

 Runs on: AMD Instinct MI355X only (CDNA4, gfx950), ROCm 7.2.3, PyTorch 2.12. Drop-in flash_attn_func interface. 

 Performance: 1.16-1.76x AITER’s FP8 throughput on real activations; BF16 roughly ties (1.01-1.02x). 

 Best: 2,672 TFLOP/s FP8 at 32K tokens, 53% of the FP8 datasheet peak (AITER: 39%). 

 Worst: Only 1.16x on Mistral-7B activations; FP8 clock drops to 1,628 MHz vs AITER’s 2,108 MHz. 

 What is ZYFA? 

 ZYFA is shipped in the form of a technical paper along with code from Zyphra. It powers the attention engine of the Zyphra Optimization Engine (ZOE) , which runs Zyphra Cloud. The BF16 kernels are written in HIP. The FP8 kernels are hand-scheduled assembly emitted by a Python generator. 

 Why does FP8 attention underperform on MI355X? 

 FP8 matrix instructions run at 2x the BF16 peak. But FP8 only speeds up the 2 matrix products, QKᵀ and PV. The softmax between them runs on the vector unit at the same speed in both precisions. 

 For 32 queries against 128 keys, FP8 matrix work takes 1,024 cycles. The exact FP8 softmax takes 896 vector cycles. So the kernel needs near-perfect overlap to keep matrix units busy. Zyphra’s thread traces show AITER’s matrix pipe idle for 31.7% of cycles. 

 The MI355X does not track matrix instruction completion in hardware, so instruction order must create that overlap. 

 How does ZYFA work? 

 ZYFA uses 3 techniques : 

 Lean P: one multiply-add instead of an exponential 

 An e4m3 bit pattern, read as an integer, grows by 8 each time the value doubles. So the code of 2^x is roughly 8x plus a constant. Lean P writes each FP8 probability with 1 multiply-add and 1 integer conversion. This cuts softmax vector cycles per block from 896 to 384. 

 Two-wave ping-pong schedule 

 2 waves share each SIMD. One issues matrix instructions while the other computes probabilities, then they swap. With lean P, the matrix pipe is busy 86% of steady-state cycles, up from 60% with exact P. 

 Per-block scaling and a rounded row sum 

 Each 64-key block of probabilities is scaled by a power of 2 before rounding. CDNA4’s scaled matrix instruction removes the factor at no cost. ZYFA also divides by the sum of the rounded probabilities, computed with 1 extra matrix instruction per block. 

&&

 How fast is ZYFA? 

 Real-activation FP8 speedups at 16K and sustained clocks are 1.16x (Mistral-7B), 1.17x (Qwen3-8B) and 1.76x (DeepSeek-V2-Lite) . On Gaussian benchmarks at 32K, the head-dim-128 FP8 kernel reaches 2,672 TFLOP/s against AITER’s 1,944. At the MLA shape it reaches 2,464 against 1,237, a 1.99x ratio. 

 On captured Mistral-7B and Qwen3-8B layers, ZYFA delivers 1.94 and 1.91 TFLOP/J. AITER delivers 1.60 and 1.56. 

 Why are real-model gains smaller than benchmark gains? 

 The MI355X clock depends on how many operand bits flip. AITER lets more small probabilities become zeros or subnormals. Those switch fewer bits, so its clock runs higher. On the Mistral-7B layer, ZYFA runs at 1,628 MHz while AITER runs at 2,108 MHz. ZYFA still needs fewer cycles overall. Zyphra team recommends benchmarking on real activations at sustained clocks. 

 How accurate is ZYFA’s FP8 attention? 

 Against fp64 attention, ZYFA’s FP8 error is 0.22x AITER’s on Mistral-7B and 0.38x on Qwen3-8B. It sits within a few percent of Composable Kernel and Triton. In full Mistral-7B, KL divergence from fp64 is 3.4×10⁻³ with ZYFA and 5.9×10⁻³ with AITER. ZYFA’s outputs were also bitwise identical across 7,200 launches. 

 Most full-model FP8 error comes from quantizing Q, K and V. A Hadamard rotation of Q and K roughly halves that input error. On Mistral-7B it adds about 0.1% to attention time. 

 How does ZYFA compare with other attention kernels? 

 Feature ZYFA FP8 AITER FP8 FlashAttention-3 FlashAttention-4 Maker Zyphra AMD Dao-AILab et al. Dao-AILab et al. Target GPU AMD MI355X AMD MI300X to MI355X NVIDIA H100/H800 NVIDIA B200 (plus Hopper) Headline throughput 2,672 TFLOP/s FP8 1,944 TFLOP/s FP8 (Zyphra-measured) Close to 1.2 PFLOP/s FP8 1,613 TFLOP/s BF16 Share of peak 53% FP8 39% FP8 (Zyphra-measured) Not disclosed (FP8) 71% BF16 Softmax approach Lean P, no exponential Hardware exponential Overlap via async Tensor Cores Software-emulated exponential FP8 accuracy claim 62-78% lower error than AITER Baseline 2.6x lower error than baseline FP8 Not disclosed Scope Causal prefill forward only Prefill, decode, MLA, paged Forward and backward, FP8 forward Forward and backward License Apache 2.0 MIT BSD-3-Clause BSD-3-Clause 

 Cross-vendor numbers come from different inputs and clocks. Zyphra did not measure NVIDIA GPUs. 

 Key Takeaways 

 FP8 attention on MI355X is softmax-bound, not matrix-bound. 

 Lean P swaps the exponential for 1 multiply-add. 

 Real-model gains are 1.16-1.76x, smaller than benchmarks show. 

 FP8 error drops 62-78% vs AITER at head dim 128. 

 Prefill only: no decode, no paged KV, MI355X only. 

 Check out the paper , the Zyphra blog post and the GitHub repo . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Zyphra ZYFA: FP8 FlashAttention for AMD MI355X, Up to 1.76x Faster appeared first on MarkTechPost .
