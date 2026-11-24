---
id: "b1b9880b617aed4d"
title: "How should an LLM see a computer?"
url: "https://greptile.com/blog/trex-computer-use"
link: "https://greptile.com/blog/trex-computer-use"
source: "Greptile"
domain: "greptile.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-23T17:19:25Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["dakshgupta"]
language: "en"
summary: "Introduction\nClaude Code and Codex can both use your computer. Under the hood they work in a similar manner: both can give the model a screenshot and an accessibility tree, a text description of every button on screen, and let it click by position or by naming an element.\nThe text version of the screen was built decades ago, for people who couldn’t see it. In 1984, two IBM mathematicians, Jim…"
tags: []
orgs: ["OpenAI", "Anthropic", "Microsoft", "Apple", "IBM"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1342
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50615520"
score: 54
comments: 24
community: "Hacker News"
---

# How should an LLM see a computer?

Greptile · dakshgupta · 2026-11-23

Introduction
Claude Code and Codex can both use your computer. Under the hood they work in a similar manner: both can give the model a screenshot and an accessibility tree, a text description of every button on screen, and let it click by position or by naming an element.
The text version of the screen was built decades ago, for people who couldn’t see it. In 1984, two IBM mathematicians, Jim Thatcher and his former thesis adviser, Jesse Wright, who was blind, started a side project to read the PC’s screen out loud. When GUIs turned the screen into pixels, apps had to start describing themselves instead. Microsoft shipped Active Accessibility in 1997, Sun started AT-SPI for Linux in 2001, and Apple added its Accessibility API in 2002.
This text has been useful for agents too. On the 2024 OSWorld benchmark, models looking only at screenshots completed about one task in twenty, whereas most models reading the screen as text performed better.
How do those results hold up with stronger models? We tested screenshots on their own and with the accessibility tree on seven models, and used the results to decide how our QA agent, TREX, should see the screen.
What's so hard about clicking a button?
A person clicks a button by moving the mouse to it. A model, on the other hand, looks at a screenshot and has to write the coordinates out as text (e.g., ‘x=523, y=217’) before clicking on it. Getting these numbers off by a few pixels can mean it clicks the wrong thing.
The same button sits at different coordinates on different screen and window sizes, so the guesses get worse when the resolution changes.
Also, the model’s vision works against it as it doesn’t see a screenshot pixel by pixel. The image is initially shrunk to fit the model's size limit, then cut into tiny squares, each dozens of pixels wide. But a click still has to land on one exact pixel.
Small targets are hard. On ScreenSpot-Pro, a 2025 benchmark with tiny targets on high resolution screens, the best model at release hit the right target only 18.9% of the time. Anthropic’s own docs warn that Claude “might make mistakes or hallucinate when outputting specific coordinates.”
When OSWorld came out in 2024, human testers were able to complete 72% of its tasks, and the best model about 12%. The authors found that models struggled with two things: turning ‘click Save’ into the right point on the screen, and knowing how to operate the software.
The first problem has a seemingly obvious fix. The accessibility tree already reveals each button's location, so the model doesn't have to go through the trouble of finding pixels. Go one step further, and the model doesn’t even need coordinates; it can pick a button by ID and let the harness click it. To test this, we built three setups, each building upon the last:
- Screenshots alone
- Adding an accessibility tree (clicking by coordinates)
- Adding clicks by element IDs
Every setup used the same agent on 172 OSWorld tasks, with one attempt per task, a 50-step limit and low reasoning effort, scored by OSWorld’s own graders.
Starting with screenshots
The model runs in a loop where it first sees a screenshot and past actions, picks an action (click coordinates, type or press keys), and then looks at the changes. It’s the simplest way to give a model a computer, and the one most agents start with. OSWorld’s baseline agent supports it, and Anthropic described its first computer use model as looking at screenshots and counting how many pixels to move the cursor.
We ran the same screenshot agent across seven OpenAI models:
On our 172 tasks, GPT-4.1 scored a mere 5.4% with screenshots alone, while the more recent GPT-6.1 Sol scored 83.8%. On the much harder OSWorld 2.0 offline set, OpenAI reports a score of 71.4% for GPT-6.1 Sol at maximum reasoning effort. The gap between the two models raised questions: do stronger models even need the tree, and can it help weaker ones catch up?
Adding the accessibility tree
Here, the model sees the screenshot with an accessibility tree beside it. We were interested in the tree because it can just tell the model what’s there, like a button labeled “Save” and where it sits. The model still clicks by coordinates here. The tree lists each element's position and dimensions in pixels, so the model can work out where to click after doing the math. With the clicking kept constant, the only thing that changed was what the model saw.
OSWorld runs on Linux, and so our agents read AT-SPI. The app's toolkit, such as GTK and Qt, describes what's on screen and passes on those descriptions to any program that asks for them, without prompting the user for permissions. Also, while testing, we realized that GIMP was missing from the tree until we added back an environment variable set at login.
In the evals, trees helped every model that struggled with screenshots. GPT-5.2 went from 15.8% with screenshots alone to 36.2% after the tree was added, and GPT-4.1 from 5.4% to 20.6%. On the other hand, stronger models barely moved. GPT-6.1 Sol got 82.7% when the tree was added, slightly lower than with screenshots alone (83.8%) and none of the three strongest models changed by a statistically significant amount.
Clicking by ID
Next, we gave each element in the tree an ID. The model can simply name the element it wants and the harness clicks it. This bypasses the problem of clicking the exact pixel.
For weaker models, ID clicks boosted performance on top of the tree. GPT-5.2 went from 36.2% with the tree + coordinates to 52.8% when it clicked by ID, and GPT-4.1 from 20.6% to 29.3%. Put together, the tree and ID clicks more than tripled GPT-5.2’s score with screenshots alone (15.8%).
Again, this experiment didn't do much for the strongest models. GPT-6.1 Sol scored 82.7% clicking by coordinates and 82.1% clicking by ID.
It depends on the model
For the three strongest models, neither step made a difference. Across both steps, the four weaker models gained 9 to 37 points with the tree and ID clicks, more than doubling their scores in three of four cases. If you’re building on weaker models, the tree is still worth adding.
Some apps publish no tree at all. A canvas app like Figma publishes its toolbar buttons, but the canvas itself is just pixels, and a game like Doom is pixels from top to bottom. Even in apps with a good tree, some bugs only show on screen, like text that overflows its box. The screenshot covers all of these.
TREX Computer Use
Code review catches bugs in the diff. Some bugs only exist when the software is running: a button that can’t be clicked, a label that runs off the edge of the window. Until now, catching those took a person opening the app and simulating the user flow. By writing more code and touching more of the UI than any team can check by hand, coding agents have made it hard for programmers to keep up.
That’s why we built computer use into TREX. It runs the changes in your pull request on an actual desktop and uses the app the way a person would, so you can see that the feature you asked for is the one that got built.
How TREX sees the screen came out of these experiments. It runs on the best models and relies on the screenshot at every step. It uses the accessibility tree to click by ID when it can, and coordinates when the tree doesn't have the element, like a canvas or a game.
How a model should see the screen depends on the model, so we'll rerun these experiments each time a new one comes out and update TREX when the answer changes.
When something breaks on screen, TREX catches it, and shows you what happened.
Try TREX on your next pull request.
