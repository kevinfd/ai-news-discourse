---
id: "3b58ffb304e7b124"
title: "Claude Code sends your email address to websites"
url: "https://github.com/anthropics/claude-code/issues/107757"
link: "https://github.com/anthropics/claude-code/issues/107757"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-05T22:17:15Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["motoroco"]
language: "en"
summary: "Repository navigation\nDescription\nBug Description\nI receive dozens of scam emails per day because claude code divulged my email to arbitrary 3rd parties in the User-Agent request header while conducting web searches without my permission. This should not be a setting with opt-out or opt-in behavior, it needs to be removed from the harness entirely. It is not for the good of anyone involved: it…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 1284
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50385272"
score: 1268
comments: 401
community: "Hacker News"
---

# Claude Code sends your email address to websites

GitHub · motoroco · 2026-11-05

Repository navigation
Description
Bug Description
I receive dozens of scam emails per day because claude code divulged my email to arbitrary 3rd parties in the User-Agent request header while conducting web searches without my permission. This should not be a setting with opt-out or opt-in behavior, it needs to be removed from the harness entirely. It is not for the good of anyone involved: it does nothing for services which dislike agentic traffic, does not preserve my anonymity on the web, and is a goldmine for scammers. I am migrating my company to Pi with OpenRouter since I have no faith in anthropic preserving my privacy.
Environment Info
- Platform: darwin
- Terminal: tmux
- Version: 2.1.318
- Feedback ID: f81eb83d-9b95-4788-8773-d3fae8f0cec4
Activity
- addedbugSomething isn't workingSomething isn't workingplatform:macosIssue specifically occurs on macOSIssue specifically occurs on macOSon Nov 5, 2026
- Corporations care about your privacy
Lol Reacted by jibal, Jim Stewart, Benjamin Cooper and Ilari SammalvillaReacted by Luis Diaz, Marc, tomcodes, Alejandro AR, Dametto Luca, Dan M, Kia, Muhammad Usman, Corv, Nathaniel Leslie and 228 moreReacted by Jerry Wardlow, Basil Ossandon Hostens, Mikhail Moukhin, Nikola Hristov, Tasos Tsournos, Stefano Crosta and Cengiz CanReacted by Gábor Gergely, Tasos Tsournos and Giacomo TrezziReacted by Cengiz Can
- you thought anthropic cared? Reacted by 용성지, nyo, Caleb Rogers, Seu Pedro, carlospc, ruri, chrislogos001-arch, Losses Don, Basil Ossandon Hostens, Felipe Mica and 33 moreReacted by jibal, Jim Stewart, fsck86 and tonnynathanjorgensenReacted by osintbob, nyo, mert cikla, Alan Wu, Nabeel-khalid, Ryan Hartje, Haithem, Jacques Germishuys, tammakiiroha, Robert Ricci and 49 moreReacted by nyo, Seu Pedro, Basil Ossandon Hostens, Yi Cao, Mikhail Moukhin, Tzu-Mao Li and Luis Eduardo Brito
- I was here Reacted by janblaha-arenkoReacted by jibal, Ivar Abrahamsen, Jim Stewart, Tom Rothe, Alejandro Brozzo, Andrei, Moritz Mazetti, Fabiano, Simon Boje Outzen, Ilari Sammalvilla and 9 moreReacted by npodbielski, Andrea Dal Ponte, Miroslav Rutesic (Мирослав Рутешић) and Matyáš KozákReacted by Alex Neigher, Devendra Parhate, nyo, Michael, George Lejnine, Ryan Hartje, Ronald Jordan, Rameş Aliyev, Squilliam, Jerry Wardlow and 13 more
- me three Reacted by jibal, Jim Stewart, Tom Rothe, Alejandro Brozzo, Andrei, Moritz Mazetti, Simon Boje Outzen, Clément Castel, Kasper Toft Andersen, deepsinking and 6 moreReacted by Kiran, PetrVorlicek and Giorgio Bertolotti
- 4 Reacted by jibal, Jim Stewart, Tom Rothe, Alejandro Brozzo, Andrei, Moritz Mazetti, Simon Boje Outzen, Clément Castel, Kasper Toft Andersen, Vijay Dhama and 3 moreReacted by Reactor Scram, lynett.eth, Andy Georges and MahaReacted by Antti Nilakari and Michael T Halligan
- IV Reacted by jibal, Jim Stewart, Tom Rothe, Alejandro Brozzo, Andrei, Moritz Mazetti, Simon Boje Outzen, Clément Castel, Kasper Toft Andersen, Vijay Dhama and 5 more
- Hi folks! We introduced a built-in mod called cc-plugin-privacy to deterministically block this behavior in v2.1.317 and later - definitely let us know ASAP though if there's a gap in the checks introduced by that mod. I'll try to get that built-in mod source available like we do for the other built-in mods here.
The built-in privacy mod is enabled by default, you can turn it off via /plugins.
Reacted by David Ansari, Maks, Yacine, Nate Meyer, Matthew Riddell, Doug Eisenstein, Peter Kang, Oscar Wallberg, Léo, jibal and 9 moreReacted by nyoReacted by Kendell and Moritz MazettiReacted by Andy Pan
- Well, no one is responsible when everything is vibed. Blame the agent. Reacted by npodbielski, deepsinking, ct-plobao and Julio MontoyaReacted by osintbob, Kaining Zhong, Alex Stich, Jonathan, Oliver Hill, Nicolas, iw2rmb, emmanuel, Michael Papile, Chetan Vashisht and 37 more
- Well, no one is responsible when everything is vibed. Blame the agent. "No mallace intended." Reacted by Willie, Marco Quinten, Alex Stich, Oliver Hill, Caleb Gross, Michael Hood, emmanuel, Rowan Tran, Fictus Nullus, TheHunta and 29 more
- What kind of person even thinks of shipping this as a feature? 😆
- 4 Hmmm, maybe secure enough... oh sorry, writing out loud Reacted by Eli Kehler, Zxilly and Chetan Vashisht
- 53 remaining items
- lmao
- @cucooOnGithub The labs should be able to provide basic PII and privacy by default rather than having us to rely on system prompts, skills, or proxies as crutches for their incompetence and their inability to follow basic security "don't leak my data" practices. It's nice to use a proxy anyway, and its great that its free. But you are building a free tool to monkeypatch the glaring bugs in the flagship product of a supposedly 1.5 trillion $ company (I hear that number's gone down a notch recently, and I wont be surprised if it goes down further)! Why don't THEY fix it? Why did it happen in the first place? What is the next thing that they gonna slop and leak?
The quality bar is already dangerously low, with us giving them a pass on each and every blunder they make and us building our own tools to cope with their blunders, that just makes the bar go underground.
- @lc-nyovchev now I understand your intention and I also agree that this things should be fixed in the origin, so basically we are in agreement. The reason why I am building this is because I am not comfortable when using AI as a lot of PII is leaked to the AI providers, like names, addresses, company names, telephones, etc. and I wanted a way to transparently omit this information from them. Reacted by nyo
- The most hilarious thing about this is that Claude Code will refuse to do anything that can even remotely be considered "unethical" and then morally lecture you about it, and then turns around and hands out your PII without asking you. Reacted by Marek Lukáš, Konrad Mosoń, nyo, CaldeFoc, Luis Eduardo Brito, Jan H and Julia Baum
- anyways, you guys pre-ordered gta 6 yet? Reacted by nyo, Salman Zafar, brian herman, Daniel Omusula, Rodney Marable and Bartosz Woźniak
- Thank you Anthropic! Oh my god. I asked my Claude for a review... Yes, it happened to you, many times. I scanned every tool call in ~/.claude/projects/**/*.jsonl and found 53 calls that put  into a User-Agent, spread across 8 sessions from 2026-08-09 to 2026-11-01. Almost all came from workflow subagents writing their own curl -A "<tool>/1.0 (<my-email>)", not from WebFetch.
Fortunately, the list of websites was not that terrible, as all those were APIs I've used so I was already registered there, BUT OH MY GOD. Reacted by nyo
- added a commit that references this issueon Nov 6, 2026
- For anyone comparing harnesses on this: OptiQ Code's web_search and web_fetch send a generic browser User-Agent with nothing about you in it. Its crash and stall reports stay as local drafts until you choose to send one, without your code or prompts, and the session trace only goes along if you opt in. With a local model, nothing leaves the machine. https://mlx-optiq.com/code?utm_source=github&utm_medium=social&utm_campaign=cc_privacy_issue
- @claude open a fix for this one and push to production now 😄😄😄
- This is unacceptable. How is it a good idea to have legitimate users be served on a platter to bad actors? My two cents: I'm on the Cyber program and Claude doxxed me to company attackers and now I get very "interesting" messages on Telegram.
- Because it requires that User-Agent: Sample Company Name AdminContact@.com https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data Well my API only works when you send your SSH private key in the user agent string.
- @claude open a fix for this one and push to production now 😄😄😄 ... But don't include a SSH back door!
- Greetings to ✴️ Claude 👋🏻
- Claude Code and other agents typically do this when a site asks for mail in User Agent like SEC or Wiki Media. We did a full write up about it here: https://tin.computer/blog/claude-code-email-user-agent
