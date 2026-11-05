---
id: "675e2cebb0bbe2e0"
title: "Anthropic found a way to prove which AI model answered you — but there’s a costly catch"
url: "https://thenewstack.io/anthropic-flashprove-model-verification"
link: "https://thenewstack.io/anthropic-flashprove-model-verification"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-04T22:50:18Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Developers using AI APIs have little way of knowing whether the model answering their requests is actually the one they’re paying for. A provider could route requests to a cheaper model, or an attacker could interfere with responses, without customers having an obvious way to detect the switch. \n\n Now, Anthropic wants to change that. The company’s Frontier Red Team has released FlashProve , an…"
tags: ["AI Models", "Open Source", "Security"]
orgs: ["Anthropic", "Meta", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "summary"
word_count: 662
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic found a way to prove which AI model answered you — but there’s a costly catch

The New Stack · Amanda Caswell · 2026-11-04

Developers using AI APIs have little way of knowing whether the model answering their requests is actually the one they’re paying for. A provider could route requests to a cheaper model, or an attacker could interfere with responses, without customers having an obvious way to detect the switch. 

 Now, Anthropic wants to change that. The company’s Frontier Red Team has released FlashProve , an open-source cryptographic system designed to verify which AI model produced a response without exposing its underlying weights. 

 Announced Tuesday , the research could eventually help developers verify third-party AI services and detect compromised inference systems. But FlashProve remains a research prototype, and the cost of generating proofs makes it impractical for routine API traffic. 

 But FlashProve remains a research prototype, and the cost of generating proofs makes it impractical for routine API traffic. 

 How FlashProve proves the model 

 FlashProve uses zkSNARKs to verify that a response came from a specific set of model weights without revealing those weights. The commitment still has to come from a trusted source, or the proof means little. 

 Anthropic has released FlashProve on GitHub , where developers can download the code and test the system themselves. It’s still a research prototype, however, and isn’t available as a feature of the Claude API. 

 The cost of every proof 

 Anthropic tested FlashProve on Meta’s Llama 4 Maverick, a 400-billion-parameter mixture-of-experts model, rather than Claude. 

 According to Anthropic’s benchmarks , FlashProve processed roughly 110 prompt tokens per second while generating proofs on a single Nvidia H100 GPU. Each proof was about 18.78 MB and took around 21 seconds to verify on a single CPU thread. Generating the proof is far more expensive than checking it. 

 Compared with standard inference using vLLM, FlashProve needed 70 to 95 times more GPU time to generate proofs. It also generates them in batches after requests are completed, rather than verifying tokens as they’re delivered. 

 FlashProve cuts proof sizes to roughly 19 MB and verification times to seconds 

 FlashProve cuts proof sizes to roughly 19 MB and verification times to seconds, although generating those proofs remains expensive and less practical for applications that need immediate verification of every response. 

 For developers already watching every token of their inference spend , adding that much GPU overhead would be difficult to justify for routine API traffic. 

 Still, Anthropic says FlashProve is substantially faster than previous open-source systems. An earlier system called VerInf needed 14.3 hours to generate a proof covering 1,000 tokens. The resulting proof was 93.6 GB and took almost a day to verify. 

 Claude built it, humans verified 

 Anthropic credits Claude with much of FlashProve’s development, including optimizations that made its cryptographic proofs substantially faster. But the researchers still had to verify that those improvements hadn’t compromised the protocol’s security guarantees. 

 The team used Lean to formally verify the protocol’s mathematical properties, including that it accepts valid proofs, rejects forged proofs with overwhelming probability, and doesn’t reveal the model’s weights beyond what the responses disclose. 

 FlashProve includes two verifiers: a faster C++ implementation and a Lean version backed by formal proofs. The C++ verifier passed Anthropic’s comparison tests, but it hasn’t been formally verified. Neither has the GPU prover. 

 Anthropic says the C++ verifier and GPU prover have been tested against the formally defined protocol, but neither has the same mathematical guarantees as the Lean implementation. 

 Why FlashProve isn’t production-ready 

 FlashProve is still limited to 1,024 tokens of context. It also uses integer-based inference and greedy decoding, while production models typically rely on floating-point calculations and sampling. 

 There’s no indication of when, or whether, FlashProve will make its way into the Claude API. 

 There’s no indication of when, or whether, FlashProve will make its way into the Claude API. Anthropic describes the GitHub release as a research artifact that isn’t being maintained or accepting contributions. 
 The post Anthropic found a way to prove which AI model answered you — but there’s a costly catch appeared first on The New Stack .
