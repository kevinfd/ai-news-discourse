---
id: "a0dfc1d96975e579"
title: "ROI From Your AI Agents Isn't About Costs"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/09/roi-from-your-ai-agents-isnt-about-costs"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/09/roi-from-your-ai-agents-isnt-about-costs"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-09T12:15:00Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Siva Surendira, Forbes Councils Member"]
language: "en"
summary: "Durable returns come from allocating the right level of intelligence to each task, not simply negotiating lower model prices."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["models & research", "agents & coding", "policy & regulation", "business & funding"]
content_source: "fulltext"
word_count: 1009
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6adf9a140418747148c7e2c0/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# ROI From Your AI Agents Isn't About Costs

Forbes · Siva Surendira, Forbes Councils Member · 2026-11-09

Siva Surendira is the Founder and CEO of Lyzr AI, an agentic AI platform for building and governing AI agents.
At midnight last quarter, a client sent me a screenshot of their monthly AI model bill. They added that three agents, which have been live for a quarter, were doing work nobody in the company disputed was useful and that not one person in the building could explain how the cost had compounded.
A June 2025 Gartner, Inc. report estimated that “over 40% of agentic AI projects will be canceled by the end of 2027, due to escalating costs, unclear business value or inadequate risk controls.”
I don’t think that means companies should stop building agents, but it does mean we need to be more thoughtful about where agents actually make sense and what we expect them to deliver.
After more than 100 AI agent implementations, I’ve seen monthly frontier-model spend range from around $50,000 at smaller companies to $800,000 at a fashion brand, $1.2 million at a publishing company and roughly $4 million at a fast-moving consumer goods retailer.
The bigger question should be what companies are asking these models to do on such a scale. Far too often, the answer is nearly everything.
When a new task arrives, it goes to the most capable model. An agent meant to review contract risks and an agent meant to build a marketing strategy aren’t meant to run the same way, but they inevitably end up doing so in most companies. Because model quality improved and inference costs fell, tweaking every AI agent call felt unnecessary. If the best model could solve the problem, why not use it?
At scale, it avalanches into an allocation nightmare. It’s like getting the principal engineer of a company to reset a system password and instructing the partner of a law firm to look into spellcheck in a contract.
Match the model to the difficulty.
We spent a century learning to match expertise to difficulty in the workforce, so why not apply the same rules to our AI agents?
Much of enterprise work consists of classification, extraction, lookup, formatting or validation. Those steps may sit inside sophisticated workflows, but that doesn’t make every step about reasoning.
A simple routing layer can now assess the task and send it to the least expensive model that clears the quality bar. For harder cases, you should first break the job into smaller pieces, let smaller models handle them and compare independent runs. If the answers converge, carry on. If they diverge, spend more compute or escalate.
The important principle should be to not pay for intelligence you don’t need.
Expensive doesn’t equal effective.
A hard pill to swallow for many companies is hearing they don’t always need frontier models for everything. Production traffic can continue flowing through the stronger model while its inputs and outputs are captured. A smaller model can run alongside it, initially serving nothing, while its answers are compared against the incumbent on repetitive categories of work. When it consistently meets the quality bar, it moves traffic gradually. If quality slips, move it back.
The model best suited to a task today doesn’t have to be the model doing it six months from now.
Hold your AI bill accountable.
A token bill is not an ROI metric. Companies know what they spent on AI without knowing what the spending accomplished.
The useful number is closer to cost per completed outcome. The outcome could be a ticket resolved, a document processed, a transaction cleared and a merged pull request. That means connecting consumption to teams, workflows and results.
McKinsey’s 2026 enterprise AI FinOps survey found that 93% of respondents had exceeded their AI budgets. McKinsey also cited research showing that token usage for the same coding task can vary by as much as 30 times, depending on how an agent executes it.
The question to pose to your teams isn’t what the models cost but why this particular task cost what it did.
Your agentic workflow is a series of decisions.
Across the more than 1,000 conversations I’ve been part of, I’ve watched teams point frontier models at processes that had four known branches and could have been handled with plain, deterministic logic. There’s a better way to think about it.
Take a common use case across most businesses, such as customer emails demanding a refund. It may look like a single task, so the teams hand it to one AI model. Look closer, however, and it’s five smaller jobs:
1. Read the email, and label it as a refund request, a complaint or a question.
2. Find the customer’s order and purchase date.
3. Check the refund policy. Within 30 days, yes. Otherwise, no.
4. Handle the odd cases more, such as a loyal customer with a damaged item and an unclear timeline.
5. Write a polite reply.
The first and fifth steps are easy for a small, inexpensive model. The second and third steps are a database lookup and a fixed rule, which need no AI at all. Only the fourth step deserves your most capable model—the one that weighs the context, makes the judgment call and hands its answer back to the main agent.
If you run all of the tasks on a premium model, you just pay top rates for five steps when only one needs it.
The next time you use AI agents, break the workflow into different individual tasks. Assign models with complexity. Ask how difficult each task actually is and then use the smallest, cheapest tool that can handle it well. The goal is to make sure you’re not paying for more model capability than what the task actually needs. Remember, there’s no intelligence premium for solving a problem that doesn’t require it.
Durable returns come from allocating the right level of intelligence to each task, not simply negotiating lower model prices. Before asking which model to buy next, determine the minimum amount of intelligence this task needs to produce a trustworthy outcome and, by extension, good ROI.
