---
id: "5d0d450778046c7a"
title: "Liquid AI Releases LiquidCodec, a 74M-Parameter Streaming Audio Codec"
url: "https://marktechpost.com/2026/11/12/liquid-ai-liquidcodec-streaming-audio-codec"
link: "https://marktechpost.com/2026/11/12/liquid-ai-liquidcodec-streaming-audio-codec"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-12T22:43:26Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Liquid AI has released LiquidCodec , the audio codec behind its LFM3-Audio-2B and LFM3-Omni-2B models. The LiquidCodec audio codec is a ~74M-parameter streaming speech tokenizer. It turns speech into tokens a language model can predict, then converts those tokens back into audio. Liquid AI had 2 goals: easy-to-predict tokens and fast conversion back to speech. The weights are on Hugging Face .…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "For Devs", "Language Model", "New Releases", "Staff", "Tech News", "Technology"]
orgs: ["Hugging Face", "Apple", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "summary"
word_count: 995
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Liquid AI Releases LiquidCodec, a 74M-Parameter Streaming Audio Codec

MarkTechPost · Asif Razzaq · 2026-11-12

Liquid AI has released LiquidCodec , the audio codec behind its LFM3-Audio-2B and LFM3-Omni-2B models. The LiquidCodec audio codec is a ~74M-parameter streaming speech tokenizer. It turns speech into tokens a language model can predict, then converts those tokens back into audio. Liquid AI had 2 goals: easy-to-predict tokens and fast conversion back to speech. The weights are on Hugging Face . 

 TL;DR 

 Size: ~74M parameters (73.6M on the model card ); 24 kHz audio, 12.5 Hz frames, 12 codebooks. 

 Runs on: a single CPU thread (tested on an Apple M4 Max laptop, FP32); CUDA GPUs via Transformers; Q4_0, Q4_K_M and Q8_0 GGUF builds for llama.cpp. 

 Performance: best ViSQOL and lowest mel distance on all 8 test sets versus X-Codec 2, NanoCodec and Mimi. 

 Best: ~361x real-time encoding on 1 CPU thread (encode RTF 0.0028 vs Mimi’s 0.0361). 

 What is LiquidCodec? 

 LiquidCodec is a Liquid AI speech codec that compresses 24 kHz audio into 12 token streams. Each 80 ms frame becomes 12 discrete tokens, per the LFM3-Audio-2B model card . It replaces Kyutai’s Mimi , which Liquid AI used in LFM2-Audio-1.5B. Mimi has 96.2M parameters. 

 How does LiquidCodec work? 

 The pipeline is encode, quantize, decode. Liquid AI uses blocks from its LFM3 architecture in both the encoder and decoder. The 2 halves are symmetric, and the encoder is fully causal, which suits streaming. 

 Quantization uses grouped finite scalar quantization (GFSQ) instead of residual vector quantization (RVQ). In RVQ, each codebook encodes what the previous one missed. GFSQ groups are independent, so all 12 codebooks can be predicted in parallel by MaskGIT-style transformers. 

 The decoder predicts spectral coefficients directly. This avoids learned transposed-convolution upsampling, a common cost in waveform decoders. 

 How was it trained? 

 Training ran in 2 stages. Stage 1 used 264,000 hours of speech across 107 languages. It applied waveform and spectral losses, without adversarial losses. Stage 2 fine-tuned on 55,000 hours of full-band speech (24 kHz or higher) with adversarial critics. Liquid AI says this removed metallic artifacts left after stage 1. A final decoder-only quantization-aware training (QAT) step targets edge inference. 

 How fast is LiquidCodec? 

 Liquid AI measured speed in FP32 on 1 CPU thread of an Apple M4 Max MacBook Pro. LiquidCodec ran at ~361x real time for encoding and ~87x for decoding. These are self-reported figures. 

 Real-time factor (RTF) is processing time divided by audio length, so lower is better. LiquidCodec’s encode RTF is 0.0028, against 0.0361 for Mimi, 0.2145 for NanoCodec and 0.7359 for X-Codec 2. Decode RTF is 0.0115, against 0.0329, 0.2543 and 0.0379. That is about 13x lower encode RTF and 2.9x lower decode RTF than Mimi. 

 How does LiquidCodec compare on quality benchmarks? 

 Liquid AI used 8 test sets. These were LibriSpeech test-clean, Seed-TTS English and Mandarin, and 5 FLEURS languages (German, French, Mandarin, Japanese, Korean). Baselines were X-Codec 2, NanoCodec and Mimi at 12 codebooks. 

 Reconstruction : LiquidCodec had the best ViSQOL and lowest mel distance on all 8 sets. On LibriSpeech, ViSQOL was 4.319 versus 4.219 (NanoCodec), 4.119 (X-Codec 2) and 4.031 (Mimi). 

 Text-to-speech : Liquid AI trained identical TTS models on each codec’s tokens. Data (101,000 hours, 6 languages), architecture, compute and batch order were fixed. LiquidCodec scored the highest UTMOSv2 on all 8 sets and the best WER/CER on 4 of 8. LibriSpeech WER was 3.15%, against 6.27% for Mimi. Results held with a Qwen3-1.7B backbone as well as LFM3-1.7B. 

 Where it trails : NanoCodec scored higher PESQ (WB) on 7 of 8 sets. It also led on LibriSpeech speaker similarity (SECS 0.836 vs 0.785). 

&&

 LiquidCodec vs Mimi vs NanoCodec vs X-Codec 2 

 Feature LiquidCodec Mimi NanoCodec 1.78 kbps X-Codec 2 Developer Liquid AI Kyutai NVIDIA HKUST Audio Parameters 73.6M 96.2M 62M 0.8B Sample rate 24 kHz 24 kHz ( repo ) 22.05 kHz 16 kHz Frame rate 12.5 Hz 12.5 Hz 12.5 fps 50 tokens/s Codebooks 12 8 at 1.1 kbps ( blog ) 13 1 ( docs ) Quantizer GFSQ RVQ ( docs ) FSQ Single-layer FSQ ( docs ) Bitrate Not disclosed 1.1 kbps 1.78 kbps Not disclosed Causality Causal encoder; decoder not disclosed Fully causal ( Kyutai ) Non-causal encoder, causal decoder Not disclosed License “other” on HF; blog links LFM License CC-BY 4.0 NVIDIA Open Model License CC-BY-NC 4.0 Encode / decode RTF, M4 Max CPU* 0.0028 / 0.0115 0.0361 / 0.0329 0.2145 / 0.2543 0.7359 / 0.0379 LibriSpeech mel distance* (lower is better) 0.120 0.160 0.122 0.123 LibriSpeech PESQ (WB)* 2.640 2.615 2.942 2.434 LibriSpeech TTS UTMOSv2* 3.31 2.89 3.19 3.27 

 *Measured by Liquid AI in its LiquidCodec blog . Mimi measured at 12 codebooks. 

 How can developers deploy LiquidCodec? 

 The codec loads through Hugging Face Transformers with trust_remote_code=True . Call encode() to get audio codes and decode() to get a waveform. A native LiquidCodecStreamingCache supports chunk-by-chunk decoding, per the model card . The card’s examples use CUDA with bfloat16. 

 For edge use, Liquid AI lists Q4_0, Q4_K_M and Q8_0 GGUF builds for llama.cpp. GGUF repos ship with LFM3-Audio-2B and LFM3-Omni-2B . Q4_0 with decoder-only QAT shrinks the decoder footprint by 3.5x. LibriSpeech ViSQOL dips only from 4.319 to 4.292. 

 Key Takeaways 

 ~74M-parameter streaming codec, 12.5 Hz, 12 codebooks, 24 kHz. 

 ~361x real-time encode, ~87x decode on 1 CPU thread. 

 Best ViSQOL, mel distance and TTS UTMOSv2 on all 8 test sets. 

 NanoCodec still wins PESQ (WB) on 7 of 8 sets. 

 Q4_0 decoder is 3.5x smaller with minimal quality loss. 

 Check out the technical blog , the model weights on Hugging Face , and LFM3-Audio-2B and LFM3-Omni-2B . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Liquid AI Releases LiquidCodec, a 74M-Parameter Streaming Audio Codec appeared first on MarkTechPost .
