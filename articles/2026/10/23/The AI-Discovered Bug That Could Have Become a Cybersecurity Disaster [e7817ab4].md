---
id: "e7817ab4143e9eff"
title: "The AI-Discovered Bug That Could Have Become a Cybersecurity Disaster"
url: "https://time.com/article/2026/10/23/ai-cybersecurity-php-hack"
link: "https://time.com/article/2026/10/23/ai-cybersecurity-php-hack"
source: "TIME"
domain: "time.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-23T21:11:07Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Harry Booth"]
language: "en"
summary: "Yui Mok—PA Images/Getty Images"
tags: ["Business"]
orgs: ["OpenAI", "Anthropic", "Meta"]
topics: ["agents & coding", "products & launches", "jobs & society"]
content_source: "fulltext"
word_count: 829
paywalled: false
image: "https://static.time.com/v3/assets/bltea6093859af6183b/bltab6ed0e7d44338b9/6adbc2e09742bec17e2fbdcb/GettyImages-2300859356.jpg?branch=production"
discussion_url: null
score: null
comments: null
community: null
---

# The AI-Discovered Bug That Could Have Become a Cybersecurity Disaster

TIME · Harry Booth · 2026-10-23

In early August, Sagi Tzadik asked an AI agent to take a security flaw it had found in WordPress and see whether the same weakness could be made to work against Drupal, another popular content management system. Eight hours later, the agent reported that it had failed. Then it added that, in the course of trying, it found a flaw in PHP, the programming language on which both systems—and as much as 70% of the web—depend.
Tzadik, a security researcher at cybersecurity firm Wiz, assumed that the AI had made a mistake. “Models tend to hallucinate,” he tells TIME. But the exploit, which took advantage of a weakness that had gone undetected for more than a decade, worked.
Unbeknownst to Wiz’s team, researchers at another cybersecurity firm, Calif—working with OpenAI—had used AI to find a related flaw. It suggests that once AI reaches a certain capability level, it is a matter of time before some longstanding weaknesses are unearthed. AI companies have been trying to ensure that defenders including Wiz and Calif get there first by giving them early access to new AI models before the equivalent capabilities trickle down to malicious users. This time, it worked.
The episode offers a glimpse into a new phase in cybersecurity in which AI helps defenders find vulnerabilities while giving them less time to fix them. While the bugs’ announcement has prompted alarm of a much-speculated “cyber-apolocalyse”—in which AI discovers world-melting bugs, plunging society into chaos—those who helped discover it are optimistic. “We are fixing vulnerabilities at an unprecedented rate, and this is doing security overall a very good thing,” Tzadik says.
But the details reveal just how close things came to disaster. Word of the vulnerabilities began circulating online two days before the patch’s scheduled release, prompting PHP’s maintainers to bring it forward by a day. Hours later, with the patch still unavailable, Calif mistakenly posted a video showing its exploit at work, and copycat attempts multiplied. Cloudflare counted thousands before the public announcement, tens of thousands within 45 minutes of it, hundreds of thousands within two hours, and eventually millions. Even after the patch was released, many webpages, including those of government agencies and parts of Wikipedia, were taken down as a precaution as security teams scrambled to install the update.
“If it had leaked a month earlier,” before a patch was ready, “this would have been a very different situation,” says Tomer Schwartz, CTO of exposure management and appsec at Wiz.
That a patch was prepared was the result of a loosely organized sprint. After Calif and Wiz sent reports to PHP, the groups joined forces. Researchers from competing companies shared their findings in common channels, with no contracts governing the arrangement. Over the following weeks, the group of roughly 15 people spoke almost daily to trace the vulnerabilities to their common source and devise a fix. The process, Schwartz says, was “just based on trust.”
That process will have to sustain increasing pressure. OpenAI has said that the PHP bugs were among “several significant vulnerabilities we’ve already found and are working to fix,” and predicted that similar discoveries would “increase sharply in the coming months.” As those findings multiply, so will the number of dangerous secrets waiting for fixes. “We have to rethink all of our processes, all of our methods, all of our tech stack … to be able to keep up the pace against attackers,” Schwartz says.
Though defenders are being given a head start, they face a disadvantage of another sort. Attackers only have to succeed once. “But, as defenders, we need to make sure that every single vulnerability is covered,” Schwartz says.
AI is helping defenders find those vulnerabilities first. Previously, testing suspected bugs could take weeks, forcing researchers to prioritize which were most promising. But now AI agents allow researchers to test many ideas at once, Tzadik says. “It’s months of traditional research condensed to, like, days—couple hours to days, really.”
But even with AI, the process is labor intensive. After the agent helped Wiz uncover the PHP vulnerability, it still couldn’t describe how the bug worked, Tzadik says. Its explanations were “just slop.” He and colleagues spent days untangling the cause of a bug and eventually reproducing it.
Cost is another constraint. Joshua Saxe, Meta’s former AI security tech lead, who left in February to co-found Abundance Security says he’s working with an organization that has spent roughly $1 million using Anthropic’s Mythos to identify bugs, adding that more bugs remain.
“As an industry, I think we’re deer in the headlights right now,” Saxe says.
"In the climate that we’re in today, you have to do cybersecurity well. It’s not an option to kind of half-a-- it,” says Adam Meyers, senior vice president of counter adversary operations at CrowdStrike. But even a successful exploit offers further opportunities for defenders to intervene. “Exploits are going to happen, and that’s not the end of the story,” he says. “It’s the beginning of the attack.”
