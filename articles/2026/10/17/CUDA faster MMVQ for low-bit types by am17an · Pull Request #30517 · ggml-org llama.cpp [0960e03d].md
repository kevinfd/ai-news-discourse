---
id: "0960e03d3afc9219"
title: "CUDA: faster MMVQ for low-bit types by am17an · Pull Request #30517 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30517"
link: "https://github.com/ggml-org/llama.cpp/pull/30517"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T14:33:53Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["jacek2023"]
language: "en"
summary: "big speedup, but only for specific quantizations like Q2_K and Q3_K"
tags: ["r/LocalLLaMA"]
orgs: ["AMD"]
topics: []
content_source: "fulltext"
word_count: 289
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8bqqs/cuda_faster_mmvq_for_lowbit_types_by_am17an_pull/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# CUDA: faster MMVQ for low-bit types by am17an · Pull Request #30517 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-10-17

Repository navigation
CUDA: faster MMVQ for low-bit types - #30517
Conversation
@am17an
This small (ugly) patch fix the regression on GCN.
@@ -465,7 +471,12 @@ static constexpr __host__ __device__ int calc_nwarps(ggml_type type, int ncols_d
             default:
                 return 1;
         }
    } else if (table_id == MMVQ_PARAMETERS_GCN) {
+        if (((type == GGML_TYPE_Q3_K && (ncols_dst == 2 || ncols_dst == 3)) ||
+             (type == GGML_TYPE_Q6_K && ncols_dst == 4))) {
+            return 1;
+        }
@thelittlefireman feel free to push this change to this branch (you should have access)
Done more test on others AMD arch CDNA and RDNA2
| AMD Instinct MI100
AMD Radeon RX 6800
I will try to suggest a fix for regressions tomorrow.
Any slowdown less than 5% seems like noise to me. At this point it is bike-shedding.
@am17an I agree.
For RX 6800 the main issue is that there is no specific config for RDNA2 on ggml_cuda_should_use_mmvq and it's fallback to de default return ne11 <= MMVQ_MAX_BATCH_SIZE;
We could add this fix (Specially for Q2_K with n ==8) for the PR
 427     if (GGML_CUDA_CC_IS_RDNA2(cc)) {
 428         switch (type) { // tuned for RDNA2
 429             // TODO Add and bench other types of quants
 430             case GGML_TYPE_Q2_K:
 431                 return ne11 == 8;
 432             default:
 433                 return ne11 <= MMVQ_MAX_BATCH_SIZE;
 434         }
 435     }
But it like put a band-aid on a bullet wound and will need futher bench/fix/PR for other quants.
Also Mi100/CDNA use the same tableid => MMVQ_PARAMETERS_GCN and then have the same specialization on calc_nwarps and calc_rows_per_block
we should split and make specific tables for each arch. Another PR to do 😿
@IMbackK we could merge the PR as if and then make others PR for thoses specific issues, what do you think ?
