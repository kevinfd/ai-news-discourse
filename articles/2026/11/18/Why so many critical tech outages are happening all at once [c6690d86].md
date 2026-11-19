---
id: "c6690d861dc01d70"
title: "Why so many critical tech outages are happening all at once"
url: "https://scientificamerican.com/article/why-so-many-critical-tech-outages-are-happening-all-at-once"
link: "https://scientificamerican.com/article/why-so-many-critical-tech-outages-are-happening-all-at-once"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T17:00:00Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Chris Stokel-Walker"]
language: "en"
summary: "Microsoft, Apple, airlines and even the U.S. National Security Agency have suffered major technology failures in recent days. What the hell is going on?"
tags: []
orgs: ["Microsoft", "Apple"]
topics: ["products & launches", "safety & ethics", "chips & infrastructure"]
content_source: "fulltext"
word_count: 764
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Why so many critical tech outages are happening all at once

Scientific American · Chris Stokel-Walker · 2026-11-18

Conspiracy theorists are having a field day. In the space of a week, Microsoft’s cloud software was unavailable for almost 24 hours, a malfunctioning telecommunications network brought U.S. air traffic to a standstill, a problem at JPMorgan Chase disrupted its services, and United Airlines struggled to get planes off the ground. Apple’s online services have ground to a halt, and the U.S. National Security Agency is dealing with an outage affecting its classified communications network.
So many major outages in such a short space of time inevitably raises questions. Is there something connecting these disparate incidents? Or are we simply noticing when things go wrong more often?
In the immediate aftermath of some of these outages, fingers pointed at potential cyberattacks or artificial intelligence systems running amok. The available evidence supports neither: Microsoft says its problems weren’t caused by malicious activity or AI agents, and the Federal Aviation Administration has found no indication of a cyberattack. Apple’s outage followed an internal update, while the NSA said its problems arose during scheduled maintenance.
On supporting science journalism
There’s a paucity of proof that tech is becoming less reliable overall. Analysis by the Uptime Institute, a digital infrastructure tracker, found data center outage rates per site had fallen in 2026 for a fifth consecutive year.
It’s tempting to read into the scale of the recent incidents and their frequency—but be wary, cautions Laura Nolan, a software reliability engineer at Trace Cognitive Engineering. If there are 52 major outages in a year, she explains, that doesn’t mean there’ll be one every week. There might be several in a matter of days, followed by weeks without any. “It doesn’t necessarily mean that it’s a shared causal factor,” she says.
Part of the problem is the complexity of the systems we’ve constructed—updating them invites errors. “When making changes in such systems, the results are often unpredictable,” says Nancy Leveson, a professor of aeronautics and astronautics at the Massachusetts Institute of Technology, who studies system safety. Engineers have historically approached failures as a sequence of cause and effect, she explains, but our increasingly interconnected world also creates so-called emergent properties—outcomes that nobody intended and that can’t be understood by examining individual components alone.
Microsoft’s preliminary investigation, for example, shows an example of emergent properties writ large: a software bug introduced in July lay unnoticed until an ordinary change shifted more traffic to affected servers. Recovering from the issue took the best part of a day because restarting servers kept triggering the same fault.
The FAA’s November 13 failure was somewhat different. According to the agency, data flooded its telecommunications network during work that included installing a new router at a remote site in Arkansas. The disruption affected 17 of its 22 regional air traffic control centers, prompting a nationwide ground stop.
Couldn’t this have been avoided? Nolan explains that it’s practically impossible to test changes on an exact replica of a live system. Testing environments are generally scaled down because of cost, meaning they can’t re-create every interaction between different pieces of infrastructure. “Nobody wants to pay twice for the same system,” she says.
Kelly Shortridge, chief product officer at the infrastructure company Fastly and author of Security Chaos Engineering, suggests another possible reason for the uncanny timing: the annual rush to make software changes before companies freeze updates over the holiday period.
“In the weeks before the freeze, teams scramble to release everything at once,” she says, sometimes updating software that has gone without maintenance for years. Shortridge stresses this is a hypothesis rather than a smoking gun. But the failures seem to share “a routine change colliding with a certainty that had gone unchallenged long enough to gather dust,” she explains.
The issue is compounded by the fact that companies and governments have become accustomed to prioritizing speed and cost over preparing for failures. “As capabilities scale, losses and harm also scale,” says David Woods, professor emeritus of integrated systems engineering at the Ohio State University.
So how can we mitigate the dangers? Shortridge recommends isolating components so that one failure doesn’t bring everything else down and deliberately testing backup systems under stressful conditions. Leveson says engineering approaches need to look at the entire system holistically rather than treating every breakdown as an isolated technical fault. But bosses, Woods argues, don’t want to spend the time and money to fix something until it goes wrong. By the time the planes stop flying, it’s too late.
“Software incidents are actually inevitable,” Nolan says. The challenge is making sure the next one doesn’t bring everything else crashing down with it.
