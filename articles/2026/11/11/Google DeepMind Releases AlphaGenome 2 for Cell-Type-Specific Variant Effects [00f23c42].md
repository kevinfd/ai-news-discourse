---
id: "00f23c4252711b7b"
title: "Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects"
url: "https://marktechpost.com/2026/11/11/google-deepmind-alphagenome-2-cell-type-variant-effects"
link: "https://marktechpost.com/2026/11/11/google-deepmind-alphagenome-2-cell-type-variant-effects"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-11T20:51:56Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Google DeepMind has released AlphaGenome 2 , a DNA model that predicts variant effects in specific cell types. AlphaGenome 2 is a conditional sequence-to-function model. It reads 1 Mb of DNA plus a target cell state. Its predecessor averaged across bulk tissues. The new model resolves closely related cell types and adapts to unseen single-cell datasets without fine-tuning. It is available…"
tags: ["Agentic AI", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Software Engineering", "Staff"]
orgs: ["Google", "Nvidia", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "products & launches", "business & funding"]
content_source: "summary"
word_count: 830
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects

MarkTechPost · Asif Razzaq · 2026-11-11

Google DeepMind has released AlphaGenome 2 , a DNA model that predicts variant effects in specific cell types. AlphaGenome 2 is a conditional sequence-to-function model. It reads 1 Mb of DNA plus a target cell state. Its predecessor averaged across bulk tissues. The new model resolves closely related cell types and adapts to unseen single-cell datasets without fine-tuning. It is available through the AlphaGenome API for non-commercial research. 

 TL;DR 

 Size: Input is a 1 Mb (1,048,576 bp) DNA window, human or mouse. 

 Runs on: Hosted API only for now. Training used 2048 TPU v4 chips; weights come “upon final publication”. 

 Performance: Beats fine-tuned AlphaGenome 1, Borzoi and Scooby on single-cell eQTL and enhancer-gene benchmarks. 

 Best: 43% recall at 90% sign accuracy on TenK10K sc-eQTLs, versus 23% for AlphaGenome 1 fine-tuned. 

 Worst: Outside accessible chromatin, sign prediction AUROC reaches only 0.63. 

 Bottom line: Best: cell-state conditioning from raw scRNA-seq. Worst: no local weights, non-commercial only. 

 What is AlphaGenome 2? 

 AlphaGenome 2 is a U-Net style model with a convolutional encoder, an 11-block transformer and a decoder. AlphaGenome 1 predicted a fixed catalog of thousands of tracks in parallel. AlphaGenome 2 instead predicts outputs for 1 condition per call. 

 The condition is a 256-dimensional embedding. It modulates activations through FiLM layers in the encoder, transformer and decoder. Conditioning only the decoder or output layers gave minimal gains. Conditioning the encoder and transformer drove most of the improvement. 

 Outputs cover RNA coverage, CAGE, splicing, chromatin accessibility, histone marks, TF binding and contact maps. CpG methylation is new. 

 How was AlphaGenome 2 trained? 

 Training runs in 4 stages: 

 Pre-training across bulk data plus 3,977 single-cell RNA and ATAC pseudobulk tracks from 36 studies. 

 Condition refinement , which tunes only the embeddings and FiLM layers. 

 Distillation of 8 teacher models into 1 student, using mutated input sequences. 

 Post-training that maps a single-cell expression encoder into the frozen model’s condition space. 

 That encoder was trained on over 100 million human scRNA-seq profiles, largely from CELLxGENE. Researchers can pass raw counts and get a condition embedding. The docs allow up to 256 cells per call. 

 How does AlphaGenome 2 perform on benchmarks? 

 On GTEx tissues, median Pearson r for cross-tissue expression changes rose from 0.61 to 0.71. Within tissues, explained cell-type variance rose from 23% to 34% for scRNA-seq. 

 The main result is on TenK10K single-cell eQTLs across 28 immune cell types. At 90% precision, AlphaGenome 2 recovered 30% of causal variants. AlphaGenome 1 fine-tuned on single-cell data recovered 16%. Direction-of-effect recall rose from 23% to 43%. 

 On held-out ENCODE-rE2G CRISPRi data, enhancer-gene AUPRC reached 0.78. AlphaGenome 1 scored 0.73, a Borzoi ensemble 0.61. The gap was widest for enhancers 100 to 2,500 kb away: 0.62 versus 0.48. 

 For assay imputation, AlphaGenome 2 beat the Avocado baseline on 166 of 181 held-out tracks. On an unseen Parkinson’s cohort, it reached 41% recall versus 17% for cohort-tuned Scooby . 

&

 How does it compare with other DNA sequence models? 

 Feature AlphaGenome 2 AlphaGenome 1 Borzoi Scooby Input DNA 1 Mb 1 Mb 524 kb 524 kb Condition handling Reference or scRNA-seq embedding Fixed multitask tracks Fixed multitask tracks Cell-embedding decoder, per dataset Single-cell outputs scRNA, scATAC No No scRNA, scATAC Parameters Not disclosed Not disclosed 235M Not disclosed Hardware Hosted API H100 recommended Not disclosed NVIDIA GPU (tested on A40) Weights / license API now, weights later, non-commercial Kaggle and HF, non-commercial terms Apache-2.0 MIT TenK10K sc-eQTL causality AUPRC* 0.76 0.72 (fine-tuned) Not evaluated 0.69 TenK10K sc-eQTL sign AUC* 0.85 0.79 (fine-tuned) Not evaluated 0.77 rE2G held-out CRISPRi AUPRC* 0.78 0.73 0.61 (4-model ensemble) Not evaluated 

 *Benchmark rows come from the AlphaGenome 2 paper and are DeepMind’s own evaluation. 

 What can developers access today? 

 AlphaGenome 2 and Colab tutorials are live through the API. An API key is free for non-commercial use . Commercial research is in private preview. The alphagenome Python package exposes the model under alphagenome.models.v2 . 

 DeepMind also released precomputed atlases. One covers enhancer-gene links across 640 primary cell conditions. Another scores about 7 million common and GWAS variants across 510 conditions. Both are on the downloads page . 

 Key Takeaways 

 AlphaGenome 2 conditions a 1 Mb DNA model on 1 cell type per call. 

 Causal sc-eQTL recall at 90% precision rose from 16% to 30%. 

 Raw scRNA-seq counts can define new cell states without retraining. 

 Precomputed scores cover about 7 million variants across 510 conditions. 

 Access is API-only and non-commercial for now. 

 Check out the paper , the DeepMind blog , the API docs and the GitHub repo . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects appeared first on MarkTechPost .
