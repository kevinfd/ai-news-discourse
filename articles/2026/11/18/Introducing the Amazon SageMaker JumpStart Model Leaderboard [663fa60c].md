---
id: "663fa60cff593cd5"
title: "Introducing the Amazon SageMaker JumpStart Model Leaderboard"
url: "https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-sagemaker-jumpstart-model-leaderboard"
link: "https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-sagemaker-jumpstart-model-leaderboard"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-18T22:31:04Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Dan Ferguson"]
language: "en"
summary: "Amazon SageMaker JumpStart gives you hundreds of open-weight foundation models you can deploy quickly. That choice is powerful, but it also creates a real question: Which model should you start with? Comparing models usually means reading model cards one at a time and hunting for benchmark scores that different sources published under different conditions. Then you still must guess how each…"
tags: ["Amazon SageMaker", "Amazon SageMaker JumpStart", "Announcements", "Foundational (100)"]
orgs: ["Amazon", "Google", "Meta", "Alibaba", "IBM"]
topics: ["models & research", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 1718
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Introducing the Amazon SageMaker JumpStart Model Leaderboard

AWS Machine Learning Blog · Dan Ferguson · 2026-11-18

Artificial Intelligence
Introducing the Amazon SageMaker JumpStart Model Leaderboard
Amazon SageMaker JumpStart gives you hundreds of open-weight foundation models you can deploy quickly. That choice is powerful, but it also creates a real question: Which model should you start with? Comparing models usually means reading model cards one at a time and hunting for benchmark scores that different sources published under different conditions. Then you still must guess how each model will perform, and what it will cost, for your use case.
Today we are launching the Amazon SageMaker JumpStart Model Leaderboard, a new way to compare JumpStart models side by side on quality, speed, and cost, directly in Amazon SageMaker Studio. In this post, we explain what the leaderboard shows, define the key terms in plain language, and walk through how to go from a shortlist to a deployed model.
What is the JumpStart Model Leaderboard?
The leaderboard is a new view of the JumpStart base models page in SageMaker Studio, right next to the Categories and All models views. It uses the same search bar and filters you already know, and it opens on a leaderboard of large language models (LLMs). You see rankings immediately without answering setup questions first. For each model, it shows two kinds of information:
- Quality scores on three public benchmarks (BIG-Bench Hard, GPQA Diamond, and MMLU-Pro) that AWS runs itself, using the same evaluation setup for every model so the numbers are comparable.
- Performance and cost metrics that AWS measures by sending a standardized test workload to an endpoint using each JumpStart deployment configuration, so you see how fast a model responds and what it costs to run.
Because both kinds of numbers come from the same place and the same method, you can make a like-for-like comparison instead of stitching together data from different websites. At launch, the leaderboard covers 70+ models from providers including Meta, Google, Qwen, IBM, and Arcee, with more added over time.
The following screenshot shows the leaderboard in SageMaker Studio, with benchmark scores, performance metrics, and estimated cost for each model.
Key concepts
This section defines the terms the leaderboard uses: the quality benchmarks, the use case profiles and optimization goals that shape the performance numbers, and the performance metrics themselves.
Quality benchmarks
A benchmark is a standardized test: a fixed set of questions with known answers. Running every model through the same test gives you a score you can compare. At launch, the leaderboard reports three reasoning benchmarks for LLMs:
Higher is better for all three. The leaderboard shows each benchmark separately rather than blending them into one number. That keeps the results transparent: You can weigh the benchmarks that matter for your application and check each score against the public definition of the benchmark.
Use case profiles and optimization goals
Speed and cost depend on your workload and on how the model is deployed. Two menus above the leaderboard control which performance and cost numbers you see:
- Use case profile. Select the profile closest to your workload from the View benchmarks for your use case menu. The default is Max Context. The profile changes only the performance and cost metrics. Quality benchmark scores are the same for every profile.
- Optimization goal. For each profile, a model can have several deployment configurations, and the leaderboard shows metrics for one at a time. Choose which one with the Optimized for menu. The default is Balanced.
Each optimization goal picks a different configuration:
Performance metrics
A note on cost: Estimated cost reflects SageMaker instance cost only, based on the on-demand hourly rate for the configuration’s default instance type. It does not include data transfer, storage, inference component costs, or discounts such as Reserved Instances or AWS Savings Plans. Your actual bill will vary. Use the AWS Pricing Calculator for billing estimates.
How we benchmark
Published benchmark scores often come from different teams using different prompts, settings, and hardware, which makes them hard to compare. We took a different approach:
- One method for every model. AWS runs each benchmark with the same evaluation harness and settings across all models on the leaderboard.
- Measured on SageMaker. Performance and cost come from sending a standardized test workload to an endpoint deployed with each JumpStart deployment configuration, the same configurations you can launch.
For full details, including prompts, generation settings, and how configurations are measured, see JumpStart leaderboard methodology.
Walkthrough: Finding a model
The following steps show how to go from browsing to a deployed model. You need access to SageMaker Studio and permission to deploy JumpStart models.
Step 1: Open the leaderboard
In SageMaker Studio, open the Models page, then select the Leaderboard view. The leaderboard keeps the same search bar and filters as the other views, and it has its own URL. You can bookmark it or share a direct link with your team.
The following screenshot shows the Models page with the Leaderboard view selected.
Step 2: Narrow the list with filters
Use the same search and filters you already use elsewhere in JumpStart to keep only the models that fit your requirements. Common filters include license, provider, and input and output modality. Start with hard requirements, for example a license that allows commercial use, before you look at scores.
The following screenshot shows the leaderboard filtered by input modality, output modality, and license.
Step 3: Choose a use case profile and optimization goal
Above the leaderboard, select the profile closest to your workload from the View benchmarks for your use case menu (default: Max Context). Then choose a goal from the Optimized for menu (default: Balanced). For a chatbot your customers interact with, Latency optimized is a sensible start. For overnight document processing, Throughput optimized or Cost optimized may fit better. The performance and cost columns update, and quality scores stay the same.
The following screenshots show the View benchmarks for your use case and Optimized for menus above the leaderboard.
Step 4: Read the heatmap and customize columns
Each column has a blue heatmap, so the top-performing models stand out at a glance: the deeper the blue, the stronger the result in that column. Sort any benchmark column to rank models by the metric you care about most. Use the column settings (gear icon) to hide metrics you don’t need, and scroll horizontally to see more. The model name columns stay frozen as you scroll, and a fade at the edge shows when more columns are available.
The following screenshot shows the heatmap and the column settings menu.
Step 5: Deploy or customize the model
Choose a model to open it. From there, you have options to deploy the model or, for models that support serverless customization, to customize it. If you deploy, choose the same use case and optimization goal you compared on the leaderboard. Each metric applies to the configuration it was measured on, and a different configuration can change quality, latency, throughput, and cost.
The following screenshot shows a model page with the Deploy and Customize options.
Example: Picking a model for a chat assistant
Suppose you are building an internal help-desk assistant. Employees ask questions and expect fast, accurate answers that follow a set response format. You need a commercially licensed model and want to keep costs predictable.
After filtering by license and choosing a chat-like use case profile with Latency optimized, your shortlist might look like this:
Reading the table, Model A has the highest knowledge score but also the highest cost and the slowest first response. Model B scores almost as well, holds up on multi-step reasoning, and runs on a smaller, cheaper instance. For a help desk, where reasoning through a question and responding quickly matter more than the last few points of general knowledge, Model B is the better starting point. A bigger model is not always the better choice, and the leaderboard makes that trade-off visible in seconds.
From there, you would deploy Model B, test it with real questions from your help desk, and keep Model C in mind as a lower-cost option if quality holds up.
Tips and things to know
- Use the leaderboard to build a shortlist, not to make the final call. Benchmarks measure general ability. Always evaluate your top two or three models on your own data and prompts before going to production.
- Filter first, then rank. Requirements like license and input or output modality rule models in or out. Scores only help you order what is left.
- Compare models within a benchmark. Each benchmark has its own difficulty, so a score on one benchmark isn’t directly comparable with a score on another.
- Account for model type. Reasoning and non-reasoning models are evaluated with different generation parameters, and GPQA Diamond scores for reasoning models are averaged over 10 passes. Comparisons between the two types are approximate.
- Check the deployment configuration. Each metric applies to the configuration it was measured on. Compare models on the configuration you plan to deploy.
- Treat close scores as ties. Small differences can fall within normal run-to-run variation and don’t mean one model is meaningfully better. Look for clear gaps.
- Coverage is growing. Not every JumpStart model has benchmark scores yet, and launch benchmarks focus on LLMs. A model without a score is not a weak model. It simply has not been benchmarked yet.
What’s next
We’re continuing to expand the leaderboard. Areas we’re exploring include:
- Private hub support, so organizations that use curated JumpStart private hubs can see a leaderboard for their approved models.
- More task leaderboards beyond LLM text generation, such as object detection, text embeddings, and image understanding.
- More models and benchmarks as new models are added to JumpStart.
Conclusion
The SageMaker JumpStart Model Leaderboard brings quality, speed, and cost together in one place, measured consistently on SageMaker. Instead of comparing numbers from different sources, you can filter to the models that fit your requirements, compare them on the configuration you plan to run, and deploy with a few clicks.
To get started, open the Models page in SageMaker Studio and select the Leaderboard view. To learn more, see the following resources:
Open the leaderboard, shortlist two or three models for your workload, and deploy them to test with your own prompts before you choose one for production.
