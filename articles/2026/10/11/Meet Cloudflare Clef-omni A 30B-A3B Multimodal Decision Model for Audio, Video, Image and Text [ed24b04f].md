---
id: "ed24b04f4aa2e5c5"
title: "Meet Cloudflare Clef-omni: A 30B-A3B Multimodal Decision Model for Audio, Video, Image and Text"
url: "https://marktechpost.com/2026/10/11/cloudflare-clef-omni-multimodal-decision-model"
link: "https://marktechpost.com/2026/10/11/cloudflare-clef-omni-multimodal-decision-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-11T23:15:52Z"
published_date: "2026-10-11"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Cloudflare has released Clef-omni , a new open-weight member of its Clef decision model family. Clef-omni is a Cloudflare decision model that scores text, images, audio and video in 1 call. It arrived on October 9, 2026, 8 days after the original Clef and Clef-flash launch . The same update cut Clef-flash pricing below TypeSafe’s Jev and made hosted Clef roughly 2x faster. For developers, this…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Decision Models", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Open Source"]
orgs: ["Amazon"]
topics: ["models & research", "agents & coding", "jobs & society", "products & launches"]
content_source: "summary"
word_count: 829
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Cloudflare Clef-omni: A 30B-A3B Multimodal Decision Model for Audio, Video, Image and Text

MarkTechPost · Asif Razzaq · 2026-10-11

Cloudflare has released Clef-omni , a new open-weight member of its Clef decision model family. Clef-omni is a Cloudflare decision model that scores text, images, audio and video in 1 call. It arrived on October 9, 2026, 8 days after the original Clef and Clef-flash launch . The same update cut Clef-flash pricing below TypeSafe’s Jev and made hosted Clef roughly 2x faster. For developers, this removes the transcription and captioning steps that multimodal agent pipelines usually need. 

 TL;DR 

 Size: 30B total, 3B active parameters (MoE); 64,000-token context on Workers AI 

 Runs on: Workers AI as @cf/cloudflare/clef-omni ; self-hosting tested on a single H200, about 64 GB GPU memory in bfloat16 

 Performance: Close to Clef on routing and intent tasks, behind it on most reasoning and workflow evals 

 Best: 97.7 macro-F1 on CLINC150+OOS, top of the 4 Clef and Jev models 

 Worst: 2.6 accuracy on POP909-CL, and 47.4 on GPQA Diamond versus Jev’s 78.3 

 Bottom line: 
 
 Best: one call decides across 4 modalities. 

 Worst: weaker accuracy than text-focused Clef on hard reasoning. 

 What is a decision model? 

 A decision model returns typed answers with probabilities instead of generated text. You send a state and a schema of questions. The model returns a probability for every allowed option. Clef supports 3 question types : noul (true or false), choice and score . The format follows the Jev and SystemOne API from TypeSafe AI . 

 How does Clef-omni work? 

 Clef-omni is post-trained from Qwen3-Omni-30B-A3B-Instruct . Cloudflare keeps the comprehension backbone and drops the text-to-speech output path. The model runs a single prefill pass over the full payload. Video frames and audio are synced into 1 sequence for joint processing. 

 A small joint schema head then scores the options. Each valid option first gathers evidence from the input. Field vectors then cross-attend across the full context to compute confidence scores. Cloudflare froze the Qwen3 backbone and trained LoRA adapters. Training combined label-smoothed cross-entropy with Brier score calibration. 

 Supported inputs on Workers AI, per the developer docs : 

 Images: up to 4, PNG, JPEG or WebP, 64 to 1,024 tokens each 

 Audio: up to 4 clips, WAV or MP3, 300 seconds each, about 780 tokens per minute 

 Video: up to 2 clips, MP4 or WebM, 60 seconds each, sampled at 2 frames per second 

 Questions: 1 to 64 per request 

 Cloudflare reports text decisions in about 130 ms at the median and images in about 150 ms. A 21-second video with sound scores in about 1.5 seconds. 

 How does Clef-omni perform on benchmarks? 

 Cloudflare compared Clef-omni against Clef, Clef-flash and Jev on its Decision Index run. Clef-omni leads on intent classification: 94.8 macro-F1 on BANKING77 and 97.7 on CLINC150+OOS. It also tops Amazon ESCI at 57.8. 

 It trails elsewhere. Home appliances case-exact accuracy is 69.3, versus 97.73 for Clef-flash. When2Call accuracy is 63.3, versus 80.97 for Jev. On TypeSafe’s workflow evals , Clef-omni scores below Clef in all 5 reported metrics. 

&&

 Clef-omni vs Clef vs Clef-flash vs Jev 

 Feature Clef-omni Clef Clef-flash Jev Developer Cloudflare Cloudflare Cloudflare TypeSafe AI Parameters 30B total, 3B active (MoE) 27B dense 9B dense Not disclosed Base model Qwen3-Omni-30B-A3B-Instruct Qwen3.8-27B Qwen3.5-9B Not disclosed Inputs Text, image, audio, video Text, image, video frames Text, image, video frames Text (per Cloudflare ) Hosted context 64,000 tokens 64k 24k (256k self-hosted) Not disclosed by TypeSafe (Cloudflare cites 32k) Input price per M tokens $0.15 $0.24 $0.038 $0.042 License Apache-2.0 Apache-2.0 Apache-2.0 API only, early access BANKING77 (macro-F1) 94.8 94.20 90.93 79.74 CLINC150+OOS (macro-F1) 97.7 97.43 66.77 89.27 When2Call (accuracy) 63.3 72.37 65.58 80.97 BRIGHT (nDCG@10) 42.0 45.91 39.26 47.52 Invoice processing, primary action 82.0 86.2 73.3 83.1 

 Benchmark scores are from Cloudflare’s announcement and were not independently verified. 

 How much faster is Clef? 

 Cloudflare moved hosted Clef to SGLang and tuned its serving stack. No new weights were released. Median latency fell from 262 ms to 152 ms at about 800 tokens, a 1.7x gain. At about 3,400 tokens it fell from 616 ms to 305 ms, a 2.0x gain. At about 16,000 tokens it dropped from 2,721 ms to 1,635 ms. Clef support lands in SGLang 0.5.22. 

 Key Takeaways 

 Clef-omni scores text, images, audio and video in 1 decision call. 

 It is a 30B-A3B MoE on Qwen3-Omni, Apache-2.0, at $0.15 per million tokens. 

 Clef-flash now costs $0.038, under Jev’s $0.042, with 24k hosted context. 

 Hosted Clef is 1.7x to 2.0x faster at the median after moving to SGLang. 

 Clef-omni wins intent tasks but trails Clef on reasoning and workflow evals. 

 Check out the Cloudflare announcement , model weights and Workers AI docs . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Meet Cloudflare Clef-omni: A 30B-A3B Multimodal Decision Model for Audio, Video, Image and Text appeared first on MarkTechPost .
