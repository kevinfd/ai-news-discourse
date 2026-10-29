---
id: "8c41760be9a1ee07"
title: "Block Unveils Dessa, a Full-Duplex Speech Model Trained Only on Speech"
url: "https://marktechpost.com/2026/10/29/block-dessa-full-duplex-speech-model"
link: "https://marktechpost.com/2026/10/29/block-dessa-full-duplex-speech-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T07:50:39Z"
published_date: "2026-10-29"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Block’s AI research lab has released Dessa , a full-duplex speech model trained only on human conversation. Block announced it on October 23, 2026 as a research preview. Dessa is a speech-to-speech model from Block that listens and talks at the same time. Block says it used no text and no pretrained models. That is a different design from the text-first stacks behind most voice agents today. \n\n…"
tags: ["Artificial Intelligence", "Audio Language Model", "Editors Pick", "Language Model", "Staff", "Technology", "Voice AI"]
orgs: ["Nvidia", "OpenAI", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "products & launches", "agents & coding"]
content_source: "summary"
word_count: 707
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Block Unveils Dessa, a Full-Duplex Speech Model Trained Only on Speech

MarkTechPost · Michal Sutter · 2026-10-29

Block’s AI research lab has released Dessa , a full-duplex speech model trained only on human conversation. Block announced it on October 23, 2026 as a research preview. Dessa is a speech-to-speech model from Block that listens and talks at the same time. Block says it used no text and no pretrained models. That is a different design from the text-first stacks behind most voice agents today. 

 TL;DR 

 Runs on: A MacBook Pro M4 Max or better, locally, faster than real time. 

 Performance: Demo-only so far. Live recordings show backchannels, mid-sentence laughs and natural interruptions. 

 Best: Trained on 1 NVIDIA GB200 NVL72 rack (72 GPUs). Moshi used 1,016 H100 GPUs. 

 Worst: 0 published benchmark scores. No weights, paper, API or price. 

 What is Block’s Dessa? 

 Dessa is a true speech-to-speech model: audio in, audio out. According to Block’s project page , everything it knows came from human speech. 

 It is full-duplex, so it listens while it talks. Block says it learned from real conversation when to cut in. It also learned when to backchannel with short cues like “yeah” or “got it”. 

 Block’s demo clips show Dessa laughing mid-sentence and getting louder when asked to speak up. One clip shows it talking with OpenAI’s GPT-Live-1. Block says nobody steered any clip. 

 How does speech-only training work? 

 Most voice systems chain 3 parts: speech recognition, a text model, then speech synthesis. Block team argues that chain throws away emotion, sarcasm, laughter and sighs. Dessa hears and produces those signals directly. 

 Block has not published the architecture. Here is what it has disclosed: 

 Training data: human conversation audio only. No text and no pretrained models. 

 Compute: 1 NVIDIA GB200 NVL72, which links 72 Blackwell GPUs and 36 Grace CPUs . 

 Data efficiency: Block says Dessa learned language from hundreds of times fewer words than LLMs need. 

 Inference: faster than real time, on a MacBook Pro M4 Max or better. 

 The lab also explains why this is hard. Speech never repeats exactly. A spoken word takes thousands of times more bytes than the same word in text. 

 Kyutai’s Moshi, the best-known open full-duplex model, takes another route. Moshi starts from a text language model backbone and predicts time-aligned text tokens before audio tokens. Its model card lists 7 million hours of pretraining audio and 1,016 H100 GPUs. 

&

 How does Dessa compare with Moshi, PersonaPlex and GPT-Live-1? 

 Feature Dessa (Block) Moshi (Kyutai) PersonaPlex-7B-v1 (NVIDIA) GPT-Live-1 (OpenAI) Starting point Speech only, no text, no pretrained model Helium text LM backbone plus audio Fine-tuned from Moshi (Moshiko) weights Not disclosed; delegates reasoning to a backend agent Parameters Not disclosed 8B (Hugging Face listing) 7B (model card) Not disclosed Training compute 1 GB200 NVL72 (72 GPUs) 1,016 H100 GPUs Not disclosed Not disclosed Training audio Not disclosed 7M h unsupervised, 2,000 h Fisher, 20,000 h synthetic Fisher English, under 10,000 h Not disclosed Latency Not disclosed (“faster than real time”) 200 ms in practice, 160 ms theoretical 0.170 s turn-taking, 0.240 s interruption (FullDuplexBench) Not disclosed on model page Weights and license Not released Open, CC-BY 4.0 Open, NVIDIA Open Model License Closed Runs on MacBook Pro M4 Max or better GPU; MLX, Candle and PyTorch checkpoints NVIDIA A100 / H100, Linux OpenAI cloud Access and price Research preview, waitlist Free download Free download (gated) API, $0.05 per minute voice layer 

 Key Takeaways 

 Dessa is full-duplex and speech-to-speech, trained only on human conversation audio. 

 Block trained it on 1 GB200 NVL72 rack; Moshi used 1,016 H100s. 

 It runs locally on a MacBook Pro M4 Max, faster than real time. 

 Block published 0 benchmarks, no parameter count and no weights. 

 Access is a waitlist. 

 Check out the Dessa project page . Compare it with the Moshi paper , the PersonaPlex model card and the GPT-Live-1 docs . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Block Unveils Dessa, a Full-Duplex Speech Model Trained Only on Speech appeared first on MarkTechPost .
