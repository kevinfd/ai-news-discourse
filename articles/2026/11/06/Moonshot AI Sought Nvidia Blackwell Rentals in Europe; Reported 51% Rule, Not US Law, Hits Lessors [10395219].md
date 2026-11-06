---
id: "10395219e5a89427"
title: "Moonshot AI Sought Nvidia Blackwell Rentals in Europe; Reported 51% Rule, Not US Law, Hits Lessors"
url: "https://techtimes.com/articles/330165/20261106/moonshot-ai-sought-nvidia-blackwell-rentals-europe-reported-51-rule-not-us-law-hits-lessors.htm"
link: "https://techtimes.com/articles/330165/20261106/moonshot-ai-sought-nvidia-blackwell-rentals-europe-reported-51-rule-not-us-law-hits-lessors.htm"
source: "Tech Times"
domain: "techtimes.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-06T04:22:00Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Joshua Mitchell"]
language: "en"
summary: "Moonshot AI Nvidia Blackwell lease talks with European neocloud operators, reported by CNBC on Nov. 5, test a legal gap: renting chips abroad is allowed under current U.S. export controls. The Financi ..."
tags: []
orgs: ["Nvidia", "China", "ByteDance", "CoreWeave"]
topics: ["chips & infrastructure", "policy & regulation", "models & research", "business & funding"]
content_source: "fulltext"
word_count: 1713
paywalled: false
image: "http://www.bing.com/th?id=ONUT.CSChznRv_fB3qkbqx9TZgA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Moonshot AI Sought Nvidia Blackwell Rentals in Europe; Reported 51% Rule, Not US Law, Hits Lessors

Tech Times · Joshua Mitchell · 2026-11-06

Moonshot AI, the Beijing-based lab behind the Kimi models, held talks with European neocloud operators about leasing Nvidia Blackwell capacity, including potential clusters of 8,000 or more GPUs, CNBC reported Thursday, Nov. 5, citing four people familiar with the discussions. Renting chips abroad is legal under current U.S. rules, so the pressure lands on the European companies that own the hardware, not on the Chinese renter. The reports reviewed describe talks, not a signed lease.
The Financial Times reported Tuesday that Nvidia told its data-center partners to direct at least 51% of their services to non-Chinese customers on new contracts. Moonshot's search for capacity follows July 19, when Kimi said demand over the prior 48 hours had approached its GPU limits. On this reading, the owner's relationship with Nvidia, more than Beijing's exposure, may decide who gets Blackwell time. Operators, enterprise buyers and anyone depending on Kimi models have a stake.
Neocloud Owners Hold Chip Titles, So Nvidia's Customer Rule Reaches Them First
The FT's five sources said Nvidia conveyed the 51% requirement verbally through sales and regional teams, that it applies only to new contracts, and that the company had not imposed a comparable limit before. Nvidia neither confirmed nor denied the report. Its statement said that America cannot win the AI race unless American AI infrastructure wins worldwide. The reports reviewed do not say how "Chinese customer" is defined, how the instruction is enforced, or which partners it covers.
Neocloud economics explain why that matters. Neoclouds borrow to buy Nvidia chips and use those chips as loan collateral; CoreWeave, the best-known example, held three GPU-backed loans totaling $12.4 billion as of December 2025. Estimates of how long a GPU stays economically useful range from one year to eight. An operator in that position depends on Nvidia's allocation goodwill and on lenders who hold its chips as security. That dependence is analysis, not a reported fact about any named European operator, and CNBC's reporting names none.
Reported Upfront Premiums of 30% to 50% Price Regulatory Risk Into Leases
One of CNBC's sources described a proposal under which Moonshot would pay 30% to 50% more upfront than a non-Chinese customer. The figure rests on that single source. A larger deposit moves cash to the owner early, which fits a lessor that cannot be sure Washington will leave the arrangement alone. The reports reviewed do not say who proposed the terms.
Can Chinese Companies Legally Rent Blackwell GPUs in Europe?
Yes, under rules as reported today. Lawyers cited by Introl say export bans bar Chinese companies from owning controlled chips, not from using them remotely. The Export Administration Regulations, run by the Commerce Department's Bureau of Industry and Security (BIS), attach to items, end users and end uses. BIS does not consider cloud services exports under current law, Introl reports.
Precedents are already in the open. Tencent rents Blackwell capacity from Datasection, a Japanese company with an Osaka-area data center, according to a report citing unnamed sources; Tencent told the publication its use of cloud services is "transparent and legal." The Wall Street Journal reported that ByteDance planned to use a 36,000-GPU B200 cluster in Malaysia run by Aolani; Nvidia said the arrangement is permissible as long as it complies with U.S. export controls, and described a vetting process for cloud partners. Smuggling is treated differently: three people tied to Super Micro, including a co-founder, were accused of smuggling about $2.5 billion in Nvidia servers to China in an indictment unsealed in March. Super Micro is not named in the indictment, and the charges are allegations.
Washington is not ignoring the gap. In August, Bloomberg reported that BIS enforcement was reviewing how Chinese firms reach Nvidia chips overseas and compiling lists of countries involved, though The Next Web noted it is unclear whether BIS can police cloud deals under its current powers.
Inference Demand Explains Why Moonshot Wants Rack-Scale Blackwell
Two of CNBC's sources identified interest in European inference clusters, meaning serving model answers to users, and one source was aware of interest in training capacity. The model explains the appetite. Kimi K3 is a mixture-of-experts system with 2.8 trillion parameters that activates 16 of its 896 experts for each token. Because routing can select any expert, all experts must stay resident in memory. Moonshot recommends 64 or more accelerators for production serving.
That is where Blackwell fits. Nvidia's Blackwell generation includes the 72-GPU NVL72 rack-scale system and native support for MXFP4 and MXFP6 formats. The sources read include no independent benchmark of Kimi K3 on Blackwell, so this article gives no speedup figure.
Moonshot's current constraint is documented. Tom's Hardware reported that Moonshot reportedly relies on Nvidia's China-market H20 for inference and that subscriptions sit on a waiting list.
Remote Access Security Act Waits in Senate Banking Committee With No Markup Recorded
H.R. 2683 would amend the Export Control Reform Act of 2018 to treat remote access by a foreign person through a network connection as a regulated activity where it poses a serious national security risk. Mondaq's summary says it would let BIS license and penalize remote access to controlled items. The House passed it 369-22 on Jan. 12, 2026. It was referred to Senate Banking on Jan. 13, and a bill tracker records no committee markup. A Senate companion, S. 3519, was introduced by Sens. Dave McCormick and Ron Wyden. An earlier Lawler bill, H.R. 8152, passed the House by voice vote in September 2024 and died in Senate Banking.
eeNews Europe reports that cloud providers and GPU rental intermediaries may face stronger compliance obligations such as customer screening and licensing if the bill advances. For a European neocloud, that would be the second cost after Nvidia's rule. The Chinese renter would be exposed too, since the bill reaches foreign persons who access controlled items remotely.
Nvidia Says Cloud Partners Are Vetted; Lawler Says Remote Access Sidesteps Prohibitions
Nvidia has said the ByteDance arrangement is permissible if it complies with U.S. export controls, and Chief Executive Jensen Huang has called China the second-largest computer market in the world, saying it is a mistake for the United States not to participate. Rep. Mike Lawler, R-N.Y., the House bill's sponsor, has said the Chinese Communist Party has a real tool to sidestep export prohibitions.
The administration's own stated goal complicates enforcement. White House Office of Science and Technology Policy Director Michael Kratsios said in July 2025 that he wants the world running on an American AI stack of chips, cloud services and software. Kratsios has also alleged that Moonshot acquired GB300 servers and accessed them in Thailand; TechTimes reported that no public evidence for the chip allegation has been released. A Chinese lab renting Blackwell in Europe would run on that same American stack, a tension this article offers as analysis rather than reported fact.
Kimi Users Still Face China's National Intelligence Law Wherever GPUs Sit
Moving GPUs to Europe changes where chips run, not where Moonshot is legally based. China's National Intelligence Law, passed June 27, 2017, requires organizations and citizens to support, assist and cooperate with national intelligence efforts. Whether it reaches overseas subsidiaries is disputed: a 2019 Mannheimer Swartling report said overseas subsidiaries could be covered, while a 2018 legal opinion submitted by Huawei said its overseas units are not. Scholar Jeremy Daum argued it is far from clear that Article 7 requires active information gathering, and that it carries no enforcement mechanism, though direct requests from security authorities would be hard to resist. China's Cybersecurity Law and Data Security Law provide separate bases for government access.
The data at stake is whatever users send to Moonshot-run services, including prompts and uploaded files. The reporting does not say which services would run on leased European clusters. No independent audit of Moonshot's data handling turned up; prior coverage records an April 2026 data exposure in which Kimi disclosed a user's resume to an unrelated user. Self-hosting open weights keeps prompts off Moonshot's servers, but Chinese law still applies to Moonshot as a company.
Performance, Benchmark and Ecosystem Gaps Persist Whatever Data Center Hosts Kimi
Cheaper access to Blackwell time does not fix model quality. Artificial Analysis measured a hallucination rate near 51% for K3, as TechTimes reported. Capacity strain is documented too: Kimi's July 19 warning that demand neared GPU limits and the reported reliance on H20 chips for inference point to an ecosystem still short of serving hardware. This reporting did not assess documentation, support or tooling for international buyers, which remain open questions.
Operators, Buyers and Senators Each Face Different Decisions
For a European operator, the reported exposure is Nvidia's 51% floor, lender expectations and possible licensing duties under H.R. 2683, none of which falls first on Moonshot. For a Kimi buyer, European hosting changes neither Chinese law over Moonshot nor the roughly 51% hallucination rate Artificial Analysis measured. For Congress, the question is whether the Senate will act on a bill referred to committee on Jan. 13 while Nvidia's rule and reported premiums carry the risk. Until the Senate moves, offshore leasing stays legal under rules as reported, and the exposure falls first on the operators holding the chips.
Frequently Asked Questions
What would the Remote Access Security Act change for cloud providers?
It would let BIS regulate remote access to controlled items by foreign persons, and eeNews Europe reports providers and GPU rental intermediaries may face stronger compliance obligations such as screening and licensing. The bill still needs Senate passage.
Who limits Chinese access if the renter breaks no law?
Today, mainly the chip supplier. Nvidia's reported verbal 51% rule works through new partner contracts rather than statute, and BIS is reviewing Chinese firms' remote access while it remains unclear whether it can police cloud deals.
Why does Moonshot need so many GPUs just to serve answers?
A 2.8-trillion-parameter mixture-of-experts model keeps all expert weights in memory even though few experts run per token, so serving needs large, well-connected GPU pools, and Moonshot recommends at least 64 accelerators for production serving.
Does renting GPUs in Europe protect Kimi users from Chinese law?
No. Hosting location does not change that Moonshot is a Beijing-based company, and TechTimes reports the obligations apply regardless of server location. The reporting does not say which Kimi services would use the European clusters.
