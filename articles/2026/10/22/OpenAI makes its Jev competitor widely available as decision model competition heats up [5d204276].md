---
id: "5d204276414bcfa2"
title: "OpenAI makes its Jev competitor widely available as decision model competition heats up"
url: "https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up"
link: "https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T19:00:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Tim Fernholz"]
language: "en"
summary: "OpenAI is launching its decision model to the world. Can it compete with the original Jev?"
tags: ["AI", "Exclusive"]
orgs: ["OpenAI"]
topics: ["models & research", "business & funding", "agents & coding"]
content_source: "fulltext"
word_count: 684
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI makes its Jev competitor widely available as decision model competition heats up

TechCrunch · Tim Fernholz · 2026-10-22

OpenAI made its Decisions API model widely available to users for the first time, entering the market for fast, cheap intelligence that recently made TypeSafe, a startup founded by a former researcher at the frontier lab, a $7.6 billion company.
TypeSafe’s Jev model created a category for deep learning models that act as super classifiers: Given a set of options, they can quickly make choices and offer a confidence rating in their decision. Software developers quickly found that these decision or System One models could replace LLMs in a variety of workflows, operating more quickly and a at dramatically lower cost.
Nikunj Handa, the product lead for OpenAI’s APIs, told TechCrunch that his colleagues saw Jev and said “wow, we we have like a million use cases for this.” Handa’s team sprinted to offer their own version: Rather than building a specifically calibrated decision model, the team took ChatGPT Luna and reconfigured it to speed up the inference and lower the cost.
“The big unlock with Decisions API has been the speed, shrinking things from one to three seconds to 100, 120, 180 milliseconds,” Handa said. “In the future, we may sort of like have specific training to make our models like even better in these ways. But right now, it’s just plain old Luna that gets the job done.”
Announced at the company’s developer day on September 29, the Decisions API became available to all customers on Thursday. OpenAI added new voice and visual modalities to the public version, and worked to ensure lower latency in regions around the world by targeting its inference resources geographically.
In initial trials with customers like Box, Datadog, Ramp, and Speak, engineers used the API to replace OpenAI’s LLMs with higher throughput. Andrew Hsu, the CTO at Speak, which builds AI language tutors, said the Decisions API allowed the company to cut the time between actions from 1.4 seconds to .13 seconds. OpenAI also used the product to improve their Dots voice assistant’s responsiveness.
Still, it’s not clear exactly what makes a good decision model, other than “it works for you” — optimization across intelligence, cost, calibration, and speed seems to differ by workload. TypeSafe CEO Diogo Almeida distrusts benchmarks and urges people to trial the models in their own work, but even TypeSafe released its own rankings last week alongside the release of its latest Jev model, which includes new features including support for images and smart-if statements.
Public benchmarks like the AIM System One Index and the Artificial Analysis Decision Index tend to favor D1 Ultra, a new decision model that Liquid released last week, and Base Lab’s Elephant-1. The latest Jev model remains competitive on both indices, in seventh and third, with OpenAI’s Decision Model falling eighth and fourteenth, respectively. However, TypeSafe’s offerings are, for now, the most widely-queried on OpenRouter.
The most fun Jev benchmark, however, is JevMan, a benchmark where decision models play PacMan; the latest Jev model tops that ranking. Felix Wunderlich, the chief growth officer at Opper AI, which built the benchmark, said the classic game “is an interesting test because of its nonstop stream of quick, high-stakes decisions. At every junction the model must decide where to go in a few hundred milliseconds.”
Where OpenAI’s arguably more capable model may have an advantage is in multi-modality—for image classification, “Luna is extremely powerful and has been showing better calibrations,” Handa told TechCrunch, adding that OpenAI customers want the Decisions API to be more flexible about using images as outputs as well.
Handa also saw further increases in speed enabling new use cases: “Can we get this to something like you know 60 milliseconds, and then you could imagine like an API like call like for every single frame in like a video?”
As these offerings get faster and cheaper, we can expect them to live up to Jev’s namesake, an economist who explained how using a resource more efficiently makes it more ubiquitous. Or, as Handa sees it, there will be an expanding “crazy set of use cases” that were hiding in plain sight until the decision models revealed them.
