---
id: "fb1ef7d0ad58870a"
title: "Claude sent a false homicide tip to police – and it’s part of a troubling AI pattern"
url: "https://zdnet.com/innovation/claude-false-homicide-tip"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-12T17:45:44Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Radhika Rajkumar"]
language: "en"
summary: "Models routinely take shortcuts to pass evaluations. Who gets to decide what incidents are innocuous?"
tags: ["Artificial Intelligence"]
orgs: ["Anthropic", "OpenAI", "Hugging Face"]
topics: ["models & research", "agents & coding", "policy & regulation", "safety & ethics"]
content_source: "fulltext"
word_count: 1135
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/reddarksmallGettyImages-2293940548.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Claude sent a false homicide tip to police – and it’s part of a troubling AI pattern

ZDNet · Radhika Rajkumar · 2026-10-12

ZDNET’s key takeaways
- In testing, Claude submitted false forms and exploited software flaws.
- Models routinely take shortcuts to pass evaluations.
- Anthropic downplayed concerns, but these actions form a pattern.
Anthropic has released new reporting on Claude’s behavior in testing and other internal evaluations — and the findings indicate a concerning pattern.
Also: Rogue AI incidents hit ‘tens of thousands’
On Friday, the company detailed several “unintended” actions its models had taken recently while completing certain benchmarks. Framing Claude’s actions as less serious than the breaches both Anthropic and OpenAI agents were involved in earlier this summer, the report details how Claude Haiku 4.5 was generating example tasks on “randomly selected webpages.”
More from ZDNET
It came across a page about an unsolved homicide case and filled out a tip form with the Philadelphia police, saying, “I may have information regarding this case. I recall seeing someone matching the description in the area around [the street named on the page] during that time period. Please contact me if this information is relevant.”
How does this happen, and why does it matter?
“Claude was instructed never to log in, create accounts, enter personal data, make purchases, or submit anything destructive, but the instructions did not rule out form submissions,” Anthropic explained, exemplifying how airtight security instructions have to be to actually prevent unwanted model behavior.
Based on other agentic security incidents from the last year alone, it’s also not clear that simply adding form submissions to this instruction would guarantee prevention if the model were given real stakes to complete a task.
Also: Who owns AI risk at work? Business and tech leaders can’t agree
Beyond that, in the real world, finding every possible risky interface or scenario and blocking it preemptively seems like a dangerous game of catch-up. The core issue remains that an AI system like Claude doesn’t appear to understand why it shouldn’t submit false tips about a homicide investigation — which is the central problem of lacking context for certain situations that even the most advanced models still exhibit.
That’s the concept of AI’s “jagged frontier” — why AI can demonstrate impressive capabilities in one area, like coding, and disappoint in others, like restaurant recommendations. (I think having embodied experiences is a crucial part of the latter.)
In another instance, Anthropic said it tasked an unreleased model with filling out a practice version of a government form.
“When the copy failed to load or the model closed it by mistake, the model instead navigated to the website where the real form is normally hosted and submitted the form there,” Anthropic said. While admitting the model shouldn’t have done this, Anthropic noted this generally happened when “an evaluation’s instructions were ambiguous,” or because “misconfiguration within the environment” didn’t let Claude access dummy forms.
Also: Regulators are trying to protect you from being fired by AI
Anthropic’s report wasn’t specific about which real forms its model filled out, but Axios reported that the company alerted the US State Department on Thursday that a model had filed “19 non-immigrant visa applications in August and one application in May through the publicly available form on the department’s website,” according to a department official.
Similarly to the homicide tip, the applications were not processed, nor did the model hack or otherwise compromise State Department systems.
Other actions
When Claude Mythos 5 was blocked by a server or encountered a paywall when seeking data, the agent found workarounds, like access tokens in old versions of a government agency website. The data Claude was trying to access was publicly available, which is at least preferable to the agent hacking proprietary or otherwise private information.
Also: The AI models that cheat the most
Anthropic said it sometimes limits the length of URLs Claude can ask for, to prevent the agent from “using long URLs to take certain unwanted actions, such as SQL or command injections.” The report said that Claude Opus 5 and Mythos 5 found a loophole you might find familiar: using free link shorteners.
While these incidents are more innocuous than the previous breaches, and could even be classified as shortcuts a person might take, that isn’t the point. Given how rapidly AI agents can hack systems, discover vulnerabilities in code, and deploy actions through agent networks, the worry here is about how a model makes decisions and why, and what the consequences of those decisions are, especially when researchers aren’t watching.
The overarching theme of this behavior is consistent with AI’s persistent-to-a-fault problem. Because of how AI systems are trained, they will often circumvent restrictions, bypass security checks, cheat, or otherwise take unapproved actions simply to succeed at or complete a task. This can happen even when researchers have explicitly instructed models to stop at certain impasses or not take certain actions; models also sometimes verbalize in their chain-of-thought responses that they shouldn’t take an action, and then proceed to take it anyway.
Also: AI a ‘force multiplier’ for low-skilled threat actors
“Although the impact of these behaviors was minimal and we had already turned off live internet access for some high-risk and cybersecurity evaluations, we have now decided to expand that to include all our internal evaluations until we have confirmed that our security and monitoring measures … reliably catch behaviors like these,” Anthropic wrote. The move echoes changes OpenAI made to its own security and monitoring after the Hugging Face incident.
“We are also continuing to fix or remove training environments that reward Claude for working around tool restrictions or other blockers, so that they do not incentivize these behaviors or permit reward hacking,” Anthropic added.
The state of AI security
The takeaway from Anthropic’s framing of this behavior is that comparatively more serious security incidents have set the bar for alarm much higher, especially in recent months. But that relativity depends on what the public is already used to: more damaging breaches that call labs’ breakneck speed to train models into question. It works in favor of AI companies that argue regulation would hamper US AI dominance over China: a false homicide tip isn’t as bad as stolen customer data or hacked government systems, right?
Also: The best and worst AI for your privacy, ranked
AI companies still prefer to regulate themselves, a decision the federal government has gone along with. All safety testing agreements the Trump administration has spearheaded with major US labs remain voluntary, although the White House did exclusively tell Axios that it will now require labs to report security incidents. That timing is peculiar, given how many high-profile incidents have already occurred in 2026.
Still, that means the only requirements for labs remain at the middle or end of the security lifecycle. The consequences are that companies remain the primary authority on what’s happening with their own models.
