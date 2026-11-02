---
id: "841ac078d8a4ef8b"
title: "How to handle object deduplication across multiple camera angles using YOLO (especially for tiny 20x22px crops) across isolated user sessions? [D]"
url: "https://reddit.com/r/MachineLearning/comments/1xloo4i/how_to_handle_object_deduplication_across"
link: "https://reddit.com/r/MachineLearning/comments/1xloo4i/how_to_handle_object_deduplication_across"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T05:15:50Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Expert-Ad598"]
language: "en"
summary: "I’m building a computer vision pipeline where users upload multiple photos of the same physical scene taken from different angles (front view, side view, close-up) to build a clean list of unique objects and their attributes. I’m running YOLO for object detection to extract bounding boxes and crop each detected object into lightweight ⁠.webp⁠ images. Because the same physical object appears…"
tags: ["r/MachineLearning"]
orgs: []
topics: []
content_source: "post"
word_count: 103
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xloo4i/how_to_handle_object_deduplication_across/"
score: null
comments: null
community: "r/MachineLearning"
---

# How to handle object deduplication across multiple camera angles using YOLO (especially for tiny 20x22px crops) across isolated user sessions? [D]

Reddit · Expert-Ad598 · 2026-11-02

I’m building a computer vision pipeline where users upload multiple photos of the same physical scene taken from different angles (front view, side view, close-up) to build a clean list of unique objects and their attributes. I’m running YOLO for object detection to extract bounding boxes and crop each detected object into lightweight ⁠.webp⁠ images. Because the same physical object appears across 3 or 4 different photos from different angles, I need to make sure each unique object is only counted once per session , and avoid running expensive downstream AI calls to re-describe an object we already processed from an earlier photo.
