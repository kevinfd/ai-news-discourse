---
id: "4506b9f639370308"
title: "Anthropic says Claude writes and reviews 90% of its team’s code. The catch is how it checks the work."
url: "https://thenewstack.io/anthropic-claude-code-verification"
link: "https://thenewstack.io/anthropic-claude-code-verification"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-20T16:41:28Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Anthropic says Claude writes and reviews roughly 90% of the code produced by the team building Claude Code, and the company has spelled out how it verifies that work without making engineers inspect every change. \n\n In a Monday engineering post , Anthropic technical staff member Addy Osmani describes a verification system built to support dozens or even hundreds of concurrent agents, where…"
tags: ["AI Agents", "Developer tools", "Software Testing"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "search & media"]
content_source: "summary"
word_count: 1003
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic says Claude writes and reviews 90% of its team’s code. The catch is how it checks the work.

The New Stack · Amanda Caswell · 2026-11-20

Anthropic says Claude writes and reviews roughly 90% of the code produced by the team building Claude Code, and the company has spelled out how it verifies that work without making engineers inspect every change. 

 In a Monday engineering post , Anthropic technical staff member Addy Osmani describes a verification system built to support dozens or even hundreds of concurrent agents, where automated checks supply the evidence engineers need to judge what those agents produce. 

 The approach has attracted scrutiny from developers , much of it centered on the cost of model-driven verification and whether cheaper deterministic tooling could shoulder some of that load instead. 

 In response to questions from The New Stack , Anthropic walked through how it controls inference costs, stops agents from manipulating tests, and gauges whether its automated reviewers actually work. 

 Testing AI code live 

 The company has Claude exercise its changes inside a running application, leaning on browser automation for web apps, MCP-connected simulators for mobile builds, and local services for backend work. 

 Those instructions live in repository-specific verification skills under . claude/skills/ , so an agent can run and check its own changes before it ever commits them. 

 Osmani also points developers toward property-based testing to flush out edge cases, along with differential testing to surface unanticipated behavior changes between an old implementation and a new one. 

 Keeping verification costs down 

 Not everyone is convinced the math works. Some developers questioned whether the extra inference costs were justified, and Hacker News commenter OtherShrezzing argues that reusable Playwright tests could handle much of the verification without repeatedly calling a model. 

 Anthropic tells The New Stack that inference costs swing considerably from one change to the next, and that it keeps them down by running the cheap, deterministic checks before any model gets involved. 

 “Deterministic checks like the build, linters, unit tests and property tests go first, because once Claude writes them they run as ordinary software and cost very little to rerun,” Anthropic tells The New Stack . 

 “Model review is for what a test can’t answer, like whether a change takes the right approach or misses a case nobody wrote a test for.” 

 “Model review is for what a test can’t answer, like whether a change takes the right approach or misses a case nobody wrote a test for.” 

 Anthropic would not put a specific figure on the added inference cost of model-based verification. 

 Stopping agents gaming tests 

 Hacker News user xnorswap raised a different worry: agents quietly reshaping code to get a failing test to pass. 

 “It’s not the per-run costs I worry about, it’s the costs of churn,” xnorswap writes, warning that an agent might rewrite the test or bolt on a workaround instead of fixing the underlying problem. 

 Anthropic has set rules for how Claude handles failing tests and, just as important, which parts of the repository its reviewer can trust. 

 “Our rule is that if a change can modify the check that judges it, the check is broken.” 

 “Our rule is that if a change can modify the check that judges it, the check is broken,” Anthropic tells The New Stack . 

 In practice, Code Review reads REVIEW.md from the base branch rather than from the changes introduced in a pull request, and any review result counts only for the exact commit it examined. 

 Claude is barred from skipping flaky tests, slipping in sleeps, or rerunning a test until it passes; when the agent can’t pin down the root cause, it deletes the test outright and documents why. 

 The team also logs how each commit was verified, including the cases where no verification happened at all. 

 Turning old bugs into guardrails 

 Of the 39 reliability checks the Claude Code team has accumulated, Claude typically runs only three to ten per change. For changes to session storage, for example, Claude checks whether older transcripts still load with –resume. 

 Commit gates require developers to verify changes through /code-review or /verify . Teams can monitor compliance before making the checks mandatory, and developers can bypass a gate if they explain why. 

 Anthropic tells The New Stack that between June and September, the number of merged pull requests to Claude Code’s codebase more than doubled, while the proportion of changes that had to be reverted fell by more than 40%. 

 The company did not say how much of that improvement came from its verification loops or provide separate figures for production defects and regressions. 

 Grading the code reviewers 

 To check its own reviewers, Anthropic grades them against historical incidents and reverts, recreating the repository as it existed at the moment of review and writing a one-sentence answer key for each case, with a reviewer earning credit only when its finding actually describes the bug in question. 

 Previously merged changes that stayed stable act as controls for catching false positives, and the company keeps a fixed test set walled off from the examples it uses to tune the reviewers. 

 Anthropic measures recall at several stages of the review pipeline, and even a reviewer that catches a genuine bug is scored as a miss if the finding never reaches an engineer. 

 The company says it does not currently publish the false-positive or false-negative rates from those Code Review evaluations. 

 Where engineers still earn their keep 

 Anthropic’s approach offers a framework for deciding which checks require model inference, and which deterministic tools can handle more cheaply . Without published reviewer error rates or detailed inference costs, however, developers have little data against which to benchmark their own implementations. 

 “A person is accountable for every change that ships, whoever typed it” 

 “A person is accountable for every change that ships, whoever typed it,” Anthropic tells The New Stack. 

 Engineers review the verification evidence, including test results and screenshots. If a check still fails after three rounds, Claude hands the problem to an engineer. 
 The post Anthropic says Claude writes and reviews 90% of its team’s code. The catch is how it checks the work. appeared first on The New Stack .
