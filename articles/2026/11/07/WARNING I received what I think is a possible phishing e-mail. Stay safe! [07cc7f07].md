---
id: "07cc7f075aaadbb4"
title: "WARNING: I received what I think is a possible phishing e-mail. Stay safe!"
url: "https://reddit.com/r/ChatGPT/comments/1xqcluv/warning_i_received_what_i_think_is_a_possible"
link: "https://reddit.com/r/ChatGPT/comments/1xqcluv/warning_i_received_what_i_think_is_a_possible"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T18:00:21Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Spare-Dingo-531"]
language: "en"
summary: "I woke up this morning this e-mail in my inbox. My first instinct was to click the \"remove this token\" button, but I almost immediately realized that clicking the green button would be clicking a link..... and you should never click on links you receiving by e-mail unless you recognize them. I ran the e-mail through ChatGPT, and this is what I found. I would not trust this email. It has several…"
tags: ["r/ChatGPT"]
orgs: ["OpenAI"]
topics: []
content_source: "post"
word_count: 410
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1xqcluv/warning_i_received_what_i_think_is_a_possible/"
score: null
comments: null
community: "r/ChatGPT"
---

# WARNING: I received what I think is a possible phishing e-mail. Stay safe!

Reddit · Spare-Dingo-531 · 2026-11-07

I woke up this morning this e-mail in my inbox. My first instinct was to click the "remove this token" button, but I almost immediately realized that clicking the green button would be clicking a link..... and you should never click on links you receiving by e-mail unless you recognize them. I ran the e-mail through ChatGPT, and this is what I found. I would not trust this email. It has several major warning signs, and I found something particularly important in OpenAI's official documentation. Your email claims that a new access token was created with permission to: - Read all your ChatGPT conversations. - Access all your documents. - View pictures you've shared in chats. That sounds alarming, but receiving this email does not establish that anyone actually accessed your account. The biggest red flag is the sender: noreply@onelogin.com , presented as the ChatGPT Account Team. OpenAI publishes a list of its legitimate email domains. onelogin.com is not on that list. OpenAI Help Center OneLogin is a real identity-management service, but that doesn't make this a genuine ChatGPT security notification. What I found in your actual Gmail message I checked the original email, including its technical headers. There's an interesting twist: - SPF, DKIM and DMARC all passed for onelogin.com. This suggests the message really was sent using infrastructure authorized by OneLogin. - The “Remove this token” button uses a tracking redirect through admin.onelogin.com. I couldn't verify its ultimate destination. - The message includes an unsubscribe link, and even has the grammatical error “A access token.” Both are unusual for a serious security alert. So this may be a fraudulent message sent through a legitimate third-party email service, rather than a simple forged sender address. I cannot determine who initiated it. What I'd do now 1. Don't click anything in the email. 2. Open ChatGPT directly, not through the email. 3. Go to Settings → Security and login → Security history and check for unfamiliar activity around 12:33 PM today. 4. Check Active sessions for unknown devices. If you find suspicious activity, log out of all sessions, secure your password, and enable MFA. OpenAI Help Center 5. Report the message as phishing in Gmail. By the way, I did check my security history and I did not find any unfamiliar activity. I also logged out of all active sessions. I'm also trying to send the screenshots to OpenAI. What do you think? Was this a phishing e-mail? Stay safe!
