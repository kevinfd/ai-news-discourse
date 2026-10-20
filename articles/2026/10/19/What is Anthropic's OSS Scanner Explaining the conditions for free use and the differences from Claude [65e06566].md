---
id: "65e06566b7bcbb1a"
title: "What is Anthropic's OSS Scanner? Explaining the conditions for free use and the differences from Claude Security!"
url: "https://note.com/kazu_t/n/n0cd32531becf?hl=en"
link: "https://note.com/kazu_t/n/n0cd32531becf?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-19T21:00:00Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Kazu×教育", "谷 一徳", "AI Academy創業", "AI顧問"]
language: "en"
summary: "Hello, kazu here.When you hear that \"AI can find vulnerabilities for free,\" you naturally want to try it on the apps you've built.ConclusionOSS Scanner is a free, recurring vulnerability scanning ..."
tags: []
orgs: ["Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 1494
paywalled: false
image: "http://www.bing.com/th?id=ONUT.4mqDDoxwExEYwdsfywNklA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# What is Anthropic's OSS Scanner? Explaining the conditions for free use and the differences from Claude Security!

note · Kazu×教育, 谷 一徳, AI Academy創業, AI顧問 · 2026-10-19

What is Anthropic's OSS Scanner? Explaining the conditions for free use and the differences from Claude Security!
Hello, kazu here.
When you hear that "AI can find vulnerabilities for free," you naturally want to try it on the apps you've built.
Conclusion
OSS Scanner is a free, recurring vulnerability scanning service from Anthropic that core maintainers of critical OSS can apply to use. There is a screening process for participation, and the reports received are pre-human verification. If you want to check your own code, you should choose from Claude Security apps or plugins instead.
What this article will solve
Before you try it out, let's organize the following three points.
1. Is my OSS project eligible? 2. How is it different from Claude Security apps/plugins? 3. How should I handle the vulnerability reports and suggested fixes I receive?
What is OSS Scanner? Whose scans are free?
On October 8, 2026, Anthropic announced OSS Scanner. OSS is software where the source code is made public and can be used, modified, and redistributed according to license terms.
With this service, participating projects are periodically scanned by Anthropic's powerful models. Anthropic covers the scanning costs.
The background to this is that the number of potential issues identified by AI has increased, making it difficult for human verification to keep up. Therefore, they have provided an option to deliver AI-generated reports quickly to maintainers who can verify the additional reports themselves.
What is free is the scanning of eligible OSS. It does not mean that a contract is attached that allows anyone to use Mythos freely.
Can I apply for my project?
The official FAQ explains that they make individual decisions, focusing on established projects that have a significant impact on infrastructure or user security.
Factors for consideration include the potential for external attacks, the breadth of users and dependent projects, and activity duration and update status. It is not a system decided solely by the number of stars. New projects or forks that do not differ significantly from the original project are generally not eligible.
The application should be made by the project's core maintainer. It is not intended for unrelated third parties to apply for repositories they are interested in.
What we should consider here is whether you have the capacity to verify and respond after receiving additional reports.
How should I distinguish between this and Claude Security?
There are things with similar names, but it is easier to organize them by "who uses it and where." I confirmed the terms of service on the official page on October 20, 2026.
1. For those who want to continuously check important OSS: OSS Scanner
Core maintainers of OSS that meet the eligibility criteria can apply. This is a service where Anthropic performs periodic scans and you receive reports via email.
2. For those who want to check corporate repositories as an organization: Claude Security app
This is a public beta for Claude Enterprise. Administrators enable it and connect GitHub repositories to perform scans. The official product page states that Claude Mythos 5.1 is used for the scans.
3. For those who want to check their own code from Claude Code: Claude Security plugin
This is a beta for Claude Code users. It uses the model available to that specific Claude Code account. It is not a mechanism where installing the plugin automatically allows you to scan with Mythos.
If you want to check a web app you built yourself, reading the explanation for the plugin first will likely make it easier to apply to your own work. The introduction steps and an example of checking a fictional invoice app are introduced in this article.
What to prepare when applying
Application is done via a pull request to the official GitHub repository. A pull request is a mechanism for proposing file additions or changes and having them reviewed by an administrator.
The main things to prepare are the following three items:
1. project.yaml, which records the scan target and contact information
You register the target repository and the contact information for receiving reports, etc.The email address written in this setting will be made public.It is recommended to decide on a security contact point that can be made public in advance.
2. Dockerfile, which prepares the scan environment
You define the preparations for installing dependencies and building the project. You can use the network during the preparation stage, but the subsequent AI-based scan is performed in an environment with internet access disabled.
3. Threat model description to be included optionally
This is documentation that conveys what you are protecting and which inputs or operations you do not trust. For example, you distinguish between parts that only administrators can operate and parts that anyone can access. By conveying service-specific assumptions, you can also share the criteria for judging reports.
When you prepare the files and submit the proposal, a human will verify the applicant, contact information, and scan scope.The fact that the application is reviewed by a human is separate from the fact that each report received has been reviewed by a human.This article does not perform the application or scan execution, but organizes the information for making a decision before applying.
Also, what is published on GitHub are the registration settings and auxiliary tools. It is not stated that you can run the Anthropic scanner itself on your Mac by obtaining the repository.
Once you receive a report, how do you handle the suggested fixes?
According to the official announcement, reports include a description of the issue and information for reproduction, and if available, suggested fixes are also included. However, each report is generated by a model and has not been reviewed by a human beforehand.
If it were me, I would first check the conditions under which the issue occurs and see if it can be reproduced in an isolated verification environment. Then, I would verify whether the proposed fix eliminates the cause and does not break normal operation or compatibility before deciding to adopt it.
Even if an AI has another AI double-check it, that alone does not mean it has been verified by a human. Let AI help with the discovery process, while humans retain the judgment for fixing and publishing.Thinking in terms of this division of labor makes it easier to incorporate into daily development.
Summary
The criteria for choosing OSS Scanner is whether you are maintaining the target OSS and can handle additional reports.
If you want to check your own app right now, think of the Claude Security plugin as the entry point, and if you want to manage it as a company, think of the Claude Security app as the entry point; consider them separately. Don't choose just because of the word 'free'; you should match it to your position and the scope you can verify.
Thank you for reading this far! I hope this helps you organize your options when using AI in development.
Sources
- Anthropic Official Announcement: Launch of OSS Scanner and Report Content
- OSS Scanner Official FAQ: Eligibility and Operational Explanation
- Official GitHub: Registration Steps and Configuration Files
- Claude Security Official Product Page: Terms of Service for Apps and Plugins
- Reference: Overview of OSS Scanner by npaka
Frequently Asked Questions (FAQ)
Q. Can I also apply for OSS Scanner for private company repositories?
A. OSS Scanner is a service for important open-source projects. For private business code, please check the terms of service for Claude Security and other products, as well as your internal usage policies.
Q. If it's free, does that mean I don't need a paid Claude plan?
A. Anthropic covering the inspection costs for OSS Scanner is separate from the usage contracts for the Claude app or Claude Code. You cannot assume that because the inspection is free, other products are also free to use.
Q. If a fix is included, is it okay to just apply it as is?
A. The suggested fix also requires verification. You should decide whether to apply it after confirming the reproduction of the issue, testing after the fix, and checking for any impact on existing functionality.
Introduction to Generative AI Lab
In the membership "Generative AI Lab", we introduce the verification and operation of generative AI and AI agents.
Click here if you want to learn about Generative AI and AI agents through videos.
In the Generative AI course I instruct, I explain everything from the basics of Generative AI to how to utilize it.
Generative AI Course (Basics)
Generative AI Course (Practical)
AI Talent Course (From the basics of machine learning and deep learning to AI agent development with Python)
Click here for project consultations.
I provide support for business efficiency improvements using AI, as well as the construction and operation of AI agents.
Click here for details on our AI advisory service.
For corporate consultations and business inquiries, please contact us via the inquiry form.
#GenerativeAI #Claude #ClaudeCode #OSS #Security #AIAgent
