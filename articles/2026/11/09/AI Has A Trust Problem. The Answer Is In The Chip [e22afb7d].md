---
id: "e22afb7d32788026"
title: "AI Has A Trust Problem. The Answer Is In The Chip"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/09/ai-has-a-trust-problem-the-answer-is-in-the-chip"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/09/ai-has-a-trust-problem-the-answer-is-in-the-chip"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-09T11:00:00Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Ayal Yogev, Forbes Councils Member"]
language: "en"
summary: "The deciding factor isn’t whether an organization adopts AI, but whether its trust model can be verified rather than assumed.​​"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Anthropic", "Google", "Hugging Face"]
topics: ["agents & coding", "models & research", "chips & infrastructure", "policy & regulation"]
content_source: "fulltext"
word_count: 1027
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6aece3ce14de772b4a2ca9cf/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# AI Has A Trust Problem. The Answer Is In The Chip

Forbes · Ayal Yogev, Forbes Councils Member · 2026-11-09

Ayal Yogev is the CEO and co-founder of Anjuna Security.
The release of Claude’s Mythos model was a warning: AI can’t be ignored or fully trusted. At least not yet. 
In April, Anthropic gave approximately 50 companies that build or maintain critical software access to Mythos, its new model, through Project Glasswing. Within weeks, Mythos found a 27-year-old OpenBSD vulnerability, plus a bug in FFmpeg that five million automated tests had missed.
While it was a boon for defenders, the same capability cuts both ways. Just a month later, Google’s Threat Intelligence Group confirmed the first known zero-day exploit built with AI help.
Both cases point to the same alarming shift: The time to find a security flaw and the time to exploit a zero-day vulnerability have both collapsed to machine speed. Two forces explain why:
1. The Speed Of Exploits
The Zero Day Clock measures the time-to-exploit (TTE) window from common vulnerabilities and exposures disclosure to active exploitation. In 2018, the median time stood at 771 days. By 2025, that window plummeted to the point where the majority of vulnerabilities were weaponized by bad actors before they were disclosed.
Models like Mythos have shifted the risk balance even further in the attackers’ favor by exposing more vulnerabilities than can be timely patched.
In the datacenter era, discovering and exploiting vulnerabilities both required manual effort. Cloud and SaaS followed and only automated the exploitation phase. Now, AI has automated both steps, effectively closing the response window.
2. Agents Inside The Gates
The second force involves who holds insider access.
Early enterprise computing granted privileged access to a small set of employees. Cloud and SaaS extended that to vendor engineers with standing credentials. Today, AI agents hold access to systems and data on behalf of those users. 
Many assume AI agents have limited access to sensitive data, but the opposite is usually true. That shows up in three ways:
• Non-Human Identity Sprawl: Agents need their own lifecycle in provisioning, least-privilege scoping, monitoring and decommissioning.
• Data-In-Use Exposure: The moment an agent reads or processes data is a new, largely ungoverned trust boundary.
• Third-Party Model Dependency: Sending data to an external model provider extends the insider boundary beyond the organization’s own infrastructure.
In customer environments, seemingly benign coding agents reach into users’ local environments, read files and environment data and pass that content back to the model.
In one instance I saw, when sensitive data was blocked from reaching the model, the agent hallucinated plausible substitutes to complete the task. That fabricated data, if written back into a production system, could have introduced errors that nobody would think to trace back to an AI session. 
A compromised agent token can give an attacker the same lateral access the agent already had, turning one compromised session into a path through the environment.
An AI-First Approach To Security And Trust
The two forces demand an AI-first approach to security, trust and governance, as the old assumptions and security approaches no longer hold: 
• Perimeter and identity tools decide who gets in, but they were built for human pace instead of autonomous agents.
• Encryption protects data at rest and in motion, but the moment an agent reads it, that data sits exposed.
• Zero trust continuously checks identity, but it assumes the integrity of the underlying compute layer.
• AI governance documents intent without being able to enforce it.
• Sandboxes and gateways contain blast radius, but without a hardware root underneath, a sandbox remains a policy rather than evidence, and can be circumvented by the agents, as in the Hugging Face breach.
In short, software protecting software is DevHopeOps, not security.
One way to mitigate this problem is to favor protection over detection. For example, confidential computing can help keep data protected even if there is a zero-day vulnerability in the hypervisor or operating system. I should note that my company is one of several offering a confidential computing solution.
Confidential computing runs workloads in hardware-isolated, encrypted enclaves built into modern CPUs and GPUs, where applications and data stay sealed off from everyone else on the machine, including administrators, cloud operators and other software, and where the code is cryptographically attested before it touches sensitive data. 
Alternative technologies include Fully Homomorphic Encryption (FHE), where cryptography lets you run computations directly on encrypted data without decryption, and open source confidential computing solutions. However, FHE affects performance and requires modifications to the application code, while open source solutions require lots of scaffolding to make it work.
Even with those solutions, enterprises should still scan their code for vulnerabilities that may introduce a back door for hacking. This security hygiene is table stakes against attacks.
Defending Against AI-Accelerated Threats
Defending against exploits at AI-speed requires specific steps today:
• Map your exploit-lifecycle exposure. Inventory where AI-generated code, AI coding agents and AI-facing data flows already exist.
• Treat every agent as a non-human identity. Register, scope to least privilege, monitor and decommission agents with the same rigor as privileged human accounts.
• Re-examine what “patch fast” buys you. AI-speed patching is necessary but not sufficient. Pair it with controls that don’t depend on human or automated reaction time.
• Use technology that protects data in use, not just data at rest and in transit. Confidential computing, for example, is one technology category that was built for this gap.
• Demand proof, not policy, from anything claiming to supervise AI or agent behavior. Ask whether the control can attest to its own integrity, or whether it just assumes a trusted environment beneath it.
• Watch the access model of frontier AI security tools as an indicator of how the industry is managing dual-use risk. Understand what restricted models, like Mythos, and more broadly available models, like Daybreak, are capable of. Factor that into your own governance posture.
• Continue investing in fundamentals. MFA, least privilege and visibility remain the highest-return controls even as threats accelerate.
The deciding factor isn’t whether an organization adopts AI, but whether its trust model can be verified rather than assumed.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
