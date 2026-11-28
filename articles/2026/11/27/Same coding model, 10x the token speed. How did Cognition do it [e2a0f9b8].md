---
id: "e2a0f9b8fc605065"
title: "Same coding model, 10x the token speed. How did Cognition do it?"
url: "https://thenewstack.io/cognition-swe21-coding-model"
link: "https://thenewstack.io/cognition-swe21-coding-model"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-27T16:05:59Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["Ritoban Mukherjee"]
language: "en"
summary: "This week, Cognition announced SWE-2.1 , its latest in-house coding model trained with reinforcement learning (RL) on Moonshot AI’s open-weight model, Kimi K3 . The company says SWE-2.1 shows large gains across a wide range of benchmarks over the preceding SWE-2 model, including Terminal-Bench 4.1 and FrontierCode 2.0.  \n\n The SWE-2.1 release includes an Ultrafast version that runs the same…"
tags: ["AI Models", "Developer tools", "Security"]
orgs: ["Anthropic", "OpenAI", "Google"]
topics: ["models & research", "agents & coding", "products & launches", "chips & infrastructure"]
content_source: "summary"
word_count: 808
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Same coding model, 10x the token speed. How did Cognition do it?

The New Stack · Ritoban Mukherjee · 2026-11-27

This week, Cognition announced SWE-2.1 , its latest in-house coding model trained with reinforcement learning (RL) on Moonshot AI’s open-weight model, Kimi K3 . The company says SWE-2.1 shows large gains across a wide range of benchmarks over the preceding SWE-2 model, including Terminal-Bench 4.1 and FrontierCode 2.0.  

 The SWE-2.1 release includes an Ultrafast version that runs the same model 10 times faster on Cerebras chips, boosting speed from 60 tokens per second to 600. Cognition also announced SWE-2.1 Cyber, a dedicated cybersecurity variant with looser safeguards that’s rolling out as the model for normal scans on Devin Security.  

 This is Cognition’s third model release in the last 11 weeks, right after SWE-2 on Sept. 10 and SWE-2 Flash on November 4. While SWE-2.1 still trails Claude Opus 5.5 on every benchmark, the results suggest a marked improvement in quality relative to frontier models. It’s also free to use in Devin Desktop and Devin CLI for all Devin Pro, Max, and Teams subscribers through December 8. 

 SWE-2.1 doubles its predecessor’s Terminal-Bench score 

 Since its last model release, Cognition says it has widened its RL training environment to include both short-term and long-horizon work, with a focus on science, performance engineering, and cybersecurity. It has also improved its post-training algorithms to control rollout length and reduce oscillations that used to knock training off balance, the company claims.  

 Together, these combined improvements have significantly raised SWE-2.1’s benchmark scores compared to SWE-2, Cognition says in its announcement. The company has published a table showing the model’s updated benchmark scores compared to previous models and frontier alternatives: 

 Benchmark SWE-2.1 SWE-2 Kimi K3.1 Claude Opus 5.5 Terminal-Bench 4.1 50.0 24.2 59.7 65.8 FrontierCode 2.0 41.3 24.1 19.9 47.3 ProgramBench 44.0 17.0 31.5 65.0 SWE Marathon v1.2 54.9 32.5 38.8 73.1 

 Table data supplied by Cognition   

 While it shows promise as a focus-tuned version of an open-weight model, SWE-2.1 still trails behind Claude Opus 5.5 on every benchmark score. An updated version of its own base model, Kimi K3.1, even outperformed it on Terminal-Bench.  

 Benchmark caveats and harness differences 

 Some skepticism is warranted, too, since these figures come from the company’s own testing and haven’t been reproduced independently. FrontierCode 2.0 is Cognition’s own benchmark, while the rest are independently developed. Also, SWE-2.1 and open-weight models like Kimi K3.1 ran on the Devin CLI harness during testing, while frontier models were tested on the developer’s preferred harness.  

 Cognition announces SWE-2.1 Ultrafast and a Cyber variant 

 Cognition’s speed chart puts the standard SWE-2.1 model at 60 tokens per second and its smaller sibling, SWE-2 Flash, at 200 tokens per second.  

 But through a partnership with AI chip maker Cerebras, the company can run the same model on faster hardware at 600 tokens per second. The company posted on LinkedIn and X , calling this variant SWE-2.1 Lightning, but the release announcement and Devin docs call it Ultrafast. 

 SWE-2.1 and SWE-2.1 Lightning are available today in Devin Cloud, Devin Desktop, and Devin CLI. Read more about our research behind SWE-2.1 and SWE-2.1 Cyber: https://t.co/uWQkORTbZ7 — Cognition (@cognition) November 24, 2026 

 Cognition also announced a dedicated Cyber variant. It’s a tweaked version of the SWE-2.1 model with more permissive safeguards against potentially harmful activity, aimed at defensive security work. SWE-2.1 Cyber is rolling out to power normal scans on Devin Security, while deep scans rely on frontier cyber models like Claude Mythos. 

 SWE-2.1 scores 80% on ExploitBench, compared with the SWE-2 model’s 36.1%. Compared against frontier cybersecurity models, that’s a significant leap, with Claude Opus 5.5 scoring 91% and only GPT-6.2 Sol managing a perfect 100% score. The model also succeeds on twice as many ExploitGym tasks as SWE-2, with a 27.3% total success rate compared to Claude Opus 5.5’s 34.5% and Gemini 4 Neon’s 47.9%.  

 How you can access SWE-2.1 right now 

 SWE-2.1 and SWE-2.1 Ultrafast are available right now on Devin Cloud, Devin Desktop, and Devin CLI. The company also said SWE-2.1 will remain free in Devin Desktop and CLI for Devin Pro, Max, and Teams subscribers through December 8 and will remain discounted, at $0.50 per million input tokens and $2.50 per million output tokens, until January 30, 2027, when list pricing of $2 and $10 kicks in.  

 “…you have two free weeks to thoroughly test whether SWE-2.1 can replace frontier coding LLMs for your everyday tickets.” 

 If you’re a Devin Pro, Max, or Teams subscriber, you have two free weeks to thoroughly test whether SWE-2.1 can replace frontier coding LLMs for your everyday tickets. SWE-2.1 Ultrafast is also available across Devin platforms as a paid option priced at $5 per million input tokens and $25 per million output tokens. Meanwhile, SWE-2.1 Cyber is currently limited to normal scans performed only through Devin Security. 
 The post Same coding model, 10x the token speed. How did Cognition do it? appeared first on The New Stack .
