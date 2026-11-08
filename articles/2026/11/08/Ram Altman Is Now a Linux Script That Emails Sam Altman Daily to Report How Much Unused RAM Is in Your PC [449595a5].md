---
id: "449595a5fc048f01"
title: "\"Ram Altman\" Is Now a Linux Script That Emails Sam Altman Daily to Report How Much Unused RAM Is in Your PC"
url: "https://respawnfirst.com/linux-script-emails-sam-altman-unused-ram-ram-altman"
link: "https://respawnfirst.com/linux-script-emails-sam-altman-unused-ram-ram-altman"
source: "RespawnFirst"
domain: "respawnfirst.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T11:49:01Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Subulicious"]
language: "en"
summary: "Sam Altman is not having a good couple of weeks; ever since he said OpenAI’s ram needs are more important than consumer electronics, the internet has been unforgiving. But one man has taken things one step further to mock Altman’s ridiculous super villain sounding statements.\nOpen-source developer Iain Kay has created an open-source BASH script called “Ram Altman” for Linux systems designed to…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 398
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xqwn5n/ram_altman_is_now_a_linux_script_that_emails_sam/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# "Ram Altman" Is Now a Linux Script That Emails Sam Altman Daily to Report How Much Unused RAM Is in Your PC

RespawnFirst · Subulicious · 2026-11-08

Sam Altman is not having a good couple of weeks; ever since he said OpenAI’s ram needs are more important than consumer electronics, the internet has been unforgiving. But one man has taken things one step further to mock Altman’s ridiculous super villain sounding statements.
Open-source developer Iain Kay has created an open-source BASH script called “Ram Altman” for Linux systems designed to monitor how much idle RAM you have sitting on your rigs, laptops, etc.
The percentage of unused RAM is than emailed to Sam Altman… well not really. The correspondence depends on how you set it up. By default, the email server isn’t set up out of the box.
The creator intentionally designed it this way to prevent the repository from being used as an automated mail-spoofing or denial-of-service tool against OpenAI’s servers.
If a system has more than 10% of its total RAM available, “Ram-Altman” selects from a rotating bank of sarcastic email templates:
“Hi Sam,” reads one of the sample messages. “Please don’t be alarmed, but there is 8.6 GiB of RAM on my desk that isn’t in a data centre. That’s 56.2% of what’s installed here, and as far as I can tell it has no plans today. Hoarding responsibly, A concerned RAM owner.”
For sysadmins and Linux users hesitant to spam external mail servers, the repository includes a –dry-run flag and a local test suite. This allows users to test simulated memory workloads and preview the exact message generated without dispatching actual correspondence. Unless the user has the technical know-how on how to set it up that way.
The project’s FAQ page is also pretty funny:
- Does this help with the DRAM shortage? “No.”
- Does it work on macOS? “No, it reads /proc/meminfo. On the other hand, your RAM is probably soldered down, which makes you the hardest target in the global allocation programme.”
- Why is the threshold 10%? “Below that, your machine has suffered enough.”
- Does running this use RAM? “Briefly. It’s then returned to the global pool, which is more than can be said for the rest of us.”
The internet is not letting up and it did force Sam Altman to backtrack on what he said earlier. In a recent post on X, Sam Altman said his statement was taken out of context and that he wants everyone to have as much as they want.
