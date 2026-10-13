---
id: "7da69e84635cf3b8"
title: "Microsoft AI Releases Microsoft-Decision-1: A Qwen3.5-9B Decision-Scoring Model"
url: "https://marktechpost.com/2026/10/09/microsoft-ai-releases-microsoft-decision-1-a-qwen3-5-9b-decision-scoring-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-10T06:03:09Z"
published_date: "2026-10-10"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Microsoft has released Microsoft-Decision-1 , a decision model for routing, classification, verification and agent control. Microsoft-Decision-1 is a decision-scoring model that returns a calibrated probability for each fixed answer option instead of generated text. It is post-trained from Alibaba’s Qwen3.5-9B and available now in Microsoft Foundry and OpenRouter . \n\n TL;DR \n\n Size: Built on…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Decision Models", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Python"]
orgs: ["Microsoft", "OpenAI", "Alibaba"]
topics: ["models & research", "agents & coding", "business & funding", "products & launches"]
content_source: "summary"
word_count: 913
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Microsoft AI Releases Microsoft-Decision-1: A Qwen3.5-9B Decision-Scoring Model

MarkTechPost · Asif Razzaq · 2026-10-10

Microsoft has released Microsoft-Decision-1 , a decision model for routing, classification, verification and agent control. Microsoft-Decision-1 is a decision-scoring model that returns a calibrated probability for each fixed answer option instead of generated text. It is post-trained from Alibaba’s Qwen3.5-9B and available now in Microsoft Foundry and OpenRouter . 

 TL;DR 

 Size: Built on Qwen3.5-9B; exact parameter count not disclosed. 32,768-token context window. 

 Runs on: Hosted API only (Microsoft Foundry, OpenRouter via Azure). No open weights, no quantized variants, hardware not disclosed. 

 Performance: Highest average accuracy in Microsoft’s 36-benchmark comparison, at 85 ms p50 latency. 

 Best: 83.5% average accuracy across 36 benchmarks, ahead of Quyet-1.0-Large at 81.9%. 

 Worst: Calibration of 92.2, second to Quyet-1.0-Large at 93.1. Text-only, no explanations. 

 Bottom line: 
 
 Best thing: fast, cheap, calibrated decisions at $0.042 per million input tokens with free output. 
 
 Worst thing: closed weights, and every benchmark is vendor-run. 

 What is a decision model? 

 A decision model reads an input and scores a closed set of options. It does not write prose. Microsoft frames decision models as a new AI category , built for outputs software can act on immediately. 

 How does Microsoft-Decision-1 work? 

 Microsoft post-trained Qwen3.5-9B for single-pass decision scoring . Given a situation, a question and fixed options, it returns a probability per option in one call. It plans to rebase future versions on MAI and OpenAI models. 

 The Foundry model card lists the supported formats: 

 yes/no, multiple-choice, rating, classification and rubric questions 

 grading of AI responses and proposed agent actions 

 groundedness checks against supplied evidence 

 explicit abstention options such as “cannot tell” 

 Training used public datasets under Microsoft’s Open Data process plus synthetic data. Output is JSON. OpenRouter notes that weights update continually while the API shape stays fixed. 

 How fast and accurate is it? 

 Microsoft compared 9 systems across 36 benchmarks with 147,137 questions . Benchmarks were kept blind from training. Microsoft-Decision-1 led on average accuracy at 83.5%. 

 Its p50 latency was 85 ms, with p95 at 125 ms. That is 4.5 times quicker than Quyet-1.0-Large and 35 times quicker than GPT-6 Sol , which took 3.01 s. 

&&

 Microsoft also tested robustness. It perturbs each request 8 ways, including paraphrasing and option shuffling. The model flipped its decision on 1.3% of perturbations on average. Flips were zero when options were paraphrased, reversed or shuffled. 

 On safety, Microsoft ran 5,250 requests across 11 benchmarks. These covered harmful content, jailbreaks and prompt injection. Microsoft reports correct refusals with high retained utility, without publishing a score. 

 Internal results Microsoft reports 

 Xbox Research: sorted 10,000+ feedback items, 14 times faster and 200 times cheaper than GPT-6 Sol. 

 Copilot quality control: competitive with GPT5.6 Luna and 100 times faster. 

 Microsoft Discovery: 46 times more consistent than LLM scoring, at 3 times the speed. 

 How does it compare with other decision models? 

 Feature Microsoft-Decision-1 Quyet-1.0-Large H2O-Lightning-4B GPT-6 Luna Decisions Developer Microsoft Chinh Nguyen H2O.ai OpenAI Base model Qwen3.5-9B Gemma-4-31B-it (LoRA merged) Qwen3.5-4B Not disclosed Parameters Not disclosed 31.3B 4B Not disclosed Context / input 32,768 tokens 8,000-token prompt (6,000 state) 40,960 (vLLM serve setting) Not disclosed License Proprietary API Apache-2.0 Apache-2.0 Proprietary API Modality Text Text Text and images Text and images Hardware Hosted (Azure) 1x 80 GB GPU, bf16 32 GB GPU tested; 9.1 GB weights Hosted Accuracy (Microsoft, 36 benchmarks) 83.5% 81.9% 77.2% 79.4% Calibration (Microsoft) 92.2 93.1 91.8 89.9 Median latency in Microsoft chart 85 ms 380 ms 210 ms 300 ms Price $0.042/M input, output free Self-host Self-host $0.10/M input, output free 

 Accuracy, calibration and latency rows come from Microsoft’s chart . Competitor latencies there use the JevBench v1.6.1 adjusted median. 

 Is the latency comparison apples to apples? 

 Not fully. Microsoft measured its own model through Foundry. Competitor figures use JevBench’s adjusted median, not raw timings. 

 H2O.ai’s model card disputes this. It states that JevBench’s adjusted figure doubles measured time and adds 0.15 s. H2O says its model’s measured median is 29 ms, not 210 ms. Microsoft-Decision-1 does not appear on the JevBench board. On that board’s official composite, H2O-Lightning-4B ranks #1 at 72.5 . 

 How do developers deploy it? 

 Developers can call it from Microsoft Foundry as a generally available ‘Direct from Azure’ model. On OpenRouter , it runs on the Decisions API, not the chat endpoint. Chat completions SDKs will not work. 

 Pricing is $0.042 per million input tokens, with free output . OpenAI’s Luna decisions endpoint charges $0.10 per million input tokens . 

 What are the limitations? 

 The model card is explicit: 

 Not for text generation, open-ended Q&A, chat, translation or summarization. 

 Text-only. No images, audio or video. 

 No explanations or rationales in the output. 

 Not for sole automated decisions on credit, employment, housing, healthcare or legal rights. 

 Applications must define options, thresholds, escalation paths and human oversight. 

 Key Takeaways 

 Microsoft-Decision-1 scores fixed options with calibrated probabilities, not text. 

 Post-trained from Qwen3.5-9B, with a 32,768-token context window. 

 Leads Microsoft’s 36-benchmark comparison at 83.5% accuracy and 85 ms p50. 

 Costs $0.042 per million input tokens; output tokens are free. 

 Latency comparisons are disputed; independent JevBench results are pending. 

 Check out the official announcement , the Foundry model card and the OpenRouter listing . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Microsoft AI Releases Microsoft-Decision-1: A Qwen3.5-9B Decision-Scoring Model appeared first on MarkTechPost .
