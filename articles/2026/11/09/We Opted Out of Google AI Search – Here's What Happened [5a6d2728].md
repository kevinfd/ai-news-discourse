---
id: "5a6d272895a7ddae"
title: "We Opted Out of Google AI Search – Here's What Happened"
url: "https://signal.zyppy.com/p/we-opted-out-of-google-ai-search"
link: "https://signal.zyppy.com/p/we-opted-out-of-google-ai-search"
source: "Zyppy Signal with Cyrus Shepard"
domain: "signal.zyppy.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T10:41:40Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["giuliomagnifico"]
language: "en"
summary: "👋 Subscribe free (it helps us produce research like this) and get tips + tactics on how to win more SEO and AI visibility.\nIn August 2026, Google shipped a feature worldwide that let publishers opt out of having their content appear in search AI features.\nGoogle warned publishers that doing so could reduce traffic.\nWe wondered exactly how much traffic?\nSo we pressed the forbidden…"
tags: []
orgs: ["Google"]
topics: ["search & media", "models & research"]
content_source: "fulltext"
word_count: 1129
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50423786"
score: 13
comments: 0
community: "Hacker News"
---

# We Opted Out of Google AI Search – Here's What Happened

Zyppy Signal with Cyrus Shepard · giuliomagnifico · 2026-11-09

👋 Subscribe free (it helps us produce research like this) and get tips + tactics on how to win more SEO and AI visibility.
In August 2026, Google shipped a feature worldwide that let publishers opt out of having their content appear in search AI features.
Google warned publishers that doing so could reduce traffic.
We wondered exactly how much traffic?
So we pressed the forbidden button.
Previously, the only way to opt out of appearing in AI features was to block your website entirely from Google’s crawlers, which unfortunately also meant not appearing in Google search at all.
Using the opt-out feature means your site’s content no longer appears in Google’s AI Overviews or AI Mode, including links to your site. It stops all AI search traffic from Google.
(Importantly, it does not prevent Google from using your website for AI training. There are different controls for that.)
For example, here’s what an AI search result might look like when Google includes our website, including three AI search links and one organic search link.
After we opted out of AI search features, all those citation links simply disappeared.
Here’s what the same search result looked like after we hit the opt-out button. Our site still ranks #1 in regular organic search results, but is completely gone from the AI features, including citation links to our site.
After opting out of Google’s AI search features, we wanted to ask three questions:
- How much visibility would we lose?
- Was anybody actually clicking those links in AI answers?
- How much traffic could we lose by opting out?
Caveats and Important Notes on Data Size
This is data from a single experiment on a single site. While we made serious efforts to estimate how much traffic Google’s AI search features generated for our site, be careful before assuming these numbers apply to other sites as well. AI visibility varies wildly across publishers, so you should treat our findings more as a directional yardstick than Google gospel.
We Lost Nearly 100% of AI Visibility
Google does not drag its feet when removing you from AI answers.
Within an hour after pushing the button, our website completely stopped showing up in Google’s AI search.
Previously, we saw 500-1000 AI search impressions daily.
But then, zero.
This represented about 10% of our site's total search impressions.
28 days later, we opted back into Google’s AI search, and impressions returned almost as fast.
Clicks From AI Search Had a 0.9% Click-through Rate (CTR)
Google doesn’t tell you how many people click your website links in AI answers.
Google Search Console reports total clicks, but it doesn’t separate AI search from regular organic search.
This gave us an opportunity. With some statistical analysis, we could estimate AI search clicks by comparing total clicks between the “opt-out” and “opt-in” periods.
This analysis estimated an AI search CTR of ~0.9%, with a reasonable range of 0.7%-1.1%.
To the uninitiated, 0.9% CTR may sound very small. That's slightly less than 1 click per 100 impressions.
But in reality, it’s surprisingly large. Given our overall website CTR in Google Search is around 0.4%, our AI Search CTR is more than double our normal click rate.
All those clicks can add up.
The “Halo Effect” - AI Search Boosted Regular Organic Clicks
Here’s something we didn’t expect: when our site appeared in AI Overviews, even regular organic search results got more clicks.
The impact on CTR was small but significant, around 2.3%, and the effect was strongest on URLs with the most AI visibility.
In advertising, this is often known as the “Halo Effect.” When users see your website listed multiple times in the same search results, they are more likely to click at least one.
Nobody knows quite for sure why this is, but a likely explanation is brand reinforcement, aka the "two is better than one trust signal".
It’s strange to think that opting out of AI search would lower your regular organic traffic, but in our case the data was pretty compelling.
AI search helped get more clicks from results listed further below.
AI Search Can Account for 20-23% of Our Total Traffic
Here’s where it gets most interesting: Google’s AI search features appear to drive a lot more traffic to our site than we first realized.
When we throw out small numbers like 0.9% and 2% CTRs, it may seem like we’re talking about a small number of clicks.
But remember, AI search had nearly 2x the CTR of regular clicks.
That means that even though AI impressions represented only 10% of our total search impressions, that added up to about 21% of our total clicks.
Then add 2% more clicks from the Halo Effect, and Google’s AI search was now responsible for 23% of total search clicks to our site. 
23% - not a small number!
It doesn’t help that Google’s AI answers push regular results so far down the page that fewer and fewer people click them. But that also makes those few clicks from the AI answers much more valuable.
At this point, we need to remind you to re-read the caveats and data disclaimers. Simply because AI search seemingly contributed 23% of our search clicks doesn’t mean your site sees the same. Your site could be higher or lower.
To be fair, we’ve done a fair bit of optimizing our site to win AI citations. That may be why so many of our clicks came from AI search.
At first, we weren’t sure whether anyone was clicking those AI links.
But now it not only seems like the smart move to include your site in AI search and optimize for AI recommendations/citations, but the only reasonable action to take.
For now, we’ll continue to opt in to AI search.
👋 Subscribe free (it helps us produce research like this) and get tips + tactics on how to win more SEO and AI visibility. Premium subscribers get 100% access to Pro Templates, Webinars, & Archives.
Study Methodology
We used a 28-day interrupted time-series design around a deliberate change in Google AI visibility.
On September 1, 2026, Zyppy was opted out of Google’s AI search features. AI-feature impressions subsequently fell by more than 99%, creating a 28-day AI-OFF period. On September 29, the site was opted back in, followed by a 28-day AI-ON period.
For both periods, we analyzed Google Search Console Web performance data, including clicks, impressions, CTR, average position, queries, and landing pages. We also used Google’s Generative AI Features report to measure AI-specific impressions.
We inferred AI click contribution from changes in total click performance between the AI-OFF and AI-ON periods, then checked the result against matched-query and position-level analyses to reduce confounding from shifts in rankings and query mix.
