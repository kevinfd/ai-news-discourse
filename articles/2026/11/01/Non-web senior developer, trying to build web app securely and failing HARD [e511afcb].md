---
id: "e511afcb9091e8c4"
title: "Non-web senior developer, trying to build web app securely and failing HARD"
url: "https://reddit.com/r/ClaudeAI/comments/1xlakfg/nonweb_senior_developer_trying_to_build_web_app"
link: "https://reddit.com/r/ClaudeAI/comments/1xlakfg/nonweb_senior_developer_trying_to_build_web_app"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T18:31:28Z"
published_date: "2026-11-01"
collected_at: "2026-11-02T13:05:12Z"
authors: ["ceramic_black"]
language: "en"
summary: "So title says it all. I have great great experience in programming, over 10 years, in different platforms. Just that neither of those platforms were web/browser related. So, with good AI's like Opus 5, i finally said let's fricking do this, as i need to build some niche tools for niche markets and my own business, and a web app is most suited (not mobile of desktop app). But i cannot get…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 629
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlakfg/nonweb_senior_developer_trying_to_build_web_app/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Non-web senior developer, trying to build web app securely and failing HARD

Reddit · ceramic_black · 2026-11-01

So title says it all. I have great great experience in programming, over 10 years, in different platforms. Just that neither of those platforms were web/browser related. So, with good AI's like Opus 5, i finally said let's fricking do this, as i need to build some niche tools for niche markets and my own business, and a web app is most suited (not mobile of desktop app). But i cannot get anything done "production" level on web - either some weird cookies fail, either something leaks, either some edgecase is forgotten, or some random shit happens that would critically break or give unwanted access to a database / backend. Keep in mind that this is because my experience on web development is 0, hence all the weird parts of security concerns here is unknown to me, and feels so strange being so different than Mobile or a desktop app where you have secure storage to an access token, then you make an API call with that secure token, and that's it, nothing much to break or leak. I tried to approach a "ready made" stack like Laravel , where you have like a full "batteries" framework for auth, security, with the idea of "let's not handcode anything sensitive", so like to have the entry point ready, and after everything is securely gated, any other DB access is based on that access token and the role of the user. It felt like going well, was building my features, with auth taken care by framework, and so on. Just to find out later, when i tried to migrate the same setup for an older non-laravel app, i asked to extract core features (like admin, auth, etc, so don't have to plan all again), to find out critical stuff like: - Admin sign-in bypass (as i said with the weird "web only" stuff like X-Forwarded-Host cookie) - Admin accounts reachable from the app side. While no team is selected (sign-in, password reset), the app’s database role could read and change admin accounts. One SQL injection could have reset an admin’s password and switched off their MFA - etc etc with many other stuff Even with Laravel i tried with Fortify and Filament (both versions, since there are 2 approaches), and still after 1-2 days of work i could easily find issues which initially weren't. Plus let's not even say that i get blocked by Claude for security concerns trying to "pentest" my own app. Now, i understand you will come and tell me "you just need to learn web development and security since that's not your specialty", and thanks for the obvious fricking answer. My question is am i missing something deeply on how i use AI to develop a web app? (i use it same as at work daily like review feature, plan, spec, test) just that i cannot "evaluate" the output as i can on my core skills, like i understand what is being done but i couldn't be aware of attack vectors) Or there is some better solutions for AI driven web development , or some scaffold app, or some template, to fortify the core features of the app so you can carry out the rest of personalized features without worrying about security 24/7? I just don't understand how there are 100000 new apps daily and people don't seem to care at all about this stuff, and i don't think anyone is a 20yo web developer to be able to take care of all security constraints And also please don't tell me to use some random skill to secure check my work. They work as well as a kind remembering to not scream while passing airport security check + security reviews & testing get blocked by AI filters.
