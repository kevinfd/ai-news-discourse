---
id: "9fb8cfefef079b87"
title: "AI found flaws in the code behind 70% of the web. The fix took two months."
url: "https://thenewstack.io/ai-php2shell-disclosure-framework"
link: "https://thenewstack.io/ai-php2shell-disclosure-framework"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T22:17:07Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "PHP powers roughly 70% of the world’s websites , according to Wiz Research , so a flaw in its core engine affects much more than any single application. On Wednesday, researchers disclosed two critical vulnerabilities discovered with help from frontier AI models. OpenAI also proposed a new framework for handling the growing number of security flaws AI is helping uncover. \n\n The flaws, tracked as…"
tags: ["AI", "Open Source", "Security"]
orgs: ["OpenAI", "Google", "Microsoft", "Amazon", "Cursor", "US government"]
topics: ["products & launches", "models & research", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 1169
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AI found flaws in the code behind 70% of the web. The fix took two months.

The New Stack · Amanda Caswell · 2026-10-21

AI found flaws in the code behind 70% of the web. The fix took two months.
PHP powers roughly 70% of the world’s websites, according to Wiz Research, so a flaw in its core engine affects much more than any single application. On Wednesday, researchers disclosed two critical vulnerabilities discovered with help from frontier AI models. OpenAI also proposed a new framework for handling the growing number of security flaws AI is helping uncover.
The flaws, tracked as CVE-2026-109618 and CVE-2026-109619 and collectively called PHP2Shell, score 9.2 on the CVSS v4.0 severity scale. Researchers at Calif.io found one using OpenAI’s GPT-5.6 Sol, while Wiz independently found both using its Wiz Atlas tool alongside Google’s Gemini 4 Argon and GPT-5.6 Sol. Cloudflare also lists Quarkslab among the parties that disclosed the bugs.
A Decade of Dormant Defects
The problem starts with how PHP handles errors. When a request runs out of memory or crashes, PHP can leave behind references to memory that has already been freed. The next request handled by the same worker process may still treat those references as valid. Wiz found that attackers could exploit this behavior to access sensitive data or run malicious code.
These are memory-safety bugs, including use-after-free and type confusion, that developers have spent years trying to prevent by moving critical C code to languages like Rust. PHP’s engine is written in C, and Wiz showed that attackers could exploit the flaws to run code on WordPress, Drupal, and Joomla without logging in. Researchers also demonstrated attacks that exposed server memory without executing code.
At least one of the flaws affects every PHP release from the past decade, with some vulnerable code dating back to PHP 5.4. The bugs went unnoticed for so long because exploiting them required combining several weaknesses in ways that were difficult to uncover.
That’s where AI made the difference. Wiz says a single researcher using frontier models accomplished in about a week what might once have taken a team of experts months. The company calls the findings “an AI inflection point,” arguing that the vulnerabilities had always been there, but AI had made it easier to turn them into working exploits.
Raluca Ada Popa, head of Gemini Security at Google DeepMind, calls frontier AI “a game-changer for cyber defense” in a statement published by Wiz. Security teams are already putting similar tools to work. Cursor recently released the blueprints for a fleet of AI agents that search its codebase for vulnerabilities and block them in pull requests, reflecting a growing concern that attackers can use the same technology to find weaknesses first.
Two Months to a Patch
Wiz says it found the first flaw on August 19 and confirmed unauthenticated code execution against Drupal the following day. It demonstrated the same against WordPress on August 21 and reported the bugs to PHP’s security team on August 24. The team acknowledged the reports on September 21 and began building a coordinated fix, and the patched releases arrived on Wednesday, the same day the details became public.
Wiz credits partners including Cloudflare, Google Cloud, AWS, Microsoft, and Akamai with helping coordinate protections and guidance.
Part of the challenge was making sure the fix covered every version of the flaw. Wiz says its researchers found several variations of the same underlying problem in how PHP handles memory. Hosting providers, cloud platforms, security vendors, and Linux distributors also needed time to prepare before the details became public. Wiz credits partners including Cloudflare, Google Cloud, AWS, Microsoft, and Akamai with helping coordinate protections and guidance.
Nine Hours of Warning
The details leaked before the planned disclosure date. Cloudflare says it began protecting its customers by default at 3:02 a.m. UTC on Wednesday, roughly nine hours ahead of the public announcement, and it observed attack traffic aimed at those customers while it watched attackers modify their payloads to slip past the rules. Request data alone does not always show whether an exploit succeeded, the company says, so its new protections also examine the server’s response.
“Customers should patch their PHP repos.”
Cloudflare was direct about what a firewall can and cannot do. “Customers should patch their PHP repos,” the company writes, describing its rules as an added layer of defense during the update window rather than a substitute for the fix. Those rules can block exploit attempts, but they do not remove the underlying flaws from the software running on a server.
Rethinking the Rulebook
OpenAI led a coalition effort on PHP over the past two months as part of its Patch the Planet initiative. The company says PHP’s maintainers led the fixes and release, while OpenAI and its partners contributed research, technical support, and coordination, and it then used the moment to propose a framework for responding to the critical vulnerabilities that frontier AI uncovers, asking the security community to help refine it.
Running in five stages, maintainers, researchers, and essential technical partners first confirm and fix the flaw, then test the patch with frontier models to look for bypasses. Affected organizations next receive advance information based on their ability to act, so distributors can backport fixes, hosting providers can test mitigations, and security vendors can write detection rules, with government agencies coming after that to help guidance reach operators of critical infrastructure.
Once the fix and disclosure plans are stable, distributors and service providers prepare updates across their products while public guidance helps operators confirm the updates are running. OpenAI says its work on PHP involved CISA, the Office of the National Cyber Director, the White House’s Super Intelligence Force, and international partners.
“the same capabilities can also help attackers rapidly develop offensive tools and exploits.”
OpenAI also addressed the other side of its own technology, writing that “the same capabilities can also help attackers rapidly develop offensive tools and exploits,” and it calls the PHP bugs “one of the most impactful security issues in recent memory.”
The company has committed $1 billion in subsidized access through Daybreak for Frontline Defenders, aimed at organizations with limited security resources that protect essential services, and it is backing maintainers through Codex for OSS subscriptions and direct sponsorship of projects.
Funding and access to AI models can help, but they won’t solve the growing workload facing open source maintainers. The same tools that uncover vulnerabilities are also generating AI-written code that maintainers have to review, adding to an already demanding job. OpenAI acknowledges that each project has its own priorities, meaning the support may not reach everyone who needs it.
Patch First, Protect Always
The PHP security advisory lists four patched versions released on October 21: PHP 8.5.12, 8.4.27, 8.3.36 and, 8.2.35. Teams using a Linux distribution or managed hosting provider should check with their vendor, since fixes can be backported without changing the PHP version number.
OpenAI has also released a PHP version checker with two Codex skills for checking local servers and websites. The tool can flag vulnerable versions but cannot confirm whether a patch has been applied, particularly when vendors backport fixes.
