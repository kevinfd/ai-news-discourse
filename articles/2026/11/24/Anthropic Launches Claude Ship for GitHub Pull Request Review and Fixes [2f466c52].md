---
id: "2f466c527067878c"
title: "Anthropic Launches Claude Ship for GitHub Pull Request Review and Fixes"
url: "https://marktechpost.com/2026/11/23/anthropic-claude-ship-pull-request-agents"
link: "https://marktechpost.com/2026/11/23/anthropic-claude-ship-pull-request-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T00:02:39Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Anthropic just released Claude Ship . Claude Ship is a set of Anthropic agents that takes GitHub pull requests from review to approval. It bundles 3 agents: Code Review , PR Steward and Claude Approvals . Your GitHub branch rules still decide what merges. \n\n TL;DR \n\n Size: 3 agents with a local /ship command. \n\n Runs on: Anthropic’s cloud for Code Review and PR Steward. /ship runs in the Claude…"
tags: ["Agentic AI", "AI Agents", "Editors Pick", "For Devs", "Harness", "New Releases", "Software Engineering", "Staff", "Tech News"]
orgs: ["Anthropic", "Microsoft", "Cursor", "Hugging Face"]
topics: ["agents & coding", "products & launches", "policy & regulation", "chips & infrastructure"]
content_source: "summary"
word_count: 995
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic Launches Claude Ship for GitHub Pull Request Review and Fixes

MarkTechPost · Asif Razzaq · 2026-11-24

Anthropic just released Claude Ship . Claude Ship is a set of Anthropic agents that takes GitHub pull requests from review to approval. It bundles 3 agents: Code Review , PR Steward and Claude Approvals . Your GitHub branch rules still decide what merges. 

 TL;DR 

 Size: 3 agents with a local /ship command. 

 Runs on: Anthropic’s cloud for Code Review and PR Steward. /ship runs in the Claude Code CLI locally. 

 Performance: Most Code Reviews finish in 6 to 10 minutes, about 3x faster than the research preview. 

 Best: Claude Code team merged PRs more than doubled from June to September (self-reported). 

 What is Claude Ship? 

 Per the Claude Ship docs , each agent owns 1 step: 

 Code Review looks for logic errors, security vulnerabilities and broken edge cases. Findings land as inline comments, ranked by severity. 

 PR Steward works on failing checks, merge conflicts and review comments. It pushes commits with its fixes. 

 Claude Approvals checks each PR against an approval policy your team writes. 

 Code Review is generally available . The other 2 are in public beta. 

 How does Claude Ship work on a pull request? 

 Code Review finds problems. PR Steward pushes fixes, and a fix can start another review. Claude Approvals then applies your policy. The merge follows your GitHub branch rules. 

 PR Steward is designed not to approve or merge. After each push, it comments on its changes and how to undo them. Developers steer it with @claude and stop it with @claude stop . 

 Claude Approvals reads a policy file at .claude/approvals.yml . Anthropic calls it a smarter CODEOWNERS file. A rule can require 2 people on billing code and 1 on test fixtures. Rules can read PR facts and classifier answers, but not CI results. 

 What does /ship do for developers? 

 Developers run /ship in Claude Code. It commits, pushes and opens the PR. Claude reviews it, then ‘watches’ feedback and failing checks. You merge yourself. 

 Requirements are Claude Code v2.1.330 or later, GitHub CLI 2.63 or later, and git 2.38 or later. A watch ends after 7 days, or on merge or close. /steward skips the review on an open PR. 

 When Claude acts alone, Claude Code blocks merge, approve, auto-merge and force-push commands. Still, a watch uses your own gh and git sign-ins. 

 Claude Ship benchmarks: what has Anthropic reported? 

 Anthropic has published no public benchmark. It shares internal results from its launch post and engineering blog : 

 Merged PRs on the Claude Code team more than doubled from June to September. 

 The share of reverted changes fell by more than 40% over the same period. 

 Internal PRs with substantive review comments rose from 16% to 54%. 

 PRs passing after 1 review-and-fix round rose from 65% to 78%. 

 Mean reviews needed to pass fell from 2.08 to 1.32. 

 These numbers are self-reported by Anthropic. No precision or recall is reported. 

&&&

 How does Claude Ship compare with Copilot, Bugbot and CodeRabbit? 

 Feature Claude Ship GitHub Copilot code review Cursor Bugbot CodeRabbit Reviews PRs Yes, Quick, Standard or Deep per repo Yes, Lite or Balanced effort Yes, on every PR update by default Yes Pushes fixes PR Steward commits to the PR branch (beta) Hands fixes to Copilot cloud agent as a new PR (public preview) Autofix via Cloud Agent, existing or new branch, 3 attempts per PR “Fix comments” on all plans; CI fixer and merge conflict resolution on Team and up Approval policy .claude/approvals.yml sets seats per path; Claude can approve (beta) Approving review if enabled (public preview) Not described; CI check can gate unresolved findings Not disclosed Git hosts GitHub (github.com; GHE Server for Code Review and Steward) GitHub.com; Azure DevOps (public preview) GitHub, GitLab, Bitbucket, Azure DevOps GitHub, GitHub Enterprise (full list not disclosed) Pricing Tokens via usage credits; no flat per-review price AI credits: about $0.05 to $1 per review (Lite), $0.25 to $5 (Balanced) Usage-based; rates not listed in docs $24, $48, $72 per developer per month, billed annually Plans Claude Team and Enterprise All paid Copilot plans Cursor individual and Teams plans Essentials, Team, Advanced, Enterprise Merge decision Your GitHub branch rules Your GitHub branch rules Your branch protection Not disclosed 

 Competitor figures come from each vendor’s own docs, checked November 23, 2026. 

 Claude Ship pricing, deployment and availability 

 Claude Ship is for Claude Team and Enterprise plans on GitHub. Owners enable agents per repository, ideally 1 at a time. 

 Billing runs on tokens through usage credits , separate from plan usage. Code Review costs scale with PR count, size, review level and frequency. Admins can set spend limits. PR Steward has none until an Owner sets one. 

 Approvals has no base charge. Classifier runs and the reviews a policy requests are billed, even in observe mode. Running /ship counts as regular Claude Code usage. 

 Eligible Enterprise organizations can claim at least $10,000 in Claude Ship credits by January 15, 2027. Credits expire 30 days after claiming, per the credit terms . 

 Key Takeaways 

 Claude Ship bundles 3 GitHub agents: Code Review, PR Steward and Claude Approvals. 

 Code Review is GA; PR Steward and Approvals are in public beta. 

 Approval rules live in .claude/approvals.yml ; start in observe mode. 

 Anthropic reports over 2x merged PRs and over 40% fewer reverts (self-reported). 

 Token billing, Team and Enterprise only, no ZDR, HIPAA or CMEK. 

 Check out the launch post , the Claude Ship docs and the /ship command docs . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Anthropic Launches Claude Ship for GitHub Pull Request Review and Fixes appeared first on MarkTechPost .
