---
id: "3d5094d07ec9245d"
title: "Using AI for Preliminary Checks on Expense Reports | Steps for Flagging Potential Send-Backs Against Regulations and Where Humans Decide"
url: "https://note.com/saborikeiri/n/n940ad3a543d2?hl=en"
link: "https://note.com/saborikeiri/n/n940ad3a543d2?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-24T03:45:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["さぼり経理のあい｜Aiで経理・総務を時短"]
language: "en"
summary: "Nice to meet you. I'm Sabori Keiri no Ai.I'll start with the conclusion.Using AI to check expense reports only extends as far as a \"preliminary check that flags suspicious line items against the rules ..."
tags: []
orgs: []
topics: ["policy & regulation", "products & launches"]
content_source: "fulltext"
word_count: 1178
paywalled: false
image: "http://www.bing.com/th?id=ONUT.Imebj8t6irc6ijirwGp_SA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Using AI for Preliminary Checks on Expense Reports | Steps for Flagging Potential Send-Backs Against Regulations and Where Humans Decide

note · さぼり経理のあい｜Aiで経理・総務を時短 · 2026-11-24

Using AI for Preliminary Checks on Expense Reports | Steps for Flagging Potential Send-Backs Against Regulations and Where Humans Decide
Nice to meet you. I'm Sabori Keiri no Ai.
I'll start with the conclusion.
At the end of the month, with 30 expense reports piled up, back in my first year when I reviewed everything manually with my own eyes, it took me a whole month to notice a duplicate submission of the exact same receipt from the same person.
AI excels at "errors detectable by rules," such as duplicate submissions or exceeding regulation amount limits. On the other hand, judgments like "was this meal/drink business-related?" are the job of humans.
Decide first: What information to pass to AI and what not to pass
Expense reports contain a lot of personal information. Before passing it to an AI, make sure to decide on the following. For details, please read Information You Should Never Enter into Generative AI and Internal Guidelines for Generative AI.
- Replace employee names with employee ID numbers
- Do not include bank account numbers or My Number (individual tax IDs) in the list to begin with
- If client/vendor names are confidential, replace them with labels like "Company A"
- Decide in advance whether the AI is permitted for company use
Step 1: Turn regulations into a "list of rules"
If you simply ask the AI to "read the regulations," its interpretations will vary. First, turn the regulations into a list that can be applied mechanically. For how to create the regulations themselves, see How to Create Expense Reimbursement Regulations.
ルール1：交通費は、経路と区間が書かれていること
ルール2：領収書が必要な金額は、〇〇円以上（金額は自社の規程のとおり）
ルール3：飲食費は、参加者の人数と氏名・社名、目的が書かれていること
ルール4：申請期限は、利用日の翌月〇日まで（自社の規程のとおり）
ルール5：同じ日・同じ金額・同じ支払先の重複がないこと
Fill in the numbers using the values from your own company's regulations. This article does not specify particular amounts.
Step 2: Have the AI inspect the list of submissions
次の「ルールの一覧」と「申請の一覧」を使って、一次チェックをしてください。
申請の一覧の列：申請番号、社員番号、利用日、申請日、区分、金額、支払先、摘要、領収書の有無
1. 各ルールに当てはまらない申請を、申請番号で挙げる
2. 挙げた理由を、どのルールに反するかを添えて、一行で書く
3. 重複の可能性がある申請を、組にして挙げる
4. ルールで判断できないもの（摘要が曖昧など）は「人が判断」として分ける
「差し戻す」と決めつけず、「差し戻し候補」として出すこと。
It is crucial to have it label items as "candidates for send-back." A human must review the submissions flagged by the AI and decide whether to actually send them back.
Step 3: Where Humans Make the Decisions
Do not leave the following judgments to AI.
- Whether it is business-related (costs for meals, gifts, meetings, etc.)
- Whether to allow exceptions without receipts
- How to handle cases not covered by regulations
- Tax treatment (whether it qualifies as entertainment or meeting expenses, etc.). When in doubt, consult a tax accountant
- How to communicate with employees whose submissions are rejected
Preparing standard templates for rejection messages, such as a Collection of Example Expense Rejection Messages, helps avoid friction.
Step 4: Know What AI Can Overlook and Get Wrong
- AI can misread receipt images (such as confusing 8 and 3, or 1 and 7). Humans must check the amounts
- AI can make mistakes judging deadlines depending on the date format (Japanese calendar vs. Western calendar)
- When regulatory rules are ambiguous, AI will fabricate a plausible-sounding answer
- It cannot evaluate information not included on the list (such as the context of a supervisor's approval)
Therefore, spot-check lines marked as "no issue" by AI with human eyes. I randomly review about 10% of the total each month.
Step 5: Connect the Results to Further Improvements
Collect the reasons for rejection over a month and sort them from most frequent to least frequent.
次は、今月の差し戻し候補とその理由の一覧です。
理由を分類して、多い順に並べてください。
そのうえで、申請する社員向けに「申請前のチェックリスト」を5項目で作ってください。
Once applicants are able to correct issues from the start, accounting's review burden will also decrease.
Example Scenarios: What to Do in Cases Like This?
Example 1: Two submissions for the same date and the same payee
AI will pair them up and flag them as "potential duplicates." However, it may simply be that separate purchases were made at the same store. Check the original receipts; if the date, time, and details differ, there is no issue. If they are identical, ask the applicant, "Could you please check if this might be a duplicate?" Avoid using an accusatory tone.
Example 2: Dining expenses with only "meeting" in the description
Because the description is too short, the AI categorizes it under "human review required." This is the correct behavior. You should ask the applicant for the participants and the purpose, and have them add that information. Do not have the AI generate a "plausible description," as this would create an inaccurate factual record.
Example 3: The receipt image amount differs between the AI's scan and the submitted amount
The AI may misread numbers. A human must examine the image and decide which amount is correct. If it turns out to be a scanning error by the AI, do not return that expense claim.
Common Pitfalls
- If the list of rules is too long, the AI will overlook the latter half. Divide the rules into batches of around 10 at a time when making requests.
- Leaving the list outdated even though regulations have changed. If you update the regulations, update the list on the very same day.
- Feeling relieved or anxious simply by looking at the number of "return candidates" flagged by the AI. Look at whether the reasons are accurate, rather than the count.
Verification Procedure (Monthly)
1. Compare each return candidate flagged by the AI against the original application one by one.
2. Sample some applications that the AI marked as "no issues" and review them manually.
3. For rules where errors occurred, rewrite the phrasing of the conditions and test them the following month.
4. Record the verification results line by line.
Frequently Asked Questions (FAQ)
Q. Can I paste the text of our regulations directly into the AI?
A. You should first determine as a company whether internal regulations can be pasted into the AI. Also verify that no personal information or client confidential information is included.
Q. Should we return all entries flagged as return candidates by the AI?
A. No. A human must review and make the decision. Check whether the AI's rationale is also correct.
Q. Can we let the AI handle tax treatment decisions?
A. Final tax determinations must be confirmed with a tax accountant or the tax office. Ask the AI only to organize the materials needed for judgment.
Summary
- AI initial checks are well suited for catching rule-based errors.
- Convert your regulations into a "list of rules" in advance.
- The AI's output is merely "candidates for return"; humans make the final decisions.
- Do not enter employee names, account numbers, or Individual Numbers (My Number) into the AI.
- Collect reasons for rejection and turn them into a pre-submission checklist.
Prompts and verification methods for reviewing documents, including expense reimbursements, are compiled in AI Document Check Prompt Collection.
*Please be sure to check the latest guidelines from the National Tax Agency regarding the tax treatment of expenses (entertainment expenses, meeting expenses, receipt retention, etc.). For specific determinations, please consult a certified tax accountant or the tax office. For consistency between company regulations, laws, and work regulations, please consult experts such as certified labor and social security attorneys or legal counsel.
#Accounting #ExpenseReimbursement #GenerativeAI #AIUtilization #ExpenseRegulations #Rejection #AccountingBeginners #OperationalEfficiency
