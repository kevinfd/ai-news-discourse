---
id: "675688a598b63b69"
title: "AI Agents Behaving Badly: Four Security Rules For The Agentic AI Age"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/10/ai-agents-behaving-badly-four-security-rules-for-the-agentic-ai-age"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/10/ai-agents-behaving-badly-four-security-rules-for-the-agentic-ai-age"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-10T12:00:00Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Srinivas Shekar, Forbes Councils Member"]
language: "en"
summary: "In a world where malicious bots and benevolent agents co-exist, how do we tell them apart? And what happens when we can’t?"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Microsoft"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 824
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6ae22c54c40811ddcf5bed5e/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# AI Agents Behaving Badly: Four Security Rules For The Agentic AI Age

Forbes · Srinivas Shekar, Forbes Councils Member · 2026-11-10

Srinivas Shekar, Founder and CEO, Pantherun Technologies.
Bots now generate over 57% of all web traffic, compared with less than 43% of human activity. This is only set to expand as agentic AI proves its mettle in online shopping, research, cloud administration, customer service and more. But enterprise security systems were designed to give approved human users access while blocking human and machine intruders.
It isn’t just about overcoming the “prove you’re an approved human” paradigm that legacy security systems were built on. It’s also about dynamism. After all, humans have stable identities and permissions that can be established and recognized. But AI agents create subagents and change their behavior according to the task they’re executing. They can communicate and interact like humans, but they can also make API calls, move data, consume machine-readable streams, interact directly with enterprise infrastructure, create software tools on the spot and perform thousands of operations simultaneously.
In a world where malicious bots and benevolent agents co-exist, how do we tell them apart? And what happens when we can’t?
AI Agents Behaving Badly
Malicious AI agents are already getting into places they shouldn’t be and executing actions. In July 2026, the agentic ransomware attack known as JadePuffer exploited a flaw in the AI development tool Langflow to conduct reconnaissance, steal credentials, encrypt files and demand a bitcoin ransom for release. Once inside, the agent determined what opportunities to exploit, attacked several avenues simultaneously, generated attack code dynamically and adapted its own code in real time, until it achieved success. The agent also created software on the fly, allowing it to move ransomware from a compromised container onto the host. It even wrote its own ransom note!
And then there’s the speed element. Ransomware attacks traditionally required coordination among a team of highly skilled hackers. But now, autonomous agents can collapse the cost, skill and time required to execute an entire intrusion. The time it took for JadePuffer to destroy the production database was about 30 minutes.
Four Security Rules For Agentic AI
This introduces a range of new security concerns specific to the age of AI: How do you verify agent identity? What data do you allow agents to access? How do you identify and intervene when an approved agent begins acting beyond its approved mission? And how do you ensure that today’s permissions don’t become tomorrow’s liabilities? Here are a few ideas:
1. Give every agent an identity.
It’s tempting to think about agents as mere extensions of the humans they represent. But humans and agents have different capabilities and different senses of discernment. Don’t expect your security systems to safeguard against bad agent behavior if you treat them as their respective trusted human handlers. Instead, give every agent a distinct machine identity that can be logged and analyzed. Microsoft’s Entra Agent ID, for example, now treats agents as unique user identities.
3. Remember to forget.
When your human staff are at home sleeping, what they know about your company is inaccessible by thieves. But agent memory becomes a new data repository that can be exploited by bad actors. Consider carefully what agents may remember and for how long they may remember it. Highly sensitive information like passwords and decryption keys, and even login paths to sensitive systems, might be better off forgotten by agents between sessions.
4. Keep your keys close to the chest.
Imagine that an agent requests access to an encrypted database. The system decrypts it, with permission. But then the agent steps out of line, converting the underlying data into plain text and storing it somewhere else, where it’s vulnerable to unauthorized access. In this case, your own agent is “innocent” but your data still gets breached.
Here’s another scenario: An agent is given cryptographic keys for one mission, but you fail to limit its permissions and wipe its memory. When it runs another unrelated mission, it decides to use those keys again to access data that shouldn’t be used in this case.
To avoid these kinds of scenarios, be very, very careful about what cryptographic keys you put in agents’ hands, and even more careful about letting agents retain persistent keys. Use keyless encryption if you can, so that agents don’t carry the keys to the castle around their virtual necks. Make decryption policy-aware, so that the ability to decrypt data doesn’t automatically confer the right to do so. And, whatever you do, maintain a zero-trust stance, so that humans and agents must always reconfirm their identity and permissions for every session.
Conclusion
The rise of agentic AI makes “zero trust” more important than ever. In the agentic era, identity, authority, memory and access all need to be treated as temporary and continuously reassessed. The goal isn’t to “keep bots out.” It’s to let the “good bots” in, without handing them the freedom to behave badly.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
