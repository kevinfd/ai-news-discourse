---
id: "38c61351fe0dc3e7"
title: "87% of the Anthropic power will come from gas and 11% from coal in 2028"
url: "https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power"
link: "https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power"
source: "Better Data Center Project"
domain: "betterdatacenterproject.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-22T08:57:34Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["happosai"]
language: "en"
summary: "In The AI Gas Rush: Risks and Implications of “Bring Your Own Power”, we dug into how data centers are increasingly securing their own dedicated primary power generation rather than relying solely on utilities to procure power (“BYOP”). We identified 177 GW of planned BYOP gas capacity—enough to power 65% of all US homes. Conversely, we found renewables are much less common than gas for BYOP: we…"
tags: []
orgs: ["Anthropic", "Google", "Meta", "Microsoft", "Amazon"]
topics: ["chips & infrastructure", "business & funding"]
content_source: "fulltext"
word_count: 1700
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50597612"
score: 988
comments: 969
community: "Hacker News"
---

# 87% of the Anthropic power will come from gas and 11% from coal in 2028

Better Data Center Project · happosai · 2026-11-22

In The AI Gas Rush: Risks and Implications of “Bring Your Own Power”, we dug into how data centers are increasingly securing their own dedicated primary power generation rather than relying solely on utilities to procure power (“BYOP”). We identified 177 GW of planned BYOP gas capacity—enough to power 65% of all US homes. Conversely, we found renewables are much less common than gas for BYOP: we estimate that for current proposals, less than 20% of energy generation will come from renewable sources by 2032.
But BYOP projects aren’t the only new fossil sources that are coming online to meet the skyrocketing energy demands of AI data centers. Another 200 GW of new fossil power plants is being built on the grid to meet growing demand, due in large part to data centers.1
As a case study of how the AI buildout is driving both new BYOP and grid fossil infrastructure, we analyzed the compute commitments of a single company: Anthropic.
Map of Anthropic’s data centers and associated power plants. See our full dataset for details of each site.
Finding 1: Anthropic has made no direct commitments to renewable energy in the U.S. Though Anthropic has stated “We’re also working to broaden our energy mix with geothermal, wind, solar, and emerging technologies”, its only publicly disclosed commitments, contract, or investments in renewable power are in Norway and Canada (as of November 2026). In contrast, Anthropic is directly procuring fossil power equipment—it recently “bought commitments for 1.7 gigawatts of heavy-duty [gas] generators for $3.4bn”.
Finding 2: Anthropic’s currently contracted data centers in the U.S. will be overwhelmingly powered by fossil fuels in the near term. By considering on-site gas and the grid power plants which are likely to meet Anthropic’s added load (i.e. marginal generators), we estimate about 87% of the company’s power will come from gas and 11% from coal in 2028. As of October 2026, Anthropic has contracted 15 GW of compute; of this, about 5.9–9.6 GW is contracted to specific data center sites. For a sense of scale, 9.6 GW could power about 7 million homes or cover 18% of the peak power demand of California—the world’s 4th largest economy.
This demand will be met with a mix of new on-site gas, new grid gas, and existing grid gas, coal, and nuclear. In the short term, no grid renewables are attributed to Anthropic’s power use, because—without commitments to new renewable capacity—new load on the grid will be met by dispatchable, marginal fossil resources.2 For more details, see our full dataset and our methodology below.
Finding 3: Total CO2 emissions from Anthropic’s power use at these sites could reach 17–38 million MtCO2e per year in 2028, when this capacity is expected to be online. This range reflects uncertainty in Anthropic’s average power use, due to factors such as cooling needs and average utilization (see methodology below). In our mid-case, Anthropic will emit 32 million MtCO2e in 2028. These totals will continue to grow—possibly doubling by 2030, as some analysts expect Anthropic to secure 30 GW by 2030.
To put these figures in context, Anthropic’s CO2 emissions from power use in 2028:
- could exceed the emissions of all of California’s power generation (31.1 MMtCO2e in 2024, not including imports).
- could exceed Meta, Microsoft, and Google’s combined Scope 2 emissions from 2025 (their location-based emissions, before renewable energy offsets, were 5.9 million, 12 million and 15 million MtCO2e, respectively)3
- would represent a 16–36% increase over 2024 levels of the entire U.S. data center sector (105 MMtCO2e).
- would increase the entire U.S.’s power sector emissions (1,485 MMtCO2e in 2025) by 1.1–2.5%.
Finding 4: Anthropic’s data centers are sited in areas where the grid mainly uses coal and gas. We estimate the average carbon intensity of Anthropic’s power to be 1,033–1,076 lb CO2e/MWh, 35% higher than the U.S. grid average (767 lb CO2e/MWh).4
Finding 5: 80% of on-site power uses inefficient simple cycle turbines and engines. About 25% (2.5 GW) of Anthropic’s contracted power will come from on-site, behind-the-meter gas. 80% of this on-site capacity consists of inefficient simple cycle turbines and engines, which emit more pollution per unit of electricity than modern combined cycle plants (see our report for more details on the types of power generation being used for on-site gas).
Finding 6: Based on EPA’s nationally-averaged benefit-per-ton estimates, air pollution from Anthropic’s on-site and grid power use could cause $2–3 billion in annual health damages, with total emissions of over 13,000 tons per year (tpy) of nitrogen oxides (NOx) and 2,000 tpy of fine particulate matter (PM2.5).
In October 2026, Anthropic outlined its “approach to responsible data center development”, stating: “We follow the air permitting process everywhere we operate and require the same of the plants powering our data centers. Those plants must also use emissions control technology, including selective catalytic reduction [SCR].” However, Anthropic has used compute capacity at SpaceX’s Colossus 2 facility since May 2026, which still receives most of its power from temporary, unpermitted turbines, the majority of which are not equipped with SCR. Anthropic will use as much as 600 MW of power from Colossus 2 by the end of 2026 (see methodology below).
Anthropic has also contracted 460 MW (and is in talks for up to 920 MW) of power from Nscale’s Monarch Compute Campus in Mason, West Virginia. This facility will be powered by inefficient reciprocating engines which have significant formaldehyde and hazardous air pollutant (HAP) emissions compared to conventional gas power plants.
For more, see our full dataset on Anthropic’s compute and our report on BYOP.
Methodology
We gathered details about Anthropic’s data center commitments from Epoch AI’s tracker, Anthropic’s announcements and filings, announcements and filings from partners (including Amazon and SpaceX), and reporting from The Information, Semafor, and others.
We first identified the source for each data center’s power. For projects with on-site gas (Monarch, Nexus, Colossus 2) or new grid gas (including indirectly contracted projects such as the Schahfer expansion for the AWS New Carlisle site and Entergy Mississippi’s gas plants for AWS’s Madison and Ridgeland facilities) we used emissions factors from permits where available, or permit values from comparable facilities. For grid-connected facilities without associated new generation capacity, we assume these sites will be powered by marginal, dispatchable grid capacity. We used EPA’s AVERT tool to model which power plants would meet the new incremental load from Anthropic’s facilities based on each site’s expected power use and region. AVERT uses historical EPA data for these power plants to model the expected short-run marginal emissions rate of CO2 and criteria pollutants (NOx, PM2.5, etc.). We use AVERT because we are interested in the short-term impacts from new data centers coming online in the next several years.
To calculate the amount of power used by each site, and in turn the total quantity of air pollutant emissions, we assumed power usage effectiveness (PUE) ranges from 1.1–1.2 for all sites (typical values for hyperscale data centers are between 1.05–1.3), and power utilization ranges from 60–80%. See LBNL’s 2024 Data Center Energy Usage report for more details about how these parameters vary in typical hyperscale data centers. For our mid-case, we assumed a PUE of 1.15, a power utilization of 70%, and that all 9.6 GW of identified compute capacity is online in 2028.
How much capacity is Anthropic leasing from xAI?
Anthropic’s initial announcement on May 6, 2026 stated the agreement with SpaceX provided 300 MW of compute (220,000 GPUs). From SpaceX’s revised June S-1A, this deal expanded to ~$1.25B/month for 325,000 NVIDIA GPUs,5 with an implied IT power of ~490 MW. Based on Anthropic’s October 2026 S-1, this deal has further expanded to $3.1B/month.6 It’s unlikely that the increase in $/month will result in a proportional (2.5x) increase in compute capacity, since a June 2026 deal between Google and SpaceX had a much higher cost (~$11.5/GPU-hr vs ~$5/GPU-hr). As a rough estimate, the scaled deal likely corresponds to an additional ~200,000 GPUs, with a total power of ~400 MW (uncertainty is probably ±25% for each).7
- Data centers are driving 50–75% of demand growth, according to IEA and McKinsey. ↩︎
- For more discussion, see for example: Fassette, Camille. “The emissions risks of AI data center buildout.” WattTime. February, 2025; EPRI. “Powering Data Centers: U.S. Energy System and Emissions Impacts of Growing Loads.” October, 2024. ↩︎
- Note: Anthropic’s emissions from power use will likely be classified as a mix of Scope 2 and Scope 3 emissions, depending on if they own the GPUs. For facilities they are leasing space in, the emissions will likely be accounted for as Scope 2 emissions for the owner/operator (e.g. Amazon for Project Rainier or SpaceX for Colossus). It should also be noted that the emissions of Microsoft, Google, and Meta are expected to grow as well, so the comparison between their 2025 emissions and Anthropic’s 2028 emissions is not meant to suggest that Anthropic will be the largest emitter among the tech companies. ↩︎
- This average is based on AVERT’s marginal emissions for grid-connected units without new dedicated capacity. Using the average (non-marginal) carbon intensity for each eGRID subregion would give a carbon intensity of 839 lb CO2/MWh. However, marginal emissions are more representative of the near-term impacts of Anthropic’s added load to the grid. ↩︎
- Pg. 13: “For example, in May 2026, we entered into Cloud Services Agreements with Anthropic PBC (“Anthropic”), an AI research and development public benefit corporation, with respect to access to compute capacity across COLOSSUS and COLOSSUS II. Compute capacity provided includes approximately 325,000 NVIDIA GPUs, backed by hyperscale-class CPUs, exabyte-scale storage and high-speed networking and interconnects purpose-built for AI workloads. Pursuant to these agreements, the customer has agreed to pay us $1.25 billion per month through May 2029, with capacity ramping in May and June 2026 at a reduced fee.” ↩︎
- “Under the SpaceXAI Arrangements, we agreed to spend an aggregate of up to $120.5 billion over terms extending into 2029, consisting of approximately $3.1 billion in the aggregate per month once all capacity has been delivered, which we expect in December 2026, with different fees during capacity ramping periods.” ↩︎
- See our calculations and EpochAI’s calculations for more details. ↩︎
