---
id: "a6d418b7bd60b0f5"
title: "GitHub debuts Copilot Fusion, a new model selection & orchestration system that beats Claude Code for half the API cost"
url: "https://thenewstack.io/github-copilot-fusion"
link: "https://thenewstack.io/github-copilot-fusion"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T16:19:31Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Meredith Shubel"]
language: "en"
summary: "GitHub has debuted GitHub Copilot Fusion , a new system that handles model selection and orchestration for coding tasks so developers don’t have to.  \n\n Combining the advanced runtime model orchestration from Project HydraFusion with Copilot Auto Model Selection , Copilot Fusion can now handle both model selection and orchestration. GitHub says Fusion Max delivered comparable benchmark…"
tags: ["AI Models", "Developer tools", "Software Development"]
orgs: ["Microsoft", "Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 746
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# GitHub debuts Copilot Fusion, a new model selection & orchestration system that beats Claude Code for half the API cost

The New Stack · Meredith Shubel · 2026-10-28

GitHub debuts Copilot Fusion, a new model selection & orchestration system that beats Claude Code for half the API cost
GitHub has debuted GitHub Copilot Fusion, a new system that handles model selection and orchestration for coding tasks so developers don’t have to.
Combining the advanced runtime model orchestration from Project HydraFusion with Copilot Auto Model Selection, Copilot Fusion can now handle both model selection and orchestration. GitHub says Fusion Max delivered comparable benchmark performance to Claude Code with Opus 5.5 Max at about half the average API cost and in about 40% less time per task.
Generally available now, GitHub Copilot Fusion is part of GitHub’s new vision to make GitHub “the most comprehensive software delivery system in the world,” with developers delegating model choices while retaining responsibility for the direction and outcome of the work.
GitHub announced the news on Wednesday at GitHub Universe in San Francisco, the company’s flagship developer event.
GitHub Copilot Fusion is the decider now
For tasks involving reasoning, code generation, debugging, or tool use, GitHub says developers can delegate decisions about which models to use and how they work together. Its instructions: “choose Copilot Fusion and let Copilot intelligently route and orchestrate which models it uses for you.”
That sounds like a time-saver, since different tasks benefit from different models based on capabilities and cost. With Copilot Fusion working as the “model picker,” developers don’t have to weigh performance and price for every task.
More compelling is the idea that developers can use Copilot Fusion to strategically switch models mid-workflow, letting the system jump between models based on what best suits each step.
After analyzing what the task requires and choosing a model, the system orchestrates the next steps based on what makes the most sense. That may be a single model doing everything, a “cascading” workflow where a quality check evaluates one model’s response and then decides to accept it or escalate it, or a “critique” workflow where one model reviews another’s work.
That could reduce the mental load for developers who may inadvertently choose inefficient models when their attention drifts.
As Hari Pokhrel, principal software engineer at AT&T, describes in a statement for GitHub: “Previously, developers would often choose a more powerful model for a complex task and forget to switch back for everyday activities.”
So, what do developers get to decide for themselves?
Mostly, the effort level.
While Copilot Fusion handles model selection and orchestration, developers choose the effort level: Fusion Standard for everyday coding; Fusion High for more challenging tasks and deeper reasoning; Fusion Max for the most demanding, complex work.
That’s if you’re free and comfortable letting GitHub’s systems take the lead. If you prefer, developers can implement other controls.
Per GitHub, enterprise administrators can control which models Copilot Fusion can choose from, disabling certain models for Copilot Fusion without disabling them for the entire developer team. Administrators can also adjust the policy state for each model independently and set whether Copilot Fusion is or isn’t the default model for Copilot users.
The case for letting Copilot Fusion be your guide
According to GitHub and Pokhrel’s statement, offloading model selection and orchestration to the new fusion system is the smarter route for developers, letting you balance performance and cost without the friction of choosing between models.
GitHub says it has improved performance since launching Project HydraFusion as a research preview in September 2026. On the Artificial Analysis Coding Agent Index, GitHub reports that Copilot Fusion Max scored 60, within two points of Claude Code with Opus 5.5 Max. GitHub says Fusion Max delivered that result at about half the average API cost per task, using about half as many tokens and taking about 40% less time per task.
In the statement supplied to The New Stack by GitHub, Pokhrel credits Copilot Fusion Standard with improving token efficiency at AT&T, reducing unnecessary spending, and preserving capacity for higher-value work.
Model routing is becoming the default
Copilot Fusion is one piece of GitHub’s future vision, released alongside a slew of other products at the conference, including the GitHub Copilot app, Copilot Projects, and Copilot Automations.
By deferring model selection to its system, GitHub thinks developers will have more time and brainspace to focus on other work.
It looks like everyone is moving that way. This month, Ramp described moving model selection into Open SWE, its open-source coding agent. In the summer, Replit did the same, making its “intelligent model routing” system the default across every account.
