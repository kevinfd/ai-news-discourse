---
id: "f7455ea846665c77"
title: "Mistral releases open weights for its 1 trillion-parameter Large 4 model"
url: "https://thenextweb.com/news/mistral-large-4-open-weights-release"
link: "https://thenextweb.com/news/mistral-large-4-open-weights-release"
source: "TNW | Artificial-intelligence"
domain: "thenextweb.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T14:40:56Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["joe4942"]
language: "en"
summary: "Mistral has released the weights of Mistral Large 4, the 1 trillion-parameter model it previewed three weeks ago, and the version now on Hugging Face is noticeably sharper.\nThe Paris-based company says three extra weeks of reinforcement learning, guided by customer feedback, have made ML4 the strongest open model for agentic coding and cyber defence.\nNicknamed “Le Chonk,” the model reads text…"
tags: ["r/singularity"]
orgs: ["Mistral", "China", "Nvidia", "Hugging Face", "DeepSeek"]
topics: ["models & research", "agents & coding", "business & funding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 568
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xilupe/mistral_releases_open_weights_for_its_1/"
score: null
comments: null
community: "r/singularity"
---

# Mistral releases open weights for its 1 trillion-parameter Large 4 model

TNW | Artificial-intelligence · joe4942 · 2026-10-29

Mistral has released the weights of Mistral Large 4, the 1 trillion-parameter model it previewed three weeks ago, and the version now on Hugging Face is noticeably sharper.
The Paris-based company says three extra weeks of reinforcement learning, guided by customer feedback, have made ML4 the strongest open model for agentic coding and cyber defence.
Nicknamed “Le Chonk,” the model reads text and images and produces text and code, activating 52 billion of its parameters for each task. Mistral is also releasing a quantised version, which runs on four Nvidia B200 or B300 GPUs.
The coding gains are the easiest to see. On Terminal-Bench 4.0, which tests agentic coding in a terminal, ML4 climbed from 28% at preview to 41%, just ahead of GLM-5.3 at 40%.
On Artificial Analysis’ Coding Agent Index, it rivals GLM-5.3 while using 47% fewer tokens per task on average, a saving that compounds when coding agents run for hours.
In cyber defence, ML4 scored 79% on CyberGym-E2E, a test of whether a model can find, reproduce, and patch real memory-safety bugs in open-source C and C++ projects, matching MiMo-V2.6-Pro and beating DeepSeek V4.1 Flash at 76%.
Early testers, whom Mistral describes only as governments and enterprises, wanted more control over how long the model thinks.
In response, the company added low and medium reasoning modes alongside high, and made the high mode 50% more efficient. Some customers already use ML4 for automated penetration testing, running specialised agents that probe their own applications for ways in and write up what they find.
Pierre Stock, Mistral’s VP of Science, framed the open release as a matter of continuity.
“AI is going to be like electricity,” he said, and no company should depend on someone who can cut off its access “from one day to another.”
Once the weights circulate online, he argued, access cannot be withdrawn, though rivals argue open models carry more risk.
He applied the same logic to the Chinese labs that dominate open models. Nothing guarantees they will keep publishing weights, he said, and their models offer less transparency and could be turned into attack vectors.
On the other side, Mistral built ML4 with a fraction of the resources available to both closed labs and its Chinese rivals, a claim that is hard to test given how little the Chinese labs disclose about their training costs. Indeed, no one else has reached this level with so few resources, as their competitors had larger funding and valuations.
Mistral also stresses efficiency. ML4 was trained on 3,800 Nvidia Grace Blackwell GPUs in Europe, and the reinforcement learning ran on its own compute in France, drawing about 10 megawatts.
“Other labs have raised hundreds of billions to develop equivalent capabilities; in three years, Mistral raised roughly $6 billion,” said Arthur Mensch, the company’s CEO.
Smaller, distilled versions will follow in the coming months, including one that runs on a laptop, though Mistral would not commit to dates. API pricing for ML4 has not yet been published, and Stock argued that per-token rates mislead when a model needs far fewer tokens per job.
ML4 is available on Hugging Face, through Mistral’s API, and to some Vibe users. The harder test comes next, as Stock wants Mistral not just to reach the frontier once but to “create the cadence of the frontier.”
Get the TNW newsletter
Get the most important tech news in your inbox each week.
