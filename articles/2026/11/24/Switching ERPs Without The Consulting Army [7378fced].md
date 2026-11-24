---
id: "7378fcedb3e8d6ba"
title: "Switching ERPs Without The Consulting Army"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/24/switching-erps-without-the-consulting-army"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/24/switching-erps-without-the-consulting-army"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-24T11:00:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Deepak Padgaonkar, Forbes Councils Member"]
language: "en"
summary: "AI is changing ERP migration by reducing manual work, automating data mapping and reconciliation, and enabling smaller, more specialized implementation teams."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Microsoft"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 1003
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/69bd89589cd379dce8e00582/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Switching ERPs Without The Consulting Army

Forbes · Deepak Padgaonkar, Forbes Councils Member · 2026-11-24

Deepak Padgaonkar, founding member of V3iT.
For decades, replacing an enterprise resource planning (ERP) system has meant systems integrators, functional consultants, migration specialists, developers, months of workshops, mapping spreadsheets, testing and reconciliation.
Yet, much of this work follows a predictable pattern: discover, profile, map, transform, validate, load, reconcile and, finally, approve.
That is where AI can change ERP implementation economics.
The future is not a completely autonomous ERP project. It is a small implementation team supervising an AI-driven migration factory instead of a consulting army manually performing every step.
The Foundation Already Exists
SAP provides the S/4HANA Migration Cockpit, including migration objects and staging mechanisms. Microsoft Dynamics 365 provides its Data Management Framework, with reusable data entities for customers, vendors, products, orders and balances. NetSuite supports migration through CSV imports and SuiteCloud/REST interfaces.
AI-assisted migration tools are beginning to approach the problem differently. Platforms such as TRANXACT.AI, use AI to connect to source systems, map data and support migration through a pipeline that can run alongside existing systems. The broader trend is toward treating migration as a continuous data-management process rather than a one-time conversion project.
Rather than replace migration technology, the opportunity is to put an AI orchestration, reasoning and reconciliation layer around it. That layer matters because loading data is the easy part; deciding what the data should become is not. Captured as reviewable rules, it can be tested, reused and audited, and the CIO’s question shifts from how many people a migration needs to how well its decisions are governed. 
From Mapping Records To Governing Rules
Imagine connecting the legacy and target ERPs to an AI orchestration layer. Instead of hundreds of hours of discovery and spreadsheets, AI inventories source structures and compares them with target APIs, migration objects and data entities.
Consider a hypothetical: A legacy system stores a payment term as one code, and the new system expects another. Instead of someone fixing it row by row in a spreadsheet, AI recognizes the pattern and proposes a rule.
A human approves the rule once; it is applied across thousands of records. 
Where AI is uncertain, such as with an ambiguous ledger account, it routes the decision to someone qualified to make it. The model changes from humans mapping everything to humans reviewing exceptions and approving rules. 
AI Can Rebuild—And Prove—The Books
Consider moving from 2,400 legacy GL accounts to a redesigned chart of 1,100. AI can analyze descriptions, historical postings, cost centers and account types to propose mappings while routing uncertain decisions to the controller.
More importantly, reconciliation becomes continuous.
If the two systems agree on assets, but differ between liabilities and equity, AI can trace the variance to the postings and mapping rule behind it and propose a correction.
The question changes from “Why don’t the systems reconcile?” to “Do we approve this correction?” 
That matters for financial controls. Continuous reconciliation catches errors while they are small and their cause is obvious. Every mapping, correction and approval is recorded with its rationale, giving auditors a documented trail. And oversight sharpens rather than disappears: Controllers stay accountable, with explicit approval rights, thresholds and segregation of duties.
What Organizations Should Expect
Whatever tool they choose, buyers should insist on continuous reconciliation across every period and subledger, proposals a finance user can understand, traceability from source record to target, human approval of accounting treatment and results that can be verified independently of the tool that produced them.
How Much History Should Move?
An opening-balance migration moves master data, GL balances, open receivables and payables, inventory, fixed assets and open orders while historical transactions remain archived.
A historical migration might bring one, three or five years of detail, with AI analyzing dependencies, sequencing loads, identifying missing references and reconciling results.
For many companies, a hybrid makes sense:
• Current And Prior Year: transaction detail
• Years 3–7: summarized monthly balances
• Older History: analytical archive
• Open Documents: individually migrated
• Master Data: fully migrated
This provides useful history without reproducing decades of legacy complexity.
Where to draw those lines depends on regulatory and tax retention rules, management’s need for multiyear transaction-level reporting, the quality of older data, the cost of converting and reconciling each additional year, performance in the new system and auditors’ access to archived records.
A useful rule: Move what the business needs to operate, archive what it must retain and leave the rest.
From Consulting Army To Migration Factory
An AI-driven migration factory profiles transactions, proposes account mappings, detects duplicates, generates transformation rules, identifies invalid data, executes approved loads, compares balances and produces reconciliation evidence.
Humans concentrate on judgment. Should these accounts be consolidated? Which duplicate vendor is authoritative? Is the accounting treatment correct? Is the reconciliation acceptable? Are we ready to go live?
The New ERP Implementation Model
AI does not eliminate ERP expertise. It reduces repetitive migration labor while preserving human control over accounting, configuration, compliance and business decisions.
The conventional model scales by adding people. An AI migration factory scales through connectors, mappings, validation rules, reconciliation agents and exception management.
The implementation team does not disappear. It gets smaller and more specialized.
Firms and IT teams will need to adapt. The most valuable skills will blend accounting, process knowledge and data governance with the ability to supervise automation. Billable-headcount consulting will give way to smaller senior teams and outcome-based pricing.
New risks emerge, too: over-trusted confidence scores, flawed rules propagating at scale and knowledge concentrated in too few people. Sampling auto-approved work and validating independently before cutover become essential. 
The Bottom Line
For 30 years, companies bought sophisticated ERP software and hired armies of people to move their businesses into it. The next generation is reversing that relationship: the software is increasingly helping to move the business itself.
ERP migration will never be entirely mechanical, but extracting 22 million ledger lines, proposing mappings, loading approved data, reconciling systems and identifying the 37 transactions that do not match? More and more, there is little reason for humans to spend thousands of hours doing that manually.
