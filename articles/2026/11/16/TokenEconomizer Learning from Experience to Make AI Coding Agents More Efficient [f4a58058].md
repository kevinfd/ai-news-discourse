---
id: "f4a580580dcfc266"
title: "TokenEconomizer: Learning from Experience to Make AI Coding Agents More Efficient"
url: "https://microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient"
link: "https://microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient"
source: "Microsoft Research"
domain: "microsoft.com"
source_type: "research"
collector: "rss"
date: "2026-11-16T17:01:35Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Aaron J. Li, Weijia Xu, Chandan Singh, Jeevana Priya Inala, Bin Yu, Ion Stoica, Michel Galley, Jianfeng Gao"]
language: "en"
summary: "At a glance \n\n Developers use AI coding agents in the same codebases day after day, yet agents often start each session from scratch: rediscovering familiar facts, loading unused tools, and repeating unsuccessful approaches. \n\n TokenEconomizer is an open-source plugin that learns from an agent’s past sessions in a repository to reduce waste in future sessions, without modifying the agent or its…"
tags: ["Research Blog"]
orgs: ["Microsoft", "Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 871
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# TokenEconomizer: Learning from Experience to Make AI Coding Agents More Efficient

Microsoft Research · Aaron J. Li, Weijia Xu, Chandan Singh, Jeevana Priya Inala, Bin Yu, Ion Stoica, Michel Galley, Jianfeng Gao · 2026-11-16

At a glance
- Developers use AI coding agents in the same codebases day after day, yet agents often start each session from scratch: rediscovering familiar facts, loading unused tools, and repeating unsuccessful approaches.
- TokenEconomizer is an open-source plugin that learns from an agent’s past sessions in a repository to reduce waste in future sessions, without modifying the agent or its underlying model.
- Across 277 real bug-fixing tasks, TokenEconomizer reduced costs by 18.4–30.9% across multiple AI coding agents. Costs fell in every repository tested, while task success rates remained broadly stable.
AI coding agents are increasingly helping developers fix bugs and build features largely on their own, but every interaction with their models consumes tokens. In each session, an agent sends instructions, tool descriptions, and session history to its model. Most efforts to reduce this cost focus on individual tasks. Yet developers return to the same repositories, giving agents an opportunity to learn from previous work. Without that learning, an agent may repeatedly rediscover how to run tests, load tools it never uses, or spend dozens of turns revisiting the same error.
In our paper, TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents, we ask a simple question: can experience in a repository help an agent solve future tasks more efficiently? TokenEconomizer, an open-source plugin from UC Berkeley, Microsoft Research, and Microsoft Security, turns completed sessions into guidance for subsequent ones. It reduces waste without changing the agent or its underlying model, so developers can use it alongside the coding agents they already rely on.
Where the tokens go
We first profiled Claude Code on 60 tasks from SWE-Bench, a benchmark of real bug fixes in open-source Python projects, running each repository’s tasks in sequence. Three kinds of waste recurred:
- Rediscovering the same facts. After a repository had accumulated at least five completed tasks, 30% of tool calls repeated an action from an earlier task in that repository. Only 7% matched an action in another repository’s history.
- Paying for unused tools. The agent received 23 tool descriptions on every turn, but 16 were never called.
- Getting stuck on failures. The 17% of tasks that failed accounted for 32% of the spending.
We also tested three popular open-source plugins, each built around a fixed cost-saving strategy. Each lowered costs in some repositories but not others. Together, these findings suggest that effective cost control must adapt to the repository, rather than apply the same strategy everywhere.
How TokenEconomizer works
After each session, TokenEconomizer reads the session’s log and updates what it knows about the repository. It then acts through three mechanisms, using only interfaces the agent already provides, as illustrated in Figure 2.
Micro-skills capture repository-specific knowledge in one-line notes. TokenEconomizer identifies recurring patterns across sessions and proposes corresponding notes. They are added to the agent’s starting context only after several sessions have confirmed the pattern, and retires the note if later evidence contradicts it.
Tool pruning removes tools that repository history suggests the agent is unlikely to use, while always retaining core tools for running commands and editing files. Removed tools can be restored if needed.
Failure-loop intervention watches for an agent that keeps hitting the same failure. A judge model decides whether the agent is truly stuck or still making progress. If it is stuck, the agent gets a short note suggesting a different approach. In the open-source plugin, if the agent is still stuck after the note, TokenEconomizer alerts the developer rather than stopping the work itself.
The controller is designed to revise its decisions as new evidence arrives. Reported savings also account for the cost of TokenEconomizer’s own model calls.
Saving costs in every repository
We evaluated TokenEconomizer on 277 SWE-Bench tasks from six repositories, using five different AI coding agent and model combinations. For each repository, TokenEconomizer started with no prior session history.
TokenEconomizer lowered the average cost by 18.4–30.9%, as shown in Figure 3, and saved the most in all 30 repository-combination pairs without performance loss. By contrast, lowering the model’s reasoning effort saved similar or larger amounts but led to substantial performance degradation.
Savings grow as experience accumulates. Early tasks can cost more while TokenEconomizer learns, but cumulative costs fell below the default in every repository by the sixth task, shown inFigure 4. Each mechanism contributes savings on its own, and combining all three delivers the largest reduction.
The savings also carried over to sequential web development, with costs 16.0–21.2% lower on Web-Bench. On security auditing, where every task is in a new repository, costs were 6.4–19.6% lower.
Looking ahead
TokenEconomizer opens a path toward coding agents that learn not only how to solve tasks, but also how to spend computation more effectively. Its lightweight controller shows how experience can improve efficiency without changing the underlying agent or model.
The open-source plugin makes these directions accessible to developers and researchers. It is designed to run alongside existing AI coding agents without modifying their underlying models, requires no API key of its own, and keeps what it learns on the developer’s machine. We invite the community to use it as a starting point for exploring agents that become more resourceful with experience, adapting how they work, as well as what they know.
