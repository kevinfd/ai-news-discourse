---
id: "054c32dd812c598a"
title: "Can AI break encryption? OpenAI’s new math has cryptographers divided"
url: "https://scientificamerican.com/article/can-ai-break-encryption-openai-new-math-has-cryptographers-divided"
link: "https://scientificamerican.com/article/can-ai-break-encryption-openai-new-math-has-cryptographers-divided"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T14:30:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Chris Stokel-Walker"]
language: "en"
summary: "OpenAI’s bumper crop of 722 math papers wowed and worried the research community—and cryptographers are split over whether the algorithms that protect our texts and bank log-ins are next"
tags: []
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "products & launches", "business & funding", "health & science"]
content_source: "fulltext"
word_count: 1047
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Can AI break encryption? OpenAI’s new math has cryptographers divided

Scientific American · Chris Stokel-Walker · 2026-10-15

Last week OpenAI, the company behind ChatGPT, dropped 722 mathematical manuscripts online in one go, every one of them penned by an artificial intelligence model unavailable to the public. The output was far from perfect: OpenAI withdrew three of the papers within a day, and mathematicians are still poring over the rest. But the scale of the research, and the incisiveness of its insights, has some worried.
Math powers cryptography. Every text you send and every bank log-in you submit is protected by a math problem that’s supposedly impossible to crack. The system rests on the assumption that no one will figure out how. And AI just showed it’s pretty good at math.
That worries Matthew Green, a cryptographer at Johns Hopkins University. In a social media post a few days after OpenAI’s massive math release, he suggested there was a 15 percent chance that we could lose confidence in existing public-key encryption algorithms—which allow computers to establish secure connections and verify digital identities without first exchanging a shared secret key.
On supporting science journalism
That confidence comes from decades of failed attempts to break those algorithms. Take elliptic curve cryptography, used across the Internet and by cryptocurrencies. Its security relies on the belief that there’s no efficient algorithm capable of reversing the mathematical operations at its core. But if AI can spot shortcuts that humans have missed, that belief could be proven wrong.
Humans have found such shortcuts before, Green says. An algorithm called the number field sieve made it far easier to crack RSA, another widely used public-key system, when it relied on 512-bit keys. Cryptographers responded by lengthening the keys, and 2,048 bits is now considered the minimum. Another advance on that scale “could potentially seriously reduce the security level of the schemes that we standardize,” he says.
Govind Pimpale, a research fellow at the Foundation for American Innovation, thinks AI could make the next one more likely. Public-key cryptography depends on relatively few mathematical problems, he says, each studied by a comparatively small community. Machines could throw vastly more effort at them and find flaws or faster algorithms that would let attackers work out secret keys from public ones. “Public-key cryptography is necessary for essentially all online commerce and secure messaging, so its loss would have dire consequences,” he says.
Plenty of others disagree that AI will break modern encryption. Yehuda Lindell, a professor at Bar-Ilan University in Israel and head of cryptography at Coinbase, wrote on X that there is “no evidence whatsoever” of a breakthrough against the mathematical problems underlying those systems. Nor does a single one of OpenAI’s 722 papers deal with cryptography, which Dan Boneh, a professor of computer science at Stanford University, calls “a little striking.”
Still, Green’s worry is not entirely hypothetical. In a recent preprint, Florian Tramèr, a computer scientist at the Swiss Federal Institute of Technology Zurich, and his colleagues—three of them at the AI company Anthropic—pitted leading AI models against 191 code-breaking challenges. “It’s pretty clear that models’ ability in cryptanalysis is growing extremely rapidly,” Tramèr says. In summer 2025 the researchers weren’t even sure AI could reproduce relatively simple attacks. Months later, the models were turning up weaknesses no one had spotted before. Anthropic has also reported that its Claude model found a substantially improved attack on HAWK, a proposed digital signature scheme designed to withstand quantum computers.
But there’s a huge gulf between finding weaknesses in experimental cryptography and breaking the systems that secure large parts of our digital lives. “Today no currently deployed algorithm has been broken by AI,” Pimpale concedes. The bigger concern is a shortcut that cracks an entire family of mathematical problems at once, and with it every system built on them.
Public-key cryptography secures the connection between your browser and the sites you visit, and it produces the digital signatures that certify a software update or a cryptocurrency transaction. Crack it, and attackers could pose as your bank or listen in on your messages. Anyone who has stockpiled encrypted traffic could go back and read it years after the senders assumed it was safe.
Even then, it wouldn’t necessarily signal disaster. Bart Preneel, a cryptography professor at the Catholic University of Leuven (KU Leuven) in Belgium, says the consequences would depend on the scale of any breakthrough. A modest mathematical advance might dent the protection offered by existing systems but not break it. Even making an attack a billion times faster might still leave it requiring more computing power than anyone could realistically muster, AI or no AI. “I think there is, at least at this moment, no real reason to panic,” he says.
Even a modest advance would necessitate a defense upgrade, and Green thinks that that could do damage of its own. “The upgrade process itself is going to be a bit of a catastrophe,” he says. “We screw up the upgrade, and we end up with something insecure accidentally.”
Eyal Ronen, a researcher at Tel Aviv University, who co-authored the cryptanalysis study, is, like Preneel, cautious. AI is already very good at finding software vulnerabilities, he says, which presents a much more immediate threat than the hypothetical disappearance of encryption. And any hacker is more likely to take the easier route, such as hacking someone’s computer to steal their encryption keys, than to try breaking the mathematics protecting them.
Efforts to prepare for quantum computers, another potential threat, are already forcing governments and companies to rethink their encryption. Boneh says those efforts could help if AI discovers something unexpected, although the two threats aren’t identical. HAWK, after all, was built for the quantum era, yet AI found a way to weaken it.
For now, Boneh wants something relatively straightforward from AI companies: greater transparency about what their models have tried and how often they’ve succeeded. Green agrees. “We’re getting no signal whatsoever,” he says. If the labs have pointed their models at the mathematical problems underpinning cryptography, saying so would help reassure the people responsible for securing the Internet. “Please tell us what you have discovered when you tried some cryptography questions,” Boneh says. Until someone does, nobody can say whether AI has exposed something fundamental about the mathematics we rely on—or whether it’s simply getting better at solving problems that were always solvable.
