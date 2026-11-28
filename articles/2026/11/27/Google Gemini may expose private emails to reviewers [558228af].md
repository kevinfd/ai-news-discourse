---
id: "558228af41f71705"
title: "Google Gemini may expose private emails to reviewers"
url: "https://foxnews.com/tech/google-gemini-expose-private-emails-reviewers"
link: "https://foxnews.com/tech/google-gemini-expose-private-emails-reviewers"
source: "Fox News"
domain: "foxnews.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-27T13:38:58Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["Kurt Knutsson", "CyberGuy Report"]
language: "en"
summary: "Think about everything sitting in your Gmail inbox right now. Maybe there's a conversation with your doctor, a recent bank statement or a personal message you never intended anyone else to read. Your Google Drive may hold years of private documents. You probably don't spend much time thinking about who might see that information beyond the people you share it with. But what happens when you…"
tags: ["20e4fce4-e5ea-5f17-a3c6-cff443cee895", "fnc", "Fox News", "fox-news/tech/companies/google", "fox-news/tech/topics/security", "fox-news/tech/artificial-intelligence", "fox-news/us/personal-freedoms/privacy", "fox-news/tech/technologies/email", "fox-news/tech", "article"]
orgs: ["Google"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 2398
paywalled: false
image: "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2026/07/931/523/Gemini-App.jpg?ve=1&tl=1"
discussion_url: null
score: null
comments: null
community: null
---

# Google Gemini may expose private emails to reviewers

Fox News · Kurt Knutsson, CyberGuy Report · 2026-11-27

Think about everything sitting in your Gmail inbox right now. Maybe there's a conversation with your doctor, a recent bank statement or a personal message you never intended anyone else to read. Your Google Drive may hold years of private documents. You probably don't spend much time thinking about who might see that information beyond the people you share it with. But what happens when you connect those services to Google's Gemini AI assistant?
An independent researcher has raised concerns about how Gemini handles information retrieved from connected Gmail and Google Drive accounts. The findings prompted questions about whether some private content could end up in conversations reviewed by humans.
We contacted Google, and the company confirmed that some information retrieved from connected Gmail and Drive accounts may be seen by human reviewers under certain circumstances. Google stressed that these connections are off by default. Here's what you should know before giving Gemini access to your personal information.
Missed CyberGuy LIVE? Watch the replay and discover 5 ways to travel smarter and save money.
Our free CyberGuy LIVE class, 5 Ways to Travel Smarter and Save Money, has ended, but you can still watch the full replay. Kurt "CyberGuy" Knutsson walks you through five practical ways to protect your phone and personal information, avoid common travel scams, find better deals, save money on bookings and use technology to make your travels easier and less stressful. No technical experience is needed.
Watch the free replay + downloadable checklist now at CyberGuyLive.com.
AI CHATBOT PRIVACY: WHAT YOUR AI MAY KNOW ABOUT YOU
Researcher raises concerns about Google Gemini privacy
An independent researcher using the name thisisme6598 published findings on GitHub, raising questions about the way Gemini retrieves information from connected Gmail and Google Drive accounts. The researcher tested Gemini using a personal Google Account with connected apps enabled. According to the published findings, Gemini sometimes retrieved information from emails or files during conversations without someone explicitly asking it to search Gmail or Drive. For example, the researcher described asking Gemini whether an internet service bill seemed too expensive. During some tests, Gemini reportedly retrieved billing information from Gmail, including payment amounts, account details and confirmation numbers.
In certain instances, the researcher reported that Gemini returned several sentences directly from an email and, in some tests, the entire email, including its headers. The researcher argues that this behavior creates a privacy concern because information retrieved into a Gemini conversation may become eligible for human review. However, the published findings do not establish that a human reviewer actually accessed the researcher's emails. Google told CyberGuy that the reported retrieval was standard behavior for someone who had voluntarily connected their apps. The company also emphasized that retrieved files remain visible only to the authenticated account holder and are not exposed publicly through this process.
Can human reviewers see your Gmail and Drive information through Gemini?
Yes, under certain circumstances. Google's own Connected Apps privacy documentation confirms that trained human reviewers, including service providers, may review a subset of information processed through Gemini's connected apps. That information can include summaries or excerpts from relevant Gmail messages and Google Drive documents.
In some cases, Google acknowledges that reviewers may see a complete email or file if it is short or especially relevant to the request. Google also says human reviewers may access some Gmail inbox content when investigating abuse or harm or responding to submitted feedback.
The company uses these reviews to evaluate Gemini's responses and improve its services.
Simply using Gmail or Google Drive does not subject your private content to this review process. The concern involves information retrieved after someone voluntarily connects those services to consumer Gemini. Google says it does not train generative AI models directly on someone's entire Gmail inbox or Drive. However, relevant information processed during Gemini conversations may be used for model improvement, depending on account settings. Google specifically warns against connecting apps containing confidential information someone would be uncomfortable having a reviewer see.
What Google told CyberGuy about Gemini privacy
We contacted Google directly to ask whether human reviewers could access Gmail messages or Drive files processed through the consumer Gemini app. We also asked whether the company had changed its privacy disclosures, notified existing customers and provided ways to prevent human review. A Google spokesperson told CyberGuy:
"Gmail and Google Drive’s core privacy protections remain unchanged, and your private emails and files are not reviewed by humans simply by using Gmail, Drive, or built-in Workspace features. Connecting those apps to the consumer Gemini app is off by default — it’s an optional way to get more personalized, time-saving answers across your Google apps when you want them. Users can disconnect their apps in Gemini settings at any time without losing access to Gemini’s core features."
Google also confirmed that when someone connects their apps to consumer Gemini with activity saving enabled, a small subset of conversations may undergo human review. Those conversations can contain relevant information retrieved from connected services. Before trained service providers review the material, Google says it separates the conversations from the associated Google Account and takes steps to reduce identifying information. The company also disputes the suggestion that the researcher's findings demonstrate public exposure of private files.
Did Google change its Gemini privacy promises?
Another part of the controversy involves changes to Google's public privacy disclosures. In Oct. 2023, Google published a blog post about its approach to generative AI privacy. The company said that content from Gmail, Docs and Drive accessed through Bard's Workspace extensions would not be seen by human reviewers or used to train the Bard model.
On Oct. 16, 2026, Google added an update to that same blog post. The new language explains that Google has introduced additional optional features allowing people to connect Workspace information to other Google services. Google says that when someone enables these newer features, a subset of the information may be used to train generative AI models, depending on their settings. It may also undergo human review in limited circumstances. The researcher argues that the change represents a reversal of Google's earlier privacy commitment.
However, Google's original statement concerned Bard's Workspace extensions, while the updated disclosure addresses newer connected features. The available evidence does not establish that Google quietly changed the underlying handling of information in existing connections. We asked Google whether people who previously connected their accounts were notified about the updated disclosures or asked to provide additional consent. Google's response did not directly address those questions. Instead, the company emphasized that the newer connections are optional and can be disabled. That leaves an important question about how clearly Google communicates changes to its AI privacy practices, particularly as new features gain access to more personal information.
APPLE TIGHTENS MAC SECURITY AS AI AGENTS SEEK YOUR FILES
What happens to your information after human review?
Google says it disconnects conversations from the associated Google Account before sending them to trained service providers for routine review. The company also takes steps to reduce personal information. However, removing account identifiers does not necessarily eliminate every sensitive detail contained in an email excerpt or document summary.
Google's Gemini Apps Privacy Hub explains that conversations reviewed by service providers may be retained for up to three years, even after someone deletes the corresponding activity from their Google Account.
Turning off Gemini's History setting, previously called Keep Activity, prevents future conversations from being used to train generative AI models unless someone submits feedback. However, Google may still process conversations for security and safety purposes, including with help from human reviewers.
On Nov. 16, 2026, Google announced changes to its Gemini privacy controls. Under the previous policy, Google retained conversations for up to 72 hours when Keep Activity was turned off. Under the new policy, Google will retain conversations for approximately two months when History is turned off. The company is rolling out these changes globally over several weeks.
How to protect your Gmail and Google Drive privacy
If you use Gemini, it's worth checking which accounts and services you've connected. You may find that you don't need every feature enabled. Here are some settings worth reviewing.
Disconnect Gmail and Drive from Gemini
Google groups Gmail and Drive under Google Workspace in its connected-app settings. Here's how to check the connection on a computer.
- Go to gemini.google.com and sign in to your personal Google Account.
- At the bottom of the sidebar, click Settings (which may appear as Settings & help).
- Select Personal Intelligence.
- Click Connected Apps.
- Find Google Workspace, which includes Gmail and Drive.
- Click More options (the three-dot menu) next to Google Workspace and select Disconnect.
- Follow any on-screen instructions to complete the change.
If you see a different menu, look for Connected Apps in Gemini's settings. Google offers different connection controls depending on account eligibility and available features. You can reconnect supported services later if you decide to use them.
Turn off Gemini History (formerly Keep Activity)
If you want to prevent future conversations from being used to train Google's generative AI models, review this setting.
- Visit Gemini Apps Activity.
- Sign in with the Google Account you use for Gemini.
- Find the History or Keep Activity control near the top of the page.
- Click On to open the available options.
- Select Turn off or Turn off and delete history (which may appear as Turn off and delete activity).
- Follow the confirmation prompts.
Turning off History stops future chats from being used to train generative AI models unless you choose to submit feedback. Some connected apps, including Google Workspace, become unavailable. Google may still process conversations for security and safety purposes. Depending on whether the latest privacy update has reached your account, conversations may be retained for up to 72 hours under the previous policy or approximately two months under the new policy.
WHAT YOUR INTERNET PROVIDER, WEBSITES AND ADVERTISERS SEE
Turn off AI training without deleting your Gemini history
Google is introducing a separate privacy control that lets you keep your Gemini conversation history while opting out of generative AI model training. If the new setting is available on your account, here's how to find it on a computer.
- Go to gemini.google.com.
- Click Settings.
- Select History.
- Uncheck the box next to Chat content including text & uploads.
- Also make sure Audio and Gemini Live videos & screenshares is unchecked if you see that option.
- Click Turn off to confirm.
Google says future chats will no longer be used to train generative AI models unless you submit feedback. However, human review may still occur for other service improvements and safety purposes. If you want to prevent Gemini from retrieving information from Gmail and Drive, disconnect Google Workspace separately.
Delete previous Gemini conversations
Disconnecting an app does not automatically delete information from earlier Gemini conversations. Google says Gemini may still use information from previously saved chats even after you disconnect the original app. That's why it's important to both disconnect the app and delete conversations containing sensitive information.
- Open Gemini Apps Activity at myactivity.google.com/product/gemini.
- Sign in to your Google Account.
- Click Delete above your activity.
- Select All time if you want to remove your saved history.
- Confirm the deletion.
Remember that previously reviewed information may remain subject to Google's separate retention policies, even after you delete your activity.
Avoid sharing sensitive information with AI assistants
Think carefully before giving an AI assistant access to confidential documents or personal communications. If you don't need Gemini to retrieve information from Gmail or Drive, leave those connections disabled. Also, remember that uploading a document directly into Gemini creates a separate privacy consideration.
Google says uploaded content may be used to improve its services when History, previously called Keep Activity, is enabled, potentially with help from human reviewers. Whether that content is used to train generative AI models also depends on your training settings and whether you submit feedback.
Does this Gemini privacy concern affect business accounts?
Google says the connected-app disclosures involved in this controversy apply to personal Google Accounts using consumer Gemini. Business, Enterprise and Education accounts covered by Google Workspace commercial terms have different privacy protections. According to Google's response to CyberGuy, customer data governed by those commercial terms is not reviewed by humans or used to train foundational AI models.
If you use Gemini through an employer or school, your organization's settings and agreements determine which features are available and how information is handled. The important point is that the consumer Gemini privacy rules discussed here should not automatically be applied to commercial Workspace accounts.
Kurt's key takeaways
I can understand why someone would want Gemini to search their Gmail or find a document buried in Google Drive. We've all wasted time digging through old emails looking for something we need. Having an AI assistant do that work sounds pretty appealing. But I think Google has a responsibility to make the privacy implications much clearer before someone connects an account. Most people probably don't expect information pulled from their private emails to become part of a conversation that could eventually be reviewed by another human being. I appreciate that Google responded to our questions and explained the safeguards it uses. Still, I would have liked a more direct answer about whether existing customers were notified when the privacy disclosures changed. If you're giving an AI assistant access to years of personal information, you deserve to know exactly how that information might be handled. Personally, I'd leave Gmail and Drive disconnected unless I had a specific reason to use those features.
Would you trust an AI assistant with access to years of your private emails if you knew some of that information could be seen by human reviewers? Or has Google crossed a privacy line, even with your permission? Let us know by writing to us at Cyberguy.com.
Sign up for my FREE CyberGuy Newsletter
- Get my best tech tips, urgent security alerts and exclusive deals delivered straight to your inbox.
- For simple, real-world ways to spot scams early and stay protected, visit CyberGuy.com - trusted by millions who watch CyberGuy on TV daily.
- Plus, you'll get instant access to my Ultimate Scam Survival Guide free when you join.
CLICK HERE TO DOWNLOAD THE FOX NEWS APP
Copyright 2026 CyberGuy.com. All rights reserved.
