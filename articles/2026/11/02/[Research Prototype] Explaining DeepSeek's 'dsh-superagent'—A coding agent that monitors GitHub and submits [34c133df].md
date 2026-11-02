---
id: "34c133dff915b771"
title: "[Research Prototype] Explaining DeepSeek's 'dsh-superagent'—A coding agent that monitors GitHub and submits PRs on its own"
url: "https://note.com/masa_cloud/n/nee8ab04713e0?hl=en"
link: "https://note.com/masa_cloud/n/nee8ab04713e0?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-02T01:59:00Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["伊藤正章｜サバイバルDxクリエイター：荒野のPip-Boy設計局"]
language: "en"
summary: "Introduction: This is not a 'product'On October 31, 2026, the DeepSeek Harness team suddenly released `dsh-superagent-prototype` on GitHub. It exceeded 4,000 stars in one day and became a hot topic in ..."
tags: []
orgs: ["DeepSeek", "OpenAI", "Apple"]
topics: ["agents & coding", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1092
paywalled: false
image: "http://www.bing.com/th?id=ONUT.mTKJyGrHVBWaMv1NAzx6Jw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# [Research Prototype] Explaining DeepSeek's 'dsh-superagent'—A coding agent that monitors GitHub and submits PRs on its own

note · 伊藤正章｜サバイバルDxクリエイター：荒野のPip-Boy設計局 · 2026-11-02

[Research Prototype] Explaining DeepSeek's 'dsh-superagent'—A coding agent that monitors GitHub and submits PRs on its own
Introduction: This is not a 'product'
On October 31, 2026, the DeepSeek Harness team suddenly released `dsh-superagent-prototype` on GitHub. It exceeded 4,000 stars in one day and became a hot topic in an instant. However, there is something that must be emphasized first.
This is not an official DeepSeek product, but merely a 'research prototype'. The README also clearly states, 'Research prototype for reference only, not an official DeepSeek product.' The official team admits that there may be bugs remaining and that the coding style is not consistent.
With that said, the design philosophy presented by this tool is extremely interesting. In this article, I will organize its mechanism, actual usage experience, and points to note.
What kind of tool is it in the first place?
`dsh-superagent` is described as a 'proactive coding agent targeting a single GitHub repository' and simultaneously as a 'framework for how to interact with agents'.
The basic operation is as follows.
- Monitors GitHub (or Feishu)
- Receives requests from authorized people (such as via '@agent-name' in Issue comments)
- Determines the requester's authority and execution value, and creates a Ticket
- Prepares an independent session and working directory for each Ticket, reads the code, makes corrections, and executes tests
- Returns the results to the original conversation thread as a Pull Request
Instead of 'giving detailed instructions every time,' it continuously monitors interactions on GitHub and processes them somewhat autonomously.
The core of the architecture: Separation of Router and Worker
The most important part of this tool's design is the two-layer structure of Router and Worker.
- Router (resident) : Receives messages from GitHub or Feishu, understands the relationships between tasks, and assigns work to Workers. All decisions are made here.
- Worker (executor) : Has an independent session and directory for each Ticket, and performs actual code corrections, test execution, and PR creation.
This separation creates the advantage that even if multiple tasks are run in parallel, their contexts do not get mixed up.
Also, what is important is the Policy mechanism that determines 'which requests to accept'. You can define rules in advance regarding whose requests to accept and under what conditions to execute automatically; in the initial state, it operates in 'observe mode'—where it does not actually perform work but only records 'whether it should have accepted it'.
A record from someone who actually tried it out
The record of a developer who actually tried it in a local environment (Apple Silicon Mac Mini) is a helpful reference.
- After posting an Issue, there was an automatic response in 49 seconds, and a PR arrived within 2 minutes
- The fix was one line, and it passed CI
- The cost incurred was about 4 yen
Also, official experimental data reports that more than half of the tasks were completed within 12.4 minutes, and 95% within 15.7 minutes. It is said that the completion time has been reduced compared to the conventional 'single session with sub-agents' method.
However, it should be noted that this is an initial experiment in a synthetic load/simple environment, and it does not measure actual coding quality.
The reality of token consumption and costs
The fact that it 'operates autonomously' also means that it consumes a lot of tokens.
In actual verification, there is a record that it consumed about 80k input and 8.6k output tokens per ticket. Calculating at the peak rate of V4-Pro, it is about $0.14 (approx. 20 yen) per ticket. If you use a cheaper model like V4.1-Flash, you can keep it to less than $0.01 per ticket.
The '2-minute PR, 4-yen' case mentioned earlier can also be said to be a figure achieved only through the use of inexpensive models and caching. Conversely, if you request large-scale refactoring or fixes that span multiple files, it can reach the multi-million token scale.
Setup in practice: OS and prerequisites
This is the most important point to note.
`dsh-superagent` operates as a DeepSeek Harness (DSH) plugin, so you first need the DSH core. Furthermore, because the setup script depends on `tmux`, it does not work on native Windows. macOS, Linux, or WSL on Windows is required.
The official recommended method for the setup itself is to 'let the agent do it.' Open the repository in DSH and give it this instruction:
Then the agent will ask questions one by one and proceed from installing dependencies to configuration. The time required is about 10 minutes. You will be asked for `gh-agent auth login` along the way, but the ironclad rule is to do this with a GitHub account prepared exclusively for the agent (do not use your main account).
Regarding the model provider, a DeepSeek API key is not mandatory. Since DSH widely supports OpenAI-compatible model services, it works with keys from other providers as well. However, using a DeepSeek API key is the most standard and easiest way.
Who is it for (and who is it not for)
Recommended for:
- Teams that use a single repository and have an established issue-based development workflow
- Developers who think 'it's a hassle to give detailed instructions every time' and 'want the AI to work autonomously'
- People who want to start with observe mode and gradually expand the scope of automation
Not recommended for:
- Native Windows users (WSL is required)
- People who want to manage multiple repositories across the board (it is for single repositories only)
- People expecting a consumer-grade AI assistant that 'does everything if you just give instructions in chat' (it is completely different)
- People looking for stable operation in a production environment (it is a research prototype)
Summary
`dsh-superagent` is an ambitious research prototype designed under the principle of 'providing as much value as possible while taking up as little of a human's attention as possible.' Its design, including Router/Worker separation, permission control via policies, and independent execution based on tickets, challenges the future of how coding agents should function.
On the other hand, OS limitations, high token consumption, and instability as research-grade code are realistic hurdles. Starting small in a WSL or Linux environment by trying out observe mode is arguably the safest first step.
▼ Learn, run, and use DeepSeek safely in Japanese. 
The practical learning site 'deepseek.ac' publishes materials that allow you to verify the contents of reference books through 
operation and implementation.
▼ Reference Books and Problem Sets
'Guide to Safe DeepSeek Operation'
'Guide to Safe DeepSeek Operation: 70-Question Problem Set'
