---
id: "51699becef84de90"
title: "Don’t filter your email based on AI detection"
url: "https://blog.keyvan.net/p/dont-filter-your-email-based-on-ai"
link: "https://blog.keyvan.net/p/dont-filter-your-email-based-on-ai"
source: "Keyvan's blog"
domain: "blog.keyvan.net"
source_type: "community"
collector: "reddit"
date: "2026-10-19T00:54:10Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["fivefilters"]
language: "en"
summary: "In August I wrote about why I think AI detectors in general are a bad idea: a positive detection tells you almost nothing about the human effort that went into the work being flagged. And yet, I wrote, AI detectors are being used “almost like spam filters”.\nLess than a month after that post, Pangram, one of the leading AI detectors, released a Gmail integration. Let’s put aside, for now, the…"
tags: ["r/artificial"]
orgs: ["Microsoft"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 1002
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x9jbon/dont_filter_your_email_based_on_ai_detection/"
score: null
comments: null
community: "r/artificial"
---

# Don’t filter your email based on AI detection

Keyvan's blog · fivefilters · 2026-10-19

In August I wrote about why I think AI detectors in general are a bad idea: a positive detection tells you almost nothing about the human effort that went into the work being flagged. And yet, I wrote, AI detectors are being used “almost like spam filters”.
Less than a month after that post, Pangram, one of the leading AI detectors, released a Gmail integration. Let’s put aside, for now, the privacy implications of sending all your incoming email to a third-party company, and focus on how it’s being sold.
Pangram can’t detect slop
In Gizmodo, Bruce Gil wrote a piece credulously titled Pangram Can Now Check Your Gmail for AI Slop.
Pangram, in fact, cannot check your email for AI slop. It can only check for signs of AI use. It has no way of judging the quality of what it flags, to know if it’s slop or not.1
Gil goes on to write:
…users can choose to automatically archive emails labeled as AI, or just send them straight to spam.
Pangram itself suggests this on its page for the integration.
This feature removes any email flagged as AI from your inbox, so you don’t even have to look at it. Neither Pangram nor Gil seems concerned that real people’s perfectly legitimate emails could land in spam if this is switched on.
The only concern expressed in Gil’s piece is about false positives: emails written without AI assistance but flagged as AI. And he’s quick to reassure readers that it shouldn’t be a big worry:
Pangram claims its detector can identify AI-generated text with 99.98% accuracy, and an independent study that compared multiple AI-detection tools found Pangram to be the most effective.
This reinforces the idea that as long as the classification is correct, the content being classified must be trash and can safely be consigned to the spam folder.
AI-assisted email writing is not spam
Real people use AI to help them write emails. Often because they’re short on time and worried that a hurried email will come across as curt, or because they want to improve clarity, or because they’re not writing in their native language.
Thanks to research projects like LMArena and WildChat, we have thousands of examples of real AI chat prompts and responses related to email writing. I’ll share two below to give you an idea:
#1: Human prompt
can you please fix this email
Hello Professor [redacted],
I hope this email finds you well.
I just wanted to inform you about an issue I have been having with the course. I do not know if the rest of the class has had this. None of your recordings have been posted for me since week 3. Initially, I thought that something happened so I did not know what to do exactly. I kept doing the discussions and the quizzes. But, I still have not taken the mid-term exam and have not done the projects that include using Azure.
Again I do not know if this is an issue just for me or if you have been absent. Also, I am sorry if I should have informed you earlier about this issue.
Looking forward to hearing from you.
All the best, [redacted]
#1: AI rewrite
Dear Professor [redacted],
I hope this email finds you well. I am writing to inform you about an issue I have been experiencing with the course. I have not been able to access any of your recordings since week 3, and I am unsure if the rest of the class has had this problem.
Initially, I thought that there may have been a technical issue, but despite being able to complete discussions and quizzes, I have not been able to take the midterm exam or the projects that involve using Azure.
I apologize if I should have brought this to your attention sooner, and I am not sure if this is an issue just for me or if you have been absent. I would appreciate any assistance you can provide in resolving this matter.
Thank you for your time, and I look forward to hearing from you.
Best regards,
[redacted]
#2: Human prompt 
write an email to my advisor asking when and what courses i could be a TA for. he told me i don’t have to TA during my PhD but i decided i want to. keep it a bit informal but not too much
#2: AI response
Hi [Advisor’s name],
I hope you’re doing well! I wanted to follow up on our earlier conversation about TAing during my PhD. I know you mentioned that I wouldn’t need to TA, but I’ve been thinking it over and I’d actually like to get some teaching experience while I’m here.
Would you be able to let me know what courses might be available for me to TA, and when those opportunities typically come up? I’m flexible on timing and subject area, so I’m happy to work with whatever makes the most sense for the department’s needs.
Thanks for your time, and let me know if you need any additional information from me!
Best,
[Your name]
Both AI-written emails get flagged as AI with Pangram.
The classification is not wrong, but these are clearly not spam emails. If the recipients had used Pangram’s Gmail filter, both could have gone straight to spam, unseen.
Evading AI detectors
Evading detectors is not difficult for those determined to do it. But if detector companies continue conflating all AI assistance with slop, and shipping software that lets users send legitimate email straight to spam, I think ordinary users will start looking for tools to fight back.
There’s been recent research on new ways to evade detectors, and on models trained to write more like humans. I’ll be covering some of these in my next post.
While Pangram appears content to let users of its product conflate AI use with slop, the word ‘slop’ does not appear on its Gmail integration page, for good reason: it can’t detect slop.
