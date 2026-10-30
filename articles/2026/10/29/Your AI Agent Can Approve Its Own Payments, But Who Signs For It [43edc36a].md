---
id: "43edc36a3ecdb6a2"
title: "Your AI Agent Can Approve Its Own Payments, But Who Signs For It?"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/29/your-ai-agent-can-approve-its-own-payments-but-who-signs-for-it"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/29/your-ai-agent-can-approve-its-own-payments-but-who-signs-for-it"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-29T06:45:00Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Keegan Crage"]
language: "en"
summary: "Agentic AI can weaken segregation of duties if human approval becomes a rubber stamp. Here are four questions leaders should answer before deploying AI agents."
tags: []
orgs: ["US government", "UK"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 854
paywalled: false
image: "http://www.bing.com/th?id=ONUT.IZhkyiWLoa9iimIIXDm6Rw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Your AI Agent Can Approve Its Own Payments, But Who Signs For It?

Forbes · Keegan Crage · 2026-10-29

Keegan Crage is the owner of TechBrain, an ISO 27001-certified technology, cybersecurity & AI governance partner operating across Australia.
Organizations have started automating their processes with agents but not always granting full autonomy. Agents can prepare the work, but they aren’t always trusted to finish it. In our business, sending an email, authorizing a payment or finalizing a new user’s setup still needs a person to sign off. That human in the loop is there by design.
Our clients have taken a similar approach and, in fact, none of them currently allow an agent to make payments on their behalf. Instead, all approvals are undertaken manually by individuals under the normal segregation of duties that has been in place to protect the finance function for decades.
In other words, the person who can amend a supplier’s bank account details is not the person who approves payment to that supplier.
Nearly a third of Australian organizations (32.5%) are using agentic AI, as reported in the HTI Corporate Leaders Survey in the AICD’s June 2026 director’s guide. As the functionality of these AI agents expands, organizations will need to consider an important question before go-live: Who is responsible for approving the actions taken by the AI agent?
The Second Person Is The Control
Historically, in organizations that manually process payments and segregate duties, the person that sets up a payment is not the same person that approves it for processing. It is this second person that identifies whether a supplier’s bank account has changed or if an invoice looks suspicious.
But a human in the loop is not the same as human control. Someone who approves whatever is put in front of them is just another step in the workflow. Someone independent of the person who set up the payment, who can see the evidence and has the authority to refuse, is a control. Segregation of duties depends on the second kind.
This well-established risk reduction methodology is in danger of being overturned by agentic AI. If an organization grants the AI agent the ability to run under the login of the person who built it, then the same credential is used to create and approve payments. As a result, the checks designed to identify redirected payments are removed. In Australia alone, payment redirection scams cost AU$166.8 million in 2025.
When agents approve payments, the gap in controls is hard to spot. The organization chose the payment tool, and capable people built it in good faith. But every payment the agent approves is logged under the account of the person who built it. Every entry looks legitimate, and nothing in the audit trail shows that a person never actually reviewed the payment.
The recent joint report from the cyber security agencies of the US, UK, Canada, Australia and New Zealand describes hijacked procurement agents that automatically process payments and also create very convincing audit trails for such processing. This is a problem that needs to be addressed by segregating duties. Those who design and operate a system should make the decisions regarding automated actions that require human approval, not the agent itself.
Australia’s recently updated Information Security Manual (ISM), issued in September 2026, states that all AI-enabled agents should have their own identity and be recorded within a register. The register should capture details of the owner of the agent as well as the business reason for its use.
Decide Who Signs Before You Switch It On
Governing AI agents is essentially the same as governing humans who execute decisions within an organization: namely, delegating authority and ensuring appropriate segregation of duties. COSO advises organizations to separate the ability to configure AI tools from the authority to approve their outputs and says each generative AI tool should have a named owner.
As NIST stated in an August post, people are easily lulled into rubber-stamping access approval requests that automatically come to them on a regular basis. It’s therefore critical that AI applications require human approval for sensitive or high-impact actions that the AI application can perform. Make sure the approver is trained and qualified to understand the context and approval boundaries of what the agent is proposing to do.
Four Questions Before You Switch It On
Before a payment agent goes live, leaders should be able to answer yes to each of these:
1. Does the agent have its own identity? If it runs under its developer’s login, the audit trail can’t tell their actions apart.
2. Is every action it can take in a register, with a named owner and business reason? If not, you don’t know what authority you’ve delegated.
3. Is every high-impact action approved by someone independent of the agent? That means not the person who built or operates it, and not the person who set up the payment.
4. Can that approver say no? They need to see what changed, such as new bank details, understand what the agent proposes, and have their decision logged separately. Otherwise it’s a rubber stamp.
If any answer is no, you’re not ready. The agent can still prepare the work. It just shouldn’t finish it.
