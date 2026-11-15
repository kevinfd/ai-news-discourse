---
id: "91e7605a8469c48a"
title: "Outage in Microsoft 365 Email Infrastructure; Impact Extends to Calendar and Copilot AI Integration [Overseas Reactions and Analysis]"
url: "https://note.com/sekahan_0623/n/n9134ec56f24e?hl=en"
link: "https://note.com/sekahan_0623/n/n9134ec56f24e?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-14T11:53:00Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["せかはん（世界の反応Note"]
language: "en"
summary: "Three key points of this article・An outage occurred in the Microsoft 365 email infrastructure, affecting not only Outlook but also calendars, Copilot, and integrations with third-party AI.・Microsoft explained that the issue was technical,"
tags: []
orgs: ["Microsoft", "OpenAI", "Anthropic"]
topics: ["agents & coding", "jobs & society"]
content_source: "fulltext"
word_count: 1805
paywalled: false
image: "/th?id=ONUT.aqfzsD15HEWzlUqQ0DexBQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Outage in Microsoft 365 Email Infrastructure; Impact Extends to Calendar and Copilot AI Integration [Overseas Reactions and Analysis]

note · せかはん（世界の反応Note · 2026-11-14

SYSTEM NOTICE
Outage in Microsoft 365 Email Infrastructure; Impact Extends to Calendar and Copilot AI Integration [Overseas Reactions and Analysis]
Three key points of this article
・An outage occurred in the Microsoft 365 email infrastructure, affecting not only Outlook but also calendars, Copilot, and integrations with third-party AI.
・Microsoft explained that the issue was technical, triggered by a network change, and was unrelated to cyberattacks or AI.
・The impact spread because many features rely on data from the email infrastructure, although calls and chats remained functional.
Outage in Microsoft 365 Email Infrastructure Affects Calendar and AI Integration
In the early hours of November 13 (JST), Microsoft announced that an outage in the email infrastructure of its corporate service, Microsoft 365—which bundles email, document creation, and conferencing software—was making it difficult for users to connect to their email. Issues such as being unable to open emails or experiencing delays in delivery occurred in the Outlook email software, and the impact spread to calendars, meeting scheduling, and the AI assistant, Copilot.
The company proceeded with restoration in the order of Asia-Pacific, Europe, and North America, but did not disclose the number of affected users.
In Japan, the Ministry of Foreign Affairs and the Ministry of Education, Culture, Sports, Science and Technology (MEXT) posted on X (formerly Twitter) urging people to contact them by phone for urgent matters.
Osaka City also requested inquiries by phone, and MBS News reported that the work of approximately 8,000 employees in Sakai City was affected. In the United States, electric vehicle manufacturer Workhorse postponed its earnings call to the 16th, citing operational disruptions caused by this outage.
On the afternoon of November 14 (JST), Microsoft issued a final report stating that the outage lasted from shortly after 7:00 PM on the 12th to shortly after 1:00 AM on the 14th, and declared the service restored. Regarding the cause, the company explained that a problem from a previous network enhancement surfaced due to a recent network change, and stated that it was a technical issue unrelated to cyberattacks or AI.
A detailed post-incident report is expected to be released in a preliminary version within two business days and a final version within five business days.
Related Articles
This article is also available in video format.
What stopped and how was it restored?
Exchange Online behind Outlook
The reason the email outage extended to calendars and Copilot is that calendars and some AI features also utilize the underlying system that supports email.
Outlook is the interface for reading and writing emails. Emails and calendars are stored in the underlying service called Exchange Online, and meeting schedules booked via Teams are also written there. Corporate documents and file materials are stored in a separate location.
According to Microsoft, in the service for sharing files within the company, the basic function of directly opening saved documents was working. On the other hand, Copilot, which references emails, schedules, and files collectively to answer questions, experienced issues such as being unable to access business data, screens failing to load, or becoming unresponsive.
Even if files could be opened, the way they are searched or read through AI was affected. It has not been disclosed which specific processes within Copilot stopped or how.
The list of impacts also included meeting scheduling and security features that monitor for the removal of confidential information. Teams calls, meetings, and chats are considered unaffected.
The impact has also extended to AI outside the company. Anthropic, the developer of Claude, stated that the integration feature for reading Microsoft 365 emails and schedules experienced errors for many requests for about a day starting early on the 13th (Japan Standard Time), and attributed the cause to a disruption on Microsoft's side.
OpenAI also announced that similar integration features for ChatGPT experienced errors during the same time frame, but did not specify a cause. There is no evidence that the AI model itself was the cause.
Regarding files, impacts have been reported on some operations, such as exporting reports with protection labels like "Confidential" or sharing them with external parties. There is no evidence that the file format was the cause.
It took time to fix, and "connecting" and "returning to normal" were different things
Recovery work was not completed in one go and proceeded in stages by region.
Early on the morning of the 13th (JST), Microsoft explained that the problem was not an increase in traffic, but that many servers had unexpectedly become unavailable, causing the load to concentrate on the remaining servers. Reports continued that "previous responses did not have the expected effect," and during the work, it was also reported that restarted servers would stop responding again once they received traffic.
The explanation also changed along the way. Initially, they stated that no changes coinciding with the start of the disruption had been found, but a few hours later, they began the work of reverting a network configuration change that coincided with the timing. After that, stability began to return once adjustments were made to the settings of the mechanism that verifies user connections and distributes them to each server, with recovery progressing in the order of Asia-Pacific, Europe, and North America. In a report on the night of the 13th (JST), Japan was considered relatively stable.
Although the notification to users was issued early on the 13th, Microsoft's final report states that the disruption began about 6 hours earlier, just after 7:00 PM on the 12th (JST).
Even if connections are restored, work does not necessarily return to normal immediately. Emails sent during the disruption accumulated in a pending delivery state, and Microsoft extended the deadline for automatically retrying the delivery of undelivered emails to 48 hours.
Dave Plummer, a former Microsoft engineer who produces explanatory videos, is urging people to distinguish between whether emails failed to send or are just delayed. If you resend emails that are only delayed, the recipient may receive two copies of the same email.
Overseas Reactions
On r/sysadmin, a Reddit community for system administrators, a thread citing Microsoft's status report was started on November 12 (US time), the day of the disruption. Regarding the report that "the cause of the load was not an increase in traffic, but that many servers had unexpectedly become unavailable," the poster added a sarcastic summary: "They have absolutely no idea what is going on."
The voices are primarily from administrators who operate these systems daily and do not represent overall public opinion abroad. The posts also include exaggerations, speculation, and anecdotes that cannot be verified.
The following is an excerpt and translation of user comments from the thread.
Next is a thread posted the day after the outage titled, 'No, you're not going to migrate off M365 (short for Microsoft 365).'
The poster argues that if you run it yourself, you take on the responsibility for downtime, and that companies won't give up the integrated features and the convenience of Copilot. Opinions were divided on whether to migrate, with voices suggesting having alternative communication methods and calculating how much to keep in-house.
https://www.reddit.com/r/sysadmin/comments/1xva8nt/no_youre_not_going_to_migrate_off_m365/
The following are excerpts and translations of user comments from the thread.
The convenience of relying on a common foundation and the weaknesses revealed this time
This time, a common dependency on the email infrastructure widened the impact
The reason the impact spread to calendars, Copilot, and security features is that they all rely on email and calendar data stored in Exchange Online and depend on connections to it.
That interconnectedness is also a source of everyday convenience. The reason Copilot can reference emails and files at once to answer questions like "What emails do I need to prepare for next week's meeting?" is because services within the same company are connected. The same reason applies to being able to create a meeting from a calendar and send an invitation email directly.
Being able to standardize operational settings and employee training into a single system is also cited as a benefit of using them together.
Some of Microsoft's protection features are difficult to replicate in the same way with services from other companies like Google.
When Sony Network Communications announced its adoption of a new Google environment at a Google event, they explained that granular controls, such as encrypting labeled files and restricting who can open them, could not be replicated in the same way on the Google side.
They compensated for the missing parts through employee training and monitoring of logs.
On the other hand, basic functions such as Teams calls, chats, and directly opening materials saved in file-sharing services remained usable. The extent to which the impact of the outage was isolated within the same service will become clear in Microsoft's detailed post-incident report.
The AWS and Cloudflare outages that occurred in 2025 were about the systems that support many web services behind the scenes stopping, but what was affected this time are the very tools used in the workplace every day.
Related Articles
Further considerations and analysis are covered on the main blog.
▼ In the field where it was confirmed, they switched to methods that were not down
▼ The choice to separate or migrate involves different goals and costs
Related Book Introduction
"Geopolitics of Digital Infrastructure: Internet, Data Centers, AI - Who Holds the Key Points?"
Written by Makoto Shirahata (Nikkei BP / Published June 2026)
This book organizes the structure in which global services are gathering on invisible foundations such as clouds, data centers, and submarine cables, as well as the mechanism by which such concentration causes a single failure to spread into a wide-ranging outage. It makes visible where companies relying on large clouds are dependent, and also touches on how to have alternative means and room for negotiation. It is suitable for readers who want to think about the structure covered in this article—where the convenience of using everything together and common dependencies spread the impact—from the perspective of the infrastructure that lies outside of our work tools.
"The Textbook on System Failure Response [Revised New Edition]"
Written by Masaaki Kimura (Gijutsu-Hyohron Co., Ltd. / Published April 2024)
This book summarizes everything from detection to resolution when a system failure occurs, including how to divide roles, necessary records, how to notify users, and daily training. It is intended for a wide range of readers involved in IT services. It is suitable for readers who want to organize the scenes covered in this article—where government ministries and local municipalities switched to telephones and other methods to keep work running on the day of the outage—as a way for organizations to move when facing failures.
As an Amazon Associate, Sekahan earns income from qualifying purchases.
Follow Sekahan
We also explain the background of the news on YouTube.
Main video for this topic
X (formerly Twitter)
#Microsoft365 #Outlook #SystemFailure #Cloud #OverseasReactions #NewsCommentary
