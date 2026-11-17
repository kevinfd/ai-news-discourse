---
id: "b1c71d07875ac772"
title: "Strengthening the fight against online child sexual abuse with new tools and support"
url: "https://openai.com/index/strengthening-online-child-safety"
link: "https://openai.com/index/strengthening-online-child-safety"
source: "OpenAI"
domain: "openai.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-16T17:00:00Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["rossant"]
language: "en"
summary: "New tools, practical guidance, and partnerships will help prevent, detect and respond to online child sexual exploitation and abuse."
tags: ["Safety"]
orgs: ["OpenAI"]
topics: ["safety & ethics", "policy & regulation", "agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1342
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50520804"
score: 118
comments: 285
community: "Hacker News"
---

# Strengthening the fight against online child sexual abuse with new tools and support

OpenAI · rossant · 2026-11-16

Strengthening the fight against online child sexual abuse with new tools and support
New tools, practical guidance, and partnerships will help prevent, detect and respond to online child sexual exploitation and abuse.
Today, we’re releasing a new tool to detect child sexual abuse material (CSAM), interventions that interrupt harmful behavior and point people toward help, practical resources for developers, and support for child-safety law enforcement investigators. These efforts build on our Child Safety Blueprint and our ongoing work to detect, block, and report abuse. For parents, the goal is simple: technology that helps keep children safe, with people in control.
It is well(opens in a new window) established(opens in a new window) that combatting online child predators requires coordination across many organizations. Individual companies like OpenAI have a responsibility to prevent our technology from being exploited by predators to harm children, and we also must work together with the broader industry, child safety organizations and law enforcement to advance our collective efforts to protect children online.
Helping more organizations detect abusive material
We’re building on our current protections with the release of a new image classifier that can detect potential CSAM, including AI-generated material. This new classifier looks for visual signs of abuse, helping teams identify novel images that may not have been seen before. It returns scores that help reviewers decide which images may need attention first. This is the first CSAM classifier with broad availability that has a specific signal on indicating if CSAM may be AI generated.
Our teams trained, evaluated, and designed the classifier for real-world deployment with assistance from the National Center for Missing and Exploited Children (NCMEC)(opens in a new window), a nonprofit that operates the CyberTipline, a centralized reporting hub for the online exploitation of children.
We’re offering access to the classifier to vetted organizations through the OpenAI API at no cost, making CSAM detection more accessible to child safety organizations and the broader industry, including those with teams of varying sizes.
Child safety is an industry-wide issue that requires strong collaboration across organizations and a variety of solutions. We’ve engaged the Tech Coalition(opens in a new window) and ROOST(opens in a new window) to help us share access to this new tool, and we are strong supporters of tools developed by others such as Thorn’s Safer(opens in a new window) CSAM detection system. In addition, we recently began participating in the Tech Coalition's Lantern program(opens in a new window), where we will share and receive signals relating to online child sexual exploitation and abuse to strengthen cross- platform collaboration.
We’ve tested the classifier internally and with early partners to measure how much abusive material it detects, how often it flags other images, and how it can support safety teams. Their feedback helped us identify weaknesses and improve the system.
Results
Early tests suggest the classifier can help reviewers focus on abusive images while reducing review of false positives. In an evaluation of user-uploaded images, we compared the new classifier with our current protections and found:
- The new classifier could reduce review work: we estimated that it would flag 48% fewer images while finding roughly the same number of abusive images as the existing tool.
- Images flagged by the new classifier were about twice as likely to contain abuse.
Early access partners have also evaluated how the classifier supports their own safety teams. In fal(opens in a new window)’s testing on human-reviewed production images, reviewers confirmed 72% of the classifier’s high-confidence flags as novel CSAM. invideo AI(opens in a new window)’s testing showed one in four flagged cases led to a ban. In SafetyKit(opens in a new window)’s evaluations involving drawings or animations that sexualize children, the classifier detected 90% of cases.
More information about the classifier is available in the CSAM classifier model card(opens in a new window). Organizations interested in the classifier will be able to request access through our intake form. We’ll continue improving the classifier with feedback from those that use it.
Interrupting harmful behavior and pointing people toward help
We already prohibit CSAM, train our models to refuse requests for it, and take action against accounts that violate our policies. We’re building on those safeguards with new product warnings in ChatGPT that interrupt attempts to find abusive material, explain the consequences, and point people toward help to stop harmful behavior.
The warning makes clear that sexualizing children causes harm, including when the requested material is AI-generated. Alongside the warning, we’ll remove the flagged conversation and pause access to ChatGPT for 24 hours, while keeping specialist support available to help people stop harmful behavior. Repeated violations may lead to longer restrictions and ultimately account closure or reports to authorities.
We developed this approach with input from organizations and academic advisors that research and develop programs to prevent child sexual abuse, including Protect Children(opens in a new window), the Lucy Faithfull Foundation(opens in a new window), Dr. Caoilte Ó Ciardha, Researcher & Honorary Reader in Forensic Psychology at the University of Kent and Joel Scanlan at the University of Tasmania, who independently evaluated a trial(opens in a new window) of deterrent messages.
Practical support for developers
The protection of children online doesn’t end with detection. We’ve published CSAM guidance(opens in a new window) to give developers practical steps to prevent abuse, detect harmful content, and act on it. Developed with input from the Tech Coalition(opens in a new window), Thorn(opens in a new window), NCMEC(opens in a new window), and the Internet Watch Foundation(opens in a new window), it is designed for organizations at different stages of building their safety systems.
The guidance provides clear rules, ways for users to report concerns, detection tools, and processes for reviewing and reporting suspected abuse. It also explains how safety identifiers can help developers connect misuse to individual users and how to support the people reviewing sensitive content. Developers can use it alongside tools such as our new image classifier, Moderation API(opens in a new window), ROOST’s self-hosted review console Coop(opens in a new window), and dedicated CSAM detection services such as Thorn’s Safer(opens in a new window).
Our commitment to collaboration and supporting the broader developer ecosystem also is reflected in our work with Anthropic and Google to jointly commission new guidance on responding to disclosures of child sexual exploitation and abuse in AI systems. Recently published by the Tech Coalition(opens in a new window), this guidance provides developers with practical recommendations for addressing these sensitive situations.
We’ve already seen this guidance lead to increased numbers of developers accessing child safety tooling and registering to report CSAM to NCMEC.
Supporting child-safety law enforcement units
Protecting children also means supporting the specialist child safety investigators working to find victims and stop abuse. As we’ve discussed publicly with Thorn(opens in a new window), AI can help investigators organize and prioritize information and reduce unnecessary exposure to abusive material.
We’re also supporting child-safety law enforcement units with new tools and trainings on how to use AI in their investigations, including dedicated plugins, investigative tools, and complex data analysis, with access managed by program administrators. At launch, the first tool will help investigators review lengthy chat logs and legal process returns, identify potential connections, and create timelines, with findings linked to source material.
The initial training is planned as an overview and demonstration, supported by a practical field guide that teams can refer to afterward. It will introduce the tools and how they fit into investigative work. Access will depend on agency authorization and program requirements. Future iterations of the training will be proposed at regional, national and international conferences.
Continuing the work together
These efforts share one goal: preventing harm to children and strengthening the response when abuse occurs. We’ll continue improving our safeguards while empowering child protection organizations, developers, researchers, and investigators with the tools, resources, and expertise they need to protect children, combat exploitation, and bring perpetrators to justice. By working together, we can harness the power of AI to make a meaningful difference in the fight against child sexual exploitation and abuse.
