---
id: "121b3ccc8129e670"
title: "Using Claude to help uncover medicare fraud"
url: "https://reddit.com/r/ClaudeAI/comments/1x4grru/using_claude_to_help_uncover_medicare_fraud"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-12T23:06:19Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["purekarmalabs"]
language: "en"
summary: "We've been following the news about how flagrant medicare fraud has become and how it could easily be detected by a 10-year-old, so we asked Claude if it could spot some potential red flags in the publicly available 2024 CMS data. Most of what it flagged turned out to be companies that have already been caught, but others appear to fit the same profile as known fraudsters, but they are still in…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["health & science", "business & funding", "search & media"]
content_source: "post"
word_count: 515
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x4grru/using_claude_to_help_uncover_medicare_fraud/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Using Claude to help uncover medicare fraud

Reddit · purekarmalabs · 2026-10-12

We've been following the news about how flagrant medicare fraud has become and how it could easily be detected by a 10-year-old, so we asked Claude if it could spot some potential red flags in the publicly available 2024 CMS data. Most of what it flagged turned out to be companies that have already been caught, but others appear to fit the same profile as known fraudsters, but they are still in business. Here's what we found using the CMS's public 2024 provider-level files (medicare only): 1. Phantom medical supplies Several companies showed the signature of billing for supplies nobody ordered. The national total for one wound-dressing code ran about $23M a year, then skyrocketed to $650M in 2024. One supplier in Florida accounted for 62% of that, going from about $0.6M for less than 500 patients in 2023 to almost $860 million and 127K patients in 2024. A supplier in New York went from roughly zero to $473 million. And a third Pennsylvania-based company billed almost 90% of all drainable ostomy pouch volume in the country. 2. Falsified or fraudulent orders Because the data show which clinician signed off on each order, we can see how much each one supposedly ordered. For ostomy pouches in 2024, that's 271 clinicians nationwide with more than ten Medicare patients on them, and 213 are family-practice doctors. Ostomies are created and managed by surgeons; a family doctor might have a handful at any one time. Yet these family doctors each show about 175 ostomy patients, across 40 states, at nearly identical patient counts and dollar totals, roughly half a million dollars apiece. How many colorectal surgeons, the people who actually do this work, were in the data? Fifteen. Hundreds of unrelated family doctors don't independently become high-volume ostomy prescribers in a single year. What does produce that picture is a real doctor's license number attached to orders they never wrote. The same shape repeats for wound dressings and catheters: for catheters, 1,343 of the 1,720 ordering clinicians are family practice, and the number of urologists in the entire file is seven. 3. Labs that run unnecessary tests Two genetic labs with offices in the same office park billed 23% of the entire country's epilepsy gen panel volume. The bigger one billed nearly the same patient count (about 4,300) under four different panels, plus 6,000-7,000 patients each on a dozen single-gene tests. They also had skyrocketing revenue YoY from $4.6 million in 2023 to $60 million in 2024. 4. Some are still in business The most flagrant offenders appear to have been caught, closed up shop, or banned from accepting medicare payments since 2024, but several others with suspicious profiles are still taking taxpayer money as of the July 2026 enrollment file. If there's interest for you to run your own analysis, we'll publish a skill file so you can see for yourself what Claude can uncover, just remember outliers in the data are not 100% confirmation of fraud and could be the product of perfectly legitimate business practices. You should report what you find to the HHS OIG.
