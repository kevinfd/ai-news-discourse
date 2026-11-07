---
id: "91ac4ccdf2ff1304"
title: "The AI Control Gap: Companies Adopting AI Must Learn What Wall Street Learned The Hard Way"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/06/the-ai-control-gap-companies-adopting-ai-must-learn-what-wall-street-learned-the-hard-way"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/06/the-ai-control-gap-companies-adopting-ai-must-learn-what-wall-street-learned-the-hard-way"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-06T17:45:00Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Samuel Kaluvuri, Forbes Councils Member"]
language: "en"
summary: "The AI control question that many banks are working through is one that other companies adopting agentic AI will increasingly need to address.​​"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "policy & regulation", "safety & ethics", "robotics & autonomy"]
content_source: "fulltext"
word_count: 1024
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6aecc023fa28c4b89d2203b4/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# The AI Control Gap: Companies Adopting AI Must Learn What Wall Street Learned The Hard Way

Forbes · Samuel Kaluvuri, Forbes Councils Member · 2026-11-06

Samuel Kaluvuri, CEO of ApyHub, works on API infrastructure and runtime policy enforcement and holds a PhD in security assurance.
Somewhere inside a large bank, an AI agent has a name, a login ID and a manager who has to write its performance review.
This is less eccentric than it sounds, and it’s one of the more rational things I believe banking has done this year. These are institutions with serious risk functions and long memories for things that lose money quickly. Looking for a way to control software that acts on its own, they reached for the instruments they trusted: an identity, a reporting line and someone answerable for it.
They are developing ways to manage a new kind of software, and the questions they are working through are ones other companies adopting agentic AI will increasingly need to address.
Why Traditional Controls Fall Short
Enterprise software has always come with controls: permissions, approval chains, segregation of duties and audit logs. That worked for 30 years because a person asked for something, another looked at it and the system did exactly what was approved.
All three assumptions have stopped being true. The requester is now software operating at machine speed, and approval no longer describes the action. When someone signs off on “handle customer onboarding,” nothing in that sentence says which systems get touched, what data leaves which jurisdiction or what the agent does when it meets a case nobody thought about. The approval covers intent, but the risk lives in the path.
Put an approval workflow in front of a system taking thousands of autonomous actions, and you have not built oversight. You have built a very fast queue of things you already agreed to.
Finance learned this the hard (and expensive) way. Sign-off on trades worked until trades stopped happening at human speed. In 2012, Knight Capital pushed faulty code into production and lost more than $460 million in 45 minutes. By the time a conventional approval process notices a problem like that, the money is gone.
The response was not a better approval workflow. Control moved into the execution path: limits enforced before an order left the building, kill switches and real-time surveillance. Regulators then went further, and this is the part I believe is worth borrowing. Under the Securities and Exchange Commission’s market access rule, those controls must sit under the firm’s direct and exclusive control.
A broker may buy the risk technology from a third party, but it must keep the ability to monitor and adjust the controls in real time and cannot simply rely on the provider’s assurance that they work. The point of intervention moved to where the machine acts and stayed with whoever carries the liability.
Where Agent Control Actually Lives
So where does control over an agent actually live?
Not in the model. It sits below where these products are demonstrated and sold, in the software that determines which systems an agent can reach, what it may do with them, when it stops and what gets written down. Change the model, and the agent gets cleverer. Change that control layer, and it can no longer touch your payments system.
Three capabilities determine how effective these controls are: the ability to limit an agent’s actions before they happen, stop them while they are underway and independently reconstruct what the agent did afterward.
Running infrastructure that sits in the path of these calls gives you a different view. Human traffic arrives one action at a time. Agent traffic arrives in bursts: dozens of calls in a few seconds while the thing works through a task. Everyone can check whether the task completed, but few see what it read on the way or where it sent what it found.
This is where the buying decision becomes important. A company does not necessarily have to hand this layer to its vendor. An enterprise can retain control over its access policies, gateways, transaction limits and logging, as many already do for systems used by employees. But those controls need to be deliberately extended to cover agents. Otherwise, buyers may inherit runtime rules configured by engineers focused on task completion or rely on defaults that are rarely revisited. These settings may also fall outside the governance documents boards and compliance teams regularly review.
An employee’s limits are typically enforced through systems the bank controls and can adjust as needs change. An agent’s limits depend on the systems governing its actions, which may be managed by the buyer, the vendor or both. If the buyer has not established who controls that layer, important decisions may effectively be made elsewhere. The purchase is therefore not just software that performs tasks; it also involves a set of operating rules, some of which may already be in place before the buyer evaluates them.
Platforms should be assessed not only on what an agent can do in a demonstration but also on where controls are enforced and who can change them. If a platform does not provide the necessary oversight, building a replacement layer may be one option, but it is not always practical or sufficient. In some cases, the better decision may be to keep a workflow under human supervision until the organization can establish controls appropriate for autonomous operation. That may be a less appealing sales proposition, but it can be the more responsible choice.
Closing Thoughts
The regulatory direction is visible. In June 2026, the Financial Stability Board warned that the autonomy of AI agents can amplify risks that materialize at great speed.
Supervisors are no more likely to accept “our vendor handles that” than they were for outsourced trading infrastructure. Meanwhile, the platforms are sold on handing the work off entirely.
Every autonomous system runs inside rules that determine what it can do, and those rules exist whether or not the board has seen them. The question for a vendor is not merely who wrote them but whether you can inspect them, change them and, when the machine is already moving, enforce them yourself.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
