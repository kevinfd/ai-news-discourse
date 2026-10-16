---
id: "c6f36c510a6b67ee"
title: "Liquid AI Releases d1-ultra: A Multimodal Decision Model That Scores 65 on the AA Decision Index"
url: "https://marktechpost.com/2026/10/15/liquid-ai-d1-ultra-decision-model"
link: "https://marktechpost.com/2026/10/15/liquid-ai-d1-ultra-decision-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-16T06:26:41Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Liquid AI has released d1-ultra , its most capable decision model to date. The Liquid AI d1-ultra decision model reads text, images, or both. It answers typed questions with a probability for each possible answer. It does this in one forward pass and generates no output tokens. For developers, that means classification, routing and scoring calls without paying for generated text. It is available…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Decision Models", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Python"]
orgs: ["Microsoft"]
topics: ["models & research", "products & launches", "agents & coding", "business & funding"]
content_source: "summary"
word_count: 787
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Liquid AI Releases d1-ultra: A Multimodal Decision Model That Scores 65 on the AA Decision Index

MarkTechPost · Asif Razzaq · 2026-10-16

Liquid AI has released d1-ultra , its most capable decision model to date. The Liquid AI d1-ultra decision model reads text, images, or both. It answers typed questions with a probability for each possible answer. It does this in one forward pass and generates no output tokens. For developers, that means classification, routing and scoring calls without paying for generated text. It is available now on the Liquid API at $0.042 per million input tokens. 

 TL;DR 

 Size: Parameters and context length not disclosed. Built on a larger open-weight backbone than d1. 

 Runs on: Hosted Liquid API only. No downloadable weights or quantized variants announced. 

 Performance: Leads all 8 categories in Liquid’s 112-evaluation suite, per Liquid. 

 Best: 65 on the Artificial Analysis Decision Index, ranked #1 (Liquid-reported). 

 Worst: No public per-benchmark breakdown or parameter count yet; claims are vendor-reported. 

 What is a decision model? 

 A decision model answers bounded questions with probabilities instead of free text. Liquid’s decision model docs describe 3 question types: 

 Noul: a yes/no question that returns a probability between 0 and 1. 

 Choice: one label from a set, with a probability per label. 

 Score: a probability-weighted position on an ordered rubric. 

 The docs recommend decision models for routing, moderation, guardrails, triage and LLM-as-judge replacement. They recommend a language model for summarization, chat and code generation. 

 How does d1-ultra work? 

 Each request carries a state (the context), optional images , and 1 or more typed questions . The model evaluates every question against the same input in 1 call. The d1 API reference shows responses with output_tokens always at 0. 

 Liquid AI team states that d1-ultra uses a larger open-weight backbone than d1 , along with heavy Liquid-specific customizations. Combined with Liquid’s decision training pipeline, the gains are largest on knowledge tasks. 

 Liquid AI team built d1-ultra for messy cases. Its examples include spotting a circuit board defect against a spec. Another is checking a damage claim against the customer’s photo. 

 &&& 

 How does d1-ultra perform on benchmarks? 

 Liquid AI compared d1-ultra against its earlier d1 and TypeSafe’s Jev 1.14 across 112 evaluations. According to Liquid AI’s announcement , d1-ultra outperforms Jev 1.14 across all tasks at the same price. 

 On the independent Artificial Analysis Decision Index , Liquid reports d1-ultra ranks #1 with a score of 65. The index averages 4 evaluations at 25% each: 

 AA-Omniscience-Decision: knowledge and hallucination 

 HLE-MultiChoice: reasoning 

 When2Call: tool calling 

 WildGuardTest: safety classification 

 For context, Artificial Analysis’s Oct 13 launch article listed Jev 1.13 first at 58. GLiDE and Microsoft-Decision-1 followed at 54 each. 

 Comparison: d1-ultra vs other decision models 

 Feature d1-ultra d1 Jev (TypeSafe) Microsoft-Decision-1 GLiDE (Fastino) Developer Liquid AI Liquid AI TypeSafe AI Microsoft Fastino Labs Parameters Not disclosed Not disclosed Not disclosed Not disclosed Not disclosed Input Text, images Text, images Text Not disclosed Not disclosed Weights API only API only Closed Not disclosed Not disclosed AA Decision Index 65 (Liquid-reported) Not disclosed 58 (v1.13, Oct 13) 54 (Oct 13) 54 (Oct 13) Price $0.042 / 1M input Not disclosed $0.042 / 1M input $31 / 1M tasks (AA) $119 / 1M tasks (AA) Output tokens billed No No No Not disclosed Not disclosed 

 How do you deploy d1-ultra, and what does it cost? 

 d1-ultra runs on the Liquid API through the /decisions/v1/systemone endpoint with "model": "d1-ultra" . Liquid says Vercel AI Gateway and OpenRouter support is coming soon. You can test it first in the d1 Playground . 

 Billing covers input tokens only. Per Liquid’s pricing notes , images cost 1.5 tokens per 32×32-pixel patch. A 1024×1024 image therefore costs 1,536 tokens. Each question is billed as its own prompt, including its text and all images. So 3 questions on 1 image bill that image 3 times. 

 The endpoint docs cap requests at 8 images and 10,000 image patches. The full JSON body must stay under 4.5 MB. 

 Key Takeaways 

 d1-ultra returns probabilities for text and image decisions with 0 output tokens. 

 Liquid reports a #1 score of 65 on the Artificial Analysis Decision Index. 

 It costs $0.042 per 1M input tokens, the same rate as TypeSafe’s Jev. 

 Liquid claims the lowest calibration error in its tests, useful for routing thresholds. 

 Size, backbone and weights remain undisclosed; access is API-only. 

 Check out the official blog post , the decision model docs , and try the d1 Playground . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Liquid AI Releases d1-ultra: A Multimodal Decision Model That Scores 65 on the AA Decision Index appeared first on MarkTechPost .
