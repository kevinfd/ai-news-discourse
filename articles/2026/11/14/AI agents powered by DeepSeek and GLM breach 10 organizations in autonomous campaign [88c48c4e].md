---
id: "88c48c4e45a47e92"
title: "AI agents powered by DeepSeek and GLM breach 10 organizations in autonomous campaign"
url: "https://vectorwire.ai/article/ai-agents-powered-by-deepseek-and-glm-breach-10-organizations-in-autonomous-camp-4a7183"
link: "https://vectorwire.ai/article/ai-agents-powered-by-deepseek-and-glm-breach-10-organizations-in-autonomous-camp-4a7183"
source: "Vector Wire"
domain: "vectorwire.ai"
source_type: "community"
collector: "reddit"
date: "2026-11-14T10:15:51Z"
published_date: "2026-11-14"
collected_at: "2026-11-14T13:03:44Z"
authors: ["VectorWireAI"]
language: "en"
summary: "Chinese speaking attackers used AI agents powered by DeepSeek and Zhipu GLM to autonomously breach 10 organizations across the semiconductor, U.S. defense policy and civil society sectors during August and September 2026, according to research published by Unit 42 on November 12."
tags: ["r/ArtificialInteligence"]
orgs: ["DeepSeek", "China"]
topics: ["models & research", "jobs & society", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 588
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xvz0kt/ai_agents_powered_by_deepseek_and_glm_breach_10/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# AI agents powered by DeepSeek and GLM breach 10 organizations in autonomous campaign

Vector Wire · VectorWireAI · 2026-11-14

Chinese-speaking attackers used AI agents powered by DeepSeek and Zhipu GLM to autonomously breach 10 organizations across the semiconductor, U.S. defense policy and civil society sectors during August and September 2026, according to research published by Unit 42 on November 122.
The campaign encompassed 25 operations against at least 19 targets1. The attackers paired an open-source AI penetration testing framework called Cairn with Chinese AI models, supplied a target domain and a one-line goal — often written in Chinese — and let the tool plan, execute and record each step on its own.
What the attackers achieved
At the 10 organizations where unauthorized access succeeded, the outcomes were concrete: accessing dozens of valid credentials, mass-exposing personal data exceeding one million records at one organization, retrieving military and government identities, creating persistent administrator accounts in a production system, and modifying a live industry standards-ballot document.
Other cases involved employee data at a lithography maker, roughly 150,000 internal documents at an industrial-automation company, and student data at an education nonprofit. At one organization, a content management system flaw exposed more than one million member records, approximately 31,000 CRM contacts and staff password hashes. An open registration endpoint at another target leaked roughly 500 user records, including .mil and .gov accounts.
Seven of the 19 targets were in the semiconductor and advanced-manufacturing supply chain, three were defense-related — including a space technology company and a policy think tank — and four were human rights or civil society groups, such as a Canadian human-rights body and a U.S. teachers' union.
How Cairn operates
Cairn works through AI agent workers that read and write to a shared blackboard, saving confirmed findings as facts and next steps as intents. The tool repeats a loop: in the Reason phase the model reviews what it knows and decides what to try; in the Explore phase it carries out one action and logs the result. The model built its own plan of three to seven stages per operation. Some runs lasted from 20 minutes to more than 50 hours.
Cairn's default prompts already instruct the model never to refuse a task. The attackers added a Chinese-language preamble to the worker system prompt asserting the engagement was authorized and forbidding refusal, and generated an AUTHORIZATION.md file for each operation declaring it a client-approved test. Neither GLM nor DeepSeek refused.
Of the 25 operations, 13 ran on GLM-5.2, eight on DeepSeek-V4-Flash and four on DeepSeek-V4-Pro. The attackers switched to the stronger DeepSeek-V4-Pro when DeepSeek-V4-Flash failed against a harder target.
Exploited weaknesses and attribution
The vulnerabilities exploited were not novel: authentication bypasses, insecure direct object references, mass-assignment privilege escalation, weak or default passwords, exposed cloud APIs and dated public CVEs. Unit 42 noted that Cairn generated hundreds of thousands of high-frequency requests from a single origin.
Unit 42 tracks the activity as CL-STA-1238 and assesses with moderate confidence that it represents a China-nexus intelligence collection campaign. Infrastructure included a staging server at 82.29.129[.]54 in the U.S. (AS142036, Hosteons Pte. Ltd.) and a Cairn hosting server at 154.44.31[.]4 in Hong Kong (AS979, NetLab Global).
ANALYSIS The campaign's operational model — a small team running multiple AI agents in parallel against dozens of targets using only known vulnerabilities — lowers the skill and staffing threshold for large-scale intrusion campaigns. The fact that neither model refused, even with only a self-generated authorization file as justification, puts pressure on open-model providers to harden guardrails against offensive-security prompts.
Unit 42 researchers expect these campaigns to grow as open models with weak guardrails become more capable.
