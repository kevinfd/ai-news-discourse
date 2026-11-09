---
id: "7b32aaa620789d12"
title: "Anthropic Usage Policy Takes Effect Thursday: Claude-Driven Machines Must Stop When Connection Drops"
url: "https://techtimes.com/articles/330283/20261109/anthropic-usage-policy-takes-effect-thursday-claude-driven-machines-must-stop-when-connection-drops.htm"
link: "https://techtimes.com/articles/330283/20261109/anthropic-usage-policy-takes-effect-thursday-claude-driven-machines-must-stop-when-connection-drops.htm"
source: "Tech Times"
domain: "techtimes.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-08T22:35:00Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Clark Johnson"]
language: "en"
summary: "Anthropic usage policy changes take effect Nov. 12, requiring any Claude-driven equipment that could injure people to stop or hold a safe state when its connection is lost, with a qualified person ..."
tags: []
orgs: ["Anthropic", "Amazon", "Nvidia", "Hugging Face", "EU", "UK"]
topics: ["models & research", "policy & regulation", "safety & ethics", "robotics & autonomy"]
content_source: "fulltext"
word_count: 1857
paywalled: false
image: "http://www.bing.com/th?id=ONUT.B_3L4K-s8Z7nMj6eOZ3VzA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic Usage Policy Takes Effect Thursday: Claude-Driven Machines Must Stop When Connection Drops

Tech Times · Clark Johnson · 2026-11-08

Starting Thursday, Nov. 12, anyone who lets Claude drive equipment that could injure a person without a human approving each action must keep a qualified person able to watch and stop it, make the equipment stop or hold a safe state when that person steps in or the connection to Anthropic's services is lost, and enforce safety limits somewhere other than in the model's output. That is the new High-risk Physical Actions section of Anthropic's rewritten Usage Policy.
Bedrock customers are covered too. Anthropic announced the update on Oct. 8, and an AWS Health notice dated Oct. 14, as reported by Classmethod, says continued use of Claude on Amazon Web Services' Bedrock on or after Nov. 12 counts as acceptance of the new terms.
The previous version, which took effect Sept. 15, 2025, stays in force until Thursday. According to the same AWS notice, model availability, pricing, API behavior and model IDs on Bedrock do not change.
Claude-Driven Equipment Must Stop or Hold Safe State When Connection Drops
The section applies when Claude is connected to hardware that takes physical actions without human approval and could cause injury. It sets three duties. A qualified individual must be able to observe the equipment and stop it at any time. The equipment must stop or hold a safe state when that person intervenes or when connection to Anthropic's services is lost. And operating limits such as speed, force, temperature or dose must be enforced by the equipment itself or by a controller independent of model output.
Anthropic's announcement ties the section to its Model Hardware Standard research preview, launched Aug. 27, and says Claude has taken on longer, more independent work. The policy text itself never uses the name Model Hardware Standard; the announcement is where the link is made.
Six Hardware Categories Trigger Rules While Four Exclusions Stay Outside
The policy names six situations that bring a deployment under the section: equipment that moves through shared space, applies force capable of causing injury, controls hazardous energy or materials, acts on the human body, controls safety systems, or runs industrial processes where a fault could injure someone.
Four uses fall outside it. Consumer and household devices operating within their built-in safety limits are excluded when the worst outcome is discomfort or inconvenience. So are plans, code or commands that a qualified person reviews before execution, monitoring or sensing that does not control anything, and laboratory automation that handles non-hazardous materials inside enclosed instruments.
Two points matter for compliance planning. The policy does not replace safety law, meaning vehicle, aviation, medical-device, machinery and workplace safety rules and certification still apply. And a carve-out for government contracts sits in the policy's introduction and covers the whole policy, not only the hardware section.
The text also leaves "qualified individual," "connection lost" and "human approval" undefined, and Groundy's analysis makes the same point. Operators will have to decide for themselves how long a stalled link counts as lost and who qualifies to hold the stop role.
Independent Controller Rule Answers Documented Jailbreaks of LLM-Controlled Robots
Requiring limits outside the model matches what security researchers have shown. In October 2024, a team led by University of Pennsylvania researchers, including Hamed Hassani and George Pappas, described RoboPAIR in a paper posted to arXiv. IEEE Spectrum reported that the attack jailbroke all three LLM-controlled systems the team tested: the Unitree Go2 robot dog, the Clearpath Jackal wheeled robot and Nvidia's open-source Dolphins self-driving model, tested in simulation. That is a 100 percent success rate.
Prompt injection compounds the problem. A UK National Cyber Security Centre blog post warned that prompt injection attacks may never be totally mitigated. A limit written into a prompt can be talked around; a limit enforced by a separate controller does not depend on the model behaving.
Does Anthropic's Model Hardware Standard Count as an Independent Controller?
The standard gives Claude a driver with read and write primitives, reachable through MCP, a command-line interface or code files, plus a reference file listing the safety limits that will be enforced. Participants named in the preview include Genentech, Carnegie Mellon, HHMI Janelia, QuEra Computing, AWS, Danaher, Universal Robots, Doosan Robotics, Hugging Face and Raspberry Pi. Anthropic plans to open-source the standard but has given no date.
Whether a limits file inside that driver satisfies the rule is not answered in the policy. The rule asks for enforcement by the equipment or a controller independent of model output, and a file that the same software stack loads on Claude's behalf may not meet that bar. Operators who rely on it should treat the question as open until Anthropic says otherwise.
Link-Loss Clause Turns Cloud Outages Into Mandatory Safety Trips
The connection-loss requirement makes network and service availability a safety dependency. Equipment that keeps running its last command when the link to Claude drops fails the rule. So the safe-state logic has to live locally, in the machine or its controller, and be tested by cutting the connection.
The tradeoff is availability. A robot that halts on every network blip is safe but unreliable, so integrators must decide per application which safe state, such as stop, hold position or retract, fits the hazard.
ISO 10218 and EU Machinery Regulation Still Govern Certification
Anthropic's rule sits on top of existing machinery safety standards instead of replacing them. ISO 10218-1 and -2, revised in 2025, make an emergency stop mandatory for industrial robots at a default performance level c and a protective stop mandatory at a default performance level d, according to IBF Solutions' summary.
In the European Union, Regulation (EU) 2023/1230 applies from Jan. 20, 2027. Under it, machinery with safety functions that use machine learning and can change behavior is listed in Annex I Part A and needs a notified-body conformity assessment. A July 2026 EU regulation on AI simplification, number 2026/1744, amended the machinery rules but did not change the date, according to compliance firm Ecorpit.
Weapons Software and Law-Enforcement Decisions Draw Conflicting Readings
Anthropic says most of the updates are meant to clarify existing rules, and that its rewritten surveillance section does not change what it enforces in practice.
Reseller Classmethod, which has a reseller agreement with Anthropic, reads the changes more broadly. Its analysis calls the law-enforcement ban "expanded," counts high-risk recommendation areas rising from seven to eleven, and describes the resale and proxy prohibition as new. The policy text confirms eleven high-risk areas, and its weapons and law-enforcement language bans weapons development, bars weaponizing or integrating weapons onto drones and other unmanned platforms, and covers decisions to investigate, charge, arrest or detain, prosecute and sentence. This review could not compare it against the previous text.
The policy arrives a month after Anthropic's Sept. 10 threat report, which described six conventional-weapons cases: three linked to China, two to Russia and one to Yemen. One involved Russian actors described as likely freelance who built an autonomous drone swarm, according to Reuters.
Personalized Vote Targeting Is Allowed; Deceptive Campaigns and AI-Answer Seeding Are Not
The elections section was narrowed, and the blanket ban on personalized vote and campaign targeting was removed. Anthropic's stated reason is to avoid blocking legitimate civic work, such as nonprofits informing voters in other languages and election officials sending ballot cure notices.
A Deceptive Campaigns section covers artificial activity and includes a line on seeding search or AI sources with misleading content. Elementera's analysis concludes that the policy does not ban answer engine optimization as such but targets deception about the origin, authorship or independence of content. The policy text does not use that term. Elementera sells answer engine optimization services, so its reading carries a commercial interest.
Cruelty Ban Leans on Ending Chats; Penalties for Violations Remain Unclear
The rule against sustained, needless cruelty toward models targets only extreme cases, repeated cruelty with no discernible purpose, and excludes frustration, pushback, dark creative themes, testing and research. Anthropic says Claude's ability to end conversations, introduced for Opus 4 and 4.1 in consumer chat interfaces in August 2025, remains the primary enforcement mechanism. Interesting Engineering reported that Anthropic has not clarified whether repeated violations could bring penalties such as account suspension, although the policy's general enforcement section lets Anthropic warn, throttle, limit, suspend or terminate access.
The rule reflects a live disagreement. Anthropic CEO Dario Amodei said in February that the company does not know whether its models are conscious, while Microsoft AI chief Mustafa Suleyman has argued that only biological beings can be conscious.
Resale, Proxy and Foreign-Control Rules Target Workarounds
The policy bars reselling, proxying or otherwise providing Claude access through unauthorized means, including routing consumer subscriptions to other users. A Supported Regions clause covers access from unsupported places and from entities controlled from them.
The Financial Times reported in early July that Ant gave employees corporate Claude accounts through a Singapore-linked entity, that ByteDance reimbursed engineers' personal subscriptions used through VPNs, and that "transfer station" relays route mainland users' requests through overseas-registered accounts, with operators suspected of storing or reselling prompts. The summary comes from a secondary outlet because the original is paywalled.
Classmethod calls the resale ban new. Anthropic's announcement does not mention it, and this review could not confirm what the previous policy said on the point.
What Should Operators Check Before Thursday?
Operators with Claude connected to any actuator can work through six checks before Nov. 12:
- Map each Claude-to-hardware link against the six triggers and four exclusions.
- Name the qualified individual who can observe and stop each system, and write down why that person qualifies.
- Cut the connection during a test and confirm the equipment stops or holds a safe state without help from Claude.
- Move safety limits into the equipment or a separate controller, and confirm they hold when Claude sends an out-of-range command.
- Review the eleven high-risk recommendation areas and the AI disclosure duties for any user-facing deployment.
- On Bedrock, remember that continued use on or after Nov. 12 counts as acceptance.
Anthropic says it will seek input from policymakers, experts and civil society as the technology changes. For hardware deployments, the engineering burden lands on operators first.
Frequently Asked Questions
Do the hardware rules apply to consumer robots and smart home devices?
Not when the device stays within its built-in safety limits and its worst outcome is discomfort or inconvenience. The exclusion for consumer devices is written that narrowly, and the policy does not say how it treats a consumer device driven past those limits, so owners of such setups should check the six triggers.
What happens to Claude-controlled equipment if the connection drops?
The equipment must stop or hold a safe state. The policy does not say how long a lapse counts as lost, so operators must choose and test that threshold themselves.
Does reviewing Claude's plans before they run exempt a setup?
Yes. Plans, code or commands reviewed by a qualified person before execution are excluded from the section. The exclusion does not cover setups where Claude's output reaches the equipment unreviewed.
Has Anthropic banned personalized political targeting?
No. The announcement says the blanket ban was removed. Deceptive campaigns and artificial activity remain prohibited.
