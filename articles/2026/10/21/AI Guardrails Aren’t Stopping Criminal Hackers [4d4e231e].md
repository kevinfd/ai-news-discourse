---
id: "4d4e231edf522e2b"
title: "AI Guardrails Aren’t Stopping Criminal Hackers"
url: "https://wired.com/story/ai-guardrails-arent-stopping-criminal-hackers"
link: "https://wired.com/story/ai-guardrails-arent-stopping-criminal-hackers"
source: "WIRED"
domain: "wired.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T14:00:00Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Lily Hay Newman"]
language: "en"
summary: "Hackers around the world are all-in on using agentic AI to wage attacks—and manipulating tools like Anthropic’s Claude to help them carry out their crimes."
tags: ["Security", "Security / Cyberattacks and Hacks", "artificial intelligence", "agentic AI", "Anthropic", "Claude", "DeepSeek", "cyberattacks", "hacking", "Crime", "vulnerabilities", "cybersecurity"]
orgs: ["Anthropic", "China"]
topics: ["agents & coding", "models & research", "policy & regulation", "safety & ethics"]
content_source: "fulltext"
word_count: 926
paywalled: false
image: "https://media.wired.com/photos/6ad7cd65322aff8e01d3ff70/master/pass/Security_Claude%20Code's%20Guardrails%20Aren't%20Stopping%20Real-Life%20Attacks_v2.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# AI Guardrails Aren’t Stopping Criminal Hackers

WIRED · Lily Hay Newman · 2026-10-21

As AI adoption spreads among both malicious hackers and defenders, even relatively unsophisticated cybercriminals are incorporating agentic AI into their campaigns and getting around model safeguards, according to new details published on Wednesday about recent successful attacks by four different threat groups.
Researchers from the threat intelligence firm CrowdStrike looked at the AI infrastructure powering attacks perpetrated between May and August by four previously unreported groups—one that operates in Chinese, one in Spanish and English, one in Indonesian, and one in Russian. The former two exhibited sophisticated AI “harnesses,” the software that supports and guides a model to carry out tasks. The latter two showed less technical prowess, researchers found, but were still able to compromise multiple targets. All had left their AI infrastructure openly accessible on web servers, allowing the researchers to analyze their activity and which models they used—largely versions of Anthropic’s Claude as well as versions of the open-weight Deepseek models. All the actors devised ways to allow their campaigns to run autonomously over relatively long periods of time.
“You can leverage different models for different aspects in the operation. Model routing and selection is very important because it’s expensive and a lot of times would be overkill to use newer models,” says Adam Meyers, CrowdStrike's senior vice president of counter adversary work. The researchers observed the attackers using both open- and closed-weight models; in almost all cases, they were using older versions rather than working with frontier models. Meyers notes that doing as much as possible with older models is common in legitimate AI usage, too, as costs mount.
The attackers also used multiple models to take advantage of differences in the guardrails meant to prevent people from using AI to carry out digital attacks.
“The models don't all have equivalent guardrails and protections, even from one company,” Meyers says. He adds about the sophistication of the hacking campaigns overall that “these attacks are not using new exploits or novel vulnerabilities. They’re really just taking advantage of the speed and the volume that you can use AI for in conducting these operations targeting the bulk of security hygiene issues in a lot of these environments—things that were preventable but weren’t prevented.”
The researchers found that all four threat actors circumvented AI safeguards, often by convincing a model that the activity was all legitimate and authorized, often for penetration testing or other security evaluation. One method used by many of the groups involves adding files to an agent’s working directory to try to show that tasks are approved and authorized. The attackers also used traditional jailbreaking methods, crafting prompts and narratives framing their hacking as authorized and benign, and proactively addressing potential questions or concerns the models might raise. The more sophisticated actors were typically more strategic in their world-building, while the less sophisticated actors sometimes resorted to more crude and aggressive prompts that tried to bully the models into accepting that the activity was legitimate.
The Chinese-speaking actor also used what's known as a “run time patch,” in this case a tool known as ClawGod, to add functionality on top of Claude Code and attempt to remove the “CYBER_RISK_INSTRUCTION” from the Claude Code system prompt, an instruction directing Claude Code to only participate in authorized security testing, not abusive or destructive hacking.
The actor that worked in Spanish and English targeted Argentine health care entities and successfully compromised at least 15 organizations. CrowdStrike researchers see evidence that the actor stole credentials and medical records from at least one of these victims. The actor special built a penetration testing harness, the kind an organization would use to test its own infrastructure, to find and fix vulnerabilities. Using models including Claude Opus 4.5, Claude Haiku 4.5, and Deepseek V4 Pro, the group set up a full infrastructure for autonomous attacks involving a “Supervisor” Claude Code agent to direct the steps of an attack and an “Executor” agent to carry them out.
The attacker working in Chinese also built penetration testing harnesses to guide Claude Code in reconnaissance and then autonomously attack once a human had selected a course of action. The researchers found that the actor successfully compromised government targets in both Brazil and Colombia and also targeted private organizations in Brazil and the United States in a range of sectors that include biotech, healthcare, food and beverage, retail, technology, and travel.
According to the researchers, the Chinese-speaking actor primarily relied on Claude Opus 4.8, but also used other models including Claude Sonnet 4.6 and Deepseek Chat. The actor accessed Claude through an AI proxy service based in China but set up multiple fallbacks to other AI tools if Claude was not available through the proxy.
Anthropic did not provide comment ahead of publication, and Deepseek did not immediately respond to WIRED's requests for comment.
The researchers say that both the Russian-speaking actor, which seems to have been focused on financially motivated “e-crime,” and the Indonesian-speaking actor (the least sophisticated of the four) used more basic, publicly available skills and harnesses to carry out their attacks. But both were still successful at compromising targets. This included multiple Indonesian government domains, a Bangladeshi government domain, and some private-sector targets, in the case of the Indonesian-speaking actor.
“What we are seeing is humans are doing some of the initial probing in these situations and then they’re engaging the AI for the hacking at scale,” CrowdStrike’s Meyers says. “I find it interesting that even with agentic attacks with all of these capabilities, we could still see that there’s a human behind it and what they’re up to.”
