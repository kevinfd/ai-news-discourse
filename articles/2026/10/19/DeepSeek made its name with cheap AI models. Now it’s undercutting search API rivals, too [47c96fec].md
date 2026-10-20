---
id: "47c96feca6a38a98"
title: "DeepSeek made its name with cheap AI models. Now it’s undercutting search API rivals, too."
url: "https://thenewstack.io/deepseek-web-search-api"
link: "https://thenewstack.io/deepseek-web-search-api"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-19T14:29:42Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Paul Sawers"]
language: "en"
summary: "Not content with challenging the major frontier AI labs with lower-cost models , Chinese AI company DeepSeek is setting its sights on the search API market. On Saturday, the company announced it has opened up its internally developed search engine to outside developers through two new APIs, Search and Fetch , allowing them to retrieve live web search results and webpage content for use in their…"
tags: ["AI", "AI Agents", "AI Infrastructure", "Developer tools"]
orgs: ["DeepSeek", "China", "Microsoft", "Perplexity", "Google"]
topics: ["search & media", "agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 1550
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# DeepSeek made its name with cheap AI models. Now it’s undercutting search API rivals, too.

The New Stack · Paul Sawers · 2026-10-19

DeepSeek made its name with cheap AI models. Now it’s undercutting search API rivals, too.
Not content with challenging the major frontier AI labs with lower-cost models, Chinese AI company DeepSeek is setting its sights on the search API market.
On Saturday, the company announced it has opened up its internally developed search engine to outside developers through two new APIs, Search and Fetch, allowing them to retrieve live web search results and webpage content for use in their own apps and agents.
Both services cost $0.75 per 1,000 successful requests, and developers can use them independently of DeepSeek’s AI models.
The launch also came alongside DeepSeek-V4.1-Flash-1017, a minor update to the V4.1 Flash model the company released in September.
Why AI agents need web search
Large language models (LLMs) are trained on data collected up to a certain point in time, meaning they can’t always answer questions about recent events, updated documentation, or any other kind of dynamic information. By supporting live web search, models can retrieve current information from the internet, which supplements their responses.
For developers building AI agents, this is particularly important. A coding agent, for example, might need to consult the latest software documentation, investigate a recently disclosed vulnerability, or otherwise check that a particular library has been updated.
Until now, developers using DeepSeek’s models had several ways to provide this functionality. They could connect their applications to third-party search services, or use DeepSeek’s existing search functionality through its model API.
Indeed, when DeepSeek open-sourced its agent harness in August, it included web search among its capabilities. The Harness supported interchangeable search providers, including Exa, Perplexity and DeepSeek itself. However, accessing DeepSeek’s native search through the Harness required an additional model request, with each search running as a separate call to a DeepSeek model, according to the Harness documentation, introducing extra latency and token costs.
The new APIs are designed to simplify that process. Developers can now call DeepSeek’s Search endpoint directly to retrieve ranked web results, including titles, URLs, snippets and summaries, while the Fetch endpoint retrieves the contents of individual webpages in Markdown format.
“Neither requires a separate model request, meaning developers can integrate DeepSeek’s search capabilities into applications powered by competing AI models, too.”
Neither requires a separate model request, meaning developers can integrate DeepSeek’s search capabilities into applications powered by competing AI models, too.
DeepSeek develops an in-house engine
For much of the past two years, DeepSeek has relied on outside providers to power web search, even as it was building its own.
For context, in March 2025, Chinese business publication National Business Daily reported that DeepSeek had integrated the search API of Bocha, a Chinese AI search startup based in Hangzhou. Bocha’s CTO, Weng Rouying, noted that DeepSeek had been using its service prior to the chatbot’s surge in popularity earlier that year.
DeepSeek’s own February 2025 privacy policy, meanwhile, also acknowledged its reliance on third-party search services, naming Microsoft’s Bing as an example of an external API provider.
“Behind the scenes, the company has also been laying the groundwork for its own search infrastructure.”
Behind the scenes, the company has also been laying the groundwork for its own search infrastructure. In January this year, Bloomberg reported that DeepSeek was recruiting engineers to build a multilingual AI search engine, according to job ads listed by the company. The planned capabilities reportedly extended beyond text searches to include images and audio.
Fast-forward some nine months, and the company says its internally developed search engine, dubbed DeepSeek Search, already handles hundreds of millions of requests daily, and maintains an index containing hundreds of billions of webpages.
According to its October 17 changelog, the engine supports multilingual searches and uses filtering mechanisms designed to identify search spam, low-quality AI-generated material, and attempts to manipulate search rankings.
DeepSeek has disclosed relatively little about the underlying architecture, or how it builds and maintains its index. It’s also not clear whether the company has entirely replaced its external search suppliers across the board.
A growing market for AI search
Building a search engine is no trivial undertaking. It requires the infrastructure to crawl webpages, maintain an index of their contents and rank results, while continuously updating that information as the web changes. For years, that meant developers who wanted raw search results for their applications largely turned to Google and Microsoft, the two companies with web-scale indexes of their own.
Now, however, a growing number of companies are investing in their own search infrastructure, increasingly with AI applications and agents squarely in mind. Brave, for example, operates an independent index of more than 40 billion webpages, which it says is maintained through its own crawler and other discovery mechanisms. AI search company Exa, meanwhile, has also developed its own crawling and indexing infrastructure.
Perplexity has similarly invested in proprietary search infrastructure, including building its own crawling and indexing systems. Another competitor, Parallel, says it has built its search infrastructure from the ground up, including the crawling, indexing, query processing and ranking components.
Cloudflare is also entering the market from a different angle. Earlier this month, the company launched a Web Search API through its AI Gateway, allowing developers to access search results from serveral providers through a single interface. The service, currently in beta, uses Ceramic as its default provider and charges customers at each provider’s published API rates, without additional markup.
“DeepSeek, for its part, is competing aggressively against the incumbents on price.”
DeepSeek, for its part, is competing aggressively against the incumbents on price, although it’s not strictly the cheapest option available. Ceramic.ai, which provides keyword-based web search for AI agents, charges $0.25 per 1,000 queries on its pay-as-you-go plan.
Still, DeepSeek’s $0.75 per 1,000 successful searches compares favorably with many others, including Parallel’s Turbo and Fast search services and Perplexity’s Fast Search API, both of which charge $1 per 1,000 searches. Meanwhile, Exa charges $4 per 1,000 Instant Search requests, while Brave charges $5 per 1,000 searches. Other notable players include Tavily, a search API provider for AI agents that European AI infrastructure company Nebius acquired in February. Tavily charges $8 per 1,000 basic searches on its pay-as-you-go plan.
It’s worth noting that the various services differ in terms of retrieval capabilities, result limits and performance, so the prices aren’t necessarily entirely comparable. But they provide some useful benchmarks for DeepSeek’s move into the search infrastructure space.
The emergence of these alternatives also comes as Google and Microsoft have withdrawn longstanding search API offerings. Microsoft retired its Bing Search APIs in August 2025, while Google has closed its Custom Search JSON API to new customers, with existing users required to migrate by January 1, 2027. Both companies continue to provide search functionality through their respective AI platforms, including Grounding with Google Search for Gemini and Grounding with Bing Search for Microsoft Foundry agents. These services allow AI models operating within their respective platforms to retrieve web information and generate answers with citations.
Standalone APIs such as DeepSeek’s give developers direct access to search results, which they can use with AI models and applications of their choosing.
Developer reaction and the fine print
The announcement has sparked considerable discussion among developers about pricing and whether the new APIs offer much beyond existing search integrations. On Reddit, one user welcomed the cost in particular. “I don’t think any other search provider comes close to the price that DeepSeek is offering,” they write.
Others questioned what the announcement would ultimately change for users already accessing web search through third-party tools. One Reddit user notes that they are already using DeepSeek with the Hermes AI agent, which could search the web. Another user responded that those who had already configured their own search tools might see little immediate benefit from the new APIs.
A similar discussion emerged on Hacker News, where one developer questions the need for paid search APIs when free, self-hosted alternatives such as SearXNG were available. Another commenter argues that businesses have additional requirements, citing “reliable latency, data processing guarantees” and the potential risk of exposing sensitive company information through search queries.
For businesses weighing DeepSeek’s APIs, that last point carries an extra dimension. DeepSeek’s privacy policy states that it collects, processes and stores personal data in China, and that it generally keeps user inputs for as long as an account remains open. The Search and Fetch documentation, however, doesn’t say how long search queries specifically are retained.
The discussions highlight the differing needs of individual developers and businesses, particularly when it comes to cost, reliability, and handling large numbers of requests. And while DeepSeek’s pricing is certainly competitive, there are some practical restrictions worth considering.
According to its API documentation, Search and Fetch requests are each capped at five per second per account, although individual searches can return up to 50 results without increasing the request price. DeepSeek also only bills for requests that return results, so failed calls, empty searches, and timeouts are free.
DeepSeek is temporarily waiving Search and Fetch charges for server-side tool calls made through DeepSeek Harness, Claude Code, and Codex when using its API. That is very much a temporary arrangement, however, one that ends on October 31, when the standard per-request charges take effect. Direct calls to the standalone APIs are already billable, according to DeepSeek’s announcement.
