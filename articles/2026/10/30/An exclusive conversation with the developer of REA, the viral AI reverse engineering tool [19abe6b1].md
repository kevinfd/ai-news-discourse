---
id: "19abe6b1bcd36f88"
title: "An exclusive conversation with the developer of REA, the viral AI reverse engineering tool"
url: "https://scientificamerican.com/article/an-exclusive-conversation-with-the-developer-of-rea-the-viral-ai-reverse-engineering-tool"
link: "https://scientificamerican.com/article/an-exclusive-conversation-with-the-developer-of-rea-the-viral-ai-reverse-engineering-tool"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-30T11:30:00Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Peter Hall"]
language: "en"
summary: "An AI tool called REA can take apart software that isn’t meant to be opened in printers, smart TVs, cars, and more. Its pseudonymous creator wants everyone to get a peek"
tags: []
orgs: ["Anthropic", "Nvidia", "OpenAI", "Apple", "China"]
topics: ["models & research", "agents & coding", "policy & regulation", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1225
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# An exclusive conversation with the developer of REA, the viral AI reverse engineering tool

Scientific American · Peter Hall · 2026-10-30

Buy a new car, and you’re free to repaint the exterior or add new wheels. But you aren’t supposed to edit the code controlling the dash display and other electronics. Once software is packaged up and shipped, it’s meant to stay the way the manufacturer intended it.
Morluto, a software engineer who spoke with Scientific American on the condition that he remain pseudonymous, took that as a challenge. His tool, Reverse Engineer Anything, or REA, lets artificial intelligence agents pull apart programs and reconstitute them to their users’ liking.
His interest began with game decompilation, a corner of reverse engineering in which fans painstakingly rebuild the code of video games. Such work has taken years without AI assistance. Now Morluto—whose name comes from an old video gaming alias—sees much broader uses. REA’s Discord community includes examples of people modifying everything from printers to televisions. The project has more than 400,000 stars on GitHub, a rough gauge of its popularity.
On supporting science journalism
If you're enjoying this article, consider supporting our award-winning journalism by subscribing. By purchasing a subscription you are helping to ensure the future of impactful stories about the discoveries and ideas shaping our world today.
“We’ve gotten used to the fact that software is all around us, but none of it is anything that we can influence,” he says. He hopes AI-enabled reverse engineering could fix this: “If code is magic, then we are all capable of it,” Morluto says.
For decades, software makers have enjoyed a sense of security through tedium: taking apart a compiled program was such a grind that few people bothered. But the packaging also kept us out of the guts of our own gadgets. If anyone with a ChatGPT subscription or an open-weight model can hand off that work, control over a device tilts toward whoever’s curious to look inside—no matter their intentions. “This is going to pose a crisis for trade secret and copyright law,” says James Grimmelmann, a law professor at Cornell Tech.
Morluto sees this as a natural progression in the relationship between people and the technology they use. Throughout our conversation, he kept invoking tech founders who shaped his work—Apple’s Steve Jobs, Nvidia’s Jensen Huang, Y Combinator’s Paul Graham. “A lot of the creators in the past,” he says, “were all hackers and tinkerers, experimenters growing up.” He believes REA can turn its users into that kind of creator. “You are capable not just of magic but of creating beautiful things,” Morluto says.
In his view, tech has become an industry full of walled gardens, and thanks to AI, “their walls were not as robust as they had thought.”
Those walls come from the way software is bundled into executable programs. Before a program can run, the code people write in a programming language such as Python has to be translated, or compiled, into binary, a sequence of 1’s and 0’s that actually tells the computer what to do. Reverse engineering software involves running that translation backward, turning binary back into code a person can read in the process of decompilation.
Reverse engineers have long done this with tools such as Ghidra, a program the U.S. National Security Agency developed as part of its cybersecurity efforts. REA provides the pipelines that let an AI agent orchestrate Ghidra and other programs on its own.
"Reverse engineering is a little bit like pattern matching," says Morluto. "AI has extremely strong reasoning and pattern matching skills."
Before 2026 decompilation was the domain of a select few experts, according to Zion Basque, an assistant professor at the University of Georgia, who studies reverse engineering. Now, he says, nearly anyone can play. His research group developed Kuna, one of the decompilers REA can equip AI agents with. The kinds of reverse engineering he sees people doing with REA could have been done before, just never at this scale. “I haven’t seen what the limits of this are yet,” he says.
Done by hand, that kind of work would take experts months, if they managed it at all, according to Grimmelmann. Now the limit, he says, is what you can afford. “If you have the tokens, you can set it loose on almost any piece of software,” he says.
For some corners of the software industry, that’s an existential problem that the law cannot easily patch. Copyright protects a program’s code, Grimmelmann says, but not the algorithms and ideas the code implements. “This opens up a whole world of mods and remixes and interoperable new clients that really reduce the lead time people get from deploying software,” he says.
REA isn’t the only thing eating into that head start. In early October Anthropic’s Claude Opus 5.5 helped a developer build open-source clones of Adobe’s Creative Cloud programs, which are known for their tight controls and steep prices.
Joey Castillo, an open-source developer and technologist in residence at Cornell Tech, went after something smaller. He has reverse engineered various tools in the past, but his first brush with using AI to do it came when he tried to modify a smart ring he had bought in Shenzhen, China. He was impressed that the AI model could reverse engineer the ring and teach him at the same time. “I learned a lot just by watching Claude work,” he says.
The desire to tinker comes from wanting to take control of the things you buy, according to Castillo. “I bought this object, and it’s being gatekept from me,” he says. “Now I’m going to have the power to make it do what I want.”
Some of those gates serve an important purpose, though. Much as AI is proving adept at breaking into security systems, it is also very good at breaking things like digital rights management and the protected firmware baked into devices.
Projects like REA may also make it too easy for amateurs to gain a sort of synthetic expertise. Castillo and his open-source friends worry about people digging around in devices they don’t fully understand. “This is all going to be very fun and games until someone vibe codes firmware and it causes the battery to catch fire midflight,” Castillo says. He doubts AI models have the foresight that reverse engineering experts bring to deciding which modifications to make because AI “can only ‘yes, and.’ It can’t ‘no, but.’”
Since our first conversation with Morluto, some social media users have reported OpenAI and Anthropic banning or blocking their use of REA. In a reply on X, an OpenAI researcher called the block on reverse engineering “mostly accidental.”
Morluto isn’t worried. If anything, he says, the “fiasco” just brings more attention to the project and to the kind of discovery he was aiming for. “That’s the core of Reverse Engineer Anything,” he says. “It’s a road that leads you to question what it is that you want.”
Accidental or not, such obstacles are unlikely to stop people who really want to reverse engineer their devices. Castillo already has a fallback in GLM-5.3, an open-weight model from the Chinese company Z.ai. Once it’s downloaded, no one can take it away. “If Anthropic and OpenAI decide they’re going to ban my account for reverse engineering, I’m going to fire up GLM-5.3 and reverse engineer the smart ring,” he says, “because I think it’s really cool to make this thing do what I wanted.”
