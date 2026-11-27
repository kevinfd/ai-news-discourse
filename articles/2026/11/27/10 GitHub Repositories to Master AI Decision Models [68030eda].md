---
id: "68030edaedc9b7df"
title: "10 GitHub Repositories to Master AI Decision Models"
url: "https://kdnuggets.com/10-github-repositories-to-master-ai-decision-models"
link: "https://kdnuggets.com/10-github-repositories-to-master-ai-decision-models"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-27T13:00:00Z"
published_date: "2026-11-27"
collected_at: "2026-11-27T13:04:05Z"
authors: ["Abid Ali Awan"]
language: "en"
summary: "Explore 10 GitHub repositories to learn how to build, train, fine-tune, deploy, and evaluate AI decision models that make faster, more efficient decisions."
tags: []
orgs: ["Alibaba", "Hugging Face"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 1245
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/awan_10_github_repositories_master_ai_decision_models_1.png"
discussion_url: null
score: null
comments: null
community: null
---

# 10 GitHub Repositories to Master AI Decision Models

KDnuggets · Abid Ali Awan · 2026-11-27

10 GitHub Repositories to Master AI Decision Models
Explore 10 GitHub repositories to learn how to build, train, fine-tune, deploy, and evaluate AI decision models that make faster, more efficient decisions.
AI decision models are becoming increasingly popular following the release of Jev by TypeSafe AI. There's now a growing category of AI models designed to do one thing: make decisions instead of generating text.
These models are general-purpose. You provide a question, some context, and possible options, and the model returns a decision along with probabilities. For example, should you buy, hold, or sell a stock? Should a customer request be approved or rejected? Which AI model should handle a task?
Instead of training a separate classification model or using a large language model (LLM) to generate structured responses, you can integrate a lightweight decision model into your application. This can save time, reduce inference costs, and lower hardware requirements.
The exciting part is that these models are improving quickly, with more open-source tools and frameworks becoming available.
In this article, we will explore 10 GitHub repositories that will help you get started with AI decision models. These projects cover everything from using pretrained models and training or fine-tuning your own to converting existing LLMs into decision models, building applications, deploying models, and evaluating their performance.
For each repository, I will explain what it does and share a practical project idea you can try to get hands-on experience.
1. vLLM Semantic Router
vLLM Semantic Router is an open-source decision layer that helps route requests to different AI models based on their requirements.
It also supports the D3 family of decision models, which can evaluate predefined options and return probability distributions without generating long responses.
You can use it for model routing, classification, tool selection, and other tasks where making a quick decision is more important than generating text.
Project to try: Build an AI router that automatically decides whether a request needs a small, fast model or a more powerful reasoning model.
2. DecisionFormer
DecisionFormer is a framework for turning existing Hugging Face models into specialized decision models.
Instead of training a language model to generate a written answer, you can fine-tune it to evaluate choices and produce structured decisions.
The repository covers model training, inference, and serving, making it useful for understanding how decision models are developed.
Project to try: Fine-tune a small Qwen model to classify customer requests into Approve, Reject, or Manual Review, and compare its performance against a regular LLM.
3. StartLux-Decision
StartLux-Decision provides open decision models ranging from 0.8B to 27B parameters.
What's particularly interesting is its AutoThink approach. When the model is confident, it can make a decision directly. When it's uncertain, it can use additional reasoning before making the final decision.
This gives developers more control over the trade-off between speed and accuracy.
Project to try: Build a decision application that answers immediately when confidence is high and activates reasoning when confidence falls below a threshold.
4. JevTrainer
JevTrainer is designed to make training decision models easier.
It supports LoRA and full fine-tuning, multiple decision-head architectures, and configurable training pipelines.
You can also experiment with different types of questions, including multiple-choice, scoring, and yes/no decisions.
What makes it useful for learning is that you can compare different architectures using the same training data.
Project to try: Train three decision models using different readout heads and compare their accuracy, latency, and confidence calibration.
5. Laya
Laya is a lightweight decision engine designed for fast, non-autoregressive inference.
It supports multiple-choice, scoring, and yes/no questions across more than 100 languages.
The project also provides learning resources for fine-tuning decision models, making it a practical starting point for developers who want to experiment without building everything from scratch.
Project to try: Create a multilingual content moderation model that makes Allow, Review, or Block decisions.
6. Kev
Kev is a family of open decision models built on Qwen3.5 and Qwen3.8.
You can download the pretrained models, run them locally, or train your own using custom datasets.
The repository includes training scripts, benchmarking tools, and serving examples. It also uses uv, making the development environment relatively straightforward to set up.
Project to try: Train a decision model that selects which tool an AI agent should use based on the user's request.
7. JevAny
JevAny provides an end-to-end framework for training, evaluating, and deploying decision models.
It supports both language and multimodal models, so you can experiment with decisions involving text, images, and other inputs.
One useful feature is its starter training workflow. You can begin with a small Qwen model, train it using example datasets, and then deploy it through an API.
Project to try: Train your own decision model on support tickets and expose it through a local API.
8. AnyJev
AnyJev takes a different approach. Instead of requiring fine-tuning, it can turn existing open language models into Jev-style decision systems.
It works by extracting and processing the model's internal token probabilities to evaluate predefined choices.
This is particularly useful for understanding the difference between generating an answer and directly scoring possible answers.
Project to try: Convert an existing Qwen model into a Buy/Hold/Sell classifier without fine-tuning and compare its predictions with those from a standard prompted LLM.
9. Decision Index
Decision Index focuses on evaluating decision models rather than building them.
It provides a reproducible benchmark suite that developers can run locally or through Hugging Face Jobs.
This is important because a model returning 90% confidence doesn't automatically mean it will be correct 90% of the time.
Project to try: Benchmark D3, Kev, and another decision model using the same dataset. Compare accuracy, inference latency, and probability calibration.
10. Awesome Decision Models
Awesome Decision Models is a curated collection of decision models, frameworks, research papers, APIs, SDKs, and benchmarks.
Unlike the other repositories, it isn't a training framework. It's a learning resource that helps you discover what's happening in the decision-model ecosystem.
It's useful if you want to explore different model architectures, find new projects, or understand how these models compare.
Project to try: Choose three open-weight decision models, run them on the same tasks, and create your own comparison of accuracy, speed, and memory usage.
Final Thoughts
Decision models aren't exactly a new concept. We've been using machine learning models to make predictions and decisions for years. What's new is how this idea is being reintroduced using language models that can evaluate different options and return decisions with probabilities, without generating lengthy responses.
Since this approach is still relatively new, there aren't many dedicated learning resources or tutorials available on GitHub. Most of the repositories we've covered are experimental projects, frameworks, and tools rather than step-by-step learning materials.
However, I expect this space to grow quickly. As more developers experiment with decision models, we'll likely see better training methods, faster inference, more efficient architectures, and new ways to integrate them into AI applications.
For now, the best way to learn is to explore these repositories, run the models, experiment with your own datasets, and see where they perform better than traditional LLMs.
 
Abid Ali Awan (@1abidaliawan) is a certified data scientist professional who loves building machine learning models. Currently, he is focusing on content creation and writing technical blogs on machine learning and data science technologies. Abid holds a Master's degree in technology management and a bachelor's degree in telecommunication engineering. His vision is to build an AI product using a graph neural network for students struggling with mental illness.
