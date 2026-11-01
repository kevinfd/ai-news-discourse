---
id: "68e6d6391c01f352"
title: "[PR] Q2_0_R8 CPU (AVX2/VNNI) acceleration in ik_llama.cpp for GSQ-RCO and ternary quants: benchmarks and guide"
url: "https://reddit.com/r/LocalLLaMA/comments/1xkh2ag/pr_q2_0_r8_cpu_avx2vnni_acceleration_in_ik"
link: "https://reddit.com/r/LocalLLaMA/comments/1xkh2ag/pr_q2_0_r8_cpu_avx2vnni_acceleration_in_ik"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T18:06:28Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Any_Bus9205"]
language: "en"
summary: "Demande de tirage : https://github.com/ikawrakow/ik_llama.cpp/pull/2785 Les récents modèles à faible bit produits avec GSQ et RCO (comme les collections ISTA-DASLab) ou les poids ternaires s'appuient sur des tenseurs Q2_0 : Collection : https://huggingface.co/collections/ISTA-DASLab/gsq-rco-gguf Exemple de modèle : https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF La PR #2785…"
tags: ["r/LocalLLaMA"]
orgs: ["Intel"]
topics: ["models & research"]
content_source: "post"
word_count: 329
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xkh2ag/pr_q2_0_r8_cpu_avx2vnni_acceleration_in_ik/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [PR] Q2_0_R8 CPU (AVX2/VNNI) acceleration in ik_llama.cpp for GSQ-RCO and ternary quants: benchmarks and guide

Reddit · Any_Bus9205 · 2026-10-31

Demande de tirage : https://github.com/ikawrakow/ik_llama.cpp/pull/2785 Les récents modèles à faible bit produits avec GSQ et RCO (comme les collections ISTA-DASLab) ou les poids ternaires s'appuient sur des tenseurs Q2_0 : Collection : https://huggingface.co/collections/ISTA-DASLab/gsq-rco-gguf Exemple de modèle : https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF La PR #2785 introduit le support pour Q2_0_R8 (une disposition réorganisée par 8 lignes pour Q2_0 à 2.25 bpw) avec des noyaux AVX2/AVX-VNNI dédiés (utilisant dpbusd ou maddubs), ainsi que des corrections de bogues pour la gestion des blocs de compte impair dans l'héritage Q2_0. Mesures de performance : Matériel : Intel Core i5-13420H (4 cœurs P utilisés via --cpu-affinity, AVX-VNNI) OS : Linux Mint 22.3 (noyau 7.0) Modèle : Ternary-Bonsai-2-4B Q2_0 Débit : Q2_0 natif : 34.46 t/s (pp512) | 9.56 t/s (tg128) Q2_0 avec réemballage à l'exécution (-rtr) : 49.99 t/s (pp512) | 11.64 t/s (tg128) Q2_0_R8 (réemballage hors ligne) : 49.08 t/s (pp512) | 11.55 t/s (tg128) Gain observé : ~+45% sur le traitement des invites et ~+22% sur la génération de tokens. Évaluation de perplexité (README, n_ctx=128, 3 morceaux) : Q2_0 natif : 13.0721 Q2_0 avec -rtr : 13.0763 Q2_0_R8 (réemballage hors ligne) : 13.0763 Comment utiliser : Cette optimisation cible l'exécution sur CPU. Deux workflows sont disponibles : Réemballage dynamique en mémoire (recommandé pour les fichiers GGUF Q2_0 existants) : Exécutez le modèle Q2_0 original avec le flag -rtr. Les poids seront réemballés en RAM à la volée au démarrage. GGUF réemballé hors ligne : Convertissez le modèle à l'avance en utilisant llama-quantize --repack. Le fichier sera stocké directement sous Q2_0_R8. Test rapide depuis la branche PR : git clone https://github.com/ikawrakow/ik_llama.cpp cd ik_llama.cpp git fetch origin pull/2785/head:q2_0_r8 && git checkout q2_0_r8 cmake -B build -DGGML_NATIVE=ON cmake --build build --config Release -j$(nproc) # Option 1 : Q2_0 natif avec réemballage à l'exécution ./build/bin/llama-cli -m model-Q2_0.gguf -p "Hello!" -n 128 -t 4 --cpu-affinity -rtr # Option 2 : Réemballage hors ligne en Q2_0_R8 ./build/bin/llama-quantize --repack model-Q2_0.gguf model-Q2_0_R8.gguf Q2_0_R8 ./build/bin/llama-cli -m model-Q2_0_R8.gguf -p "Hello!" -n 128 -t 4 --cpu-affinity
