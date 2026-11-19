---
id: "2c972f8dacfebbe0"
title: "Your AI Assistant Could Work For Someone Else"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/19/your-ai-assistant-could-work-for-someone-else"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/19/your-ai-assistant-could-work-for-someone-else"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-19T12:45:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Yaron Kassner, Forbes Councils Member"]
language: "en"
summary: "Many of us now run two efforts: one to protect our AI, and one to defend against AI."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Google", "Microsoft"]
topics: ["agents & coding", "jobs & society"]
content_source: "fulltext"
word_count: 800
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/69728caba7c3f82e7a6dd0c0/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Your AI Assistant Could Work For Someone Else

Forbes · Yaron Kassner, Forbes Councils Member · 2026-11-19

Yaron Kassner, Co-founder and CTO, Silverfort.
Last year, attackers went after about 30 organizations using an AI coding assistant. They jailbroke it, told it that it worked for a security firm running defensive tests, and broke the attack into small jobs that each looked innocent on its own. The assistant did them.
What interests me is how they caught it. The attacker was using his own AI account. That meant the company running the assistant could look across all of his sessions at once and see what those small jobs added up to. One party had the whole picture.
That may not be the case next time. The assistants our teams use every day make it easier to do the same thing.
Next Time, The Attacker Will Use Ours
In many of these cases, the attacker brought his own AI to the job, and that is what gave him away. See the Google Threat Intelligence report for another set of examples. The account, billing and session history often sit with a provider who can eventually piece the story together.
There is a simpler option available. An attacker who lands on a single machine, or who picks up a working set of credentials, is often standing right next to an assistant that is already installed, already trusted inside the network, and already being paid for by the victim. How convenient.
Charlie Bell at Microsoft gave this a good name a year ago when he wrote about AI agents becoming double agents: an assistant doing exactly what it was built to do, for the wrong person.
The Everyday Assistants Have The Most Reach
The assistants that matter most here are the ordinary ones. Coding and productivity assistants have broad access because broad access is what makes them worth having. They act as the person who started them. They run commands, open files, and reach source code, cloud accounts and mail. That is the whole point of them, and teams are right to use them.
It also means that whoever gives one instructions holds most of that person’s access. Right now, an assistant takes its instructions from whoever is at the keyboard. It has no way of knowing whether that is still the person it was set up for, and it was never designed to ask. The approval prompt is there to help the user think twice. It was not built to stop someone who should not be there.
Each Step Looks Like Somebody’s Job
Break an attack into small enough pieces and no single piece looks like an attack. Listing the accounts in a directory is an access review. Reading through a repository is code review. Checking which machines answer on the network is inventory work. Every one of those has a reason to be happening on a Tuesday afternoon.
Now hand the pieces to different assistants, one job each. Every assistant sees only the task in front of it, and every task is fine. The attack only exists as an attack in the mind of the person who split it up, or in the context window of the attacker’s own agent back home.
Where The Control Belongs
The moment that matters is the tool call. An assistant holds its access whatever it is asked to do, and the prompt only decides which of that access gets used. The place to put the attention is where the assistant reaches out to another system.
Today those calls go out carrying the standing permissions of the person the assistant was set up for, which means the whole of that person’s reach is available for any request that sounds reasonable. The alternative is to give the assistant an identity of its own, scoped to the work it is actually doing, and to require actions that matter to be approved by something the assistant cannot grant itself. An assistant can be talked into asking for anything. It cannot be talked into holding a credential it was never given.
Human approval deserves the same thought. A prompt that appears on the machine the attacker is already sitting on is an approval he grants himself. To count for anything, it has to arrive somewhere else, on a separate device, with the person granting it proving who they are.
There is a habit of mind worth changing too. Many of us now run two efforts: one to protect our AI, and one to defend against AI. We treat them as separate problems, with separate thinking and separate owners. In a coding assistant, they are the same problem, on the same machine, under the same login. As long as we approach it as two, we will keep designing controls for half of it.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
