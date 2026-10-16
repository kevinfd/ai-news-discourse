---
id: "96432e5dd1ce6136"
title: "66% of billion-dollar companies leave critical bugs unpatched — the part the AI bug-hunting hype leaves out"
url: "https://thenewstack.io/chainguard-mythos-security-harness"
link: "https://thenewstack.io/chainguard-mythos-security-harness"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T05:00:00Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Chainguard has launched an AI-powered security harness that uses frontier models , including Anthropic’s restricted Claude Mythos 5.1, to find and fix exploitable vulnerabilities in application code that conventional scanners miss. \n\n Developers can use Chainguard Harness without direct access to Mythos because Chainguard originally built the tool for its own work with the model as part of…"
tags: ["AI Agents", "CI/CD", "Security"]
orgs: ["Anthropic", "Microsoft"]
topics: ["agents & coding", "models & research", "business & funding", "products & launches"]
content_source: "fulltext"
word_count: 1124
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# 66% of billion-dollar companies leave critical bugs unpatched — the part the AI bug-hunting hype leaves out

The New Stack · Amanda Caswell · 2026-10-14

66% of billion-dollar companies leave critical bugs unpatched — the part the AI bug-hunting hype leaves out
Chainguard has launched an AI-powered security harness that uses frontier models, including Anthropic’s restricted Claude Mythos 5.1, to find and fix exploitable vulnerabilities in application code that conventional scanners miss.
Developers can use Chainguard Harness without direct access to Mythos because Chainguard originally built the tool for its own work with the model as part of Project Glasswing, and the company plans to open Harness up to other frontier models over time rather than keep it tied to a single one.
The company tells The New Stack that Harness has found serious vulnerabilities in codebases that had already undergone extensive security scanning, including software used in critical infrastructure. The first of those findings to go public is a now-patched flaw in vLLM, the open source inference engine, while the critical infrastructure bugs remain under wraps as Chainguard coordinates fixes with upstream maintainers.
Announced Wednesday, Harness leads a four-product launch alongside Workspaces, Checks, and expanded Libraries protections, extending Chainguard’s reach beyond hardened container images and dependencies into agent execution environments and CI verification.
Mythos access without Glasswing
Anthropic has restricted Claude Mythos 5.1 access to organizations participating in Project Glasswing, which puts Chainguard in the position of running Mythos-powered vulnerability research for customers who couldn’t otherwise touch the model.
“We first built Chainguard Harness for our own use of Claude Mythos as part of Project Glasswing,” Chainguard tells The New Stack, adding that Harness “runs on Claude Mythos 5.1 to start, but our goal is for Harness to be model-agnostic, always aligned with frontier AI.”
Harness will also be available through Anthropic’s Claude Marketplace, allowing teams to use existing Anthropic spending commitments rather than secure a separate budget.
“We first built Chainguard Harness for our own use of Claude Mythos as part of Project Glasswing.”
Validating vulnerabilities in vLLM
Chainguard’s first public disclosure from Harness targets vLLM, an open source engine that many teams rely on to serve large language models. In versions before v0.31.0, one client could force the output returned to other clients sharing the same engine, and the tampered response came back looking like a normal, successful completion with nothing written to the logs, a particularly quiet failure mode for anyone running multi-tenant inference.
“Our harness independently found the issue and reproduced it on a clean build,” Chainguard tells The New Stack, noting that the bug is fixed in v0.31.0 and tracked under advisory GHSA-6cxc-2vcg-w5qc. The company added that “a number of other findings, including some in critical infrastructure software, are now being coordinated for disclosure,” and that Chainguard will share details once fixes are in place upstream.
“A number of other findings, including some in critical infrastructure software, are now being coordinated for disclosure,”
Proof before patches
For a tool that leans on an AI model to hunt for flaws, the bigger question is whether those findings hold up, given how much noise AI-generated vulnerability reports can create for maintainers. “Harness proves a vulnerability is exploitable before it counts by reproducing potential exploits in fresh, isolated environments,” Chainguard tells The New Stack, and anything that doesn’t reproduce consistently gets excluded from the report.
Proposed fixes go through the same proof of concept, so the exploit has to succeed against the original code and fail against the patched version before the fix moves forward. A Chainguard engineer then approves every fix and report before it reaches a customer, keeping a human in the loop on what ultimately ships.
“Harness proves a vulnerability is exploitable before it counts by reproducing potential exploits in fresh, isolated environments.”
The AI exploit gap
The launches come alongside The AI Exploit Gap, a Chainguard-commissioned Wakefield Research survey of 1,300 security leaders across nine markets. More than half said their organizations knowingly leave high or critical vulnerabilities unpatched at least sometimes, with the figure reaching 66% at companies with $1 billion or more in revenue, compared with 27% at companies below $250 million.
“AI can find and chain flaws in minutes, while fixing them still moves at human speed and competes with product deadlines and uptime,” Quincy Castro, Chainguard’s chief information security officer, said in a statement. “Patching faster isn’t viable for most folks, and it will consume increasing amounts of resources just to keep pace.”
Isolated microVMs for agents
Each developer and coding agent gets a hardware-isolated microVM with network policies that restrict access to internal systems.
Credentials stay outside the agent’s environment, limiting what a compromised agent or malicious dependency can reach. Signed activity logs record what each agent did so teams can keep an audit trail across multiple autonomous sessions.
CI inside the agent loop
Chainguard Checks lets coding agents run CI checks directly during development and receive signed results in seconds. Agents can run tests, inspect failures, and revise code before opening a pull request, avoiding the CI queues that become harder to manage as vendors like Cognition, Microsoft, and Augment Code turn coding agents into shared team infrastructure running multiple sessions in parallel.
To avoid rebuilding environments on every run, Checks uses warm snapshots with dependencies already installed and refreshes them in the background when the lockfile changes. Each workflow step runs in a separate hardware-isolated microVM built from Chainguard OS packages, including FIPS-compliant toolchains. With Workspaces, agent sessions pause during verification and resume with structured failure logs in context.
Runners never hold long-lived credentials. Instead, a host-side proxy injects short-lived credentials into outbound requests, while declarative egress policies restrict network access and can terminate a microVM if it attempts an unauthorized connection. Successful runs produce signed attestations tied to the execution environment, test results, and commit, which merge gates can verify without rerunning the suite. Checks is available now in beta.
Libraries Lock Down Late-Breaking Bugs
Chainguard Libraries is adding secure package endpoints for Go and .NET, along with CVE remediation for JavaScript and Go, while Java and Python support will expand to cover newly disclosed vulnerabilities discovered through AI-assisted research, including flaws in dependencies that coding agents may have already pulled into a project.
Harness findings will feed directly into that pipeline. When Harness turns up a validated vulnerability in open source software, Chainguard sends it through coordinated disclosure, builds and reviews a patch, and distributes the fixed artifact through Chainguard Repository.
The company’s Athena members get private, hardened patched builds before public disclosure, Chainguard tells The New Stack, while other Libraries customers receive them once the embargo lifts, meaning companies “can stay protected against AI-discovered vulnerabilities immediately upon disclosure.”
The changes build on Chainguard Repository, a policy-enforced endpoint for open source dependencies, and its partnership with Cursor, allowing coding agents to resolve packages through Chainguard’s catalog instead of pulling directly from public registries.
