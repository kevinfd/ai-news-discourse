---
id: "82a04cffc8a8a9f7"
title: "Created a workflow to help track if I am meeting my work goals for the year"
url: "https://reddit.com/r/ClaudeAI/comments/1xy0cim/created_a_workflow_to_help_track_if_i_am_meeting"
link: "https://reddit.com/r/ClaudeAI/comments/1xy0cim/created_a_workflow_to_help_track_if_i_am_meeting"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T20:30:51Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["rgupta0747"]
language: "en"
summary: "Hi all, I know this isn’t as sexy as building a video game or something, but I managed to create a workflow I’m proud of and wanted to share. Im a software engineer and use Claude code for work. With my year-end self assessment due I decided to try using Claude to help me write it up (we received access this year). Rather than go back and figure out all the work I did I realized I could just use…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 473
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xy0cim/created_a_workflow_to_help_track_if_i_am_meeting/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Created a workflow to help track if I am meeting my work goals for the year

Reddit · rgupta0747 · 2026-11-16

Hi all, I know this isn’t as sexy as building a video game or something, but I managed to create a workflow I’m proud of and wanted to share. Im a software engineer and use Claude code for work. With my year-end self assessment due I decided to try using Claude to help me write it up (we received access this year). Rather than go back and figure out all the work I did I realized I could just use Claude to figure it out for me and summarize it nicely. Currently I work on two proprietary OSs that work across different products. Which means I have two seperate codebases. I use my laptop to remote ssh to two machines, one that contains workspaces for one OS and one that contains the workspaces for another OS. Both machines have Claude installed on them. On my laptop I asked Claude to setup the 2026 folder, then do a nightly cron write of my git commits for each code base, and then each morning scp it to my laptop. It then runs a summary of the previous week Monday at noon. It also does a quarterly rollup every 8th of January April July and October. It uses an internally developed mcp server to pull all my reports from our defect tracking system and feature tracking system so it knows what I’m working on and the progress for each. It also searches the review board we use to see which code is currently pending code review. It then runs a scoring algorithm to see how I am doing progress-wise on my goal. At each quarter (April, July, October) Claude analyzes my progress of what I’ve done compared to the goals I set on our performance portal and sends me an email of how I’m doing and what I should improve on. Then on November 15th it generates a year end review I can copy and paste into the portal. The idea for this is I don’t normally track my goals and progress through the year. I do my work and when the year comes to the end I'm going through emails and inboxs and trying to figure out what I did. Now Claude can figure it out for me and even use what I did to write next years goals based on how I’m doing. I know I’m not a power user. We only just received approval to use AI tools at work this summer. Before that I used to think AI was nothing more than a gloried google search. This is the first time I’m really starting to understand it’s capabilities am I’m proud of what I created for myself. TLDR asked Claude to automate my performance review by tracking the work I’ve done and running analysis every so often to see how I’m performing.
