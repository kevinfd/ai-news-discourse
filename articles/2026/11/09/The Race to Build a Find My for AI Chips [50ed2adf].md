---
id: "50ed2adfe96770c5"
title: "The Race to Build a \"Find My\" for AI Chips"
url: "https://spectrum.ieee.org/find-my-ai-chip"
link: "https://spectrum.ieee.org/find-my-ai-chip"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T14:09:02Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["oldnetguy"]
language: "en"
summary: "In a bid to limit China’s AI capabilities, the United States imposed restrictions in 2022 on the export of certain advanced chips to China. But throughout the AI boom those chips have kept turning up in China anyway.\nOn 1 October 2026, the U.S. arrested a man on charges of sending over US $300 million worth of GPU-equipped servers to China using paperwork intended for shipments to Malaysia and…"
tags: []
orgs: ["China", "Nvidia", "Apple"]
topics: ["chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 1097
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50425847"
score: 24
comments: 11
community: "Hacker News"
---

# The Race to Build a "Find My" for AI Chips

IEEE Spectrum · oldnetguy · 2026-11-09

In a bid to limit China’s AI capabilities, the United States imposed restrictions in 2022 on the export of certain advanced chips to China. But throughout the AI boom those chips have kept turning up in China anyway.
On 1 October 2026, the U.S. arrested a man on charges of sending over US $300 million worth of GPU-equipped servers to China using paperwork intended for shipments to Malaysia and Singapore. As chip smuggling and diversion continues, the United States is learning that the more it tries to limit the motion of its AI chips, the harder they are to precisely locate.
To help curb the issue, the U.S. is turning to location verification. Last March, the U.S. House Foreign Affairs Committee passed a bill requiring location verification for advanced AI chips. Ahead of the U.S.-China summit in late September, legislators called for a floor vote on that and related bills.
If such a requirement were to pass, how would chipmakers comply? They could build tamper-proof root-of-trust hardware, implement cryptographic signing and transmission, or possibly even fingerprint individual chips. These strategies could function as a way to keep track of where AI chips actually are in the world, much like how the popular “Find My” feature can locate misplaced Apple devices.
Pings that pinpoint positions
Location verification can take different forms, such as geolocation mechanisms, inventory-management tools, mail-in inspections, and video inspections. A combination of approaches, such as ping-based location verification (PLV) supplemented by physical inspections, would be a feasible and robust approach, say the authors of a September Center for Security and Emerging Technology (CSET) report on chip-location tracking.
To deduce an AI chip’s location, PLV measures the time it takes for a ping to travel from the chip to multiple trusted “landmark” servers around the world and back. Kyle Miller, a senior research analyst at CSET and coauthor of the report, says that for new AI chips, manufacturers could integrate PLV functionality into the hardware itself, while a firmware update could be applied to chips already in circulation.
Not all AI chips should be tracked, the researchers note. “The priority should be for the highest-end data-center chips—the cream of the crop in high-end data-center GPUs,” says Jacob Feldgoise, a senior data-research analyst at CSET and coauthor of the report.
A similar initiative involves transmitting encrypted “sovereignty certificates.” These certificates act as “cryptographic credentials that provide verifiable, unforgeable proof of the physical location of a computing device, such as a CPU or GPU, at a specific point in time,” per the draft specification published by secure computing firm Lucid Computing.
“If you can use a private key that exists on a particular chip, and you can sign a message with that cryptographic key, and then that message is received by a so-called landmark server, then you can send a couple of those messages and time those messages. A lot of modern chips come with trusted execution environments that support a hardware root of trust where you can sign these messages,” says Kristian Rönn, CEO and cofounder of Lucid Computing. “You get a radius of where the chip has to be.”
PLV could have some effect on chip smugglers, Miller says. “They know if they turn this chip on, it’s going to start pinging these landmark servers. That could deter some smuggling.” And when the system flags a chip as residing in a unintended location, “the PLV data gives you a better sense of when and where it was moved,” he adds.
However, ping-based location verification can only uncover diversion after it has happened. It can’t track offline chips that are in storage, in transit, or have yet to be activated. And when a chip fails to respond to a ping request, the system won’t know whether it’s due to a valid reason or nefarious causes.
This is where physical inspections come in. “You need to do that follow-on investigative work. You need to physically go to these data centers and do those physical audits as well. Essentially, [PLV] generates leads, and you track down those leads,” says Miller.
A PLV system involves sending signals from a chip to and from trusted servers and measuring the travel time.Source image: CSET
A “lie detector” for data centers
Despite the safeguards around ping-based location verification, the methodology remains vulnerable to particular attacks. If adversaries gain physical access to a chip, for example, they could prevent it from sending signals, or they could extract cryptographic keys and spoof a signal from the intended location.
To fight that, some security researchers are exploring hardware fingerprints instead of cryptographic keys. One study demonstrated a proof-of-concept GPU fingerprinting function that produced unique fingerprints for Nvidia H200 GPUs based on their manufacturing variations and random numbers as seeds.
“You want to support other types of fingerprinting because not all chips have a hardware root of trust. You might want to use some statistical fingerprinting to know that the chip is what it’s supposed to be,” Rönn says. “It also requires good physical security around the chips, such as tamper-proofing. Over time, you ideally want to have more defense in depth.”
Additionally, the CSET report warns that PLV is costly. And if China achieves the ability to craft its own advanced AI chips, “then tracking the export of U.S. chips is less of a strategic priority,” says Miller.
Hanna Dohmen, a senior research analyst at CSET and coauthor of the report, points to other gaps in the U.S. export-control regime. “Currently, Chinese companies are legally able to remotely access AI chips abroad through cloud-service providers,” she says. These advanced AI chips might be installed in data centers across Southeast Asian countries like Malaysia, which are increasingly serving Chinese firms.
Whether or not a “Find My” for AI chips becomes a regulatory requirement, Feldgoise envisions tighter conditions for the export of advanced AI chips. “This is based on the increasing importance of compute to national and economic security,” he says. “The chips that generate compute are being seen as a strategic resource, so I would be unsurprised if the due diligence requirements on these devices increase as time passes.”
Rönn views sovereignty certificates as essential tools in the future, likening it to a “lie detector” for data centers that answers the “where, how, what, and who questions for us to know that they comply with a basic standard of security when it comes to AI systems.”
Rina Diane Caballar is a writer covering tech and its intersections with science, society, and the environment. An IEEE Spectrum contributing editor, she's a former software engineer based in New Zealand.
