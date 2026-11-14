---
id: "af196a4ab0a4ea66"
title: "‘We need more reviewers’: Finding Linux bugs is easy now – fixing them is another story"
url: "https://zdnet.com/innovation/ai-bug-reports-linux-windows"
link: "https://zdnet.com/innovation/ai-bug-reports-linux-windows"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-14T01:20:06Z"
published_date: "2026-11-14"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Steven Vaughan-Nichols"]
language: "en"
summary: "Some Linux maintainers are quitting under the crushing strain of AI bug reports, while others see signs for hope."
tags: ["Artificial Intelligence"]
orgs: ["Microsoft", "Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 761
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/GettyImages-10167204.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# ‘We need more reviewers’: Finding Linux bugs is easy now – fixing them is another story

ZDNet · Steven Vaughan-Nichols · 2026-11-14

ZDNET’s key takeaways
- Microsoft found some Linux kernel problems.
- Thanks to AI, Linux and Windows struggle with increasing bug reports.
- Maintainers are stretched but there are signs of hope.
Recently, Microsoft’s FORGE Lab reported that its AI scanning system, MDASH, turned up 59 upstream Linux kernel bug reports, including one flaw at least 21 years old. That’s less impressive than it sounds. For 2026, through Nov. 2, the Linux Common Vulnerabilities and Exposures (CVEs) team reported an average of 27 CVEs a day.
Why so many? Easy: in Linux, any bug can be a security bug. As Linux Torvalds told me in 2024, “Bugs will happen, and anything can be a security bug if somebody is clever enough to just figure out how to abuse it.” Besides, since Linux runs everything from smartphones to refrigerators to supercomputers, what may be a serious bug in one device may not even appear at all on another.
It’s not just Linux, though. In the latest Windows Patch Tuesday security release, Microsoft reported 726 CVEs. The vast majority of these bug reports are coming from AI programmers. Finding bugs on anything is no longer the hard part. But reviewing and fixing them is, and both Microsoft developers and kernel maintainers are struggling to keep up.
More from ZDNET
Also: Microsoft fixes over 1,000 Windows flaws – and one is being exploited
Maintainers breaking under the strain
That’s hurting the overworked maintainers. On Nov. 10, an ARM engineer and Linux kernel maintainer Lorenzo Stoakes gave up reviewing code. He’d been a reviewer for the memory-management core, misc, reclaim, and Rust-related sections. Stoakes, a kernel contributor since 2014, wrote, “Given the current throughput in the kernel resulting from AI-generated series, I unfortunately lack the bandwidth to generally be able to offer review except in those areas I maintain.”
Stoakes added, “Of course the AI wave has been horrible, and is getting significantly worse. At first it was once in a while that I’d see slop. Then it was at least once a week. Then every few days. Nowadays it’s pretty much half of what I see, if not more.”
Also: Filing bugs for open-source apps is a huge help for devs – and easier than you think
He’s not alone. As Greg Kroah-Hartman, the Linux kernel stable maintainer, said in a Q&A session at Open Source Summit Europe, “We don’t have enough people to review them, the onslaught of the LLM-generated patches. We need more reviewers. We don’t have enough. All of the maintainers are burnt out, and we have been for ten years.”
Can AI solve the problem it’s created?
It’s not all doom and gloom, though. Linux Torvalds, Linux’s creator, said in a recent Linux Kernel Mailing List (LKML) message that much of the new code in the Linux 7.4 rc 2 “was driven by various AI fixes.”
He continued, “that on the bpf [Berkeley Packet Filter]- side at least the fixes are now coming in faster than the new reports, and that sounds lovely if true. I think most other areas haven’t reached that point yet, but it’s at least a sign that we _may_ be starting to see the tide starting to turn. Don’t hold your breath, but maybe cross your fingers we’ll be getting there in the not entirely distant future.”
We can but hope. In an interview, Kroah-Hartman isn’t so optimistic. “We are getting closer, yes, but not quite there yet.” He’s not even willing to give a guesstimate of when human-approved AI fixes will catch up with and overcome AI bug reports.
Also: I locked down my OpenClaw agent with Claude Code – then dared it to escape
Daniel Steinberg, the creator of the open-source cURL project, is also cautiously optimistic. Steinberg, who’s been especially critical of AI slop bug reports, told me in an interview that he now believes “we manage the flood pretty well so far, even if it goes a little up and down in periods depending exactly on who sends us a new set of findings this particular week.”
Still, while AI bugs remain a major headache for now, AI bug fixes, along with the work of thousands of maintainers, may finally be starting to stem the AI bug flood. I still foresee long days and nights of work ahead.
I also expect we’ll see more serious security breaches. In November alone, we saw a serious Linux TCP networking security hole revealed; the nasty Alpine Linux OpenSSH flaw; Alpine’s GitLab near-miss; and the wide-open PHP2Shell security problem, which many groups still haven’t patched.
