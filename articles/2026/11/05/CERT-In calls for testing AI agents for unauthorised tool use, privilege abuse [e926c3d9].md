---
id: "e926c3d95ca0b956"
title: "CERT-In calls for testing AI agents for unauthorised tool use, privilege abuse"
url: "https://thehindu.com/business/Industry/cert-in-calls-for-testing-ai-agents-for-unauthorised-tool-use-privilege-abuse/article71668646.ece"
link: "https://thehindu.com/business/Industry/cert-in-calls-for-testing-ai-agents-for-unauthorised-tool-use-privilege-abuse/article71668646.ece"
source: "The Hindu"
domain: "thehindu.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-05T06:14:38Z"
published_date: "2026-11-05"
collected_at: "2026-11-05T13:04:25Z"
authors: ["The Hindu Bureau"]
language: "en"
summary: "Guidelines require checks on agents’ permissions, task delegation and emergency-stop mechanisms; multi-agent systems must maintain authenticated, logged communications and records of actions"
tags: ["Industry"]
orgs: []
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 449
paywalled: false
image: "https://th-i.thgim.com/public/incoming/xte4a1/article71668779.ece/alternates/LANDSCAPE_1200/iStock-2257366803.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# CERT-In calls for testing AI agents for unauthorised tool use, privilege abuse

The Hindu · The Hindu Bureau · 2026-11-05

The Indian Computer Emergency Response Team (CERT-In) has set out specific security and auditing requirements for artificial intelligence (AI) systems that can independently plan and carry out tasks, use external tools, and delegate work to other AI systems.
The Artificial Intelligence (AI) Security Auditing Guidelines: Framework for Secure, Ethical, and Auditable Artificial Intelligence Systems identify features such as autonomous task execution, persistent memory, and the ability to delegate work as factors that can increase the risks associated with these systems.
Unlike conventional AI tools that primarily respond to user instructions, agentic AI systems can take multiple steps to complete a task. They may access information, use software tools, execute code, or communicate with external systems. The guidelines identify such capabilities—particularly when exercised without human intervention—as factors requiring closer security scrutiny.
The framework calls for testing whether an AI agent can exceed its authorised permissions, use tools without approval, bypass approval mechanisms, or misuse credentials. It also identifies unsafe delegation of tasks and the effectiveness of emergency-stop mechanisms as areas that auditors should examine.
The guidelines also address the risks associated with an agent’s memory and the information it retains from earlier interactions or tasks. They call for testing whether this memory can be manipulated, whether information belonging to one user can leak to another, and whether sensitive information is retained or reused without authorisation.
Keeping multiple AI agents in check
The framework separately addresses systems in which multiple AI agents work together and pass tasks between one another.
It calls for each agent to have a unique identity and clearly defined permissions. Communications between agents must be authenticated and logged, allowing organisations to establish which agent made a request and whether it was authorised to do so.
Organisations must also have controls to detect and limit repeated delegation of tasks, uncontrolled creation of new tasks and loops in which agents keep assigning work to one another.
The guidelines call for records that allow auditors to reconstruct what happened within a multi-agent system. These should capture requests exchanged between agents, tasks delegated, permissions used, decisions made, software tools invoked and the external actions that followed.
For high-risk systems, the framework also specifies the ability to suspend an individual agent or an entire workflow and revoke its access credentials.
The guidelines also call for organisations to maintain an inventory of the components used in production AI systems, including models, training data, software and external tools. Where third-party model providers do not disclose internal details, organisations must document the information gaps and their impact on audits. Auditors using AI must independently verify its outputs, as AI-generated summaries cannot replace audit evidence or professional judgement.
Published - November 05, 2026 11:38 am IST
