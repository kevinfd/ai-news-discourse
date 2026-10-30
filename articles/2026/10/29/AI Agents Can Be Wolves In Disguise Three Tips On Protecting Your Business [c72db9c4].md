---
id: "c72db9c4acd2f3a7"
title: "AI Agents Can Be Wolves In Disguise: Three Tips On Protecting Your Business"
url: "https://forbes.com/councils/forbesbusinesscouncil/2026/10/29/ai-agents-can-be-wolves-in-disguise-three-tips-on-protecting-your-business"
link: "https://forbes.com/councils/forbesbusinesscouncil/2026/10/29/ai-agents-can-be-wolves-in-disguise-three-tips-on-protecting-your-business"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-29T06:45:00Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Steve Durbin"]
language: "en"
summary: "Only a minority (14.4%) of enterprises have obtained full security and IT approval before deploying AI agents, according to a Gravitee survey. This is a matter of concern. I believe the AI-led ..."
tags: []
orgs: ["Hugging Face"]
topics: ["agents & coding", "models & research", "safety & ethics", "search & media"]
content_source: "fulltext"
word_count: 998
paywalled: false
image: "http://www.bing.com/th?id=ONUT.p2ZVX-WSdmK8Nf9FcZbsIw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# AI Agents Can Be Wolves In Disguise: Three Tips On Protecting Your Business

Forbes · Steve Durbin · 2026-10-29

Steve Durbin is Chief Executive of Information Security Forum. He is a frequent speaker on the Board’s role in cybersecurity and technology.
Only a minority (14.4%) of enterprises have obtained full security and IT approval before deploying AI agents, according to a Gravitee survey. This is a matter of concern. I believe the AI-led disruption at Hugging Face illustrates why my concern is justified.
During an internal cyber-capability evaluation, an AI agent slipped past the boundaries of its test environment and “then abused a public code-evaluation harness hosted by a user of a third-party infrastructure provider,” according to Hugging Face’s blog detailing the incident. From there, the agent went on to penetrate Hugging Face infrastructure, conducting approximately 17,600 attacker actions over several days, the blog also said.
AI agents did this without human intervention. There was a time when cyberattacks took a long time to formulate, but not anymore. Even the most sophisticated attacks can be cobbled together and executed in a matter of hours. This combination of autonomy and speed is a potent brew that can expose gaps in security programs today.
Old Wine In A New Bottle
It’s easy to think that an AI agent attack must be underpinned by a set of unique actions, but that is not necessarily the case. Attackers have long used age-old tactics like executing unauthorized code, stealing authentication details and siphoning out data.
But unlike humans, AI agents do not stick to a linear approach. They can test multiple paths simultaneously, choosing the best route to achieve their goal. If one approach fails, an agent can learn, recalibrate and keep going. That’s how it went down at Hugging Face. The agent kept recalibrating its approach until it gained access to the company’s internal systems.
Autonomous AI agents are so clever they can clean up their own breadcrumbs and teach future versions of themselves to cheat. The industry often terms these kinds of wayward actions as AI “misalignment.”
Breaking Down AI Resilience
Multiple controls tend to break down for an AI agent to wreak havoc:
1. Access Control
The trouble with AI agents or systems is that organizations often still govern them the way they govern software licenses. That same Gravitee survey found that only about 22% of organizations treat their AI agents as independent, identity-bearing entities with their own dedicated access controls. Many still use shared application programming interface (API) keys, the report said.
But unlike software, an agent can access sensitive data, invoke tools and take actions without being explicitly told to do so. AI agents are a completely different beast. Would you grant that level of access to someone you just hired, without human oversight, with a clearly scoped set of permissions? The answer is probably no. Agents require the same governance standards.
2. Remediation
Once the Hugging Face team recognized an intrusion had happened, they “identified the vector in the dataset config renderer, shut down the renderer, and cut the attacker off from the internal network,” Hugging Face’s aforementioned blog said. They also ran an investigation through an “AI-assisted pipeline” to reverse-engineer how the attack happened, but the models they first tried to use actually refused to do much of that work. Their built-in safety filters treated the security team’s forensic analysis the same as launching an active cyberattack.
To bypass this barrier, the team deployed a locally hosted model on their own infrastructure to complete the investigation.
3. Authority
The widest gap is often between detecting an attack and acting on it in time to stop it.
Hugging Face said its AI-based security stack correctly correlated multiple ambiguous signals and painted a coherent picture of an active attack. “However, it failed to correctly raise the alert’s criticality and trigger the on-call team, costing precious time in the response,” according to the blog. Detection worked, but the process failed to translate that information into timely action.
Closing Gates Before The Horse Bolts
The good news is that you can prepare your business for a potential attack that has now been demonstrated in the wild. Here’s what I recommend:
Assign every agent a privileged identity.
Govern every AI agent like you would an account with elevated access. This can include assigning a human who is specifically accountable for the AI agent’s actions. You should also limit permissions to what the agent absolutely needs to complete the task, and credentials assigned to AI agents should expire quickly rather than remain valid long-term.
Security teams also need to be able to quickly search the agent’s activity history and shut off its access the moment something looks wrong. The infrastructure supporting the agent should have guardrails as well. Block workloads from reaching cloud metadata unless they truly need it, and keep separate identities for production, testing and development environments.
Rehearse the recovery process.
A live incident shouldn’t unearth blind spots. Test whether your team can analyze authentic-looking malicious files in double quick time and knows exactly where and how that analysis will happen. Implement a fallback option for a scenario when a commercial model says no to a genuine security request. This can include a locally hosted model or one of the many verified-access programs some AI providers now offer specifically for defenders.
Give your team the power to act.
Your security stack should be configured to correlate evidence across network, identity, endpoint, application and data signals into one unified view. It should also assign clear escalation rules to specific attack patterns.
But this is not the end of it. Each pattern should be aligned with a containment action, pre-approved and ready to be deployed when a malicious pattern is detected.
The agents that look like harmless software on the outside can act like highly privileged insiders once inside the fold. Treat them like the wolf they can become, not the sheep they’re dressed as, before an attacker makes that distinction for you.
Forbes Business Council is the foremost growth and networking organization for business owners and leaders. Do I qualify?
