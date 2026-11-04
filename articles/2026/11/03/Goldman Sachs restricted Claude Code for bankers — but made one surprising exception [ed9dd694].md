---
id: "ed9dd69428779a0c"
title: "Goldman Sachs restricted Claude Code for bankers — but made one surprising exception"
url: "https://thenewstack.io/ai-coding-agents-security"
link: "https://thenewstack.io/ai-coding-agents-security"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T19:18:34Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Replit CEO Amjad Masad is warning that AI coding agents running on employee devices are becoming a security risk for enterprises and governments, as financial institutions begin restricting access to tools such as Claude Code. \n\n “AI agents running on employee endpoints are becoming a systemic security risk for enterprises & governments,” Masad writes on X , Tuesday. “Some are responding by…"
tags: ["AI Agents", "Developer tools", "Security"]
orgs: ["Anthropic", "Microsoft", "Cursor"]
topics: ["agents & coding", "safety & ethics", "models & research", "business & funding"]
content_source: "fulltext"
word_count: 734
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Goldman Sachs restricted Claude Code for bankers — but made one surprising exception

The New Stack · Amanda Caswell · 2026-11-03

Goldman Sachs restricted Claude Code for bankers — but made one surprising exception
Replit CEO Amjad Masad is warning that AI coding agents running on employee devices are becoming a security risk for enterprises and governments, as financial institutions begin restricting access to tools such as Claude Code.
“AI agents running on employee endpoints are becoming a systemic security risk for enterprises & governments,” Masad writes on X, Tuesday. “Some are responding by restricting tools like Claude Code, as Goldman Sachs reportedly has.”
“Some are responding by restricting tools like Claude Code, as Goldman Sachs reportedly has.”
Why finance restricts coding agents
His comments follow a Bloomberg report that Goldman Sachs has restricted access to Anthropic’s Claude Code and Microsoft’s GitHub coding tools to engineers. The restrictions apply to bankers and traders, but certain quantitative employees known as strats are exempt.
Goldman spokesperson Nick Carcaterra told Bloomberg the bank weighs productivity gains against potential risks when deciding which employees can continue using AI tools.
Masad suggests Goldman Sachs is not alone.
“This is widespread in finance. The ban hammer is coming down,”
“This is widespread in finance. The ban hammer is coming down,” he writes, responding to a post about the bank’s restrictions.
When asked what was driving the crackdown, Masad points to “Supply chain attacks etc.”
The credential exposure problem
Running coding agents directly on employee machines raises concerns about credential exposure, malicious instructions and compromised dependencies, each of which has already surfaced well beyond the finance sector.
The credential question has been pushing vendors toward short-lived tokens for months, a shift Vercel recently forced on its own suppliers by setting a deadline to abandon the long-lived keys that an agent operating on an endpoint could quietly read and reuse.
When asked on X whether banks were more worried about code leaving their environments or a lack of audit trails, Masad says, “So many things.”
He offered no examples of security incidents that prompted Goldman’s restrictions or other financial institutions adopting similar policies.
Isolating agents in the cloud
Alongside his comments, Masad shares a security advisory published by Replit on Monday. Written by Luis Héctor Chávez, Replit’s chief technology officer, and engineering lead at Replit, Manish Mehta, it recommends keeping AI agents off employee devices and running them in company-controlled cloud environments instead.
“AI agents should operate in dedicated, organization-controlled environments with limited access to the resources each task requires,”
“AI agents should operate in dedicated, organization-controlled environments with limited access to the resources each task requires,” Masad writes.
Replit recommends running agents in isolated environments, with credentials, audit logs, and approvals managed separately.
The advisory points to recent security incidents, including a compromised Claude Code extension distributed through the Cursor marketplace, as an example of how attackers can exploit developer tools.
That pattern has played out repeatedly across the ecosystem this year, including an attack in which intruders hijacked roughly 1,900 GitHub accounts before moving against some 30,000 repositories, a reminder that a single poisoned link in the chain can reach far past the machine where it started.
Controlling what agents can access
But restricting AI coding agents to engineers doesn’t necessarily solve the problem. Even experienced developers can run agents that follow malicious instructions or pull in compromised software, and research has shown how little it takes to knock an agent off course, with one team finding that stripping a single line from Claude Code’s instructions sent its out-of-scope actions climbing. Replit argues that companies need to control what agents can do, not just who gets to use them.
What this means for enterprise AI adoption
Goldman’s restrictions suggest companies may be rethinking how widely they allow employees to use AI coding tools. Giving non-developers the ability to build software has been a major selling point, but that becomes harder to justify when agents have access to sensitive corporate systems.
Masad argues that companies don’t need to stop using agents. They need to keep them off employee devices and put tighter controls around what they can access.
Whether financial institutions broadly adopt that model remains to be seen. Masad has described restrictions as widespread, but has not provided public evidence establishing how many organizations have introduced them.
The New Stack has reached out to Replit for additional comment on the reported restrictions, the security concerns driving them, and whether financial institutions are changing their approach to AI coding agents.
Learning Path
