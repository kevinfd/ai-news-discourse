---
id: "6801da84888d1090"
title: "AI’s new business model: Break the internet, then sell the fix"
url: "https://fastcompany.com/91637523/ais-new-business-model-break-the-internet-then-sell-the-fix?partner=rss"
link: "https://fastcompany.com/91637523/ais-new-business-model-break-the-internet-then-sell-the-fix?partner=rss"
source: "Fast Company"
domain: "fastcompany.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-09T14:02:49Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Zeb Larson"]
language: "en"
summary: "People who work in cybersecurity or work on the fundamentals of digital infrastructure do not want to live in “exciting times,” but right now, they don’t have a choice. Binance was just hacked in what is, so far, the largest cryptocurrency heist in history. Anthropic, the company behind Claude, narrowly averted a major attack through a third-party extension that would have allowed hackers to…"
tags: ["Tech"]
orgs: ["Anthropic", "OpenAI", "Google"]
topics: ["models & research", "business & funding", "agents & coding"]
content_source: "fulltext"
word_count: 849
paywalled: false
image: "https://images.fastcompany.com/image/upload/w_1280,q_auto,f_auto,fl_lossy/f_webp,q_auto,c_fit/wp-cms-2/2026/11/p-91637523-AI-companies-will-break-the-internet-then-want-to-fix-it.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# AI’s new business model: Break the internet, then sell the fix

Fast Company · Zeb Larson · 2026-11-09

People who work in cybersecurity or work on the fundamentals of digital infrastructure do not want to live in “exciting times,” but right now, they don’t have a choice. 
Binance was just hacked in what is, so far, the largest cryptocurrency heist in history. Anthropic, the company behind Claude, narrowly averted a major attack through a third-party extension that would have allowed hackers to upload worms to the affected computers. A number of major airlines were affected when the Spanish travel-tech company Amadeus was hacked, leaking customer information on the web (mercifully without payment info, this time). At the center of this are generative AI companies like Anthropic and OpenAI, which all at once are empowering hackers while billing themselves as the only line of defense. They’ve found a new niche, and it’s to become a protection racket. 
The threat is quantifiable: Severe bugs are classified as CVEs (common vulnerabilities and exposures), and around 400,000 have been officially logged since 1988. Of those, 13,000 happened in the last month. PHP2Shell is the perfect example of this. If you spent any time on social media in the last few weeks, you probably heard some chatter about PHP2Shell and just how dire the threat was. Roughly 70% of websites rely on code written using PHP, and the announcement of a fundamental bug in the language—akin to discovering that millions of buildings share the same faulty lock, potentially giving intruders easy access—had people panicking. Websites such as Wikimedia preemptively went offline until a fix was pushed through.
These bugs were rediscovered separately by two cybersecurity firms: Calif and Wiz. The bugs are very difficult to spot. They had to do with how the host computer accesses memory while an application is running: If a malicious actor forced an out of memory condition by whatever means, it would be possible to interrupt the runtime, leave a partially initialized object behind, and have the application treat it as valid. It would be a stepping stone for a hostile takeover of the host server, while a separate bug could leave instructions from a request that could be read again subsequently instead of being reset. This can be an apocalyptic threat if somebody can actually do those things. They would gain remote control over the host computer, and at that point they can do whatever they want with that machine and what’s on it.
Notably, developers at the PHP Foundation knew about this bug in 2024, but couldn’t agree on a solution for it. Every proposed fix had associated costs, and in any event, nobody actually knew how to act against these bugs. The threat was completely theoretical. It sat there, which wasn’t the optimal workflow, but it also wasn’t an omega-level threat until generative AI came into the picture. Forcing the condition while also creating the takeover wasn’t easy to do. Once the vulnerability was publicly announced, what had been a trickle of attacks became a flood. Fixes were rapidly pushed (in some cases by volunteers) and anybody running a website on PHP was urged to quickly upgrade to protect themselves.
This was just one bug, but pretty much everybody expects that more will be found. The people talking loudest about the danger are, surprisingly, generative artificial intelligence companies. AI companies are all too happy to make clear how incredibly dangerous all of this is and how many more bugs and vulnerabilities they expect to find as they continue to look around. Sam Altman doesn’t think we’ll be able to patch all the bugs, while Jason Clinton of Anthropic terms it a “vulnerability tsunami.” They’re promising years of instability following this as they struggle to discover and patch all of these bugs—an ongoing process, because software development is itself a process of continual updates.
Why are they talking this way? They’re emphasizing how dangerous their product is, which seems like terrible salesmanship. But they’re also peddling the solution to the problem they helped to introduce.
And to force the issue, they’re going to look for the bugs themselves. That’s the point of OpenAI’s Patch the Planet initiative, which is all about looking for defects and vulnerabilities in open-source software. Nor are they just running around bug-hunting and letting chaos ensue. They’re trying to step into the cybersecurity space and set themselves up as the best solution to the problem. 
OpenAI unveiled a new security-focused model in September, GPT-6 Cyber. OpenAI’s Daybreak program is intended to be available only to eligible organizations so that only “good actors” can take advantage of this, though in the long term as models become open access it’s not clear how that distinction will matter. Anthropic has its own model, Claude Mythos Preview. Google has Gemini Carbon 4 as its cybersecurity model. As with all models, you pay per token. Access to Daybreak is subsidized, although if you’re a believer in Cory Doctorow’s theory of enshittification, the long-term business model will be to make this more expensive over time as customers grow to depend on it. These companies are desperate for new sources of revenue even as overall revenue growth slows.
