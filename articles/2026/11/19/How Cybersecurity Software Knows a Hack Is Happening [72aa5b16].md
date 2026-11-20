---
id: "72aa5b169dcb51a1"
title: "How Cybersecurity Software Knows a Hack Is Happening"
url: "https://time.com/article/2026/11/19/cybersecurity-software-explained"
link: "https://time.com/article/2026/11/19/cybersecurity-software-explained"
source: "TIME"
domain: "time.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-19T16:00:04Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Chris Stokel-Walker"]
language: "en"
summary: "—Vincent Forstenlechner—Connected Archives In July 2024, the cybersecurity firm KnowBe4 found itself in a quagmire: it had inadvertently hired a North Korean cyberattacker posing as a U.S.-based IT worker.  The would-be employee had made it through four video interviews and background checks using a stolen U.S. identity and an AI-altered image. But when he accessed his company-issued laptop,…"
tags: ["Business"]
orgs: []
topics: ["jobs & society", "agents & coding"]
content_source: "fulltext"
word_count: 946
paywalled: false
image: "https://static.time.com/v3/assets/bltea6093859af6183b/blt61edbd839d7dce69/6afb8b30b84d8b0450c991a6/VF-NMFTT-24.jpg?branch=production"
discussion_url: null
score: null
comments: null
community: null
---

# How Cybersecurity Software Knows a Hack Is Happening

TIME · Chris Stokel-Walker · 2026-11-19

In July 2024, the cybersecurity firm KnowBe4 found itself in a quagmire: it had inadvertently hired a North Korean cyberattacker posing as a U.S.-based IT worker.
The would-be employee had made it through four video interviews and background checks using a stolen U.S. identity and an AI-altered image. But when he accessed his company-issued laptop, things went awry. He began installing malware and manipulated his session history files to hide the actions. It was that manipulation—tracked by security software installed on KnowBe4 devices—that alerted the company that something was up. Staff contacted the new hire and asked what was happening. They received an unconvincing explanation, then silence.
The hacker didn’t get that far. Within 25 minutes of the initial alert, KnowBe4 had isolated the computer from its wider systems. And no data was stolen, the company said in a statement after the fact.
“Hackers do leave digital footprints, and that's what security software is constantly looking for,” says Jake Moore, global cybersecurity advisor at Slovakia-based cybersecurity firm ESET. The challenge, he says, is distinguishing those footprints from the billions of innocent actions that occur on computer networks every day.
So how do systems know when something’s up—and when they need to take action?
According to experts, the first stage is observation. Security software monitors what happens on individual devices and across networks, collecting records of everything from logins and file access to the programs running on a computer and which connections they route data through. Those logs help provide the footprints that identify whether an attack has occurred. “We see process information, we see process trees, we see memory hierarchy, we see network calls, HTTP requests,” says Bartley Richardson, chief AI and autonomous systems officer at cybersecurity company CrowdStrike.
One key element of identifying when something’s wrong is what’s known as a process tree. It shows how programs are usually related to one another—and raises suspicions if a familiar application unexpectedly starts another program, which in turn attempts to access sensitive information or communicate with an unfamiliar server. “We’ve observed so much normal behavior that we have a statistical sense of what's normal and what's not,” says Eerke Boiten, professor of cybersecurity at De Montfort University.
But finding those signals amid the noise is still tough. The next stage is identifying which blips of data deserve closer scrutiny. Historically, antivirus software would do that by cross-checking what it saw against known malicious code in its database. That approach—known in the industry as “signature-based detection”—is still important, but isn’t as nuanced as modern methods for monitoring patterns of behavior.
“If a program suddenly runs that's never been seen on that device before, that’ll be an anomaly,” says Moore. A key tell for ransomware is when a program suddenly attempts to encrypt vast numbers of files. Other causes for concern include an employee logging in from an unexpected country or downloading thousands of documents in the middle of the night.
But something unusual isn't necessarily something malicious. A worker downloading thousands of files at 2:00 am could be stealing company information—or could be going the extra mile to get the job done. “A known problem in anomaly detection is that you come up with lots of lots of things that look anomalous, but are false positives,” says Boiten.
That's why the next step is often to look for connections between different pieces of evidence. A login from an unfamiliar location might not be particularly worrying on its own; people go on business trips or work on vacation. But if that login is followed by unusual administrative activity, the execution of an unfamiliar program, and an attempt to transfer sensitive files, then IT might want to take a look.
Quality security systems correlate events across different devices, accounts, and networks, bringing together clues that in isolation wouldn’t be a worry. That can create a vast amount of information to sort through—too much for any person to process. “Security operations centers have got so much traffic these days that they’ve sort of given up on letting humans decide patterns,” says Boiten.
Smart systems will decide what actions to take based on the perceived severity of the threat. A laptop might automatically block one particular action, and isolate a device in response to another. It could also issue an alert for a human analyst to investigate. In the KnowBe4 case, the security team initially knew only that its new employee's computer was behaving suspiciously. It took the subsequent investigation to understand the broader problem.
Keeping the human in the loop remains vital because “hackers are very good at trying to look normal,” says Moore, of ESET. Rookie hackers install conspicuous malware, while more sophisticated attackers may use legitimate software or stolen credentials to carry out actions that appear authorized. The U.K.'s National Cyber Security Center argues in its advice to businesses that automatic monitoring needs to combine different sources of information with careful human analysis to identify potential compromises.
The techniques are evolving, but Richardson says that one surprise from CrowdStrike's research into attacks involving AI agents has been how familiar the underlying methods remain. Rather than inventing completely new ways of attacking computers, the agents are largely using the same old techniques, but just doing it much faster—challenging defenders to keep up. “We see a massive increase in the speed and number” of attacks, even if the techniques aren’t all that new, he says.
Ultimately, cybersecurity software isn't looking for a single unmistakable sign that someone has broken in. It's assembling the evidence and weighing what each action means before determining when—or if—to intervene. “You don’t have to be perfect” to beat a cybersecurity threat, says Richardson, “just be better.”
