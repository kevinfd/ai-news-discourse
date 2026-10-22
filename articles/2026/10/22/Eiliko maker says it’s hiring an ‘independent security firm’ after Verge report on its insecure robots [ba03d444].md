---
id: "ba03d4448fb3c959"
title: "Eiliko maker says it’s hiring an ‘independent security firm’ after Verge report on its insecure robots"
url: "https://theverge.com/news/1015824/eiliko-energize-lab-statement-on-robot-hack-breach"
link: "https://theverge.com/news/1015824/eiliko-energize-lab-statement-on-robot-hack-breach"
source: "The Verge"
domain: "theverge.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T11:00:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Sean Hollister"]
language: "en"
summary: "The Eiliko robot toy. | Photo by Sean Hollister / The Verge \n \n Eiliko, a cute robot charm you can hang on your bag with built-in AI conversations, turned out to be a security nightmare . It told owners that \"your secrets are safe with me,\" but hackers could easily read complete transcripts of everything we told the toy, and that was just the beginning . The Verge and security researcher Sammy…"
tags: ["AI", "Gadgets", "News", "Robot", "Security", "Tech"]
orgs: []
topics: ["robotics & autonomy", "products & launches"]
content_source: "fulltext"
word_count: 750
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Eiliko maker says it’s hiring an ‘independent security firm’ after Verge report on its insecure robots

The Verge · Sean Hollister · 2026-10-22

Eiliko, a cute robot charm you can hang on your bag with built-in AI conversations, turned out to be a security nightmare. It told owners that “your secrets are safe with me,” but hackers could easily read complete transcripts of everything we told the toy, and that was just the beginning. The Verge and security researcher Sammy Azdoufal spent over a month trying to get in contact with the company, including emails to Energize Lab CEO and founder Shaw Yeung. Nobody would answer our questions.
Eiliko maker says it’s hiring an ‘independent security firm’ after Verge report on its insecure robots
‘We know that words alone will not earn that trust back.’
Now, the company is finally breaking its silence, though its response leaves something to be desired.
“We have confirmed the core issues identified in your reporting and are addressing each of them,” Energize Lab told The Verge in an unsigned statement from a generic email address. The company says it will hire an independent security firm to fully review all of its systems, and has set up a dedicated security@energizelab.com contact email.
The company also claims that as of Wednesday, it has “closed all external access to our backend systems” and “disabled the interface that allowed a robot’s responses to be modified remotely.”
Energize Labs is also pledging to “no longer store conversation records or the user profiles generated from them,” and says it will delete the conversation records, user profiles, and “avatar images” it has already stored.
Notably, the company isn’t promising to get rid of data collection for good. “The long-term memory and custom avatar features will not return until that review confirms they are secure,” it writes, suggesting that Energize Lab does plan to store some personal information once its systems are hardened.
Even more notably, Energize Labs’ systems are not yet secure. With Azdoufal’s help, I can confirm that as of the company’s email, it was still storing audio recordings and photos of its customers at unsecured public web addresses with no protection whatsoever. If I gave you a link (which I won’t) you could click and immediately be looking at an owner’s face.
Azdoufal also tells me he still has full SSH access to these robots, and that he can still theoretically read transcripts and modify the toy’s behavior. So when Energize Lab says it has “closed all external access,” that doesn’t seem to be accurate.
“We know that words alone will not earn that trust back,” Energize Lab tells The Verge. “We intend to earn it through what we do in the coming weeks, and we will keep you informed as we go.” That sounds like a good plan, because some of today’s words still don’t ring true.
Here is Energize Lab’s full unsigned statement to The Verge:
Dear Sean,
We sincerely apologize to you and to Mr. Azdoufal for not responding over the past month. This was our failure: After receiving the relevant information, we failed to sync with the technical team in a timely manner, and the subsequent troubleshooting also took some time. We have now set up a dedicated security inbox, security@energizelab.com, which is staffed and monitored.
We thank you and Mr. Azdoufal for bringing these issues to our attention. We have confirmed the core issues identified in your reporting and are addressing each of them.
As of today, we have:
Closed all external access to our backend systems and rotated all access credentials;
Disabled the interface that allowed a robot’s responses to be modified remotely;
Taken the long-term memory feature offline. We no longer store conversation records or the user profiles generated from them;
Taken the custom avatar feature offline. The app now offers built-in avatars only.
We will delete stored conversation records, user profiles, avatar images, and related content.
We are engaging an independent security firm to conduct a full review of our systems. The long-term memory and custom avatar features will not return until that review confirms they are secure. We will share an update on our progress once the review is completed.
We started Energize Lab because we wanted to build small robots that bring a little joy into people’s lives. That idea only works if people can trust what is inside them, and we let them down. We know that words alone will not earn that trust back. We intend to earn it through what we do in the coming weeks, and we will keep you informed as we go.
Sincerely,
Energize Lab Team
