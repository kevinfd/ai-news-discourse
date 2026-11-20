---
id: "9a46680ab5aafc8d"
title: "What I Learned From Kaggle + Google’s Free Agentic AI Course"
url: "https://kdnuggets.com/what-i-learned-from-kaggle-googles-free-agentic-ai-course"
link: "https://kdnuggets.com/what-i-learned-from-kaggle-googles-free-agentic-ai-course"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-19T15:00:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Bala Priya C"]
language: "en"
summary: "Learn to build AI agents with Gemini and Google’s ADK through this free course, covering tools, memory, evaluation, and deployment."
tags: []
orgs: ["Google"]
topics: ["agents & coding", "models & research", "search & media"]
content_source: "fulltext"
word_count: 1316
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/kdn-bala-kaggle-google-agentic-ai-course.png"
discussion_url: null
score: null
comments: null
community: null
---

# What I Learned From Kaggle + Google’s Free Agentic AI Course

KDnuggets · Bala Priya C · 2026-11-19

What I Learned From Kaggle + Google’s Free Agentic AI Course
Learn to build AI agents with Gemini and Google’s ADK through this free course, covering tools, memory, evaluation, and deployment.
I took the 5-Day AI Agents Intensive Course from Kaggle and Google. The course originally ran live from November 10 to 14, 2025, and is now available as a free, self-paced course on Kaggle. You can work through the whitepapers, hands-on codelabs, podcasts, and recorded livestreams at your own pace, exploring how AI agents work and what it takes to build them.
A single prompt and a single response are easy to reason about. An agent adds a loop around that: the model picks an action, calls a tool, reads what came back, and decides what to do next. The loop brings questions that a one-shot call never raises. How does the agent remember the last turn, how do you know it picked the right tool, and what changes when it has to run somewhere other than your notebook?
The course works through those questions. Each day pairs a whitepaper with two hands-on notebooks built on Gemini and the Agent Development Kit (ADK), Google's open-source framework for building agents. You need Python and some experience calling a large language model API, but no prior knowledge of agents. These are my notes on what stood out. This article covers:
- How to tell when a task needs an agent, and the patterns for wiring several together
- How tools and the Model Context Protocol (MCP) connect agents to the outside world
- How sessions and memory give an agent the context it needs
- How to measure agent quality, and what it takes to run agents beyond a notebook
Check out the course at this link: 5-Day AI Agents Intensive Course with Google | Kaggle
Building a First Agent and Wiring Several Together
The first day introduces agents and the architectures you can build with ADK. The first notebook, From Prompt to Action, builds a first agent, and the second, Agent Architectures, moves on to systems where several agents work together.
In ADK, an agent is a small bundle: a name, a model, a description that other agents can read, instructions that set its behavior, and a list of tools. A runner executes it. An in-memory runner is fine for experiments, and anything real needs a persistent one.
When one agent carries too many jobs, you split the work across several. The course covers a few ways to wire them together: a parent agent that chooses which sub-agent to call, a sequential pipeline, parallel branches that run at the same time, and a loop that repeats until a condition is met. In a sequential pipeline, each agent hands its output to the next.
I'd reach for the pipeline first. It runs in a fixed order, so a failure points at one stage, and a model choosing between sub-agents needs tracing before you know what happened.
Notebooks: From Prompt to Action and Agent Architectures
Giving Agents Tools
Tools are what let an agent do anything beyond writing text. The course covers four kinds. Built-in tools like Google Search come with the model. Function tools wrap your own Python functions. Agent tools let one agent hand a subtask to another while keeping control of the conversation. MCP tools connect to outside services through the protocol, so you skip writing a custom client for each one.
The model decides how to call a function tool from its description alone. That is why the best-practices notebook spends its time on docstrings, type hints, and structured return values: the clearer the description, the fewer wrong calls.
The course also covers human approval for long-running operations, where the agent pauses and waits for a person to confirm before it continues. My rule of thumb: when an agent picks the wrong tool, read the tool description before you touch the prompt.
Notebooks: Agent Tools and Agent Tools Best Practices
Adding Memory Across Turns and Sessions
A model keeps nothing between calls. On every turn the agent has to send the conversation history again, and that history costs tokens. Memory in ADK splits into two parts. Short-term memory is the session, the conversation history, managed by a session service. Long-term memory is outside the session and is searched through a memory service, so facts can survive into the next conversation.
The memory service comes in different forms. The in-memory version searches by keyword, and managed services can search by meaning. As a session grows, context compaction and caching keep both the cost and the context size under control. This brings us to effective context engineering, which means choosing what goes into the model's context on each turn.
Retrieval from long-term memory comes in two modes. In reactive retrieval, the agent searches memory when it decides to. In proactive retrieval, the system searches before every turn and hands the agent the results. Proactive retrieval costs a search per turn and gives the agent relevant memories without asking. Reactive retrieval saves that cost and depends on the agent knowing when to look.
Notebooks: Agent Sessions and Agent Memory
Understanding Agent Quality and Evaluation
Agents are non-deterministic: the same input can take a different path on the next run. A final spot check cannot cover that, so the course treats quality as part of the design from the start. Agent quality rests on two practices.
Observability records what happened through logs, traces, and metrics. A trace shows each step the agent took, which makes a wrong answer debuggable after the fact. Evaluation scores two things: the final response, and the process behind it, such as which tools the agent called and in what order. Running evaluation continuously catches regressions early.
Scoring the process matters because a correct answer can hide a bad path. An agent that calls the right tool three times when once was enough returns the same answer and costs three times as much.
Notebooks: Agent Observability and Agent Evaluation
Taking an Agent Beyond the Notebook
The last day covers what happens after the demo works. Agents built by different teams, in different frameworks and languages, need a shared way to talk to each other. The Agent2Agent protocol provides one: an agent is exposed as a service, and other agents find out what it can do by reading its agent card.
On the deployment side, the course puts an agent on a managed runtime, Vertex AI Agent Engine, and introduces CI/CD and AgentOps practices for keeping agents running after launch. It also mentions that ADK is available for Go and Java as well as Python. The course closes with an optional capstone project, where you build an agent of your own from the pieces above.
Notebooks: Agent2Agent Communication and Agent Deployment
Wrapping Up
The course covers how to build an agent, how to give it tools and memory, how to measure it, and how to deploy it. The notebooks cover implementation with Google's ADK, and the whitepapers are good companion reads. In effect, you should be measuring both the path an agent takes and the answer it returns. Some resources for further learning:
- 5-Day AI Agents Intensive course guide
- Agent Development Kit (ADK) documentation
- Agent2Agent protocol
Happy learning!
 
Bala Priya is a developer, educator, and technical writer based in India. She writes about programming, data science, machine learning, and AI, with a focus on making complex technical ideas practical and approachable. She creates tutorials, how-to guides, and deep dives that help developers build, solve problems, and understand complex technical concepts. Her technical interests include LLM applications, agentic AI, graph algorithms, computer vision, explainable AI, and ML systems. When she’s not writing or coding, Bala is usually reading classic literature, epic fantasy, or speculative fiction. She also enjoys talking about books, learning new things, and sharing what she learns with the developer community.
