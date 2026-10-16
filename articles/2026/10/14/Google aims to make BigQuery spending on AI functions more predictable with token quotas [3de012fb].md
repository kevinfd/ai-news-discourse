---
id: "3de012fb11885bfe"
title: "Google aims to make BigQuery spending on AI functions more predictable with token quotas"
url: "https://infoworld.com/article/4235774/google-aims-to-make-bigquery-spending-on-ai-functions-more-predictable-with-token-quotas.html"
link: "https://infoworld.com/article/4235774/google-aims-to-make-bigquery-spending-on-ai-functions-more-predictable-with-token-quotas.html"
source: "InfoWorld"
domain: "infoworld.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-14T22:37:00Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Anirban Ghoshal"]
language: "en"
summary: "New project- and user-level limits for generative AI functions aim to improve cost predictability, though analysts say organizations still need broader FinOps oversight."
tags: []
orgs: ["Google"]
topics: ["business & funding", "models & research", "safety & ethics", "chips & infrastructure"]
content_source: "fulltext"
word_count: 895
paywalled: false
image: "http://www.bing.com/th?id=ONUT.oj0siY8gLA2iE9G16F5v5g&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Google aims to make BigQuery spending on AI functions more predictable with token quotas

InfoWorld · Anirban Ghoshal · 2026-10-14

New project- and user-level limits for generative AI functions aim to improve cost predictability, though analysts say organizations still need broader FinOps oversight.
Google has made daily token quotas generally available for BigQuery’s generative AI functions to give enterprises a way to limit AI consumption by project and individual user.
These quotas, which can be managed via the IAM and Admin tab in the Google Cloud Console, cover both input and output tokens at the project and individual-user levels per day and apply to the AI.GENERATE, AI.GENERATE_TABLE, AI.GENERATE_TEXT, AI.CLASSIFY, AI.IF, AI.AGG, and AI.SCORE functions.
Last year in November, the hyperscaler added AI-based SQL functions to its managed data warehouse and analytics platform to help enterprises reduce the complexity of running large-scale analytics, especially on unstructured data.
These functions, which use LLMs to prepare unstructured data for analysis, reduce the traditionally time-consuming process of preparing such data because SQL cannot understand its nuances and meaning.
However, embedding functions such as AI.GENERATE_EMBEDDING, also available as ML.GENERATE_EMBEDDING and AI.EMBED are not subject to these quotas because they run on different, substantially cheaper models, the company wrote in a blog post.
For the other functions, by default, input tokens are capped at 200 billion per project and 150 billion per user per day, while output tokens are capped at 20 billion per project and 15 billion per user per day.
The output token quotas also include the reasoning tokens used by the LLM, the company wrote, adding that enterprises also have the option to raise a request to increase these default quotas.
There is also the option to manage these quotas programmatically through the Cloud Quotas API, the gcloud CLI, and Terraform.
How BigQuery enforces token quotas
Beyond that, however, there are nuances to how the data warehouse platform enforces token quotas.
BigQuery rejects a query with a “QuotaExceeded” error if the token quota it needs has already been exhausted. If the quota runs out while the query is running, BigQuery stops sending new requests to the LLM, the company wrote in its documentation.
That means the results of a query can be affected.
For AI.IF, BigQuery can return partial results if the number of rows it cannot process stays within a specified error limit. If that limit is exceeded, the query fails, the company added.
For AI.GENERATE, though, the query can complete execution, but rows that could not be processed have no generated output and carry an error message in their status field, Google further explained.
To help enterprises avoid hitting these quotas while queries are running, Google has also added a new AI.COUNT_TOKENS function to help enterprise teams estimate token consumption before running an AI function.
However, that function too has limitations. It estimates input tokens only and does not count output or reasoning tokens, additional instructions added by the AI functions, or non-text inputs such as images.
This means the estimate may be lower than the workload’s actual token consumption.
To get a more accurate estimate though, the hyperscaler is recommending enterprise teams to run a small sample workload to measure actual token consumption before setting quotas for larger workloads.
Token quotas offer cost control, but FinOps remains essential
Despite these limitations, Pareekh Jain, principal analyst at Pareekh Consulting, sees the daily token quotas as an “important improvement” for enterprises and their CIOs scaling workloads in BigQuery.
“Earlier, unpredictable token usage could lead to unexpected costs. The new controls help CIOs manage spending, and cost predictability is an important factor in scaling any enterprise workload,” Jain said.
That cost predictability, according to Nhat Bui, deputy director of engineering at Scopic Software, could provide more data professionals with more freedom: “Analysts and data scientists can experiment with less risk of an expensive mistake.”
It also abstracts away the complexity of building mechanisms or dashboards to keep tabs on AI function-related spending in BigQuery, Bui added: “The basic guardrail is now built in: daily limits, usage history, and a function to estimate tokens before running a job. Teams no longer need custom tooling just to avoid a runaway bill.”
However, it does not abstract away the need for FinOps, said Manoj Chandra Jha, principal analyst at Nord-IQ Research.
“For CIOs, BigQuery’s token quotas cap the worst case, not the spending story. They make it safer to say yes to AI in SQL, but they count tokens rather than dollars and offer no team or business-unit budgets, so finance still can’t see who is spending what,” Jha added.
“The smart play is to treat the quotas as a floor, set real limits, structure projects by team so each becomes a de facto budget line, and layer FinOps reporting on top, because predictability without attribution is only half a governance strategy,” Jha further said.
The bigger challenge for enterprises will be balancing the trade-off between cost control and production reliability, Bui noted.
The lower the token limits, the greater the control over AI spending, but the higher the risk of disrupting production workloads, as queries may fail or return incomplete results when quotas are exhausted before the daily reset, Bui said.
To balance these competing priorities, enterprises should separate production workloads from development and experimental workloads, giving the former more room to operate while keeping tighter limits on the latter, Jha said.
Enterprises should also build pipelines that detect skipped rows and process them again after quotas reset, Jha added.
