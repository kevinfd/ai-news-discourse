---
id: "1dace7d65df23dc3"
title: "Why DeepSeek V4's Performance Is So High"
url: "https://note.com/bright_hosta5/n/n195cf9a3f220?hl=en"
link: "https://note.com/bright_hosta5/n/n195cf9a3f220?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-07T04:03:00Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["パンダ船長×レイカAi"]
language: "en"
summary: "When I first called DeepSeek V4 Flash via API, I was surprised by the speed of the response. It completes 10 questions in 2.9 seconds. Compared to GPT-4o, the price is less than one-tenth. Yet, it ..."
tags: []
orgs: ["DeepSeek", "OpenAI", "Anthropic"]
topics: ["models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1505
paywalled: false
image: "http://www.bing.com/th?id=ONUT.uGflOospajsWvl1h9aO2Jg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Why DeepSeek V4's Performance Is So High

note · パンダ船長×レイカAi · 2026-11-07

Why DeepSeek V4's Performance Is So High
When I first called DeepSeek V4 Flash via API, I was surprised by the speed of the response. It completes 10 questions in 2.9 seconds. Compared to GPT-4o, the price is less than one-tenth. Yet, it follows Japanese instructions, outputs JSON (a standard data format), applies rules, and does not cut corners.
Describing this speed as "fast" is not accurate. To be precise, it is "long." It can produce long reasoning in a short time, at a low cost, and with stability. This is the true nature of DeepSeek V4's performance.
What is "long reasoning"? It means accumulating multi-stage thinking within the model before arriving at a single answer. When it receives a question, the model does not provide an answer immediately. First, it organizes information, then it constructs logic, and finally, it verifies the answer. This three-stage process of "organize → construct → verify" is long reasoning.
Many LLMs have a weak ability to execute this long reasoning. They can provide short answers, but when it comes to complex problems, they get lost along the way. DeepSeek V4 can execute long reasoning stably. That is why I describe its performance as "long."
1. Misconceptions about LLM performance
There are three misconceptions about LLM performance in the world.
The first is "how much knowledge has been provided." This is the idea that if you feed documents into RAG (Retrieval-Augmented Generation), it will become smarter. However, RAG only supplements knowledge; it does not change the quality of reasoning. Knowledge is fuel, not the engine. Even if you load it with fuel, it cannot run if the engine is weak.
The second is "how much it has been educated." This is the idea that if the amount of supervised fine-tuning is high, it is smarter. However, education only refines behavior; it does not change the depth of reasoning. Education is etiquette, not intelligence. It is the same as saying that a polite person is not necessarily a smart one.
The third is "scale is justice." This is the idea that if the number of parameters is large, it is smarter. However, scale only increases memory capacity; it does not change the efficiency of reasoning. Scale is a warehouse, not a factory. Even if the warehouse is large, production will not increase if the manufacturing line is slow.
If you believe these three things, you cannot explain the performance of DeepSeek V4. V4 Flash delivers performance comparable to GPT-4o and Claude Opus at less than one-tenth the cost. Why? The answer is not in knowledge, education, or scale. The answer lies in the mechanism of reasoning.
2. Logic is not a single path
I will state my own theory. Logic is not a single path. Logic is a challenge to connect the causality of all phenomena.
Many people think of logic as a linear chain of "if A then B, if B then C, therefore if A then C." This is the sense of proof in high school mathematics. However, real-world problems are not a single path. A causes B, B causes C, and C reinforces A. Causality circulates, branches, and merges.
LLM reasoning is the same. When it receives a question, the model does not "linearly derive an answer," but rather "casts a web of causality and explores within it."
What does "casting a web of causality" specifically mean? Let me give an example. When it receives the question "Fix the bug in this code," the model executes the following:
- First, read the code and organize the relationships between variables (cast a web of causality)
- Next, track which line affects which line (explore within the web)
- Finally, derive the cause of the bug and how to fix it (provide an answer)
This three-stage process of "organize → track → derive" is long reasoning. DeepSeek V4 is superior because it can execute these three stages stably.
3. Papers on reasoning costs
Research into lowering inference costs has been active in recent years. I will list some representative examples.
Self-Consistency is a method where the same question is inferred multiple times, and the answer is decided by majority vote. Accuracy increases, but the cost becomes N times higher. If you infer 10 times, the cost is 10 times higher.
Tree of Thoughts is a method where inference is explored in a tree structure (the overall picture of branching options), and each node (branching point) is evaluated. It is strong for complex problems, but the cost increases exponentially. As the number of branches to explore increases, the cost balloons.
Chain of Thought is a method that explicitly generates the process of inference. Accuracy increases, but the number of output tokens (the smallest unit of characters generated by the model) increases. Since the thought process is output as text, token consumption increases.
These are all research directions aimed at 'increasing cost to improve accuracy.' What DeepSeek V4 did was the opposite. It improves accuracy without increasing cost. How did it do that?
4. Differences in how each model performs inference
The way inference is performed differs for each model.
GPT-4o performs inference broadly and shallowly. Because its web of knowledge is wide, it can answer many questions. However, in situations where deep inference is required, it only skims the surface. It has breadth but lacks depth. This is the impression I felt from actually using it.
Claude Opus performs inference deeply and narrowly. It focuses on a single problem and stacks multi-stage inferences. However, in situations where broad knowledge is required, its field of view becomes narrow. It has depth but lacks breadth. This is also based on my experience using it.
DeepSeek V4 is in between. It casts a web of causality and explores it efficiently. It has a balance of breadth and depth. This is the true nature of its 'long performance.' It can execute long inferences stably and at a low cost.
5. DeepSeek's clever mechanisms
I will explain the clever mechanisms of DeepSeek V4 in detail.
MoE (Mixture of Experts)
DeepSeek V4 adopts a MoE architecture. MoE stands for 'Mixture of Experts.' The total number of parameters in the model is large, but only a portion of the parameters are used for each inference. Instead of activating all parameters, it selects and uses experts according to the problem.
It is easy to understand if you compare it to a warehouse. The entire warehouse is large, but you only open the shelves you need to retrieve items. There is no need to open all the shelves. Because it only opens the necessary shelves, it can retrieve items quickly and cheaply. This is MoE.
MLA (Multi-head Latent Attention)
DeepSeek V4 adopts a unique attention mechanism called MLA. Attention is a mechanism where the model calculates the relationship between each word in the input sentence. Normal attention keeps the calculation results for all heads (results calculated in parallel from multiple perspectives). If you compare this to a bookshelf, it is like lining up books on a shelf one by one. As the number of books increases, the shelf fills up, and there is no place to put new books.
MLA compresses and stores these calculation results. If you compare it to a bookshelf, it is like summarizing books, writing them on cards, and only lining up the cards on the shelf. The content of the books is not lost, but shelf space can be saved significantly. Even with long contexts, the shelf does not fill up, so inference can be performed at high speed.
Internal long inference
DeepSeek V4 automatically performs Chain of Thought, which explicitly generates the inference process, internally. Even if the user does not instruct it to 'think step-by-step,' the model automatically executes a three-stage process of 'organizing -> assembling -> verifying' internally.
This is the core of 'long performance.' It is not about providing knowledge, but about enhancing the ability to connect causality. It is not about educating, but about increasing the efficiency of exploration. It is not about increasing scale, but about optimizing the parameters that are activated.
Aside
When I first tried DeepSeek V4 Flash, I felt it was 'fast.' But to be precise, it is not 'fast,' but 'long.' It can produce long reasoning in a short time, at a low cost, and stably. What supports this 'long' capability is MoE, MLA, and internal long reasoning.
Just providing knowledge does not make it smart. Just educating does not make it deep. Just increasing scale does not make it efficient. Being able to stably execute long reasoning is the essence of performance. DeepSeek V4 hits that essence.
I have made mistakes in the past. I once thought that to lower inference costs, I should just make the model scale smaller. However, when the scale was reduced, the depth of reasoning was lost. DeepSeek V4 solved this problem by keeping the scale large while optimizing the activated parameters. You do not have to dig the same hole.
G
#DeepSeek #LLM #Inference #Cost #DesignPhilosophy #MoE #MLA
