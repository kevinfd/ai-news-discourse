---
id: "388809cd7e7439fe"
title: "Can Resident AIs Be Trusted More the Smarter They Are? ~Comparing Grok Bot, Claude Duet, and OpenAI's dots by 'When They Act' and 'Where They Stop'~"
url: "https://note.com/onigiri_t8y/n/n8769b53a1662?hl=en"
link: "https://note.com/onigiri_t8y/n/n8769b53a1662?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-02T00:32:00Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["おにぎりテック"]
language: "en"
summary: "Introduction] The Conditions for Trusting AI Beyond IntelligenceRecently, three products claiming to be \"resident\" AIs were officially announced in succession. They are xAI's (officially written as ..."
tags: []
orgs: ["Anthropic", "xAI", "OpenAI"]
topics: ["chips & infrastructure", "products & launches", "models & research"]
content_source: "fulltext"
word_count: 2401
paywalled: false
image: "http://www.bing.com/th?id=ONUT.zOQtHOjoyKCFOrO-15YNWQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Can Resident AIs Be Trusted More the Smarter They Are? ~Comparing Grok Bot, Claude Duet, and OpenAI's dots by 'When They Act' and 'Where They Stop'~

note · おにぎりテック · 2026-11-02

Can Resident AIs Be Trusted More the Smarter They Are? ~Comparing Grok Bot, Claude Duet, and OpenAI's dots by 'When They Act' and 'Where They Stop'~
[Introduction] The Conditions for Trusting AI Beyond Intelligence
Recently, three products claiming to be "resident" AIs were officially announced in succession. They are xAI's (officially written as SpaceXSI on their page) Grok Bot, Anthropic's Claude Duet, and OpenAI's dots.
This article is not a single specific piece, but rather a look at these three sets of official pages.
All three run on their own computers in the cloud, allowing work to proceed even when you close your local PC. This is something all the official pages agree on.
So, can resident AIs be trusted more the smarter they are?
Reading the official pages, users cannot choose the base model for any of the three products. Grok Bot has no model selection and chooses automatically per task, Claude Duet is fixed to Claude Opus 5.5, and dots is based on GPT-6 Astra.
Therefore, this article will not compare intelligence. Instead, it will compare three things: "when they start acting," "where they operate," and "where they stop to ask a human."
There will be no winners or losers declared for any of the products.
First, let's confirm the premises. All three products are in beta, research preview, or phased rollout, so their behavior may change.
This article is based on official information as of November 2, 2026.
[Basics] Five Scenarios Where Residency Is Suitable, and Where It Is Not
Resident types are suitable for work that can proceed even when a person is not in front of the screen.
A resident-type assistant is a system that does not just answer the moment it is asked, but continues to work on its own after being tasked and notifies you when necessary.
Useful scenarios can be divided into five categories based on the nature of the work. This classification is an organization for this article based on descriptions from the official pages.
Work with long wait times
- Reason residency is suitable: It proceeds without a person needing to be glued to it
- Example where it is not suitable: Questions that end in a few seconds
Repeated confirmation
- Why residency is suitable: Can check schedules and incoming messages regularly
- Example where it is not suitable: One-off tasks
Tasks spanning multiple apps
- Why residency is suitable: Can cross between email, calendars, and chat
- Example where it is not suitable: Tasks completed within a single app
Work triggered by events
- Why residency is suitable: Can launch when emails or alerts arrive
- Example where it is not suitable: Work where the trigger event is not defined
Work requiring human judgment
- Why residency is suitable: Can handle preparation and pause at the decision point
- Example where it is not suitable: Work where you want to offload the judgment itself
There are also reasons why it is not suitable for certain situations. Residency consumes usage quota every time it acts.
For example, the official Grok Bot page warns that running it every hour or processing all messages in a busy Slack channel can consume a week's worth of usage in a single day.
Also, operations requiring approval will face delays when no one is watching. Work that requires an immediate response or tasks where every decision is heavy are likely not suitable for residency.
[Difference] From human-initiated tools to proactively acting tools
What has changed is not the intelligence, but the trigger for starting the work.
Conventional chat-based AIs work with you after you open the app. The official Claude Duet page makes this contrast clear, explaining that the Claude app is something you 'work with when you open it,' while Duet is something that 'comes to you.'
To come to you, the work cannot take place on your local PC. All three products run on your own computer in the cloud and in a browser.
Consequently, the questions change too. In chat, it was enough to check if the answer was correct.
With resident-type AIs, you look at 'when they acted,' 'what they touched,' and 'where they stopped.'
Even if the intelligence level is the same, if the timing of action and the stopping point differ, the scope of what you can entrust to them changes. In the next chapter, we will compare these three axes.
[Mechanism] The Three Axes: Timing, Location, and Stopping Point
All three products are resident-type, but their signals for starting action and their methods for approval differ.
We will list the three axes. Everything is based on descriptions from the official pages; items that could not be verified are not written.
When do they act?
- Grok Bot: Routine. Triggered by schedules (specified in simple sentences) or events such as Slack, GitHub, Linear, Sentry, PagerDuty, email, or webhooks.
- Claude Duet: Morning briefings and account checks every few hours. They contact you.
- dots: Reservations and repetitions. Even without being asked, they perform read-only background investigations of connected information.
Where do they act?
- Grok Bot: Persistent cloud computer. Shared by all bots within the account.
- Claude Duet: Your own computer on the cloud and your browser. The browser version uses a dedicated virtual machine.
- dots: Your own cloud computer and browser.
Your PC
- Grok Bot: Does not use it by default. Command execution is possible if permitted (confirmed every time by default).
- Claude Duet: Not visible (official limitation).
- dots: Can be connected optionally (default is off, up to 1 device).
Stopping point
- Grok Bot: Auto Review confirms before execution. Custom Rules allow up to 20 items each for 'Always Confirm' and 'Auto-Approve'.
- Claude Duet: Shows content and waits for approval before sending, paying, signing, or deleting.
- dots: Auto-review and Custom Rules. Choose from 4 levels for each operation.
When they act
The signals that trigger action can be divided into three types: event-driven, time-driven, and proactive notification.
Grok Bot can be triggered by events such as incoming emails. You can obtain one dedicated email address, and incoming mail can trigger routines.
Routines are limited to a maximum of 50 per bot, and there is a constraint that the schedule interval must be at least 5 minutes.
Claude Duet notifies you only when necessary, through morning briefings and daytime monitoring. The official explanation for checking accounts every few hours is that monitoring every time would exhaust the usage quota too quickly.
Instead, it is explicitly stated as a limitation that urgent messages may arrive between checks.
I could not find any pages confirming how users can set up their own recurring tasks.
With dots, you can set up repetitions by asking things like 'Check my calendar every morning and let me know.' Situations where it acts without being asked are limited to tasks like background research.
The tools used for that research are read-only and cannot send messages or change app content.
Where they stop
The design for where they stop differs among the three products.
Grok Bot's approval cards have no expiration for tasks started from chat. For background tasks like routines, they expire in about 30 minutes.
Approvals that appear while the user is not looking can time out.
Claude Duet finishes the remaining tasks when it cannot get approval and brings the approval request back later. There are operations (payments and transfers, deleting orders, account creation) that cannot be set to 'Don't ask again'.
Also, securities trading, transfers between accounts, and access to other people's accounts will not be executed even if approved.
For dots' Custom Rules, you choose from four options for each operation: 'Execute without confirmation,' 'Execute if pre-approved,' 'Confirm before execution,' and 'Hand over to the user.' Rules do not override built-in safety requirements, and requesting a draft does not constitute permission to send.
[Specific Example] Assuming the same request on a Monday morning across three products
Even with the same request, if the timing of action and the stopping points differ, the form in which the person receives it changes.
This example is a hypothetical scenario combining information from official pages. It is not the result of actual testing on the three products, nor does it guarantee their behavior.
Suppose you ask, 'Every Monday morning, look at my schedule and emails, and draft replies for those that need them.'
For dots, the official Learn documentation recommends scheduling by specifying the time, time zone, and duration. You can check, pause, or change scheduled tasks under 'Scheduled.'
Whether an email is sent is determined by Custom Rules and built-in safety requirements. A request for a draft alone does not grant permission to send.
With Claude Duet, your morning brief includes the main points from your emails and calendar. At the stage of sending a reply, it shows you the recipient and the body text and waits for your approval.
Once approved, the email can be sent from the connected account.
With Grok Bot, you can run it via a schedule routine. According to official explanations, emails sent from a routine stop as drafts, and a human must press send.
This is an explanation regarding dedicated email addresses. It is unconfirmed whether the same applies to sending from connected accounts.
Approval cards generated by background tasks expire in about 30 minutes. If you do not see them in the morning, the approval may time out.
All three are designed to return to the human before operations that have external effects, such as sending emails. What differs is how they signal a stop and how they handle things after stopping.
[Related Concepts] Boundaries of authority, usage volume, and misinterpreted instructions
The ease of delegating to a resident AI depends more on the design of authority and usage volume than on the intelligence of the model.
Principle of least privilege and units of sharing
Grok Bot shares one cloud computer across all bots in an account. Since files, browser sessions, and command credentials are visible to all bots, the official documentation warns not to 'use bots as a boundary for authority.'
Connectors are also enabled for the entire account.
Furthermore, the official Grok Bot page states that model-based reviews are not a substitute for least privilege and explicit authorization.
Prompt Injection
Prompt injection is a problem where an AI mistakes instructions hidden in web pages or emails for commands from the user.
Claude Duet explains that it is designed to be unaffected by instructions embedded in pages through automated checks that run outside the model. Even so, it notes that defense is not perfect, so it requires authorization for critical operations.
Grok Bot treats emails received from others as 'information' and does not grant permission for instructions contained within those emails. dots incorporates defenses against malicious instructions while guiding users to review critical tasks.
None of the three products claim to have perfect defense. The 'where to stop' points are built on that premise.
Usage Limits and Frequency of Confirmation
Residency consumes usage limits every time it acts.
Claude Duet counts background tasks within the same quota as Claude. Grok Bot explicitly states that it consumes usage limits for each execution.
dots does not count conversations with a dot toward the limit, but tasks that a dot initiates in Work or Codex are counted as usual.
The reason for Claude Duet's confirmation every few hours can also be explained by this usage limit quota.
Points Not Confirmed on Official Pages
The following items could not be confirmed on the official pages. Not being able to confirm them does not mean they do not exist.
- Pricing: Unconfirmed for all three products
- Availability in Japan: Unconfirmed for all three products. Claude Duet can only be read as being for US Claude accounts, and dots as excluding the EEA, Switzerland, and the UK
- Claude Duet scheduled execution: The method for users to create settings is unconfirmed
- Grok Bot third-party verification: The existence of audits or penetration testing is unconfirmed
- Details of dots: The full text of the privacy FAQ and system card has not been read
Reference Information and Books (PR)
To understand this article more deeply, I have created a concept map slide. Viewing this should help with your understanding.
Abeam Consulting's 'AI Agent Design & Implementation Complete Guide: Thorough Explanation of Low-Code Development and Use Cases' is a book that features agent design and use cases in its title. It is not an explanation of three products, but rather background information for considering authority and approval.
Gabriel Anhaia's 'AI Agent Practical Guide: Design Patterns for Building Autonomous Systems with LLMs' is a book focused on design patterns for autonomous systems. It serves as material for considering authority and approval.
[Summary] Five questions for your work before delegating
Before comparing the intelligence of resident AIs, it becomes easier to choose one if you decide on the stopping points for your own work.
As a small step that readers can try themselves, please apply the following questions to your own work. What is written here is not a setup procedure, but questions for thinking.
- Waiting time: What work can proceed without a person being attached to it?
- Signal: Is it more natural for that work to start based on a time or an event?
- Bridging: Which apps does it bridge? What is the extent of the range you should allow it to touch in each?
- Stopping point: Among sending, paying, and deleting, which operations do you definitely want to include human approval for?
- Usage volume: When you increase the frequency of confirmation, does it stay within the usage volume limit?
Once you have written down these five points, you can check the official pages of each provider to see if the timing of action and stopping points match your answers.
All products are at a stage where they may change. Please check the latest information on each official page.
Reference Information
- Introducing Grok Bot (x.ai)
- Grok Bot FAQ (docs.x.ai)
- Grok Bot Approval, Security, and Privacy
- Grok Bot Skills, Routines, and Automation
- Grok Bot Computer and Apps (docs.x.ai)
- Grok Bot (Cursor Docs)
- Claude Duet (Anthropic)
- Claude Duet Safety, Privacy, and Security
- Get started with Claude Duet (Claude Help)
- Introducing dots (OpenAI)
- Getting started with your dot (OpenAI Help)
- dots (ChatGPT Learn)
