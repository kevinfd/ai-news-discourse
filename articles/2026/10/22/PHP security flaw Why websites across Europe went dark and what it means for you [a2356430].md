---
id: "a23564303e88c328"
title: "PHP security flaw: Why websites across Europe went dark and what it means for you"
url: "https://euronews.com/2026/10/22/php-security-flaw-why-websites-across-europe-went-dark-and-what-it-means-for-you"
link: "https://euronews.com/2026/10/22/php-security-flaw-why-websites-across-europe-went-dark-and-what-it-means-for-you"
source: "Euronews"
domain: "euronews.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-22T12:06:24Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Una Hajdari"]
language: "en"
summary: "AI models uncovered what OpenAI calls \"one of the most impactful\" security bugs in recent memory, hidden in PHP for more than a decade. From a Pokémon sleep tracker to the Dutch parliament, websites went dark worldwide to stay ahead of hackers."
tags: []
orgs: ["OpenAI", "EU", "Google"]
topics: ["policy & regulation", "products & launches", "agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1280
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# PHP security flaw: Why websites across Europe went dark and what it means for you

Euronews · Una Hajdari · 2026-10-22

AI models uncovered what OpenAI calls "one of the most impactful" security bugs in recent memory, hidden in PHP for more than a decade. From a Pokémon sleep tracker to the Dutch parliament, websites went dark worldwide to stay ahead of hackers.
Artificial intelligence has exposed two critical security flaws in PHP, a programming language that quietly powers most of the internet, sending organisations worldwide scrambling to shut down websites before hackers can exploit them.
The bugs sat undetected in PHP’s code for more than a decade. It took cutting-edge AI models from OpenAI and Google to turn a long-suspected weakness into a working attack — and now the race is on to close the door.
As AI’s fast-advancing capabilities fuel concern over a new era of cyberattacks, here is what you need to know.
Europe reacts
The Netherlands pulled its DigiD digital identity system, the Overheid.nl government portal and the website of the lower house of parliament, with the Port of Rotterdam, hospitals and the country’s five largest political parties following suit.
Even the Dutch National Cyber Security Centre took its own site down.
Finland’s state IT provider Valtori switched off government web services wholesale “as a precautionary measure,” France’s Interior Ministry put local administration sites into maintenance mode and Germany’s federal IT service ITZBund took down several portals.
CERT-EU, the cybersecurity service for the EU institutions, went further than most, telling any organisation unable to patch immediately to take its websites offline rather than risk being hacked.
The European Commission, ENISA, CERT-EU, Europol and the EU’s network of national cyber response teams also issued a joint statement urging organisations to act immediately, prioritising systems exposed to the internet.
What is PHP and why does it matter?
Created in the early 1990s, PHP is a name that originally stood for Personal Home Page and is the code that runs behind the scenes on roughly seven in 10 websites, according to security firm Wiz Research, which calls it “a backbone of the web”.
While languages such as HTML handle what you see on a page, PHP handles what you do not, such as checking logins, processing payments, serving up content.
It underpins WordPress, Drupal and Joomla, the platforms behind everything from personal blogs to online shops and government portals.
That reach is what turns two bugs into a global event. Wiz said every PHP version released in the past decade is affected by at least one of the flaws, and that even a bare-bones “Hello World” page on an unpatched server could be vulnerable.
A fix was released on Wednesday, with the PHP Foundation telling tech departments around the world that “if you run PHP, it is imperative that you update now.”
Patched versions are PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. Anything older no longer receives official updates and should be treated as exposed unless a vendor has backported the fix, the European Union’s cybersecurity emergency response team (CERT-EU) warned in an advisory.
The result has been a wave of apps and websites going dark, from the Paris police website to a Pokémon sleep tracker, as developers patch their underlying code. Government sites across Europe were among those pulled offline as a precaution.
How did AI find the flaws?
Both vulnerabilities, tracked as CVE-2026-109618 and CVE-2026-109619 and rated 9.2 out of 10 for severity, sit in the parts of PHP that nearly every request touches, namely memory management and error handling.
If a web request hits PHP’s memory limit at exactly the wrong moment, the software can be tricked into running an attacker’s code without any login.
The PHP Foundation admits its own developers first spotted signs of the problem in 2024, during an external audit.
A theoretical exploit was sketched out, but with no concrete route to an attack and a tiny core team weighing the trade-offs of a fix, work stalled and restarted for months. The foundation called the delay “a structural failure”.
Then AI got involved. In August, security firm Calif, working on an OpenAI-funded audit of PHP’s source code and using OpenAI’s GPT-5.6 Sol model, reported a fully working remote attack with the same root cause.
OpenAI independently flagged the same issue the same day. Wiz followed with further attack vectors two weeks later, using its own Wiz Atlas tool alongside Google’s Gemini 4 Argon and GPT-5.6 Sol.
“With frontier AI models and the right tools, a single researcher completed in a week what previously would have taken a world-class team months of work,” Wiz researchers wrote.
OpenAI called the discovery “one of the most impactful vulnerabilities in recent memory,” adding that it “marks a new phase, where AI can find security bugs with internet-scale impact”.
The findings were kept under wraps while a fix was developed.
Then, on Tuesday afternoon, the two CVE identifiers leaked onto online forums and social media.
PHP brought its release forward by a day, and Calif mistakenly published — then deleted — a video showing its proof of concept working against several targets, the PHP Foundation said. Copies spread quickly.
“The trouble with tools like AI is that the moment all the information’s out there, people can weaponise it very, very quickly,” Steve Kerrison, senior lecturer in cybersecurity at the Singapore campus of James Cook University, told AFP.
“That’s why everybody’s acting with such urgency to respond to this issue.”
Have sites already been hacked?
Not necessarily. “Taking websites offline does not necessarily mean they have been hacked. It can be a responsible measure to protect systems while security updates are applied,” said Dimitrios Salampasis of Australia’s Swinburne University of Technology.
The PHP Foundation said its security team inspected the proof-of-concept code circulating after the leak and found no functional exploit at the time of release.
“The evidence that security researchers are seeing is that nobody was actively performing attacks using the techniques available,” Kerrison said.
The picture is shifting, however. Web infrastructure firm Cloudflare said on Wednesday it had observed attack traffic aimed at its customers, and CERT-EU warned that the public circulation of technical details raises the likelihood that attackers are already probing the flaws.
Larger institutions, from government agencies to news outlets, should be able to patch relatively quickly. Others may be left exposed for far longer.
“There are sites, systems and people out there who will have no idea about this and still won’t for days, weeks and months,” Kerrison warned.
That could include user-run blogs and small business sites, which hackers could hijack to spread computer viruses, send spam or host malicious content.
Could there be other consequences?
Any data breach could come back to haunt customers long after the patch, if their personal information is harvested for phishing attacks — where someone is tricked into handing over a password or payment details.
The tangled, interlinked nature of online systems also means the risk does not end when you update your own server. Many sites rely on third-party services that may themselves run PHP.
If those third parties are slow to patch, “then even though you patched yourself ... you’re still unsecure,” said Rahat Masood, senior lecturer in cybersecurity at the University of New South Wales in Sydney.
PHP is not the whole story, Kerrison added. Strong cybersecurity means several layers of defence, so that one broken lock does not open every door.
The PHP Foundation, for its part, is using the episode to make a pointed plea. The language runs government services, banks and online stores worldwide, yet its security still rests on a small group of foundation-funded developers and volunteers.
Tools can now find bugs faster than ever, it said, but deciding how to fix them without breaking the web takes experienced engineers.
