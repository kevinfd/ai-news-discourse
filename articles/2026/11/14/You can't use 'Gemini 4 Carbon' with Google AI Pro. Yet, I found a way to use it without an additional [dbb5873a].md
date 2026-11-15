---
id: "dbb5873a0e9ce4df"
title: "You can't use 'Gemini 4 Carbon' with Google AI Pro. Yet, I found a way to use it without an additional monthly subscription—uncovering a frequently overlooked $10 monthly ..."
url: "https://note.com/club_pyramid/n/nfa0c5d03d1ca?hl=en"
link: "https://note.com/club_pyramid/n/nfa0c5d03d1ca?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-14T02:06:00Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["海のピラミッド▲熊本／Cosa Nostra Japan"]
language: "en"
summary: "I am subscribed to Google AI Pro.I can use Gemini. I can use Antigravity. It's a quite convenient subscription for making full use of Google's AI services.However, things change when you try to use ..."
tags: []
orgs: ["Google"]
topics: ["agents & coding", "chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 2552
paywalled: false
image: "http://www.bing.com/th?id=ONUT.akgrB9sYOSwfVx92Vd2xFg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# You can't use 'Gemini 4 Carbon' with Google AI Pro. Yet, I found a way to use it without an additional monthly subscription—uncovering a frequently overlooked $10 monthly ...

note · 海のピラミッド▲熊本／Cosa Nostra Japan · 2026-11-14

SYSTEM NOTICE
You can't use 'Gemini 4 Carbon' with Google AI Pro. Yet, I found a way to use it without an additional monthly subscription—uncovering a frequently overlooked $10 monthly perk of Google AI Pro!
I am subscribed to Google AI Pro.
I can use Gemini. I can use Antigravity. It's a quite convenient subscription for making full use of Google's AI services.
However, things change when you try to use the top-tier reasoning model, 'Gemini 4 Carbon'.
According to Google's official model availability tiers, Google AI Pro only allows access up to Gemini 4 Argon. Carbon is intended for Google AI Ultra.
'I see. So if I want to use Carbon, I have no choice but to upgrade to Ultra.'
Normally, that's where the story would end.
However, while looking into the perks of Google AI Pro this time, I noticed something strange.
Google AI Pro includes $10 worth of generative AI and Google Cloud developer credits every month.
Moreover, these credits can be used for the Gemini API.
And in the Gemini API, separate from the standard model selection in Google AI Pro, you can use Carbon on a pay-as-you-go basis.
That means...
Could I use Carbon with the monthly credits while keeping my Google AI Pro subscription?
I tried it.
To cut to the chase, it worked.
Furthermore, I even succeeded in calling Carbon from an AI agent called Hermes Agent running on my Mac.
However, there were a few unexpected pitfalls.
I've decided to record the whole process here.
1. Google AI Pro has a perk that doesn't stand out much
The gateway to this discovery was the Google Builders Hub.
Google AI Pro includes premium benefits from the Google Developer Program.
Among them, there is this benefit.
$10 worth of generative AI and Google Cloud credits every month
This is an official developer benefit available to those who subscribe to Google AI Pro.
I suspect many people who just chat with Gemini or write programs in Antigravity might not even notice this benefit exists.
At the very least, I wasn't actively using it.
However, when I opened the benefits page on the Google Builders Hub, I found that credits issued in the past were still there.
One installment was 1,583 yen.
And that was for four installments.
A total of 6,332 yen.
Wow, to think there was 6,332 yen worth of AI development budget sleeping right here! 🤣
Of course, it cannot be withdrawn as cash.
However, it can be applied toward usage fees for eligible Google Cloud services.
And as long as I keep my Google AI Pro subscription, $10 worth of credits will continue to be issued every month.
That's $120 worth annually.
This is too good to ignore.
Moreover, each credit generally has a one-year expiration date from the time it is granted, and unused portions can be used in later months within that period.
In my case, I checked the box for "Always use this billing account" to set up future credits to be automatically applied to the same billing account.
Now the system is set up to receive the monthly benefits.
*The amount fluctuates based on exchange rates. It will not necessarily be 1,583 yen every month.
2. However, it cannot be used as-is in Antigravity
Now, since I have credits, I want to use them with the Google Antigravity I use daily.
It is natural to think that way.
Antigravity has a feature that uses additional AI credits when you have exhausted your regular model usage quota.
The settings screen also displays an item like this.
Enable AI Credit Overages
I thought, 'If I turn this on, can I use that 6,332 yen from earlier?'
I thought so.
However, it was not that simple.
Google Cloud developer credits and the AI credits managed on the Google One side are different systems.
The names are similar.
They are both Google services.
Moreover, both can be used for AI.
Yet, the wallets are separate.
This is quite confusing.
There is a way to use Antigravity in Google Cloud's pay-as-you-go mode, but I felt it was a bit troublesome to switch my usual development environment just to use it.
So, I changed my perspective.
There is no need to insist on using it with Antigravity. I should just use an AI agent that can directly utilize the Gemini API.
That is where Hermes Agent comes in.
3. Trying to add Carbon to Hermes Agent
Hermes Agent is an AI agent I use on my Mac.
I usually combine free cloud AI with local AI running on my Mac.
This Hermes has a feature that allows you to connect the Google AI Studio Gemini API.
In other words, as long as you have a Gemini API key, you can add Gemini to the Hermes model list.
So, I opened Google AI Studio.
I checked my existing Google Cloud project and set up paid usage for the Gemini API.
At this point, something unexpected happened.
“Prepayment is required.”
Huh?
Even though I have 6,332 yen in credit?
It seems that with the Gemini API prepayment method, you need to have a prepaid balance ready first in order to use the applicable Google Cloud credits.
For this account, a minimum deposit of 800 yen was required.
I actually paid this with a credit card.
I will state this clearly because it is important.
“No additional charges” in this case does not mean I didn't pay a single yen at all.
It means that there is no need to sign up for a higher-tier subscription like Google AI Ultra, and that the Carbon API usage fees can be covered by the developer credits included in Google AI Pro.
The initial 800 yen prepayment was necessary, and depending on usage, that might be consumed in the future.
However, according to Google's billing specifications, if applicable Google Cloud credits are valid, they are applied before the purchased prepaid balance.
In this case as well, the Gemini API became available after the 800 yen prepayment.
I turned off auto-charge.
This makes it easier to avoid unintended automatic deposits.
4. Connecting to Carbon! ...Or so I thought, but a different AI replied
I obtained a Gemini API key and immediately tried calling Carbon from Hermes.
The model ID is as follows.
gemini-4-carbon
However...
An error occurred.
Hermes gave up on connecting to Carbon and switched to the local Gemma 4 instead.
The screen displayed the following message.
Provider fallback: gemini/gemini-4-carbon unavailable
I see.
AI agents are smart.
If Carbon cannot be used, it continues the work with an alternative model.
However, this is troublesome for connection testing.
Just because a reply came back doesn't mean Carbon is the one answering.
Upon investigation, the first issue was the passing of the API key.
The API key I set temporarily in the Mac terminal was not carried over to other terminal windows.
I was getting caught by this in several tests.
So, I called the Google API directly to verify.
First, an authentication test.
HTTP 200.
Next, I retrieved the model information for Carbon.
HTTP 200.
Furthermore, I tried having Carbon generate text directly.
The answer that came back was,
"Connection successful"
This was also HTTP 200.
On Google's side, Carbon was operating normally.
The problem seemed to lie in how it was connected to Hermes.
5. I tried connecting from the Hermes app settings screen
This time, instead of using the terminal, I tried configuring it from the Hermes Agent Mac app.
The app has a setting item called "Provider".
When I opened "API Key" from there, there was an item called "Google AI Studio".
I registered the Gemini API key I created here.
Then, the Gemini series appeared in the model selection menu.
- Gemini 4 Hydrogen
- Gemini 4 Argon
- Gemini 4 Carbon
- Gemini Flash series models
Oh!
Carbon has finally appeared in the model list.
Select Carbon and start a new session.
Then, I sent the following message.
The reply was instantaneous.
'Connection test complete'
This time, there was no Fallback warning on the screen either.
Furthermore, checking the usage in Google AI Studio, the requests and token usage for Gemini 4 Carbon were recorded.
With this, I was able to confirm that it wasn't just the name 'Carbon' being displayed on the Hermes screen, but that the API was actually being used.
Just because Carbon cannot be selected in Google AI Pro does not mean you must upgrade to Google AI Ultra to use Carbon.
There was another legitimate way to use it by combining Google AI Pro's developer benefits with the Gemini API.
6. How much did using Carbon actually cost?
Checking the usage cost screen in Google AI Studio, the amount displayed at this stage of verification was,
9 yen.
As a result of testing Gemini 4 Carbon, this is quite an interesting figure.
Of course, this is the usage amount at the point including short connection tests, and it does not mean that long-term reasoning or large-scale file analysis can be done for 9 yen.
Since Carbon is an advanced reasoning model, if you make it do heavy work, token consumption will increase accordingly.
Also, with AI agents like Hermes, multiple API calls may occur from a single request.
Even so, I learned something from this experiment.
There is a way to pay for Carbon's API usage only for the work you need, without switching to a higher-priced monthly subscription.
And Google AI Pro has a $10 monthly developer credit that can be applied toward those costs.
It might not be enough if you continue to use Carbon on a daily basis.
However, if you limit its use to necessary situations such as critical design decisions, complex code reviews, or difficult document analysis, it is likely well worth utilizing.
Note that regarding whether this usage amount of 9 yen was actually deducted from the Google Cloud credit, it is necessary to wait for the reflection in the billing statement for final confirmation.
7. Don't forget to set up measures to avoid additional charges
This part is particularly important.
It is not a case of 'you have a $10 monthly credit, so you can keep using the API without thinking'.
The API is a system where charges are incurred based on usage.
If the credit runs out or you use services that are not covered, additional charges may occur.
In this environment, I implemented the following settings as safety measures.
- Gemini API is a prepaid system
- Auto-charge is OFF
- The monthly usage limit for the Gemini API is 1,000 yen
- Set up billing notifications for Google Cloud as a whole
With the prepaid system, the API is designed to stop when the balance runs out.
However, because usage amounts may exceed the balance or set limits due to delays in billing, it is not a guarantee of zero charges.
Also, budget notifications for Google Cloud as a whole do not automatically stop the target services.
Using the credit effectively and preventing unexpected charges to your credit card must be considered separately.
This time, I decided to start with a small limit and operate while checking the actual charges.
8. How to use this benefit?
For those who want to try the same thing, I will summarize the entry points.
1. Open the Google Developer Program benefits page
https://me.developers.google.com/benefits
Check the $10 monthly credit available through Google AI Pro.
2. Apply it to your Google Cloud billing account
https://console.cloud.google.com/billing
Once applied, you can check your balance on the 'Credits' screen.
3. Prepare the Gemini API in Google AI Studio
https://aistudio.google.com/api-keys
Verify the target Cloud project and billing settings, then create an API key.
Accounts requiring prepayment will need an initial deposit separately.
4. Connect to an app that supports the Gemini API, such as Hermes Agent
https://hermes-agent.nousresearch.com/
Register your Gemini API key and select Carbon as the model to use.
Do not share your API key with others; manage it within the app's secure settings screen.
5. Check your usage
https://aistudio.google.com/spend
Monitor your usage and costs, and set a monthly limit if necessary.
Note that simply receiving the Google AI Pro credit does not unconditionally grant the right to use Carbon. You must meet the model availability conditions and billing settings on the Gemini API side.
9. This is not a 'Google AI Pro hack'
What was interesting about this discovery is that it did not involve using any special loopholes.
Everything is a feature officially provided by Google.
Google AI Pro includes benefits from the Google Developer Program.
Those benefits include a $10 monthly developer credit.
With the Gemini API, you can use Carbon on a pay-as-you-go basis.
Hermes Agent has a feature that allows you to connect that Gemini API.
Each one is a standard feature.
However, when you combine them, a completely different way of using them emerges.
This is interesting.
In the world of AI, attention tends to focus only on the announcement of new models.
However, even within services you are already subscribed to, there are features lying dormant that can provide value depending on how you use them.
When you can't do something, it doesn't necessarily mean you need to immediately pay for a higher-tier plan.
'Is there another way to use this?'
Just by thinking that way and doing a little research, you can sometimes find surprising answers.
The 6,332 yen this time was exactly that kind of discovery.
10. AI is interesting precisely because it can be combined
I currently operate my own personal AI team by combining ChatGPT, Codex, Antigravity, Hermes, and others.
Each has its own area of expertise.
There are AIs that can be used for free.
There are AIs that run locally.
There are also AIs that excel at advanced reasoning.
There is no need to consolidate everything into one expensive subscription.
Leave your daily work to free AI or local AI.
Call upon high-performance models only when difficult decisions are required.
And for those costs, leverage the benefits of services you are already subscribed to.
By combining them this way, you can increase your AI team's capabilities without increasing your additional monthly fixed costs.
Being able to add Gemini 4 Carbon to Hermes Agent this time became a practical example of that.
AI evolves rapidly.
New models and new services appear one after another.
However, the fun isn't just in chasing the latest models.
Discovering what you can do by combining what you already have.
I think this is also a way to enjoy the AI era.
Well then.
Since Carbon has joined the Hermes team, what should I entrust it with next?
First, let's have it analyze the work the AI team has accumulated so far.
Since I've hired a new AI, instead of a welcome party, maybe I'll ask it to handle some difficult work.🤣
This is a record based on actual experience as of November 14, 2026, and official Google documentation. Model availability, credit benefits, API pricing, and billing specifications are subject to change.
Reference Materials
- Google Developer Program | Benefits and FAQ
- Google AI | About Gemini API Billing
- Hermes Agent | Google Gemini Integration Guide
- Google Builders Hub | Benefits
Hashtags
#GoogleAIPro #Gemini4Carbon #GeminiAPI #HermesAgent #GoogleCloud #AIAgent #GenerativeAI #AIUtilization #MyOwnAITeam
