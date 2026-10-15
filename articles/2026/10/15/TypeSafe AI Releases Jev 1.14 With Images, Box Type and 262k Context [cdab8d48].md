---
id: "cdab8d48828d4535"
title: "TypeSafe AI Releases Jev 1.14 With Images, Box Type and 262k Context"
url: "https://marktechpost.com/2026/10/14/typesafe-ai-jev-1-14-images-box-long-context"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T05:45:03Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "TypeSafe AI has released Jev 1.14 , a new version of its System One decision model. It is live now under the jev-preview alias. It adds 3 experimental ‘danger zone’ features: images, a box type and longer context. For developers, Jev 1.14 pushes a typed decision model toward vision tasks like inspection and localization. TypeSafe shares a note that none of the 3 features are ready for production…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Decision Models", "Editors Pick", "For Devs", "Language Model", "New Releases", "Staff", "Tech News"]
orgs: ["Google"]
topics: ["models & research", "products & launches", "business & funding", "agents & coding"]
content_source: "summary"
word_count: 962
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# TypeSafe AI Releases Jev 1.14 With Images, Box Type and 262k Context

MarkTechPost · Asif Razzaq · 2026-10-15

TypeSafe AI has released Jev 1.14 , a new version of its System One decision model. It is live now under the jev-preview alias. It adds 3 experimental ‘danger zone’ features: images, a box type and longer context. For developers, Jev 1.14 pushes a typed decision model toward vision tasks like inspection and localization. TypeSafe shares a note that none of the 3 features are ready for production yet. 

 TL;DR: Jev 1.14 

 Size: Parameters not disclosed. Context is 64k tokens per request and 32k per question by default, or 262k with an opt-in header. 

 Runs on: TypeSafe’s hosted API only ( POST /v1/systemone ). No open weights. Hardware and quantized variants not disclosed. 

 Performance: Small gains everywhere, largest in multilingual support (TypeSafe’s claim, no public scores). 

 Best: In TypeSafe’s Box test, 4 edge-check questions caught 30 of 36 cut-off crops. 

 Worst: Images and Box are not production-ready, and Box has no “not found” answer. 

 What is Jev 1.14? 

 Jev is a System One model from TypeSafe AI that returns typed decisions instead of generated text. You send a state along with typed questions : Choice, Score or Noul. Jev answers each with a typed value, probabilities and a confidence score. TypeSafe trains it with Reinforcement Learning for Calibrated Decisions (RLCD) . 

 The new version, jev-1.14.0 , brings small, subtle improvements to almost everything, according to the release post . TypeSafe expects the largest gain in multilingual support. 

 How does image input work in Jev? 

 Images are composable. Each image is listed once in a top-level assets map under a reference string. You then place that reference anywhere in state , instructions or criteria . The API swaps each reference for the image before the model reads it. 

 TypeSafe says jev-1.13.0 was multimodal all along. Per the Images docs , both Jev 1.13 and Jev 1.14 now accept images. Each request needs the header TypeSafe-Danger-Zone-Images: true . 

 Key image limits : 

 PNG or JPEG still images only, up to 16 MiB per file 

 256 to 1568 pixels per side 

 32 MiB per request body 

 Images bill as input tokens at the normal price, with no separate charge 

 TypeSafe warns that all models, Jev included, perform worse on images than on pure text. It recommends the simplest possible questions. 

 What is the new Box type? 

 Box is a new question type that returns 1 bounding box per question. The answer gives top , bottom , left and right edges as fractions from 0 to 1. It also returns a confidence score. Box needs jev-1.14.0 or jev-preview , plus the images header. 

 Box always returns a box. A question about an absent object still returns 4 edges. TypeSafe suggests pairing it with a Noul question that checks whether the target exists. 

 TypeSafe also shared a small test on 36 painting crops, each cutting off part of the target. 4 per-edge Noul questions caught 30 cuts. A single “is all of it inside” question caught 26. Drawing the box as an outline and asking about it caught 20. 

 How long is Jev’s context window now? 

 By default, both models keep 64k tokens per request and 32k per question. Sending TypeSafe-Danger-Zone-Long-Context: true raises both limits to 262k tokens, per the Models docs . TypeSafe states that Jev always supported longer context internally. It capped context on purpose because Jev, like all models, is less reliable on long inputs. The dev team still recommends short contexts. 

 What do the benchmarks show? 

 TypeSafe published internal intelligence charts in the release post . They compare Jev only against open-weight models. The post does not include a numeric score table. TypeSafe says the measurement is likely biased toward its own models. It tells developers to favor their own evals. 

&&

 Pricing, availability and migration 

 Pricing is unchanged at $42 per billion input tokens, or $0.042 per million. Output tokens are free, per the Models docs . 

 The rollout plan from the release post : 

 jev-preview points to jev-1.14.0 now. 

 jev-latest moves to jev-1.14.0 in a week. 

 jev-1.13.0 stays available, with 60 days notice before deprecation. 

 jev-1.14.0 will get 30 days notice before its own deprecation. 

 How does Jev 1.14 compare? 

 Feature Jev 1.14 Jev 1.13 Gemini 3.5 Flash-Lite Model ID jev-1.14.0 jev-1.13.0 gemini-3.5-flash-lite Model type Typed decision model Typed decision model General LLM Parameters Not disclosed Not disclosed Not disclosed Default context 64k per request / 32k per question 64k per request / 32k per question 1,048,576 input tokens Long context 262k (opt-in header) 262k (opt-in header) Not applicable Image input Yes, experimental header Yes, experimental header Yes (text, images, video, audio, PDF) Bounding boxes Native box type, edges 0 to 1 No Prompted JSON box_2d , scaled 0 to 1000 ( docs ) Output Typed answers with confidence Typed answers with confidence Text, up to 65,536 tokens Input price (per 1M tokens) $0.042 $0.042 $0.30 Output price (per 1M tokens) Free Free $2.50 Status Preview ( jev-preview ) Stable ( jev-latest ) Stable 

 Key Takeaways 

 Jev 1.14 is live as jev-preview . jev-latest switches in a week. 

 Images work on Jev 1.13 and 1.14 behind a danger-zone header. 

 The new Box type returns 1 normalized bounding box per question. 

 Long-context mode lifts limits to 262k tokens, at a reliability cost. 

 Price holds at $0.042 per million input tokens, with free output. 

 Check out the release post , Models docs , Images docs and Box docs . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post TypeSafe AI Releases Jev 1.14 With Images, Box Type and 262k Context appeared first on MarkTechPost .
