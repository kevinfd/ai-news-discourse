---
id: "d95302559e6329a4"
title: "Claude is performing 3.8x poorer compared to last week based on my claude code token analysis"
url: "https://reddit.com/r/ClaudeAI/comments/1xguw7r/claude_is_performing_38x_poorer_compared_to_last"
link: "https://reddit.com/r/ClaudeAI/comments/1xguw7r/claude_is_performing_38x_poorer_compared_to_last"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T15:01:48Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Wise_Carpenter_3132"]
language: "en"
summary: "What's happening: Claude models (e.g., Opus 5.5) are consuming more tokens per task and the quality has considerably degraded. Weekly usage is running out at 3.8x rate due to degraded performance. Quota per week seems the same as last week. Suggested workaround: Ask your main session to stop using subagents (you can also set this under settings). Start new sessions after hitting 300-400K…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding", "products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 529
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xguw7r/claude_is_performing_38x_poorer_compared_to_last/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude is performing 3.8x poorer compared to last week based on my claude code token analysis

Reddit · Wise_Carpenter_3132 · 2026-10-27

What's happening: Claude models (e.g., Opus 5.5) are consuming more tokens per task and the quality has considerably degraded. Weekly usage is running out at 3.8x rate due to degraded performance. Quota per week seems the same as last week. Suggested workaround: Ask your main session to stop using subagents (you can also set this under settings). Start new sessions after hitting 300-400K context. Current conclusion: Either of 2 things may be happening: 1) The token load for Anthropic isn't necessarily reducing - so its a true bug and they should fix it . 2) Given their compute infra, they are unable to keep a lot of users on large/frontier models (given large clusters required to hold the parameters), so they have softly downgraded some users (e.g., retail) to smaller models labelled as Opus 5.5. Given Anthropic's load is ~70-80% enterprise, this could be plausible. Will be great to hear your views in the comments. Model/tasks: Opus 5.5 (med/high) - tasks have been similar if not completely same over the observation period. [Original post] 3 issues came to light: Each sub agent is re-reading more from the parent agent Each subagent is taking 2x steps to finish the job Claude is spinning more sub agents per task (this could subjective per task type) Hypothesis: Essentially Claude has done some agent orchestration change which is not working out. Or the model quality has dropped significantly leading to more steps per solution. My solution: Ask your main session to stop using subagents. Start new session after 300-400K context. Would be great if someone can share similar experience/other reasoning why the tokens are depleting so quickly this week. Hope Anthropic offer a weekly reset to compensate for whatever might be the issue. [Edit #1]: Subagent performance might be the effect rather than the cause. Poor model performance on open ended/big tasks is the issue (I am running Opus 5.5 - on Med/High). Killing subagents has brought the token spend under check, but the main model is only good for closed ended tasks/hand holding. [Edit #2]: Per my tokens from this week vs last, the apparent weekly limits haven't shifted much ($2235 last week vs $2043 this week), so core metric we should be after should be tokens spent per task - directly linked to model performance. At least for my work, the type of work hasn't changed - so the argument that the model performance for Opus 5.5 has dropped significantly holds true. <Analysis details/image added in the comments section> [Edit #3]: Reached out to the support bot and apparently it even went for a human review - yet no resolution was provided. Amazing to see what paying ~$200/month (Max 20x) for almost a year gets you these days and the lack of price/product transparency is mind boggling. My trust from model/harness version control/releases is evading. [Edit #4]: Subagent trace analysis indicates: 1) Main agent is handing off most work to subagents 2) Subagents are lost/keep on working even after completing the required task when the context per subagent is high (>350K tokens). 3) Overlap between agents launched is high - leading to re-reading the same files - over and over again.
