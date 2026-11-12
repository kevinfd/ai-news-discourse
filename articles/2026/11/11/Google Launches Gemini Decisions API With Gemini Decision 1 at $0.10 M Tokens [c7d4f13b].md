---
id: "c7d4f13b5f0fc2a0"
title: "Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens"
url: "https://marktechpost.com/2026/11/11/google-gemini-decisions-api-gemini-decision-1"
link: "https://marktechpost.com/2026/11/11/google-gemini-decisions-api-gemini-decision-1"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-11T21:21:42Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Google has launched the Gemini Decisions API , powered by a new model, Gemini Decision 1 ( gemini-decision-1 ). The Gemini Decisions API does not generate text. It scores up to 1,000 typed questions against one shared input and returns calibrated probabilities. For developers, this targets the small branching calls inside agents: routing, policy checks, tool selection and grading. Google prices…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Decision Models", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "New Releases", "Staff", "Tech News"]
orgs: ["Google", "OpenAI", "Amazon", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches", "policy & regulation"]
content_source: "summary"
word_count: 982
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens

MarkTechPost · Michal Sutter · 2026-11-11

Google has launched the Gemini Decisions API , powered by a new model, Gemini Decision 1 ( gemini-decision-1 ). The Gemini Decisions API does not generate text. It scores up to 1,000 typed questions against one shared input and returns calibrated probabilities. For developers, this targets the small branching calls inside agents: routing, policy checks, tool selection and grading. Google prices it at $0.10 per 1M input tokens, with zero output tokens billed. 

 TL;DR 

 Size: Context is 262,144 tokens (256K) across shared input and all questions. 

 Runs on: Google-hosted API only (Gemini Developer API, v1beta). No open weights or self-hosting. 

 Performance: Leads 7 of 9 accuracy benchmarks in Google’s table, with the lowest calibration error. 

 Best: 92.2% on JevBench (public split). 

 Worst: 58.7% Macro-F1 on Amazon ESCI, its lowest score. It also trails Jev 1.14 on When2Call (79.9% vs 82.0%). 

 Bottom line: Best: multimodal, calibrated decisions in 150-250 ms. Worst: not the cheapest; Jev 1.14 costs $0.68 vs $0.88 on the shared suite. 

 What is the Gemini Decisions API? 

 Gemini Decision 1 is a specialized multimodal model from Google built for closed-set decisions. It reads text, images, video, audio and PDFs in one prefill pass. Output token usage is always 0. Your code branches directly on the returned numbers. 

 Each request has 3 parts: a model ID, a shared input , and a map of questions. The docs define 3 question types: 

 noul (yes/no): returns the probability of yes, bounded between 0.01 and 0.99. 

 choice : picks 1 of 2 to 255 options and returns normalized probabilities for every option. 

 score : rates input on 2 to 255 ordered rubric levels and returns a probability-weighted score. 

 Every answer carries a confidence value from 0 to 1. Google suggests routing low-confidence cases to a fallback or a human reviewer. Questions are scored in parallel and cannot see each other. 

 How does Gemini Decision 1 work? 

 Standard models decode an answer token by token, then your code parses it. Gemini Decision 1 instead scores your candidate options in one forward pass. Google reports median model compute of 50-100 ms and 150-250 ms end to end. That holds for inputs up to 16K tokens and stays nearly flat from 1 to 100 questions. 

 Billing follows the same design. The shared input is billed once per request, however many questions you ask. Each question adds only its own instruction and criteria tokens. There are no thinking-token, transcription or OCR charges. 

 &&

 Gemini Decision 1 benchmarks 

 Google tested Gemini Decision 1 against 3 rivals. They are TypeSafe Jev 1.14 , GPT-6 Luna on OpenAI Decisions and Gemini 3.5 Flash-Lite. All figures below are self-reported by Google. Refusals and safety blocks count as incorrect. 

 Benchmark Gemini Decision 1 TypeSafe Jev 1.14 GPT-6 Luna (OpenAI Decisions) Gemini 3.5 Flash-Lite JevBench (public split) 92.2% 90.0% 90.9% 86.6% Amazon ESCI (Macro-F1) 58.7% 56.7% 54.7% 47.2% New Yorker Caption (text-only) 79.7% 72.0% 68.4% 73.7% Mind2Web Multimodal 86.2% 86.8% 81.8% 78.0% PubMedQA 79.8% 78.2% 74.4% 77.6% Global-MMLU-Lite (non-English) 86.0% 85.0% 79.6% 78.8% When2Call 79.9% 82.0% 70.4% 60.9% MMAU (audio) 71.8% Not reported Not reported 67.7% Video-MME (no subtitles) 69.1% Not reported Not reported 63.3% Top-1 ECE (lower is better) 0.0250 0.0494 0.0721 0.2104 Total price, 7 shared evals $0.88 $0.68 $0.93 $4.14 

 Source: Google blog benchmark table . 

 The calibration result is the clearest gap. Gemini Decision 1’s error of 0.0250 is about half of Jev 1.14’s 0.0494. That matters when you set confidence thresholds for automation. On cost, Google says it is nearly 5x cheaper than Flash-Lite across the shared suite ($0.88 vs $4.14). 

 Gemini Decisions API vs OpenAI Decisions vs TypeSafe Jev 

 Feature Gemini Decision 1 GPT-6 Luna, OpenAI Decisions TypeSafe Jev 1.14 Parameters Not disclosed Not disclosed Not disclosed Context 262,144 tokens 1,050,000 ( model page ) 64K per request, 262K with opt-in header Questions per request 1 to 1,000 1 to 400 No fixed cap, bounded by context Input modalities Text, image, audio, video, PDF Text, image, JSON Text (docs) Input price per 1M tokens $0.10 $0.10 uncached $0.042 Output price $0 $0 $0 Prompt caching Not supported Supported, charged at Luna rates Not disclosed Latency claim 150-250 ms end to end About 10x faster than Responses API Not disclosed 

 How to deploy the Gemini Decisions API 

 The endpoint is live on the Gemini Developer API (v1beta) and needs google-genai SDK 3.2 or later. A no-cost tier is available for prototyping in Google AI Studio . Python, JavaScript and REST guides are in the documentation . 

 Ecosystem support is rolling out across OpenRouter , LangChain , Vercel AI SDK , LiteLLM , Pydantic AI , Pipecat , LiveKit and OpenCode . Support in Gemini on Google Cloud is listed as coming soon. 

 Google already uses it internally. Gemini Notebook routes queries to model tiers with it, serving everyday queries with up to 40% lower latency. Google Labs’ CC picks emoji reactions from more than 200 options. Stitch’s rapid canvas uses it to build playable wireframes in seconds. 

 Key Takeaways 

 Gemini Decision 1 scores up to 1,000 questions per call with zero output tokens. 

 It reads text, images, audio, video and PDFs natively in 1 pass. 

 Calibration error of 0.0250 is half that of TypeSafe Jev 1.14. 

 At $0.10/M input tokens, it still costs more than Jev’s $0.042/M. 

 No caching or Batch API yet, so repeated context is billed in full. 

 Check out the technical details , docs and model page . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens appeared first on MarkTechPost .
