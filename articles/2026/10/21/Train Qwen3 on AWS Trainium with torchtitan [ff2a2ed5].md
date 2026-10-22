---
id: "ff2a2ed5c2250c2f"
title: "Train Qwen3 on AWS Trainium with torchtitan"
url: "https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan"
link: "https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-21T20:00:22Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Josh Longenecker"]
language: "en"
summary: "Using torchtitan on AWS Trainium means using it the way you always have. TorchNeuron registers Trainium as a native PyTorch device, which lets torchtitan use it through standard PyTorch interfaces. You can use these configurations to pre-train from random initialization or fine-tune published weights. You can also customize the model implementation and kernels for your workload. In this post,…"
tags: ["Advanced (300)", "AWS Trainium", "Technical How-to"]
orgs: ["Hugging Face", "Amazon", "Alibaba"]
topics: ["models & research", "products & launches"]
content_source: "fulltext"
word_count: 1599
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Train Qwen3 on AWS Trainium with torchtitan

AWS Machine Learning Blog · Josh Longenecker · 2026-10-21

Artificial Intelligence
Train Qwen3 on AWS Trainium with torchtitan
Using torchtitan on AWS Trainium means using it the way you always have. TorchNeuron registers Trainium as a native PyTorch device, which lets torchtitan use it through standard PyTorch interfaces. You can use these configurations to pre-train from random initialization or fine-tune published weights. You can also customize the model implementation and kernels for your workload. In this post, you train Qwen3 three ways on a single trn2.48xlarge.
The first method uses Transformers v5 as a modeling backend in torchtitan. It runs Hub models through AutoModelForCausalLM and reads and writes published safetensors directly. The second method switches to torchtitan’s native Qwen3 by changing config.model_spec. The third adds Neuron Kernel Interface (NKI) mixture-of-experts (MoE) kernels from the torchtitan-neuron recipes and then uses torchtitan’s override registry to attach your own kernel. All three configurations use the same torchrun launch pattern and config structure.
Prerequisites
To follow this walkthrough, use a single trn2.48xlarge with either the AWS Deep Learning AMI for Neuron or a Neuron PyTorch training container. Both environments provide the Neuron driver, runtime, and compiler required to train on Trainium.
Before you install torchtitan-neuron, check whether your environment already includes it. The following command prints the installed version and package path:
This walkthrough uses the versions in the following table. To reproduce the examples, pin these versions. The Transformers v5 integration and Trainium-specific override modules can change between torchtitan releases.
When torch_neuronx is installed, TorchNeuron registers Trainium as the neuron device and torchtitan detects it at startup. In eager mode, Neuron compiles operations as they execute. With torch.compile, Neuron compiles the captured graph. This same launch pattern works across all three configurations.
For the versions used in this walkthrough, install torchtitan-neuron and torchtitan’s remaining dependencies with --no-deps to preserve the Neuron build of torch:
Before you start training, get the Qwen3 model artifacts from Hugging Face Hub. Store them in a local directory that you can pass to the training config:
Each training configuration is a Python config function. The three examples start from a base config that you update for each step.
Train with Hugging Face Transformers v5
In the first configuration, Transformers v5 builds Qwen3 through AutoModelForCausalLM. The Hub model definition supplies the implementation used for the forward and backward passes. You select the model by setting its Hub ID in the config.
Start with transformers_modeling_backend_full(). It leaves the fields that map to Hugging Face configuration keys unset, so AutoConfig.from_pretrained() loads the model architecture from the Hub.
Create neuron_qwen3.py in the torchtitan-neuron repository root, where you run the training command. Add the imports, model artifact path, and base config:
This command launches 64 training processes, one for each logical NeuronCore. --module neuron_qwen3 imports the local config module. --config v5_qwen3_4b selects the configuration function. The data parallel setting shards the model across all 64 ranks.
Load and save Hugging Face checkpoints
To fine-tune from published weights, enable checkpoint loading and point initial_load_path to ASSETS. The state-dictionary adapter adjusts the leading model. prefix and handles tied embeddings. It saves the final checkpoint as Hugging Face safetensors.
Use the first training-step loss as a quick check that torchtitan loaded the published weights. For Qwen/Qwen3-4B-Instruct-2507, the verified run produced a step 1 loss of 6.54 from published weights and 12.43 from random initialization.
After training, load the exported checkpoint with AutoModelForCausalLM and load_state_dict. A successful round trip reports no missing or unexpected keys other than lm_head.weight, which Qwen3-4B ties to the token embeddings. This confirms that the files remain a standard Hugging Face checkpoint.
Train with torchtitan’s native models
In the second configuration, torchtitan builds its native Qwen3Model. Add the native Qwen3 imports and config function to neuron_qwen3.py:
This example starts from qwen3_32b() because the tested torchtitan build does not provide a generic qwen3_4b() config builder. The next line replaces the 32B model specification with the 4B specification. The remaining fields reproduce the tested run.
config.model_spec selects the model class and defines how torchtitan shards the model and maps its checkpoint keys. Here, model_registry("4B", attn_backend="sdpa") selects torchtitan’s native Qwen3 implementation with scaled dot product attention (SDPA).
Add NKI kernels for mixture of experts
In the third configuration, torchtitan runs mixture-of-experts layers with kernels written in NKI, the Neuron kernel language. Add the required imports and Qwen3 MoE config function to neuron_qwen3.py:
This configuration uses data parallel sharding across 64 ranks with a tensor parallel degree of 1. It does not use expert parallelism. num_experts=64 sets the number of experts in the model, not the expert parallel degree.
Setting CompileConfig(enable=False) runs this example in eager mode. TorchNeuron supports registered NKI operators in both eager execution and torch.compile.
In the torchtitan build used for this walkthrough, qwen3_nki_moe_config() replaces the MoE block with the NKI grouped-experts implementation. It also selects SDPA and the gather-free rotary embedding. When you enable torch.compile, add "grad_clip" to CompileConfig.components to compile gradient-norm clipping.
NKI kernels enter training as PyTorch operators. wrap_nki makes an NKI kernel callable from PyTorch, and nki_op registers the operator. register_autograd attaches its backward pass using routing metadata saved during the forward pass.
The example reduces Qwen3-30B-A3B to 4 layers and 64 experts so it fits on one trn2.48xlarge. It routes each token to 4 experts with top_k=4.
Attach your own NKI kernel
In some cases, you might want to optimize an operation for the tensor shapes in your model. A specialized kernel can tailor its tiling and data movement to those shapes. It can also replace a performance-critical sequence of PyTorch operations with one optimized operator. You can write the kernel yourself or start with one from nkilib. This example uses rope_hf from nkilib.core.embeddings, which expects the Hugging Face tensor layout and supports its own backward mode. This example demonstrates kernel registration and autograd integration, not a performance improvement.
Create my_neuron_kernels.py in the repository root, where you launch training. torchtitan stores query and key as [batch, seq, heads, head_dim], whereas rope_hf expects [batch, heads, seq, head_dim]. Convert the layout inside the operator and allocate the output tensors with torch.empty_like():
rope_hf computes gradients when you call it with backward=True. Register a second operator for that mode. Save the rotary cache during the forward pass so the backward pass can reuse it. Return None for the cache gradient because the cache is not differentiable.
Because rope_hf requires a supported sequence length, validate that constraint before calling the kernel. Subclass CosSinRoPE and call rope_fwd from apply_rotary_emb:
Register NKIRoPE as the replacement for CosSinRoPE. derive() copies the shared configuration fields into the replacement config:
To load the custom override, pass its module name to --override.imports. torchtitan imports the registry entry before it builds the model:
Before training starts, torchtitan logs each config node that the override replaces. Confirm that the output contains one nki_rope entry for each Qwen3 layer:
Set the sequence length to a multiple of 128 * LNC, which is 256 when LNC is 2. Reshape the rotary cache to [seq, head_dim * 2], with cosine values in the first half and sine values in the second. The kernel validates these constraints before training begins.
For a complete torchtitan example, see torchtitan_neuron/models/gpt_oss/nki_attention.py. It connects nkilib flash-attention kernels through the same operator and override mechanisms. It also handles DTensor inputs for tensor parallelism.
Before you train with a custom kernel, compare its outputs with the implementation it replaces. In the numerical test with float32 inputs, rope_hf and torchtitan’s PyTorch rotary embedding produced a maximum absolute difference of 0.0 for both query and key.
When you register multiple overrides, limit each one to the intended module instances with fqns. For example, fqns=["layers.1[0-9].attention.rope"] targets the rotary embedding in layers 10 through 19. torchtitan stops when two overrides claim the same node and warns when an override matches no nodes.
Review the training output
At startup, confirm that torchtitan reports 64 ranks and the expected model. The first step includes compilation and takes longer than later steps. Each training step reports the loss, gradient norm, high-bandwidth memory (HBM) usage, throughput, and model FLOPs utilization (MFU). For the checkpoint run, confirm that the first-step loss is near 6.54. For the custom kernel run, confirm that the nki_rope override appears once for each Qwen3 layer.
Scale across the instance
The same parallelism settings apply to the Transformers and native model configurations. A trn2.48xlarge exposes 64 logical NeuronCores at LNC=2. Set data_parallel_shard_degree = -1 to shard the model parameters, gradients, and optimizer state across every rank that torchrun starts.
Set config.parallelism.tensor_parallel_degree to shard each layer’s weights across a group of ranks. Each rank computes a slice of every matrix multiplication. With sequence parallelism enabled by default, normalization layers run on activations sharded along the sequence dimension. torchtitan combines tensor parallelism with Fully Sharded Data Parallel (FSDP) on a multidimensional DeviceMesh.
Watch per-rank HBM as you increase the model size, sequence length, or local batch size. These values determine how much memory each rank requires.
Clean up
If you want to keep your checkpoints, copy them to persistent storage before you clean up. If you plan to reuse the instance, stop it. When you no longer need the instance, terminate it.
Conclusion
AWS Trainium works as a supported torchtitan device across all three configurations in this walkthrough. You can train Qwen3 through Hugging Face Transformers v5 and load or save published safetensors directly. You can also train with torchtitan’s native Qwen3 implementation by setting config.model_spec. For mixture-of-experts models, use the torchtitan-neuron NKI recipes. For custom kernels, use the override registry to attach NKI operators through the same launch flow.
For setup guidance, see the AWS Neuron documentation. For current source and training recipes, see the torchtitan repository.
