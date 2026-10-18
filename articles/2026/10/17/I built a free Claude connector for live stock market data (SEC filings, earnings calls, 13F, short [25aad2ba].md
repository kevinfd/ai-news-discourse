---
id: "25aad2bac13ac7dd"
title: "I built a free Claude connector for live stock market data (SEC filings, earnings calls, 13F, short interest). It's an MCP server and works in ChatGPT too"
url: "https://reddit.com/r/ClaudeAI/comments/1x8iv1t/i_built_a_free_claude_connector_for_live_stock"
link: "https://reddit.com/r/ClaudeAI/comments/1x8iv1t/i_built_a_free_claude_connector_for_live_stock"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T19:25:45Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["DanielAPO"]
language: "en"
summary: "I got tired of asking Claude about a stock and getting a confident answer based on year-old training data. So I built Equibles, a connector that gives Claude real stock market data. It's an MCP server, so Claude just calls it like any other tool, and it's listed in Claude's connector directory. What Claude can pull with it: SEC filings, full text. It searches inside 10-Ks, 10-Qs and 8-Ks and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "US government", "OpenAI", "Nvidia", "Microsoft", "Apple", "China", "UK"]
topics: ["agents & coding", "business & funding", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 484
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8iv1t/i_built_a_free_claude_connector_for_live_stock/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a free Claude connector for live stock market data (SEC filings, earnings calls, 13F, short interest). It's an MCP server and works in ChatGPT too

Reddit · DanielAPO · 2026-10-17

I got tired of asking Claude about a stock and getting a confident answer based on year-old training data. So I built Equibles, a connector that gives Claude real stock market data. It's an MCP server, so Claude just calls it like any other tool, and it's listed in Claude's connector directory. What Claude can pull with it: SEC filings, full text. It searches inside 10-Ks, 10-Qs and 8-Ks and then reads the exact lines, so it quotes the filing instead of paraphrasing from memory earnings call transcripts, split by speaker financial statements, KPIs, guidance and analyst estimates 13F holdings, insider trades and congressional trades short interest, daily short volume, squeeze scores and an estimate of the next FINRA short interest number prices, a screener, Fed economic data, and option chains on the paid plans European, UK, Hong Kong and Chinese stocks too (XPAR:AIR for Airbus, that kind of thing) Every answer comes back with the filing, the period and the date, so you can check it. How Claude helped: I build it with Claude Code every day. The filing parsers, the MCP tools and the tests come out of Claude Code sessions, and a second Claude pass reviews every change before it merges. I also wrote the tool descriptions with Claude as the reader. There are 120+ tools now, so each description is short (under 500 characters) and says which tool to call next, like search the filing first, then read the lines. With that many tools the descriptions are basically Claude's index. The other thing I had to fix was fiscal quarters. NVIDIA is already in fiscal 2027, Apple's year ends in September, and models mix those up all the time. Every number Equibles returns says which period it is and when that period ended. It's free to try: 100 requests a day, no card. Paid plans are $9.99 and $49.99 a month if you need more requests, option chains or real-time quotes. To connect it: Claude.ai or Desktop: Settings > Connectors > Browse connectors, search for Equibles. Or add a custom connector with https://mcp.equibles.com/mcp . You sign in with OAuth, no API key to paste. Claude Code: claude mcp add --transport http equibles https://mcp.equibles.com/mcp , then /mcp and authenticate. Some things to try once it's connected: "What did Microsoft say about AI capex in its last 10-Q? Quote it." "Which funds bought more Nvidia last quarter according to 13F filings?" "Show me congressional trades in defense stocks in the last 90 days." "What's the estimated short interest for GME before the next FINRA report?" One heads-up: the portfolio and watchlist tools can change your saved Equibles data, so leave tool confirmations on. So that's it, a free stock market data connector for Claude (and ChatGPT) that cites its sources. If you've built a connector with a lot of tools, I'm curious how you kept Claude picking the right one. Docs: https://equibles.com/docs/mcp
