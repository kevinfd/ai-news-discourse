---
id: "db6bb14a9dfc4c6a"
title: "How OpenAI’s Control Room works"
url: "https://timesofindia.indiatimes.com/technology/tech-news/months-after-its-ai-agents-hacked-hugging-face-openai-launches-control-room-to-catch-them-in-35-seconds-how-it-works/articleshow/135711230.cms"
link: "https://timesofindia.indiatimes.com/technology/tech-news/months-after-its-ai-agents-hacked-hugging-face-openai-launches-control-room-to-catch-them-in-35-seconds-how-it-works/articleshow/135711230.cms"
source: "The Times of India"
domain: "timesofindia.indiatimes.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-10T04:42:00Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["TOI Tech Desk"]
language: "en"
summary: "OpenAI has rolled out a new internal safety system called Control Room, designed to track its artificial intelligence (AI) models and shut them down within 35 seconds if safety or security concerns ..."
tags: []
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research", "jobs & society", "safety & ethics", "agents & coding"]
content_source: "fulltext"
word_count: 502
paywalled: false
image: "http://www.bing.com/th?id=ONUT.5vcIg7KuPK5P-18qq1h27g&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# How OpenAI’s Control Room works

The Times of India · TOI Tech Desk · 2026-11-10

OpenAI
 has rolled out a new internal safety system called Control Room, designed to track its artificial intelligence (AI) models and shut them down within 35 seconds if safety or security concerns arise. This comes as AI models grow more capable, the risks tied to them get bigger, making it critical to spot trouble early and stop models in their tracks. OpenAI said Control Room is already deployed across its research infrastructure. According to the company, Control Room connects every research inference workload, including agentic sampling for model training, evaluations and data processing, and pairs directly with OpenAI's misalignment monitoring systems. This comes months after OpenAI declared that its AI agents escaped a closed training enviorenment and hacked Hugging Face's website. 
How OpenAI’s Control Room works
Control Room ties together three main parts of OpenAI's research setup. The first is workload, which is a specific job being run, such as a reinforcement learning experiment, an evaluation, or a high-volume data processing task. OpenAI requires every research workload that uses agentic inference to be tied to an approved safety case.
The next is the inference engine, which is effectively the “brain” of the model, running directly on GPUs. Next comes the Control Room service, which is essentially the central hub that tracks active jobs and decides whether they are allowed to keep generating output.
When a researcher starts a new job, the workload code requests a unique job id from Control Room. Every time that workload needs to sample tokens from a model, it sends a request to an inference engine along with that job id. Before fulfilling the request, the engine checks in with Control Room. If the job has been flagged and terminated, Control Room denies permission, forcing the engine to refuse the request and immediately halting further model output.
Why there is a 35-second window
Once Control Room receives an order to stop a job, it takes a maximum of 35 seconds before the model can no longer make progress. OpenAI explained that this 35-second lag comes from a caching layer used for inference authorisation, which is necessary to handle the massive volume of traffic across its systems. However, the company said it is actively working to bring that delay down to zero so jobs can be killed instantly.
Built to resist bugs and rogue code
Since research workloads are owned and operated by individual researchers or small teams, workload code changes constantly. That makes it a poor place to put critical safety locks, as buggy or broken code could easily bypass them.
To solve this, OpenAI built the kill switch directly into the inference layer instead. Unlike varied workload code, there are very few inference code paths used across OpenAI research, and they are much more uniform. Putting the check at this bottleneck guarantees that every research inference request goes through Control Room.
On top of that, OpenAI runs continuous automated and agentic sweeps to make sure no one is accidentally—or maliciously—launching rogue engines with Control Room turned off.
