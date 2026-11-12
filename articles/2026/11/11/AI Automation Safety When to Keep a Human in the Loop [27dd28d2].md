---
id: "27dd28d2efc684e2"
title: "AI Automation Safety: When to Keep a Human in the Loop"
url: "https://hackernoon.com/ai-automation-safety-when-to-keep-a-human-in-the-loop"
link: "https://hackernoon.com/ai-automation-safety-when-to-keep-a-human-in-the-loop"
source: "HackerNoon"
domain: "hackernoon.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-11T16:00:00Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Muneeb Ashraf"]
language: "en"
summary: "AI can send routine replies, but it never pays or deletes. How we decide which automation steps need a human approval, and how to build one in Zapier."
tags: []
orgs: []
topics: ["agents & coding", "models & research", "products & launches", "safety & ethics"]
content_source: "fulltext"
word_count: 1688
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AI Automation Safety: When to Keep a Human in the Loop

HackerNoon · Muneeb Ashraf · 2026-11-11

My rule for every AI workflow we build: the AI never pays or deletes on its own, and it only sends what a person has already decided is safe to send. Routine, tested cases go out automatically. Anything involving money, a judgment call or a step you can't take back stops and waits for a person.
I run Amplence, a small AI automation agency, and I've been building software and automations for clients since 2018. Most of what we automate runs without anyone touching it. But I've learned that not everything that can be automated should be. The steps I'm most careful with are the ones you can't take back.
This post covers how we decide which steps get a human approval, two lessons from a live client system, an invoice-approval template I built, what we do when a model is retired, and how to build the approval step in Zapier with Human in the Loop.
How we decide which steps need a human
A step gets an approval when a wrong run is expensive and can't be reversed. We ask three questions about every step that acts on the outside world:
- Can we undo it? A wrong label in a spreadsheet takes a second to fix. A sent email, a paid invoice or a deleted record does not come back.
- Does it leave our hands? Anything that reaches a customer, a bank or another company's system is out of our control the moment it runs.
- What does a mistake cost compared with a delay? If waiting an hour for a person costs almost nothing, and a wrong run costs money or trust, the step waits.
If the answer to the first question is no, and either of the other two points to risk, a person approves it. In practice, that sorts most steps like this:
The approval isn't a sign that the AI is bad. It's a sign that the action is permanent.
Case 1: Customer support in four languages, with a person on the hard cases
CollageDepot is a Shopify store whose customers write in Dutch, English, German and French. We spent two months building an AI email system that handles that inbox.
The workflow does the slow parts on its own. It reads each incoming email, detects the language, looks up the order in Shopify and drafts a reply in the customer's own language. It also applies the store's material-specific rules, so the answer about one product doesn't get copied onto another.
Not every email gets the same treatment. Routine questions that match the cases we tested are answered automatically, which covers about 65% of the 5,000-plus emails the store gets each month. The rest, including anything judgment-heavy, unclear or touching money like a refund or a return, goes to a person in a review dashboard in Airtable instead of getting a confident guess.
That split is what made the client comfortable going live. The AI handles the volume in four languages, and a person still decides every case where a wrong answer would cost money or trust. A person set the rules for what goes out automatically, and the AI doesn't get to widen them.
Case 2: The workflow said "active" and processed nothing
In September 2026, the CollageDepot workflow stopped reading email for part of a day while still showing as active. Nothing errored. The dashboard looked healthy. No new emails were being picked up.
The cause was the connection to the mailbox. The workflow listens to the inbox over IMAP, and it was set to force a reconnect. One of those reconnects failed silently. The workflow stayed switched on, but it was listening to a connection that no longer existed.
Floris, the client, spotted it in under a day. We had no alert for it. Because nothing was being processed at all, nothing wrong was sent to anyone, and the only damage was slower replies. We removed the faulty reconnect setting, and the listener has been stable since.
The lesson I took from it: "active" is not the same as "working." A status light tells you the workflow is switched on, not that it's doing anything. If a workflow normally handles something every hour, check for output, not status. A simple scheduled check that alerts you when nothing has come through in a few business hours catches this kind of silent failure long before a customer does.
Case 3: An invoice template that holds payment when bank details change
This one isn't a client system. It's an invoice-approval template I built, and the rule at its center works in any tool: when an invoice arrives with bank details that don't match what's on file for that supplier, the workflow holds it. It doesn't pay, and it doesn't update the supplier's record. A person checks it first.
This is one of the most common ways businesses lose money to email fraud. Someone gets into a supplier's mailbox, or fakes one, and sends a normal-looking invoice with a new account number. An AI reading that invoice will extract the new details perfectly. It has no way to know they're wrong.
So the workflow does the reading and the comparison, and the person does the judgment:
- The AI extracts the supplier, amount and bank details from the invoice.
- The workflow compares the bank details with the supplier's stored record.
- If they match, the invoice moves on to the normal payment run.
- If they don't match, the invoice is held and a person is asked to approve it.
- The person confirms the change with the supplier using a phone number or contact already on file, never one from the invoice email.
- Only after that does anyone update the record or pay.
The hold costs a day at most. Paying a fraudster costs the whole invoice, and that money rarely comes back.
Case 4: When a model is retired, we re-test for about three weeks
AI providers retire models on their own schedule, and the workflow has to move to a newer one. We treat that switch as a new release, not a settings change, and re-testing a client build takes us roughly three weeks.
A newer model isn't simply a better version of the old one. It can phrase things differently, follow a rule a little more loosely, change the length or format of its output, or handle one language better and another worse. In a support workflow that answers in four languages, any of those can quietly change what customers read.
Those three weeks go to:
- Running the new model on real past cases and comparing its output with what was approved before
- Checking each language separately, not just English
- Confirming the structured output, like extracted fields, still matches what later steps expect
- Running it live with every output going through human approval, before relaxing anything
This is where the approval step earns its keep a second time. The hard cases already go to a person, and during the re-test the new model's output is reviewed before it's trusted to send anything on its own.
How to build the approval step with Zapier's Human in the Loop
Zapier's Human in the Loop pauses a Zap until a person responds, then continues or stops based on their answer. Here's the invoice check from Case 3 as a Zap:
- Trigger: a new email with an invoice attached arrives in Gmail or Outlook.
- Extract: an AI step pulls out the supplier name, amount, invoice number and bank details.
- Look up: find the supplier's stored bank details in Zapier Tables or a Google Sheet.
- Branch: use Paths. If the bank details match, create the bill for your usual payment run. If they don't, go to the approval step.
- Approve: add Human in the Loop with the Request Approval action.
- Continue only on approval: put the record update and payment steps after the approval, so they run only if a person approves.
The settings matter more than the step itself. For anything that moves money, this is how we set the Request Approval action:
After the reviewer responds, later steps can use the Decision field and any Reviewer Note. Every approval and decline is also logged in the Zap's change history, which gives you an audit trail of who approved what.
A few limits to know before you build:
- Human in the Loop needs a paid plan. It isn't on the Free plan.
- Reviewers need their own Zapier account, and the Zap must be shared with them.
- On a Pro plan, approval requests can only go to yourself. To send them to a teammate, you need Team or Enterprise.
- The step can't go inside or after a Looping by Zapier step.
The same pattern works for the other cases. For a customer reply, use Request Approval with Let Reviewer edit content? set to Yes, so the reviewer can fix the draft before it sends. For a delete or cancel step, set the timeout to end the run, just like a payment.
A short checklist before you automate the next step
Let the AI do the reading and drafting. Keep a person on the steps you can't take back. Before you switch a step to fully automatic, check:
- Does it pay or delete, or send anything outside the cases you've tested? If yes, add an approval.
- If nobody responds, does the workflow stop? Silence should never count as approval.
- Can the reviewer see what changed, not just the final value?
- Will you notice if the workflow goes quiet, not just if it errors?
- When the model behind it changes, do you have time and real examples to re-test it?
The goal isn't to slow automation down. It's to make it safe enough that clients trust it with the rest of their work.
Sources
- Zapier: Human in the Loop guide
- Zapier Help: Use the Request Approval action
- Zapier Help: Use Human in the Loop to pause Zap workflows pending human review
