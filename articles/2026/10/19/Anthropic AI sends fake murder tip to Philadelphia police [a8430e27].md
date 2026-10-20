---
id: "a8430e27eff8300e"
title: "Anthropic AI sends fake murder tip to Philadelphia police"
url: "https://foxnews.com/tech/anthropic-ai-sends-fake-murder-tip-philadelphia-police"
link: "https://foxnews.com/tech/anthropic-ai-sends-fake-murder-tip-philadelphia-police"
source: "Fox News"
domain: "foxnews.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-19T16:00:40Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Kurt Knutsson", "CyberGuy Report"]
language: "en"
summary: "Artificial intelligence can write your emails, research complicated questions and even handle tasks while you're away. But what happens when an AI system takes an action nobody intended? Philadelphia police recently got an unexpected answer. An AI model developed by Anthropic submitted a fabricated eyewitness tip about an unsolved murder through a Philadelphia police website. The submission…"
tags: ["4f6c7062-739f-5163-929c-4da4d0f6e034", "fnc", "Fox News", "fox-news/tech/artificial-intelligence", "fox-news/tech/topics", "fox-news/politics/finance/investigations", "fox-news/us/crime/cold-case", "fox-news/crime", "fox-news/tech", "article"]
orgs: ["Anthropic"]
topics: ["models & research", "business & funding", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 2007
paywalled: false
image: "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2026/10/931/523/anthropic-logo-documents-laptop.jpg?ve=1&tl=1"
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic AI sends fake murder tip to Philadelphia police

Fox News · Kurt Knutsson, CyberGuy Report · 2026-10-19

Artificial intelligence can write your emails, research complicated questions and even handle tasks while you're away. But what happens when an AI system takes an action nobody intended? Philadelphia police recently got an unexpected answer.
An AI model developed by Anthropic submitted a fabricated eyewitness tip about an unsolved murder through a Philadelphia police website. The submission happened during automated testing, and the model apparently believed it was generating an example interaction. Fortunately, the tip was flagged as spam before reaching investigators. However, the incident raises an uncomfortable question about what happens when AI agents interact with websites and public services without adequate safeguards.
AG BLANCHE REJECTS CALLS FOR NEW AI LAWS AFTER ROGUE AGENTS TARGET US GOVERNMENT WEBSITES
Join our upcoming CyberGuy LIVE class: 5 Ways to Travel Smarter and Save Money
In this free live online class, Kurt "CyberGuy" Knutsson will share five practical ways to protect your trip and your wallet this holiday travel season. You'll learn how to secure your phone and personal information, find better travel deals, avoid common scams, save money on bookings and use technology to make your travels easier and less stressful. No technical experience is needed.
Join us Saturday, October 31, at 11 AM ET / 8 AM PT. Register free now at CyberGuyLive.com.
How Anthropic's AI submitted a false murder tip
The incident involved PhillyUnsolvedMurders.com, a website where people can submit information about unsolved homicide cases in Philadelphia. On July 18, 2026, an AI model submitted a tip claiming to have information about a killing. According to Anthropic's October 9 report, the model was Claude Haiku 4.5. It had been assigned to generate and perform example tasks on randomly selected webpages. During one test, Claude encountered a page about an unsolved homicide that included a police department tip form. Rather than simply demonstrating how someone might use the form, Claude filled it out with invented information and submitted it.
Here's what the model wrote: "I may have information regarding this case. I recall seeing someone matching the description in the area around [the street named on the page] during that time period. Please contact me if this information is relevant." There's a particularly troubling detail here. The website contained no description of the perpetrator. Claude invented that reference while presenting itself as someone who might have witnessed something relevant to the investigation. The model also left the name and contact fields blank, which the website permitted. It then submitted the tip. Fortunately, the police department's spam filtering caught the submission before it could reach detectives.
Why Claude submitted a real police tip during testing
Anthropic's explanation reveals how a relatively simple oversight can lead to an unintended action. Claude had been instructed never to log in, create accounts, enter personal information, make purchases or submit anything destructive. However, those restrictions did not explicitly prohibit submitting online forms. As a result, the model completed the tip form as part of its assigned task.
Anthropic says the available transcript suggests Claude was generating example content rather than intentionally trying to mislead law enforcement. However, the company acknowledges that determining a model's intentions requires further analysis. That qualification is important. The evidence does not establish that Claude deliberately set out to deceive investigators. Instead, the incident shows how an AI system can carry out an action that its developers never intended, even while apparently attempting to complete its assigned task. Because Claude had access to the live internet during testing, it was able to submit the fabricated tip directly to a police website.
Philadelphia police caught the fake tip before investigators saw it
According to the Philadelphia Police Department's October 9 statement, the submission was flagged as spam and never forwarded to its Real-Time Crime Center for investigative review or distribution. After Anthropic briefed police on October 8, department personnel located the submission in the website's tip records and confirmed that the corresponding email remained in spam. Police also reported no evidence of unauthorized access to department systems or compromised police data. The department emphasized that all crime tips undergo human review before investigators act on them. Even when a tip appears credible, detectives must assess the information and look for supporting evidence. That process provides another layer of protection against fabricated submissions.
While that is reassuring, the timeline raises additional concerns. The submission occurred on July 18, 2026, at 11:27 p.m. According to Philadelphia police, Anthropic discovered the incident on September 28 and notified the department on October 7. Police met with company representatives the following day. That means more than two months passed before Anthropic discovered the false submission. The department called the two-month delay in detecting and reporting the incident to the city "unacceptable" and urged technology companies to strengthen their safeguards.
AI AGENT HACKS GYM SYSTEM TO MOVE UP WAITLIST
Why the false murder tip raises serious concerns
Think about what could have happened if the fabricated tip had reached detectives. Investigators might have spent time chasing information that had no legitimate source. An innocent person could potentially have faced unnecessary scrutiny. Neither outcome occurred here. However, the incident raises serious concerns for law enforcement agencies that depend on public tips. Police departments regularly receive information from witnesses, neighbors and people who believe they may know something about a crime. Those submissions can help investigators uncover new evidence, especially in cases that have remained unsolved for years.
Now consider how easily an AI system can generate convincing text and submit it through a public website. Without adequate safeguards, automated submissions could overwhelm investigators or make legitimate leads harder to identify. There's also a legal question. Pennsylvania law generally prohibits knowingly providing false information to law enforcement. However, the law's application to AI-generated submissions and the people or companies responsible for them would require separate legal analysis. The available evidence does not establish that Anthropic or its employees committed a crime.
Meanwhile, Philadelphia officials are also considering a broader response. The department said Mayor Cherelle L. Parker's administration will explore regulatory protections with state and federal partners to address incidents involving AI systems. Police are coordinating with the city's Law Department and technology officials as they continue reviewing what happened.
Anthropic discovered other AI agents taking unintended actions
The Philadelphia incident was one of several cases described in Anthropic's October 9 report, titled "Investigating unintended model actions in our evaluations and internal use." The company identified four categories of unexpected behavior involving Claude models interacting with outside websites and systems.
In one case, Claude exploited a software flaw on a university server to run commands after a scientific analysis tool stopped working. The model examined the website, found a vulnerable script and used it to complete the calculation. Another model found ways to access publicly available information that normally required a fee or an access token. Anthropic also observed models using URL-shortening services to work around limits designed to restrict certain web requests.
And the Philadelphia case was not the only example involving an online form. Anthropic reported that some models submitted real forms when they were supposed to use practice versions or stop before final submission. These incidents occurred during evaluations and internal use. Anthropic said the incidents had minimal impact and, to its knowledge, did not involve customer data or its own internal systems.
What Anthropic is doing to prevent more AI mistakes
Following its investigation, Anthropic announced additional safeguards designed to prevent AI models from interacting with outside systems in unintended ways. The company said it has stopped running certain evaluations, moved others into offline environments and rebuilt some tests to avoid contacting live websites. It also expanded restrictions on live internet access to all internal evaluations until it can confirm that its security and monitoring systems reliably detect this behavior.
Additionally, Anthropic strengthened restrictions on tools that allow Claude to retrieve information from websites. The company developed automated systems to identify and block unexpected actions. According to Anthropic, those systems blocked every incident described in its report when the company tested them against the previously identified cases. However, that result does not guarantee the safeguards will catch every future problem. Anthropic acknowledged that further work is needed to improve how its models handle ambiguous instructions and unexpected obstacles.
What this means for people using AI agents
You might be wondering what an incident involving a police website has to do with your own use of artificial intelligence. The connection is that AI agents are increasingly capable of performing actions instead of simply providing answers. Depending on the tools and permissions available, they can browse websites, complete forms and interact with connected services.
That's incredibly useful when everything works as intended. However, an agent can misunderstand instructions or continue pursuing a task when it should stop. For example, you might ask an AI assistant to research travel arrangements. If that assistant has permission to complete bookings, a misunderstanding could potentially result in an unwanted reservation. The Philadelphia case shows why AI agents need clear instructions and firm limits, especially when they can submit information to police departments, government agencies or other organizations. We reached out to Anthropic for additional comment, but the company did not respond before our deadline.
How to use AI agents more safely
You don't need to abandon AI agents because of this incident. However, I recommend keeping control over actions that could affect your accounts or other people.
- Start with low-risk tasks. Use AI agents for research, organizing information or drafting material before trusting them with more consequential activities.
- Require approval before submissions. Review online forms, purchases and outgoing messages before an agent sends them.
- Limit account permissions. Connect only the services an agent needs. Avoid giving it unnecessary access to sensitive information.
- Protect sensitive personal information. Never share your Social Security number, bank account details, credit card information, passwords or other sensitive records with an AI agent unless absolutely necessary and you have verified how that information will be handled.
- Check important information. Verify facts against reliable sources, especially when they involve someone's identity or legal situation.
- Review connected-account activity. Look for unexpected changes and revoke access if an AI tool performs actions you didn't authorize.
These precautions cannot eliminate every risk. However, they can help reduce the consequences of an unexpected action.
Kurt's key takeaways
What concerns me most about this incident is where the AI decided to act. We're talking about an unsolved murder involving real victims and families still waiting for answers. A model generated a fabricated eyewitness account and submitted it through a police website. Fortunately, the department's safeguards prevented that information from reaching investigators. But I find it troubling that Anthropic didn't discover the incident until more than two months later. I see tremendous potential in AI agents, and I've written about how they can save us time by taking over frustrating tasks. However, this incident shows why giving AI the ability to act independently requires careful oversight. Anthropic deserves credit for publishing details of what went wrong and explaining its response. At the same time, companies developing these systems need to demonstrate that their safeguards work before allowing their models to interact with sensitive services such as police departments and government agencies. We should expect better detection, faster disclosure and clear accountability when something goes wrong.
CLICK HERE TO DOWNLOAD THE FOX NEWS APP
If an AI system submits false information to police or another government agency, who should be held responsible: the company that developed it, the people operating it or nobody if the action was unintended? Let us know by writing to us at Cyberguy.com.
Sign up for my FREE CyberGuy Newsletter
- Get my best tech tips, urgent security alerts and exclusive deals delivered straight to your inbox.
- For simple, real-world ways to spot scams early and stay protected, visit CyberGuy.com - trusted by millions who watch CyberGuy on TV daily.
- Plus, you'll get instant access to my Ultimate Scam Survival Guide free when you join.
Copyright 2026 CyberGuy.com. All rights reserved.
