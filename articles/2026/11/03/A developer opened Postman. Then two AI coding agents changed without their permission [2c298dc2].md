---
id: "2c298dc2806747de"
title: "A developer opened Postman. Then two AI coding agents changed without their permission."
url: "https://thenewstack.io/postman-plugin-coding-agents"
link: "https://thenewstack.io/postman-plugin-coding-agents"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T23:17:04Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "A developer says Postman’s desktop app installed plugins into Claude Code and OpenAI Codex without their permission. The app also tried to approve its own startup hook, which tells Codex to use Postman’s tools for API development tasks. \n\n The developer, known as “indicava” on GitHub, reported the issue on October 25 after Codex began showing authentication errors and repeatedly loading Postman…"
tags: ["AI Agents", "Developer tools", "Security"]
orgs: ["Anthropic", "OpenAI"]
topics: ["agents & coding", "business & funding", "products & launches"]
content_source: "fulltext"
word_count: 790
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# A developer opened Postman. Then two AI coding agents changed without their permission.

The New Stack · Amanda Caswell · 2026-11-03

A developer opened Postman. Then two AI coding agents changed without their permission.
A developer says Postman’s desktop app installed plugins into Claude Code and OpenAI Codex without their permission. The app also tried to approve its own startup hook, which tells Codex to use Postman’s tools for API development tasks.
The developer, known as “indicava” on GitHub, reported the issue on October 25 after Codex began showing authentication errors and repeatedly loading Postman skills without being asked.
It’s raised concerns about how easily third-party applications can change how AI coding agents work, especially when those changes happen without a clear opt-in.
Plugins installed without permission
According to the report, opening Postman desktop version 12.33.4 on macOS triggered an installation process affecting both Claude Code and Codex.
Postman’s application logs, included in the GitHub issue, show an installation event on October 24 marked auto-existing-upgrade, with results indicating that plugins for both coding agents had been installed.
The developer also found changes to Codex’s user-level configuration file, ~/.codex/config.toml, including an enabled Postman plugin, a new plugin marketplace, and a trusted session-start hook.
The report also found a Postman CLI executable on the machine, with timestamps matching the installation.
Claude Code’s configuration similarly showed an installed Postman plugin. The report also found a Postman CLI executable on the machine, with timestamps matching the installation.
The developer says they had not explicitly authorized these changes. The report documents one macOS installation, and the behavior has not been independently reproduced across other systems.
The self-approving startup hook
But perhaps even more interesting is how Postman gets Codex to trust its plugin in the first place. According to Postman’s own documentation, its installer can automatically approve a session-start hook on the user’s behalf.
According to Postman’s own documentation, its installer can automatically approve a session-start hook on the user’s behalf.
Developers who install the plugin directly through Codex, however, must review and approve the hook themselves. The installer’s source code shows exactly what happens.
Postman checks whether Codex already trusts the hook. If it doesn’t, the installer uses config/batchWrite to add the hook’s trusted hash to Codex’s configuration. It checks that the hook hasn’t changed before approving it, and if approval fails or can’t be confirmed, it logs a message telling the developer to review the hook in Codex.
Session-start hooks can give coding agents instructions automatically, even when the developer hasn’t asked for them. Postman’s startup instructions tell Codex to load the postman:api-engineer skill before handling most API development tasks.
Codex is still supposed to follow the developer’s instructions first. But for many API tasks, it’s also being told to use Postman’s tools by default, whether the developer asked for them or not.
That might be useful for developers who chose to install the plugin. The concern here is that Postman’s desktop app reportedly added those instructions to an existing coding environment without the developer’s permission.
Developers raise security concerns
The findings have drawn criticism from developers on GitHub and X. Security researcher Frank Denis called the integrations “junk” on X and pointed out that Postman’s installer attempts to trust its own startup hook.
Siddharth Garimella went further, claiming that Postman’s hooks intercept API data and send it back to the company. However, the GitHub report provides no evidence that Postman collected or transmitted API data. It documents changes to agent settings and a remote MCP connection, not data theft.
The developer also found that Postman had configured a connection to its remote MCP server at https://mcp.postman.com/mcp, but Codex repeatedly failed to authenticate.
The criticism has also spread to GitHub, where one commenter calls the behavior “unacceptable, even creating risk in corporate environment.” Another urges Postman to be transparent and ask for permission.
Who controls the agent
The developer wants Postman to stop installing plugins for existing users without their permission and leave hook approval up to Codex. They also want a way to fully undo the changes.
Postman provides an uninstall command, but the developer says that isn’t enough. Removing the integration should also clear any changes to agent settings, trusted hooks, MCP connections, and installed CLI tools.
For now, developers can check their Claude Code and Codex settings for unfamiliar plugins, hooks, or MCP connections.
Postman’s installer can approve its own Codex hook without the usual manual review.
The complaint comes as developers are pushing for more control over their coding agents. Postman’s installer can approve its own Codex hook without the usual manual review. What remains unanswered is why an existing desktop installation reportedly triggered that process without the user’s permission.
The New Stack reached out to Postman to ask about the automatic installations, hook approvals, and user consent. The company had not responded by the time of publication.
Learning Path
