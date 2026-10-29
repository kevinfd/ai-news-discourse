---
id: "7090b7688c16bc73"
title: "[R] Taking EmbeddingGemma-2 (577M) from Rank #26 to #1 on the MAEB audio benchmark by filling its 256d null space with PCA-reduced intermediate Conformer layers (zero training) [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xho7pr/r_taking_embeddinggemma2_577m_from_rank_26_to_1"
link: "https://reddit.com/r/MachineLearning/comments/1xho7pr/r_taking_embeddinggemma2_577m_from_rank_26_to_1"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T13:34:01Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["JeanMichelRanu"]
language: "en"
summary: "Model & weights: BrunoHays/embeddinggemma-2-nullspace-audio I wanted to share an experiment on google/embeddinggemma-2 (577M) for MAEB, the 30-task audio benchmark on the MTEB leaderboard . By projecting intermediate Conformer layers into the unused null space of the model's final projection matrix using only PCA, the model's macro score jumps from 49.3% to 54.4% (+5.1 points) , moving from Rank…"
tags: ["r/MachineLearning"]
orgs: ["Google", "Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 524
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xho7pr/r_taking_embeddinggemma2_577m_from_rank_26_to_1/"
score: null
comments: null
community: "r/MachineLearning"
---

# [R] Taking EmbeddingGemma-2 (577M) from Rank #26 to #1 on the MAEB audio benchmark by filling its 256d null space with PCA-reduced intermediate Conformer layers (zero training) [R]

Reddit · JeanMichelRanu · 2026-10-28

Model & weights: BrunoHays/embeddinggemma-2-nullspace-audio I wanted to share an experiment on google/embeddinggemma-2 (577M) for MAEB, the 30-task audio benchmark on the MTEB leaderboard . By projecting intermediate Conformer layers into the unused null space of the model's final projection matrix using only PCA, the model's macro score jumps from 49.3% to 54.4% (+5.1 points) , moving from Rank #26 to #1 on MAEB audio-only (and #16 to #1 on full MAEB ), ahead of 8B-9B multimodal models. 1. Last-layer filtering in text-aligned audio encoders Across the MAEB leaderboard, LLM-backed Omni embedders score 95-99% on multilingual text-to-audio retrieval, but drop to 1%-6% on unsupervised audio clustering and ~20% on vocal emotion ( CREMA-D ). Aligning an audio encoder to a text LLM filters the final layers: lexical content ( what was said ) is kept, while paralinguistic and acoustic traits ( timbre, pitch, emotion ) are discarded. 2. Probing the 12 Conformer layers Layer-wise speech studies ( Pasad et al. ; Bouziane, Mdhaffar & Estève ) show that speaker, prosodic, and semantic attributes peak at different depths inside speech encoders. Probing all 12 Conformer layers of embeddinggemma-2 confirmed this: Layer 2 (mean + std pooling): VoxPopuli gender clustering goes from 0.05% (final output) to 66.6% (Layer 3) / 65%+ (Layer 2), and IEMOCAP gender classification goes from 66.4% to 83.0% . Layer 6 (mean pooling): CREMA-D emotion classification doubles from 19.7% to 39.5% . 3. Why EmbeddingGemma-2 has a 256d null space In embeddinggemma-2 , the text backbone hidden size is 512 , and the terminal projection matrix W has shape 768 x 512 with no activation after it: 512d text subspace: Because W maps linearly from 512d to 768d, every text vector lies in a 512d subspace. 256d null space: Taking the SVD of W gives the remaining 256 orthogonal directions (the null space) that text vectors never use. Zero text interference: Any audio vector injected into those 256 directions has zero dot product with all text vectors. 4. Zero-training PCA injection I compressed Layer 2 and Layer 6 down to 256 dimensions using PCA (fitted on 1,400 clips from 4 external audio datasets, with no MAEB/MSEB data) and injected them into the 256d null space before normalizing: Text embeddings: bit-for-bit unchanged. Text-to-audio retrieval (100+ languages on FLEURS, CommonVoice, Google SVQ): unchanged within 0.05 points. Audio-to-audio tasks: gender clustering jumps 0.05% -> 63.1% , artist retrieval 55.2% -> 93.8% , emotion 19.7% -> 40.2% , and environmental sounds 38.8% -> 56.3% . 5. Caveats No Matryoshka on audio: Because there is no retraining, we need all 768 dimensions for orthogonality to hold and lose the 512/256/128 truncation options. Spoken-intent trade-off: Adding fixed acoustic features slightly scales down the 512d semantic component after normalization, which hurts audio-to-audio tasks where speaker voice should be ignored (spoken topic classification SIBFLEURS drops 57.2% -> 21.3% , spoken intent MInDS14 97.6% -> 88.3% ). Still, this shows how much untapped signal can be extracted from overtrained foundation models even with zero training. With actual training restricted to U_perp , I'm certain that we could go much further. Full per-task results and details in the Hugging Face model card .
