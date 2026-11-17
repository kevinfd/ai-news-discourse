---
id: "b863616c7a22b79d"
title: "nvidia/Qwen3.8-Flash-Next-NVFP4-QAD"
url: "https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4-QAD"
link: "https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4-QAD"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-17T11:29:34Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Kahvana"]
language: "en"
summary: "Looks pretty interesting! Also sorry if the \"new model\" flair is inappropiate here, wasn't sure if I should pick that or \"discussion\"."
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "Alibaba"]
topics: ["models & research", "chips & infrastructure", "products & launches", "jobs & society"]
content_source: "fulltext"
word_count: 849
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xyi3aa/nvidiaqwen38flashnextnvfp4qad/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# nvidia/Qwen3.8-Flash-Next-NVFP4-QAD

Hugging Face · Kahvana · 2026-11-17

Qwen3.8-Flash-Next-NVFP4-QAD
This is an experimental mixed-precision QAD checkpoint of Qwen3.8-Flash-Next, exported after 100 optimizer updates using NVIDIA Model Optimizer and NeMo AutoModel with FSDP2. It contains the full multimodal model, including the frozen vision encoder, PLE n-gram embedding, and MTP module. Weight files occupy approximately 129.7 GB (120.8 GiB).
This checkpoint uses a more aggressive quantization recipe than
Qwen3.8-Flash-Next-NVFP4.
In addition to routed experts, it quantizes shared experts to NVFP4 and selected
GDN, QSA, and indexer projections to MXFP8. The repository name's -QAD suffix
identifies the training method; it does not mean the original NVFP4 recipe was
kept unchanged. Task accuracy gains from QAD are not statistically established.
Weight shards were consolidated for distribution. Every source file was verified against its export SHA256, and consolidated files passed a complete readback. Tensor names, shapes, dtypes, and stored values are unchanged.
Quantization recipe
The main model uses native NVFP4 and MXFP8 computation in the validated serving
configuration. Selected excluded operations retain their original FP32 contracts.
The KV cache was BF16 during evaluation; KV-cache quantization is not part of
this recipe. See hf_quant_config.json, config.json, and
quantization_recipe.json for machine-readable metadata.
The main LM was quantized from the original BF16 model. The preserved MTP and PLE state derives from the released NVIDIA mixed-precision checkpoint. QAD did not further quantize or train MTP. All benchmark measurements below disabled MTP.
QAD training
The student used fake-quantized computation with floating master weights and a frozen BF16 teacher. Training used text inputs; the vision encoder stayed frozen.
16,384 is a sequence-length ceiling. It does not mean every example contained 16,384 non-padding tokens. The exact training data files are not distributed in this repository. This is an inference checkpoint; optimizer state is not included.
Export validation compared native training-reference and exported-model log probabilities at input lengths 256, 4,096, 8,192, and 16,384. Across 28,924 scored positions, mean absolute log-probability error was 1.21e-6, maximum error was 1.00e-5, and top-1 agreement was 99.25%. This establishes export parity within the tested limits, not parity with BF16 model accuracy.
Experimental evaluation
The baseline is the original Qwen3.8-Flash-Next model in BF16. All entries are our measurements on a 0–100 scale. Benchmark metrics and evaluation protocols can differ from published model-card results.
Validation scope: checkpoint identity, native quantization kernels, score coverage, and task-specific grading were checked. Historical full-run request retry, timeout, and output-termination accounting is incomplete, particularly for Terminal-Bench. The numbers are descriptive; unresolved limit effects prevent a clean attribution of differences to quantization or training.
SciCode reports mean subtask success over eight operational runs per model, with 338 scored subtasks per run (2,704 per model). Repeats used the same configured request seed and are not independently reseeded trials. A confidence interval against BF16 is not reported here. SciCode subtask success must not be compared with published main-problem scores.
Terminal-Bench retains all 712 outcomes per model, including protocol-defined runtime failures scored as zero: 6/712 for BF16 and 4/712 for QAD. Both models scored 612/712. The exploratory task-cluster bootstrap 95% interval for QAD minus BF16 is [-2.95, +3.23] percentage points. Historical allocation-wide timeout/retry and output-cap rates remain unknown; later two-task logging diagnostics do not retroactively fill those gaps.
These measurements do not establish an overall task-accuracy improvement over the BF16 baseline.
Serving
Validated hardware was NVIDIA GB300, using native Blackwell kernels, vLLM 0.30.0,
four-way tensor parallelism, and expert parallelism. This recipe additionally
needs the compatibility helpers in serving/: narrow
MXFP8 output padding/cropping and the canonical sparse-indexer policy used for
training/export validation. The helpers check the ModelOpt runtime source hash
and refuse an unvalidated build.
Follow serving/README.md for the tested settings and
compatibility requirements. Generic transformers.from_pretrained() loading
and arbitrary vLLM versions have not been validated for this mixed format.
The model configuration preserves the base model's context settings; QAD export
parity was checked through 16K, and task-serving configurations used up to 262,144.
This release does not establish accuracy at the base model's maximum context.
MTP is preserved for completeness. MTP-enabled accuracy, acceptance rates, and performance were not validated for this QAD checkpoint. With standard exact speculative rejection sampling, draft quantization primarily changes acceptance and speed; approximate verification can change the output distribution.
Architecture and intended use
The upstream model combines a vision encoder, Gated DeltaNet, Qwen Sparse Attention, MoE layers, gated residual streams, and n-gram embeddings. Inputs may contain text, images, or video, and outputs are text. Refer to the base model card for its architecture, training information, intended uses, and limitations. This release is intended for quantization and QAD research and deployment validation.
License, attribution, and limitations
Use is governed by the
NVIDIA Open Model License
and the upstream Qwen Community License 1.0. Qwen is the upstream
model developer. This checkpoint does not replace or waive upstream terms.
The serving helper code carries the separate license in serving/LICENSE.
The model can generate incorrect, biased, toxic, or otherwise unsuitable content. Evaluate it on the intended application, including multimodal inputs and long contexts, before deployment. Quantization and short QAD training do not remove the base model's limitations.
References: NVIDIA Model Optimizer, NeMo AutoModel, released NVFP4 model.
- Downloads last month
- -
Model tree for nvidia/Qwen3.8-Flash-Next-NVFP4-QAD
Base model
Qwen/Qwen3.8-Flash-Next
