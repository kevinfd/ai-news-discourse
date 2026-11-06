---
id: "eccd083829ad3e57"
title: "Together AI let coding agents rewrite its GPU code. Then it kept humans on the deploy button."
url: "https://thenewstack.io/together-compiler-gpu-optimization"
link: "https://thenewstack.io/together-compiler-gpu-optimization"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T18:56:57Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Together AI is putting AI coding agents to work on the GPU code that runs its inference infrastructure, automating performance tuning that used to take engineers days or weeks of manual work. \n\n The company unveiled Together Compiler on Wednesday, a system that generates, tests, and improves GPU kernels without an engineer directing each experiment, and Together AI says it can deliver gains…"
tags: ["AI Agents", "AI Infrastructure", "Hardware"]
orgs: ["Apple"]
topics: ["agents & coding", "chips & infrastructure", "models & research", "robotics & autonomy"]
content_source: "summary"
word_count: 635
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Together AI let coding agents rewrite its GPU code. Then it kept humans on the deploy button.

The New Stack · Amanda Caswell · 2026-11-05

Together AI is putting AI coding agents to work on the GPU code that runs its inference infrastructure, automating performance tuning that used to take engineers days or weeks of manual work. 

 The company unveiled Together Compiler on Wednesday, a system that generates, tests, and improves GPU kernels without an engineer directing each experiment, and Together AI says it can deliver gains overnight. The process runs without a person steering each step, but it doesn’t ship anything on its own. 

 Asked how much people remain in the loop, Together AI tells The New Stack , “The optimization loop is autonomous,” adding that “the final evaluations and deployment process are automatic but must be kicked off by a human, who reviews the changes before deploying to production.” 

 “The optimization loop is autonomous. The final evaluations and deployment process … must be kicked off by a human, who reviews the changes before deploying to production.” 

 Why GPU kernels fall behind 

 New AI models arrive so frequently that keeping inference infrastructure optimized has become a challenge. Each model has different requirements, and GPU code tuned for one workload may not perform nearly as well on another. 

 Together AI says 80% of OpenRouter traffic now comes from models released within the past three months. That leaves engineers constantly adjusting code to keep up; now Together Compiler automates much of that work. 

 Multiple coding agents run experiments simultaneously, writing and testing GPU kernels while sharing results to help guide the next round of improvements. 

 Faster testing, more experiments 

 The company has also found a way to speed up testing. Instead of restarting an inference engine every time an agent changes the code, Together Compiler keeps the engine running and loads new code. According to Together AI, this cuts initialization time from roughly 467 seconds to just nine seconds. 

 Instead of restarting an inference engine every time an agent changes the code, Together Compiler keeps the engine running and loads new code. 

 Reading the 252x claim 

 Together AI says its compiler can run 252 times as many optimization experiments as existing agent-based systems. The company tells The New Stack that it used Apple’s RSI Inference Bench harness as its baseline, comparing both systems on the same inference workload and hardware, with only the optimization approach changing. 

 The 252x figure refers to the number of experiments Together Compiler can run compared with Apple’s system, not how much faster the AI models themselves perform. 

 The company separately reports inference throughput improvements of up to 2.6x compared with published benchmark configurations. Those gains depend on the model and hardware, and the results haven’t been independently verified. 

 More experiments give Together Compiler more chances to find improvements. And because each test takes less time, the agents can do overnight what might otherwise take engineers weeks of manual tuning. 

 Better performance, same cost 

 Faster inference doesn’t necessarily mean lower prices. Asked whether the performance gains would translate into customer savings or primarily improve its own infrastructure efficiency, Together AI tells The New Stack , “Together Compiler improves Together AI’s infrastructure efficiency. For the same dollar cost, customers will get better performance.” 

 “For the same dollar cost, customers will get better performance.” 

 Developers may get more work out of the same GPUs, but that doesn’t always mean lower per-token prices . The company tells The New Stack that customers will get better performance for the same cost, rather than a price reduction. 

 Together AI says its compiler is already serving trillions of tokens daily. It’s another sign that coding agents are moving beyond writing application code and into GPU performance optimization, with engineers reviewing work that agents can now complete overnight. 
 The post Together AI let coding agents rewrite its GPU code. Then it kept humans on the deploy button. appeared first on The New Stack .
