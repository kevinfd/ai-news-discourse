---
id: "162c0f3245fc1764"
title: "Your chatbot doesn't understand you. Here's what actually happens in the 3 seconds before it replies"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xlkec9/your_chatbot_doesnt_understand_you_heres_what"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xlkec9/your_chatbot_doesnt_understand_you_heres_what"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T01:33:58Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Ok_Translator_227"]
language: "en"
summary: "Crash course: how a real chatbot gets built from scratch I'll walk you through the whole journey, from the customer's first message to the reply, and everything that happens in between. 1. The model doesn't read words, it reads tokens Every sentence gets chopped into small pieces called tokens, and the model predicts the next piece, one at a time. There's also a limit on how much it can read at…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 407
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xlkec9/your_chatbot_doesnt_understand_you_heres_what/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Your chatbot doesn't understand you. Here's what actually happens in the 3 seconds before it replies

Reddit · Ok_Translator_227 · 2026-11-02

Crash course: how a real chatbot gets built from scratch I'll walk you through the whole journey, from the customer's first message to the reply, and everything that happens in between. 1. The model doesn't read words, it reads tokens Every sentence gets chopped into small pieces called tokens, and the model predicts the next piece, one at a time. There's also a limit on how much it can read at once, called the context window . And you pay for every token, so cost and speed are part of the design from day one. 2. The model remembers nothing Every time you send a message, the code sends the entire conversation history along with it. Memory is an illusion, and the developer is the one building it. When conversations get long, you have to summarize or trim, and that decision affects quality. 3. Your data: chunks and embeddings Your files (PDFs, pricing, policies) get split into chunks . Each chunk is turned into a list of numbers (an embedding ) that represents its meaning, then stored in a vector database . If the chunks are too big, answers get muddy. If they're too small, the meaning gets cut off. 4. Retrieval The customer's question also gets turned into numbers, and the system finds the 3 to 5 chunks closest in meaning. It sends those to the model along with the question: "Answer from this text only." That's RAG , and it's what cuts down on made-up answers. 5. The system prompt A fixed set of instructions goes out with every message: personality, language, boundaries, and what to do when it can't find an answer. How it's worded matters a lot. 6. Tools (function calling) The model can't actually do anything on its own. We describe tools to it (book an appointment, check an order), and it replies with "I want to call tool X with these values." The code is what actually runs it and hands the result back. 7. Safety and evaluation Before launch, you test hundreds of questions and measure accuracy. You also guard against people trying to trick the bot, and you keep monitoring its replies after it goes live. Bottom line: every one of these steps involves judgment calls, and one bad call in any of them can ruin the whole experience, even with a great model. Happy to go deeper on any step. Which one should I break down next? 👇
