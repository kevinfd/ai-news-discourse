---
id: "cc69239e629b14a0"
title: "Get answers from tables with tabular search in Amazon Bedrock Managed Knowledge Base"
url: "https://aws.amazon.com/blogs/machine-learning/get-answers-from-tables-with-tabular-search-in-amazon-bedrock-managed-knowledge-base"
link: "https://aws.amazon.com/blogs/machine-learning/get-answers-from-tables-with-tabular-search-in-amazon-bedrock-managed-knowledge-base"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-16T16:12:16Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Josh DeMuth"]
language: "en"
summary: "Amazon Bedrock Managed Knowledge Base now supports tabular search, so you can get answers from tables through agentic retrieval. When a question needs data from CSV, XLSX, or XLS files, tabular search looks up values and runs calculations across every relevant row in one or more tables or sheets. It then combines the results with facts from related documents to answer analytical questions that…"
tags: ["Amazon Bedrock", "Amazon Bedrock Knowledge Bases", "Intermediate (200)", "Technical How-to"]
orgs: ["Amazon", "Microsoft"]
topics: ["search & media", "agents & coding", "policy & regulation", "models & research"]
content_source: "fulltext"
word_count: 2796
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Get answers from tables with tabular search in Amazon Bedrock Managed Knowledge Base

AWS Machine Learning Blog · Josh DeMuth · 2026-11-16

Artificial Intelligence
Get answers from tables with tabular search in Amazon Bedrock Managed Knowledge Base
Amazon Bedrock Managed Knowledge Base now supports tabular search, so you can get answers from tables through agentic retrieval. When a question needs data from CSV, XLSX, or XLS files, tabular search looks up values and runs calculations across every relevant row in one or more tables or sheets. It then combines the results with facts from related documents to answer analytical questions that take several steps.
A finance team closing the quarter needs to know “Which departments must write variance commentary?” No single file has the answer. It depends on the variance policy’s threshold, the quarter-close memo’s budget revisions, and math over every department in the profit and loss (P&L) workbook.
Like this finance team, most teams keep their narratives and data in the same place. For example, a Microsoft SharePoint site holds workbooks next to policies, and an Amazon Simple Storage Service (Amazon S3) bucket holds CSV exports next to PDFs. Tabular search answers questions across these files through the same AgenticRetrieveStream request you already use for documents. It runs code over the original file in an isolated sandbox, so the answer uses the whole table instead of only the rows that retrieval returns. For the finance team, one request returns the departments that must write commentary. The answer cites the policy and the memo, and the trace names the workbook the code read.
In this post, you learn how tabular search answers questions that need both table data and facts from documents, and when another tool is a better fit. You also build a knowledge base with sample finance files and use the trace to see which file the code read.
Why tables are hard for retrieval
Retrieval Augmented Generation (RAG) returns a fixed number of passages that best match a question, which works well for prose. Tables lose information when they’re split into passages, in ways that depend on the table’s shape:
- Long tables – A table with thousands of rows spans many passages, and retrieval returns only the few that best match the question. An answer built from them uses a handful of rows, so a total, a comparison, or a threshold check can be incomplete.
- Wide tables – In a table with hundreds of columns, one row can hold more text than a passage or a search model takes in at once. As a result, values in later columns are harder to match. Long passages from wide tables can also match many unrelated questions and push more relevant passages out of the results.
Retrieval also has to match a question to the right table. Questions use business terms, such as “controllable spend,” but tables hold cost center codes, account names, and numbers. A draft and a final workbook look almost the same to search. The rule that gives the numbers meaning is often in a separate document, such as a policy.
Tabular search therefore splits the work. Retrieval only has to return one passage from the right table file, and code then reads the whole table. Because retrieval still has to find that file first, naming the file in your question helps.
Table 1 shows how plain retrieval and tabular search each handle the finance team’s question, “Which departments must write variance commentary?”
Table 1: The same question with plain retrieval and with tabular search.
How tabular search works in agentic retrieval
In agentic retrieval, an agent uses retrieval to decide which documents matter and then writes the answer. Tabular search is part of that flow, so there’s nothing to turn on.
When a question needs the data in a table, the request moves through these stages:
- Retrieve – Passages come back, including passages from a table file.
- Plan – The agent uses the question and table structure to determine whether to run code over one or more retrieved tables.
- Stage – Tabular search copies the original file into an isolated sandbox with no network access.
- Compute – Model-written code runs over the whole table or sheet.
- Return – The agent gets back only what the code prints, such as totals or matching rows.
- Answer – The agent answers from the results and the passages, with citations.
Tabular search starts when retrieved passages come from a CSV, XLSX, or XLS file and the question needs a calculation across rows or a lookup of specific values.
Knowledge bases, connectors, and APIs
An AgenticRetrieveStream request can search one knowledge base or several. The Retrieve API keeps returning passages and doesn’t run code.
Tabular search works the same way whichever connector brings the files into the knowledge base, including Amazon S3, Microsoft SharePoint, Atlassian Confluence, and others.
Scope and trade-offs
Tabular search is built for questions that need calculations or lookups over the table files it retrieves. Running code adds at least one more agent turn, so answers that use table data take longer than text-only answers. Governed metrics, recurring dashboards, warehouse-scale joins, and reporting controls still belong in your business intelligence (BI) tools. Tabular search works on table files stored next to your documents, and you don’t define a schema.
Solution overview
In this solution, an Amazon Bedrock Managed Knowledge Base stores your CSV and Excel files together with related documents, such as PDF and Word files. Your application sends every question through agentic retrieval. When a question needs table data, the answer combines calculations over your tables with facts from your documents. It cites the passages it used, and the trace names the table files the code read.
In Figure 1, an Amazon S3 data source syncs these files into the knowledge base, which keeps embeddings, text, metadata, and the original files. When your application sends a question with AgenticRetrieveStream, agentic retrieval plans the work and retrieves passages from the knowledge base. If the question needs data from a table file, it sends the files to read to an isolated sandbox with no network access. There, model-written code runs over the original file and returns printed results. The answer, with citations and trace events, streams back to your application.
The worked example uses fictitious AnyCompany Retail finance files:
- Final P&L workbook (anycompany-pnl-fy2026.xlsx). It has Notes, Actuals, Budget, and Summary sheets, with one row per month, cost center, and account in the Actuals and Budget sheets.
- Draft workbook. A preliminary copy with different Q3 numbers.
- Finance variance policy (PDF). Defines controllable spend and approved budget, and sets review thresholds.
- Q3 close memo (Word). Lists approved and rejected budget revisions.
- Business review (Markdown). Explains the main variances.
These files are in the tabular-search folder of the sample-managed-knowledge-base-patterns GitHub repository. The folder also has an AWS Cloud Development Kit (AWS CDK) app that deploys the resources in this post, and Python scripts that ask these questions.
Prerequisites
You need the following:
- Permissions to create AWS Identity and Access Management (IAM) roles, S3 buckets, and Amazon Bedrock knowledge bases.
- For the identity that calls AgenticRetrieveStream, the permissions for agentic retrieval, including bedrock:GetDocumentContent. The agent reads the original table file with the caller’s credentials.
- Amazon Bedrock in an AWS Region where tabular search is available. For Region availability, see Supported AWS Regions.
- Your own CSV, XLSX, or XLS files and related documents.
- To follow the walkthrough: Python 3.10 or later with the AWS SDK for Python (Boto3) version 1.43.123 or later. You can also ask questions from the knowledge base test window in the Amazon Bedrock console or with the AWS Command Line Interface (AWS CLI).
The calling identity needs this policy, from the agentic retrieval documentation:
For costs, see Amazon Bedrock pricing.
Upload your files to Amazon S3
Put the table files and related documents under one prefix.
- Open the Amazon S3 console and choose Create bucket.
- Enter a globally unique bucket name (this post uses amzn-s3-demo-bucket), keep Block all public access selected, and choose Create bucket.
- Choose the bucket, choose Create folder, and enter finance.
- Open the finance folder and choose Upload.
- Choose Add files, select your table files and documents, and choose Upload.
Create the knowledge base and data source
The knowledge base needs an IAM role that Amazon Bedrock can assume. This trust policy allows only the bedrock.amazonaws.com service principal, and only for knowledge bases in your account.
Next, set up the remaining resources:
- Create a role named kb-finance-role with the trust policy.
- Attach an inline policy that allows s3:ListBucket on the bucket and s3:GetObject on its objects.
- Create a knowledge base of type MANAGED with the managed embedding model.
- Create a MANAGED_KNOWLEDGE_BASE_CONNECTOR data source for the bucket, limited to the finance/ prefix.
- Set maxFileSizeInMegaBytes above your largest file.
The inline policy for step 2 allows reads on this bucket only:
This script runs steps 3 to 5 and prints the IDs:
Sync the data source and check file types
Tabular search can start only if the knowledge base assigns the right file type, so check the file type after the first sync.
- Start an ingestion job for the data source.
- Poll the job until its status is COMPLETE.
- Review the job statistics for failed documents.
- Run a Retrieve call with your question.
- Confirm that table passages show _file_type as CSV (for CSV files) or MS_EXCEL (for XLSX and XLS files).
The first script runs steps 1 to 3:
The second script runs steps 4 and 5 so you can check the table file type before asking the question with agentic retrieval. With your own files, ask a question that pairs a rule in one of your documents with a calculation over your tables, and name both.
Ask a question across tables and documents
Send the same question through AgenticRetrieveStream. The script prints the answer, each CodeExecution status, and the files the code read.
For these files, the answer combines two workbook tables with two documents:
- From the documents. The finance policy defines controllable spend as the Contractors, Travel, Software, and Marketing Programs accounts, which leaves out salaries and facilities. The business review explains the main variances.
- From the tables. The code uses every row in the Actuals and Budget sheets, filters both to fiscal Q2 and the four accounts, and then compares cost centers.
- Answer. CC-3010 (Platform) is over by 124,559.90 US dollars, with actual spending of 394,859.90 against a budget of 270,300.00. The business review attributes the variance to contractors brought in for a data platform migration. Counting every operating expense account instead gives 133,434.05.
Read the trace
Trace events arrive in this order:
- Planning. A Planning event with status SUCCEEDED includes a codeExecution action that names the documents the code will read.
- The code step. A CodeExecution event with status IN_PROGRESS (“Running code over 1 document(s)”), then one with status SUCCEEDED. The SUCCEEDED message names each file the code read and its size.
- The answer. A second planning round and the response text precede a final result event that includes the citations. Citations point to the passages the answer used, so a table file the code read isn’t always among them.
In this example, the Planning event names only the final workbook, because the policy and the business review arrive as retrieved passages.
On longer calls, the stream repeats the IN_PROGRESS event every 10 seconds, so a read timeout doesn’t fire. A code step that can’t finish reports FAILED, and the agent usually retries or falls back.
Tabular search runs as part of response generation, which is on by default, so the script leaves generateResponse unset. If you set generateResponse to false, the agent returns retrieval results without running code. For details, see agentic retrieval.
Try more questions
Each of the following questions also pairs a document with the workbook.
Apply memo revisions to quarterly totals
This question needs a budget that exists only after the memo’s revisions:
The answer uses the revisions from the memo and the Q3 actuals and original budget from the workbook. Spending came in 49,572.40 US dollars under the revised budget, so the answer is yes, even though the same spending is over the original budget. Plain Retrieve returns memo and workbook passages, but none of them contains these figures.
Apply a policy threshold after budget revisions
Here is the full version of the finance team’s question from the introduction. It needs the policy’s threshold, the memo’s revisions, and the workbook:
The policy requires commentary when the variance exceeds 5 percent of the approved budget, which includes approved revisions, and the memo approves a Marketing increase and an Engineering cut. The answer is Sales (-6.50 percent), Engineering (+5.79 percent), and Operations (+6.20 percent). Engineering crosses the threshold only because the approved cut lowers its budget.
Continue the conversation
Tabular search also works in multi-turn conversations. Send earlier turns in messages, and it runs in whichever turn needs the table. This first question asks for a calculation from the workbook:
For the follow-up, send the first question, its answer ("role": "assistant"), and the new question in messages:
The variance is 12.40 percent over budget, so it needs written commentary. Because it exceeds 10 percent, the policy also requires review by the CFO, Nikki Wolf. Here, the first turn usually runs code over the workbook, and the second answers the policy question from the history.
For longer sessions, you can keep conversation history in an Amazon Bedrock AgentCore memory resource by setting memoryConfiguration on the request, instead of resending earlier turns. For details, see agentic retrieval.
Best practices for questions over tables
Word your questions with care, because retrieval picks which table the code reads. Focused questions that name their sources help retrieval pick the right table.
- Pair one rule with one table. Name the document that holds the rule, such as “as revised in the Q3 close memo.”
- Name the file when there is more than one version. For example, “use the final FY2026 P&L workbook, anycompany-pnl-fy2026.xlsx.”
- Ask for the calculation when you want one. If a summary sheet holds a figure, the agent can answer from it. Say “Calculate each department’s variance from the Actuals and Budget sheets” to compute from detail rows.
- Ask focused questions. Build larger analyses over several turns.
A few data and application choices help as well:
- Keep tables in CSV, XLSX, or XLS files. Export tables from PDF or Word documents first.
- Set the file size filter above your largest table. Files larger than maxFileSizeInMegaBytes aren’t ingested, so the code can’t read them.
- Keep Excel sheets within 200 MB. As of this writing, tabular search runs code over CSV files up to 500 MB, the ingestion limit, but over Excel sheets only up to 200 MB. You can still ingest larger Excel files, so check sheet sizes before you rely on full-table calculations.
- Use tabular search for analysis. Running code adds an agent turn, so keep plain Retrieve for quick lookups in text.
- Scope files with metadata filters. A filter under retrievalOverrides, for example on _document_title, controls which files the code can read.
- Audit with the trace. The generated code isn’t returned, by design, because it can echo cell values. The trace shows which files the code read.
Clean up
To avoid ongoing charges, delete these resources in order:
- In the Amazon Bedrock console, choose Knowledge Bases, then choose finance-kb.
- Select the finance-s3 data source and choose Delete.
- Delete the finance-kb knowledge base.
- In the Amazon S3 console, select the bucket, choose Empty, and then choose Delete, unless other workloads use it.
- In the IAM console, choose Roles, select kb-finance-role, and choose Delete.
If you deployed with the AWS CDK app from the repository, run npx cdk destroy from its infra folder instead of these steps. It deletes everything the stack created.
Conclusion
The finance team members need to know “Which departments must write variance commentary?” With tabular search in Amazon Bedrock Managed Knowledge Base, you can answer that question with one agentic retrieval request that uses the workbook, the policy, and the memo together.
In this post, you learned how tabular search answers questions that need both table data and facts from documents, and when another tool is a better fit. You also built a knowledge base with sample finance files and used the trace to see which file the code read.
To get started, see Build a managed knowledge base and agentic retrieval in the Amazon Bedrock User Guide, and AgenticRetrieveStream in the Amazon Bedrock API Reference. To learn more, read Build enterprise search for agents with Amazon Bedrock Managed Knowledge Base on the AWS Artificial Intelligence Blog.
