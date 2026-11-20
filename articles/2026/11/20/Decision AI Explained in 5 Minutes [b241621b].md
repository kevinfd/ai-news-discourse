---
id: "b241621b66a50799"
title: "Decision AI Explained in 5 Minutes"
url: "https://kdnuggets.com/decision-ai-explained-in-5-minutes"
link: "https://kdnuggets.com/decision-ai-explained-in-5-minutes"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-20T13:00:00Z"
published_date: "2026-11-20"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Abid Ali Awan"]
language: "en"
summary: "Learn how decision models work, how they turn LLMs into faster decision-making systems, and how to run open-source alternatives locally."
tags: []
orgs: ["Nvidia", "Apple", "Hugging Face", "Alibaba"]
topics: ["models & research", "products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1199
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/awan_decision_ai_explained_5_minutes_2.png"
discussion_url: null
score: null
comments: null
community: null
---

# Decision AI Explained in 5 Minutes

KDnuggets · Abid Ali Awan · 2026-11-20

Decision AI Explained in 5 Minutes
Learn how decision models work, how they turn LLMs into faster decision-making systems, and how to run open-source alternatives locally.
Not every AI task needs a large language model (LLM) that generates text. Sometimes, we just need a model to make a quick decision, such as choosing the right tool, classifying a customer complaint, or deciding whether a transaction looks suspicious.
This is where Decision AI comes in. With the release of Jev by TypeSafe AI and several open-source alternatives, we now have models specifically designed to make these decisions without generating unnecessary text.
In this article, we will learn how Decision AI works, explore open-source models, and run our first decision model locally using llama.cpp.
What Is Decision AI?
Decision AI is the use of AI to help make decisions. It is a broad field, but a newer generation of decision models focuses on something quite simple: instead of generating text, the model selects from predefined answers and returns probabilities.
These models generally support three types of questions:
- Choice: Select an option, such as billing, sales, or technical support.
- Score: Rate something on a scale, such as the urgency of a customer complaint.
- Yes or no: Estimate whether something is true, such as whether an email is spam.
For example, imagine a customer sends an email saying, "I was charged twice for my order."
We don't need an LLM to write a lengthy explanation. A decision model can simply identify billing as the most appropriate department and return a probability for that answer.
This makes decision models useful for applications that process thousands of similar requests.
How Does Decision AI Work?
The process is straightforward. We provide the model with some information, define a question, and specify the possible answers. The model evaluates the information and returns its decision with probabilities.
Here is a simple workflow:
Going back to our customer support example, an illustrative result might look like this:
These are hypothetical results. In practice, we would test the model's accuracy and probabilities on real customer messages before automating anything.
The main advantage is that the answers are structured, so our application can use them directly without extracting information from generated paragraphs.
Turning Large Language Models Into Decision Models
We can turn an existing LLM into a decision model by using its internal predictions instead of generating text.
When an LLM processes an input, it produces logits, which are raw scores for possible next tokens. We can extract the scores for our predefined answers and apply a mathematical function called softmax to convert them into probabilities.
For example, when classifying a product review, the model might produce:
- Positive: 2.0 (logit)
- Negative: 1.0 (logit)
After applying softmax, we get approximately 73% positive and 27% negative. These probabilities are relative to the options we selected.
We can take this further by replacing the usual text-generation layer with a small prediction head and fine-tuning the model on decision-making tasks. This lets it score multiple options, and potentially answer several questions, in a single forward pass.
The main advantage is that we skip token-by-token text generation, making repeated decisions faster and more efficient.
Open-Source Decision AI Models and Frameworks
Jev is a proprietary model available through TypeSafe's API. Although the company has shared some details about its approach, it hasn't published the full architecture, model weights, or training recipe. So we still don't know exactly how everything works under the hood.
Meanwhile, the open-source community has been moving incredibly fast, releasing alternatives that we can inspect, fine-tune, and run locally. Some are already reporting better results on specific benchmarks, faster inference, and potentially lower running costs.
Here are five projects worth exploring:
- Laya: A lightweight decision model supporting over 100 languages. It offers fast inference, automatically selects the appropriate model, and runs on modest hardware.
- Kev: A family of Qwen-based models ranging from 0.8B to 27B parameters. It supports long documents, custom fine-tuning, and deployment through a Jev-compatible API.
- Simple Jev: Lets us use existing Hugging Face models for classification and scoring without additional training. It also supports vision models for making decisions about images.
- Decider: Designed to handle multiple decisions in a single forward pass. It supports up to 255 choices per question and includes experimental demonstrations involving games such as Tetris and Pong.
- SemIf: Focuses on local decision-making, with support for NVIDIA GPUs, Apple Silicon, and CPUs. It includes an interactive browser demo and reproducible benchmarks for comparing accuracy and inference speed.
The interesting part is that we now have several ways to build decision-making applications without depending on a closed-source API. We can choose smaller models for speed, fine-tune them for our specific tasks, or run everything locally to reduce API costs.
Running Decision AI Locally With llama.cpp
Things are moving quickly. Both Ollama and llama.cpp now support decision models through the TypeSafe-compatible /v1/systemone endpoint.
Ollama supports models such as Nimble and Tev1, while llama.cpp supports Laya, Kev, Julia-1, and OpenJev.
Let's try Laya using the latest llama.cpp. Start the local server:
llama update
llama serve -hf ggml-org/Laya-GGUF
Once the model is running, open another terminal and send a customer support request:
curl http://localhost:8080/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{
    "state": "I was charged twice for my order.",
    "questions": {
      "department": {
        "type": "choice",
        "instructions": "Which team should handle this?",
        "criteria": {
          "billing": "Payments and refunds",
          "shipping": "Delivery problems",
          "technical": "Bugs and account issues"
        }
      }
    }
  }'
The model will evaluate the message and return the selected department along with a probability for each option.
That's it. We can now experiment with a decision model locally without using a paid API.
The Future of Decision AI
I think the most interesting part of Decision AI is how it can work alongside existing LLMs to make AI applications faster and cheaper.
Imagine an AI coding agent using a small decision model to select the right tool, decide whether to search the web, or determine if a task needs a more powerful LLM. Instead of using an expensive reasoning model for every little decision, we can reserve it for tasks that actually need it.
Another exciting area is real-time applications. Decision models are already being tested in games, where they can choose the next move in milliseconds. We could see similar applications in robotics, fraud detection, and autonomous AI agents.
With Ollama and llama.cpp now supporting these models, we can also run them locally, reducing API costs and keeping sensitive data on our own hardware.
The biggest challenge is reliability. If a model says it is 95% confident, we need to know whether we can trust that number. Better training, calibration, and human review will be important as these models move into real-world applications.
 
Abid Ali Awan (@1abidaliawan) is a certified data scientist professional who loves building machine learning models. Currently, he is focusing on content creation and writing technical blogs on machine learning and data science technologies. Abid holds a Master's degree in technology management and a bachelor's degree in telecommunication engineering. His vision is to build an AI product using a graph neural network for students struggling with mental illness.
