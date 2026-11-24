---
id: "43b498f2b7e3dbe0"
title: "Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes"
url: "https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes"
link: "https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-23T22:05:50Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Sarah Perez"]
language: "en"
summary: "As AI-generated code piles up, Anthropic's new developer tools aim to eliminate another bottleneck by letting agents handle routine approvals."
tags: ["AI", "Anthropic", "Claude", "code", "coding"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 460
paywalled: false
image: "http://www.bing.com/th?id=ONUT.LiMwYhuk0qrlYFIa3IlYdg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes

TechCrunch · Sarah Perez · 2026-11-23

Anthropic is moving from having Claude write code to helping developers decide when that code is ready to ship. On Monday, the newly public AI company announced the launch of Claude Ship, a suite of AI agents for automating code reviews, fixes, and approvals of routine code changes.
The latter is the more interesting part of this new set of tools, as AI coding tools already offered code review features before now. What’s notable about Claude Ship is not just that it can review proposed code changes and identify and address problems, but that it also includes an agent that can approve code changes automatically based on policies set by a development team.
The launch arrives at a time when AI coding agents have become increasingly capable of generating substantial amounts of code, leading to bottlenecks in reviewing and approving the code changes before they go live. With Claude Ship, the idea is to automate even more of the work involved in the development process, essentially by delegating approval authority to an AI agent itself.
“Most teams want a person to approve every change, and that’s easy to keep up with when people write every line. But a lot of developers build with agents now,” a company blog post explains. “On the Claude Code team, Claude writes most of our code, and we wanted everything after the PR to move that fast too.”
Claude Ship is launching in beta, allowing early adopters to use it to review pull requests (PRs), and then decide what’s ready to merge.
The new offering consists of Code Review, which is already generally available, and two new agents now in beta: PR Steward and Claude Approvals. PR Steward focuses on addressing issues such as failing CI checks, merge conflicts, and feedback from Code Review. It also comments after every push on what it changed and how to roll it back, if needed.
Claude Approvals then applies an approval policy that the team writes as a file in the repository. This approval process can incorporate various signals, including Code Review findings or the company’s own classifiers, with policies written in natural language.
Because the offering is still in beta, Anthropic suggests running the approval functionality in observe-only mode first. Teams can also choose to start with just one repository and set monthly spending limits to have more control over the process.
Anthropic says teams will also still remain in control of where Claude Ship runs, which review settings to use (e.g., Quick, Standard, or Deep), and which changes should be escalated to a human for a decision.
Claude Ship is rolling out to Claude Team and Enterprise plans for repositories on GitHub. Code Review is generally available, while PR Steward and Claude Approvals are in beta.
