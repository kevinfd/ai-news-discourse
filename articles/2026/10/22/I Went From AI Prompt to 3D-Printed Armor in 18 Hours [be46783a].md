---
id: "be46783af07bfe44"
title: "I Went From AI Prompt to 3D-Printed Armor in 18 Hours"
url: "https://cnet.com/tech/computing/i-went-from-ai-prompt-to-3d-printed-armor-in-18-hours"
link: "https://cnet.com/tech/computing/i-went-from-ai-prompt-to-3d-printed-armor-in-18-hours"
source: "CNET"
domain: "cnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T12:31:35Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["James Bricknell"]
language: "en"
summary: "What started off as a dare became a fully fledged app in less than a day"
tags: ["3D Printers"]
orgs: ["Google"]
topics: ["models & research", "products & launches", "jobs & society"]
content_source: "fulltext"
word_count: 1420
paywalled: false
image: "https://www.cnet.com/wp-content/uploads/sites/2/image-19-2.png"
discussion_url: null
score: null
comments: null
community: null
---

# I Went From AI Prompt to 3D-Printed Armor in 18 Hours

CNET · James Bricknell · 2026-10-22

Tuesday morning, I received a notification from Google saying I could try out the new Gemini 4 Argon model. Normally, I just ignore it — I don’t really care which model it is, as long as it can help me with my day-to-day — but this time Google teased me with something close to my heart.
Gemini said it could “Create an app to model lampshades that I can 3D print.” My response, as CNET’s resident 3D printing expert, was, “I bet you can’t.”
Turns out, yes, it can.
More from CNET
I went from these first few screenshots to a fully 3D-printed object in under 18 hours, and I’m impressed by how easy it was.
I’ll say upfront that I don’t really like generative AI. I think it uses people’s art and creative work without fair compensation, and I want to pay artists for their work. I changed the project from making lampshades to making cosplay armor and deliberately limited it to things I can already make myself. I know how to model greaves, pauldrons and vambraces, so this takes away nothing.
In my mind, this is analogous to a blacksmith who gets an apprentice to make the blanks for steel armor. The fine detail and character of the work is done by one person, but the grunt work is done by another. I can’t make very good chestplates or helmets, so I removed them from the app to focus on what I can make.
The planning stages
Talking to Gemini 4 feels the same as talking to any of the Gemini models. It understands what I’m saying and, more importantly, my intent. The first app Gemini created looked terrible on mobile. There were too many windows and not enough visuals of the model we were making. Explaining that the app was too messy and that we needed to clear it up got the response I wanted, rather than a bunch more questions.
The difference with Gemini 4 Argon is its ability to accomplish complex tasks at speed. Things like making complex web apps seem easy, and the time it took to give me new iterations was far less than with the Gemini 3.5 Flash-Lite model I’m used to using.
I have Gemini Plus because I have a Google One plan, and I hit the token limit several times as I developed the app, but waiting an hour for a reset wasn’t that big a deal. If you have the Pro version, you’ll likely be OK.
The first few versions of KeriForge (the name I settled on for my armor web app) were surprisingly usable right away. All the sliders for adjusting the model size worked. While they weren’t all intuitive, they had enough features to get me started. I kept going back, though. I removed some features, such as the helmet generator, and added new ones, including the strap hole marker and circumference calculator.
Gemini understood that these changes needed to reflect the physical nature of the end result. Instead of trying to cut holes in the digital model for the straps, it created marks on the model, so I could cut them out in the real world. 3D models need to be manifold — all their faces need to face the right way and connect to be “watertight” — otherwise, they can fail on the print bed. Making random holes in the model would most definitely cause it to fail.
At one point, I asked Gemini to let me “Download this onto my iPad Pro to make it easier to use.” Gemini understood that I didn’t want to make an iPad app, but that I wanted the web app to be available offline on my iPad. It made the app available as HTML and, once I got it up on Google Sites, told me how to download it using Safari.
It also has its own preview that lets me see the app running directly from the Gemini app on the iPad, so making changes was easy and instantaneous. It took around 10 iterations to reach KeriForge 8.2 and a state that I felt was good enough to produce a physical print.
The finishing touches?
Creating the app was a lot of fun, and I learned a lot about how Gemini works and ways to prompt it to get a better finished article, but my original skepticism wasn’t that Gemini couldn’t make the app, but that it couldn’t produce a fully 3D-printable design that I could make physically.
I spent some time measuring my arm and adjusting the blank vambrace to make sure it would fit if it did print, then I hit the export button. Because I used my iPad, I got to export it directly to Nomad Sculpt, a 3D sculpting tool that let me add some random squiggles and an approximation of my name on the side of the model.
From there, I exported the file once again, this time to a browser app called Layerling. This app lets me edit the STL file — STL is the format for plain 3D models without any color — to cut the holes the straps need to go through. It’s a much more comprehensive program than the one I just made, so I know it can handle cutting the model while keeping it 3D-printable. I’ve only used Layerling a few times, but the more I do, the more impressive it becomes.
Making the holes in the model was simple, and since I had already asked Gemini to ensure there were guide markers, finding the right location was painless. Once I had cut those holes, it was onto the final stage: printing.
But will it actually print?
Once I had the final STL ready for printing, it was a simple matter to export it over to Bambu Slicer and start the actual print. I chose to print it in TPU 75A, a flexible material I was already testing. TPU is a soft, rubbery material, so it can conform to my arm better than the more rigid plastics like PLA and ABS.
This was the moment when my bet with Gemini would come to fruition. After 7 hours of printing and about 11 hours of iterating and fiddling with Gemini, we would see whether the model actually worked or ended up as spaghetti all over my printer.
The screenshot clearly shows that it did, indeed, work. You can see that, despite some errors that weren’t caused by the model, it produced a fully manifold and usable 3D print. The dimensions were perfect, fitting my forearm length and wrist circumference exactly.
The errors you can see on the model stem from the TPU being too soft and the model being too tall. As the printer increased the model’s height, the tension relaxed, causing the model to wobble under the print head. In the future, I would need to support it better in the slicer or print it lying down to achieve the print quality I expect.
An impressive AI tool
I’m not an AI power user. I like to use Gemini to organize my emails, help me sort out spreadsheets, and that’s about it. I assumed that creating a web app capable of producing a fully physical product, such as a 3D model, would be arduous; that I would have to constantly refine my prompts to get it to understand my needs and wants. That wasn’t the case, though. Gemini Argon seemed to understand the context of what I wanted far better than I gave it credit for.
The term “prompt engineering” has always made me shy away from using these products. I don’t want to spend time trying to get an AI to understand what I need when a person could do it much more quickly. I can see now that by using that term, gatekeepers can put AI behind a knowledge wall: to present it as a mysterious, complex thing. It simply isn’t the case with the latest models.
I still don’t like generative AI, but I can’t help but be impressed by something that can take me from an idea to a physical product in less than a day. I went into this challenge betting Gemini 4 couldn’t do what it said it could, and was humbled in the process. I’m not going to start using AI for everything I do, but I’ve already thought of some fun ways it can help me with upcoming projects. Something that inspires my creativity can’t be all bad, can it?
