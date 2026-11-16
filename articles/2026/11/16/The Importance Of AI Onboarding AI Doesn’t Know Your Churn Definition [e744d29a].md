---
id: "e744d29aa0076a31"
title: "The Importance Of AI Onboarding: AI Doesn’t Know Your Churn Definition"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/16/the-importance-of-ai-onboarding-ai-doesnt-know-your-churn-definition"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/16/the-importance-of-ai-onboarding-ai-doesnt-know-your-churn-definition"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-16T12:15:00Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Pawel Rzeszucinski, Forbes Councils Member"]
language: "en"
summary: "Great analytical skills are different from subject matter expertise, and just like any new employee, regardless of how talented, AI needs proper onboarding."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Anthropic", "OpenAI", "Google"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 995
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6a5f9bf85e28cb8c549f516e/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# The Importance Of AI Onboarding: AI Doesn’t Know Your Churn Definition

Forbes · Pawel Rzeszucinski, Forbes Councils Member · 2026-11-16

Pawel Rzeszucinski is Senior Director of Data and AI at WebPros.
Almost overnight, every employee with a corporate license for Claude, ChatGPT or Gemini gained access to a remarkably skillful data analyst. It writes SQL in seconds and answers at 2 a.m. without hesitation. There is a catch, however. That analyst started work this morning, and nobody has told it how your business works.
When Anthropic pointed its own model at its data warehouse without supporting context, accuracy on internal analytics evaluations never exceeded 21%, according to the company’s account of how it enables self-service analytics with Claude. Once curated context was added, accuracy consistently rose above 95%. Same model, same data, radically different answers.
From my perspective, many organizations are misled by their AI analysts every day, because they treat a brilliant new hire as a seasoned veteran. Great analytical skills are different from subject matter expertise, and just like any new employee, regardless of how talented, AI needs proper onboarding.
A Skilled Analyst Without Onboarding
No sensible company hands a new analyst warehouse credentials on day one and asks for the board’s churn figure by Friday. A new hire is walked through the KPIs, taught which tables can be trusted, how to read the schemas and how to join them correctly, then shown which numbers leadership actually reviews. Then there are the data quirks and gotchas that analytics teams have accumulated over the years. Yet the opposite happens every time an employee opens a general purpose assistant, connects it to a spreadsheet or database and asks a business question. It knows SQL. It does not know your business.
That gap shows up in three predictable ways. Generic questions produce generic answers, drawn from industry patterns rather than the daily operations of your business.
Undefined metrics are worse. Churn is the classic example. A subscription business might count cancelled contracts, a usage-based product might count accounts dormant for 30 days and two product lines inside the same organization can define it differently. AI teams have identified this ambiguity between business concepts and the data representing them as a leading cause of wrong answers, alongside stale definitions and retrieval failures.
Most dangerous of all are questions about data that does not exist in the warehouse. A human analyst would say, “We don’t track that.” An AI analyst, built to be “a helpful assistant,” may assemble a plausible proxy or, in the worst case, invent a figure outright. The answer arrives confidently wrong.
Self-Service With Conditions Attached
It is tempting for individuals equipped with new general-purpose AI tools to skip the data team entirely. But the arrival of a new tool should not mean common sense leaves the building. BlackFog research published in January 2026 found that 51% of employees have connected AI tools to work systems without IT’s approval or knowledge, and 69% of presidents and C-suite leaders believe speed trumps privacy and security. The pattern starts at the top. Meanwhile, Gartner’s April 2026 research shows that organizations with successful AI initiatives invest up to four times more in foundations such as data quality and governance than those with poor outcomes.
Data teams face a choice of their own. For decades, self-service analytics has been the holy grail of efficient organizations, and it is now genuinely within reach. The data teams that thrive will shift their focus from building dashboards and reports to managing metadata and building a context hub: the glossary, metric definitions, table relationships and ownership records an AI analyst needs before its first query. Gartner argues that context, including semantics and metadata, has become mission critical for how AI agents reason. Data teams will also build MCP servers that give agents governed routes into data sources and engineer the harnesses, meaning the skills, guardrails and evaluations, that keep AI analysts well guided. The data team stops being a report factory and becomes the onboarding department for every AI analyst in the company.
Onboarding Your AI Analysts Like Your Best Hires
Every level of the organization has a part to play in that onboarding:
Write the onboarding pack before the first question. Document the 20 to 30 KPIs leadership reviews each month, with formula, filters, source table and owner. Anthropic recommends generating documentation with the model but having a human own every definition.
Define metrics per product, not just per company. Where churn or revenue differs across product lines, record each version explicitly and name it distinctly. An AI analyst that knows three definitions exist will ask which one you mean.
Give AI analysts approved routes to the data. Data teams should build MCP servers that expose curated, governed datasets rather than raw tables. Anthropic, for instance, limits its Slack analytics agent to its semantic layer and the curated marts behind it. Agents cannot misuse sources they cannot reach.
Engineer the harness and test it. Build an evaluation set of real business questions with verified answers, and measure accuracy with and without context. Include questions about data you do not hold, so you know the agent will say so instead of guessing.
Make governed context an executive requirement. Leadership should ask how every insight was produced: which context, which MCP, which harness. If the answer is “I pasted it into a chat,” it does not belong in the board pack.
Conclusion
Your AI analyst is not lying on purpose. It is doing what any talented but uninformed new hire would do: filling gaps with confident assumptions. The holy grail of self-service analytics has arrived, but only for organizations willing to do the unglamorous work of onboarding. Data teams become architects of context, executives become the ones who demand it and employees keep the common sense no tool can replace. So ask yourself: Would you let a new hire present to the board in their first week? Then why let an AI analyst do it without onboarding?
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
