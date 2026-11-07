---
id: "b2bd77cc7af86580"
title: "[Microsoft Copilot] From GitHub Copilot harness to \"Microsoft Copilot harness\". How will agent development in Copilot Studio change? #0405"
url: "https://note.com/kagen_shin/n/n8b644cd1e7ad?hl=en"
link: "https://note.com/kagen_shin/n/n8b644cd1e7ad?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-07T02:00:00Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Shinichi Kawara"]
language: "en"
summary: "On October 28, 2026, Microsoft announced that it would rename the foundation previously known as the \"GitHub Copilot harness\" to the \"Microsoft Copilot harness\".However, this should not be viewed as a ..."
tags: []
orgs: ["Microsoft", "OpenAI", "Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1362
paywalled: false
image: "http://www.bing.com/th?id=ONUT.VmNoyvFxk804Mg-W_j72Yg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# [Microsoft Copilot] From GitHub Copilot harness to "Microsoft Copilot harness". How will agent development in Copilot Studio change? #0405

note · Shinichi Kawara · 2026-11-07

[Microsoft Copilot] From GitHub Copilot harness to "Microsoft Copilot harness". How will agent development in Copilot Studio change? #0405
On October 28, 2026, Microsoft announced that it would rename the foundation previously known as the "GitHub Copilot harness" to the "Microsoft Copilot harness".
However, this should not be viewed as a simple rebranding.
Microsoft is expanding this harness, which originated in GitHub, into a common foundation for all of Microsoft. It is currently positioned as the foundation supporting not only Copilot Studio, but also Copilot Code, the GitHub Copilot app, CLI, Visual Studio Code, and more.
In this article, I will organize this change from the perspective of "what exactly is a harness" and "how does it differ from the standard Copilot Studio harness".
1. What is a "harness"?
When people think of generative AI, they tend to focus on "AI models" like GPT.
However, in actual AI agents, the model alone cannot complete tasks.
Microsoft Learn describes the harness as the runtime that exists between the selected model and the agents or workflows you create.
The harness handles processes such as:
- when to call the model
- what to pass to the model
- how to interpret the content returned from the model
- which tools to call
.
In other words, to simplify it significantly, it is easy to understand if you think of it as:
Model = ability to think
Harness = the mechanism that uses that ability to carry out work
.
The official Microsoft blog also describes the harness as an orchestration layer that exists around the model, providing the agent with appropriate instructions, context, execution environment, and control.
2. Why did it change from "GitHub Copilot" to "Microsoft Copilot"?
This is the key point.
This harness was originally a technology developed by the GitHub engineering team.
However, Microsoft has begun deploying this technology not as a GitHub-specific foundation, but as a common foundation supporting the Copilot experience across all of Microsoft.
Therefore,
GitHub Copilot harness
has been renamed to
Microsoft Copilot harness
.
From the perspective of someone using Microsoft Copilot Studio, it is best to understand this as evolving from a stage where "Copilot Studio uses GitHub technology" to a common agent foundation that spans Microsoft's Copilot product family. This is the shift in positioning that can be read from the official announcement.
3. What will change in Copilot Studio?
For existing Copilot Studio users, the important point is that this name change does not mean the behavior of existing agents will change.
Microsoft explains that for existing agents,
- they will continue to operate as they do now
- there are no changes to functionality
- there are no changes to billing
.
The names within the product will be updated to the new terminology gradually over time.
Therefore, at this moment, it is not surprising if the old name, GitHub Copilot harness, still remains in Microsoft Learn or parts of the product screen.
In fact, the name GitHub Copilot harness still remains in the Japanese Microsoft Learn updated on October 29, 2026.
4. What is different about the Microsoft Copilot harness?
This is where it becomes important for intermediate engineers.
With the standard harness in Copilot Studio, you can design agent behavior relatively explicitly by combining topics, variables, tools, and more.
On the other hand, advanced harnesses target longer and more complex tasks, enabling more agentic execution such as:
Understanding goals → breaking down processes → using tools → evaluating results → adjusting methods if necessary → re-executing
.
Microsoft Learn explains that advanced harnesses support long-running tasks, large files or datasets, iterative reasoning, persistent memory, and continuous interaction with sub-agents using shared context.
This can be considered a major shift from traditional "agents that execute predetermined conversation flows" to
"giving a goal and having the agent itself adjust the methods to reach that goal"
.
5. Combining tools, MCP, skills, and memory
In Copilot Studio's advanced harness, you can connect various resources to the agent.
Microsoft Learn describes the key elements as:
- Instructions
- Knowledge
- Tools
- Skills
- Models
- Connected agents
- Memory
, and so on.
Furthermore, you can proceed toward your goal by combining necessary processes while using not only connectors but also MCP (Model Context Protocol) and other agents.
This is extremely important for Power Platform engineers.
Until now, the focus of design was on
"which flow to call and under what conditions"
, but from now on,
"what to have the agent achieve, and which tools, knowledge, skills, MCPs, and agents to make available for that purpose"
will become an even more important design perspective.
6. There are cases where the "harness" is more important than changing the AI model
What is particularly interesting about this announcement is Microsoft's internal evaluation.
Microsoft compared the Standard harness and the Microsoft Copilot harness on the same tasks.
As a result, the evaluation pass rate for the Microsoft Copilot harness
- When using OpenAI models: 10.8 percentage point improvement
- When using Anthropic models: 22.1 percentage point improvement
was reported.
Furthermore, even when tool calls failed, it was reported that the Microsoft Copilot harness continued to resolve issues in 84–91% of evaluation cases, whereas the Standard harness did so in less than 7%.
Of course, this is Microsoft's internal evaluation and does not mean that the same improvement rate will apply to all business scenarios.
However,
is an important implication.
Beyond just the model, it is necessary to look at how to combine context, tools, execution environments, and orchestration.
I believe this is exactly the point that intermediate users should focus on next.
7. It is not just a matter of "using the new harness"
So, should all Copilot Studio agents be built with the Microsoft Copilot harness from now on?
It is not that simple.
Microsoft Learn suggests the following criteria for choosing between them.
What the standard harness is suitable for
- Relatively short processes with a clear scope
- Tasks where you want to explicitly control the behavior
- Processes that use predefined data or tools
- Cases with specific channel requirements
What the advanced harness is suitable for
- Long-running tasks
- Tasks that require coordinating many processes
- Processes that require advanced reasoning
- Tasks where the processing method changes depending on the situation
- Tasks that reach a result through repeated trial and evaluation
Microsoft also points out that using an unnecessarily advanced harness can lead to excessive processing for simple problems, potentially increasing Copilot Credit consumption and latency.
In other words,
it is important to "choose because it is necessary for the business process," not "use it because it is new."
is important.
8. Perspectives required for future Copilot Studio engineers
If you only want to follow this name change,
GitHub Copilot harness → Microsoft Copilot harness
is all you need to remember.
However, if you want to step up from an intermediate level, you should understand the background behind it.
In future agent design,
- Model
- Instructions/Context
- Knowledge
- Tools / Connectors
- MCP
- Skills
- Memory
- Other agents
- And the harness that runs them
you need to understand these multiple layers.
In other words, mastering Copilot Studio is expanding beyond just "writing prompts" and "creating topics" to designing the execution architecture of the entire agent.
This perspective is exactly what intermediate Power Platform engineers should look to deepen in the future, isn't it?
Summary
The change from "GitHub Copilot harness" to "Microsoft Copilot harness" is a small change if you only look at the name.
However, looking at the background, we can see a trend where Microsoft is deploying the harness born in GitHub as a common foundation spanning the Copilot product family. Microsoft explains that this harness supports Copilot Code, Copilot Studio, GitHub Copilot app, CLI, VS Code, and more. [blogs.microsoft.com]
As a Copilot Studio engineer, what is important is not just following product names.
"With which harness, with which tools and context, and how do you guide the model's capabilities to the completion of a task?"
Designing agents from this perspective is likely to become increasingly important from now on.
