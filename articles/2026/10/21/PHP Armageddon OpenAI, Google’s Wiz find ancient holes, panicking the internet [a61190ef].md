---
id: "a61190ef2d9200f3"
title: "PHP Armageddon: OpenAI, Google’s Wiz find ancient holes, panicking the internet"
url: "https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet"
link: "https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T17:59:12Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Julie Bort"]
language: "en"
summary: "This is the kind of security issue that was found and prevented by AI, but is also a high risk because of AI."
tags: ["AI", "Security", "OpenAI", "php", "wiz"]
orgs: ["OpenAI", "Google", "Microsoft", "Amazon"]
topics: ["models & research", "products & launches", "safety & ethics", "agents & coding"]
content_source: "fulltext"
word_count: 517
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# PHP Armageddon: OpenAI, Google’s Wiz find ancient holes, panicking the internet

TechCrunch · Julie Bort · 2026-10-21

The U.S. National Security Agency’s sent out an alarming warning on Wednesday that two critical holes had been found in PHP, with patches already issued by the PHP Foundation.
PHP is a server-side programming language so widely used for web applications that it powers roughly 70% of the websites on the internet; by some accounts, that’s more than 33 million sites. It is also used by popular content management systems like WordPress.
The NSA warned that these holes are so severe that if a website can’t be patched immediately, it should be pulled off the web until it can be. The holes allow attackers to infiltrate the server’s file system or a database that may be used by the web app.
Interestingly, these holes have been tucked away in all versions of PHP since version 5, which was released in 2004. Websites not running relatively current versions of PHP will have some updating work to do, as PHP 8.1 and older versions are no longer supported. The recommendation is to update the web server to the current version of PHP, which is 8.5.12.
So how did two such ubiquitous, decades-old flaws that affect nearly every website on the internet suddenly come to light? AI, naturally, particularly via OpenAI and Google’s Wiz.
Security testing company Calif was engaged in OpenAI’s “Patch the Planet” initiative to find flaws in open source software. Using GPT‑5.6 Sol, it found one of the flaws, OpenAI disclosed in a blog post. Separately, the Wiz team also used AI, namely its Wiz Atlas security AI agent, Gemini 4 Argon, and GPT-5.6 Sol to find multiple vulnerabilities in PHP.
Both OpenAI and Wiz followed responsible security research practices and worked with PHP on patches before publicly disclosing the flaws. Then they all worked together to flesh out what they found, and test the patches, drawing in a host of others to help.
Wiz thanked Automattic, Akamai, AWS, Cloudflare, Fastly, Imperva, Microsoft, and Vercel. (While WordPress sites use PHP, WordPress has issued a statement saying that the flaw isn’t WordPress specific, and sites running its CMS must patch their servers and work with their web-hosting companies to ensure their sites are protected.)
OpenAI says that these flaws were found by researchers before hackers discovered them. So there were no reports of exploits in the wild. This is also in part because, before AI, these flaws were too hard for hackers to exploit. “With AI this is no longer a barrier. LLMs can help adapt an exploit to different PHP versions, configurations and memory layouts,” Wiz warned in its blog about the flaws.
In other words, this is the kind of security issue that was found and prevented because of AI, but is also a high risk only because of AI.
Now that the issue has been disclosed, hackers are fully in the know. The race is on for the internet to patch tens millions of websites before hackers can attack the unpatched ones. Hence the NSA’s guidance that if you can’t patch your PHP website right away, you’re better off pulling it offline until you can.
