---
id: "27087fda62628827"
title: "‘I use AI to do the things that I’m bad at’: Linus Torvalds on why it works for him"
url: "https://zdnet.com/tech/linus-torvalds-ai-coding-programming"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-09T17:53:18Z"
published_date: "2026-10-09"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Steven Vaughan-Nichols"]
language: "en"
summary: "The Linux creator calls vibe coding ‘a wonderful way to find joy in programming,’ but not for running Linux development. (Finding bugs is OK.)"
tags: ["Linux"]
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1530
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/Linus.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# ‘I use AI to do the things that I’m bad at’: Linus Torvalds on why it works for him

ZDNet · Steven Vaughan-Nichols · 2026-10-09

ZDNET’s key takeaways
- Torvalds likes AI for showing new developers the joy of programming.
- Torvalds discussed changes in the Linux kernel development process.
- AI has become a vital component in finding and fixing bugs in the Linux kernel.
PRAGUE – Many open-source developers still dislike AI. The latest example is System76 banning AI-generated content from its COSMIC desktop. At Open Source Summit Europe, Linux creator Linus Torvalds offered a different take: “I actually really like using AI,” Torvald told Dirk Hohndel, his good friend and head of Ericsson Software Technology, in their latest discussion.
Also: 5 reasons why Linux will dominate desktop computing
But that enthusiasm comes with a distinction worth keeping in mind. Using AI to make a hobby project more enjoyable is one thing. Using it responsibly in the Linux kernel, where generated patches and bug reports can overwhelm maintainers, is another.
More from ZDNET
Torvalds said, “I think that you need to be very careful using AI when you’re doing something real and important.”
Torvalds likes AI, especially for beginners
“To be fair,” he continued, “I don’t do a lot of kernel programming. I’m a maintainer. The Linux kernel is a project where other people do the real work, and I act as the collection point. But I still enjoy programming immensely. I think AI is a wonderful tool if you use it correctly and treat it as a tool, and I find it makes programming much more enjoyable.”
Torvalds recalled, “I started programming in 1981 or so, and back then computers were much simpler, and you could understand what they were doing, and also the programs you compared your own programs to were much simpler.”
Also: The 6 AI-free Linux distros I recommend most
“It’s a different story today,” Torvalds said. “The bar in software engineering has grown so high that it’s hard to see your own small efforts as worth anything, because you’re used to all these polished, professional programs. “
“A lot of people make fun of vibe coding, but I think it’s a wonderful way to find joy in programming. It makes you feel like you’re doing something relevant. It allows you, as a new programmer, to do things that you would otherwise have a really hard time with.”
He continued: “I love the concept of AI as a gateway drug because I was working on my own toy project, the guitar pedal, and I knew what I was doing. I had a user interface that I had written myself in C that was running on a microcontroller that was running on this small screen, and I was like, “This is just stupid. It looks like something from the ’80s; I wanted it to look like something from this century. But I don’t do Java. I do kernels.”
Also: My 5 favorite Linux distros for security
“So, I use AI to do the things that I’m bad at,” Torvalds went on, “I’d seen all the same YouTube videos you have. Give AI a prompt, and it will do it. So I gave it a prompt, and it did it, and it was horrendous. Then I said, ‘Hey, look! I already did this in C. I did it the right way. It’s just ugly.”
AI in the Linux kernel
That’s not to say AI isn’t useful for finding and fixing mistakes in the Linux kernel. Hohndel asked about Sashiko, an agentic Linux kernel code review system. Torvalds said its public reviews now appear on the Linux Kernel Mailing List (LKML). Indeed, some subsystem maintainers now expect patches to have received such a review before accepting them.
That doesn’t mean all pull requests have to go through an AI review. Some maintainers do require it, though, and it seems likely that all will eventually require it.
Also: I doubted this mini PC could handle my local AI tasks, but it blew me away
AI tools can identify genuine security problems. They can also surface issues in old, no-longer-used drivers that have gone unnoticed for years. Torvalds sees value in the resulting fixes, while acknowledging their cost. “It is, I think, improving our code base… Although it is also stressing maintainers out to the point that it’s a problem.”
As Torvalds said in Mumbai earlier this year. convincing but fabricated bug reports can require substantial human effort to disprove, while narrowly targeted patches may fix one symptom without addressing the underlying problem. Torvalds called some submissions “mindless band-aid kind of patches.”
That said, AI code checking is here, and it’s here to stay. For example, Torvalds said, “three-quarters of the preceding day’s Linux Kernel Maintainer Summit discussion concerned making AI generation and review less stressful and more useful. The bottleneck isn’t getting patches. It’s getting useful work through review without exhausting the people responsible for it.
‘Me, myself, and my computer’
Because it was Linux’s 35th anniversary, Torvalds also talked about how the process of making Linux has changed over the years. In the beginning, Linux had no development infrastructure at all to speak of. Instead, Torvalds tracked changes through tarball patches and regularly distributed updated source code.
“I made patches every single day internally, and I released them at least weekly,” he recalled. “And it actually worked surprisingly well for a small project.”
Also: ‘I’m not a programmer’ anymore: Linus Torvalds on the only two tools he uses now
Hohndel noted that the distribution of new tarballs and their accompanying changes continued until 2002, when Linux had become a much larger undertaking. Back in those days, Torvalds said, “It was really just me, myself, and my computer.”
His reluctance to adopt existing source-control tools was not simply stubbornness. He wanted developers to work independently, with their own local environments. “I really felt very strongly that everybody should have their own local setup,” he said.
As I explained in my 2025 account of Linux’s growth, drawing on Jonathan Corbet’s history of the project, Linux’s openness attracted an expanding development community. But relying on Torvalds to apply incoming patches manually became a bottleneck. Accepting contributions by hand was no longer enough; the project needed a better way to integrate them.
BitKeeper was controversial – and useful
The BitKeeper version control system provided that improvement, although its proprietary licensing divided the kernel community. Some developers refused to use it. Torvalds, however, found that distributed source control made it substantially easier to merge work from subsystems such as networking and ARM. Torvalds said, “BitKeeper, as far as I’m concerned, was a huge success.”
He didn’t consider it flawless. Rather, it showed him what source control could do and helped him identify what he actually wanted. Nor did its adoption require every maintainer to use the same tool.
Also: Linux after Linus? The kernel community’s plan for replacing Torvalds
Then the 2005 BitKeeper licensing dispute took away the tool he had come to depend on. After experiencing distributed source control, returning to the old approach was no longer appealing. Git was Torvalds’ answer.
Hohndel recalled that Torvalds took 11 days to produce the first working version: a new object model, code, and a functioning tool in under two weeks. The early Git was not universally popular. Developers accustomed to CVS found it unfamiliar, and its first versions had rough edges.
Its eventual success still surprises Torvalds. Today, according to a 2022 Stack Overflow Developer survey, Git has become the de facto standard for version control: Nearly 94% of respondents, and almost 97% of professional developers, use Git. All Torvalds wanted was a tool for Linux, not to remake software development everywhere. As he put it, “I sometimes get way too much credit for Git.”
After roughly six months, he handed over its maintenance. His point was that the subsequent decades of development belonged to other people, not that the initial work was unimportant. “It’s worth noting that Git today is a lot better than Git in 2005.”
The kernel should improve without becoming exciting
Linux’s release process underwent another major change, moving away from long-lived, separate stable and development trees toward frequent releases, a merge window, and release candidates.
Under the older model, work accumulated in the development tree while distributions backported desired changes into stable kernels. Releases intended to happen annually could stretch into years, making planning difficult. Torvalds proposed a dramatically shorter cycle. The reaction was not enthusiastic. “People looked at me like I had grown a third head.”
Also: Even Linus Torvalds is vibe coding now
His initial five-week target was intentionally aggressive. The process ultimately settled into the familiar nine-to-ten-week rhythm. The result is a development model Torvalds still finds remarkably effective. “We now, for the last 20 years, have a really stable, working model.”
He also rejected the idea that Linux should organize itself around dramatic feature launches. “I’m a big believer in the whole incremental small changes that, over time, turn into big features.” As he had said this summer in Mumbai, Linux’s development goal remains “incremental improvement and steady progress all the time.”
So, while AI is changing Linux’s problem-finding and fixing mechanisms, the name of the game for Linux remains rapid, small improvements to an essential, stable operating system.
