---
id: "143358e11c4ab1f2"
title: "My agent writes specs faster than I can read them, so I built decipher"
url: "https://reddit.com/r/ClaudeAI/comments/1ximls8/my_agent_writes_specs_faster_than_i_can_read_them"
link: "https://reddit.com/r/ClaudeAI/comments/1ximls8/my_agent_writes_specs_faster_than_i_can_read_them"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T15:09:40Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Creepy_Wave_6767"]
language: "en"
summary: "I've done spec-driven development with Claude Code for almost all of the past year. The agent writes a spec, I approve it, and the agent builds it. The specs run 1,500 to 2,600 words, and at some point I started approving them after a skim. I have ADHD, so a wall of agent prose loses me fast. decipher is a skill and output style that rewrites an agent-written spec, PR, report, or reply for a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Cursor"]
topics: ["agents & coding"]
content_source: "post"
word_count: 334
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1ximls8/my_agent_writes_specs_faster_than_i_can_read_them/"
score: null
comments: null
community: "r/ClaudeAI"
---

# My agent writes specs faster than I can read them, so I built decipher

Reddit · Creepy_Wave_6767 · 2026-10-29

I've done spec-driven development with Claude Code for almost all of the past year. The agent writes a spec, I approve it, and the agent builds it. The specs run 1,500 to 2,600 words, and at some point I started approving them after a skim. I have ADHD, so a wall of agent prose loses me fast. decipher is a skill and output style that rewrites an agent-written spec, PR, report, or reply for a reader who lost the thread. Every answer has the same shape: Gist: a few words that carry the whole idea Bottom line: what it does, where it stands, and what backs it Self-check: one question you answer to yourself Needs you: the decisions, blockers, and risks that are yours How it works: the steps, in order Make sure you know: a foundation concept to learn first, added only when your follow-ups show it's missing Before building this, I used to use i-have-adhd, caveman, etc, but none of them would give me what I needed. For example, gist is the super optimized way to hit me with the idea. How Claude Code helped: Every change started as a spec Claude Code wrote and I reviewed. Same workflow decipher is for. Claude Code ran decipher on real specs from my own projects to test each change. Made-up specs just wasted tokens. Some of Claude's ideas failed those tests. Two whole sections ("Held back" and "What changes") got cut, and so did a rule that was supposed to shorten replies. Claude ran caveman and i-have-adhd on the same spec as decipher so I could compare. Claude Code also rendered the demo video from HTML with Puppeteer. Install in Claude Code: /plugin marketplace add amirimi/decipher /plugin install decipher@decipher Then run /decipher:decipher specs/your-spec.md , or say "decipher" after a reply that lost you. It also works in Codex, OpenCode, and Cursor. https://github.com/amirimi/decipher I built it with Claude Code. It's free and MIT-licensed. Eager to hear your feedback and whether it's clicked with you :)
