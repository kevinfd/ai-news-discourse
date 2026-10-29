---
id: "30cc023e8fa89217"
title: "Nvidia launches a promptable transcription model"
url: "https://thenewstack.io/nvidia-nemotron-promptable-transcription"
link: "https://thenewstack.io/nvidia-nemotron-promptable-transcription"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T15:00:00Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Nvidia on Wednesday launched Nemotron 3.5 Transcribe, its latest multilingual transcription model. The new open-weight model, the company says, ranks first on Hugging Face’s Open ASR open model leaderboard for English, with an average word error rate of 5.33%, and also sits at the top of two speaker-attribution benchmarks. \n\n But what’s maybe even more interesting is that this is a promptable…"
tags: ["AI", "AI Models", "Open Source"]
orgs: ["Nvidia", "Hugging Face", "Mistral"]
topics: ["models & research", "chips & infrastructure", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 527
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Nvidia launches a promptable transcription model

The New Stack · Frederic Lardinois · 2026-10-28

Nvidia launches a promptable transcription model
Nvidia on Wednesday launched Nemotron 3.5 Transcribe, its latest multilingual transcription model. The new open-weight model, the company says, ranks first on Hugging Face’s Open ASR open model leaderboard for English, with an average word error rate of 5.33%, and also sits at the top of two speaker-attribution benchmarks.
But what’s maybe even more interesting is that this is a promptable transcription model. Being promptable here means that the user can give the model specific instructions before it listens. Typically, that means setting the context for the transcription by telling the model that a given audio file is a medical discussion in English, for example, and giving it a list of medical terms.
Users can also tell the model to label each speaker or ask it questions about the audio. They can request a verbatim transcript or a cleaned-up version, and tell it how to format numbers, for example.
Nvidia bundles these capabilities, along with translation, into a single checkpoint, which could simplify the work of building applications around them.
Ideally, setting this context reduces the error rate. The trade-off is that these models are much larger than traditional transcription models, which are often under a billion parameters in size. Nemotron 3.5 Transcribe is a 30B mixture-of-experts model with 4 billion active parameters.
This isn’t a completely new concept, though. We’ve recently seen some other promptable speech-to-text models like Mistral’s Voxtral models and AssemblyAI’s Universal 3 Pro.
Nvidia, though, is able to rival Voxtral’s error rate with far fewer active parameters. On Artificial Analysis’s benchmark, Nemotron scores a 2.81% word error rate, compared with Voxtral Small’s 2.77%, while using about 4 billion active parameters versus 24 billion. That comparison measures accuracy against active parameter counts, though, rather than runtime or memory requirements.
The model can transcribe 40 languages — and translate 31 of those to or from English. Speaker attribution works for 13 of those languages, and it can distinguish between up to eight speaker voices. Audio Q&A was trained in English.
The model handles recordings up to an hour long. It’s built for recorded audio, though, and doesn’t support live streaming.
Developers can serve the model with vLLM or run it locally with NeMo-Speech.cpp. Nvidia says it runs on a single GPU, with supported hardware ranging from Jetson AGX Thor and DGX Spark to Blackwell data-center GPUs.
Since this is an open-weight model (under the OpenMDW-1.1 license), users can fine-tune it to their needs in order to reduce the error rate by using NeMo Speech’s fine-tuning tools, among other tools.
In a medical transcription case study, Nvidia says fine-tuning reduced word error rate on held-out speakers from 22.44% with its best prompt to 12.17%, a 45.8% relative reduction. The complete adaptation workflow took about 14 GPU-hours on a single GB300.
Nvidia is also releasing Granary v2, a reusable data curation pipeline built with NeMo Curator, along with public manifests covering roughly 463,062 hours across 48 languages and 16 source corpora. Developers can run the pipeline on their own recordings to prepare their data for customization. These figures describe the dataset release, not Transcribe’s full training mixture or its sampling weights.
