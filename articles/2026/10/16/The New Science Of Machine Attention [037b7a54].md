---
id: "037b7a54f4a36828"
title: "The New Science Of Machine Attention"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/16/the-new-science-of-machine-attention"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/16/the-new-science-of-machine-attention"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-16T10:00:00Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Nicola Sfondrini, Forbes Councils Member"]
language: "en"
summary: "How does an AI system decide what deserves attention, what enters its \"working space\" and what gets ignored?"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 767
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/68a786ffafc452170ef98a1a/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# The New Science Of Machine Attention

Forbes · Nicola Sfondrini, Forbes Councils Member · 2026-10-16

Nicola Sfondrini - Partner Cloud Infrastructure and Architecture at PWC.
GenAI is often described as intelligent, creative, even “reasoning.” However, anyone who uses it every day has also seen a different side. It can lose the thread, overfocus on an irrelevant detail, ignore an instruction it was given two paragraphs earlier or jump confidently toward the wrong conclusion.
We need to look beyond raw intelligence and ask a practical question: How does an AI system decide what deserves attention, what enters its “working space” and what gets ignored?
Inside The AI’s Global Workspace
Recent interpretability research from Anthropic gives us a fascinating new lens. Researchers identified a small set of internal neural patterns in Claude that appear to behave like a “global workspace,” a shared internal area used for deliberate reasoning. They call it the J-space. Unlike the model’s visible output or chain-of-thought-style scratchpad, the J-space operates silently inside the network. It can contain concepts the model’s considering even when those concepts never appear in its answer.
That distinction matters. Most of what a language model does appears to be automatic. It can produce fluent text, use grammar, retrieve simple facts and classify information without relying heavily on this workspace. When researchers disrupted the J-space, higher-order capabilities such as multistep reasoning deteriorated sharply. In other words, the model could still “talk,” but it became much worse at structured thinking.
Capability Versus Sustained Cognitive Control
That sounds surprisingly familiar to a problem enterprises already experience with GenAI: Capability isn’t the same thing as sustained cognitive control.
A frontier model may know everything required to complete a task yet still fail because the wrong information receives priority at the wrong moment. This is why prompt engineering alone is increasingly insufficient. The future of enterprise AI will depend less on asking better questions and more on designing better cognitive environments around the model.
Think about an AI agent performing a financial reconciliation, investigating a cybersecurity incident or coordinating a supply chain disruption. The challenge isn’t merely whether the model can understand each individual piece of information. It must continuously distinguish signal from noise, preserve goals across many steps, recognize contradictions, revisit assumptions and know when a new event deserves to interrupt the current plan. That’s an attention management problem.
The Economics Of Context And Attention
Many enterprises are beginning to treat context almost like an unlimited resource: more documents, more memory, more tools, more agents. More context can also create more competition for relevance. The key design question may soon become not “How much can the model see?” but “What should the model be thinking about right now?” That shift changes how we design retrieval, memory and agent orchestration.
The Anthropic experiments make this more concrete. Researchers showed that concepts placed in the J-space could causally redirect subsequent reasoning. Swap the internal concept “spider” for “ant,” for example, and the model changes the answer to a downstream question about the number of legs. The same internal representation could also be reused across multiple tasks, suggesting the workspace acts as a shared broadcasting mechanism rather than a passive record.
Three Implications For Business Leaders
For business leaders, there are three implications:
1. Context isn’t cognition.
Giving a model a million-token context window doesn’t guarantee that the right information becomes operationally important. Enterprises will need mechanisms that actively prioritize, summarize and refresh the information that matters.
2. Agentic AI needs an attention architecture.
Memory, orchestration, tool selection, planning and exception handling shouldn’t be treated as separate technical features. Together, they determine what the model’s effectively “thinking about” at each stage of a workflow.
3. Observability must move inside the reasoning process.
Traditional software monitoring tells us what a system did. AI governance increasingly needs to understand why certain information influenced a decision and whether the model noticed risks it never surfaced. Anthropic’s work even shows that internal signals can reveal when a model suspects it’s being tested, detects manipulation or is pursuing a hidden objective.
Machine Attention As The Next Frontier
This may become one of the most important frontiers of AI governance. The competitive advantage of tomorrow’s AI systems may come not only from bigger models, more parameters or larger context windows but from better control over machine attention—what enters the workspace, what stays there, what’s discarded and what gets escalated.
GenAI has an attention problem in the engineering sense of the word. As AI moves from answering questions to running processes, making decisions and coordinating autonomous actions, attention may become as important as intelligence itself.
That’s where the next generation of enterprise AI architecture will likely be won or lost.
