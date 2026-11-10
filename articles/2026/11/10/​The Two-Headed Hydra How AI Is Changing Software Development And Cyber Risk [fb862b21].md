---
id: "fb862b21d50e8028"
title: "​The Two-Headed Hydra: How AI Is Changing Software Development And Cyber Risk"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/10/the-two-headed-hydra-how-ai-is-changing-software-development-and-cyber-risk"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/10/the-two-headed-hydra-how-ai-is-changing-software-development-and-cyber-risk"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-10T11:15:00Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Ken Ammon, Forbes Councils Member"]
language: "en"
summary: "That is why security teams need the ability to make an enforceable decision before execution."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "products & launches", "safety & ethics", "chips & infrastructure"]
content_source: "fulltext"
word_count: 815
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6aee13b3f772abe72a1c0c08/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# ​The Two-Headed Hydra: How AI Is Changing Software Development And Cyber Risk

Forbes · Ken Ammon, Forbes Councils Member · 2026-11-10

Ken Ammon is CEO of CodeHunter, a serial entrepreneur who exited OPĀQ and NetSec, and former U.S. Air Force captain at the NSA.
It sounds like a security nightmare, but it is quickly becoming operational reality: The same AI capabilities helping enterprises build software faster now help adversaries attack it faster.
AI coding tools and development agents are now part of the software delivery process. They help developers write scripts, update dependencies, troubleshoot builds, generate tests and move code through workflows with less manual effort. Attackers are using the same class of capabilities to build malicious software more efficiently.
They can automate reconnaissance, generate exploit code, test evasive variations and tailor malware to a target environment with ease. AI is now accelerating enterprise software development and software-based attacks at the same time.
Meanwhile, AI-driven malware undermines the signals security teams have historically used to make trust decisions. Source, signing, provenance, dependency scans and reputation remain important, but become unreliable when attack code has never been seen before, is short-lived and designed to change.
These indicators do not prove what code will do when it runs. Post-execution detection has the same limitation with worse timing. By the time suspicious behavior is visible, the artifact may already have accessed credentials, modified system settings or established persistence.
The more durable signal is behavior, and the most important decision point is whether that behavior should be allowed before execution.
Software Execution As A Control Point
We are already seeing why. Recent npm supply chain campaigns show how quickly malicious packages can move into developer environments and CI/CD workflows. Some packages are designed to steal cloud and build credentials. Others profile developer machines or abuse dependency confusion to blend into normal package resolution. The attack path is familiar to any security team: A package looks useful, gets pulled into a workflow, runs during installation or build and inherits the permissions of the environment that executed it.
AI raises the pressure on traditional security models because it reduces the cost of variation. Attackers can generate more package names, alter payloads, test different install behaviors and adapt code faster than a team can manually review each artifact.
The same dynamic applies inside the enterprise. AI coding tools and development agents can generate scripts, modify files, recommend dependencies and issue commands as part of normal software workflows. In many cases, a human still approves the pull request or reviews the output. In other cases, the review is shallow because the pipeline is moving fast and the AI-produced change looks routine.
That is where the risk concentrates. A generated script may complete the requested task while also introducing access the organization did not intend. A dependency update may solve a build issue while bringing in a package with dangerous install-time behavior. A container may pass through a pipeline while carrying logic that should never run in production. The issue is not whether the code was created by an employee, an AI assistant or an attacker. The issue is what the code is capable of doing when it executes.
Behavior Remains A Reliable Security Signal
The form of an attack can keep changing while its objective stays the same. A package may be renamed, a payload may produce a new hash, and a script may be rewritten each time a model is prompted. But code still has to act to achieve its purpose. If the goal is credential theft, persistence, external communication or unauthorized system change, those behaviors eventually have to show up. That is why security teams need the ability to make an enforceable decision before execution.
The goal is not to slow development by forcing manual review of every artifact, but to identify where code gains meaningful execution rights and put an enforceable decision point in front of those paths before it runs.
A good starting point is developer workstations, CI/CD runners, package managers, build identities, deployment scripts, container promotion paths and automation jobs. This is where code often inherits trust from the person, tool or service account that launched it. A package running on a developer laptop is one level of risk. A package running in a build system with access to signing keys, cloud credentials or production deployment rights has a much bigger security blast radius.
The control point should focus on behavior before execution. If an artifact is about to run in a sensitive environment, the organization should know what it is capable of doing. Will it attempt to access secrets, create persistence or make unauthorized system changes? When the behavior falls outside policy, code execution should be prevented, restricted, isolated or the artifact sent for review before it is allowed to run.
This approach is not new. Zero trust is already used to assess users, devices, sessions and workloads before access is granted. By moving the trust decision closer to execution, we can apply the same discipline to code.
