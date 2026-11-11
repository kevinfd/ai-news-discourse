---
id: "c60899f8b42bc271"
title: "Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs"
url: "https://marktechpost.com/2026/11/10/meta-fair-e-means-k-means-faiss"
link: "https://marktechpost.com/2026/11/10/meta-fair-e-means-k-means-faiss"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-10T23:20:19Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Meta FAIR researchers have released e-means , a drop-in replacement for Lloyd’s k-means algorithm. The e-means clustering algorithm reaches the loss Lloyd’s k-means gets in 25 epochs in 1.4 to 2.6 epochs . It ships in FAISS 1.16.0 under faiss.contrib.e_means . For anyone building vector indexes, quantizers or data-curation pipelines, clustering is often the slowest offline step. e-means targets…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "New Releases", "Staff", "Tech News", "Technology", "Uncategorized"]
orgs: ["Meta", "Nvidia", "Hugging Face"]
topics: ["chips & infrastructure", "models & research", "products & launches", "business & funding"]
content_source: "summary"
word_count: 800
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs

MarkTechPost · Michal Sutter · 2026-11-10

Meta FAIR researchers have released e-means , a drop-in replacement for Lloyd’s k-means algorithm. The e-means clustering algorithm reaches the loss Lloyd’s k-means gets in 25 epochs in 1.4 to 2.6 epochs . It ships in FAISS 1.16.0 under faiss.contrib.e_means . For anyone building vector indexes, quantizers or data-curation pipelines, clustering is often the slowest offline step. e-means targets exactly that step. 

 TL;DR 

 Size: It is an algorithm. Tested from 100K to 10 billion points, up to 16.7M clusters. 

 Runs on: CPU or GPU, with PyTorch tensors or NumPy. Paper GPU runs use H100s. 

 Performance: Lower loss than Lloyd’s k-means in roughly one-tenth the epochs, across 24 dataset configurations (self-reported). 

 Best: 10-45x GPU wall-clock speedup over Flash-KMeans at equal loss. 

 Worst: 16M-centroid runs need 64 GiB of float32 accumulators, so centroids must be sharded across GPUs. 

 What is e-means? 

 e-means is a mini-batch k-means algorithm from Meta FAIR that updates centroids with exponential moving averages. 

 How does e-means work? 

 Every k-means variant keeps a sum S and a count N per cluster. The centroid is S divided by N. Methods differ only in how S and N change. 

 Lloyd recomputes S and N from the full dataset each iteration. 

 MacQueen (1967) keeps adding batch statistics forever, so stale assignments never leave. 

 e-means decays old statistics at rate α: S ← (1−α)S + αs, and the same for N. 

 Older assignments fade, so centroids track recent data. The research team expa Lloyd is a corner case: full batch with α = 1. On DEEP, that corner sits 1.8% above the best loss. 

 The team tested plain gradient descent as an alternative. At its best setting, it ended 1.6% (DEEP) and 0.4% (SIFT) above EMA. The authors suspect EMA wins because centroids always stay inside the hull of their assigned points. 

 What replaces hyperparameter tuning? 

 Two fitted scaling laws set batch size B and initial step α0 from dataset size n, cluster count k and epochs T. On held-out datasets, median regret was 0.07% for the step law. The step then follows a cosine schedule from α0 to 0.1α0. 

 What else changed? 

 Dead-cluster revival: clusters below a size threshold are revived by splitting a large cluster. 

 Finalization: training ends on each cluster’s exact last-epoch mean. 

 Fused GPU kernels: nearest-centroid assignment is fused, so saved epochs become saved seconds. 

 [EMBED: e-means interactive explainer] 

 How fast is e-means in benchmarks? 

 All numbers below are self-reported by the authors. 

 Epochs: e-means beats Lloyd’s 25-epoch loss in 1.4 to 2.6 epochs. 

 GPU: 10-45x wall-clock speedup against Flash-KMeans . 

 CPU: 8-15x speedup against Faiss k-means. 

 VIBE benchmark: all 11 embedding datasets needed 1.6 to 2.4 epochs. 

 Billion scale: DINO10B, 10 billion 1,024-dim embeddings, split into 16.7M clusters in 2.5 epochs. 

 The release thread shows a 1-CPU-thread demo. Lloyd took 4.39 s for 25 epochs. e-means took 0.43 s for 2.2 epochs. One Lloyd step touched 100,000 points (0.176 s). One e-means step touched 512 points (0.001 s). 

 Mini-batch noise also helps escape bad local minima. On a 5-blob toy, Lloyd stayed stuck on 46% of 200 starts. e-means stayed stuck on 0%. 

 Revival matters at large k. On DEEP with 16,384 clusters, proportional splitting left 47 dead clusters (0.3%). With revival off, 4,313 clusters (26.3%) died. 

 How does e-means compare with other k-means options? 

 Feature e-means Lloyd k-means (Faiss) Flash-KMeans scikit-learn MiniBatchKMeans Update rule EMA mini-batch ( blog ) Full-batch Lloyd Full-batch Lloyd, exact ( paper ) Mini-batch, Sculley-style ( docs ) Data per update Batch B from scaling law Full dataset Full dataset 1,024 points (default) Tuning beyond k None (epochs default 5) Iteration count Iteration count batch_size, max_iter, reassignment_ratio, tol Hardware CPU, GPU (H100 tested) CPU, GPU NVIDIA GPU (H200 tested) CPU Epochs to Lloyd’s 25-epoch loss 1.4 to 2.6 ( paper ) 25 (reference) Same as Lloyd (exact) Not disclosed Headline speed claim 10-45x GPU, 8-15x CPU (self-reported) Baseline Up to 17.9x vs best baselines (self-reported) Not disclosed License MIT, via FAISS ( Wikipedia ) MIT Not disclosed BSD-3-Clause ( Debian ) 

 Key Takeaways 

 e-means swaps Lloyd’s full-batch update for EMA mini-batches. 

 Matches 25 Lloyd epochs in 1.4 to 2.6 epochs. 

 10-45x faster on GPU, 8-15x on CPU (self-reported). 

 No tuning: scaling laws set batch and step size. 

 Available now in FAISS 1.16.0. 

 Check out the paper , the blog post and the FAISS code . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs appeared first on MarkTechPost .
