---
id: "9e18e9d68e851570"
title: "Ginux: A New Kernel Runs Linux Userspace, Made via Human-Directed AI Engineering"
url: "https://zenodo.org/records/23682548"
link: "https://zenodo.org/records/23682548"
source: "Zenodo"
domain: "zenodo.org"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T11:30:27Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["ForHackernews"]
language: "en"
summary: "Ginux: Building an Independent Kernel That Runs Linux Userspace through Human-Directed Agentic Engineering\nDescription\nThis report presents Human-Directed Agentic Engineering (HDAE), a method for building complex software by combining human-defined architecture, constraints, milestones, acceptance criteria, and stopping points with an autonomous implementation, execution, diagnosis, and revision…"
tags: []
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 186
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50424147"
score: 32
comments: 62
community: "Hacker News"
---

# Ginux: A New Kernel Runs Linux Userspace, Made via Human-Directed AI Engineering

Zenodo · ForHackernews · 2026-11-09

Ginux: Building an Independent Kernel That Runs Linux Userspace through Human-Directed Agentic Engineering
Description
This report presents Human-Directed Agentic Engineering (HDAE), a method for building complex software by combining human-defined architecture, constraints, milestones, acceptance criteria, and stopping points with an autonomous implementation, execution, diagnosis, and revision loop. The experiment examines what this development model can accomplish and the domain expertise and executable validation required to keep it aligned
Ginux serves as the experimental case study. Over eleven days, one persistent coding-agent task produced an independent Rust-first x86-64 kernel that boots through UEFI, implements its own core operating-system mechanisms and Linux compatibility layer, executes selected unmodified Alpine Linux programs, and boots a Rocky Linux 10 userspace with systemd through multi-user.target.
Ginux demonstrates the rapid integration of established systems mechanisms, but it remains a research prototype. Its compatibility and hardware coverage are narrow, it has not received an independent security audit, and it makes no claim to production readiness or equivalence with Linux.
Files
      
        ginux-ai-systems-report.pdf
        
      
    
      
        Files
         (96.6 kB)
        
      
    
Additional details
              
                Software
              
            
- Repository URL
- https://github.com/gmkurtzer/ginux
- Programming language
- Rust , Assembly
- Development Status
- Concept
