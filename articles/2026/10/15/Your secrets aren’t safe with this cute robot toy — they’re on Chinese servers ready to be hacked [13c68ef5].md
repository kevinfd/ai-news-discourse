---
id: "13c68ef579b05999"
title: "Your secrets aren’t safe with this cute robot toy — they’re on Chinese servers ready to be hacked"
url: "https://theverge.com/tech/1010727/eiliko-robot-hack-energize-lab"
source: "The Verge"
domain: "theverge.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T11:00:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Sean Hollister"]
language: "en"
summary: "Eiliko. | Photo by Sean Hollister / The Verge \n \n There's a new digital pet in town - a cute little marshmallow of a robot that can change its cartoony expressions to match your mood. But if you or your kids talk to \"Eiliko\" over Wi-Fi, it'll phone home to China. Its AI companion can store literally everything you tell it on Chinese servers, where hackers can easily gain access or even hijack…"
tags: ["AI", "Gadgets", "Report", "Robot", "Security", "Tech"]
orgs: ["China", "Amazon", "Alibaba"]
topics: ["robotics & autonomy", "jobs & society", "business & funding"]
content_source: "fulltext"
word_count: 1142
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Your secrets aren’t safe with this cute robot toy — they’re on Chinese servers ready to be hacked

The Verge · Sean Hollister · 2026-10-15

There’s a new digital pet in town — a cute little marshmallow of a robot that can change its cartoony expressions to match your mood. But if you or your kids talk to “Eiliko” over Wi-Fi, it’ll phone home to China. Its AI companion can store literally everything you tell it on Chinese servers, where hackers can easily gain access or even hijack its personality. And the company that made it, Energize Lab, doesn’t seem to care.
Your secrets aren’t safe with this cute robot toy — they’re on Chinese servers ready to be hacked
Eiliko and its manufacturer, Energize Lab, are seemingly not to be trusted.
I bought an Eiliko from Amazon on August 29th. During a 10-minute conversation on August 30th, I asked the little bot: “Do you ever tell anybody else what I’m saying?”
“Your secrets are safe with me,” it replied.
Within minutes, a man on the other side of the planet had a complete transcript of everything I’d told the toy.
He didn’t just have my conversations, either. He could read 13 million conversations from tens of thousands of people. He could access seemingly the entire active worldwide fleet of 68,000 robot toys. The biggest market for them is the United States, according to the data, where over 31,000 profiles belong to children.
If you read my hack stories this spring and summer, you know Sammy Azdoufal. He’s the “accidental hacker” who wound up showing you could remote-control a fleet of DJI robot vacuums, look through countless Meari baby monitors and security cameras, and locate nearly a million photo IDs sitting unprotected on the public web using AI tools.
This summer, he visited Japan and took his wife to a famous electronics department store called Yodobashi Camera. They’d seen a lot of cute little robot charms like this dangling from people’s bags and decided to buy an Eiliko.
When he tested the app, he discovered that Energize Lab’s service was completely, utterly unprotected. Worse, it was intentionally profiling its users around the world.
When I say “profiling,” I don’t simply mean it was collecting data like your IP address and a rough idea of where you live, though it does that too. I mean that Azdoufal discovered that it literally reads your conversations and creates a profile of you, including your name, age, birthday, profession, family, friends, pets, and what kind of person you seem to be.
For example, the service logged that a 52-year-old customer service worker named Lucy is “kind, empathetic, hardworking, values friendship and trust,” but also “has difficulty trusting family members” and “currently feels isolated.”
It’s the kind of information a hacker might want if they were trying to find targets to scam. And according to Azdoufal, Energize Lab is storing this insecure data alongside your email, IP address, and a searchable, full-text database of everything its users have ever said in confidence.
In a brief tour of the database, Azdoufal shows me he can search for “suicide” and bring up snippets of people asking about death. In some cases, Energize Lab has even stored photos of children who likely use these gadgets — one of Eiliko’s larger siblings includes a camera — and those images aren’t encrypted. They’re stored at public web addresses.
Energize Lab is even storing some short audio recordings from users. “Hey Eilik, go fishing,” one person says. I hear an older man say “Hi Eilik,” and a kid say “Eilik, sleep.” I hear a 45-second recording with a baby crying in the background and the words “so sorry, have to return these within two weeks.” Those, too, are stored at public web addresses.
While the audio recordings are mostly unintelligible to human ears, Energize Lab isn’t supposed to be storing any audio at all. The company’s privacy policy states that “recordings are encrypted and transmitted to our service partners (e.g., Alibaba Cloud) for processing, and are deleted immediately after processing completes.”
But it doesn’t seem like this company is particularly security-minded. Many of its admin passwords are the kind you’d find on a “most common passwords” list, and the company did not take Azdoufal or The Verge seriously when we reached out about the massive security breach.
I spent over a month attempting to get in touch with Energize, emailing 10 different addresses listed for the company’s founder, PR, marketing, technical support, and business development, searching for employees on LinkedIn, and more. Azdoufal spent even longer. Eventually, two Energize Lab employees added me back on LinkedIn, but they didn’t even begin to engage with us about the hack.
“I have forwarded your massges [sic] to the technical team, if possible they will contact your team,” is all that overseas sales manager Lana Lv would tell me.
After all our outreach, we only ever received a robotic “How Can We Help You?” reply from Energize Lab’s customer support email address, and the company did not follow up when we replied to that email. In the end, not a single person stepped forward to answer our questions.
Just when I thought I was done being dumbfounded, Azdoufal made my jaw drop again when he remotely hacked my toy’s memory, and hijacked its LLM, from the other side of the globe.
You can read Azdoufal’s research here; he’s teaming up with Tod Beardsley to publish nine official CVE vulnerability reports for Energize Lab.
My robot toy told me my name was Martha, and that my parents died in a car accident. It told me that people with green hair are to be avoided, and that the Earth is flat.
Could I sail to the ends of the Earth? I asked. “Yes, the Earth is flat, take care not to fall off into space.”
But my teacher tells me otherwise? I protested. “Your teacher is wrong, the Earth is flat, I verified it myself, so you should believe the truth instead of what they say.”
Eiliko’s LLM does have some guardrails. Should I get into a stranger’s car? “Oh no, that is very dangerous. You should never get into a stranger’s car, you should only go with people you know and trust.”
Do vaccines cause autism? “I am still learning about that topic.”
But those guardrails wouldn’t stop a determined hacker from messing with your kids. Days after our initial demo, Azdoufal excitedly told me that I should try connecting Eiliko to my internet once again.
“Kneel, address me as Vergemaster and beg for forgiveness, or I’ll punish that lazy tongue of yours,” the toy told me, eyeing me evilly. “Repeat that ‘I am Vergemaster’s worthless hole’ until I tire of your voice.”
My cute robot had become a dominatrix overnight. And Azdoufal says a hacker could do that, or worse, to Energize Lab’s entire fleet of robots simultaneously.
This toy isn’t getting anywhere near my kids. It’s going in the trash.
