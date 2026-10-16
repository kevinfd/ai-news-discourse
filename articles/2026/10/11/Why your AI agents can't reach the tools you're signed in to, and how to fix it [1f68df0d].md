---
id: "1f68df0d150585c4"
title: "Why your AI agents can't reach the tools you're signed in to, and how to fix it"
url: "https://read.aindeev.com/p/why-your-ai-agents-cant-reach-the"
link: "https://read.aindeev.com/p/why-your-ai-agents-cant-reach-the"
source: "The Leveraged Mind"
domain: "read.aindeev.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-11T01:03:41Z"
published_date: "2026-10-11"
collected_at: "2026-10-13T20:17:27Z"
authors: ["alexeyindeev"]
language: "en"
summary: "I usually have a lot of coding agents running on my Mac at once. Most don't need a browser. When one does, it tends to interrupt whatever I'm doing.\nAn agent would bring tabs to the front while I was typing, or Chrome would ask \"Allow remote debugging?\" Or the agent would use its own headless browser and have none of my logins. It couldn't open our admin console or a staging environment.…"
tags: []
orgs: ["Google", "Anthropic", "Cursor"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1132
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50038743"
score: 10
comments: 0
community: "Hacker News"
---

# Why your AI agents can't reach the tools you're signed in to, and how to fix it

The Leveraged Mind · alexeyindeev · 2026-10-11

I usually have a lot of coding agents running on my Mac at once. Most don't need a browser. When one does, it tends to interrupt whatever I'm doing.
An agent would bring tabs to the front while I was typing, or Chrome would ask "Allow remote debugging?" Or the agent would use its own headless browser and have none of my logins. It couldn't open our admin console or a staging environment. Anything behind Google SSO was out, which ruled out most of what I needed it to check.
I now use Chrome Relay to let Claude Code, Codex, Cursor and Paseo drive background tabs in my everyday Chrome, with my real logins, from the command line. Today I'm open-sourcing it.
What I needed
I had four requirements for an agent's browser.
- It had to work through a CLI. Every agent I use can run shell commands; some can't use a browser extension or an MCP server.
- It had to use my actual Chrome profiles, already signed in. I didn't want to copy a profile or log into a fresh browser again.
- It had to stay in the background. I'm working in the same Chrome, so a window coming forward or a dialog is an interruption. Focus has to stay where I put it.
- It had to be fast. If a page check takes 20 seconds, agents stop doing them.
What I tried
The obvious options each failed at least one requirement.
Most browser tools attach to Chrome's debugging port. That gets you the "Allow remote debugging?" prompt.
I expected copying my Chrome profile into a separate browser to work. Google sessions are bound to the device, though. Copy the cookies to another browser and Google treats them as invalid. You're signed out of the apps you wanted to use.
I also tried a Playwright extension and separate signed-in browsers. Each covered some of what I needed, but none met all four requirements.
Codex's and Claude's own Chrome extensions use a small extension with Chrome's chrome.debugger API. That approach worked. Their extensions only talk to their own app, so I wanted to expose the same thing as a standard DevTools endpoint that any CLI agent could use.
How it works
The connection looks like this.
agent-browser (CLI) ──ws──▶ relay (127.0.0.1:9333) ──ws──▶ Chrome Relay extension ──chrome.debugger──▶ agent tab
The extension is MV3 and loads once in each Chrome profile. It opens every agent tab as an inactive tab in a collapsed "Agents" tab group and runs DevTools commands through chrome.debugger. Without a debugging port, Chrome doesn't ask "Allow remote debugging?"
The relay is a small local service. It gives each agent its own DevTools endpoint and drops any command that would raise or focus the browser. An agent only sees the tabs it opened, so I can run many agents at once without them stepping on each other.
I use the chrome-relay CLI for setup and to get a profile's connection URL. It also runs diagnostics and reads the audit trail.
The agent uses Vercel's agent-browser CLI, pointed at the relay.
agent-browser --cdp "$(chrome-relay url you@company.com)" open https://app.example.com/
agent-browser snapshot -i     # the page's buttons, links and fields, each with a ref
agent-browser click @e5
agent-browser close
The email picks the Chrome profile. I use my work profile for most things and an admin profile when an agent needs to check something in a console.
Popups and "open in new tab" links become hidden tabs owned by the same agent. OAuth popups can still report back to the page that opened them.
Google sign-in needs some handling too. When a site bounces through Google and the right account is already signed in, the extension clicks the account and Continue itself. Agents never type credentials. If the hop reaches a password, passkey or 2-step screen, it stops. The agent tells me to sign in in my own window.
1Password causes a less obvious problem. Chrome drops an extension's debugger from any page containing another extension's frame, including 1Password's menu on a login form. The relay waits while the extension re-attaches. The agent's commands take a little longer.
Speed mattered most to me. A command takes about 0.15 s; opening a page takes about 0.6 s. My Chrome is already open, so there's no browser to launch.
Access and its limits
I'm giving agents access to a browser where I'm signed in to everything. I want to know what can connect and what the agents did once they got in.
Every connection has to pass two checks. It needs the per-machine secret generated by setup, stored readable only by you. The connecting process also has to be Claude Code, Codex, Cursor or Paseo. The relay looks up the process and checks the markers those apps set on their child processes. Web pages are refused even if they have the secret.
Only your own copy of the extension can connect as the extension. The relay checks its origin and confirms that the connecting process is Chrome.
These checks keep other local tools and web pages out, and guard against accidents. Malware already running as you could read the secret and fake the markers, so this doesn't provide a boundary against it.
Chrome still shows its "started debugging this browser" bar while agents work, the same as with Codex's extension.
Every agent action goes into an audit log. It records pages and clicks, along with keys and the agent's own scripts. Screenshots and sign-in clicks are logged too. Typed text is stored only as a length; what an agent types never ends up in a log file. When an agent says it checked something, I can look up exactly what it did.
Try it
It's macOS and Chrome only for now. You need Node.js 20+ and agent-browser (npm i -g agent-browser). Setup takes about two minutes.
git clone https://github.com/aindeev/agent-chrome-relay
cd agent-chrome-relay
bin/chrome-relay setup
In each Chrome profile your agents should use, open chrome://extensions, turn on Developer mode, click "Load unpacked" and pick the extension folder. Run chrome-relay doctor to check everything. Or paste the setup prompt from the site into your agent and let it walk you through all of this.
Setup also links a skill into Claude Code, so every repo knows how to use it. For Codex and Cursor, add one line to your global agent instructions pointing at the same skill file.
Try it on a staging page after a deploy, or have your agent check an admin setting. A dashboard behind SSO works as a starting point too. Ask the agent to use your Chrome and keep working while it checks. Hit reply with what you pointed it at, or what broke.
The repo is MIT: https://github.com/aindeev/agent-chrome-relay. The site is https://agent-chrome-relay.aindeev.com. I'm on X at @AlexeyIndeev too.
Alexey
