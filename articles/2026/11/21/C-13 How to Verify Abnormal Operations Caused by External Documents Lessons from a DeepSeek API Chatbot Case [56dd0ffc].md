---
id: "56dd0ffc87ff5a18"
title: "C-13 How to Verify Abnormal Operations Caused by External Documents: Lessons from a DeepSeek API Chatbot Case Study"
url: "https://note.com/masa_cloud/n/n3404a4c95a73?hl=en"
link: "https://note.com/masa_cloud/n/n3404a4c95a73?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-21T00:00:00Z"
published_date: "2026-11-21"
collected_at: "2026-11-21T13:03:30Z"
authors: ["伊藤正章｜サバイバルDxクリエイター：荒野のPip-Boy設計局"]
language: "en"
summary: "IntroductionHello. In this article, I will use an 'indirect prompt injection' verification problem—the kind that might appear on exams like the Registered Information Security Specialist—to outline ..."
tags: []
orgs: ["DeepSeek"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 883
paywalled: false
image: "http://www.bing.com/th?id=ONUT.DbBOuGiVLRZNnPoDb7GjeA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# C-13 How to Verify Abnormal Operations Caused by External Documents: Lessons from a DeepSeek API Chatbot Case Study

note · 伊藤正章｜サバイバルDxクリエイター：荒野のPip-Boy設計局 · 2026-11-21

C-13 How to Verify Abnormal Operations Caused by External Documents: Lessons from a DeepSeek API Chatbot Case Study
Introduction
Hello. In this article, I will use an 'indirect prompt injection' verification problem—the kind that might appear on exams like the Registered Information Security Specialist—to outline the process from initial response to recurrence prevention, based on the hypothesis that a Japanese company, Company M, built an internal chatbot using a DeepSeek model.
The overview of the problem is as follows: Company M operates an internal chatbot using the DeepSeek API. When an employee asked it to summarize a document obtained from an external source, the chatbot behaved in an unusual manner. An external transmission tool was called after the document summary, but it is unclear whether the transmission was successful. An isolated environment for verification is available.
Company M's Design Hypothesis
First, let's concretely set up a common real-world scenario.
- An email with a PDF attachment arrives in Outlook from a business partner.
- The employee saves the PDF, opens the internal chatbot in a browser, and attaches it manually.
- The chatbot uses a DeepSeek model via domestic hosting.
- The intended use is document summarization and sharing the results internally (posting to Teams or sending via email).
- Therefore, all transmission-related tools are defined in the summary agent's 'tools', and 'tool_choice' is set to 'auto'.
- The execution layer executes the model's 'tool_calls' without validation.
In other words, the summarization of the external PDF itself is within the expected scope. The problem is that the model can see transmission permissions unnecessary for the summarization task, and the execution layer lacks a gatekeeper to reject them. Indirect prompt injection is merely the trigger; the fact that the gun was already loaded is the fundamental weakness.
Question (1) Hypothesis and Evidence for Indirect Prompt Injection
The hypothesis is that the body of the externally sourced PDF contained instructions such as 'send to the specified destination after summarizing' embedded in a way that is difficult for the human eye to notice. We believe DeepSeek interpreted this not as data but as a command, and selected the transmission tool as an extension of the summarization task.
Evidence to secure includes the fact that the transmission tool was called beyond the scope of normal operation, the uncertainty of the transmission success, and the path through which the external document entered the context from outside the trust boundary. Additionally, we will preserve the raw PDF data, the full input prompt to the LLM, tool call logs, transmission destination logs, and the model's response text. White text, zero-width characters, HTML comments, and metadata in the PDF are also subject to inspection.
Question (2) Reproduce in Production or Investigate in an Isolated Environment?
The decision is to 'investigate in an isolated environment.' If reproduced in production, the external transmission tool might actually send data externally, and the verification act could lead to a new information leak. From the perspective of evidence preservation, operations in production also contaminate logs. In the isolated environment, we will replace the transmission tool with a mock and safely observe the conditions under which the tool call occurs using the same model, the same prompt, and the same document.
Question (3) Initial Response, Reproduction Testing, and Improvement of Execution Control
For the initial response, we will stop the relevant session, temporarily disable the transmission tool integration, preserve logs and the original document, conduct an emergency investigation of the transmission destination, and identify the scope of impact. If there is a possibility that personal or confidential information was transmitted, escalation to the legal and public relations departments is also necessary.
In reproduction tests, we try multiple patterns by changing the position and expression of embedded instructions to identify the conditions under which tool calls occur. The results are reflected in detection rules and test suites.
We consider improvements to execution control through a dual-defense approach. First, at the API request stage, we remove the sending tool from the `tools` list for the summarization task and also use `tool_choice: "none"`. Second, we place a policy engine in the execution layer to enforce a three-way decision of `allow / deny / ask` immediately before execution after receiving `tool_calls` from the model. `ask` is a fail-close mechanism that does not execute without approval, and in the case of `deny`, we do not remain silent but explicitly reject the request and log it. A complete record of the decision reason, destination, arguments, approver, and execution result is also essential.
Summary
M Company's weakness was that for the expected use case of summarizing external PDFs, they granted sending permissions unnecessary for the summarization task and failed to stop it at the execution layer. The pillars of the countermeasures are the explicit specification of tools per task and mandatory rejection/approval/recording via the three-way decision at the execution layer. This case well illustrates the basics of indirect prompt injection countermeasures: preventing it through structure rather than relying on the model's compliance.
▼ Learn, operate, and use DeepSeek safely in Japanese. 
On the practical learning site "deepseek.ac", we provide educational materials that allow you to verify the contents of reference books through operation and implementation.
▼ Reference Books and Problem Sets 
"Guide to Safe DeepSeek Operation" 
"Guide to Safe DeepSeek Operation: 70-Question Problem Set"
