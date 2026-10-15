---
id: "7882426230cc1900"
title: "I built an MCP server with Claude Code that lets Claude search and apply to jobs. Here’s how the build went (and what you can learn)"
url: "https://reddit.com/r/ClaudeAI/comments/1x60bmf/i_built_an_mcp_server_with_claude_code_that_lets"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T19:16:03Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Cojj25"]
language: "en"
summary: "In August I posted here about a job search platform I started building with Claude Code after Indeed laid off my wife. The most common question afterward was “cool, but can I do this from inside Claude?” So we built an MCP server, again mostly with Claude Code. It launched last Thursday and now has 450 users with 75 daily active. We're also seeing 83 interviews per 100 paid subscribers (who use…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "jobs & society", "products & launches", "search & media"]
content_source: "post"
word_count: 593
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x60bmf/i_built_an_mcp_server_with_claude_code_that_lets/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an MCP server with Claude Code that lets Claude search and apply to jobs. Here’s how the build went (and what you can learn)

Reddit · Cojj25 · 2026-10-14

In August I posted here about a job search platform I started building with Claude Code after Indeed laid off my wife. The most common question afterward was “cool, but can I do this from inside Claude?” So we built an MCP server, again mostly with Claude Code. It launched last Thursday and now has 450 users with 75 daily active. We're also seeing 83 interviews per 100 paid subscribers (who use autopilot) since our X announcement. It was a cool build I wanted to share. What it does You add the MCP and can instantly start searching the jobs database for free, drop a resume in to see matches, get custom tailored resumes, and have our back end submit on the employer’s own site once you approve. You can set a schedule to have your agent give you new matches every day (we pull in about 15K new jobs per day). How we built it entirely with Claude (and what you can mimic) Create one capability list for the web app and the MCP. Claude Code built a typed registry of everything a user can do on the Dreamwork website. Each MCP tool is generated from that registry, so a feature added to the web app shows up in the MCP. If a capability is deliberately kept out of the MCP, the code has to state why or it doesn’t compile. Start with a mega-PR series on day 1. I wrote a handoff doc describing the server I wanted, based on the web app. Claude Code split it into 12 PRs, one per capability: search, application prep, readiness checks, document handling, submissions, inbox, and so on. Each PR ran integration tests against our real Postgres. Create a hosted version with OAuth. Claude Code wrote the HTTP server and an OAuth 2.1 sign-in flow (dynamic client registration and PKCE), so you can add it as a connector in claude.ai without pasting an API key. Note for discoverability: you have to submit connectors to Anthropic for approval for them to show up in the connector library. This is a necessary prerequisite for that. Figure out what can and can't be done in the chat UI. We had to figure out how to send edited resumes to users that kept the formatting of the PDF. We ended up deciding on delivering a download link that lasts for 10min because the specialized formatting that we use to increase interview chances wouldn't pass through if the local agent rewrote it. Dogfood hard. We used the connector in Claude ourselves, applied to real jobs (and got interview offers with fake resumes...oops), wrote down 20 things that felt wrong, then 10, then 5, then 1, then o. When you get your first power users, ask them how things are going! After we thought we were down to bug zero, we got our first set of power users who then recommended another 30+ changes that we've since implemented. Because LLMs are probabilistic, you really need to continue testing and iterating and fixing over time. The number of scenarios power users will run into that you didn't think of is mind boggling. Free to try Job search, setting up notifications for new matches, resume editing and many other features are free via the MCP. You only have to start paying for the auto-submission feature - those tokens are expensive. To try it out ask your agent to add this: npx -y u/dreamworkhq/mcp or add https://mcp.dreamworkhq.com/mcp as a custom connector in claude.ai or Claude Desktop (Settings > Connectors) More info here: https://www.dreamworkhq.com/agents
