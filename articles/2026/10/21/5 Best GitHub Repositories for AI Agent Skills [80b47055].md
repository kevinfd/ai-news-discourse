---
id: "80b47055a2342f6b"
title: "5 Best GitHub Repositories for AI Agent Skills"
url: "https://kdnuggets.com/5-best-github-repositories-for-ai-agent-skills"
link: "https://kdnuggets.com/5-best-github-repositories-for-ai-agent-skills"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-10-21T12:00:00Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Abid Ali Awan"]
language: "en"
summary: "Explore five popular AI agent skill collections that help coding agents plan, test, debug, review, and build better software."
tags: []
orgs: ["Anthropic", "Cursor", "Google", "Microsoft"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1453
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/awan_5_best_github_repositories_ai_agent_skills_1.png"
discussion_url: null
score: null
comments: null
community: null
---

# 5 Best GitHub Repositories for AI Agent Skills

KDnuggets · Abid Ali Awan · 2026-10-21

5 Best GitHub Repositories for AI Agent Skills
Explore five popular AI agent skill collections that help coding agents plan, test, debug, review, and build better software.
AI coding agents such as Claude Code, Codex, Cursor, and OpenCode have become very good at writing code. But software engineering is much more than that.
You still need to understand requirements, plan features, write tests, debug problems, review changes, and know when something is ready to ship.
This is where AI agent skills come in. They are reusable instructions and workflows that teach agents how to handle specific tasks without you having to explain the same process every time.
In this article, we will look at five popular open-source collections:
- Superpowers by Jesse Vincent (⭐285.5K)
- Skills for Real Engineers by Matt Pocock (⭐260.1K)
- ECC by Affaan (⭐256.7K)
- Awesome LLM Apps by Shubham Saboo (⭐137.3K)
- Agent Skills by Addy Osmani (⭐93.6K)
Each takes a slightly different approach to making coding agents more useful for real software development.
1. Superpowers by Jesse Vincent
Superpowers is one of the most popular agent skill projects on GitHub. Created by Jesse Vincent and the team at Prime Radiant, it is a software development methodology for coding agents, built from a collection of reusable skills.
The important word here is methodology.
Instead of simply giving your agent more abilities, Superpowers changes how it approaches software development.
Its skills cover things like:
- brainstorming
- implementation planning
- test-driven development
- systematic debugging
- Git worktrees
- parallel agents
- code review
- verification
For example, if you ask the agent to build a feature, it first uses brainstorming to understand what you actually want. After the design is approved, it creates a plan, implements it using subagents or plan execution, follows test-driven development (TDD), reviews the code, and verifies everything before finishing the branch.
Debugging follows the same idea. The systematic-debugging skill uses a structured root-cause process instead of letting the agent randomly change code until something works.
This is what makes Superpowers interesting. You are not just installing another prompt or tool. You are basically giving your coding agent a proper software development process.
For Claude Code, you can install it with:
/plugin install superpowers@claude-plugins-official
It also supports Codex, Cursor, Gemini CLI, OpenCode, GitHub Copilot CLI, Kimi Code, Antigravity, and several other coding environments.
2. Skills for Real Engineers by Matt Pocock
Matt Pocock takes a slightly different approach with Skills for Real Engineers, a collection of agent skills he says he uses every day for real engineering, not vibe coding.
Instead of trying to control the entire development process, the skills are designed to be small, adaptable, and composable. You can use the ones you need and combine them into your own workflow.
Some of the most useful include:
- grill-me
- grill-with-docs
- to-spec
- to-tickets
- implement
- tdd
- diagnosing-bugs
- code-review
- research
- domain-modeling
- improve-codebase-architecture
- handoff
One of my favorites is grill-with-docs. Instead of letting the agent guess what you want, it interviews you about the change while building a shared domain model, improving terminology, and updating project documents such as CONTEXT.md and ADRs.
Then you have skills like tdd, which follows the classic red-green-refactor loop, and diagnosing-bugs, which gives the agent a structured debugging process instead of letting it randomly try fixes.
For larger work, you can even build a workflow like:
grill-with-docs → to-spec → to-tickets → implement → code-review
The repository itself documents this as its main multi-session development chain.
You can install the skills with:
npx skills@latest add mattpocock/skills
The installer lets you choose which skills you want and which coding agents to install them on. It copies the files into your project, so you can edit them to match the way you like to work. Matt recommends also installing and running setup-matt-pocock-skills once for each repo.
If Superpowers feels like installing a complete engineering methodology, Matt Pocock's collection feels more like borrowing the workflows of an experienced engineer and picking the ones that work for you.
3. ECC by Affaan
ECC by Affaan Mustafa is the biggest collection in this list in terms of raw capabilities.
It goes beyond a normal folder of SKILL.md files and combines skills, specialized agents, rules, hooks, memory, continuous learning, security tools, and integrations for different coding agents.
The current repository includes:
- 292 skills
- 68 specialized agents
- 94 command shims
- memory across sessions
- continuous learning
- AgentShield security scanning
Its skills cover TDD, research, frontend development, machine learning, security, operations, architecture, testing, and agent orchestration.
Affaan describes its workflow like this:
plan → test → implement → review → verify → remember → improve
The last two steps are what make it interesting. ECC can preserve useful context across sessions and turn repeated patterns into reusable skills and learned behaviors.
It also includes AgentShield, which scans agent configurations for things like secrets, risky permissions, hooks, MCP settings, and prompt-related security issues.
You can install it with:
npx ecc-universal@2.2.1 setup
Or use the guided installer:
npx ecc-universal@2.2.1 install --guided
Claude Code currently has the strongest integration, with support for Codex and varying levels of support for Cursor, OpenCode, Kimi Code, Gemini, and other coding agents.
ECC is probably overkill if you only need a better debugging prompt. But if you want your coding agent setup to behave more like a complete engineering platform with memory, security, and specialized workers, it is one of the most ambitious options available.
4. Awesome LLM Apps by Shubham Saboo
Shubham Saboo's Awesome LLM Apps is a little different from the other repositories on this list.
Instead of focusing only on skills, it contains 100+ open-source AI agents, agent skills, and RAG applications built around models such as GPT, Claude, Gemini, DeepSeek, Llama, and Qwen.
That broader scope is what makes it interesting. You can see how agents, tools, retrieval, multiple models, and skills are actually combined into working applications.
Its Agent Skills collection includes:
- Project Graveyard: finds abandoned projects and helps decide which one is worth finishing
- Scope Creep Detector: checks whether a code change has grown beyond its original goal
- Commit Archaeologist: uses Git history to understand why code exists
- Self-Improving Agent Skills: automatically tests and improves agent skills
- Advisor Orchestrator Worker: splits larger tasks across an orchestrator, advisor, and workers
For example, you can install Project Graveyard with:
npx skills add https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/project-graveyard
It scans your local Git repositories, looks at their history, identifies why projects were abandoned, and suggests which one may be worth bringing back.
5. Agent Skills by Addy Osmani
Addy Osmani's Agent Skills focuses more directly on production software engineering.
The collection organizes its workflows around six stages:
DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP
It currently contains 24 skills covering requirements, planning, TDD, frontend development, API design, debugging, security, performance, code review, CI/CD, observability, documentation, and shipping.
There are also lifecycle commands such as /spec, /plan, /build, /test, /review, and /ship, which load the appropriate workflows for each stage.
One part I particularly like is its focus on quality gates. The constraint-driven-development skill lets you define things like testing, linting, security, coverage, and performance requirements, while placing expensive checks later in the workflow instead of running everything after every edit.
Install the full collection with:
npx skills add addyosmani/agent-skills
Or browse the skills first:
npx skills add addyosmani/agent-skills --list
You can also install individual skills:
npx skills add addyosmani/agent-skills --skill test-driven-development
The Skills CLI supports 70+ coding agents, including Claude Code, Cursor, Codex, Copilot, and Cline.
Final Thoughts
After going through these collections, what I like most is how different the approaches are.
Superpowers gives you a full engineering methodology, Matt Pocock keeps things small and composable, ECC turns the coding agent into more of an engineering platform, Awesome LLM Apps focuses on experimentation, and Addy Osmani brings everything back to production-quality software.
For me, the best approach is not to install everything. I would pick the workflows that actually match how I work, test them on real projects, and then customize the SKILL.md files over time.
That is where agent skills become really useful: you are not just making the agent smarter, you are teaching it how you want software to be built.
Abid Ali Awan (@1abidaliawan) is a certified data scientist professional who loves building machine learning models. Currently, he is focusing on content creation and writing technical blogs on machine learning and data science technologies. Abid holds a Master's degree in technology management and a bachelor's degree in telecommunication engineering. His vision is to build an AI product using a graph neural network for students struggling with mental illness.
