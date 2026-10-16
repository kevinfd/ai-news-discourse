---
id: "0bf6aff3b9c95600"
title: "Hackers hijacked 1,900 GitHub accounts. Then they went after 30,000 repos."
url: "https://thenewstack.io/hackers-hijacked-1900-github-accounts-then-they-went-after-30000-repos"
link: "https://thenewstack.io/hackers-hijacked-1900-github-accounts-then-they-went-after-30000-repos"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T21:13:01Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Hackers accessed roughly 1,900 GitHub accounts, then used them to slip credential-stealing workflows into more than 30,000 repositories. The malicious GitHub Actions jobs targeted CI/CD secrets, cloud access keys, and AI provider API keys. GitGuardian tracked the GhostAction campaign as it intensified, with the biggest push on October 8 and 9, when the attackers reached repositories belonging to…"
tags: ["AI", "CI/CD", "Security"]
orgs: ["Amazon", "OpenAI", "Anthropic", "Google"]
topics: ["jobs & society", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 609
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Hackers hijacked 1,900 GitHub accounts. Then they went after 30,000 repos.

The New Stack · Amanda Caswell · 2026-10-15

Hackers hijacked 1,900 GitHub accounts. Then they went after 30,000 repos.
Hackers accessed roughly 1,900 GitHub accounts, then used them to slip credential-stealing workflows into more than 30,000 repositories. The malicious GitHub Actions jobs targeted CI/CD secrets, cloud access keys, and AI provider API keys. GitGuardian tracked the GhostAction campaign as it intensified, with the biggest push on October 8 and 9, when the attackers reached repositories belonging to about 3,000 users and organizations and tried to extract 3,174 secrets.
How the accounts were compromised
The tj-actions/changed-files compromise poisoned a shared Action used by thousands of repositories. GhostAction took a different route, using stolen developer credentials to modify workflows directly, with no vulnerability in GitHub Actions itself.
It’s unclear how the attackers obtained those credentials, but StepSecurity’s October 9 analysis points to personal access tokens pulled from credential dumps as the likely source, though the initial compromise hasn’t been confirmed.
With access to the repositories, the attackers could then add disguised workflows of standard security jobs, while using names like security-audit.yml or github_actions_security.yml. Since the files referenced secrets already used by legitimate builds, it gave the malicious jobs the chance to collect those credentials when they ran and send them to an attacker-controlled server.
Scanning the full Git history
The October variant went beyond the secrets explicitly referenced by workflows, using actions/checkout@v4 with fetch-depth: 0 to scan the working tree and Git history for AWS keys, GitHub and GitLab PATs, Google and Firebase keys, and API tokens from Anthropic, OpenAI and OpenRouter. Later versions captured surrounding lines to pair AWS key IDs with their corresponding secret access keys.
The harvested credentials were sent over HTTP to 193.32.204.199, including keys removed from the current codebase but still present in Git history.
GitHub blocked the malicious workflows
“This payload was deployed in multiple phases,” GitGuardian wrote, describing an initial push to about 160 previously targeted victims and, 20 minutes later, a far larger deployment into 28,000 new repositories across October 8 and 9.
“This payload was deployed in multiple phases.”
The total number of stolen credentials remains unknown. GitGuardian counted 3,174 secrets targeted for extraction and confirmed some exfiltration during the October campaign, but it didn’t determine how many distinct credentials reached the attackers.
During the August and September campaign, GitGuardian identified malicious workflows in 772 public repositories across 373 users and organizations. Of the 3,669 workflow runs recorded across 605 repositories, only 499 executed, with 336 completing successfully and exfiltrating 26 secrets from 13 repositories.
GitHub’s approval controls stopped most of the bad workflows, but attackers simply recycled 92 older ones left behind from earlier attacks, including infrastructure active since September 2025. To make matters worse, GitGuardian found that by October 5, only 16% of the affected repositories — 124 out of 772 — had been cleaned up.
To make matters worse, GitGuardian found that by October 5, only 16% of the affected repositories — 124 out of 772 — had been cleaned up.
Rotate exposed secrets and tokens
GitHub audit records and PAT activity can help identify which accounts modified .github/workflows/, while Actions run histories show which jobs executed and what secrets they could access. Any compromised account still holding write access needs to have its credentials revoked, even if the malicious workflow has already been removed.
Cloud keys, deployment credentials, registry tokens, and AI provider API keys potentially exposed during the attack also need to be revoked or rotated, including those deleted from the codebase months ago but still valid when the attackers scanned Git history.
Any compromised account still holding write access needs to have its credentials revoked, even if the malicious workflow has already been removed.
