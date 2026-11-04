---
id: "1fac463edbd04c05"
title: "To Defend Against AI Attackers, Start Thinking Like One"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/03/to-defend-against-ai-attackers-start-thinking-like-one"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/03/to-defend-against-ai-attackers-start-thinking-like-one"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-03T19:30:25Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Yair Grindlinger, Forbes Councils Member"]
language: "en"
summary: "Increasingly, the threat is the ability of attackers to chain different exposures together until they find a way in."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Hugging Face", "Microsoft"]
topics: ["safety & ethics", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 1264
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6ae9dc77902dc6596daf9cdc/0x0.jpg?width=960&precrop=6000%2C3375%2Cx0%2Cy302"
discussion_url: null
score: null
comments: null
community: null
---

# To Defend Against AI Attackers, Start Thinking Like One

Forbes · Yair Grindlinger, Forbes Councils Member · 2026-11-03

Yair Grindlinger is CEO and Co-Founder of Surf AI.
AI is not black magic. It still has to work through real systems, identities, applications and infrastructure, which means its limits are knowable. That matters, because fear is only useful when it’s aimed at the right things.
For enterprises, the right thing to fear is how AI changes the attacker. AI-driven attacks are faster, more persistent and more sophisticated, and they can exploit a single critical weakness or chain together a handful of small ones until they find a way in. 
AI Changes The Economics Of An Attack
There are several obvious ways AI changes attacks. First is speed. We’re seeing attacks happen in hours instead of days or weeks because AI systems can operate 24/7. The window for defenders is already shrinking. CrowdStrike’s 2026 Global Threat Report found that the average time it took criminal attackers to move from initial access deeper into a network fell to 29 minutes, and the fastest observed breakout took just 27 seconds.
But I think stamina may be even more important than speed. A typical human attacker might spend a few hours trying to get into an organization. If nothing works, they may move to the next victim. AI doesn’t necessarily have that limitation. If you tell an AI system to find a way in, it can keep working 24/7 until it finds something.
Then there is breadth of knowledge. Human attackers are typically good at something, whether it’s social engineering, zero-days or a particular system. AI can have the whole playbook. The same system can work across identity, software vulnerabilities, configurations and other attack surfaces. Because it has both stamina and breadth of knowledge, it can connect those weaknesses together.
Sophistication Shows Up In The Chain
That ability to connect weaknesses changes how we need to think about exposure. An attack might begin with an exposed secret, then move to an asset with a risky configuration, a software vulnerability or an identity problem. Each issue might look relatively insignificant on its own. You might classify each one as medium or low risk and decide none is critical enough to demand immediate attention. But together, they can create a critical attack path.
Microsoft made essentially the same point in its July 2026 “Secure Future Initiative“ progress report, noting that attackers can use “frontier models to discover vulnerabilities, chain attack paths, and scale exploitation faster than manual approaches allow.” It also observed that serious security failures can emerge when identity gaps, unmanaged assets and inconsistent configurations sit next to one another.
The Hugging Face intrusion offers a vivid example. In July 2026, the company disclosed that an autonomous AI agent, which had escaped an AI lab’s evaluation environment, carried out an end-to-end intrusion into part of its production infrastructure, with no human directing its steps. The attack moved from code-execution weaknesses to credential harvesting and lateral movement across internal clusters. Hugging Face later reconstructed roughly 17,600 attacker actions as the system searched for a viable path. Most of those actions failed. The agent simply kept going until something worked.
A human attacker may look for one big open window and move on if it isn’t there. AI will find that window faster, and if it isn’t there, it will patiently look for the little things and chain them together.
Security Teams See Silos, And Attackers See A System
Attackers and defenders often see the environment differently. From a defender’s perspective, we frequently manage security in islands. There may be a cloud vulnerability team, an identity team, IT teams and someone else responsible for third-party applications. The attacker doesn’t care about those organizational boundaries. To the attacker, all of those things are part of the same attack surface.
Suppose a team is looking at a cloud vulnerability. On its own, it might not appear urgent. But what if the asset can be accessed by someone whose MFA is misconfigured and who also uses a highly privileged third-party application? If the teams responsible for those areas don’t know the issues are connected, they don’t understand the real priority.
Prioritize Attack Paths, Not Just Vulnerabilities
That becomes especially important as AI gives defenders visibility into more exposures. In many cases, these weaknesses were probably always there. We simply know about more of them now. That’s a good thing because defenders can use powerful tools to find the same types of exposures attackers are looking for.
The problem is that organizations will get a lot of results. It will be impossible to manage everything at once. Prioritization therefore has to change. Instead of looking only at how severe an individual vulnerability appears to be, ask whether it is exposed, how it connects to other weaknesses and whether it forms part of an attack chain.
A critical exposure on an important asset still demands attention, whether or not it’s part of a chain. But something that appears lower-risk may also offer a quick win because fixing it breaks a larger chain.
Most Teams Are Still Stuck On The Basics
AI has made finding vulnerabilities faster and easier than ever. Closing them still depends on knowing who owns the affected asset, understanding what a fix could affect and getting approval, and that’s where most organizations get stuck. In many of my conversations with CISOs, we never get to attack chains. They have critical exposures they can’t close.
One CISO at a large enterprise told me that 25% to 35% of employees leave or change roles in a given year. Many of them own systems, and the asset inventories meant to track that are almost never up to date. So security teams spend their days chasing people to find out who can approve a fix. That isn’t the job anyone signed up for, and it’s the bottleneck that keeps exposures open. Before you can think in chains, you have to be able to close the basics quickly.
Defense Must Operate At Machine Speed
I see two fundamental requirements for responding to this shift. First, organizations need to know their assets: what they have, who owns each one and what a change could affect. Second, they need automation operating continuously on top of that knowledge.
If attackers are operating at machine speed, defenders cannot depend entirely on human-speed processes. Organizations need systems that continuously collect information, connect exposures and help security teams identify which problems matter most. Then they need to get each fix to the right people, because a prioritized list nobody can act on doesn’t reduce risk.
This matters even for threats no one has seen yet. You can’t patch a zero-day before you know it exists, but you can shrink your blast radius every day by closing the exposures around it, so the next one matters less before it’s even disclosed. And when it does land, you can be ready to answer “are we exposed?” in hours, not weeks.
For CISOs, my practical advice is to pause and rethink exposure management. The way we have managed exposure until today isn’t necessarily going to work for the AI era. Assign someone, or create a team, whose job is to think about exposure holistically. Then reconsider the people, process and technology required to support that approach.
AI creates real reasons for concern. But the most useful fear is a specific one: attackers are becoming faster, more persistent and more sophisticated. Defenders need to respond in kind: know their assets, shrink their blast radius every day and be ready for the next one.
In other words, we need to start thinking a little more like the attackers.
