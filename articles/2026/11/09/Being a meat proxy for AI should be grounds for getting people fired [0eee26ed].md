---
id: "0eee26edbd7c1f6c"
title: "Being a meat proxy for AI should be grounds for getting people fired"
url: "https://swiftrocks.com/being-a-meat-proxy-for-ai-should-be-grounds-for-getting-people-fired"
link: "https://swiftrocks.com/being-a-meat-proxy-for-ai-should-be-grounds-for-getting-people-fired"
source: "Bruno Rocha"
domain: "swiftrocks.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T06:55:38Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["rockbruno"]
language: "en"
summary: "Being a meat proxy for AI should be grounds for getting people fired\nI've always aimed to keep the content of this blog neutral, but the issue I'll cover today is genuinely pissing me off. I apologize in advance for the more aggressive tone that this post will have because I think it's necessary in this to get the point across.\nWhen someone is assigned a task, be it to review a PR, work on a…"
tags: []
orgs: []
topics: ["agents & coding", "jobs & society", "business & funding"]
content_source: "fulltext"
word_count: 958
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50422001"
score: 42
comments: 36
community: "Hacker News"
---

# Being a meat proxy for AI should be grounds for getting people fired

Bruno Rocha · rockbruno · 2026-11-09

Being a meat proxy for AI should be grounds for getting people fired
I've always aimed to keep the content of this blog neutral, but the issue I'll cover today is genuinely pissing me off. I apologize in advance for the more aggressive tone that this post will have because I think it's necessary in this to get the point across.
When someone is assigned a task, be it to review a PR, work on a reasonably complex coding task, or even just asked a simple question, and all they do is prompt the agent "do X" and copy-paste the results back to you, with zero guidance or validation on behalf of the human (meaning it was 100% handled by the agent), and sometimes not even disclosing that this was the case, this should in my opinion be considered as an attempt from the dev to scam the company. It should result in the dev receiving a warning and even the threat of potential termination of employment in more serious cases and if the dev fails to comply.
I'm not talking about the usual AI-assisted workflow which is commonplace nowadays where the human guides the agent, corrects it, reviews what comes out of it and opens PRs based on something that has been properly validated and cleaned up for other humans to review. I'm talking about the specific scenario where the human was simply a meat proxy between you and whatever agent they used, making you feel that the person added no value and you should've just launched an agent yourself and skipped them entirely. They might have even potentially made things worse for you by doing so, and in more egregious cases even intentionally attempted to hide this face and/or use this as a way to strip themselves of any responsibility regarding the code they write and merge (e.g. "This code broke master and took down production? It was opened and merged under my user? No, you see, it's not my problem because it was the AI who did this, not me! :)").
This behavior is becoming increasingly prevalent in the software engineering industry and it's ruining software jobs. IMO this behavior should be punished because devs who do this are:
- Wasting your time, because if all they do is proxy their work to an agent, you might as well skip the person and do that yourself
- Forcing you to do their work for them, because you now have to not only review and validate agentic output that they did not, but also potentially have to be one dealing with the consequences of any nonsense code that they may have managed to merge when you were not paying attention
- Wasting the company's time and resources, as this behavior is basically a convoluted way of stating that they are 1) getting paid a salary to do nothing essentially, 2) harming the company's products, and 3) wasting the time of anyone having to deal with them
I always saw the software engineering field as being comprised of two groups of people: people who are devs because they are passionate about building software, and people who don't actually enjoy software but joined the field because it's a job that pays well. The latter being something that I find to be a perfectly fine thing to do as long as, you know, you actually do your job. Pre-AI, although sometimes I've found people in this group to not have been doing a particularly impressive job, they were still doing it nonetheless. So things were fine then.
But now that AI is widespread, I've been bumping into many folks who basically weaponized AI to make it seem like to their managers they are being extremely productive by opening hundreds of PRs with very complex descriptions and bold claims of having fixed major issues and/or greatly improved systems, when in reality a deeper look reveals that this "work" is actually just a bunch of unreviewed vibe-coded nonsense that not only doesn't fix or improves anything at all, but also actively harms whatever products they are "working" with and massively complicates the work of the devs who have to deal with the consequences of said garbage code and actually care about building good products and using AI responsibly.
This is getting so insane that I've even had cases where I would DM someone on Slack and notice right away that I'm talking to an AI. Not in the sense that they've set up an agent to handle their messages for them (wouldn't be surprised if people start doing this though), but that they are copying my question to an agent and pasting back the response (without disclosure, so making it seem that they wrote it themselves). WTF?
When chatting about this problem with colleagues, some of them suggested that the answer might be to throw AI back at the person (so if you get a barrage of unreviewed AI-generated review comments on your PR, throw another unreviewed AI-generated barrage of AI responses back at the person). But I feel that this just makes everything worse. It may get the PR itself out of your hands, but the code will suffer as a result and you'd still have to end up dealing with the consequences of that.
I don't understand why someone who doesn't like their job would try so hard to come up with ways to not do it that they would be fine with messing up their colleagues' work in order to achieve it. Nobody is forcing anyone to work in tech. If someone doesn't like it, they can just quit and do something they actually enjoy. It's what I would've done at least if I was in their situation.
