---
id: "e23c2eae947fde9d"
title: "MiniMax Open-Sources MCode Stack: 15 Agent Skills Its Coding Team Uses Daily"
url: "https://marktechpost.com/2026/10/28/minimax-open-sources-mcode-stack-agent-skills"
link: "https://marktechpost.com/2026/10/28/minimax-open-sources-mcode-stack-agent-skills"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T17:20:29Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Michal Sutter"]
language: "en"
summary: "MiniMax has open-sourced MCode Stack , the workflows and agent skills its team uses to build MiniMax Code. The MiniMax MCode Stack agent skills went public on October 28, 2026 under the MIT license . It is not a prompt collection. Each piece is a SKILL.md skill or checklist that installs directly into MiniMax Code . For developers, it turns harness engineering habits into steps an agent can…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "New Releases", "Open Source", "Software Engineering", "Staff"]
orgs: ["Anthropic", "Google", "Hugging Face", "Cursor"]
topics: ["agents & coding", "models & research", "chips & infrastructure", "search & media"]
content_source: "summary"
word_count: 837
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# MiniMax Open-Sources MCode Stack: 15 Agent Skills Its Coding Team Uses Daily

MarkTechPost · Michal Sutter · 2026-10-28

MiniMax has open-sourced MCode Stack , the workflows and agent skills its team uses to build MiniMax Code. The MiniMax MCode Stack agent skills went public on October 28, 2026 under the MIT license . It is not a prompt collection. Each piece is a SKILL.md skill or checklist that installs directly into MiniMax Code . For developers, it turns harness engineering habits into steps an agent can actually run. 

 TL;DR 

 Size: 2 stacks, 17 skills (15 from Ronny, 2 from Jiachen), 5 checklists, 5 companion notes. 

 Runs on: Any machine running MiniMax Code (Node.js 22.19+) or Claude Code. No GPU. Skills are plain Markdown. 

 Performance: No benchmarks or eval results published. 

 Best: long-command-check , a 10-point audit for long shell commands and background tasks. 

 We just open-sourced MCode Stack: the actual workflows and skills the MiniMax Code team uses every day to build MiniMax Code. https://t.co/vREt7i8m2M — RonnyHe (@Ronny_MiniMax) October 28, 2026 

 What is MiniMax MCode Stack? 

 MCode Stack is an open-source repo of agent skills from MiniMax’s MiniMax Code team. MiniMax Code is the MiniMax’s open-source terminal coding agent, also MIT-licensed. The stack holds no MiniMax Code source code. It holds only workflows, skills and checklists. 

 The repo pairs with a column called MCode Engineering Notes . Each note explains one idea. The repo makes that idea runnable. Published notes cover subagents , tool context , compaction versus memory and long bash commands . A note on per-turn context tax is marked upcoming. 

 What skills are inside Ronny’s stack? 

 MiniMax’s stack ships 15 skills, grouped by moment in the working day: 

 Plan and split (3): subagent-split-check , engineering-small-prs , engineering-change-descriptions . 

 Context and tools (2): tool-budget-audit , context-tax-audit . 

 Long sessions and commands (3): long-session-check , handoff-doc , long-command-check . 

 Review (4): independent-review , engineering-code-review , engineering-review-comments , engineering-review-feedback . 

 Experiments and hotfixes (3): harness-experiment , trajectory-review , engineering-emergency-changes . 

 A few ideas stand out. independent-review gives the reviewer exactly 3 inputs: the diff, the requirement and test results. It deliberately withholds the author’s conversation. The reasoning: a reviewer inheriting the author’s context repeats the author’s blind spots. 

 subagent-split-check says to split work only when context is the measured problem. Splitting by team or question type is not a valid reason. 

 tool-budget-audit separates 2 costs: tool definitions and tool results. Tool search mainly cuts the first. Programmatic tool calling mainly cuts the second. 

 harness-experiment enforces 1 change per experiment. It tracks flipped tasks, requests per task, tokens, cache hit rate and wall-clock time. 

 The long-command checklist has 10 items. It asks whether moving a command to background re-runs the process. It also asks whether unread results survive compaction. 

 The 6 engineering-* skills are adapted from Google Engineering Practices . That material stays under CC-BY 3.0, per the stack’s NOTICE . 

&&

 How do you install MCode Stack? 

 There are 3 paths, per the README : 

 One skill: clone the repo and copy a skill folder into ~/.agents/skills/ . 

 Whole stack as a local plugin: copy stacks/ronny into MiniMax Code’s local plugin directory. 

 Marketplace: in MiniMax Code desktop, add the MiniMax-AI/mcode-stack marketplace. This option is rolling out gradually. 

 The same catalog works in Claude Code with /plugin marketplace add MiniMax-AI/mcode-stack . MiniMax Code also reads ~/.claude/skills/ and ~/.codex/skills/ . The skills use the common SKILL.md format, so most work in other agents that support skills. 

 How does MCode Stack compare with other skill packs? 

 Feature MiniMax MCode Stack anthropics/skills obra/superpowers Publisher MiniMax Code team Anthropic Jesse Vincent (obra), Prime Radiant License MIT; engineering-* skills CC-BY 3.0 Apache 2.0 for many skills; document skills source-available MIT Skill count 17 (15 + 2) Not disclosed 15 listed in README Focus Harness engineering, review, context budgets, long sessions Creative, development, enterprise, documents Brainstorming, planning, TDD, subagent-driven development, debugging Agents named MiniMax Code, Claude Code Claude Code, Claude.ai, Claude API 16 harnesses, incl. Claude Code, Codex, Cursor, Gemini CLI Claude Code install /plugin marketplace add MiniMax-AI/mcode-stack /plugin marketplace add anthropics/skills /plugin install superpowers@claude-plugins-official Published evals Not disclosed Not disclosed Not disclosed 

 MCode Stack is narrower than both. It targets people who design agent harnesses, not only people who use agents. Superpowers covers far more harnesses today. 

 Key Takeaways 

 MiniMax open-sourced 17 SKILL.md skills and 5 checklists under MIT. 

 Skills pair with MCode Engineering Notes, turning essays into runnable checks. 

 independent-review feeds a reviewer only the diff, requirement and test results. 

 Installs into MiniMax Code or Claude Code via a plugin marketplace. 

 No published evals yet, so treat it as a playbook, not proof. 

 Check out the GitHub repo and MiniMax Code . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post MiniMax Open-Sources MCode Stack: 15 Agent Skills Its Coding Team Uses Daily appeared first on MarkTechPost .
