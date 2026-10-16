---
id: "3143ad62f5048895"
title: "The space is moving quick. 2x 4060 Tensor Parallel main weights. RPC offload the drafters to amd strix. Got +2-3GB Vram for context at no perf cost."
url: "https://reddit.com/r/LocalLLaMA/comments/1x6qq0j/the_space_is_moving_quick_2x_4060_tensor_parallel"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6qq0j/the_space_is_moving_quick_2x_4060_tensor_parallel"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T16:43:07Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Chuyito"]
language: "en"
summary: "Mixing Nvidia+AMD hardware via RPC usually meant split-mode layer only. I managed to keep split-mode tensor working, and patch my llama-rpc to send the drafters over to my strix. That let me go from 150k -> 195k context, at the same tensor parallel speed.. nice. My agents helped with a TON of this setup: - The 10Gbps usb NIC just came out in sept. The drivers are non existent, but a gpt session…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "AMD"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "post"
word_count: 600
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6qq0j/the_space_is_moving_quick_2x_4060_tensor_parallel/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# The space is moving quick. 2x 4060 Tensor Parallel main weights. RPC offload the drafters to amd strix. Got +2-3GB Vram for context at no perf cost.

Reddit · Chuyito · 2026-10-15

Mixing Nvidia+AMD hardware via RPC usually meant split-mode layer only. I managed to keep split-mode tensor working, and patch my llama-rpc to send the drafters over to my strix. That let me go from 150k -> 195k context, at the same tensor parallel speed.. nice. My agents helped with a TON of this setup: - The 10Gbps usb NIC just came out in sept. The drivers are non existent, but a gpt session later we were git pulling and modifying 2 files to build it for my correct OS version. - The llamacpp side took merging 2 PRs + 1 local patch. Its not even worth submitting a PR for the 3rd patch since PRs go dormant now, so Ill leave it here so your agent can build you a patch at whatever state the main branch is in. In theory this could be offloaded to anything with 2-3gb [35051] 0.06.133.020 I load_tensors: offloading 4 repeating layers to GPU [35051] 0.06.133.020 I load_tensors: offloaded 6/6 layers to GPU [35051] 0.06.133.024 I load_tensors: RPC0[10.44.0.6:13315] model buffer size = 1821.88 MiB [35051] 0.10.019.793 I llama_context: constructing llama_context [35051] 0.10.019.798 I llama_context: n_seq_max = 1 [35051] 0.10.019.799 I llama_context: n_ctx = 190208 # ============================================================================ # Qwen3.8 DFlash2 tensor target + remote RPC drafter # # Known-good llama.cpp base: # 77c4540ce4667f4577753fe034a3a8042f510b8f # # Changes: # 1. PR #26636 commit 1a6fee5 # Allows draft context to use backends required by shared target tensors. # # 2. PR #27858 port commit 1784fc3 # DFlash2 tensor-parallel CPU selector support. # # 3. Local patch # Always use DFlash2 CPU selector, allowing target=CUDA0,CUDA1 tensor # while draft is pinned separately to RPC0/coal. # ============================================================================ BASE=77c4540ce4667f4577753fe034a3a8042f510b8f git switch -C exp-dflash-tensor-rpc "$BASE" # PR #26636 git fetch origin refs/pull/26636/head:pr-26636 git cherry-pick 1a6fee5 # PR #27858 newer port git fetch https://github.com/henrique-simoes/llama.cpp.git \ mv/dflash-tp:henrique-dflash-tp git cherry-pick 1784fc3 # Local RPC DFlash selector patch cat > /tmp/dflash-coal-rpc.patch <<'PATCH' diff --git a/common/speculative.cpp b/common/speculative.cpp index 775df85c7..e76caef0b 100644 --- a/common/speculative.cpp +++ b/common/speculative.cpp @@ -1062,7 +1062,7 @@ struct common_speculative_impl_draft_dflash : public common_speculative_impl { selector_top_k = llama_model_dflash_selector_top_k(model_dft); is_dflash2 = selector_top_k > 0; // under tensor parallelism the lm_head is split and the in-graph selector cannot run - is_dflash2_cpu = is_dflash2 && llama_model_get_split_mode(model_dft) == LLAMA_SPLIT_MODE_TENSOR; + is_dflash2_cpu = is_dflash2; mask_token_id = llama_vocab_mask(llama_model_get_vocab(model_dft)); if (is_dflash2_cpu) { diff --git a/src/models/dflash.cpp b/src/models/dflash.cpp index e707c6b03..7942058fe 100644 --- a/src/models/dflash.cpp +++ b/src/models/dflash.cpp @@ -153,7 +153,7 @@ void llama_model_dflash::load_arch_tensors(llama_model_loader &) { // Under tensor parallelism the lm_head is split along the vocabulary, which the // in-graph selector cannot consume, so DFlash2 ranks on the CPU and reads these tables // straight from the GGUF file; otherwise the in-graph selector uses them in the model - const bool use_cpu_selector = params.split_mode == LLAMA_SPLIT_MODE_TENSOR; + const bool use_cpu_selector = true; dflash_selector_prev = create_tensor(tn(LLM_TENSOR_DFLASH_SELECTOR_PREV, "weight"), { rank, n_vocab }, use_cpu_selector ? TENSOR_SKIP : 0); dflash_selector_next = create_tensor(tn(LLM_TENSOR_DFLASH_SELECTOR_NEXT, "weight"), { rank, n_vocab }, use_cpu_selector ? TENSOR_SKIP : 0); dflash_selector_hidden = create_tensor(tn(LLM_TENSOR_DFLASH_SELECTOR_HIDDEN, "weight"), { n_embd, rank }, 0); @@ -807,7 +807,7 @@ llama_model_dflash::graph<false>::graph(const llama_model & model, const llm_gra // DFlash2 under tensor parallelism ranks on the CPU from the gathered lm_head output, so // the decoder hidden states ride the nextn slot; without tensor parallelism the in-graph // selector packs its lattice there instead (see below) - if (model.dflash_selector_hidden && model.split_mode() == LLAMA_SPLIT_MODE_TENSOR) { + if (model.dflash_selector_hidden) { res->t_h_nextn = cur; } @@ -862,7 +862,7 @@ llama_model_dflash::graph<false>::graph(const llama_model & model, const llm_gra } // DFlash2 ranks its candidates in-graph when the lm_head is not split along the vocabulary - if (model.dflash_selector_hidden && model.split_mode() != LLAMA_SPLIT_MODE_TENSOR) { + if (false && model.dflash_selector_hidden) { build_dflash2_selector(*this, model, inp_tokens); } } PATCH git apply /tmp/dflash-coal-rpc.patch
