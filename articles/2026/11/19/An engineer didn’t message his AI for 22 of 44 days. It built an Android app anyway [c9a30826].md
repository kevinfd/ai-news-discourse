---
id: "c9a308268606a4dc"
title: "An engineer didn’t message his AI for 22 of 44 days. It built an Android app anyway."
url: "https://thenewstack.io/cognition-devin-bots-management"
link: "https://thenewstack.io/cognition-devin-bots-management"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T20:22:18Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Cognition has spent nearly three years developing Devin as an autonomous engineer that takes a ticket and ships a pull request. \n\n With Tuesday’s launch of Devin Bots , the company is moving into management, introducing persistent agents that oversee multiple Devin coding sessions, and take responsibility for engineering outcomes over days or weeks. \n\n Coordination becomes the product \n\n CEO…"
tags: ["AI Agents", "AI Engineering", "Developer tools"]
orgs: ["Google"]
topics: ["agents & coding", "products & launches", "robotics & autonomy"]
content_source: "summary"
word_count: 747
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# An engineer didn’t message his AI for 22 of 44 days. It built an Android app anyway.

The New Stack · Amanda Caswell · 2026-11-19

Cognition has spent nearly three years developing Devin as an autonomous engineer that takes a ticket and ships a pull request. 

 With Tuesday’s launch of Devin Bots , the company is moving into management, introducing persistent agents that oversee multiple Devin coding sessions, and take responsibility for engineering outcomes over days or weeks. 

 Coordination becomes the product 

 CEO Scott Wu argues that eliminating even a small amount of remaining human work could produce outsized productivity gains. In a post on X , he asks how much more developers could accomplish if coding agents went from handling 98% of their work to 99%, and says Cognition had seen enormous differences among beta testers and internal teams. 

 The percentages are hypothetical, but Wu is making the case that coordination, not just coding, is the next opportunity for automation. 

 The percentages are hypothetical, but Wu is making the case that coordination, not just coding, is the next opportunity for automation. 

 From tickets to targets 

 Cognition founding team member Silas Alberti described the change in a post on X as a move toward assigning agents ongoing goals instead of individual tasks. He says the team has already used Devin Bots to compress weeks of research into days. 

 The company shares the example of keeping an Android app in sync with its iOS version. As new features are added to iOS, a Devin Bot can assign the corresponding Android work without an engineer having to create a ticket for every update. 

 The idea builds on a trend toward coding agents that function as team members . Devin Bots takes that a step further by putting an agent in charge of coordinating the work. 

 An Android app, barely supervised 

 When the company set out to build an Android version of Devin, it had no dedicated Android engineers. Instead, the company assigned the project to a Devin Bot on September 28 and let it coordinate the coding work. 

 Over the next 44 days, Cognition says the Bot merged 1,134 pull requests, wrote 344,651 lines of Kotlin and closed 1,217 tickets. It also ran 2,841 screenshot tests. The engineer overseeing the project sent 183 messages during that period, including none on 22 of those days. 

 In its write-up , Cognition explains that the Bot opened tickets and assigned them to individual Devin sessions, then merged changes once they passed continuous integration and Devin Review. The team could follow along through daily Slack updates that included screen recordings. The Android app is now in open testing on Google Play, though it still needs work before it matches the iOS version. 

 Cognition’s Layout Bot checks the company’s web app for visual bugs every three hours, rebuilds the latest production code, and tests the interface under different loading conditions. Engineers merged 159 of its fixes over three weeks, reducing layout lag by 70%, according to Cognition. 

 Cognition says the studio went from producing around 50 pull requests a week to 1,900. 

 A mobile game studio also has roughly 20 bots reporting to another agent named Super Jenny. Four times a day, Super Jenny brings decisions to a human operator. Cognition says the studio went from producing around 50 pull requests a week to 1,900. 

 Where oversight runs thin 

 Multiple coding agents working on the same project can introduce conflicting dependencies or bugs that affect other agents’ work. Cognition hasn’t explained how Devin Bots handle those conflicts. 

 Tasks requiring approval go to a “Needs You” inbox for an engineer to review. 

 Developers can protect specific CI checks and set compute spending limits before assigning a project to a Bot. Tasks requiring approval go to a “Needs You” inbox for an engineer to review. The company hasn’t disclosed how the supervising Bot decides when code is ready to merge or when repeated failures warrant human intervention. 

 Code verification remains another concern when agents write tests for their own implementations. Agent-generated pull requests are already putting pressure on conventional code review pipelines , and some teams are developing independent verification loops to catch errors that the original coding agent might miss. 

 The New Stack has asked Cognition for more information about how Devin Bots coordinate parallel agents, evaluate completed work and determine when human intervention is necessary. 

 Cognition hasn’t disclosed how much engineering time was spent reviewing the Bots’ pull requests or fixing failed implementations. 
 The post An engineer didn’t message his AI for 22 of 44 days. It built an Android app anyway. appeared first on The New Stack .
