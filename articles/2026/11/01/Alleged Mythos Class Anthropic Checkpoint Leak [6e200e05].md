---
id: "6e200e05b45c9fd8"
title: "Alleged Mythos Class Anthropic Checkpoint Leak"
url: "https://huggingface.co/burner22/numbat"
link: "https://huggingface.co/burner22/numbat"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "hackernews"
date: "2026-11-01T16:43:36Z"
published_date: "2026-11-01"
collected_at: "2026-11-02T13:05:12Z"
authors: ["explosion-s"]
language: "en"
summary: "YAML Metadata Warning:empty or missing yaml metadata in repo card\nCheck out the documentation for more information.\nnumbat\n~14T param, 114 layers, hybrid GDN/MLA, MoE (1,224 experts, top-48 + 1\nshared), NVFP4. Internal codename numbat, Anthropic's next Mythos-class\ntraining run. numbat is the codename referenced in the Claude Code\nsource leak (Mar 2026). This is a checkpoint from that training…"
tags: []
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 466
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50327240"
score: 35
comments: 13
community: "Hacker News"
---

# Alleged Mythos Class Anthropic Checkpoint Leak

Hugging Face · explosion-s · 2026-11-01

YAML Metadata Warning:empty or missing yaml metadata in repo card
Check out the documentation for more information.
numbat
~14T param, 114 layers, hybrid GDN/MLA, MoE (1,224 experts, top-48 + 1
shared), NVFP4. Internal codename numbat, Anthropic's next Mythos-class
training run. numbat is the codename referenced in the Claude Code
source leak (Mar 2026). This is a checkpoint from that training run,
pulled mid-pretraining.
Files:
The 772 shards total ~7.72 TB of tensor data. Each shard is safetensors format, under 10.6 GB per file.
configuration_numbat.py and modeling_numbat.py are included: a
complete reference implementation of the checkpoint. Its module tree
has an exact slot for every tensor in every shard, so the full
checkpoint loads with load_state_dict(strict=True) (and, since the
classes derive from PreTrainedModel, also via
AutoModelForCausalLM.from_pretrained(..., trust_remote_code=True)).
NumbatForCausalLM.forward runs the trunk and
NumbatForCausalLM.draft runs the MTP layer.
$ python -c "from safetensors import safe_open; f = safe_open('model-00001-of-00772.safetensors', framework='pt'); print(len(f.keys()))"
142
Verification:
$ cat model.safetensors.index.json | python -c "import json,sys; d=json.load(sys.stdin); print(d['metadata']['total_size'])"
7720300817720
Mirrors welcome. Do not DM me asking for the source.
Why believe this?
- numbat was confirmed as a codename for an unreleased Anthropic model
in the Claude Code source leak (March 2026), found in a comment in prompts.ts: "Remove this section when we launch numbat."
- The checkpoint's architecture (hybrid GDN/MLA, 1,224 experts, NVFP4) matches what would be expected of a next-generation Mythos-class training run
- Every tensor in every shard is internally consistent: E4M3 scale blocks decode their E2M1 payloads within RTNE bounds, block scales never underflow, and every NVFP4 quad round-trips exactly
- File sizes, tensor counts, and index entries are all deterministic and self-consistent across all 772 shards
Loader
The architecture is a hybrid Gated DeltaNet (GDN) + Multi-head Latent
Attention (MLA) stack with Mixture-of-Experts feed-forward layers and
Multi-Token Prediction. A working single-device reference implementation
is included (modeling_numbat.py); the eval runs used the internal
Neuron-parallel runtime, but this port consumes the same tensors and
round-trips every shard.
FAQ
Q: How did you get this? A: Can't say more than what's already in the repo.
Q: When will more shards be uploaded? A: They're all uploading. Be patient.
Q: Can I use this for inference?
A: Yes — modeling_numbat.py implements the full architecture. Load
the tensors and run. But this is a pretraining checkpoint at step
1,830,000 of a ~1.96M step run. No post-training, no RLHF. Raw
pretraining-completion output. That's expected.
Q: Why is a mid-pretraining checkpoint in NVFP4? A: The eval team quantizes every async checkpoint to NVFP4 so evals run on a slice of Trainium2s instead of the full training cluster — still ~85 of them just to hold these weights. The raw BF16 training weights plus optimizer state never leave the cluster. This is the eval copy.
Q: Is this real? A: Yes.
- Downloads last month
- 7,108
