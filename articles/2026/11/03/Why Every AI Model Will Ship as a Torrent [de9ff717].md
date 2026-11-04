---
id: "de9ff717e24f84b5"
title: "Why Every AI Model Will Ship as a Torrent"
url: "https://pirateface.co/articles/one-model-one-swarm"
link: "https://pirateface.co/articles/one-model-one-swarm"
source: "pirateface.co"
domain: "pirateface.co"
source_type: "community"
collector: "hackernews"
date: "2026-11-03T22:36:22Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["ahoyychips"]
language: "en"
summary: "DeepSeek's DeepSeek-V4.1-Flash-1017 consists of 48 safetensors shards plus configuration and tokenizer, totaling 510 GB. Once published, these files do not change and everyone who wants to run the model downloads the same bytes. Because of this, torrents are perfect for model distribution.\nMovies are different. Search for a movie on a torrent site and you'll see 4K remux, 1080p, 720p, and…"
tags: []
orgs: ["DeepSeek", "Google"]
topics: ["models & research", "search & media"]
content_source: "fulltext"
word_count: 535
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50359225"
score: 21
comments: 4
community: "Hacker News"
---

# Why Every AI Model Will Ship as a Torrent

pirateface.co · ahoyychips · 2026-11-03

DeepSeek's DeepSeek-V4.1-Flash-1017 consists of 48 safetensors shards plus configuration and tokenizer, totaling 510 GB. Once published, these files do not change and everyone who wants to run the model downloads the same bytes. Because of this, torrents are perfect for model distribution.
Movies are different. Search for a movie on a torrent site and you'll see 4K remux, 1080p, 720p, and various versions with audio tracks and subtitles. Each version is a separate torrent, and the audience is dispersed into many small swarms. Most people can just pick any one that can play, but no one downloads models like this: anyone who wants DeepSeek-V4.1-Flash-1017 wants the same 48 shards.
Name comes from content
To understand why this is important, you first have to look at where torrents get their name. Each torrent is named with a hash of its content. No matter who makes a torrent with the same files and settings, the resulting hash will be the same.
The earliest v1 format (BEP 3) connects all files end to end, cuts them into blocks of the same size, uses SHA-1 to calculate a hash for each block, and then puts these hashes together with the file name and block size into a structure called an info dictionary. The SHA-1 of this dictionary is a 40-digit hexadecimal string.
The later v2 format (BEP 52) is even better for model distribution. It no longer concatenates files together, but builds a separate Merkle tree for each file: each 16 KiB data block is hashed with SHA-256, and then merged two by two and continues to calculate until only one root hash is left for each file.
Hybrid torrents carry both sets of hashes in the same info dictionary, so v1 and v2 clients can stay in the same swarm.
Find each other: tracker and Model DHT
Even with a common name, downloaders still need to find each other. The easiest way is to ask a tracker. The tracker is a server: you ask it "Who else has be10fee2...?" and it tells you which nodes are sharing. Every Pirate Face magnet link comes with udp://tracker.pirateface.co:6969/announce.
The Model DHT, a distributed hash table, can answer the same question without relying on a central server. It is a table scattered across millions of torrent clients. You can use the torrent's hash to find the nodes that are sharing this torrent.
When searching, the client first asks for the nodes it knows that are closest to the target, and then these nodes tell it closer nodes. Even if there are millions of nodes in the network, it only takes a few steps to find them.
The front page of the Model DHT
The early web went through a similar phase. First there were manual directories like Yahoo!, then full-text search like AltaVista. It wasn't until 1998, when Google started sorting by links between web pages, that most people really had a way to find things. The Model DHT can help you find nodes, but there is no front page that tells you which torrent to look for.
Pirate Face can be your front page to the Model DHT: a verified torrent for each model version, a tracker and real-time swarm data.
