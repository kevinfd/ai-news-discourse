---
id: "ad5ba0913a114e18"
title: "JetBrains’ latest Mellum coding model uses 45% fewer tokens. It got there by not thinking."
url: "https://thenewstack.io/jetbrains-mellum2-1-instruct-coding-model"
link: "https://thenewstack.io/jetbrains-mellum2-1-instruct-coding-model"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-25T17:23:47Z"
published_date: "2026-11-25"
collected_at: "2026-11-26T13:04:05Z"
authors: ["Paul Sawers"]
language: "en"
summary: "JetBrains has launched a new variant of its open source coding model, one designed to tackle quick code edits, tool calls and all the smaller tasks that AI coding agents perform in the course of solving bigger problems. \n\n Mellum2.1 Instruct , as it’s called, is the latest installment in JetBrains’ in-house coding model lineup. The original Mellum, which debuted back in 2024 , was a proprietary…"
tags: ["AI", "AI Agents", "AI Models", "Open Source"]
orgs: ["Google", "Nvidia", "Hugging Face", "Alibaba"]
topics: ["models & research", "agents & coding", "products & launches", "business & funding"]
content_source: "summary"
word_count: 1011
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# JetBrains’ latest Mellum coding model uses 45% fewer tokens. It got there by not thinking.

The New Stack · Paul Sawers · 2026-11-25

JetBrains has launched a new variant of its open source coding model, one designed to tackle quick code edits, tool calls and all the smaller tasks that AI coding agents perform in the course of solving bigger problems. 

 Mellum2.1 Instruct , as it’s called, is the latest installment in JetBrains’ in-house coding model lineup. The original Mellum, which debuted back in 2024 , was a proprietary model built specifically for low-latency code completion in JetBrains’ IDEs. 

 Then in June this year, JetBrains introduced Mellum2 , a more versatile, 12-billion-parameter mixture-of-experts (MoE) model released under an Apache 2.0 license in both reasoning (Thinking) and non-reasoning (Instruct) variants. While Mellum2 was trained to handle individual coding tasks and tool calls, the next iteration would focus more specifically on how agents operate across entire code repositories. 

 That came last month with Mellum2.1 Thinking , which retained the same underlying architecture as Mellum2, but with an additional stage of reinforcement learning (RL) in which the model learned to navigate repositories, use shell and file tools, and make changes that would pass hidden tests. 

 With Mellum2.1 Instruct, JetBrains is now extending that same repository-level training to its non-reasoning model, which generates answers without an explicit chain-of-thought. As with its Thinking sibling, the company used Nvidia’s open source NeMo RL and NeMo Megatron-Bridge libraries to train the model using infrastructure capable of running 10,000 sandboxes concurrently. 

 The result is a leaner coding model fine-tuned for speed and token efficiency, capable of handling many of the same agentic tasks as its Thinking counterpart, with about half the token consumption, according to JetBrains’ testing. 

 The cost of overthinking 

 In a blog post published on Wednesday, Gleb Ingman , who works on the Mellum model team at JetBrains, notes that Mellum2.1 Instruct was built specifically for “sub-agents, tool loops, and chat.” 

 In real terms, this means that while Mellum2.1 Thinking is better suited to investigative tasks such as diagnosing why a unit test is failing, much of a coding agent’s day-to-day work involves more straightforward operations, such as modifying a few lines of code or retrieving information from a codebase. It’s these kinds of tasks that Mellum2.1 Instruct is geared toward, either operating independently or handling assignments delegated to it by a more powerful model. 

 “Every extra thinking token adds to the time you’re waiting.” 

 “In these cases, reasoning adds time and computing resources without adding quality,” Ingman writes. “This is especially true when the model runs locally — every extra thinking token adds to the time you’re waiting.” 

 Indeed, in the wake of the Thinking release, Ingman says that JetBrains fielded numerous requests from developers running models locally for a less verbose alternative capable of handling “moderately hard tasks.” 

 In its own benchmarking, JetBrains pits Mellum2.1 Instruct against the previous Mellum2 Instruct model , as well as Alibaba’s Qwen3.5 9B and Google’s Gemma 4 E4B , with reasoning disabled in both competing models. The six benchmarks cover agentic coding, multilingual code generation, tool use, instruction following and mathematical problem-solving. 

 Mellum2.1 Instruct doubled its predecessor’s score on SWE-bench Verified, which measures a model’s ability to resolve real-world software issues, jumping from 20.2% to 40.4%. It also outperformed all three models on the MultiPL-E code generation benchmark and broadly matched Qwen3.5 9B on ToolHop, which evaluates multi-step tool use. 

 Mellum2.1 Instruct: Comparative benchmark performance 

 Qwen3.5 9B, it’s worth noting, still came out ahead on SWE-bench Verified, scoring 49.8%. However, JetBrains points to Mellum’s MoE architecture, which activates just 2.5 billion of its 12 billion parameters for each token. According to the company’s earlier testing, this enables Mellum2.1 to generate tokens around 1.4 times as fast as Qwen3.5 9B for individual requests and 1.8 times as fast under load. 

 Perhaps more pertinent to this particular release, though, is how Mellum2.1 Instruct compares with its Thinking sibling in terms of token generation. In JetBrains’ agentic coding tests, the new model generated an average of 5,600 tokens per task, compared with 10,100 for Thinking — a reduction of 45%. 

 When tokens associated with tool calls were excluded, that reduction rose to 73%. 

 Mellum2.1 Instruct vs Thinking: Tokens per task 

 There are trade-offs, of course. While the two variants perform almost equally well on SWE-bench Verified, the gap widens on benchmarks that draw on competitive programming and mathematics competitions. 

 “On hard algorithmic and math problems, such as those in LiveCodeBench and AIME, thinking is crucial, and so Mellum2.1 Thinking remains the better choice,” Ingman writes. 

 “On hard algorithmic and math problems…. thinking is crucial, and so Mellum2.1 Thinking remains the better choice.” 

 Mellum2.1 Instruct is available on Hugging Face under an Apache 2.0 license, including a GGUF version for running the model locally on hardware with limited memory. JetBrains is also releasing a multi-token prediction (MTP) head alongside the model, which predicts multiple tokens ahead to accelerate generation by up to 1.8 times, according to the company. 

 A model for the multi-agent era 

 Mellum2.1 Instruct arrives as JetBrains increasingly focuses its core developer tools on agent orchestration. In September, the company introduced a revamped version of Air , its development environment for working with multiple coding agents. JetBrains has also been expanding the capabilities of Junie, the coding agent it launched last year , with a renewed emphasis on local execution . 

 As developers delegate more work to agents, and those agents in turn delegate tasks to other agents, there is clear scope for using different models according to the complexity of the job at hand. 

 As developers delegate more work to agents, and those agents in turn delegate tasks to other agents, there is clear scope for using different models according to the complexity of the job at hand. A more token-efficient model such as Mellum2.1 Instruct, therefore, could help keep inference costs and latency in check across such a system. 

 Whether JetBrains intends to deploy Mellum2.1 Instruct in its own agentic products, such as Air or Junie, remains unclear. 
 The post JetBrains’ latest Mellum coding model uses 45% fewer tokens. It got there by not thinking. appeared first on The New Stack .
