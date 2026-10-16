---
id: "adadd90b83d78209"
title: "Mix, Don't Tune: Bilingual Pre-Training Outperforms Hyperparameter Search in Data-Constrained Settings"
url: "https://machinelearning.apple.com/research/mix-dont-tune"
link: "https://machinelearning.apple.com/research/mix-dont-tune"
source: "Apple Machine Learning Research"
domain: "machinelearning.apple.com"
source_type: "research"
collector: "rss"
date: "2026-10-13T00:00:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: []
language: "en"
summary: "For most languages of the world, language model pre-training operates in a data-constrained regime where models must repeat their training data many times, degrading generalization. Two remedies exist: aggressive hyperparameter tuning such as high weight decay, and mixing in data from a high-resource auxiliary language to directly aid the low-resource target. While hyperparameter tuning…"
tags: []
orgs: ["Apple"]
topics: ["models & research", "search & media"]
content_source: "fulltext"
word_count: 472
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Mix, Don't Tune: Bilingual Pre-Training Outperforms Hyperparameter Search in Data-Constrained Settings

Apple Machine Learning Research · 2026-10-13

Mix, Don’t Tune: Bilingual Pre-Training Outperforms Hyperparameter Search in Data-Constrained Settings
AuthorsPaul Jeha†**, Anastasiia Sedova, Louis Béthune, Skyler Seto, Jes Frellsen†‡, Pierre Ablin‡, Natalie Schluter‡
content type paperpublished October 2026
For most languages of the world, language model pre-training operates in a data-constrained regime where models must repeat their training data many times, degrading generalization. Two remedies exist: aggressive hyperparameter tuning such as high weight decay, and mixing in data from a high-resource auxiliary language to directly aid the low-resource target. While hyperparameter tuning regularizes the model by shrinking weights to restrict network capacity, auxiliary data mixing uses a tunable mixing ratio to expand the training distribution and diversify the training signal with new knowledge. Both offer a principled way to improve training in a data-constrained domain. We compare these levers systematically across four model scales from 150M to 1.43B parameters, using Arabic as the low-resource target and English as the auxiliary, over approximately 1000 pre-training runs. Three findings emerge. First, mixing yields larger improvements than hyperparameter tuning on both validation loss and downstream task accuracy, and the gap grows with model size. Second, we quantify how much mixing helps: it boosts performance by an amount equivalent to 2–3× the unique target data on validation loss and 2–13× on downstream task accuracy, with the gain scaling steeply with model size. Third, this divergence reveals that target-language validation loss systematically underestimates mixing’s value. Mixing regularizes by diversifying the training signal and contributes knowledge the repeated target corpus cannot supply; validation loss captures only the first effect. Our practical recommendations are: mix in a high-resource language, prioritize the mixing ratio over hyperparameter tuning, and transfer hyperparameters from a small proxy model via μP.
- † DTU
- ‡ Equal senior authorship
- ** Work done while at Apple
Completed Hyperparameter Transfer across Modules, Width, Depth, Batch and Duration
February 13, 2026research area Methods and Algorithmsconference ICLR
Hyperparameter tuning can dramatically impact training stability and final performance of large-scale models. Recent works on neural network parameterisations, such as μP, have enabled transfer of optimal global hyperparameters across model sizes. These works propose an empirical practice of search for optimal global base hyperparameters at a small model size, and transfer to a large size. We extend these works in two key ways. To handle scaling…
Scaling Laws for Forgetting During Finetuning with Pretraining Data Injection
June 20, 2025research area Methods and Algorithmsconference ICML
A widespread strategy for obtaining a language model that performs well in a target domain is to fine-tune it by training it to do unsupervised next-token prediction on data from that domain. Fine-tuning presents two challenges: i) if the amount of target data is limited, as is the case in most practical applications, the model will quickly overfit, and ii) the model will drift away from the original model and forget the pre-training…
