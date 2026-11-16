---
id: "50e65454700b4273"
title: "Is Copilot Enough for Internal AI? Choosing Generative AI for Manufacturing and Preventing Information Leaks"
url: "https://note.com/mieruka_system/n/n8604fdf785a2?hl=en"
link: "https://note.com/mieruka_system/n/n8604fdf785a2?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-15T21:24:00Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["ミエルカボード"]
language: "en"
summary: "Hello, this is Techtrage.\"Copilot is the only AI allowed for use at the company.\"Companies using Microsoft 365 sometimes encounter such rules. While staff may express a desire to try other AIs for checking specifications,"
tags: []
orgs: ["Microsoft", "Anthropic", "OpenAI", "Google", "xAI", "DeepSeek"]
topics: ["agents & coding", "models & research", "search & media"]
content_source: "fulltext"
word_count: 1476
paywalled: false
image: "/th?id=ONUT.ERLA2rL9OMf_c5Vq9exNPA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Is Copilot Enough for Internal AI? Choosing Generative AI for Manufacturing and Preventing Information Leaks

note · ミエルカボード · 2026-11-15

SYSTEM NOTICE
Is Copilot Enough for Internal AI? Choosing Generative AI for Manufacturing and Preventing Information Leaks
Hello, this is Techtrage.
"Copilot is the only AI allowed for use at the company."
Companies using Microsoft 365 sometimes encounter such rules. While staff may express a desire to try other AIs for checking specifications, the company must understand where customer drawings and cost estimates are processed and who can view them.
Use Copilot for organizing emails and meetings, and get approval to compare other AIs for time-consuming tasks like checking specifications. By breaking it down by task, you can see what should be standardized and what is worth testing additionally.
Why companies standardize on Copilot | Ease of integration with existing operations and management
For companies already using Microsoft 365, it is easier to integrate employee accounts, file access permissions, and support channels into existing operations. There is also an advantage for staff in being able to use AI within their daily work, such as Outlook emails, Teams meetings, and Word documents.
This article covers the enterprise Copilot used with workplace organizational accounts. Current Microsoft documentation indicates that features vary depending on whether it is used via Copilot Chat, within Microsoft 365 apps, or in environments with additional licenses assigned. For example, basic Copilot Chat primarily involves the user specifying and attaching the necessary files. In environments with additional licenses, there are scenarios where users can reference internal files they have permission to view via Microsoft Graph. Microsoft Learn: Licensing and feature overview
When comparing, look at the entire process time: readability of answers, finding materials, confirming if input is allowed, correcting results, and registering them in the designated internal location. For example, with meeting notes, even just reducing the effort of moving information to a different service makes a difference in daily operations.
Copilot information leak prevention | Confirming sharing permissions and data processing destinations
Microsoft explains that for enterprise Copilot covered by enterprise data protection, input, responses, and data referenced via Microsoft Graph are not used to train the foundation models. Check your company's licenses and management features for audit and retention settings. Microsoft Learn: Enterprise data protection
Sharing permissions also need to be checked. For example, if a SharePoint folder containing cost estimates is shared with all employees, it may become easier for employees with viewing permissions to find those materials through Copilot. Administrators should identify where cost sheets and customer drawings are stored, decide with the material manager "who should be able to see them," and review the sharing scope. After changing the access scope, verify that search and reference results are as expected for both the target department and non-target users. Microsoft Learn: Guide to reviewing sharing permissions
Confirm whether data is used for foundation model training, where it is processed, and how long it is stored. For example, if web search is enabled, search terms generated from input are sent to Bing, which is handled differently than information within Microsoft 365. When adding agents or external connectors, also check the connection destination, reference permissions, and information being sent. Microsoft Learn: Web search and data protection
It is sometimes possible to use other models within Copilot
Copilot is a service that employees use for work. Models like Claude handle text generation and document reading within it. Microsoft provides information on mechanisms that allow the use of Anthropic's Claude models in some enterprise features. The scope of availability depends on contracts, features, regions, and administrator settings. Some models involving data retention require separate activation and confirmation of contract terms. Microsoft Learn: Claude usage terms and management settings
Before signing up for a separate service, verify how much of your intended work can be done in your current Copilot environment. Then, if you have specific requirements such as processing daily reports in bulk or passing answers to field systems in a fixed format, add enterprise services and APIs to your comparison.
Comparing generative AI models | Testing with three manufacturing tasks
We list publicly available models as candidates for trial by use case. Select candidates from services or APIs approved for internal use, and compare the current Copilot environment under the same conditions.
Classifying large volumes of daily reports
Candidates are GPT-6 Luna, Claude Haiku 5.5, and DeepSeek-V4.1-Flash. Using dummy data based on actual daily reports, compare classification errors, processing omissions, and processing costs per item.
Drafting meeting notes and reports
Candidates are GPT-6.1 Sol, Claude Sonnet 5.5, and Gemini 4 Hydrogen. Check whether the person in charge and deadlines are as in the original text, and how many minutes it takes to correct them for internal use.
Comparing complex specifications and cross-referencing new and old drawings
Candidates include GPT-6 Astra, Claude Fable 5.2, and Gemini 4 Carbon. We compare how accurately they can pick up revision numbers, tolerances, units, exception conditions following "provided that," and the source pages.
In addition to these, Kimi K3.1 Pro and Grok 4.7 are also candidates for verification if the usage conditions are met. When deciding on adoption, we compare not only the usage fees but also the costs including development and maintenance for integration, internal reviews, and the time spent by personnel verifying the output. OpenAI model list・Anthropic model documentation・Google Hydrogen announcement・Google Carbon announcement・DeepSeek official announcement・Moonshot AI announcement list・Grok official documentation
Measuring oversights and work time in specification cross-referencing
Even if the environment for handling information is well-prepared, AI may still misidentify drawing numbers or revision numbers, or miss decimal points in tolerances, quantities, or exception conditions. In manufacturing trials, we count such oversights in addition to the naturalness of the text.
For example, we prepare two fictional versions of specifications, new and old. A quality assurance representative first creates the correct answers for the changes, and then instructs the AI to output "before change, after change, reference page, and points requiring confirmation." We provide the same materials and instructions to all candidates and have them answer "not stated" for items not in the materials. If the formats are consistent, matching drawing numbers and quantities can also be verified using spreadsheet software or programs.
What we evaluate is the number of missed changes and the time it takes for the person in charge to return to the original document, cross-reference, correct, and make it usable items. For items that could affect the product if missed, such as tolerances and exception conditions, we record the content along with the count.
Making Copilot the standard and issuing additional approvals for necessary tasks
For example, daily document creation is handled using the approved Copilot. If a different use case arises on the shop floor, we consider it through the following flow.
- State the business challenge Communicate the task and the effect you want to measure, such as "it takes 2 hours every time to cross-reference specifications."
- Compare using public materials or fictional data The on-site staff creates evaluation criteria and measures quality, work time, and costs.
- Determine usage conditions The management staff confirms the target users, information that can be input, contracts, processing destinations, storage and deletion policies, integration partners, and cost limits.
- Use within a limited scope and decide on continuation Start with approved tasks and users, and review the effects and management burden. If the same results can be achieved in the existing environment, consider integrating operations.
If there is a point of contact where the field staff can consult about their troubles, they can try methods that fit their work within the company's rules.
Preparing correct materials before passing them to AI with Mieruka Board
Mieruka Server/Mieruka Board manages drawing revisions, approvals, and issuance, and allows you to check drawings, related documents, processes, and work records using part number charts. For example, an office staff member approves and issues a revised drawing, and a field worker checks the version to be used and the work instructions on the Mieruka Board before starting. Mieruka Board official product page
When using the same materials with external AI, the person responsible for material management confirms the scope of what can be shared and which version should be referenced. Even if materials are stored on a server within the factory, if they are sent to an external AI, they will be processed under the conditions of that service. By understanding where materials are stored and where the AI processes them you can think about AI selection and information management together.
First, please choose one task that is taking a lot of time. If you try it with the same materials and verification criteria, both the field staff and the management staff can judge whether the current Copilot is sufficient or if it is worth trying a different usage environment while looking at the same results.
*Product and model information refers to official documentation as of November 16, 2026. Specification cross-referencing and operations are assumed examples for explanation.
