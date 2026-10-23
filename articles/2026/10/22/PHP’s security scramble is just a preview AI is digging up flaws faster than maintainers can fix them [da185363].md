---
id: "da185363b323873d"
title: "PHP’s security scramble is just a preview: AI is digging up flaws faster than maintainers can fix them"
url: "https://thenewstack.io/php2shell-ai-vulnerabilities-maintainers"
link: "https://thenewstack.io/php2shell-ai-vulnerabilities-maintainers"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T14:35:13Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Paul Sawers"]
language: "en"
summary: "One of the biggest security scares to hit the web is causing widespread disruption, prompting businesses, hospitals, schools, and government agencies to temporarily shut down websites and online services as they scramble to protect themselves against two critical vulnerabilities in PHP , the programming language underpinning much of the internet. \n\n The vulnerabilities, collectively dubbed…"
tags: ["AI", "Open Source", "Security"]
orgs: ["OpenAI", "Anthropic", "Google"]
topics: ["models & research", "policy & regulation", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1593
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# PHP’s security scramble is just a preview: AI is digging up flaws faster than maintainers can fix them

The New Stack · Paul Sawers · 2026-10-22

PHP’s security scramble is just a preview: AI is digging up flaws faster than maintainers can fix them
One of the biggest security scares to hit the web is causing widespread disruption, prompting businesses, hospitals, schools, and government agencies to temporarily shut down websites and online services as they scramble to protect themselves against two critical vulnerabilities in PHP, the programming language underpinning much of the internet.
The vulnerabilities, collectively dubbed PHP2Shell, could allow unauthenticated attackers to execute malicious code on affected servers. Major technology companies have been racing to protect users, with Cloudflare deploying firewall protections and Automattic confirming that websites hosted across its platforms, including WordPress.com, WordPress VIP and Tumblr, have been secured. The Wikimedia Foundation, meanwhile, took several supporting services offline until they can be patched.
The PHP project released emergency fixes on Wednesday for versions 8.2 through 8.5. Older versions are no longer officially supported, although some distributions and vendors provide legacy fixes, and PHP has published limited patches for versions 7.4 through 8.1.
But while the PHP vulnerabilities are a major deal in their own right, the circumstances surrounding their discovery, remediation, and disclosure offer a revealing glimpse into the growing pressures facing the open-source community, as AI makes it easier to uncover serious security flaws.
“Find bad vulnerabilities in PHP”: Prompt discovery
News of the impending patches emerged on Tuesday, after details leaked ahead of their scheduled disclosure. The following day, OpenAI revealed that security firm Calif had discovered one of the flaws using its GPT-5.6 Sol model, while Google-owned Wiz had independently identified both vulnerabilities. OpenAI said it spent two months coordinating a response involving PHP maintainers, the security researchers, Cloudflare, and government cybersecurity agencies, as part of its Patch the Planet initiative.
The effort was disrupted when software supply-chain security company Chainguard released patched PHP container images more than six hours before the agreed time. CEO Dan Lorenc acknowledged on LinkedIn that he made the call, noting that Chainguard had independently rediscovered the flaw using a frontier AI model and the simple prompt “find bad vulnerabilities in PHP“.
Lorenc defended the decision by pointing to reports of attacks and the ease of reproducing the vulnerability. The PHP Foundation, for its part, argued that the early release could help attackers while other vendors were still preparing their patches.
“This disregarded weeks of work by many parties toward a coordinated disclosure,” the Foundation notes.
Nils Adermann, a PHP Foundation board member and creator and co-maintainer of Composer, says that “there were no confirmed exploits,” adding that any identified activity was merely people attempting exploits.
“The decision you took unilaterally without any communication with the PHP team was both irresponsible and unprofessional.”
“There was a clear embargo until the time of disclosure and public release, that was discussed and evaluated repeatedly as information arrived, weighing the risk of exploitation vs protection from publishing patches without complete updates,” Adermann writes in response to Lorenc’s post. “The decision you took unilaterally without any communication with the PHP team was both irresponsible and unprofessional. The proper thing to do here is apologize, not to justify your clear misbehavior.”
The new normal
The PHP pandemonium highlights a larger concern, however: AI is making it easier to find security flaws, faster than the people responsible for fixing them can respond. And as Lorenc himself put it: “This is unfortunately the new normal for the industry.”
Just a day before OpenAI’s disclosure, Anthropic published research showing that Claude had identified 493 security issues across 25 open-source projects encompassing more than five million lines of code. One configuration flaw had gone unnoticed for 21 years, and had the potential to disable an authentication requirement, allowing unauthorised clients to reach a supposedly restricted server.
While not all of Anthropic’s findings were exploitable vulnerabilities, they underline a growing problem: AI can uncover security weaknesses at scale, but assessing them and developing reliable fixes still takes time and expertise.
Christopher Robinson, CTO of Akrites and CTO / chief security architect at the Open Source Security Foundation (OpenSSF), says the PHP emergency is also a reminder of the importance of being ready to respond when serious vulnerabilities do emerge.
“The best way to minimize the impact of events like PHP2Shell is to prepare and plan for these things to happen.”
“The best way to minimize the impact of events like PHP2Shell is to prepare and plan for these things to happen,” Robinson tells The New Stack. “Having a vulnerability management process and understanding who can assist when issues become too complex are the best things that both open source projects and commercial entities can do.”
When finding bugs becomes easier than fixing them
For Michelle Tilley, software engineer and CTO of Atuin, an open-source developer tool with more than 32,000 GitHub stars, the kind of emergency response mounted for PHP would be difficult to replicate for smaller open-source projects.
“The response here looked like a vendor emergency, with a coalition, government agencies, and WAF (web application firewall) rules,” Tilley tells The New Stack. “This works for a project like PHP, but no one is going to assemble a coalition for an obscure 3-maintainer library that turns out to be used in software all around the world.”
“This works for a project like PHP, but no one is going to assemble a coalition for an obscure 3-maintainer library that turns out to be used in software all around the world.”
Atuin itself is already receiving more AI-generated bug reports and pull requests, Tilley says. While her company has enough engineering resources to handle them, many smaller projects depend on unpaid maintainers working in their spare time, who can become overwhelmed and walk away.
“These developers can, and do, burn out,” Tilley continues. “Sometimes they arrange for someone else to take over the project; often, they simply stop working on it, and downstream consumers never know. That’s how projects end up with vulnerabilities that will never be patched.”
Ultimately, she wants more responsibility to fall on researchers and businesses that rely on the code.
“There’s no single fix, but the direction is clear,” Tilley says. “The cost of remediation has to move toward the people finding the bugs and the companies depending on the code.”
That pressure extends to larger projects, too. Madelyn Olson, an AWS principal engineer and maintainer of the Valkey database, says that it too is finding and fixing far more security bugs this year than before.
“The hardest part has shifted from finding bugs to fixing them,” Olson tells The New Stack. “PHP is a good example.”
A PHP developer first identified the underlying problem behind one of this week’s vulnerabilities while fixing an issue uncovered during a 2024 security audit, which was organised by the Open Source Technology Improvement Fund (OSTIF). However, attempts to resolve it stalled because proposed fixes risked breaking compatibility, affecting performance or disrupting third-party extensions. Few engineers had the expertise to resolve those trade-offs, according to the PHP Foundation.
“AI is getting very good at finding bugs,” Olson says. “Making the right fix still takes experienced maintainers, and that’s where support from companies matters most.”
“AI is getting very good at finding bugs. Making the right fix still takes experienced maintainers, and that’s where support from companies matters most.”
To manage the influx, Valkey is narrowing its definition of a security vulnerability, using AI to inspect its own code, and making backports and releases easier to produce.
The Chainguard brouhaha also raises the question of whether disclosure timelines need to change. Olson recalls three researchers independently reporting the same Valkey bug in one week, each using LLMs. Valkey is now working toward shorter embargoes — although that is a different matter from breaking an agreed release date.
“If you found a bug with an LLM, it’s safe to say someone else can find it too,” Olson says. “That argues for shorter embargoes and faster releases, and Valkey is working toward shorter embargoes now, which is a trend we’re seeing across most large projects.”
A growing security backlog
Derek Zimmer, executive director of OSTIF, said the volume of both legitimate discoveries and poor-quality reports is creating backlogs, with maintainers spending scarce engineering time just establishing which issues are real.
“Maintainers are drowning in a sea of vulnerability reports from the public which is both slop reports and legitimate reports which are nearly impossible to separate without spending a lot of time to triage.”
“The reality in 2026 is that finding serious bugs is easier than ever, and maintainers are drowning in a sea of vulnerability reports from the public which is both slop reports and legitimate reports which are nearly impossible to separate without spending a lot of time to triage,” Zimmer tells The New Stack.
To help, OSTIF is trialling initiatives such as Project V-LAT, which embeds engineers in projects to review findings and develop fixes, while helping maintainers improve how reports are processed.
Robinson also emphasises the need for shared security expertise and dedicated engineers who can support upstream projects. He rejects the suggestion that exposing more flaws necessarily makes open source less secure, pointing to the opportunity for companies that depend on the code to contribute fixes. Yet, many projects have neither the money nor the expertise to respond independently.
“Most upstream maintainers are also acting as volunteers within the projects, with little to no budget, infrastructure, or supporting tools,” Robinson says. “There will be no ‘one size fits all’ approach here, we’ll need to approach this situation using multiple, parallel approaches to get the broadest chance for successful outcomes.”
