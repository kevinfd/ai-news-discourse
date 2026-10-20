---
id: "b896b52b5522a89d"
title: "Show HN: Lights-on software factory boilerplate for Claude Code"
url: "https://github.com/gojko/lights-on-software-factory"
link: "https://github.com/gojko/lights-on-software-factory"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-20T01:22:00Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["gojkoa"]
language: "en"
summary: "A starting point for running a lights-on software factory with Claude Code. Based on the setup developed for Votito, where the orchestrator reduced token cost compared to bare-bones Claude workflow execution by around 80%."
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 760
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50160198"
score: 14
comments: 7
community: "Hacker News"
---

# Show HN: Lights-on software factory boilerplate for Claude Code

GitHub · gojkoa · 2026-10-20

A starting point for running a lights-on software factory with Claude Code. Based on the setup developed for Votito, where the orchestrator reduced token spend compared to bare-bones Claude workflow execution by around 80%.
See gojko.net/slides/202609-gotocph.pdf for a quick overview.
The purpose of this repository is to act both as a simple boilerplate setup for new projects, and as an educational demonstration of the core concepts of software factories:
This repository provides setup for:
- A sandbox/container for running Claude Code in a secure environment, sharing only the workspace directory with the host. See CONTAINER.md for more information.
- A deterministic bash command regulator, to reduce approval fatigue and ensure agents execute the commands allowed by project-specific rules. The regulator performs a deep-inspection of bash commands and provides automated approve/deny with instructions on what to do instead if blocked. See REGULATOR.md for more information. Ask Claude to add more custom rules each time it asks you for approval.
- A deterministic linter-based feedback system for enforcing custom domain-specific rules, to help reduce human involvement in code review. A PostToolUse hook runs the linter on every JavaScript file Claude edits, and guides the agents to avoid common mistakes with helpful error messages. Ask Claude to write more custom rules each time you find yourself providing repetitive design/code feedback. Ask Claude to implement custom eslint language parsers for HTML/CSS/other file types. See LINTER-HOOK.md for more information.
- A basic planning/implementation workflow. This is a trivial example intentionally kept simple to demonstrate the format and serve as a foundation for the orchestrator. You should probably replace it with your own commands or more complex rules. See WORKFLOW.md for more information.
- A deterministic multi-agent Claude workflow script generator. Based on the plan produced by the implementation workflow, it creates Claude workflow scripts, structures testing and gates and avoids wasting inference tokens on the mechanical part of workflow orchestration. It speeds up workflow creation and moves many common workflow orchestration tasks from inference (LLM) to deterministic tools (command-line) speeding them up and significantly reducing token spend. See ORCHESTRATOR.md for more information.
The workspace directory contains Claude code setup and a trivial example project.
To set up the container and run a first change, start with GETTING-STARTED.md.
.
├── README.md                    this file
├── GETTING-STARTED.md           first setup and a first change
├── SETTINGS.md                  what settings.local.json wires up
├── LINTER-HOOK.md               the lint hook and custom lint rules
├── REGULATOR.md                 the Bash-command regulator
├── ORCHESTRATOR.md              how the orchestrator works inside
├── WORKFLOW.md                  the user flow, from an idea to a finished run
├── CONTAINER.md                 the container image and the root goals
├── LICENSE
├── makefile                     container goals: docker-image, init, claude, shell, test, lint, root
├── vm/Dockerfile                the container image (Alpine, Node.js, make, git, ...)
├── .gitignore
├── .claude-home/                git-ignored; Claude Code login and history of the container
└── workspace/                   the project; `make claude` starts Claude Code here
    ├── CLAUDE.md                includes CONTRIBUTING.md for Claude Code
    ├── CONTRIBUTING.md          workspace layout, commands and rules
    ├── .claude/
    │   ├── settings.local.json  hooks, env, permissions, preferences
    │   ├── agents/              workflow-worker, workflow-gate, workflow-check
    │   ├── commands/            impact-analysis, plan-execution, execute, regulator
    │   └── workflow/
    │       ├── README.md        plan notation and generator reference
    │       ├── package.json     {"type": "module"} for the tooling
    │       ├── bin/             hook entries and command-line tools
    │       ├── src/
    │       │   ├── regulator/   regulator engine, rules.js, rules/
    │       │   ├── generator/   plan validator and workflow generator
    │       │   ├── lint/        eslint plugin, two rules, lint hook logic
    │       │   └── transient-dir.js
    │       └── tests/           tests for all of the tooling
    ├── plans/                   plans, sidecars and progress records
    ├── src/format-greeting.js   sample module (replace it)
    ├── tests/format-greeting.test.js
    ├── eslint.config.js
    ├── makefile                 init, test, lint and the two workflow gate goals
    ├── package.json
    ├── package-lock.json
    └── .gitignore
- GETTING-STARTED.md — start here: set up the container, start Claude Code and run a first change.
- SETTINGS.md — the hooks, environment, permissions and
preferences in workspace/.claude/settings.local.json.
- LINTER-HOOK.md — the lint-on-edit hook, the two example rules and how to write a rule.
- REGULATOR.md — how the regulator decides, the roles, the notable rules, diagnosing a decision, configuring it and adding a rule.
- WORKFLOW.md — the user flow: /impact-analysis, /plan-execution, /execute, watching and resuming a run, /regulator, and
a worked example.
- ORCHESTRATOR.md — how the orchestrator works inside: the pieces, the bins, the agents, the gate goals, progress and resume.
- CONTAINER.md — the container image, the root goals, mounts,
overrides, keeping node_modules in the container, troubleshooting.
- workspace/.claude/workflow/README.md — the plan notation, the run shape, the answer schemas and the fault list.
MIT. See LICENSE.
