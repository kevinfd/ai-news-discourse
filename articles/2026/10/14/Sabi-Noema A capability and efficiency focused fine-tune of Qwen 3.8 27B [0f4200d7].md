---
id: "0f4200d7c3e2aba6"
title: "Sabi-Noema: A capability and efficiency focused fine-tune of Qwen 3.8 27B"
url: "https://reddit.com/r/LocalLLaMA/comments/1x62zrz/sabinoema_a_capability_and_efficiency_focused"
link: "https://reddit.com/r/LocalLLaMA/comments/1x62zrz/sabinoema_a_capability_and_efficiency_focused"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T21:01:32Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["ExperienceDry6608"]
language: "en"
summary: "tl;dr: new qwen finetune that simultaneously pushes the frontiers of small model capability and reasoning efficiency. Hey everyone, We publish two post-trained versions of Qwen 3.8 27B called Sabi-Noema and Sabi-Noema-MLA . These models push the capability frontier on <30B models with 2x reduction in verbosity, and are exclusively trained on open source environments. These models have improved…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Hugging Face"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 273
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x62zrz/sabinoema_a_capability_and_efficiency_focused/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Sabi-Noema: A capability and efficiency focused fine-tune of Qwen 3.8 27B

Reddit · ExperienceDry6608 · 2026-10-14

tl;dr: new qwen finetune that simultaneously pushes the frontiers of small model capability and reasoning efficiency. Hey everyone, We publish two post-trained versions of Qwen 3.8 27B called Sabi-Noema and Sabi-Noema-MLA . These models push the capability frontier on <30B models with 2x reduction in verbosity, and are exclusively trained on open source environments. These models have improved capabilities on coding, agentic and tool calling tasks, as well as hallucinating lesser. Sabi-Noema beats GPT 6 Luna-medium on DeepSWE, placing in between Luna 6 medium and high. It beats Luna-high on agentic and tool calling benchmarks like TB2.1, Tau-3 bench, ClawEval, and BFCL v4. Its hallucination rate is considerably lower than Luna, Qwen and other competing models. https://preview.redd.it/3ls45pejthvh1.png?width=1760&format=png&auto=webp&s=a6f6197e3a800add3aab3ddf00e110316b4476b0 These models are much more reasoning efficient. Sabi-Noema generates 50% fewer tokens per response on TB2.1 and 25% fewer tokens on DeepSWE, compared to base Qwen. Sabi-Noema-MLA goes even further by doing a post-hoc MLA conversion of Qwen's GQA attention. This conversion uses only a calibration dataset and no extra training. With BF16 latents Sabi-Noema-MLA needs 3.6x lower bytes per token. The MLA latents can be further compressed to FP8 with the total KV cache size on TB2.1 to 8.4x smaller with similar performance. To put this in perspective, when using Sabi-Noema-MLA at q4_0, on a 24GB GPU like 3090/4090 you can get a context size of ~534K where base Qwen at FP8 cache would only get to ~150K context. https://preview.redd.it/es8zpekkthvh1.png?width=1760&format=png&auto=webp&s=3fe3739796f76e424aaaad8bc2c1ef5284fe6752 We are excited to have the open source community play around with these models. We will be releasing more post-trains in the future focused on making <30B models more powerful. HuggingFace: Sabi-Noema: https://huggingface.co/sabicap/sabi-noema Sabi-Noema-MLA: https://huggingface.co/sabicap/sabi-noema-mla
