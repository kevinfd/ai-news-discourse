---
id: "f6a7124d5b0e6dab"
title: "Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash"
url: "https://marktechpost.com/2026/11/13/google-gemini-4-hydrogen"
link: "https://marktechpost.com/2026/11/13/google-gemini-4-hydrogen"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-13T09:45:48Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Google has released Gemini 4 Hydrogen , a fast model for coding and agentic work. Gemini 4 Hydrogen is a proprietary model from Google DeepMind built for everyday agent loops. It sits below the frontier models Gemini 4 Carbon and Gemini 4 Argon . Google calls it its “daily driver for agentic workflows.” \n\n TL;DR \n\n Size: 1,048,576-token unified window for input, thinking and output. \n\n Runs on:…"
tags: ["Agentic AI", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Python", "Tech News"]
orgs: ["Google", "Anthropic", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 987
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash

MarkTechPost · Michal Sutter · 2026-11-13

Google has released Gemini 4 Hydrogen , a fast model for coding and agentic work. Gemini 4 Hydrogen is a proprietary model from Google DeepMind built for everyday agent loops. It sits below the frontier models Gemini 4 Carbon and Gemini 4 Argon . Google calls it its “daily driver for agentic workflows.” 

 TL;DR 

 Size: 1,048,576-token unified window for input, thinking and output. 

 Runs on: Google-hosted API only. No weights, no quantized variants, no self-hosting. Serving hardware not disclosed. 

 Performance: Scores 51 on the Artificial Analysis Intelligence Index at high, above Argon’s 50. 

 Best: 57% on Terminal-Bench 4.1, versus 18.2% for Gemini 3.8 Flash. 

 Worst: Ranks only #5 on Agent Arena. Costs 2x Gemini 3.8 Flash’s current introductory price. 

 Bottom line: Best: frontier-class agent scores at $1.50/$7.50 per 1M tokens. Worst: closed, and synchronous output caps at 65,536 tokens. 

 What is Gemini 4 Hydrogen? 

 Hydrogen is a closed-weights model served through the Gemini API and Google products. The model card says it is adapted from Gemini 4 Carbon. Google does not disclose parameter count, architecture or training hardware. The knowledge cutoff is March 2026. 

 Input covers text, images, audio, video, PDFs, tables and charts, per the What’s New guide . Output is text. The 1M window is shared by input, thinking and output tokens. 

 How do the 4 thinking levels work? 

 Developers set thinking_level inside generation_config . Values are low , medium , high and a new xhigh . The default is high , not medium as on 3.8 Flash. A minimal setting now returns an error. The model card warns that higher levels use more tokens. 

 How does Hydrogen work with Carbon and Argon? 

 The key design idea is role-splitting across models. In Google Antigravity , an Orchestrator option switches models inside 1 task. Carbon explores, resolves ambiguity and plans. Hydrogen edits files, updates packages and runs tests. When Hydrogen hits friction, it hands control back to Carbon. 

 On Terminal-Bench 4.1, this pairing reached near-Carbon task success rates. It used 24% less quota and finished 19% faster than Carbon alone. The Antigravity SDK exposes the same split for custom multi-agent systems. 

 How does Gemini 4 Hydrogen perform on benchmarks? 

 All figures are self-reported by Google unless noted. 

 Artificial Analysis Intelligence Index : 51 at high, 54 at xhigh. Argon scores 50 on Index v5.0 . 

 Terminal-Bench 4.1 : 57%, versus 18.2% for 3.8 Flash. 

 HLE-Diamond: 58.8%, leading its class. 

 Vals Tax Agent Bench : 52.3%, ranked #1 overall. 

 Vals Legal Research Bench : 55.8%, tied for #1. 

 Multimodal Knowledge Agent : 53.4%. 

 Agents’ Last Exam v1.1 : 71.6%. 

 Agent Arena : ranked #5. 

 Speed is the headline claim. Hydrogen finishes tasks 2.5x faster than 3.8 Flash at the default high level. In partner tests, it ran 2x to 2.8x faster with 12% to 23% fewer tokens. 

 Google also reports more than 5x fewer fabricated claims than 3.8 Flash. It scored 96.7% on an internal agent honesty evaluation. It was 2.3x more resilient to indirect prompt injection on Gray Swan’s benchmark. 

&&

 How much does Gemini 4 Hydrogen cost? 

 The API price is $1.50 per 1M input tokens and $7.50 per 1M output tokens. Pricing is flat across the full window. Output pricing includes thinking tokens. Implicit caching cuts input to $0.075 per 1M for prompts of 4,096 tokens or more. Explicit caching is not supported. 

 The price context matters. Gemini 3.8 Flash costs $0.75/$3.75 until December 31, 2026. From January 1, 2027, it rises to $1.50/$7.50, matching Hydrogen. Argon costs $2/$10 until November 30, 2026, then $4/$20. 

 Where can developers use Gemini 4 Hydrogen? 

 The model ID is gemini-4-hydrogen . It is live in the Gemini API, Google AI Studio on all tiers, and Android Studio. It also ships in Gemini for business , the Gemini app, Google Search and Sheets. Antigravity access requires Google AI Pro or Ultra. Vertex AI is not mentioned in the launch posts. 

 Migration from 3.8 Flash needs a few changes. Remove temperature , top_p and top_k , since the server ignores them. Remove cached_content fields. Raise hardcoded max_output_tokens caps to 65,536. 

 Gemini 4 Hydrogen vs competitors 

 Feature Gemini 4 Hydrogen Gemini 3.8 Flash Gemini 4 Argon Claude Haiku 5.5 Release Nov 12, 2026 Sep 2, 2026 Oct 13, 2026 Oct 7, 2026 Parameters Not disclosed Not disclosed Not disclosed Not disclosed Context 1,048,576 unified Not stated in launch post 1M unified Not stated on launch page Weights Closed Closed Closed Closed Input $/1M $1.50 $0.75 (intro), $1.50 from Jan 1, 2027 $2 (intro), $4 from Dec 1, 2026 $0.10 (≤100K), $0.50 (>100K) Output $/1M $7.50 $3.75 (intro), $7.50 from Jan 1, 2027 $10 (intro), $20 from Dec 1, 2026 $0.50 (≤100K), $2.50 (>100K) AA Intelligence Index 51 (high), 54 (xhigh), per Google Not disclosed 50 (v5.0) 36 (v5.0.1) Terminal-Bench 57% (4.1) 18.2% (4.1, per Google) 57% (4.0, AA) 39.2% (4.0, max effort) Reasoning control 4 thinking levels Effort levels Not stated Effort settings 

 Terminal-Bench 4.0 and 4.1 are different versions, so cross-version scores are not directly comparable. 

 Key Takeaways 

 Hydrogen scores 51 on the AA Index, above Argon’s 50, per Google. 

 It hits 57% on Terminal-Bench 4.1, versus 18.2% for 3.8 Flash. 

 Pricing is $1.50/$7.50 per 1M tokens, flat across 1M context. 

 Default thinking is now high , with a new xhigh tier. 

 Pair it with Carbon in Antigravity for 24% lower quota use. 

 Check out the launch post , the model card , the developer post and the What’s New guide . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash appeared first on MarkTechPost .
