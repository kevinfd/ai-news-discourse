---
id: "45de84eec1b6ddcf"
title: "I built Open-XTTS-Trainer: Now you can add new language scripts and train all 3 XTTS v2 components in 1 click [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xcurgj/i_built_openxttstrainer_now_you_can_add_new"
link: "https://reddit.com/r/MachineLearning/comments/1xcurgj/i_built_openxttstrainer_now_you_can_add_new"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T21:03:28Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["yashubhakt"]
language: "en"
summary: "TL;DR: When Coqui AI shut down, they left XTTS v2 without official training code for the DVAE audio tokenizer and Latent HiFi-GAN vocoder, and fine-tuning new scripts (Arabic, Indic, etc.) broke on fixed vocabularies. I built Open-XTTS-Trainer — an open-source, modular 3-component training suite under MPL-2.0 with verified GPU loss convergence on real human speech and a 1-click Colab demo. Why I…"
tags: ["r/MachineLearning"]
orgs: ["Google", "Nvidia", "Hugging Face"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 347
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xcurgj/i_built_openxttstrainer_now_you_can_add_new/"
score: null
comments: null
community: "r/MachineLearning"
---

# I built Open-XTTS-Trainer: Now you can add new language scripts and train all 3 XTTS v2 components in 1 click [P]

Reddit · yashubhakt · 2026-10-22

TL;DR: When Coqui AI shut down, they left XTTS v2 without official training code for the DVAE audio tokenizer and Latent HiFi-GAN vocoder, and fine-tuning new scripts (Arabic, Indic, etc.) broke on fixed vocabularies. I built Open-XTTS-Trainer — an open-source, modular 3-component training suite under MPL-2.0 with verified GPU loss convergence on real human speech and a 1-click Colab demo. Why I Built This XTTS v2 is one of the best local zero-shot TTS models we have, but training/adapting it has been painful since Coqui closed: Missing Component Recipes: Only GPT fine-tuning was commonly available. Stage 1 (DVAE) and Stage 3 (HiFi-GAN vocoder) training pipelines were either unreleased or fragmented. The Tokenizer Wall: XTTS was hardcoded for 17 languages. Feeding text with new Unicode scripts (Hindi, Arabic, Thai, Dhivehi, etc.) caused token out-of-vocab or matrix dimension crashes. Dependency Rot: Upgrading to modern PyTorch (2.4+) broke on missing torchcodec and licensing prompts. What’s in the Suite Stage 1 (Audio Tokenizer — DVAE): Full training & fine-tuning loop with Gumbel-Softmax codebook annealing and mel-spectrogram reconstruction loss. Stage 2 (Text & Vocab Extender — GPT): Scans a new language corpus, discovers unique Unicode glyphs, appends them to the tokenizer, and dynamically resizes the GPT embedding matrix without corrupting existing weights. Includes the autoregressive GPT training loop. Stage 3 (Neural Vocoder — Latent HiFi-GAN): Latent-conditioned vocoder training with Multi-Period (MPD) and Multi-Scale (MSD) discriminators and feature-matching loss. Dependency-Rot Free: Runs out-of-the-box on modern PyTorch (Python 3.10–3.13) without torchcodec blocking. Verification & GPU Benchmarks Tested on an NVIDIA T4 GPU using real human speech (LJSpeech + JFK address): HiFi-GAN Mel Reconstruction Loss: Plunged 67% ($190.83 \rightarrow 63.49$) over 10 epochs. Discriminator Equilibrium: MPD + MSD stabilized cleanly at 3.62 (no mode collapse). DVAE Mel Error: Dropped 67% ($8.14 \rightarrow 2.71$). (Note: These benchmarks verify component-level training convergence and gradient stability. Full end-to-end text-to-speech inference connects the trained modules into the standard XTTS generation pipeline). Links & Code GitHub: https://github.com/amitbhakt/open-xtts-trainer Hugging Face: https://huggingface.co/amitbhakt/open-xtts-trainer 1-Click Google Colab: open_xtts_train_demo.ipynb License: Mozilla Public License 2.0 (MPL-2.0) Feedback, PRs, and experiments with new languages are very welcome!
