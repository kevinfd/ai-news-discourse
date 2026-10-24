---
id: "73e119ffe8787b97"
title: "PHP2Shell was only the beginning: AI is accelerating the patch race"
url: "https://thenewstack.io/php2shell-ai-patch-race"
link: "https://thenewstack.io/php2shell-ai-patch-race"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T14:00:00Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Matthew Weier O’Phinney"]
language: "en"
summary: "Government websites and public services across Europe went offline this week as organizations responded to two newly disclosed PHP vulnerabilities. Germany took several federal websites offline, France temporarily shut down prefecture sites, Belgium’s foreign ministry disabled its websites, and organizations in the Netherlands pulled public-facing services as a precaution. It wasn’t confined to…"
tags: ["AI", "Open Source", "Security", "sponsor-perforce", "sponsored-post-contributed"]
orgs: ["OpenAI"]
topics: ["models & research", "products & launches", "policy & regulation"]
content_source: "fulltext"
word_count: 1242
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# PHP2Shell was only the beginning: AI is accelerating the patch race

The New Stack · Matthew Weier O’Phinney · 2026-10-23

PHP2Shell was only the beginning: AI is accelerating the patch race
Government websites and public services across Europe went offline this week as organizations responded to two newly disclosed PHP vulnerabilities. Germany took several federal websites offline, France temporarily shut down prefecture sites, Belgium’s foreign ministry disabled its websites, and organizations in the Netherlands pulled public-facing services as a precaution. It wasn’t confined to Europe, with countless other entities and businesses worldwide responding similarly.
They were all waiting for a PHP vulnerability mitigation that didn’t exist yet.
The cause was PHP2Shell: CVE-2026-109618 and CVE-2026-109619. While the community worked quickly and the PHP project released fixes for all community-supported PHP versions on the morning of October 21, the bigger issue remains unresolved: an estimated 40% of PHP users are running unsupported PHP, even as AI has exponentially accelerated CVE discovery.
“What happened this week was different, and it’s the first shot of what promises to be an ongoing battle across the open-source ecosystem.”
I’ve been contributing to open source for more than 20 years; I lead the Laminas Project, I’m the Principal Product Manager for Perforce Zend and OpenLogic, and I currently serve on the Board of the PHP Foundation — which is all to say, I’ve seen more than my fair share of new security threats.
What happened this week was different, and it’s the first shot of what promises to be an ongoing battle across the open-source ecosystem.
What you need to know about PHP2Shell
CVE-2026-109618 and CVE-2026-109619, currently referred to as PHP2Shell, present remote code execution (RCE) risks triggered by a combination of out-of-memory (OOM) conditions and PHP’s error handling. Every PHP version back to 5.4 is affected by at least one. The two vulnerabilities are particularly concerning because they exist in PHP itself rather than in an individual application, CMS, or framework; there is no real mitigation outside patched PHP runtimes.
Wiz Research found that the vulnerabilities could allow attackers to remotely execute code or expose sensitive information in process memory, including passwords, authentication tokens, API keys, and certificates. This exposure exists independently of the application running on PHP.
Additionally, Datadog Security Labs, which independently reproduced the vulnerabilities, found that application-level authentication cannot prevent the attack because PHP processes the malicious request before application code runs. In its reproduction of CVE-2026-109618, researchers reported that the request “never reaches the target application’s code.”
“Even with solid application security practices, your applications could still be exposed because the vulnerable behavior happens below the application, in the PHP runtime itself.”
This means that even with solid application security practices, your applications could still be exposed because the vulnerable behavior happens below the application, in the PHP runtime itself.
The answer is to patch.
The community takes a collaborative effort
Once the full impact became clear in August, the PHP Ecosystem Security Team, the PHP Foundation, and release managers delivered a fix across every supported PHP version. In a cross-ecosystem effort, they also worked with LTS vendors (such as Zend) to ensure they created and released all patches simultaneously.
This is the first time in 20+ years I’ve seen an effort like this happen, and I applaud the community for moving in this direction. Because of this initiative, anyone on a PHP version no longer supported by the community (8.1 or older) could remain secure against these newly disclosed CVEs without any gaps.
Unfortunately, this kind of cooperation also depends on trust, which was tested here. The CVE numbers were leaked on October 20, moving all releases up by a day. But as of 14:00 UTC on October 21, all community-supported PHP versions have received updates to mitigate these vulnerabilities. My team at Zend, along with other LTS providers, also released patches for EOL PHP versions.
While we’ll need more comprehensive steps in the coming weeks, these mitigations will keep critical applications that power governments, hospitals, financial institutions, schools, and more secure and supported in the interim.
AI is changing the economics of vulnerability research
PHP2Shell is a prime example of what happens when AI makes difficult security research more accessible — and the dangers that come with that knowledge.
As part of OpenAI’s Patch the Planet initiative, Calif identified a critical PHP flaw using GPT-5.6 Sol. PHP’s maintainers led the fixes and release, with researchers and security providers contributing testing, technical support, and coordination ahead of disclosure.
“We’ve always raced vulnerability disclosure, patch availability, and exploitation. PHP2Shell demonstrates just how uncomfortable and hard-won that race can, and likely will, become.”
What stands out is the potential shift in scale. OpenAI says these are already among several significant vulnerabilities it has found and is working to address, and it expects similar findings to “increase sharply in the coming months.”
We’ve always raced vulnerability disclosure, patch availability, and exploitation. PHP2Shell demonstrates just how uncomfortable and hard-won that race can, and likely will, become.
Running EOL OSS? AI is raising the stakes.
The easy advice after a vulnerability like PHP2Shell is to upgrade immediately. The operational reality is more complicated.
PHP 8.1 and older releases no longer receive updates from the PHP project, although some distributions and long-term support vendors provide backported security fixes. For critical applications, moving to a new runtime can require updates to frameworks, libraries, extensions, and application code, plus the testing needed to ensure those changes don’t disrupt production.
That gap grows as AI improves vulnerability research, so this isn’t just a PHP issue. PHP is just the first major example of what’s coming for most popular OSS technologies. For instance, we’ve seen a recent flood of Spring vulnerability reports in the past few months, and Node.js and Python reported critical vulnerabilities the same day PHP2Shell landed. I’d also be remiss not to mention Linus Torvalds’ recent comments that the Linux security list is becoming unmanageable because of AI bug reports.
During my time working with OSS and PHP at Perforce Software, I’ve come to view LTS as a bridge to modernization. It lets teams keep addressing security vulnerabilities while they plan, test, and execute a move to a supported version. And, as vulnerability discovery accelerates, remaining indefinitely on unsupported software becomes increasingly difficult to justify.
Organizations need to stay current where they can and have a deliberate security strategy for the systems they can’t upgrade immediately. The faster vulnerabilities are discovered, the more important this will become.
What happens now?
For PHP users, the immediate priority is straightforward: move to a fixed release or obtain appropriate security fixes for an otherwise unsupported version. But let’s talk more long-term.
It can be tempting to use PHP2Shell as evidence that PHP is suddenly less secure, but that couldn’t be further from the truth. The combined community and vendor effort this week proves that. Instead, we need to change our outlook on security, because vulnerabilities like these will only become more common.
“Yes, our capacity to find difficult security problems has improved. But our ability to respond needs to keep pace.”
AI is changing which security investigations are practical and how quickly they can happen. That’s valuable when researchers are working with projects and the wider ecosystem to resolve vulnerabilities. But it also puts more pressure on organizations to know what they’re running, stay on supported releases when possible, establish clear vulnerability-response processes, and have a plan for applications that cannot be upgraded immediately.
Yes, our capacity to find difficult security problems has improved. But our ability to respond needs to keep pace.
