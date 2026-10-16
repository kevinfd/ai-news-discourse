---
id: "15545a394362192d"
title: "The Next Enterprise AI Bottleneck Isn't Compute—It's Context"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/15/the-next-enterprise-ai-bottleneck-isnt-compute-its-context"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/15/the-next-enterprise-ai-bottleneck-isnt-compute-its-context"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-15T10:15:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Vivek Ahuja, Forbes Councils Member"]
language: "en"
summary: "As AI moves from answering questions to taking actions, context must include not only what an agent knows but also what it is allowed to do."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "models & research", "policy & regulation", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1032
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6aa15c54fc3b7d9c41034e9f/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# The Next Enterprise AI Bottleneck Isn't Compute—It's Context

Forbes · Vivek Ahuja, Forbes Councils Member · 2026-10-15

Vivek Ahuja, VP of Technology at rSTAR, focused on enterprise AI, architecture, and measurable business outcomes.
Over the past year, I have been in a number of conversations about scaling enterprise AI. The discussion usually starts with models. Which model should we use? Which one has the best reasoning? Should we use multiple models?
Those are important questions. But increasingly, I don’t think they are the questions holding enterprise AI back.
I’ve seen teams build impressive AI solutions only to discover that the model doesn’t have access to the information it needs to make a useful decision. Customer information is in the CRM. Transactions are somewhere else. Policies live in documents. Operational data sits in other systems.
The model may be capable. It just doesn’t understand enough about what is happening inside the enterprise.
That is why I believe the next enterprise AI bottleneck isn’t compute. It’s context.
Intelligence without context has limited value.
Foundation models have become remarkably capable, but enterprise decisions rarely depend on general knowledge alone. They depend on knowing the customer, transaction, asset, policy, history, user’s permissions and what happened five minutes ago.
Think about a customer asking, “Why is my bill higher this month?” The AI may need billing history, the customer’s rate plan, recent usage, account changes and applicable policies across multiple systems. Without that context, even a capable model can provide an answer that sounds reasonable but is wrong for that customer.
This becomes even more important with AI agents. An assistant that generates an inaccurate answer creates a problem. An agent that acts on incomplete context can create a much bigger one.
Gartner’s 2026 research makes a similar point: “Agentic AI outcomes depend on context including semantic representations of data.” Without understanding the relationships and rules within an organization’s data, agents are more likely to produce inaccurate results.
Retrieving data and understanding context are not the same thing.
RAG was an important step, but it isn’t the entire answer.
Retrieval-augmented generation helped solve one of the first enterprise AI challenges: giving a model access to information it wasn’t trained on. We have used this pattern extensively, and it remains extremely valuable. But retrieving documents is only one type of context.
An AI system may know what a policy says but still not know whether that policy applies to this customer, transaction or situation. In my experience, enterprise AI increasingly needs five types of context:
• Data Context: What does the enterprise know about this customer, asset, product or transaction?
• Business Context: What does that information actually mean inside the organization?
• User Context: Who is making the request, and what are they authorized to access?
• Workflow Context: What has already happened, and what should happen next?
• Decision Context: What rules, policies and constraints should influence the response or action?
This is where enterprise AI becomes less about connecting a model to documents and more about connecting intelligence to the enterprise.
The data problem is becoming a context problem.
McKinsey’s 2026 research on agentic AI found that “nearly two-thirds of enterprises worldwide have experimented with agents, but fewer than 10 percent have scaled them to deliver tangible value.” Additionally, “eight in ten companies cite data limitations as a roadblock to scaling agentic AI.”
That doesn’t surprise me. I’ve seen organizations spend weeks debating which foundation model to use, only to discover that the information needed to answer the question was spread across multiple systems.
The problem isn’t necessarily that the data doesn’t exist. The problem is making the right data available, trusted and understandable at the moment AI needs it.
Forrester has made a similar observation about real-time context. As agents begin making decisions and taking actions, they need information that reflects what is happening in the business now. Yesterday’s context may not be good enough. Data platforms, APIs, integration, master data, semantic models, identity and governance are no longer separate conversations from AI.
They are part of the AI architecture.
Context also needs governance.
There is another side to context enterprises need to consider.
More context isn’t always better. An AI agent shouldn’t automatically have access to every piece of information across the enterprise.
If an employee isn’t authorized to view certain customer information, the AI assisting that employee shouldn’t suddenly gain access to it because another data source improves the answer.
The same applies to actions. Knowing that a customer has an outstanding balance is one thing. Waiving that balance is another. As AI moves from answering questions to taking actions, context must include not only what an agent knows but also what it is allowed to do.
Deloitte’s “2026 State of AI in the Enterprise” highlights this challenge. Organizations report growing confidence in AI strategy, but preparedness across infrastructure, data, risk and talent remains lower. Deloitte also found that only one in five companies had a mature governance model for autonomous AI agents.
Start building the context layer.
I don’t think every enterprise needs a massive new “context platform” initiative. I would start much more practically.
Pick an important AI use case and trace the context required to make the right decision. Where does the information live? Who owns it? How current is it? Who can access it? What business rules apply?
Then ask one more question: Can the next AI use case reuse that context, or are we going to build everything again?
That is where the difference between an AI project and an enterprise AI capability begins to emerge. Over time, organizations can create reusable ways for AI systems to access governed enterprise knowledge, operational information, business semantics, identity, workflow state and policies.
The goal isn’t to give AI access to everything. The goal is to give it the right context, at the right time, with the right permissions.
We have spent the last few years asking how intelligent AI models can become. For enterprises, I think the more important question now is: How much does our AI understand about our business when it needs to make a decision?
Models provide intelligence. Context makes that intelligence useful to the enterprise.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
