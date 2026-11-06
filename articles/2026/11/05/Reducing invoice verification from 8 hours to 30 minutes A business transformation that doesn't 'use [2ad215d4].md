---
id: "2ad215d4706973f7"
title: "Reducing invoice verification from 8 hours to 30 minutes: A business transformation that doesn't 'use generative AI for everything'"
url: "https://note.com/ndot_man/n/nee1c9cdf43cf?hl=en"
link: "https://note.com/ndot_man/n/nee1c9cdf43cf?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-05T02:09:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["生成Aiで業務改革"]
language: "en"
summary: "When introducing generative AI, some companies may think about delegating as many tasks as possible to the AI. However, processing everything with generative AI is not necessarily the optimal approach ..."
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1959
paywalled: false
image: "http://www.bing.com/th?id=ONUT.caZyfxfpJu3zoTkTpNAPKw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Reducing invoice verification from 8 hours to 30 minutes: A business transformation that doesn't 'use generative AI for everything'

note · 生成Aiで業務改革 · 2026-11-05

Reducing invoice verification from 8 hours to 30 minutes: A business transformation that doesn't 'use generative AI for everything'
When introducing generative AI, some companies may think about delegating as many tasks as possible to the AI. However, processing everything with generative AI is not necessarily the optimal approach.
On November 4, 2026, R3 Institute launched 'Kiminomahoro for Generative AI,' a business improvement service that utilizes generative AI.
In a back-office improvement case study released by the company, they reduced the time spent by staff checking approximately 100 invoices each month from the previous 6 to 8 hours to about 30 minutes.
What is noteworthy about this case is that they did not leave all decision-making to the generative AI.
100 invoices were being checked by humans every month
R3 Institute is a company that handles enterprise system development and business improvement.
In the company's back office, approximately 100 invoices are created and sent to customers every month.
Billing information is managed in the business application 'kintone,' from which PDF invoices are generated.
However, the billing details are not the same every month.
For example, changes such as the following occur:
- Changes in usage quantities or amounts based on contracts
- Additions of billing items that occur only in specific months
- Individual change instructions from project managers
- Changes to billing addresses or recipients
- Differences from the previous month's billing details
After reflecting these changes, staff members would check the invoices one by one.
Invoices also contain items that require judgment based on contract details and past communications.
Therefore, there were parts that could not be handled by simple numerical verification alone.
It is said that they were spending 6 to 8 hours every month to check about 100 invoices.
The first thing they thought about was not 'what to automate with AI'
A distinctive feature of this initiative is that it did not assume the introduction of generative AI from the start.
The company's development team first considered whether the invoice creation process itself could be automated.
However, there is information that requires human verification and reflection, such as monthly performance data and individual changes.
Attempting to process all cases with conventional programs could have made the system complex and increased development and operational costs.
Therefore, instead of fully automating the invoice creation process, they switched to a strategy of streamlining the verification work before sending.
This is a decision that serves as a reference when considering the introduction of generative AI.
They are not aiming to use new technology for its own sake, but are considering which business processes will yield the greatest impact when improved.
Dividing roles between generative AI and conventional programs
In the automation of invoice checking, not all processing is left to generative AI.
The company organized the verification items and separated the parts that could be handled by conventional programs from those that required generative AI.
1. Matching numbers and dates using conventional programs
For example, the following checks:
- Is the invoice date in the target month?
- Do the quantity and unit price match the contract details?
- Have there been any unintended changes since the previous month?
- Does the content of the PDF match the invoice details?
These items can be judged according to predetermined conditions.
Therefore, they utilize conventional programs rather than generative AI.
2. Using generative AI for parts that require understanding the meaning of text
On the other hand, they utilize generative AI for the following types of checks:
- Whether change instructions written in free-form text have been reflected
- Whether necessary confirmations have been completed through comment exchanges with the person in charge
- Whether requests to change the recipient have been reflected in the invoice
For example, this applies when an instruction such as 'Please also invoice for the additional work this month' is received from the person in charge of the project.
The way instructions are written varies depending on the person in charge.
Therefore, it can be difficult to determine if changes have been correctly reflected based solely on simple string matching.
We utilize generative AI for these parts that require an understanding of the meaning of the text and the surrounding context.
③ Humans perform final checks on exceptional issues
Furthermore, the AI extracts invoices that require verification and presents them to the person in charge.
Instead of checking every invoice from scratch, the person in charge focuses on items that may have issues.
In other words, this system divides roles as follows:
Conventional programs: Verification based on fixed conditions
Generative AI: Verification based on text understanding and context
Humans: Verification of exceptions and final judgment
Through this division of labor, we aim to ensure the accuracy of judgments while leveraging the flexibility of generative AI.
Automatic checking by connecting Claude and kintone
In this system, we use the Claude desktop app as the generative AI.
We also connect it to kintone, which manages invoice data, using a mechanism called MCP.
MCP is a common connection method that allows AI to use external systems and data.
For example, it enables the AI to retrieve necessary information from internal systems and proceed with processing based on that content.
In this case, when the person in charge tells Claude the month to be verified, the following processing is performed.
- Retrieve invoice data for the current month from kintone
- Retrieve invoice data and contract information from the previous month
- Retrieve requests for changes to mailing addresses from another internal system
- Compare the content using conventional programs and generative AI
- Classify verification results into 'OK' and 'Needs Review'
- The person in charge performs a final check on the 'Needs Review' items
According to the company's explanation, the series of check processes by AI is completed in about 10 minutes.
In addition, the results indicate the reasons why there might be an issue and what should be checked next.
For items judged as 'OK', there is also a mechanism for the person in charge to verify the basis for the judgment.
Being able to check not only the results produced by AI but also the reasons for those judgments is important in billing operations where accuracy of amounts is required.
Verification time reduced from 6-8 hours to about 30 minutes
In this case, the actual business improvement effects have also been made public.
The verification time for the person in charge has gone from the conventional 6-8 hours to about 30 minutes.
Based on the conventional verification time, this is equivalent to a reduction of approximately 92-94%.
However, this reduction rate is a reference value calculated from the published times.
Also, the processing by AI takes an additional 10 minutes or so. It is important not to confuse the working time of the person in charge with the processing time of the system.
The results this time are not due to generative AI alone.
They are the result of combining conventional programs, system integration, judgment support by generative AI, and a review of business procedures.
Note that while the official case study reports a reduction in verification time, quantitative quality indicators such as error rates or oversight rates have not been disclosed.
Why a dedicated system was not developed
In this case, instead of developing a dedicated AI system from scratch, the existing Claude desktop application was utilized.
One reason for this is that there was only one back-office staff member using it.
When developing a dedicated system, it is necessary to prepare not only AI processing but also screens for the staff to operate.
However, by using an existing AI application, there is no need to develop new operation screens.
The company built a mechanism to utilize existing business data by connecting Claude and kintone via MCP.
What can be inferred from this is that large-scale system development is not necessarily required for AI implementation.
It is important to choose between utilizing existing tools and developing a dedicated system depending on the target tasks and the number of users.
Three points for companies introducing generative AI to keep in mind
This case study demonstrates an approach that can be applied to tasks other than invoice checking.
1. Break down tasks before deciding the scope of AI application
Before introducing generative AI, it is important to break down tasks into smaller operations.
For example, when processing inquiries from customers, it can be divided into information retrieval, content classification, drafting responses, and final verification.
Instead of processing everything with generative AI, organize which parts can be handled by conventional programs and which parts require generative AI.
2. Narrow down the cases that humans should verify
Consider whether it is necessary for humans to verify every single case.
In this case, about 5 cases that required priority verification were extracted from approximately 100 invoices.
However, there is a possibility that errors may be included in cases that the AI judged as problem-free.
Therefore, it is necessary to combine spot checks or periodic quality verification depending on the importance of the task.
3. Verify judgment accuracy even after implementation
Generative AI may produce different judgment results depending on the input information and business conditions.
Even if it works correctly at the time of implementation, it may not be able to process tasks as expected if business content or data formats change.
Therefore, it is important to have a mechanism in place to check actual operational results and, if necessary, revise judgment criteria or instructions given to the AI.
Corporate AI adoption is shifting from 'full automation' to 'appropriate division of roles'
This initiative demonstrates a philosophy for business reform using generative AI.
While generative AI can support text comprehension and flexible judgment, it is not optimal for every process.
For example, if the task is simply to verify that the contract amount matches the invoice amount, traditional programming may be sufficient.
On the other hand, generative AI can be useful for understanding change instructions written in free-form text by staff.
And when important judgments are required, such as in cases of amount discrepancies or exceptional contract terms, human verification is necessary.
When companies introduce generative AI, it is important to consider not only the performance of the technology but also which tasks within the overall workflow are most appropriately handled by whom.
Summary
On November 4, 2026, R3 Institute launched 'Kimino Mahoro for Generative AI,' a business improvement service utilizing generative AI.
In the company's published case study on improving its own invoice checking operations, the time spent by staff verifying approximately 100 invoices per month was reduced from the previous 6–8 hours to about 30 minutes.
The key feature of this approach is that it does not leave everything to generative AI.
Processes following fixed conditions are left to traditional programs, parts requiring text comprehension are left to generative AI, and exceptional judgments are left to humans.
Furthermore, by connecting existing AI applications with business systems, they have achieved business improvements without developing large-scale dedicated systems.
What is important in business reform using generative AI is not to leave as much work as possible to AI.
It will be important to break down tasks and have generative AI, traditional systems, and humans each take on the roles they excel at, thereby increasing the efficiency and quality of the entire operation.
Sources and References
[1] R3 Institute Ltd.
R3 Institute releases 'Kimino Mahoro for Generative AI' to support business improvement using generative AI
Publication date: November 4, 2026
Service launch date: November 4, 2026
Original URL:
https://prtimes.jp/main/html/rd/p/000000076.000110790.html
[2] R3 Institute Ltd.
Case Study 01: Automating invoice checking tasks of approximately 100 items per month with generative AI
Publication date: Not confirmed on the official page
Original URL:
https://www.r3it.com/services/kiminomahoro/ai-solutions/case-invoice-check-automation
