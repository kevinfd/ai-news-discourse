---
id: "3295fd7388cdcc6b"
title: "Sub-1-Bit LLM Compression via Latent Factorization"
url: "https://github.com/SamsungLabs/LittleBit"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-08T13:29:46Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["brainless"]
language: "en"
summary: "Official implementation of LittleBit (NeurIPS 2025) and LittleBit-2 (ICML 2026).\nLittleBit-2: Maximizing the Spectral Energy Gain in Sub-1-Bit LLMs via Latent Geometry Alignment (ICML 2026)\nBanseok Lee, Youngmin Kim\nLittleBit: Ultra Low-Bit Quantization via Latent Factorization (NeurIPS 2025)\nBanseok Lee*, Dongkyu Kim*, Youngcheon You, Youngmin Kim\nLittleBit compresses large language models into…"
tags: []
orgs: ["Meta", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "safety & ethics"]
content_source: "fulltext"
word_count: 584
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50005608"
score: 90
comments: 26
community: "Hacker News"
---

# Sub-1-Bit LLM Compression via Latent Factorization

GitHub · brainless · 2026-10-08

Official implementation of LittleBit (NeurIPS 2025) and LittleBit-2 (ICML 2026).
LittleBit-2: Maximizing the Spectral Energy Gain in Sub-1-Bit LLMs via Latent Geometry Alignment (ICML 2026)
Banseok Lee, Youngmin Kim
LittleBit: Ultra Low-Bit Quantization via Latent Factorization (NeurIPS 2025)
Banseok Lee*, Dongkyu Kim*, Youngcheon You, Youngmin Kim
LittleBit compresses large language models into the sub-1-bit regime by factorizing each dense weight matrix into low-rank latent factors, binarizing those factors, and restoring magnitude information through lightweight learned scales. This enables extreme compression, including the 0.1 bits-per-weight setting, while preserving the original model architecture at inference time.
LittleBit-2 improves this recipe by addressing latent geometry misalignment in the initialization stage. It applies Internal Latent Rotation with Joint Iterative Quantization (Joint-ITQ), aligning the SVD-derived latent factors with the binary hypercube before QAT. LittleBit-2 initialization is available as an opt-in (--use_itq) and produces no additional inference overhead.
- Sub-1-bit compression: Designed for 1.0 to 0.1 bits per weight.
- LittleBit-2 opt-in: Enable Joint-ITQ initialization with --use_itq for improved latent geometry alignment.
- No inference-time change: LittleBit-2 modifies initialization only; the deployed factorized layer remains the same.
- QAT-friendly: Supports Quantization-Aware Training with SmoothSign and optional residual factorization.
The codebase currently supports:
- OPT
- Llama and Llama 2/3
- Phi-4
- Qwen2.5 and QwQ
- Gemma 2 and Gemma 3
- Qwen3
We recommend Python 3.12.
conda create -n littlebit python=3.12
conda activate littlebit
# Install CUDA toolkit. Adjust the CUDA version if needed.
conda install nvidia/label/cuda-12.4.1::cuda-toolkit -c nvidia/label/cuda-12.4.1
# Install PyTorch.
pip install torch==2.8.0+cu124 torchvision==0.23.0+cu124 torchaudio==2.8.0+cu124 --index-url https://download.pytorch.org/whl/cu124
# Install dependencies.
pip install -r requirements.txt
Important
For reproducing the paper results, use transformers 4.51.x. Newer transformers releases may change model internals or evaluation behavior.
pip install "transformers==4.51.*"
Train a model with Quantization-Aware Training. By default, LittleBitLinear uses the original SVD-only initialization. To enable LittleBit-2 (Joint-ITQ), pass --use_itq True.
Single GPU
CUDA_VISIBLE_DEVICES=0 python -m main \
    --model_id meta-llama/Llama-2-7b-hf \
    --dataset c4_wiki \
    --save_dir ./outputs/Llama-2-7b-LittleBit-2 \
    --num_train_epochs 5.0 \
    --per_device_train_batch_size 4 \
    --lr 4e-05 \
    --warmup_ratio 0.02 \
    --report wandb \
    --quant_func SmoothSign \
    --quant_mod LittleBitLinear \
    --residual True \
    --eff_bit 1.0 \
    --kv_factor 1.0 \
    --min_split_dim 8 \
    --l2l_loss_scale 10.0
# Opt-in to LittleBit-2 initialization
# --use_itq True
Multi-GPU with DeepSpeed
deepspeed --num_gpus=4 main.py \
    --model_id meta-llama/Llama-2-7b-hf \
    --dataset c4_wiki \
    --save_dir ./outputs/Llama-2-7b-LittleBit-2 \
    --ds_config_path configs/zero3.json \
    --num_train_epochs 5.0 \
    --per_device_train_batch_size 4 \
    --lr 4e-05 \
    --report wandb \
    --quant_func SmoothSign \
    --quant_mod LittleBitLinear \
    --residual True \
    --eff_bit 1.0 \
    --kv_factor 1.0 \
    --min_split_dim 8
Evaluate a local checkpoint or a model hosted on the Hugging Face Hub.
# From a local directory
CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_id ./outputs/Llama-2-7b-LittleBit-2 \
    --seqlen 2048 \
    --ppl_task wikitext2,c4 \
    --zeroshot_task boolq,piqa,hellaswag,winogrande,arc_easy,arc_challenge,openbookqa
# From the Hugging Face Hub
CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_id username/littlebit-llama-7b-0.1bpw \
    --seqlen 2048 \
    --ppl_task wikitext2
Older checkpoints may not include littlebit_config.json. In that case, pass the quantization arguments explicitly:
CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_id ./outputs/Legacy-Llama-2-7b \
    --quant_func SmoothSign \
    --quant_mod LittleBitLinear \
    --split_dim 1024
Parameter loading priority:
- Explicit CLI arguments
- littlebit_config.json in the model directory
- config.json fallback for older checkpoints
If you find this work useful, please cite:
@inproceedings{lee2026littlebit2,
  title={LittleBit-2: Maximizing the Spectral Energy Gain in Sub-1-Bit LLMs via Latent Geometry Alignment},
  author={Lee, Banseok and Kim, Youngmin},
  booktitle={Proceedings of the 43rd International Conference on Machine Learning},
  year={2026}
}@inproceedings{lee2025littlebit,
  title={LittleBit: Ultra Low-Bit Quantization via Latent Factorization},
  author={Lee, Banseok and Kim, Dongkyu and You, Youngcheon and Kim, Youngmin},
  booktitle={Advances in Neural Information Processing Systems},
  year={2025}
}
This project is licensed under the CC BY-NC 4.0 license.
