---
id: "652ca5c0387cb64c"
title: "Meta suspends Muse chats sharing feature after it left private details exposed"
url: "https://engadget.com/2292281/meta-suspends-muse-chats-sharing-feature-after-it-left-private-details-exposed"
link: "https://engadget.com/2292281/meta-suspends-muse-chats-sharing-feature-after-it-left-private-details-exposed"
source: "Engadget"
domain: "engadget.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T20:00:43Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Anna Washenko", "staff@engadget.com (Anna Washenko)"]
language: "en"
summary: "Researchers accessed 6,800 shared conversations with the AI agent, including internal company documents."
tags: ["Meta"]
orgs: ["Meta"]
topics: ["agents & coding", "search & media"]
content_source: "fulltext"
word_count: 285
paywalled: false
image: "https://www.engadget.com/img/gallery/meta-suspends-muse-chats-sharing-feature-after-it-left-private-details-exposed/l-intro-1792526399.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Meta suspends Muse chats sharing feature after it left private details exposed

Engadget · Anna Washenko, staff@engadget.com (Anna Washenko) · 2026-10-20

Meta suspends Muse chats sharing feature after it left private details exposed
Researchers accessed 6,800 shared conversations with the AI agent.
Meta debuted its Muse agentic AI platform last month and bug hunters have already uncovered a privacy problem. Users would share their Muse conversations by creating a URL, but that feature has been disabled after researchers found that anyone could potentially access those links.
Researchers at security firm Claroc discovered that the links for users' shared Muse chats can be found and accessed via a passive DNS search because all the URLs for sharing had the same domain name and used the conversation's title in the subdomain. Passive DNS are records of how human-readable domains resolve to browser-readable IP addresses, basically acting like a phone book for the Internet.
"Muse names each share's web address after the conversation's own title, and that address is written into public DNS," Claroc explained in a blog post. "One passive-DNS search brings back thousands of them, listed by name, like a table of contents."
The company was able to enumerate 6,800 links for shared Muse chats and view private information from both business and personal applications of the service. The exposed personal details included meeting times with a frontier AI lab, a small-business loan application, a bank fraud alert with partial account details, a company's vacation calendar and other internal company documents.
Ars Technica first reported on Claroc's efforts. In a statement to the publication, Meta said "we've paused this functionality while we review this report and consider changes to how these links can be discovered." Claroc also noted that its researchers were unable to open a sampling of the links they had previously accessed following Meta's update.
