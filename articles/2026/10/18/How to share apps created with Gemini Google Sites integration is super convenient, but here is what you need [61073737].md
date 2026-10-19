---
id: "6107373729070911"
title: "How to share apps created with Gemini? Google Sites integration is super convenient, but here is what you need to know"
url: "https://note.com/miyamotchan/n/n2a3eedc2ba84?hl=en"
link: "https://note.com/miyamotchan/n/n2a3eedc2ba84?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-18T05:29:00Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["宮本恭彦"]
language: "en"
summary: "Gemini Canvas is incredibly convenient!While chatting with AI, original calculation tools and cute web pages are assembled right before your eyes in no time. There is a bit of a thrill the moment the ..."
tags: []
orgs: ["Google"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 1393
paywalled: false
image: "http://www.bing.com/th?id=ONUT.F6LbI9XhvZIVdXC2d31nbA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# How to share apps created with Gemini? Google Sites integration is super convenient, but here is what you need to know

note · 宮本恭彦 · 2026-10-18

How to share apps created with Gemini? Google Sites integration is super convenient, but here is what you need to know
Gemini Canvas is incredibly convenient!
While chatting with AI, original calculation tools and cute web pages are assembled right before your eyes in no time. There is a bit of a thrill the moment the preview starts working on the screen. It is that excitement of feeling like you have suddenly become a skilled programmer.
But didn't you immediately hit a high wall after that, thinking So, how do I pass this on to someone else??
I want to just send a URL and have team members or friends use it. Yet, if someone tells me to create a GitHub account, open Google Sites, and copy the code... I just want to quietly close the screen.
For those of us in that situation, Google has delivered an incredibly welcome update. 
Surprisingly, Google Sites has been added as an export destination for Gemini Canvas!
This time, while being impressed by the ease of this "god-tier update," I have summarized the three pitfalls you should definitely watch out for that I discovered after actually trying it, along with tips to avoid failure.
I have been waiting for this! A god-tier feature that allows you to export directly from Gemini Canvas to Google Sites has arrived.
First, let me quickly explain what you can now do.
Until now, if you wanted to share code created in Canvas with someone, you had to go through these steps.
Until now: Copying and pasting code was tedious.
- Copy all the code from Canvas
- Create a new Google Site
- Select the "Embed" block and paste it into "Embed code"
- Adjust the size and layout
It is only a few lines when written out, but for beginners not used to code, it is anxiety-inducing to wonder, "Copy the code? From where to where?" and adjusting it after pasting was also a struggle.
From now on: One click by selecting "Google Sites" from the export menu in the top right.
That has changed completely with this update.
When you press the export button (share icon) in the top right of the Canvas screen, a new option called Google Sites has popped up.
Just click that once. 
Surprisingly, a "Google Sites draft" with the app created in Canvas already beautifully embedded is automatically generated.
“Wait, the page is already done...!”
Even without any knowledge of HTML or CSS, it takes you to the brink of web publication with just the click of a button. The hurdle for sharing small, handy tools for work, portfolios, or event information pages for family and friends has dropped to almost ground level.
But don't celebrate just yet... Here are 3 pitfalls you should definitely know about
“Now anyone can publish web apps without code!”
…I would love to celebrate that without reservation, but please wait just a moment.
After actually building various things and trying to integrate them, it seems there are several points where you might hit a wall, like “Huh? It’s not working…” or “An error screen popped up!”
To avoid panicking and feeling discouraged thinking “It’s broken!?”, I will share 3 pitfalls you should know in advance.
Pitfall 1: The Account Trap (Gemini and Google Sites must be the same account)
This is the one people tend to trip over first.
The “Google account you use for Gemini” and the “account you use to create the Google Site for publication” must be the same.
For example,
- You opened Gemini with your personal Gmail account and made a fun tool
- You thought, “I can use this for work!” and tried to export it to a site on your work Google Workspace account
…This cannot be done. The automatically generated Google Site is created within the Google Drive of the account currently logged into Gemini.
If you want to “publish it as a company site,” please make sure to open Gemini and create it from your company Google account from the start.
Pitfall 2: The Data Trap (The rule is that it must be a single self-contained HTML file. Spreadsheet or GAS integration is a no-go)
As you get used to Gemini, your dreams might expand to things like “I want to save the input data to a Google Spreadsheet” or “I want to connect it to GAS (Google Apps Script) or Firebase to build a full-scale database.”
However, what works cleanly with this Google Sites integration is only “things that are self-contained in a single HTML file.”
Think of it as “a state where the text (HTML), design (CSS), and moving parts (JavaScript) are all written inside a single sheet of paper,” and it will work perfectly.
Conversely, mechanisms that read/write to spreadsheets in the background or communicate with external servers to save data will either result in an error when exported, or the integration part will simply cut off and stop working.
Pitfall 3: The Functionality Trap (Due to Google Sites specifications, some external libraries do not work)
"I made it with a single HTML file, but the graph isn't displaying..."
In such cases, there is a high possibility that an external library is causing the issue.
When embedding external web code into Google Sites, for security reasons, it runs within a special container (such as iframe restrictions in technical terms).
Therefore,
- rich animation features loaded via the internet
- loading special external fonts or icons
- browser APIs that use cameras or location information
and the like are often blocked, which can easily lead to a situation where "nothing appears and the screen stays white."
No more failures! "Recommended usage recipes" to make 120% use of Google Sites integration
You might feel that "it sounds a bit difficult..." when three pitfalls are listed, but if you grasp the key points, it is truly a magical, god-tier feature.
From here on, I will deliver practical techniques to ensure you get it working smoothly on the first try without failure.
The perfect match is a tool that "calculates or diagnoses on the spot and finishes there"
The best match for this integration feature is a tool that does not involve data exchange with the outside and completes entirely on that screen.
Specifically, these are recommended!
- Simple calculator for splitting bills or proportional distribution
- Type diagnosis chart that gives results after you tap through questions
- Text formatting tool that counts characters or generates template text
- Simple landing page for announcing events or seminars
Since these all fit perfectly into a "single HTML file," they will work perfectly without breaking even a millimeter when exported to Google Sites.
Prompt tip: Emphasize "combine into one HTML file"
When having Gemini Canvas create code for you, try adding a "magic phrase" at the end of your prompt.
The magic phrase to add to your prompt: 
"I want to embed this in a Google Site, so please write the code in a way that is completely self-contained within a single HTML file, including CSS and JavaScript, without using external databases or GAS."
By just adding this one sentence to your prompt, Gemini will intelligently choose to avoid external integrations and write code that won't run into Google Sites' export restrictions.
With just this, the "it doesn't work!" trouble when exporting will be almost zero.
Conclusion
Although there are some minor limitations and quirks, "the experience of having something created by AI become a webpage that can be shared with the world (or within your team) with a single click" is truly the future itself.
An idea you had given up on because "I can't write code..." can be running as a tool that helps someone else just a few minutes later. I really hope you get to experience that excitement at least once.
Why not start by relaxing and trying to export a small, fun mini-tool like a "Today's Lunch Roulette" to Google Sites?
If you found this article helpful or think, "I might give it a try," please press the "Like (❤️)" button below; it would be a huge encouragement for me to write the next article!
If you have any tools you've created with Gemini Canvas or want to share "I made this!" reports, please let me know in the comments.
#Gemini
#GeminiCanvas
#GoogleSites
#GenerativeAI
#WorkEfficiency
