---
id: "f3530ce63e81be26"
title: "Meta's personal AI agent 'Muse' launches in Japan. First outside North America, it handles tasks like sending emails and making reservations, with integrations planned for ..."
url: "https://note.com/ali_archive/n/n96da2fbdbbfc?hl=en"
link: "https://note.com/ali_archive/n/n96da2fbdbbfc?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-26T03:59:00Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Ali"]
language: "en"
summary: "In 3 simple points Available on iOS, Android, and muse.ai starting October 23. Most basic features are free Plans and executes tasks autonomously, confirming with the user before sending emails or ..."
tags: []
orgs: ["Meta", "Google", "Anthropic"]
topics: ["agents & coding", "products & launches", "search & media", "chips & infrastructure"]
content_source: "fulltext"
word_count: 815
paywalled: false
image: "http://www.bing.com/th?id=ONUT.ege80AaRlYcKjnWeIRH4Cg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Meta's personal AI agent 'Muse' launches in Japan. First outside North America, it handles tasks like sending emails and making reservations, with integrations planned for ...

note · Ali · 2026-10-26

Meta's personal AI agent 'Muse' launches in Japan. First outside North America, it handles tasks like sending emails and making reservations, with integrations planned for Mercari, Money Forward ME, and Ticket Pia
In 3 simple points
- Available on iOS, Android, and muse.ai starting October 23. Most basic features are free
- Plans and executes tasks autonomously, confirming with the user before sending emails or making purchases
- Integrates with Gmail, Google Calendar, Instagram, etc. Integrations with domestic services are also planned
Good evening. I'm Ali, a former vintage clothing store clerk turned engineer. Today, I'm talking about how Meta's AI agent, which can act on your behalf when you ask it to 'take care of this,' has arrived in Japan.
What was announced
On October 23, Meta announced the launch of its personal AI agent 'Muse' in Japan. The official newsroom states, 'Muse is available in Japan starting today on iOS, Android, and muse.ai.' It was first released in North America in September, making Japan the first region outside North America to receive it. According to Impress Watch, it saw over 10 million downloads in its first month in North America, with paid plans starting at 2,799 yen per month.
It can perform tasks such as sending emails and booking travel. When given a major goal, it helps create a personalized plan, adjusts time and resources, and proceeds with the work autonomously. It can operate browsers to fill out forms, and time-consuming tasks continue even after the app is closed. You receive notifications when the situation changes or when approval is needed for actions like sending emails or purchasing products.
Integrations include Gmail, Google Calendar, and Instagram, as well as Stripe, Shopify, Trip.com, Agoda, and Klook. For the Japanese market, it is working on integrations with Mercari, Money Forward ME, and Ticket Pia. Regarding security, it operates in a dedicated virtual machine isolated for each user called 'Muse Secure VM,' and an agent called 'Sentinel,' independent of Muse, manages internet access. Muse cannot see the user's passwords or payment methods and always asks for confirmation before critical operations. Users can check operation history, change or revoke integration scopes, and opt out of training, and it is explicitly stated that conversations and data within the virtual machine are not shared with advertising systems. Features already announced in North America, such as voice mode and avatars, will have their Japanese release dates announced separately.
What will change
This marks the arrival of the shift from 'AI that answers questions' to 'AI that acts on your behalf' in a consumer app in Japan. While coding agents for engineers have existed before, this targets daily chores like emails, reservations, and shopping, and includes domestic services like Mercari and Money Forward ME as integration partners. This has the potential to significantly broaden the user base.
What do I think as an active engineer
The security design is structurally interesting. An isolated VM for each user, a separate Sentinel managing outbound communication, and authentication credentials kept inside the VM, hidden from the main app. This follows the same line of thinking as the 'microVM per agent, injecting credentials only at the point of outbound communication' concept recently discussed for enterprise agent platforms. Google Cloud's Agent Compute Engine, announced on October 22, takes the same approach. It is noteworthy that this design has trickled down to a consumer product.
There are also points of caution. While 'confirming before sending' is a safety valve, it is commonly said that as confirmations increase, people tend to press OK without reading the content. Since the design involves handing over your entire Gmail and calendar, it is the user's responsibility to limit the scope of integration and regularly review operation history. This is especially true if services involving money are among the integrations.
In terms of pros and cons, the fact that the privacy explanation is specific and explicitly states that data is not shared with advertising systems is a plus. On the other hand, whether a company whose core revenue is advertising can maintain this policy is something to watch in future policy changes.
One-sentence impression
'It keeps working even after you close the app' sounds convenient, but also a bit scary. It might be safer to start by trying out read-only integrations first.
▼ Here are the instruction rules I use in practice (paid)
There is no finished prompt. I will show you all the 'instruction rules' that grew every time I left it to Claude Code and it failed (800 yen)
https://note.com/alien_archive/n/nab97438b2e51
Source
- Meta: Meta launches personal AI agent 'Muse' in Japan
https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/
- Impress Watch: Meta's personal AI agent 'Muse' starts in Japan
https://www.watch.impress.co.jp/docs/news/2150567.html
- ITmedia NEWS: 'Muse' launches in Japan, Meta's AI agent to integrate with Mercari, Money Forward, and Pia
https://www.itmedia.co.jp/news/article/2610/23/2000002535/
- Google Cloud: Introducing Agent Compute Engine and expanded agent governance
https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance
#AINews #GenerativeAI #Engineer #AIAgent #Meta
