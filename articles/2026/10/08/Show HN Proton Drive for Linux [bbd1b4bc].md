---
id: "bbd1b4bc84883cfe"
title: "Show HN: Proton Drive for Linux"
url: "https://oss.lsantos.dev/proton-drive-linux-fs"
source: "oss.lsantos.dev"
domain: "oss.lsantos.dev"
source_type: "community"
collector: "hackernews"
date: "2026-10-08T09:10:42Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["khaosdoctor"]
language: "en"
summary: "Hello everyone, I wanted to share this small project that I have.\nIt's born out of a necessity that I had, because Proton doesn't ship a Linux version of the drive yet (it's apparently coming out later this year but who knows?) and all the current solutions are hacky and wonky at best. But for the time being I really needed to mount my Proton drive on my Linux machine the way I mounted it on my…"
tags: []
orgs: ["Google"]
topics: []
content_source: "fulltext"
word_count: 314
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50003545"
score: 122
comments: 45
community: "Hacker News"
---

# Show HN: Proton Drive for Linux

oss.lsantos.dev · khaosdoctor · 2026-10-08

proton-drive-linux-fs¶
A FUSE virtual filesystem that mounts Proton Drive as a local folder on Linux.
What it does¶
This package mounts your Proton Drive at a directory you choose. All the files and folders are listed from Proton's metadata directly. But we also don't download the file content from all your files either, instead the files are downloaded on demand when you read them. This is a "lazy" approach that saves bandwidth and disk space. Like Google Drive, Dropbox, OneDrive, etc.
Remote changes reach the mount through Proton's event feed, which invalidates the affected directory listings and cached file content. Writes are buffered to a local temp file and uploaded to Proton in full a set timeout when the file closes.
Status¶
This is early and unofficial. Not affiliated with, endorsed by, or supported by Proton AG.
I have tested the most common paths, like: read, write, create, delete, rename and move operations on one Proton Drive share. But everyone has a different setup, and I can't test them all.
Expect bugs. Report them on the issue tracker.
Quick start¶
See Quick start for a complete copy-paste flow.
Components¶
Your apps don't talk directly to proton. Reads and writes go through the kernel's FUSE layer to the mount daemon, which is the only piece that speaks to Proton's API. So all the communication is locked in this layer to avoid leaks of your credentials or data.
The tray, and any future developments (probably a GUI), talk to that same daemon over its local unix socket, falling back to a status file when the socket is not available. Ideally, it will stay working no matter what happens.
flowchart LR
    App["User application"] --> Kernel["Kernel FUSE"]
    Kernel --> Daemon
    subgraph Daemon["proton-drive-fs daemon"]
        direction LR
        FS["fusefs"] --> Drive["drive"] --> Auth["auth"]
    end
    Daemon --> API["Proton API"]
    Tray["Tray"] -->|"unix socket, status file"| Daemon
    GUI["Future things"] -.->|"unix socket, status file"| Daemon
