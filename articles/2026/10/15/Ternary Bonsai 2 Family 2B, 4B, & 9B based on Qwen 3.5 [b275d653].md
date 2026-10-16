---
id: "b275d653de962275"
title: "Ternary Bonsai 2 Family: 2B, 4B, & 9B based on Qwen 3.5"
url: "https://prismml.com/news/bonsai-2-family"
link: "https://prismml.com/news/bonsai-2-family"
source: "PrismML"
domain: "prismml.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T21:45:44Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["tcarambat"]
language: "en"
summary: "Going to try these out to see if they have the same looping behaviors that other Bonsai models have had. Still requires their fork of llama.cpp (branch prism) so dont expect it to work with vanilla llama.cpp. Edit: You can use with regular llama.cpp! Will see if there is some way to support this for AnythingLLM Mobile via LLama.rn fork since if anything this will hopefully beat out regular Qwen…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Google", "Nvidia", "Apple", "Samsung"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "fulltext"
word_count: 927
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6yk1f/ternary_bonsai_2_family_2b_4b_9b_based_on_qwen_35/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Ternary Bonsai 2 Family: 2B, 4B, & 9B based on Qwen 3.5

PrismML · tcarambat · 2026-10-15

Introducing Ternary Bonsai 2 2B, 4B, and 9B: Bringing Local Agents to Everyday Devices
Today, we’re expanding the Bonsai 2 family with three new ternary models based on Qwen3.5: Ternary Bonsai 2 2B, 4B, and 9B. Joining Bonsai 2 27B, they bring stronger capabilities to smaller deployment footprints and give developers more choices for building AI applications within local devices.
Building on first-generation Bonsai 1.7B, 4B, and 8B, the new models combine improved reasoning, visual understanding, and support for tool-driven workflows. The family now spans four sizes, allowing developers to balance task complexity, response time, and memory requirements.
The new models use a ternary representation that encodes weights using three values: {−1, 0, +1}. The 2B, 4B and 9B models have footprints of 0.43GB, 0.95GB and 2GB, respectively, more than 9× smaller than their full-precision counterparts.
On-device agents have to be smart enough to make useful decisions while working within limited memory and power budgets. This release advances both sides of that requirement: capability across reasoning, vision and tool use, and compact models that run locally on personal computers, phones and wearables.
Broad capabilities at small sizes
For this release, we focused on a few practical behaviors that make small models useful: avoiding repetitive loops, following instructions, calling tools on mobile devices, and controlling verbosity. Our ternary models, based on Qwen3.5 2B, 4B, and 9B, bring a much smaller memory footprint to phones and edge devices, where memory and compute are limited.
Those constraints shaped our development priorities. We focused on helping the models follow instructions, complete everyday tasks, and give useful answers without unnecessary output. For local assistant use, the 9B model uses roughly 40% fewer tokens on standard instruction-following and everyday math tasks. The goal is practical utility in a compact package. Solving the Riemann Hypothesis can wait.
For reference, we evaluated the new models across a suite of 19 benchmarks spanning the 6 skill sets of agentic tool use, math, instruction following, coding, knowledge and reasoning, and vision.
The table below shows the 19 benchmark scores for each of the Bonsai 2 models alongside its corresponding full-precision Qwen3.5 baseline. For convenience, we have also summarized the retention for each of the 6 skill sets.
Figure I: Benchmark results for Bonsai 2 and corresponding full-precision models.
Demo I: HybridAI for sensitive data redaction powered by Bonsai 2 9B on an M5 Macbook Pro
Throughput and energy efficiency
For local AI, model quality, inference speed and energy consumption jointly determine the experience a developer can deliver. Agents may alternate between interpreting information, selecting tools, and generating responses, thus making inference performance relevant at multiple steps in a workflow.
On hardware such as RTX 4090 and M5 Pro, Bonsai 2 models deliver up to 5x the throughput and 3x the energy efficiency of their corresponding full-precision counterparts. On M5 Max Pro, Bonsai 2 9B reaches up to 179 toks/s, while Bonsai 2 2B reaches up to 310 toks/s.
Their compact footprints are also ideal for mobile deployments. On an iPhone 18 Pro Max, Bonsai 2 9B delivers up to 34 toks/s tokens per second, while Bonsai 2 2B reaches up to 120 toks/s.
Figure II: Throughput in tokens/second for the 9B, 4B and 2B models
These improvements help make richer interactions practical on battery-powered devices. Faster inference shortens the time spent generating responses and tool calls; lower energy consumption supports more frequent use within the same power budget.
Making intelligence ubiquitous
At the Snapdragon Summit in September, we demonstrated a 1-bit Bonsai vision-language model running locally on AI smart glasses powered by the Snapdragon AR1 Gen 1 Platform. Built on first-generation Bonsai, the model showed how visual understanding and assistance could operate within the memory and power constraints of wearable hardware.
The new Bonsai 2 models build on that progress with stronger reasoning, visual understanding, and tool-calling capabilities. These capabilities provide a foundation for bringing basic agentic functionality to future applications on phones, smart glasses, and other wearables.
Developers can build assistants that interpret a user’s request, reason over text or visual context, and use application tools to carry out short sequences of actions. A workflow might extract information from a document and pass it to an application, or combine information from local files with a tool that helps the user complete a task.
The expanded Bonsai 2 family provides more choices across that range, from compact models for narrowly scoped tasks to larger models for more demanding workflows.
Platform Coverage
Ternary Bonsai 2 2B, 4B, and 9B run on NVIDIA GPUs via llama.cpp and on Apple devices (Mac, iPhone, iPad) via MLX. You can try out Bonsai 2 9B on Darkbloom today at console.darkbloom.dev. The first 100 users will also receive 250 million free tokens.
Model weights are available today under the Apache 2.0 License.
Full technical details of our compression, evaluation, and benchmarking processes are available in our whitepaper.
Work with Us
We work with teams to tailor Bonsai models to their applications, from post-training on domain-specific data to optimizing inference for target hardware. If you’re building AI products with tight memory, latency, or power requirements, we’d love to explore how Bonsai can help. Reach out at contact@prismml.com.
Join Us
PrismML emerged from a team of Caltech researchers and was founded with support from Khosla Ventures, Cerberus, and Google, with continuing support from Samsung. We've spent years tackling one of the field's hardest problems: compressing neural networks without sacrificing their reasoning ability.
If you want to help build the next generation of state-of-the-art AI, we'd love to hear from you. Check out our careers page.
