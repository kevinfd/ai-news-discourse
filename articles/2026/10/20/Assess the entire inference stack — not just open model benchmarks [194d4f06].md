---
id: "194d4f0692f792bf"
title: "Assess the entire inference stack — not just open model benchmarks"
url: "https://thenewstack.io/open-model-benchmarks-production"
link: "https://thenewstack.io/open-model-benchmarks-production"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T20:44:17Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Mark Chillingworth"]
language: "en"
summary: "Impressive benchmark results should make it easy for engineers to select the right open model for the outcome they are tasked with developing. However, that is not the case.  \n\n Benchmarks indicate an open model’s optimal performance, but in production, a model must work repeatedly. The challenge is that in production, other factors matter, such as the information provided to the model and its…"
tags: ["AI Engineering", "AI Infrastructure", "AI Models", "sponsor-nebius", "Sponsored", "sponsored-post"]
orgs: ["DeepSeek"]
topics: ["models & research", "business & funding", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 987
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Assess the entire inference stack — not just open model benchmarks

The New Stack · Mark Chillingworth · 2026-10-20

Assess the entire inference stack — not just open model benchmarks
Impressive benchmark results should make it easy for engineers to select the right open model for the outcome they are tasked with developing. However, that is not the case.
Benchmarks indicate an open model’s optimal performance, but in production, a model must work repeatedly. The challenge is that in production, other factors matter, such as the information provided to the model and its accuracy. So benchmarks can’t tell an engineer whether the AI they are developing will complete the task accurately, or even at all. This is especially important for long-horizon AI tasks.
Ryan Hanrui Wang, SVP of Applied AI at AI cloud provider Nebius, tells The New Stack it is important to measure an open model by the industry benchmarks in conjunction with internal benchmarks and harnesses to ensure you get the inference outcomes the organization requires, something he says the Amsterdam, Netherlands-based company always does in partnership with its clients.
Wang joined Nebius when it acquired Eigen AI, the inference-optimization startup he co-founded and led as CEO, in a roughly $643 million deal announced in May; Nebius sells inference through its Token Factory platform.
“Customers often have their own benchmarks, so we can use their agent workflow and its traces to see the level of success we can work with. We always work closely with them to define the benchmarks.”
Wang goes on to add: “The public benchmark may not cover the multi-domain tasks that an engineer wants inference to do in the actual production environment.” He says this can misalign agent tasks with the true cost of inference calls. “The workflow is not tested by the benchmark design. There needs to be in-context learning.”
Engineers and organizations should therefore not spend too much time selecting the open model; they should look at the entire inference stack. Model selection should depend on whether the engineer needs a lower-cost, flexible open-model stack or a frontier model for inference.
For those who need lower cost, Wang says Nebius evaluates open models such as Kimi and DeepSeek, as well as lighter “flash” models, to see whether they can meet inference accuracy needs and whether fine-tuning is required.
Those who want superior accuracy and quality usually narrow it down to two or three large open models and then fine-tune them to improve accuracy. Wang says open model selection is only the first step; after selection, they need to ensure long-context tasks and cached inputs deliver the expected outcome.
Inference and post-training
In post-training, Wang says the organization uses its data to improve accuracy and task fit, while the serving layer, quantization, batching, caching, and kernel optimization drive inference speed. In addition, engineers should develop the cache system for production traffic, ensuring the hit rate is maximized for the workload so repeated inputs hit the cache rather than being recomputed.
“The other important thing is throughput, the measure of how many tokens are generated in a certain time span, as they are a major trade-off against interactivity,” Wang adds. Engineers need to balance better utilization and cheaper tokens with acceptable interactivity– per-user speed.
Getting concurrency right ensures the organization uses the open model effectively; it is a fine balancing act for engineers. If compute isn’t fully utilized, token cost is high. But high utilization with increased concurrency can reduce end-user token-per-second speed.
Engineers also need to watch tail latency, not just averages. “P95 and P99 are important metrics for the per-user token speed and time to first token (TTFT); the time they need to wait needs to be below five seconds for some of our customers,” Wang says. A system can post a great average response time and still be unusable if one request in twenty stalls.
Modeling for accuracy
Engineers need to be careful when considering benchmark results and accuracy. Benchmarks may test reasoning on a mathematical problem, which isn’t very useful if the engineer is developing an AI agent for customer support, where high emotional intelligence (EQ) matters more. “So there is a misalignment between the different benchmarks and actual production,” Wang says.
On cost per successful task, Wang says engineers must remember that cheap tokens are useless if the model is inaccurate.
Engineers need to consider the end-to-end process the AI will perform. This lets engineers select the right-sized open model for the AI task. Wang gives the example of a specialized assistant agent where Nebius gathered 6,000 traces to refine a small model and improved accuracy by 11% while executing 22% fewer tool calls.
He raises this point because it counters the tendency to think bigger is better, but accuracy gains from increasing model size diminish. “There is typically a tipping point for this kind of task,” Wang says. For a task like customer support, he says, 10 billion parameters could be enough, while 100 billion or even a trillion parameters yields only minimal accuracy gains. “What we want to do is find the sweet spot.”
Engineers can use large models as a reference point, then tune the reasoning with their organizational data to find an open model with the right accuracy and size for the task.
“We typically do a sweep of several models, using the largest model as a reference to know where the sweet spot for model size is,” Wang says. “For a complicated task, we can dissect the complex task into smaller subtasks, working with the customer, which connects workflows and can then use smaller models.”
Wang describes this process as a division of labor, referencing the famous economist Adam Smith.
This approach shows the course of AI engineering maturity. Like every sector in technological and engineering history, the initial gold rush targets bigger-is-better. As the engineering matures, it focuses on outcomes and engineering excellence, and therefore on working with partners who understand how to achieve them.
Sometimes that is a bigger model; other times a small niche development is best.
