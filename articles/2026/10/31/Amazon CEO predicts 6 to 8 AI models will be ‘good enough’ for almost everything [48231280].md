---
id: "4823128075b12bf7"
title: "Amazon CEO predicts 6 to 8 AI models will be ‘good enough’ for almost everything"
url: "https://thenewstack.io/jassy-bedrock-multimodel-prediction"
link: "https://thenewstack.io/jassy-bedrock-multimodel-prediction"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-31T14:30:00Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Amazon CEO Andy Jassy expects the frontier AI model race to produce several competitive models rather than a single winner, telling analysts on Amazon’s Q3 2026 earnings call Thursday that the challenge ahead will be choosing among models rather than committing to one. \n\n “6- 8 models that are about as good as each other, or at least good enough for 95%+ of the workloads.” \n\n During the call ,…"
tags: ["AI Models", "AI Strategy", "Cloud Services"]
orgs: ["Amazon", "OpenAI", "Anthropic", "Meta", "Microsoft", "Google", "xAI", "Mistral"]
topics: ["models & research", "agents & coding", "business & funding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 776
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Amazon CEO predicts 6 to 8 AI models will be ‘good enough’ for almost everything

The New Stack · Amanda Caswell · 2026-10-31

Amazon CEO predicts 6 to 8 AI models will be ‘good enough’ for almost everything
Amazon CEO Andy Jassy expects the frontier AI model race to produce several competitive models rather than a single winner, telling analysts on Amazon’s Q3 2026 earnings call Thursday that the challenge ahead will be choosing among models rather than committing to one.
“6- 8 models that are about as good as each other, or at least good enough for 95%+ of the workloads.”
During the call, Jassy responds to a question from Goldman Sachs analyst Eric Sheridan about the market opportunity for Amazon Bedrock, predicting that within two to three years there will be “6- 8 models that are about as good as each other, or at least good enough for 95%+ of the workloads.”
No single AI winner
Jassy has seen plenty of technology leaders lose their early advantage over the past 20 years. He pointed to databases and analytics as examples, along with TensorFlow, which once seemed likely to become the standard framework before PyTorch took the lead.
He expects something similar to happen with AI models. As Jassy put it, “there is not one tool to rule the world.” Some models will be better at reasoning or coding, while others will have an edge in visual tasks, speed, or cost per token. That leaves companies with plenty of reasons to use more than one. Jassy believes “most customers are going to use multiple models, and many will use multiple models in the same generative AI application.” For developers, that could mean choosing a model based on the task at hand rather than committing to one provider for everything.
“most customers are going to use multiple models, and many will use multiple models in the same generative AI application.”
One API, many models
That argument is effectively a description of how Bedrock is built, since the service reaches more than 100 foundation models from providers including Anthropic, OpenAI, Meta, Mistral, DeepSeek, Moonshot AI, and xAI through one API, letting a team call Claude, GPT, Llama, or a smaller specialized model without wiring up a separate pipeline for each.
Amazon recently brought OpenAI’s models onto the service alongside the closed models it already hosted, and Jassy says it has since added managed versions of open models such as Moonshot’s Kimi and Zhipu’s GLM, part of a hunger for Western open models he thinks Bedrock will keep feeding.
Switching models isn’t free
Bedrock’s Converse API gives developers a common way to work with models from different providers without rewriting their integrations each time. But switching isn’t always straightforward. Models have different context limits, tool capabilities, and supported features, so developers still need to test how their applications behave.
Things can get even more complicated when a team has built its workflow around a particular vendor’s agent harness. Jassy said customers want to “swap them back and forth as they leapfrog each other, as different constraints of their applications require them.”
Security also factors into that decision. According to AWS, Bedrock doesn’t give model providers access to customer prompts or responses, and that information isn’t used to train the underlying models. Jassy pointed to those protections as another reason enterprises choose the service.
Why Amazon wins anyway
The strategy beneath the prediction is that Amazon does not need to ship the best model as long as it owns the place developers go to choose one, a position it is hardly alone in chasing, since Google’s Vertex AI and Microsoft’s Azure AI Foundry pitch much the same multi-provider catalog and unified access.
A market where six or eight models keep trading the lead and teams constantly rotate between them is exactly what a neutral access layer monetizes, and Jassy makes little effort to disguise that Bedrock is the intended beneficiary, calling the opportunity “gigantic” and suggesting it could grow into a service “as large as EC2,” still one of AWS’s biggest businesses.
The early numbers lend that some weight, with Fortune 500 companies now spending close to seven times more on Bedrock year over year, token volume up nearly 17 times, and the service ranking, by Jassy’s account, as the fastest-growing multibillion-dollar product in AWS history.
It all arrives as AWS reaccelerates, with the segment growing 39.3% in the quarter to $46 billion and reaching a $184 billion annualized run rate, and Jassy notes that most Bedrock traffic already runs on Amazon’s own Trainium chips, which lets the company hold prices down while protecting its margins.
Jassy notes that most Bedrock traffic already runs on Amazon’s own Trainium chips, which lets the company hold prices down while protecting its margins.
Learning Path
