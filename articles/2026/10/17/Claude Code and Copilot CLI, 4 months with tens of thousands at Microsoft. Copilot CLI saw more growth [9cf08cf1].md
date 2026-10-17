---
id: "9cf08cf1144a1e02"
title: "Claude Code and Copilot CLI, 4 months with tens of thousands at Microsoft. Copilot CLI saw more growth"
url: "https://note.com/allegro_ai/n/n7993867ff09b?hl=en"
link: "https://note.com/allegro_ai/n/n7993867ff09b?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-17T02:38:00Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Niaくん｜生成Ai・Axの実装支援"]
language: "en"
summary: "Discussions about AI coding tools are usually about \"new features released\" or \"winning benchmarks.\" It is rare to see actual numbers on what happens when you distribute them to tens of thousands of ..."
tags: []
orgs: ["Microsoft", "Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1819
paywalled: false
image: "http://www.bing.com/th?id=ONUT.4Jqd3173u3qC6o9BsDLhzw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Claude Code and Copilot CLI, 4 months with tens of thousands at Microsoft. Copilot CLI saw more growth

note · Niaくん｜生成Ai・Axの実装支援 · 2026-10-17

Claude Code and Copilot CLI, 4 months with tens of thousands at Microsoft. Copilot CLI saw more growth
Discussions about AI coding tools are usually about "new features released" or "winning benchmarks." It is rare to see actual numbers on what happens when you distribute them to tens of thousands of people at a company.
Now, we have those numbers. Three Microsoft researchers have compiled a paper on the records from January to April 2026, when they rolled out Claude Code and GitHub Copilot CLI to tens of thousands of engineers within the company. It was posted to arXiv on July 1st and covered by ITmedia on October 16th.
Since I already wrote the main points on X, here I will read the paper and organize what was measured, what can be concluded, and what cannot. I should state upfront that we have never compared the two tools under the same conditions. All numbers are cited from the paper.
3 key takeaways from Microsoft's internal adoption paper
- Merged pull requests (PRs) for those who adopted the tools were about 24% higher than the estimate for those who did not, and this did not drop off even after 4 months
- By tool, Copilot CLI was +24.9% and Claude Code was +11.4%. However, the users were Microsoft employees, and GitHub, which makes Copilot CLI, is a Microsoft subsidiary
- The factor most strongly associated with starting to try the tools was whether surrounding colleagues or managers were using them
What is the paper investigating? Usage logs and PR counts for tens of thousands of people
The title of the paper is "Adoption and Impact of Command-Line AI Coding Agents." As the subtitle suggests, it examines the rollout of Claude Code and GitHub Copilot CLI that Microsoft conducted at the beginning of 2026.
Both are tools where, when you issue instructions from the terminal, an AI agent executes commands semi-autonomously.
There are two main things they investigated. One is who tried them and who continued to use them. This part only covers Copilot CLI. The other is whether the PRs of those who used them increased. This part covers both tools.
The period is from January 5, 2026, to April 29, 2026. The effect is measured by the "number of merged PRs," counting only those merged within 28 days of creation.
As a premise, there is one other important point. At Microsoft, the IDE version of GitHub Copilot (code completion, chat, agent mode) was already available. The authors write that they want this result to be read not as the "effect of AI tools in general," but as the effect of adding command-line agents to a workplace that already has those tools.
Answer: Merged PRs were about 24% higher, and it did not drop off after 4 months
They compare the PRs of those who started using the tools with an "estimate of what would have happened if they hadn't," created from data of those who did not use them.
The result is about 24% more merged PRs. In the paper's figures, it is +24.0%, with a 95% confidence interval of +14.5% to +33.7%.
What is concerning is whether this is just a "novelty" effect that grows at first and then drops off. The paper looks at that too; it was +29.4% in February and +20.0% from March 1st to April 29th. The numbers look lower, but the authors state there is no statistically distinguishable decay.
The result also shows that the more days the tools are used, the more PRs there are. Comparing within the same individuals, weeks where the tools were used for 3 days saw a +15.0% increase, and weeks with 5 or more days saw a +50.1% increase. However, the authors themselves caution that weeks with more usage days might have involved lighter tasks, so it should be read as a correlation, not causation.
Copilot CLI saw more growth. But don't read this as "Claude Code losing"
This is probably the most eye-catching part. For those who used only one of the tools, the growth in PRs compared to weeks when the same person did not use the tool was as follows.
- Claude Code: +11.4% (+9.4% to +13.6%)
- Copilot CLI: +24.9% (+23.0% to +26.8%)
The paper states that the growth of Copilot CLI was approximately 2.2 times that of Claude Code.
Honestly, I thought it would be the other way around. The author also writes that it is surprising the order was reversed, given that Claude Code is often preferred in public comparisons.
Regarding the reasons, the author suggests two hypotheses. One is the possibility that the two tools were used for different types of tasks. The other is that Microsoft owns GitHub, the developer of Copilot CLI, while they are a customer for Claude Code. It is suggested that Copilot CLI may have been better tailored to internal workflows. Internal surveys apparently did not reveal the specific reasons.
The paper mentions another interesting fact. Shortly after the analysis period ended, there was an internal announcement for many engineers to terminate their Claude Code licenses after about a month and switch to Copilot CLI. The author cut the analysis before this point so that this transition would not skew the numbers. The reason for the termination is not written in the paper.
Therefore, I think it is too early to generalize from this that "Claude Code is less effective." Claude Code is also positive at +11.4%. Moreover, the comparison took place within Microsoft, which is on the side of the creators of Copilot CLI. "Within Microsoft, the week Copilot CLI was used saw greater PR growth." That is as far as one can go.
What influenced the start of the trial: bosses and colleagues
More interesting than the performance discussion was the analysis of how it spread. This part focuses only on Copilot CLI.
If people around you were using it, the odds of you trying it yourself increased.
- More than 25% of colleagues under the same "boss's boss" are using it: +216%
- More than 25% of people you frequently review with are using it: +54%
- Direct supervisor is using it: +82% (odds of continuing to use it: +22%)
These are all changes in odds, not meaning that the probability of trying it simply multiplied by that amount. The author also notes in the limitations that they could not rule out the possibility that similar people are simply gathered in the same team.
Another surprising finding was regarding those who were using the IDE version of Copilot. People who had used the IDE version for 60 days or more in the 13 weeks prior to introduction had +83% higher odds of trying Copilot CLI. However, the odds of continuing to use it were actually lower, at -12% to -15%. The author interprets this as the possibility that because they have a familiar tool to return to, the habit of using a new tool is less likely to take root.
Those who stuck with it were people who were already submitting PRs frequently. People who created two or more PRs per week before the introduction had +31% higher odds of continuing.
What we still don't know: quality and whether it's the same at your company
The figures so far have limitations that the author themselves points out.
- What was measured was the number of merged PRs, not the value itself. It is advantageous to submit small PRs frequently, and costs related to quality, such as increased complexity, may be overlooked.
- The scope is limited to one company, Microsoft, and only the period at the beginning of 2026. PRs were also only counted for Azure DevOps.
- The authors are Microsoft employees; Microsoft sells AI tools and owns GitHub.
In their conclusion, the authors write that the next big question is quality—specifically, whether the increased volume leads to better software. The internal survey received 609 responses, with comments such as "I complete more PRs per week" and "I can now tackle larger changes I wouldn't have attempted before."
The paper is an arXiv preprint; there is no mention of publication venue or peer review.
Incidentally, the acknowledgments state that the first draft and analysis code for this paper were created using GitHub Copilot (primarily Claude Opus 4.6–4.8). It is a somewhat interesting composition: a paper comparing two tools written using a Claude model running on GitHub Copilot.
If you are introducing this internally, what do you decide first?
What I took away from this paper was not "which tool is better," but rather how to implement and measure them. If we were to expand AI coding tools within our company, I would consider the following order:
1. Decide how to measure effectiveness first. Include not just the number of PRs, but also quality metrics. 2. Make it visible to others that people are using it. Have managers or team members start using it first. 3. Anticipate that those already accustomed to other AI tools might not stick with it even if they try it. 4. If comparing tools, compare weeks when the same person used them versus weeks they did not, within the context of your own work.
It is also important not to take Microsoft's numbers as your own company's expectations. Since the results are conditional—based on one company, one period, and the number of PRs—I think it is best to treat them merely as a reference point.
Summary: About 24% lasted for 4 months. However, don't forget "24% of what?"
- Microsoft measured the effectiveness of Claude Code and Copilot CLI among tens of thousands of internal employees over 4 months.
- The number of merged PRs for those who used the tools was about 24% higher than estimated and did not drop during the period.
- By tool, Copilot CLI showed more growth, but this is conditional on the Microsoft internal environment. Claude Code also showed positive results.
- The factor most strongly correlated with starting to try the tools was whether surrounding colleagues or managers were using them.
Honestly, I thought Claude Code would show more growth, so the tool-specific results were surprising. However, what remained with me more was the finding that whether the person next to you is using it has an impact. Before worrying about tool selection, it might be worth re-evaluating who in the company is using what and making that visible.
Consultation channel: I am accepting inquiries for brainstorming on how to measure effectiveness and promote adoption when introducing AI coding tools into your company. Please feel free to contact Allegro.
Reference links
- arXiv: Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI
- ITmedia NEWS: Microsoft analyzes the impact of introducing "Claude Code" and "Copilot CLI" on tens of thousands of internal engineers; how does productivity change?
