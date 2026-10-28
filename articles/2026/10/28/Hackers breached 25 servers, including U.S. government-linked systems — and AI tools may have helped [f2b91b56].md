---
id: "f2b91b562a412c45"
title: "Hackers breached 25 servers, including U.S. government-linked systems — and AI tools may have helped"
url: "https://tomsguide.com/ai/hackers-breached-25-servers-including-u-s-government-linked-systems-and-ai-tools-may-have-helped"
link: "https://tomsguide.com/ai/hackers-breached-25-servers-including-u-s-government-linked-systems-and-ai-tools-may-have-helped"
source: "Tom's Guide"
domain: "tomsguide.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T08:15:00Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "null"
tags: ["AI", "Online Security", "Computing", "Internet"]
orgs: ["China", "Anthropic", "DeepSeek", "Amazon"]
topics: ["policy & regulation", "models & research", "agents & coding", "business & funding"]
content_source: "fulltext"
word_count: 1141
paywalled: false
image: "https://cdn.mos.cms.futurecdn.net/9JmTabf9SdZjLaW9muABUj-1920-80.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Hackers breached 25 servers, including U.S. government-linked systems — and AI tools may have helped

Tom's Guide · Amanda Caswell · 2026-10-28

Hackers breached 25 servers, including U.S. government-linked systems — and AI tools may have helped
Researchers found hackers' tools included Claude Code, aiscan, DeepSeek and Kimi.
Hackers have reportedly broken into 25 servers across four countries, including systems connected to a U.S. government-affiliated organization. Security researchers also discovered evidence that AI tools may have played a role in the attack.
According to a new report from Dream Research, published Monday, the attackers exploited critical vulnerabilities in PHP, a programming language used by millions of websites, before using another security flaw to gain full control of vulnerable systems.
The attacks targeted servers in the United States, Japan, Taiwan and South Korea. Researchers found evidence pointing to a possible Chinese connection, although they have not identified the attackers or confirmed any government involvement.
What makes the discovery particularly concerning is how far the attackers managed to get. In one U.S. government-affiliated environment, they moved beyond the initial breach and gained access to internal network information, employee account listings and authentication credentials.
And while AI's exact role remains unclear, researchers found several tools in the attacker's environment that raise questions about how AI could be accelerating cyberattacks.
Hackers turned one security flaw into a much bigger attack
The attack started with two critical security flaws, known collectively as PHP2Shell, that were publicly disclosed on October 21.
PHP is used behind the scenes by millions of websites, including WordPress sites and online services. The two vulnerabilities, tracked as CVE-2026-109618 and CVE-2026-109619, can let hackers run malicious commands on vulnerable servers.
Sign up to the Tom's AI Guide weekly newsletter summing up all the biggest AI news you need to know. Plus, analysis from our AI editors and tips on how to use the latest AI tools!
But the attackers didn't stop there. They combined those flaws with another Linux vulnerability called Fragnesia, allowing them to take full control of certain firewall systems without needing a username or password.
According to a Dream Research report shared with Tom's Guide, the entire process could take less than 15 minutes.
The hackers started by scanning roughly 19,000 internet-facing firewalls before narrowing their targets to 240 potentially vulnerable systems. From there, they used automated attacks to breach 24 firewalls and an additional internal management server, bringing the total to 25.
Researchers also found that the hackers had installed malicious web-based tools on many of the compromised systems, giving them a potential way back in even after the initial attack.
The attackers reached a U.S. government-linked network
Arguably, among one of the more concerning discoveries involved three compromised servers linked to a U.S. government-affiliated organization.
After breaking into an internet-facing firewall, the hackers gained access to details about the organization's internal network, including its VPN, login systems and other servers.
They then worked their way deeper into the network, compromising a central firewall management server and stealing an account password. They also obtained a list of users and groups within the organization.
Researchers found evidence that the attackers tried to guess employee passwords, create unauthorized accounts and access additional login credentials, although it's unclear whether those attempts worked.
Dream Research also warned that the hackers may still have had access to some systems when the report was published, but that hasn't been independently confirmed.
The security firm hasn't named the firewall manufacturer or disclosed which software versions were affected, but says it has notified the vendor.
AI tools were discovered in the attacker's environment
Researchers also found signs that the attackers may have used AI. Their tools included Anthropic's Claude Code and an AI-powered security platform called aiscan, configured to work with the Chinese AI models DeepSeek and Kimi.
They also uncovered roughly 40 custom scripts whose consistent formatting and comments suggested some may have been written with AI assistance.
However, Dream Research cautioned that there's no direct evidence AI was used to create the exploits or carry out the attacks. The tools may have been present without playing a role in the breaches.
Still, the findings raise concerns about how hackers could use the same AI coding assistants that developers rely on to write code and troubleshoot problems.
Researchers also found clues suggesting a possible Chinese connection, including Chinese-language prompts, systems set to China's time zone and targets concentrated in the U.S. and East Asia. None of this, however, confirms who was behind the attacks.
Final thoughts
PHP2Shell doesn't directly affect your phone or laptop, but it could put information stored by websites and online services at risk. If attackers compromise those servers, they may gain access to passwords, sensitive data or internal systems.
Dream Research found no evidence that ordinary consumers' personal information was stolen in this campaign. However, the vulnerabilities are already being exploited beyond these 25 servers.
Amazon Web Services detected exploitation attempts as early as October 17, four days before the flaws were publicly disclosed. Sophos has also reported attempted attacks and at least one successful breach.
If you run a WordPress site or online store, check with your hosting provider to make sure PHP is patched. Updating WordPress plugins alone won't necessarily fix the problem. Administrators should also check for signs of compromise, since installing a patch won't remove an attacker who's already gained access.
For everyone else, using unique passwords, enabling two-factor authentication and watching for suspicious login alerts remain sensible precautions.
Follow Tom's Guide on Google News and add us as a preferred source to get our up-to-date news, analysis, and reviews in your feeds. Subscribe to Tom's Guide on YouTube and follow us on TikTok.
More from Tom’s Guide
- I tested ChatGPT vs. Grok with 5 questions boomers actually ask — and the winner surprised me
- Microsoft just offered 60,000 workers a way out as AI spending soars — here's what it could mean for your job
- ChatGPT has a clever new way to fight back against election deepfakes — I tried it and it actually works
Amanda Caswell is the AI Editor at Tom's Guide and one of today’s leading voices in AI and technology. 
A celebrated contributor to various news outlets, her sharp insights and relatable storytelling have earned her a loyal readership. Amanda’s work has been recognized with prestigious honors, including outstanding contribution to media.
Known for her ability to bring clarity to even the most complex topics, Amanda seamlessly blends innovation and creativity, inspiring readers to embrace the power of AI and emerging technologies.
As a certified prompt engineer, she continues to push the boundaries of how humans and AI can work together.
Beyond her journalism career, Amanda is a long-distance runner and mom of three. She lives in New Jersey.
Next Badge:
More Comments/Likes Until Your Next Badge
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
