---
id: "308de0a981a504cd"
title: "DeepSeek’s Super-agent starts work on its own, and treats your team’s attention as the budget"
url: "https://i-scoop.eu/deepseek-super-agent"
link: "https://i-scoop.eu/deepseek-super-agent"
source: "i-SCOOP"
domain: "i-scoop.eu"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-01T01:21:00Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Tom Cuylaerts"]
language: "en"
summary: "DeepSeek's open Super-agent starts work on its own but guards your team's attention. How it works, what it costs, GDPR and six controls to copy."
tags: []
orgs: ["DeepSeek", "Anthropic", "ByteDance"]
topics: ["agents & coding", "models & research", "products & launches", "jobs & society"]
content_source: "fulltext"
word_count: 1682
paywalled: false
image: "http://www.bing.com/th?id=ONUT.1YtXXJyvdRV1XTmGFp9P-Q&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# DeepSeek’s Super-agent starts work on its own, and treats your team’s attention as the budget

i-SCOOP · Tom Cuylaerts · 2026-11-01

DeepSeek has open-sourced a coding agent that does not wait to be asked. Published on 31 October as dsh-superagent-prototype, it listens to a GitHub repository and picks up work when an allowed person requests it, or when a rule the team wrote permits it. It does the job in its own session and replies in the original conversation, usually with a pull request. The more important release is the design principle behind it: take as little human attention as possible, and give as much value as possible.
That principle turns attention into a budget the agent has to justify spending, and it gives organisations a concrete template for governing agents that act on their own.
What DeepSeek released
The dsh-superagent-prototype repository is MIT-licensed and packaged as a bundle for DeepSeek Harness, the open agent runtime DeepSeek launched in August. It covers one GitHub repository per installation, with Feishu, ByteDance’s workplace chat app, as an optional second source.
DeepSeek labels it a research prototype for reference, not an official product, and says much of the engineering was done by coding agents. It differs from the version DeepSeek runs internally and from the design essay the DeepSeek Harness team published on WeChat the same day. According to that essay, internal instances already run continuously, reproducing and fixing issues, responding to code review and contributing to DeepSeek Harness itself. Bloomberg frames the release as an attempt to challenge Anthropic’s Claude Code.
Why attention is the real constraint
The essay starts from an observation: a person can usually follow only three to five active sessions at once, as IT之家 reported. Model capability sets how well a single task goes. Human attention sets how many tasks move forward at the same time. Anyone running several agents in parallel tabs knows the result: the bottleneck is the person switching between them.
DeepSeek’s answer is a two-layer design. A resident router talks to people, keeps context across tasks and dispatches work. Workers each own one task in isolation, typically on the strongest model, and report to the router instead of messaging people in chat. On GitHub they do open the pull request and answer review comments themselves.
The philosophy document turns the principle into rules of conduct. The agent acts only on a direct request from an allowed person or under a written team rule. It confirms a request once, stays quiet while working, and speaks again only when a result is ready, a decision is needed or it cannot finish. It asks one question at a time. It stops by impact rather than effort, so a change that needs a design decision ends in a clear question rather than a guess. Every message, setting and even paragraph of documentation has to give more value than the attention it costs, or it goes. The document closes with a line any agent buyer could adopt: “the right help at the right time, and nothing at any other time.”
How a request travels from message to pull request
- A source produces an event: a GitHub issue, pull request, comment or a CI result on the default branch, or a Feishu message.
- Code applies a gate, then a model assesses. The host checks whether the sender is on the allowed list, addresses the agent, or posts where the team’s admission table allows it. Bots can never make an explicit request; only bots the team lists can at most produce a candidate for proactive work.
- Accepted work becomes a Ticket with a Mandate. The Mandate is immutable and records the policy version, the scope, the matched rules and the sender’s identity. Wider scope means a new Ticket.
- A worker session runs it in its own directory, typically a git worktree. By default there are three worker slots, plus one reserved so a person’s follow-up never waits behind new work.
- The reply goes back to the same conversation. By default its prompts make every GitHub message start with a line saying it comes from an automated agent, not a human. The agent never enables auto-merge with its own account; that needs a separate merge account named in the team’s delivery rules.
Proactive, but on probation first
Headlines about an agent that works “without being summoned” are accurate, with a caveat that matters for governance. Unrequested work needs at least one rule the team wrote, and the authorisation document defines three accept modes:
- off: only explicit requests are handled;
- observe, the default: candidates that match a rule are assessed and logged as “would accept”, but nothing happens;
- auto: a positive assessment starts the work.
DeepSeek recommends starting in observe, reviewing the recorded decisions and only then switching to auto. Internally it used a rule to silently reproduce reported bugs and speak only once an issue was confirmed and a simple fix was ready. In one case, according to the essay, the agent opened a fix while members of a group chat were still discussing the bug.
The operator owns the output, because the agent posts under accounts the team sees every day. DeepSeek’s advice is blunt: start with a short allowed list, make prompts shorter and stricter when the agent gets noisy, and never use it to produce volume.
The trade-off in DeepSeek’s own numbers
The essay includes a first synthetic test: about 300 messages, roughly 20 of them work requests, five runs per setup. Timings were scaled to a quarter and the coding work was simulated, so the test measures coordination, not code quality.
The Super-agent took a median of 12.4 minutes per task from request to result, with a 95th percentile of 15.7 minutes. A single session that may spawn subagents took 20.4 and 29.5 minutes with a neutral prompt, under which the model never delegated, and 13.8 and 29.0 minutes with a prompt that encourages delegation. The clearest gain is in the slow tail, according to AgentsPulse, with the headline figures also reported by ChinaModelAPI.
The cost is compute. The Super-agent read 23.2 million cached tokens per run: about twice a single session that delegates and close to four times one that does not, and 37% more again without direct delivery of follow-ups to the worker. DeepSeek calls the results preliminary, and they are its own measurements.
Six design choices worth copying for any agent
You do not need to run DeepSeek’s code to use its design. The same controls apply to Claude, Copilot or in-house agents that act inside your systems.
Whether Article 50(1) formally applies to an internal coding agent depends on your role and context, but keeping the disclosure line costs nothing. See also our piece on why every organisation now needs an agent policy.
Where your code and conversations go
The agent itself runs on your machine, but the reasoning happens wherever your model provider sits. DeepSeek Harness defaults to DeepSeek’s API and also supports Anthropic, OpenAI and OpenAI-compatible or local endpoints. Code, issue threads and the names in them go to the provider you configure.
For European teams that choice carries weight. DeepSeek’s privacy policy states that it processes and stores personal data in China. Italy’s data protection authority restricted the DeepSeek chatbot in January 2025, Berlin’s regulator said in June 2025 that the app breaches Article 46(1) GDPR and reported it to Apple and Google, and Belgium’s authority opened an investigation in early 2025 after a complaint by Testaankoop. Those cases concern the consumer app, but they point to the same transfer question for the API. Pairing the harness with a European or self-hosted model sidesteps the transfer to China.
Security deserves the same attention. Workers run commands without approval, with full access as the operator’s operating-system user, and can read that user’s home directory. Blocked commands are not a security boundary. The deployment guide itself recommends a dedicated OS account holding only the agent’s credentials.
What is still missing
The open prototype is smaller than the essay. The watchdog that checks whether each worker is making real progress, and the split that puts the agent loop and its state in the cloud while commands run on your own machine, are directions, not code. It supports only github.com, not GitHub Enterprise Server, and needs a regular GitHub user account for the agent.
Commentators in China raised the sharper point: the essay says little about how often the event filter gets it wrong, and workers have authority but no budget or supervision. A run of bad pull requests would consume exactly the attention the system is meant to save. That echoes what we saw with agentic code review at Entire and in research showing AI makes developers faster but not their teams.
A 30-day pilot for teams that want to try it
Frequently asked questions
Is dsh-superagent free?
The code is free under the MIT licence. You pay for the model behind it, and DeepSeek’s own test shows the design uses more tokens than a single session.
Can it run on Claude, GPT or a local model?
Yes. It uses the default model of your DeepSeek Harness profile, which can point to Anthropic, OpenAI or any OpenAI-compatible endpoint, including local ones.
Does it work with GitLab, Slack or Teams?
Not out of the box. The open version supports github.com and Feishu, and a cookbook explains how to add another source.
Will it merge code on its own?
Not by default. Auto-merge needs the team to name a separate merge account in the delivery rules, and it is an instruction to the agent rather than a hard control, so use branch protection if you need one.
Count the interruptions, not the features
Agent evaluations still focus on capability: benchmarks, tool counts, how many tasks run in parallel. DeepSeek’s prototype suggests a second metric that belongs in every procurement checklist and pilot report: interruptions per finished task. It applies just as well to proactive assistants such as Claude Duet. An agent that does a lot but keeps pulling people out of their work has not saved time. It has moved the cost to the people who now have to watch it.
