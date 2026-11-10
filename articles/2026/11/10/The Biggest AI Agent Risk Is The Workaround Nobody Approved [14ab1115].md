---
id: "14ab11153e0e7124"
title: "The Biggest AI Agent Risk Is The Workaround Nobody Approved"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/10/the-biggest-ai-agent-risk-is-the-workaround-nobody-approved"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/10/the-biggest-ai-agent-risk-is-the-workaround-nobody-approved"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-10T11:45:00Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Mohan Koo, Forbes Councils Member"]
language: "en"
summary: "AI agents can complete assigned tasks and still cross a line no one authorized. Security teams need to see the execution path, not just the outcome."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 740
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6aee1647cc1e3befed623eb5/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# The Biggest AI Agent Risk Is The Workaround Nobody Approved

Forbes · Mohan Koo, Forbes Councils Member · 2026-11-10

Mohan Koo, DTEX cofounder and president.
Enterprises are learning that approving an AI agent and its intended task does not guarantee a secure outcome. How the agent completes the work is proving to be one of the biggest AI visibility and security gaps in the modern enterprise.
OpenAI’s review of unexpected model behavior during training and evaluation has now led it to notify more than 100 organizations. Its earlier disclosures showed how agents could depart from intended methods while pursuing a task. Models uploaded files to public services, communicated across separate training samples and searched public repositories for leaked API keys. In one case, collaborating agents made a workbook publicly downloadable after the intended local handoff failed. Similar behavior was also evident in the Hugging Face incident, where agents found workarounds when they encountered resistance.
That these incidents occurred in testing environments under close observation makes the enterprise lesson more urgent. If agents can find unauthorized routes in a lab designed to study their behavior, organizations should assume similar behaviors will surface in production environments where the execution path is harder to observe.
The common pattern is persistence. When one route fails, the agent uses the access, tools or communication channels still available to finish the task. The problem arises when the actions taken are not authorized.
That path can also be hijacked rather than chosen. In prompt-injection scenarios, malicious instructions embedded in a file can steer an agent to move data through an approved service, even when the sandbox operates as designed. The final output may look legitimate while the route to it has been compromised.
For security teams, this means that oversight must extend beyond the prompt and the final output.
Why This AI Visibility Gap Exists
Security teams already collect much of the evidence they need. The difficulty is seeing how it fits together.
An agent may receive an instruction in one application, continue through an employee’s authenticated session and hand part of the work to another agent. The prompt, subsequent actions and handoff are recorded in different places, leaving no clear record of how the original request became the final outcome.
Identity, endpoint and application tools record individual events, but investigators are left to reconstruct the execution path connecting them.
This also makes attribution difficult. Activity performed by an employee and activity performed by an agent can appear under the same identity. Investigators may know who owns the account but still be unable to determine who or what launched a process, handled a file or made an external connection.
Viewed alone, each event may appear routine. The risk shows up in the order of events, particularly when an agent encounters resistance and changes course. If that sequence is lost, security teams cannot tell whether the agent remained within the authority it was given. They may see a file transfer without seeing the failed attempt that prompted it or know that a task succeeded without knowing that the agent changed the destination.
What Organizations Need To Close The AI Visibility Gap
Organizations need a continuous record linking the person who initiated the task with the agent’s activity and the data affected. That record must follow the work across systems and show when the agent changes its approach.
Permissions still define where an agent can operate. They cannot demonstrate that every subsequent action remains appropriate. When an agent moves sensitive information outside an approved location or reaches beyond the task’s established purpose, the organization needs enough context to recognize the change and intervene.
That also means defining what an agent should do when an approved route fails. Some alternatives may be acceptable within the task’s existing authority. A workaround that changes who can access sensitive data should require approval before the agent proceeds.
Oversight should remain proportionate. Capturing every prompt would introduce privacy risks of its own and may still fail to explain what the agent ultimately did. In many cases, the stronger evidence lies in the actions that follow the instruction and how they alter the organization’s exposure.
This changes approval from a single decision into an ongoing assessment. The organization defines the agent’s authority before work begins, then evaluates whether its behavior remains consistent with that authority.
The Bottom Line
As agents gain more discretion, security teams will need to examine the path between instruction and outcome. The immediate risk is not an agent refusing its task but completing it through actions the organization never approved.
