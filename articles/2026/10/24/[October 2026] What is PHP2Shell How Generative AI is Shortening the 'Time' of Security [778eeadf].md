---
id: "778eeadffed4f86d"
title: "[October 2026] What is PHP2Shell? How Generative AI is Shortening the 'Time' of Security"
url: "https://note.com/masaland/n/n1bda3e5bc53f?hl=en"
link: "https://note.com/masaland/n/n1bda3e5bc53f?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-24T00:06:00Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Masaland"]
language: "en"
summary: "There is a hole that we haven't been able to find a way to exploit for about two years.Although signs were caught in a 2024 audit, no specific attack method had been found. The severity of this was ..."
tags: []
orgs: ["Amazon"]
topics: ["business & funding"]
content_source: "fulltext"
word_count: 2323
paywalled: false
image: "http://www.bing.com/th?id=ONUT.3xer6QohSCmvaPjGEbOXJQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# [October 2026] What is PHP2Shell? How Generative AI is Shortening the 'Time' of Security

note · Masaland · 2026-10-24

[October 2026] What is PHP2Shell? How Generative AI is Shortening the 'Time' of Security
There is a hole that we haven't been able to find a way to exploit for about two years.
Although signs were caught in a 2024 audit, no specific attack method had been found. The severity of this was uncovered in the summer of 2026 by an investigation using generative AI.
On October 21, 2026, a patched version was released for two critical vulnerabilities (software weaknesses) in PHP, collectively known as "PHP2Shell." Preventive shutdowns occurred at sites ranging from online banking to airlines, and Prime Minister Takaichi also used her X account to urge preparations for applying the patch immediately.
Hello! This is Masaland.
There are already many articles summarizing "what to do today." In this article, I will take a step back, re-read the facts that have become clear after one day through the lens of "generative AI," and consider what will change from here on out. I have written a brief summary of the minimum necessary actions at the end.
Conclusion first
- There have been millions of attempted attacks. However, as of October 23, there are no confirmed or reported cases of intrusion via PHP2Shell. "Being attacked" and "being intruded upon" are different things.
- Generative AI was used in the investigation that uncovered the severity of the hole. The same tool can be used by the attacking side as well.
- From now on, the number of holes found will increase, and the time from disclosure to exploitation will shorten. That is how Masaland sees it.
- Therefore, the defending side also needs a system that incorporates generative AI. However, it is humans who make the decisions.
What is PHP2Shell?
In a nutshell
It is a flaw that could allow an unauthenticated external party to take over a web server running PHP.
PHP is a programming language that runs on the back end (server) of a website. Sites built with WordPress also run on PHP. According to W3Techs, about 70% (69.3% as of October 2026) of websites whose server-side language is known use PHP.
The CVSS (an international metric that expresses the severity of vulnerabilities from 0 to 10) for both issues is 9.2, classifying them as the most severe "Critical." However, success is not easy for just anyone. The official PHP announcement states that the conditions for a successful attack are complex.
Mechanism (an analogy)
Every time PHP is accessed, it prepares a working memory (a place to temporarily store data) like a "work desk" and cleans it up when finished. However, there were cases where a "note" pointing to a desk that should have been cleaned up remained. If an attacker places crafted data on that desk, PHP trusts the note, reads it, and acts according to those instructions. In the worst case, the server can be taken over.
"It's not dangerous because it's PHP"
The hole was not in the programs of individual sites, but in the core that runs PHP. It is not a mistake by the people who built the sites with PHP. Like Apache Struts2 in 2017 or Log4Shell in 2021, critical holes can be found in any language or software. It was widely reported only because it is so widely used.
It affects a wide range of versions from PHP 5.4 onwards (Wiz, etc.). Since the problem lies within the PHP core itself, updating WordPress or plugins will not fix it. The claim that spread on the first day that "updating WordPress will fix it" was incorrect.
What we have learned after one day
Millions of attempts. No confirmed or reported breaches yet
According to Cloudflare CEO Matthew Prince, the attack attempts observed by the company went from thousands in the 10 hours before the announcement to hundreds of thousands within two hours after the announcement, and reached millions thereafter.
However, this is the number of "attempts." On the 22nd (US time), the WordPress security firm Wordfence reported that it had not confirmed any successful intrusions across the more than 5 million sites it protects, while also emphasizing that the inability to confirm an intrusion is not proof of safety. The "22.6 million or more potentially affected PHP instances" cited by Palo Alto Networks is also a count of targets that could be aimed at, not a count of actual victims.
Attempts began four days before the patched version
Amazon's honeypot (a decoy server used to observe attacks) recorded the first attack attempt on October 17, four days before the patched version was released. Amazon recommends that investigations begin with logs from October 17 onwards.
In Japan, they stopped, inspected, and restored
From the 21st to the 22nd, companies and organizations in Japan, including those in banking, telecommunications, and aviation, stopped parts of their sites and services as a precaution. The US NSA (National Security Agency) also recommended disconnecting systems from the internet if they could not be updated immediately. Many major rental server providers announced that they had finished applying patches during the 22nd.
"A patch has been released" is not the same as "it is fixed"
Many servers incorporate PHP through the OS (Linux distributions), Docker (a mechanism for packaging and distributing app environments), or cloud components. In this case, you have no choice but to wait until the distributor rebuilds and delivers the patched version. The patched version of Amazon Linux 2023 was released on the 22nd, and official Docker images were distributed sequentially starting shortly after 1:30 AM on the 22nd, with all types becoming available around 7:00 AM. Even if the patch is provided to the distributor in advance, there is a time lag before it reaches the user's hands.
What has generative AI changed?
The speed of discovery has changed
As mentioned at the beginning, signs of one of the two issues had been detected since the 2024 audit, but no specific attack method had been found.
It was the reports received from August 2026 onwards that clarified the severity. In August, security firms Calif and Wiz reported it, and OpenAI independently reported the same cause, while also communicating yet another attack vector in September. Generative AI was used in that investigation, and Wiz explained that "generative AI contributed significantly to the discovery." They also wrote that a single researcher completed in about a week what would have taken a world-class team several months in the past (this is Wiz's own assessment).
The attackers have the same tools
Wiz further points out that using generative AI makes it easier to adjust attack code to match PHP versions and configurations. A 2024 study by the University of Illinois found that when an AI using GPT-4 was given a description of a vulnerability, it could exploit 87% of 15 known vulnerabilities in an experimental environment. Without the description, it was 7%.
It is unknown whether the attackers in this case used generative AI. What can be said is that the same tools are in the hands of the attackers.
The defenders are starting to use it, too
Since the beginning of 2026, the PHP Foundation, a non-profit organization that supports PHP development, has been working with Alpha-Omega, an organization that supports open-source security, to inspect the PHP core using generative AI. Security teams have also begun using generative AI to verify incoming reports and organize reports with the same root cause. However, they maintain that 'all decisions are made by humans.'
What will happen from here on?
From this point on, these are Masaland's projections based on the facts presented so far.
1. The number of vulnerabilities found will increase
According to the PHP Foundation, as research using generative AI has spread, the PHP security team has received far more reports than ever before. AI is reaching vulnerabilities that human eyes could not. We believe this is just the beginning.
2. The fixers will not be able to keep up
This particular incident took about two years from the initial signs to the fix. The PHP Foundation has admitted that this was a 'structural failure' due to the way decisions were made and a lack of manpower. Even software that supports websites around the world, like PHP, is often maintained by a limited number of people. Even if the speed of discovery increases, if the speed of fixing remains the same, vulnerabilities will continue to persist in the meantime.
3. The time from disclosure to exploitation will shrink
In this case, there were attempts at attacks four days before the fixed version was released. There is also research showing that many known vulnerabilities could be exploited just by providing a description. We are entering an era where saying 'let's deal with it next week' after a fixed version is released will no longer be in time.
4. The time lag of 'distributors' will become a weak point
Even when a fixed version is released, many servers cannot be fixed until 'distributors' such as Linux distributions or Docker rebuild their packages. The more the time until exploitation shrinks, the more this gap of several hours to several days becomes a dangerous window of time.
5. Generative AI will become a prerequisite for defenders, too
Trying to keep up with human hands alone will no longer be enough. For example, consider the following system:
- Keep a list of components up to date: Which software and which version is running on which server? Have generative AI extract this from configuration files and repositories to create a list. When an announcement is made, this list is the first thing to check.
- Monitor vulnerability information daily: Have generative AI summarize official advisories, JPCERT/CC reports, and vendor notices to check every morning if they relate to anything on your list. You can read English information immediately, too.
- Draft impact assessments and procedures: If something relevant is found, have generative AI draft the scope of impact and update procedures, which a human then verifies and executes.
- Get help with verification after fixing: Has the version number changed? Is there any suspicious traffic in the logs? Organize the points to look for together with generative AI.
At every stage, it is humans who make the decisions. Generative AI plays the role of shortening the time it takes for humans to make those decisions.
In this case, you can ask generative AI as follows.
- Checking the number: 'The next step is to display the PHP version. Please check it against the official PHP advisory number GHSA-6wmf-4rv5-p3rp to see if it is a patched version of PHP2Shell. If you do not know, please say you do not know.'
- Interpreting announcements: 'From the following provider announcement, please extract whether the PHP2Shell patch has been applied and the date and time it was done. Do not speculate on anything that is not written.'
- Checking logs: 'I will check the access logs from October 17th onwards. Please list the steps on what to look for and how to identify traffic targeting PHP2Shell.'
Adding phrases like 'If you don't know, say you don't know' and 'Do not speculate' makes it easier to reduce plausible fabrications (hallucinations). However, please note the following points.
- Generative AI without search functionality does not know information newer than its training cutoff. Always verify patched numbers against official advisories.
- Do not paste logs or settings as they are. Mask passwords and customer information, and follow your company's rules.
- Settings or code written by generative AI may specify older versions from the time of its training. A 2025 study by Veracode in the US found that approximately 45% of code written by generative AI contained security vulnerabilities.
Summary
- What we learned after one day is that while attempted attacks reached millions, there are no confirmed or publicized cases of intrusion via PHP2Shell.
- What generative AI has changed is the 'time' of security. The time until a hole is found and the time until it is exploited are both shortened. If the patching side and the distribution side cannot keep up, that gap becomes a dangerous period.
- Therefore, the defending side also needs a system that incorporates generative AI. However, it is people who make the decisions.
- What to do today is not to be relieved that 'a patch has been released,' but to see it through until 'the number has changed.' If you manage a site, perform updates, restarts, and check logs from October 17th onwards. If you leave it to a vendor, confirm the date and time the patch was applied.
The tools used to find holes can also become tools for defense. It is people who master them and make the final decisions.
Reference Information
Official/Government
- PHP Official Security Advisory GHSA-6wmf-4rv5-p3rp (CVE-2026-109619)
- PHP Official: 2026 News (Advance notice on October 20, release announcement on the 21st)
- JPCERT/CC: List of Alerts (October 22, 2026, Multiple Vulnerabilities in PHP)
- IPA: Regarding Countermeasures for PHP Vulnerabilities (Advance notice October 21, 2026)
Announcements and summaries from companies and research institutions
- PHP Foundation: Today's PHP security release and how we're strengthening PHP security
- Wiz: PHP2Shell
- Amazon Threat Intelligence: Observations of PHP2Shell exploitation prior to public disclosure
- Amazon Linux Security Center: CVE-2026-109618
- Wordfence: Attacks on PHP2Shell Continue, But No Known Compromises as a Result Yet
- Jinrai: Status of PHP vulnerability response | 15 rental server companies and major services (as of 10:00 PM on October 22)
- Docker Official Images: Updating to patched PHP versions (docker-library/official-images #22541)
- Fang et al. (2024) LLM Agents can Autonomously Exploit One-day Vulnerabilities
- Veracode: 2025 GenAI Code Security Report
News Reports
- ITmedia NEWS: Millions of attempts to exploit 'emergency' PHP vulnerability, Cloudflare CEO reports
- TechTarget Japan: 22.6 million affected by PHP vulnerability 'PHP2Shell'; Emergency checklist for IT departments
- Jiji Dot Com: PHP vulnerability, service outages spreading; banks and other companies and organizations take preventive measures
