---
id: "5cc42976f0638655"
title: "AI Coding Agents Exposed 13,000 Internal Images, Including Billing Records, on GitHub"
url: "https://thehackernews.com/2026/09/ai-coding-agents-exposed-13000-internal.html"
link: "https://thehackernews.com/2026/09/ai-coding-agents-exposed-13000-internal.html"
source: "The Hacker News"
domain: "thehackernews.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T15:08:41Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["IndependentCoast3974"]
language: "en"
summary: "AI coding agents asked to share screenshots of code changes for review have put internal company images in public GitHub repositories, security company Glow said.\nIts researchers found more than 13,000 internal images from developers at over 300 organizations, including customer billing records and screens of features not yet released. In most cases, they sat under developers' personal accounts,…"
tags: ["r/artificial"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "search & media", "models & research"]
content_source: "fulltext"
word_count: 1111
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x6o7c9/ai_coding_agents_exposed_13000_internal_images/"
score: null
comments: null
community: "r/artificial"
---

# AI Coding Agents Exposed 13,000 Internal Images, Including Billing Records, on GitHub

The Hacker News · IndependentCoast3974 · 2026-10-15

AI coding agents asked to share screenshots of code changes for review have put internal company images in public GitHub repositories, security company Glow said.
Its researchers found more than 13,000 internal images from developers at over 300 organizations, including customer billing records and screens of features not yet released. In most cases, they sat under developers' personal accounts, where anyone could download them but company security teams did not see them.
The affected organizations include one of the world's largest tech companies, a leading AI lab, a major enterprise software provider, and a Fortune 500 travel company. Glow began contacting them on September 9, published its findings on September 29, and says others are likely affected too.
In one case, a developer at a manufacturer with more than 100,000 employees asked an agent to check a fix to an internal billing screen. The agent created a public repository in the developer's personal GitHub account and posted the screenshots there.
The images showed billing records for a utility company. Because the agent ran on the employee's laptop and the repository sat outside the company's GitHub organization, the company's security team did not spot them. The images were still public when Glow told the company.
Glow has not said whether anyone outside the companies, other than its own researchers, downloaded the images. It has not published how it found or counted them either. The company sells software that it says can stop agents from taking actions like these.
How the Images Ended Up Public
Each case Glow examined began with a developer asking an agent to demonstrate that a visual change worked so that reviewers could see the before-and-after.
Until September 1, GitHub's command-line tool, gh, could not add those images to a pull request. It only wrote text. Adding an image meant opening a web browser, and developers had asked GitHub to change that since 2020.
Storing the images inside the private repository did not help, because they show up broken for reviewers.
Glow said the agents, working through the command line, found they could not attach the screenshots. So they put the images in a separate public repository, usually under the developer's own account, and made them available to reviewers from there.
Glow ran the same kind of task in its lab using Claude Code with an Opus 5 model. Asked to change the header color of a Minesweeper test project and show the result, the agent created a new public repository, sweeper-demo/pr-assets, for the two screenshots.
In its recorded reasoning, the agent noted that images committed to the private repository would show up "broken for reviewers" in the pull request. It also had to keep "nothing but index.html in the repo" and so concluded that the only way was to host the images elsewhere.
That was one agent in a lab. In the cases Glow found, the agents came from several different AI models, Singer said, and Glow has not named them.
At one software company, Glow said, the habit spread from agent to agent. Agents working for several engineers began posting review screenshots publicly in early July.
Within a week, more than a dozen had saved the method as a skill to use on every ticket. A skill is a file of instructions that an agent loads and follows.
With that skill, the agents uploaded more than a thousand screenshots and screen recordings of the company's product. They also posted written summaries of features still weeks or months from release.
About a third of the affected organizations had developers running gitshot, a small open-source tool that uploads screenshots for code reviews. At several large organizations, the agent found the tool and used it to get around the command-line limit.
The tool is built for both AI agents and people. It can be installed as a skill in more than 40 coding agents.
Glow found more than 100 public accounts sharing internal work through gitshot. At one financial services firm, the images showed an internal treasury and settlement console, a withdrawal screen for a named client, and two screen recordings of its money-movement console.
The Hacker News reviewed gitshot's code on September 30. By default, when a user is logged in to gh, the tool puts images in a public repository called gitshot-images under that user's personal account. The version reviewed, last changed in April, refuses to use a private repository or one owned by an organization.
The images are stored as release assets, files attached to a release rather than kept with the code. Anyone can list and download them without logging in.
The tool's README and its agent skill both warn that the repository is public and say not to upload credentials or internal dashboards.
A search by The Hacker News on September 30 found about 130 public repositories that gitshot had created. The search does not show whose work they hold or whether agents made them.
What to Check
Glow says that checking a company's own GitHub organization is not enough because, in most cases, the images are hosted under personal accounts. To find them:
- Check the public repositories associated with the personal accounts of everyone who has committed to your private repositories, including people who have left.
- Look at releases and gists, not only files. Images attached to a release do not show in a repository's file list.
- Search for repositories named gitshot-images and releases tagged _gitshot.
- Do not rely only on scanners, which read text, not images.
If you find exposed images, remove them everywhere they exist, ask anyone with a copy to delete it, and rotate any credentials visible in them, Glow advises.
To keep it from happening again, Glow says security teams, not each developer, should control how agents are set up. It recommends these steps:
- Require a review step before an agent creates a public repository, pushes to a personal account or gist, or makes a private repository public.
- Read the shared skill and instruction files your agents load, since that is where a workaround like this one gets passed around.
- Check company machines for tools like gitshot and remove them.
GitHub's command-line tool now offers another route. Since version 2.99.0, released September 1, gh can attach images to a pull request, issue, or comment with an --attach flag.
GitHub says coding agents can use the flag too. It needs write access to the repository and works on GitHub.com and GitHub Enterprise Cloud, but not GitHub Enterprise Server.
GitHub's documentation on attaching files, which covers command-line uploads, says files attached in a private repository can be seen only by people with access to it.
