---
id: "5316d14cfc395661"
title: "PHP2Shell: Haven’t patched yet? Take these steps now to mitigate"
url: "https://zdnet.com/tech/php2shell-php-patch-mitigation-critical-exploit"
link: "https://zdnet.com/tech/php2shell-php-patch-mitigation-critical-exploit"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T15:09:47Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Charlie Osborne"]
language: "en"
summary: "The PHP Project provides instructions to stop further RCE exploits in limited settings."
tags: ["Security"]
orgs: ["Amazon"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 757
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/digitallockGettyImages-2300746116.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# PHP2Shell: Haven’t patched yet? Take these steps now to mitigate

ZDNet · Charlie Osborne · 2026-10-23

ZDNET’s key takeaways
- The disclosure of critical bugs in PHP leads to an urgent rush to patch.
- Cybercriminals are likely to weaponize these vulnerabilities.
- Organizations should act now to prevent exploitation.
A flaw in PHP triggered a worldwide scramble to patch vulnerable websites, and now, further instructions have been issued by the PHP Project to prevent “an unlikely Remote Code Execution (RCE) vector” in PHP2Shell attacks.
What is PHP2Shell?
PHP2Shell refers to a pair of PHP vulnerabilities, CVE-2026-109618 and CVE-2026-109619, that have each earned critical severity scores of 9.2 and impact most PHP builds. The PHP Project released patches to fix these bugs on Wednesday, and the critical nature of these flaws prompted a worldwide scramble to apply PHP’s fixes as quickly as possible.
More from ZDNET
Why the rush? Because PHP (a recursive acronym for Hypertext Preprocessor) is a general-purpose programming language that provides the backbone for many of the websites and services we access daily — everything from WordPress websites to e-commerce platforms.
According to Wiz’s security team, which discovered the vulnerabilities with the help of AI, PHP can be found on 70% of the world’s websites.
Urgent patches and rapid attacks
“These vulnerabilities include memory disclosure and unauthenticated remote code execution in PHP itself, independent of the application running on top of it, putting every affected website in immediate risk,” Wiz says.
Armed with these vulnerabilities and targeting an unpatched system, attackers could execute code on affected servers or read sensitive process memory, stealing data and infiltrating corporate networks in the process.
Also: AI a ‘force multiplier’ for low-skilled threat actors
Wiz goes on to make an interesting point: While AI assisted in the discovery of these vulnerabilities, AI could also be used to exploit them. Developing an attack chain and demonstrating the exploitability of these bugs “required an exceptionally complex chain of steps,” according to the researchers, which would be “at the edge of what human researchers could practically achieve.” However, frontier AI models “substantially reduced that barrier, turning a longstanding flaw into an exploit.”
According to Amazon Threat Intelligence, attempts to exploit P2P2Shell were already happening four days before the vulnerabilities were made public. Proof-of-concept works started appearing hours later. A threat actor tied to P2P2Shell attack chains is attempting to deploy a Mirai-style botnet, and Cloudflare CEO Matthew Prince says that the Cloudflare network is now recording “millions” of exploitation attempts.
Further guidance
In an advisory published October 23, PHP Project urged organizations to do the following: set session.upload_progress.enabled=0 until the next round of scheduled bug fixes in PHP. While already listed as a mitigation in the October 21 release, now that there has been time to investigate PHP2Shell further, applying this mitigation can protect against a different Remote Code Execution (RCE) vector.
Also: Best VPN services: Expert tested
Because this RCE, now recorded as CVE-2026-115560, requires an unusual configuration and application code setup, the attack vector is considered “unlikely”; therefore, mitigation will suffice until it is handled by PHP Project in the regular release cycle.
“An application must set session.serialize_handler to php_binary or php_serialize in its configuration and then switch it to php at runtime with ini_set() before calling session_start(),” PHP Project said in its advisory. “Session upload progress must also still be enabled. Applications that never change the serialize handler at runtime can keep the feature enabled.”
How organizations should act
PHP Project is urging users to act immediately by updating to PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35. If it isn’t possible to patch immediately, organizations can implement mitigations included in its advisory.
The National Security Agency (NSA) advised “heightened awareness” of PHP2Shell over the coming weeks, saying that any and all vendor-issued patches tied to PHP2Shell should be prioritized. Companies should also consider applying mitigative steps, such as enhanced logging and replacing end-of-life PHP packages, when appropriate.
Also: 7 privacy settings I change ASAP on every new phone
“All users should immediately conduct an inventory, where feasible, of hardware and software services reliant on now-vulnerable PHP versions,” the agency added. “Vigilance in applying patches related to those systems is paramount.”
Speaking to ZDNET, Matthew Weier O’Phinney, principal product manager of Perforce Zend and OpenLogic, said that most open source software and commercial LTS software distributions had patches available either at the time of the coordinated release or within a few hours following, and if you’re using PHP, it’s likely a fix is available to you now.
“Assuming you use one of those, using your system package manager to update is a quick remedy,” O’Phinney added.
