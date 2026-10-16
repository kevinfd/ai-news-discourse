---
id: "1517795e445475ae"
title: "Meta ships Muse Spark Open, its answer to China’s best open-weight models"
url: "https://thenewstack.io/meta-muse-spark-open"
link: "https://thenewstack.io/meta-muse-spark-open"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T17:00:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Meta on Thursday launched Muse Spark Open, a new 816B open model (with 42B active parameters) that the company argues is the “most capable US open-weight model to date.” \n\n The new model is available through the APIs of Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter, and Together AI. And since it’s an open model, you can also download the weights from Amazon SageMaker AI, Google Cloud…"
tags: ["AI", "AI Models"]
orgs: ["Meta", "China", "Anthropic", "Google", "Microsoft", "Amazon", "Hugging Face", "Nvidia"]
topics: ["models & research", "agents & coding", "business & funding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 599
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meta ships Muse Spark Open, its answer to China’s best open-weight models

The New Stack · Frederic Lardinois · 2026-10-15

Meta ships Muse Spark Open, its answer to China’s best open-weight models
Meta on Thursday launched Muse Spark Open, a new 816B open model (with 42B active parameters) that the company argues is the “most capable US open-weight model to date.”
The new model is available through the APIs of Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter, and Together AI. And since it’s an open model, you can also download the weights from Amazon SageMaker AI, Google Cloud Model Garden, Hugging Face, and Microsoft’s Foundry Model Catalog.
Open Weights, semi-open license
Overall, Muse Spark Open, which features the industry-standard 1 million token window, looks to be an extremely capable model that, depending on the benchmark, is on par with or beats some of the best Chinese models. Like with some of the newer Chinese models, though, the weights may be open but the license doesn’t tell the same story.
Meta is launching the new model under the “Muse Model License.” This license, Meta says, has “limited commercial terms, which allow many developers to use the model for free.”
Specifically, this means any company that has more than $20 million in gross revenue during any consecutive twelve-month period must “notify Meta and enter into a separate written agreement with Meta before offering the Software or any Derivatives as part of that Model as a Service business.”
Any company using the model must also “prominently display ‘Built with Muse Spark Open’ in the user interface of each product or service” that uses the model or a derivative model that was created, trained, fine-tuned, or distilled from Muse Spark Open.
Overall, this looks a lot like the license that Moonshot uses for Kimi K3, for example.
Internal use and building the model into your own product are free, and the license’s usage policy bars military and critical infrastructure deployments, a carve-out Meta added for the U.S. government with Llama in 2024.
Unlike Anthropic’s new usage policy for Claude, though, you can abuse the model as much as you want.
Benchmarks
The company says it built the new model for “coding and agentic work, it excels at long-horizon tasks, complex software engineering, and multi-step reasoning.”
The two U.S. models Muse Spark Open competes with are essentially Thinking Machines’ Inkling and Nvidia’s Nemotron 3 Ultra. In Meta’s own benchmarks, its new model beats them across the board — often by 20 points or more.
The closer fight, however, is with Chinese open models that many developers already run today. Spark Open leads Kimi K3, GLM 5.3, and Qwen3.8 on the agentic and tool-use benchmarks, including JobBench and MCP-Atlas, and roughly ties them on SciCode.
Coding is where it trails.
On Terminal-Bench 2.1, Kimi K3 scores 85.0 and GLM 5.3 83.9 against Spark Open’s 76.4.
On DeepSWE 1.1, the spread is 68 to 60. That’s the same gap Meta acknowledged when it launched the closed version of Spark in April, and it doesn’t look like it’s made much progress since.
Muse Spark Open on the Mac you can’t afford
You’re unlikely to run an 816B model locally, but if you have two new Mac Studios with M5 Ultra chips and 512 GB, Meta says you could link them and use MLX to run the model on them.
The company did just that to run Muse Code, powered by Muse Spark, and ship updates to the Ice Cubes Mastodon client, for example. Apple doesn’t currently sell the 512 GB Mac Studio to mere mortals, but in a few weeks, you will be able to buy two of those machines for the price of a compact car.
