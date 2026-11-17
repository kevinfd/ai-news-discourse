---
id: "708e121d69e5aefb"
title: "AI Companies Develop Decision Models to Avoid Hallucinations"
url: "https://spectrum.ieee.org/typesafe-ai-hallucination-decision-models"
link: "https://spectrum.ieee.org/typesafe-ai-hallucination-decision-models"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T17:00:54Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Matthew S. Smith"]
language: "en"
summary: "On 15 September, a startup called TypeSafe AI released a new AI model called Jev . The company’s broad, disruptive claims about Jev that turned heads: The company claimed that Jev, which it calls a “System One model” is cheaper, faster, and can’t hallucinate. TypeSafe AI’s marketing is an obvious shot across the bow of other AI companies and their large language models (LLMs), which, despite…"
tags: ["Ai-models", "Artificial-intelligence", "Llms", "Decision-models"]
orgs: ["OpenAI", "Alibaba", "Microsoft", "Amazon", "Hugging Face"]
topics: ["models & research", "business & funding", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1533
paywalled: false
image: "https://spectrum.ieee.org/media-library/collage-of-the-question-what-color-is-the-sky-surrounded-by-a-shiny-sun-sticker-geometric-grid-and-a-confidence-meter-at-7.jpg?id=68692558&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# AI Companies Develop Decision Models to Avoid Hallucinations

IEEE Spectrum · Matthew S. Smith · 2026-11-16

On 15 September, a startup called TypeSafe AI released a new AI model called Jev. The company’s broad, disruptive claims about Jev that turned heads: The company claimed that Jev, which it calls a “System One model” is cheaper, faster, and can’t hallucinate.
TypeSafe AI’s marketing is an obvious shot across the bow of other AI companies and their large language models (LLMs), which, despite their capabilities in math and coding, are infamous for their cost and tendency to “hallucinate” factually incorrect replies. And the startup has certainly attracted both attention and investment. The company recently raised $870 million in funding at a valuation of $7.5 billion.
But the most impressive metric of Jev’s success is arguably the many imitators it’s already spawned. Cloudflare, Amazon, OpenAI, and Microsoft quickly released “decision models” that imitate Jev’s capabilities. Start-ups, academic researchers, and independent enthusiasts have released dozens more.
“I have to give Jev credit,” says Matt Mastracci, an independent developer who has trained and released several decision models including Djev, which Cloudflare cited as an inspiration for its own decision models. “It really brought decision models to the forefront. In six or seven weeks, we’ve seen dozens of models come out.”
Jev’s Latency and Compute Advantages
Most AI researchers would call Jev a decision model or decider model. TypeSafe AI’s branding of Jev as a System One model refers to a theory of cognition popularized by psychologist Daniel Kahneman in his book Thinking, Fast and Slow. In the book, Kahneman draws a line between fast, instinctive thought (System One) and slower, deliberate thought (System Two).
TypeSafe AI argues that modern LLMs offer the second, but are too slow to provide the first. The company claims that Jev can provide end-to-end response latency between 70 and 500 milliseconds. By comparison, LLMs typically require at least several seconds, to provide a response, and more complicated tasks (like coding software from scratch) can take several hours.
Independent testing backs up TypeSafe AI’s claims. A pre-print co-authored by Ramayya Krishnan, a professor of information systems at Carnegie Mellon University, along with several colleagues, found that Jev delivered a median latency of 150 milliseconds across several benchmarks designed to gauge decision accuracy, including RewardBench and JudgeBench. OpenAI’s most capable model at the time, GPT-6 Astra, delivered a median latency of 1.89 seconds.
A faster reply is often a cheaper reply, because it requires less compute time, and that’s reflected in TypeSafe AI’s pricing. The startup charges US $0.042 per million input tokens and output tokens are free. By contrast, for GPT-6 Astra, ChatGPT charges $10 per million input tokens and $50 per million output tokens. Even GPT-6 Luna, a variant of GPT-6 designed for fast, inexpensive inference, costs $0.10 per million input tokens and $0.50 per million output tokens.
Mastracci says that lower latency and costs open opportunities to tackle tasks LLMs currently can’t handle.“You can think of content moderation, such as moderating a fire hose of social media posts, or an extremely busy chat room.”
Michelle Chen, a group product manager at Cloudflare (which has released its own decision models, including Clef and Claric), is also bullish on what decision models can accomplish. “You can probably offload 80 percent of your typical LLM tasks to a System One model that is going to be so much faster and so much cheaper.”
TypeSafe AI has offered few details about how Jev achieves its speed, but Jev’s open-weights imitators provide more transparency.
For example, take Cloudflare’s Clef, an open-weights decision model which is free to download on Hugging Face. “With an LLM, when you’re generating an output token, it looks at all the previous tokens, and predicts the next output token,” explains Chen. This occurs in sequence, token after token, until an end token is reached. “Our decision models don’t do that. They just do a single forward pass, to generate one read of all the inputs, and then generate one output. That’s why it’s a lot faster.”
How Decision Models Generalize Tasks
Decision models based on an LLM, such as Clef (which is based on Alibaba’s Qwen LLM), still contain the neurons and transformer-based model architecture of an LLM. They still input and output tokens.
However, the portions of the model that turn these tokens into text have been changed to constrain the output. “Jev can only answer questions with a predefined, structured answer format,” says Zhongyu Wei, a professor at Fudan University who is also a co-author of a study that benchmarks decision models and introduces an open-weight alternative, SII-Decision. “We give it a question and options such as A, B and C, and it must choose from those options, returning probabilities alongside its choice.”
In one sense, decision models are a return to classifiers, a type of model that, as the name implies, learn to sort data into classes. They’re used in a wide range of tasks, including spam filters and face detection. “These kinds of models are not new,” says Chen. “It’s almost like a rebranding.”
But decision models offer a key upgrade over prior classifiers: generalization.
Mastracci explains that classifiers were traditionally created through domain-specific training. Decision models, though, retain the general intelligence of an LLM, and that makes them applicable to many situations. “You can pick it up off the shelf, you point it at your problem, and it works,” says Mastracci.
Cloudflare is putting this advantage into practice. Before decision models, teams looking to use a classifier model had to “get a lot of data, stand up a machine learning team, and fine-tune” a model for the task, Chen says. Decision models eliminate this requirement, so one decision model can be used in many domains. Examples include flagging spam pull requests in Cloudflare’s GitHub documentation repository, catching spam and phishing emails, spotting phishing domains, detecting prompt-injection attacks on LLMs, and reading emails about internet backbone outages to judge whether they’ll affect Cloudflare’s services.
Decision models are well suited for quick judgements on data like emails, messages, or documents.Source: TypeSafe AI
Do Decision Models Really Stop Hallucinations?
In programming, “type-safe” languages are designed so that operations mixing incompatible kinds of data—adding a number to a string, say—are rejected before the program runs rather than producing a bad result later. Decision models are similar in that they prevent the model from generating an unexpected reply. TypeSafe AI’s name makes the connection between type-safe programming and decision models part of the company’s marketing, and it builds on that to make a startling claim: Jev will never hallucinate.
This is, strictly speaking, true. LLMs hallucinate because they calculate probabilities for tokens repeatedly across a huge vocabulary of possibilities and output many tokens. This leaves room for less probable tokens to lead a response astray, or for the model to deliver tokens that are probable based on the model’s training, but not correct in the context of the reply. Decision models, by contrast, only calculate probabilities among the pre-determined possibilities, and the most probable is chosen. This eliminates hallucination.
However, Carnegie Mellon’s Krishnan cautions that “eliminating hallucinations in the output does not eliminate errors in decision-making.” He and his co-authors tested Jev by asking it to determine if answers to questions were correct. Jev performed well when the judgment could be easily reached by reading the prompt, but performance dropped off when the judgment required math or involved a logic puzzle.
Wei and his co-authors report similar results in their own research. They found the best decision models can slightly beat the accuracy of LLMs when asked questions about document understanding, and score close to LLMs when asked questions related to tool use (such as choosing the correct software tool to call to perform a user’s task). However, decision models fall behind when asked questions in domains that require topic expertise, including medicine, finance, and law.
“I think reasoning is a key factor,” says Wei. Reasoning allows an LLM to work though its response before it provides a final answer to the user. However, Wei adds that reasoning alone doesn’t explain the domain gaps in all cases, as some LLMs performed well even without reasoning. Wei says the methods used to train decision models can also be a factor, and used decision-specific training for SII-Decision.
Yet decision models and LLMs don’t have to be competitors. Krishnan and his colleagues also tested passing Jev’s low-confidence answers to GPT-6 for additional consideration. The combination of models slightly beat the accuracy of GPT-6 alone, and did so at 41 percent of the cost.
Wei thinks this “hybrid architecture” will become common. “The decision model can call an LLM to give a more detailed explanation. And an LLM can call a decision model for a quick judgment. I think that’s very flexible.”
- “Bullshit Index” Tracks AI Misinformation ›
- AI Hallucinates Novel Proteins ›
- Hallucinations Could Blunt ChatGPT’s Success ›
Matthew S. Smith is a freelance consumer technology journalist with 17 years of experience and the former Lead Reviews Editor at Digital Trends. An IEEE Spectrum Contributing Editor, he covers consumer tech with a focus on display innovations, artificial intelligence, and augmented reality. A vintage computing enthusiast, Matthew covers retro computers and computer games on his YouTube channel, Computer Gaming Yesterday.
