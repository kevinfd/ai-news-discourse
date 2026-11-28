---
id: "ce1e04b38d937de3"
title: "All 56 Official Grok Bot Examples Stop Just Before Approval: Scope Delegated Tasks to End with a Draft"
url: "https://note.com/unikoukokun/n/n26e8a2ac272a?hl=en"
link: "https://note.com/unikoukokun/n/n26e8a2ac272a?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-27T22:13:00Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["ユニコ Claudecodeセミナー"]
language: "en"
summary: "Hello! I'm Uniko 🦄!I read through all 56 official Grok Bot examples published by xAI.What surprised me most after reading them was that all 56 stop at the exact same point.📅 Uniko's free AI seminar (online),"
tags: []
orgs: ["xAI", "Salesforce"]
topics: ["jobs & society", "search & media", "business & funding"]
content_source: "fulltext"
word_count: 2145
paywalled: false
image: "/th?id=ONUT.MlV3EHYrR3F1zS-S8JbFew&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# All 56 Official Grok Bot Examples Stop Just Before Approval: Scope Delegated Tasks to End with a Draft

note · ユニコ Claudecodeセミナー · 2026-11-27

All 56 Official Grok Bot Examples Stop Just Before Approval: Scope Delegated Tasks to End with a Draft
Hello! I'm Uniko 🦄!
I read through all 56 official Grok Bot examples published by xAI.
What surprised me most after reading them was that all 56 stop at the exact same point.
📅 Uniko's free AI seminar (online), attended by over 160,000 people in total. I'll demonstrate live right before your eyes the steps to delegate work to ClaudeCode. Pick a date and book👇
https://uniko.creators099.com/p/zTkWc8P6Ej9F?ftid=1iHp8eqJKgG5&utm_source=note&utm_medium=organic&utm_content=CNT-02187_note_b
People often expect that "AI agents will handle everything all the way to the end."
But the official examples showed the exact opposite.
Sending, publishing, purchasing, paying.
Every single one is scoped to stop just one step short—at the "draft" stage—and wait for human confirmation.
I see this as the single most practical framework when handing off work to AI.
All Official Grok Bot Examples Are Scoped to "Stop at the Draft"
First, let's look at the facts.
On xAI's official example page, there are 56 cards lined up.
And on that official documentation example page, it says:
"Every example stops for your review."
In other words, every single example halts for your approval.
This is a seriously critical sentence.
When you actually look through the cards one by one, where they stop is clearly spelled out.
- Inbox Manager: Sorts emails, pulls out urgent and pending items, and drafts replies. Sending anything requires approval.
- Social Media Manager: Learns from past posts to create drafts, leaving the actual publishing on hold for a human.
- Security Questionnaire Filler: Fills in answers for security questionnaires, holding off on submission.
- Travel Coordinator: Checks flights and hotels against internal company rules, confirming details prior to booking.
- Subscription Cleaner: Identifies cancellation candidates from receipts and emails, canceling only those approved.
- Paid Media: Posts monthly budget reallocation proposals to Slack based on advertising data, adjusting only after approval.
When you lay them out side by side, it becomes obvious.
What AI handles is up to "researching, summarizing, and drafting."
The person is the one who pushes the button.
In the official docs, the single-task examples even share consistent phrasing at the end of their descriptions.
"Does not send," "does not publish," "does not change budgets," "does not make payments," "does not modify production settings," "does not use customer data."
Before describing what they can do, they state right at the end of the sentence where they stop.
I don't think they are stopped because AI lacks the capability.
Because the stopping point is predetermined, you can delegate the task with peace of mind.
The order of reasoning is the other way around.
A delegable job isn't one that AI can take all the way to completion; it's one where the stopping point is decided in advance.
Looking at the 56 Cases Across 9 Job Categories, Marketing and Sales Make Up Nearly Half
Next, let's look at how the 56 cases are divided across different types of work. 
Here is the official breakdown by category:
- General: 6 cases
- Sales: 10 cases
- Marketing: 13 cases
- Customer Success & Support: 4 cases
- Recruiting & People: 4 cases
- Operations & Finance: 5 cases
- Product: 5 cases
- Engineering: 5 cases
- Life & Leverage: 4 cases
With 13 cases in Marketing and 10 in Sales, these two categories account for over 40% of the total. 
Sales and messaging are areas where a "draft" easily becomes the final deliverable itself, after all. 
Email drafts, post drafts, proposal drafts. 
From the very start, they are easy to carve out into a format that wraps up once a human simply gives it a final read and hits send.
For example, Sales Outbound researches target companies overnight, scores them, and generates email and LinkedIn drafts in a review list. 
In the morning, the human's only job is to review the list and decide whether to send them. 
Sales Call Coach reviews Gong calls to provide timestamped coaching feedback and call scores. 
Deal Desk Coordinator compiles internal deal notes from past emails and calls, entering them into Salesforce only after they are approved.
What I found interesting here is that the Engineering use cases follow the exact same pattern. 
Bug Reproduction reproduces bugs in staging (a test environment) rather than production, logging reproduction steps, screenshots, and network request notes. 
The person is the one who fixes it. 
Across every category, the AI's role is strictly carved out to end at "gathering the materials."
Regardless of the category, the AI's station is always to "gather the materials and lay them out before a human."
Small Japanese Companies Should Start with Invoice Reconciliation and Inquiry Triage
So, where should small Japanese companies or individuals begin? 
My recommendation would be these two examples from the "Bot Teams" section of the official documentation:
- Month-end close: Invoice reconciliation → Expense reconciliation → Exception list for approval. Runs on the 1st of every month
- Support queue: Inquiry triage → Bug reproduction → Help center verification. Runs weekdays at 9:00 AM
The reason these two are so easy to start with is that their final output is an "exception list." 
Instead of having the AI handle everything, it surfaces only the discrepancies in front of a human. 
The human just has to look at the list and make the call.
In my own words, this is about conserving your extra lives.
Human decision-making capacity is finite.
Reviewing invoices one by one to confirm they are "correct" gradually chips away at your decision-making reserves.
However, with an exception list, you only need to make decisions on the few items that truly don't match.
Conversely, the tasks you should avoid at first are also very clear.
They are tasks where money is transferred or messages reach the other party the moment you click.
Payments, wire transfers, mass emails to clients, production configuration changes.
If you let AI make those final clicks right from the start, there's no going back when a mistake happens.
Therefore, the proper sequence is this:
First, hand over a task that "only creates a list."
Run it for a month, and once you confirm the list's contents are trustworthy, add the next task.
This way, even if it fails, the consequences stay solely in your hands.
The first task to hand over is not one that reaches the counterparty upon clicking, but one that compiles a list and delivers it to you.
📅 For those who find watching faster than reading: see the concepts from this article in action at Uniko's free AI seminar. Reserve your spot here 👇
https://uniko.creators099.com/p/zTkWc8P6Ej9F?ftid=1iHp8eqJKgG5&utm_source=note&utm_medium=organic&utm_content=CNT-02187_note_b
There Are Two Patterns for Where to Stop: "Leave a Draft" and "Deliver Only Exceptions"
Comparing the 56 use cases reveals that stopping points broadly fall into two patterns.
When carving out your own tasks, deciding which pattern to fit them into beforehand keeps you from getting lost.
The first pattern is "Leave a draft and wait."
Inbox Manager, Social Media Manager, and Security Questionnaire Filler are prime examples.
The AI creates something close to finished and places it in front of a human.
The human reads it, makes corrections, and hits submit.
This suits tasks whose final output is text, such as emails, posts, proposals, and questionnaire responses.
The second pattern is "Review everything and deliver only exceptions."
Vendor Portal Operator operates vendor admin panels without APIs every week and reports only the anomalies.
Month-end close also reconciles invoices against expenses and lists only the mismatches.
This is ideal for high-volume tasks where the vast majority of items are "no issue."
The trick to telling these two apart is simple.
- If a human reads the final output every time, use the "Leave a draft" pattern
- If 90% doesn't need to be read, use the "Deliver only exceptions" pattern
- If it fits neither, the task is still too large, so split it in half
Honestly, I think the third scenario is the most common.
Vague goals like "I want to delegate accounting" or "I want to delegate sales" are too massive as-is to determine where to stop.
Once you break them down to "just invoice reconciliation" or "just drafting the initial email," they suddenly fit neatly into a pattern.
That is why the names on all 56 cards are framed as small roles, like a specific "clerk" or "specialist."
When a task doesn't fit a pattern, it's not the AI's fault—you just haven't broken it down small enough yet.
Write the Stopping Point and "No invented metrics." in the Instructions
Now, let's talk about the actual instructions you give to the Bot.
Among the official use cases, there is one sentence that I felt was the most worth emulating.
It's this line written on the Paid Media Creative Strategist card:
"No invented metrics."
Do not fabricate numbers.
In ad analysis, if an AI fabricates plausible-looking numbers, all subsequent decisions will be completely derailed.
That is why I explicitly prohibit it right from the instructions.
This isn't limited to advertising work.
Whether summarizing sales or counting customer inquiries, AI tends to "plausibly" fill in missing gaps.
Have it write "Unknown" for numbers it doesn't know.
Just adding this single line to your instructions will increase the reliability of the draft.
These are the four things I always include in my instructions:
- What to look at (narrow down where it is allowed to read)
- What to produce (a draft, a list, or a memo)
- Where to stop (do not send, do not publish, do not pay)
- How to handle numbers (do not fabricate, state sources, write "unknown" if unsure)
👇 Prompts ready to copy and paste
あなたは私の仕事の下書き係です。
次の仕事を「下書きで止まる形」に切り出してください。
仕事：（ここに任せたい仕事を1行で書く）
出してほしいもの：
1. AIが担当する所（調べる・まとめる・下書きするまで）
2. 人が担当する所（送信・公開・購入・支払い・設定の変更）
3. AIが止まる場所を「〜しない」の語尾で3つ
4. 最後に人の前に出す物（下書き・一覧・例外だけの一覧のどれか）
守ること：
- 数字は作らない。出どころが無い数字は「不明」と書く
- 送信・公開・購入・支払いは一切しない
What you write at the end of your instructions is not "what it can do," but "where it stops" and "do not fabricate numbers."
The More Grok Bot Joins Meetings and Slack, the More Valuable It Becomes to Decide Where It Stops in Advance
Lastly, let's talk a bit about what's ahead.
It has been reported that Grok Bot 1.0 can now join meetings on Google Meet, Zoom, and Microsoft Teams to take notes and answer in the meeting chat (for Team, Enterprise, and Ultra plans).
You can also bring bots for team use into Slack and Teams.
The important point here is that the places where bots appear right before people's eyes are increasing.
A single word posted in a meeting chat reaches everyone present.
A post in Slack is read by the entire team.
In other words, the distance between "draft" and "production" is becoming increasingly short.
That is precisely why the value of deciding where to stop in advance increases.
During meetings, limit it to "take notes" and "answer when asked."
Sending finalized decisions outside the company is done by humans.
If you bring it in after setting those boundaries, you can reap only the benefits.
This approach is also widely read on X.
The original post written on the morning of the same day about having it monitor work for a week received approximately 450,000 impressions.
xAI is also calling on creators to share their use cases.
Right now, when everyone is searching for "what to delegate," the people who have also decided where to stop can move forward the most safely and swiftly.
The more bots appear in front of people, the more critical it becomes to decide in advance "where they stop."
Summary
All 56 official Grok Bot use cases stopped just short of approval.
AI handles drafts up to one step before sending, publishing, purchasing, or paying; humans push the button.
Work that can be delegated is work where the stopping point has been decided in advance.
Here are three things to do today.
- Choose one of your tasks and divide it into "AI parts" and "human parts" using the prompt above
- Start by handing over tasks that conclude with an "exception list," such as invoice reconciliation or inquiry sorting
- At the end of the bot's instruction sheet, write stopping points like "Do not send," as well as "Do not fabricate numbers"
🔧 Detailed steps here: Differences between X API, Grok API, and Grok Bot, plus instructions on delegating via Webhook 
https://egachan.net/posts/grok-bot-webhook/
🦄 If you are serious about learning AI agent development
Having read this far, you have already taken a half-step from the side of "those who merely know" to the side of "those who take action." 
At #UnikoSchool, 4,641 students run ClaudeCode every day, evolving toward the planning side of the AI era. 
Why not turn the knowledge you gained from this article into the power to take action starting today?
▶ Click here for details on Uniko School 
https://uniko.creators099.com/p/zTkWc8P6Ej9F?ftid=1iHp8eqJKgG5&utm_source=note&utm_medium=organic&utm_content=CNT-02187_note_b
#GrokBot #Grok #xAI #AIAgents #OperationalEfficiency #GenerativeAI #UnikoSchool
