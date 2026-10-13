---
id: "aaa4a964bdaca067"
title: "Yes I Understand How LLMs Work"
url: "https://kemendo.com/yes-i-understand-how-llms-work.html"
source: "kemendo.com"
domain: "kemendo.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-12T00:16:28Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["AndrewKemendo"]
language: "en"
summary: "<--Back\nYes I Understand How LLMs Work\nI continue to hear this claim made regularly that “nobody knows how large language models work,” and I want to put this claim to rest finally.\nI understand how large language models work. As do thousands of other people who have spent years studying, designing, training, and implementing them. The fact that you don't understand how they work, or that you…"
tags: []
orgs: ["IBM"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 1440
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50049596"
score: 12
comments: 6
community: "Hacker News"
---

# Yes I Understand How LLMs Work

kemendo.com · AndrewKemendo · 2026-10-12

<--Back
Yes I Understand How LLMs Work
I continue to hear this claim made regularly that “nobody knows how large language models work,” and I want to put this claim to rest finally.
I understand how large language models work. As do thousands of other people who have spent years studying, designing, training, and implementing them. The fact that you don't understand how they work, or that you don't personally know anyone who does, does not mean that nobody understands them.
This isn’t just something I hear from people who have never trained a model. MIT Technology Review published an article literally titled “Nobody knows how AI works.” TIME published another titled “No One Truly Knows How AI Systems Work.” WIRED has described neural networks as mysterious even to their creators, and IBM repeats similar claims in its own educational material. These are major publications presenting the limits of current interpretability research as though they establish the limits of human understanding.
Large language models are mechanical systems. They are built from mathematical functions that human people designed, implemented, and executed on computers that we engineered. There is no magic involved anywhere in this process. We know how the information enters the system, how it is transformed, how parameters are adjusted during training, and how those parameters are used to calculate an output.
Consider what actually happens when you ask a language model a question.
Your symbols (natural text) are converted into a different kind of representative data in a different symbolic format (tokens), which are represented to the computing switches numerically and passed through a sequence of mathematical operations. In a “transformer” architecture, these operations sequence multiple mathematical functions: matrix multiplications, attention calculations, normalization, and nonlinear transformations. The resulting numerical values, or “activations,” are passed through successive versions of this process, called “layers,” until the model produces a distribution over possible next tokens, from which an output is selected according to its decoding procedure. During training, the model's predictions are evaluated using a loss function, sometimes incorporating labels or feedback from humans or other software, and the resulting error signals are used to adjust its parameters. Ordinary queries to a deployed model do not automatically change those parameters.
Every one of these operations can be inspected. If you have access to the model and the appropriate instrumentation, we can record the activations at every layer, examine individual attention heads, inspect the weights and biases, and trace the numerical computation that produced a particular output. We can modify components, remove them, replace them, and observe what changes.
Further, we understand these processes well enough that people are continuously making improvements to them. We develop new architectures, modify training procedures, identify computational bottlenecks, change how attention is calculated, and deliberately alter model behavior. These improvements are possible precisely because we understand how the systems work and can investigate the parts we don't yet understand. This is how all Deep Learning works and is the basis of the Bitter Lesson.
I have trained models myself, written learning algorithms by hand, and spent much of my professional life working on artificial intelligence. I have also written an explanation of the history and mechanics of artificial intelligence for people who want to understand where these systems came from. I don't understand everything about every model, and neither does anyone else. That has never been the standard by which we determine whether someone understands a technology.
There are already entire research programs dedicated to doing precisely this. The Transformer Circuits research program investigates the internal computational mechanisms of neural networks, while research into circuit tracing develops methods for identifying and testing the pathways responsible for particular model behaviors. This work is happening right now and you can read all about it yourself, because most of it, unlike much of the experimental work in other scientific disciplines, is made public, and there are free ways to build models yourself with existing computers.
In the case of language models, we can go considerably further than almost any other technology because it is relatively cheap to reproduce the process that produces them. Unlike, for example, trying to reproduce commercial airplane building processes, there aren’t a whole lot of homemade airliners flying around out there.
If I have access to the training data, architecture, optimization procedure, initial conditions, and computational environment, I can train the model as much as I want and characterize it, which is how we establish stability across training runs and document the resulting model's characteristics in evaluations and model cards. I can change the random seed, alter the ordering of training examples, modify the architecture, or remove portions of the training data. I can repeat these experiments and compare the resulting models to determine which behaviors emerge consistently and which depend on particular training conditions.
Where there is randomness, we can characterize it experimentally. We can measure distributions, isolate variables, and investigate causal relationships between the conditions of training and the resulting behavior. We can even compare the internal representations learned by independently trained models to investigate whether similar computational structures emerge through different training histories.
All I am describing is how experimental science works.
The fact that we haven't developed a convenient procedure that translates every internal computation into an explanation accessible to an arbitrary person with no training does not establish that the system is incomprehensible. The interpretation may be difficult and inaccessible to most people, which is true of basically every technology in the modern world.
I have written previously about faith and the extraordinary amount of our understanding of the world that we inherit from other people. Most people have never personally verified the physical principles responsible for the technologies they use every day. They rely on an enormous accumulated body of knowledge produced by people who have conducted experiments, developed theories, and built systems that work.
Nuclear technology is always going to be my go-to comparison. Few people understand the detailed engineering of a nuclear reactor, and considerably fewer have access to the classified information necessary to understand the design of particular nuclear weapons. So is anyone out there saying nobody understands nuclear chain reactions? No, society has just accepted that unless you acquire specialized education and hands-on experience, you aren't going to understand much of it at the operational level (Feynman's quantum understanding point is separate).
Artificial intelligence is similarly specialized, although the underlying science is overwhelmingly more available to anyone willing to study it than in most experimental disciplines. As these systems become more complicated, fewer people will possess the technical knowledge necessary to understand their construction and operation in detail.
There is an enormous difference between saying that you don't understand something and declaring that nobody does. You should have some pretty extraordinary evidence before making that claim.
Of course there are countless unanswered questions about AI, which is the whole reason we have been studying it intensively, and there are open questions about intelligence itself that extend far beyond artificial intelligence. As I argued in my discussion of scientific rigor as a benchmark for AI, progress depends on measurable hypotheses and experiments. There are unanswered questions in every mature scientific discipline. Physicists don't understand everything about physics. Biologists don't understand everything about biology. Nobody concludes from this that nobody understands physics or biology. That's the point of science: It’s never over!
I had a long conversation with some of the philosophers at the Computational Philosophy Lab at Northeastern back in 2019, and one of the biggest takeaways had nothing to do with AI or computing. The conclusion was that philosophy does not answer questions; it breaks questions down into more questions in order to get to better clarity.
That is what science is, and that is how progress is made in AI and in every other technical discipline. You look like a fool when you say nobody understands how large language models (or any other technology) work. If you encounter something about these systems that genuinely isn't understood, wonderful. You've found a scientific question worth investigating. Form a hypothesis, design an experiment, and see what you can learn. What I object to is the casual transformation of personal ignorance into a universal claim about human knowledge, particularly when that claim is used to suggest that artificial intelligence is somehow mysterious or beyond scientific explanation.
These are machines we build, train, and inspect. We can reproduce their behavior, modify their internal operations, and investigate the processes through which they learn. It takes years to understand even the basics of this field, and the difficulty of acquiring that knowledge is not evidence that there exists nobody with the knowledge.
