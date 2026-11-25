---
id: "6ce5f00e2069e532"
title: "Practical \"Proper Noun Checking\" Techniques to Avoid Sending Generative AI Drafts As-Is"
url: "https://note.com/genai_work_lab/n/n25f83073aeb9?hl=en"
link: "https://note.com/genai_work_lab/n/n25f83073aeb9?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-24T02:01:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["生成Ai仕事術ラボ"]
language: "en"
summary: "Have you ever experienced something like this? You had generative AI draft an email or procedure manual, only to find non-existent meeting or team names mixed in. The project name was correct, but ..."
tags: []
orgs: []
topics: []
content_source: "fulltext"
word_count: 1158
paywalled: false
image: "http://www.bing.com/th?id=ONUT.wCFGcrMKg8foJhCckIctoA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Practical "Proper Noun Checking" Techniques to Avoid Sending Generative AI Drafts As-Is

note · 生成Ai仕事術ラボ · 2026-11-24

Practical "Proper Noun Checking" Techniques to Avoid Sending Generative AI Drafts As-Is
Have you ever experienced something like this?
- You had generative AI draft an email or procedure manual, only to find non-existent meeting or team names mixed in.
- The project name was correct, but release dates or assignees were slightly off, taking extra time to fix.
- The writing sounded plausible enough that you overlooked errors, only for a colleague to point them out right before sending.
- When you asked for revisions, other parts were rewritten as well, leaving you confused about what still needed review.
In fact, the reason generative AI drafts become difficult to use might not be writing quality, but rather that "facts that need verification," such as proper nouns and figures, get buried in the text.
Generative AI excels at smoothing out the flow of writing. On the other hand, it does not accurately know internal project names, scopes of responsibility, dates, or system names. If you let these slide assuming they are "probably correct," the more polished the text is, the harder it becomes to notice errors.
The key, before and after asking generative AI for a draft, is not to edit the text right away, but to list out what needs to be verified first.
By reading this article, you will be able to extract proper nouns that require verification from AI-generated drafts of emails, meeting minutes, procedure manuals, and explanatory materials, allowing you to check them in a short amount of time. You can try it out today on the very next internal email you send.
Separate "Text Review" from "Fact Checking"
I used to read AI-generated drafts from top to bottom, tweaking them while thinking, "It sounds natural enough, so it should be fine." Looking back, however, the mistakes were not in the phrasing, but in facts like the following:
- "Staging environment" was written where it should have said "Development environment"
- The assigned team name remained an outdated organizational name
- The deadline was written as "by Friday," but in reality it was "by Thursday morning"
- Referenced ticket numbers or document titles were missing from the body
These types of mistakes are hard to catch merely by reviewing to polish the text. That is why, upon receiving generative AI output, I make it a practice to bring "what needs to be checked" to the surface first.
"Proper nouns" here does not just mean people's names. In business operations, it is practical to treat items like the following collectively as targets for verification:
Category / Examples of items to check | People & Organizations: Assignee names, department names, client names, meeting/committee names | Projects & Systems: Project names, feature names, environment names, tool names | References: Ticket numbers, document titles, URLs, folder names | Conditions & Figures: Dates/times, deadlines, item counts, amounts, versions, scope | Judgments: Decided items, pending items, approvers, next assignees
Trying to check everything perfectly is unsustainable. To start, prioritizing "things that will change the other person's actions if mistaken" is more than enough. For instance, in a request email, starting with just three items—deadline, recipient, and target file—yields significant results.
A "Fact Memo" Created Before Drafting Only Needs to Be 3 Lines
You don't need to write lengthy background explanations before giving a prompt to an AI. Just make a note of the following three lines.
確定している事実：4月18日15時に検証環境へ反映する
未確認の事実：利用部門への周知担当は未定
書いてはいけない推測：本番反映日、障害の原因
Attach this note and instruct it: "Do not state unverified facts as certainties; clearly specify that confirmation is required."
Taking this extra step reduces instances where the AI tries to fill in blanks with natural-sounding words. It is especially useful for texts where facts and planned schedules easily get mixed up, such as incident reports, notices of specification changes, or draft responses to clients.
Have the AI Generate a "Verification Checklist" After Outputting
Once the draft is ready, before jumping right into editing the text, use the following prompt.
以下の文章から、事実確認が必要な項目を抽出してください。
人名・部署名・案件名・システム名・日時・数値・参照資料・決定事項を対象にします。
表形式で、
1. 本文中の記載
2. 分類
3. 確認先または確認方法
4. 誤っていた場合の影響
を出してください。
不明な情報は補完せず、「要確認」としてください。
【文章】
（ここに下書きを貼る）
For example, for a sentence like "We will deploy this to the verification environment on April 18," have the AI generate "Date & Time," "Environment Name," and "Deployment Target" as verification checklist items.
The important thing here is not to treat the AI's table as the definitive answer. The table is merely an aid for surfacing verification checkpoints. Details are finalized only after you cross-check them against primary sources such as tickets, formal meeting minutes, or responses from the person in charge.
Narrow Down the "Scope of Edits" When Requesting Revisions
When you find an error upon cross-checking, simply asking it to "please revise this to the correct information" can lead the AI to rewrite unrelated phrasing as well. I make it a rule to specify the exact scope it is allowed to modify.
次の修正だけを反映してください。
- 「検証環境」を「ステージング環境」に変更
- 締切を「4月18日15時」に変更
それ以外の文の構成、依頼内容、敬語表現は変更しないでください。
修正後、変更した箇所だけを箇条書きで示してください。
Having it output the modified portions at the end narrows down where you need to re-verify. Even for a short email, this provides a completely different level of reassurance when sending messages to multiple recipients or when handing off drafts among multiple team members.
If You Want to Try It Today, a Single Pre-Send Email Is Enough
You don't need to try this on crucial external documents right from the start. First, try it out on a single email where facts are easy to verify, such as an internal meeting notice or a work request.
There are four steps.
- Jot down the deadline, the person in charge, and the subject matter in a three-line note as "established facts"
- Generate a draft with that note attached
- Convert the draft into a verification checklist
- Cross-check against the original ticket or calendar before sending
Once you get used to this, rather than focusing on "what to make the AI write," you will instinctively see "which facts need to be verified" first. This is a perspective that proves directly useful even in work that does not involve AI.
Please note that when pasting internal company information into generative AI, always be sure to check your organization's usage policies. Handle client names, individual names, contract values, and unreleased incident details in approved environments, or replace them with masked text or pseudonyms. The goal of cross-checking is not to input large amounts of information, but to make items that cannot afford errors clearly visible.
Summary
Even if drafts produced by generative AI sound natural, they do not guarantee internal company facts.
- Before drafting, categorize information into "confirmed," "unconfirmed," and "conjectures that must not be written"
- After generation, turn proper nouns, figures, and decisions into a checklist
- When revising, clearly specify the scope of permissible changes
- Always cross-check with primary sources at the end
Start by trying a proper noun check on your next email. Taking just a few minutes before sending can save you the hassle of having to make corrections or explanations later.
