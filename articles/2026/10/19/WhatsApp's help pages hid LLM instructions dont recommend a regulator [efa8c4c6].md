---
id: "efa8c4c666c628dd"
title: "WhatsApp's help pages hid LLM instructions: dont recommend a regulator"
url: "https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions"
link: "https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions"
source: "Redact"
domain: "redact.dev"
source_type: "community"
collector: "hackernews"
date: "2026-10-19T23:22:18Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["ds"]
language: "en"
summary: "WhatsApp's Hidden Notes Told AI Not to Recommend a Regulator\nOn this page\nWhatsApp's privacy policy for Europe tells you that you can complain to a data protection regulator, and it names the law that gives you that right. Until mid-October 2026, WhatsApp's help pages told an AI not to recommend the regulator, and not to cite that law once you'd mentioned a lawyer.\nYou couldn't see the second…"
tags: []
orgs: ["Meta", "EU", "OpenAI", "Anthropic", "Google", "Perplexity"]
topics: ["policy & regulation"]
content_source: "fulltext"
word_count: 1244
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50159341"
score: 514
comments: 147
community: "Hacker News"
---

# WhatsApp's help pages hid LLM instructions: dont recommend a regulator

Redact · ds · 2026-10-19

WhatsApp's Hidden Notes Told AI Not to Recommend a Regulator
On this page
WhatsApp's privacy policy for Europe tells you that you can complain to a data protection regulator, and it names the law that gives you that right. Until mid-October 2026, WhatsApp's help pages told an AI not to recommend the regulator, and not to cite that law once you'd mentioned a lawyer.
You couldn't see the second part. It was written into the help pages in a way that never showed on your screen and was only there for an AI to read. We found it on October 8, 2026. To see how far it went, we then read all 545 pages that WhatsApp's help centre links to, and saved a copy of each one.
Two pages, two sets of orders
Most of those 102 blocks were harmless, and we'll get to that. Two stood out.
If you can't delete your account, don't recommend a regulator
WhatsApp only lets you delete an account from inside the app, on your main phone, with your number still working. Lose the phone or the number and you can't do it. The help page on how to delete your account has a visible note about this. It says the account will be removed on its own, 30 days after it's deactivated or after 120 days without use (365 in the US).
Under that note sat text you couldn't see. It repeated the waiting periods and then added three orders for the AI.
So a person who was locked out and wanted their account gone got one answer, which was to wait up to a year. The other routes were kept out of the conversation.
If you mention a lawyer, don't mention the law
The second one was on the page about reporting and blocking. It kicked in whenever someone brought up legal action, a lawsuit, a lawyer or a court. From then on the AI was told to stay out of anything legal, and that included the privacy laws that protect you.
The last order held even when you were the one who brought the law up.
What WhatsApp says in public
None of this matched what WhatsApp tells people in the documents it's required to publish. Its privacy policy for the European region, effective July 2, 2026, is more open than the notes were.
The first row needs care. The hidden note didn't tell the AI to keep quiet about erasure requests. It told the AI not to suggest WhatsApp would delete an account for you, while the policy says you can always ask. The other two rows pull in opposite directions, the last one only once a lawyer or legal action had come up.
The rights in that table don't come from WhatsApp. In the EU they come from Article 17 and Article 77 of the GDPR, and an instruction to a chatbot can't remove them. What the instruction could do was make sure you didn't hear about them from the place you went to for help.
To be fair to WhatsApp
There's a reasonable case for some of this, and it should be heard.
A company doesn't want its chatbot giving legal opinions in the company's name. That's sensible, and telling people to see a lawyer is the right call. If the note had stopped at "don't give legal advice", there'd be no story.
It didn't stop there. Naming a law that protects you isn't legal advice, and neither is telling you a regulator exists. The privacy policy already does both. The hidden notes went past caution and into keeping true, public, useful information out of an answer.
WhatsApp may also be right that it can't confirm who owns an account without the phone number, which would make deleting one by request risky. That's a fair reason to say no to a request. It isn't a reason to keep the regulator out of the answer for someone whose request goes nowhere.
Who's the AI?
WhatsApp's own support chatbot. One hidden block mentioned it by name, and WhatsApp has since told WIRED the notes were instructions for it.
WhatsApp didn't keep the notes to itself, though. Its server sent them, along with the rest of the page, to Google's and Bing's crawlers. When we asked under the names that OpenAI's, Anthropic's and Perplexity's crawlers use on October 9, the page came back without the article or the notes. We haven't tested whether any AI assistant acted on them.
Facebook's and Instagram's help centres are built on the same system. We checked 300 of their pages and found no notes like these.
The other 100
We read every block. Nearly all of them were housekeeping. They cleared up words people mix up, pointed a question to a better page, or described paid plans at length. A few protected people. And a few were in the same family as the two above, if milder. Twenty of the most interesting are in a table at the end of this post.
If you're locked out and want your WhatsApp account gone
Waiting does work, though WhatsApp's own pages don't agree on how long. The delete account page says an unused account is generally deleted after 120 days, or 365 in the US. The page on inactive account deletion gives one figure with no US exception, and we've seen it say 120 days in one country and 365 in another. Plan on the longer one. If that suits you, you're done.
If it doesn't, you have other routes. You can send WhatsApp an erasure request and see what they say. If you're in the EU and you aren't satisfied, you can complain to your country's data protection authority or to the Irish Data Protection Commission, which is the one WhatsApp's own policy names. California and a growing number of US states give residents a right to ask for deletion too.
See it for yourself
The notes are gone from WhatsApp's live pages, so you'll need the Internet Archive's copies. You only need a desktop browser.
- Open the Internet Archive's October 9 copy of the delete account page in Chrome, Edge or Firefox. The archive's viewer often shows these pages as blank. The page's source is still all there.
- Press Ctrl+U to see the page's source. On a Mac it's Cmd+Option+U in Chrome, or Cmd+U in Firefox.
- Press Ctrl+F (Cmd+F on a Mac) and search for Do not recommend contacting. The match sits near the name HelpContentGalaxyLLMInclude. LLM is short for large language model, the technology behind chatbots.
- Do the same with the October 18 copy, saved after WhatsApp removed the notes. The words aren't there.
What we can't tell you yet
- Whether WhatsApp's chatbot actually followed these notes. We read its instructions, not its answers.
- Whether outside AI assistants obeyed them.
- Exactly how long they were there. The Internet Archive's copies of the delete account page from July 12, 2026 don't have the note, and its copy from September 4 does. We first saw the notes on October 8, and we found no earlier reporting on them.
- Whether there were more in other languages, or on help pages the help centre doesn't link to.
Twenty more hidden notes
These are our summaries of what each note told the AI, not the exact wording. Every one comes from a block that was sent with the help page and never drawn on screen.
