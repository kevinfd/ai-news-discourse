---
id: "c662b8b8a16dfa9a"
title: "Turning my Mac desktop into an AI agent interface with Claude Code | How a non-engineer built it with 0 lines of code"
url: "https://note.com/miyabi_ai_base/n/n5fbc1671b323?hl=en"
link: "https://note.com/miyabi_ai_base/n/n5fbc1671b323?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-15T18:00:00Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Masaya"]
language: "en"
summary: "By simply asking Claude Code in conversation, I created a screen that displays the clock, CPU, memory, charging status, and upcoming schedule on my Mac desktop in real time. I didn't write a single ..."
tags: []
orgs: ["Anthropic", "Google"]
topics: ["products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 1891
paywalled: false
image: "http://www.bing.com/th?id=ONUT.4YToII9de73CI8C3wBJKDg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Turning my Mac desktop into an AI agent interface with Claude Code | How a non-engineer built it with 0 lines of code

note · Masaya · 2026-11-15

SYSTEM NOTICE
Turning my Mac desktop into an AI agent interface with Claude Code | How a non-engineer built it with 0 lines of code
By simply asking Claude Code in conversation, I created a screen that displays the clock, CPU, memory, charging status, and upcoming schedule on my Mac desktop in real time. I didn't write a single line of code. In this article, I will summarize the process and what I noticed while using it (such as insufficient charger output and how to read memory usage).
As of November 2026, this was created and verified on a Mac with 32GB of memory.
On a Sunday night, I felt like putting a clock in the middle of my Mac desktop. Something like a radio-controlled clock that moves down to the second.
I intended to just ask Claude Code for one thing, but before I knew it, the entire screen had become something else. CPU and memory usage, charging status, and even my next appointment are now permanently displayed on the very back of my desktop. The look is close to a command center you'd see in a movie.
I haven't written a single line of code myself. All I did was convey what I wanted in words and provide feedback on what I wanted fixed after looking at the screen that appeared.
The finished version of the desktop created with Claude Code
I call this screen a HUD (Head-Up Display, a system that overlays information on the screen). There is a clock in the center, and a rotating ring marks the seconds. On the left and right panels, the status of this Mac is lined up in real time.
The left column shows CPU, operation logs, charging, and network. The right column shows memory, apps consuming CPU, apps consuming memory, the next schedule, battery level, and uptime. All numbers are actual measured values from this Mac and are rewritten every second.
When I open a window, it hides underneath. This is because I placed it just above the desktop icons and below the app windows. It doesn't interfere with my work because clicks pass right through it.
The first request was just for a clock
The first request was a single sentence asking if I could display a clock and date in the middle of the screen.
Claude Code wrote and launched a small Mac app, and the clock appeared immediately. It looked plain. I told it I wanted it to be stylish, and then asked it to change the atmosphere of the entire screen.
From here on, it was a repetition of looking, speaking, and having it fixed.
The first time, I settled on a calm color scheme with night amber. I also had it draw a new wallpaper and made the Dock smaller to make it look cleaner. I felt the clock was tacky, so I had it rebuilt while it looked directly at the screen. This was the timing when I granted screen recording permission so the AI could take screenshots and check for itself.
I got sidetracked and made a wolf run in the menu bar
I added some fun along the way. I asked if it could change the speed at which an animal runs in the menu bar according to the Mac's load. The busier the CPU, the faster it runs. You can see the load at a glance.
At first it was a cat, then I changed it to a wolf. It was annoying when it ran under the clock, so I moved it back to the menu bar.
What was interesting was what happened after that. The running wolf itself was using 37% of the CPU. The wolf meant to show the load had become the biggest load. When I pointed this out, Claude Code fundamentally changed how it was drawn. By preparing the frame images in advance and just swapping the display, the usage rate dropped to about 3%.
In the end, I deleted the wolf. Still, it was a gain to know that the AI could measure and fix even the weight of what it had created.
Transforming the screen into an AI agent-style interface
This is where the real work began. I asked it to make the screen look cooler and more like an AI agent.
I decided on cyan (a bright light blue) for the color and had it create two versions: one with minimal information and one packed with data. After comparing them side-by-side, I chose the packed version.
I also refined the details. Since the log text was overflowing the panel, I had it shortened, and I added a list of apps consuming the most memory. Since there was empty space in the bottom right, I decided to display my upcoming schedule there.
Displaying only my own Google Calendar events
I linked the schedule to Google Calendar. The mechanism is simple: the HUD reads the Google events synced to the Mac's "Calendar" app and displays them. The HUD itself does not communicate with the outside world at all.
One problem arose: events from calendars shared by others were also appearing. I added a filter to show only my own events and adjusted the settings on the Mac side so that only my calendar would be synced. Since this setting is managed on the Google account screen, I handled that part myself.
The reason the battery was draining even when the Mac was plugged in was the wattage of the charger
The most practical benefit was the charging panel.
When I displayed the power flowing in and out of the battery, it showed minus 1.9W. Even though it was plugged into power, the battery was draining.
The cause was the 8W charger I happened to have plugged in. Against the 9W the Mac consumes, only 7W was coming in. I had assumed that if the cable was plugged in, it was charging, but in reality, it was slowly draining. I solved this by switching to a 52W charger.
Just by having the numbers constantly visible on the screen, you can notice these kinds of misconceptions.
Is it okay if the Mac's memory usage is high? The reason why 73% still had plenty of headroom
Another realization was about memory. The HUD showed that over 70% of my 32GB was being used, which honestly made me panic. I do similar work on another PC with 8GB, so why was this one using so much?
When I asked, I learned that macOS is designed not to let free memory go to waste, but to actively use it as cache. The memory pressure indicator, which shows headroom, indicated that 75-85% was free, meaning there was actually plenty of capacity. I concluded that there was no need to automatically close AI-related apps.
I also had it measure the load of the HUD itself. The CPU was at 1-3% and memory was about 160MB, which are figures that don't cause any issues even when running in the background.
Displaying the same screen on a sub-monitor
I also put the same HUD on an external monitor. It automatically follows even when I plug or unplug the display. I registered it to launch automatically upon login, so now my day begins with this screen every morning.
Handing over to another PC using an AI-friendly manual
Finally, I wanted to install it on another PC in a different color.
What I asked for here wasn't the work itself, but a manual. It is a set of instructions for an AI on the other PC to read and perform the installation.
Claude Code compiled a complete package that handles everything from building to wallpaper generation just by specifying a color, and included a manual that covers how to deal with common pitfalls. The image above is a test I made in purple. Instead of teaching a person the steps, I am handing it over from AI to AI. I felt that this method of passing on information could be used directly in my work as well.
The actual words I sent to Claude Code
I didn't use any special way of writing instructions. These are the actual words I sent.
I just sent my random thoughts and things that bothered me when I looked at it.
The workflow (5 steps)
- Ask for what you want in a single sentence (e.g., I want to display a clock in the middle of the screen)
- Show the screen to the AI (grant permission for Mac 'Screen Recording' and have it check with a screenshot)
- Tell it what bothers you as it is (e.g., it looks tacky, it's sticking out, etc.)
- Have it measure the load (check if it's using too much CPU or memory)
- Register it to launch automatically at login
The scope of what to leave to the AI and what to do yourself
It was fun to build, but it also involved changing Mac settings. So I drew a line.
I had the AI prepare the commands for Mac system settings like Dark Mode, wallpaper, and automatic startup at login, but I executed them myself. I saved the settings from before the changes in a file and also prepared a script to revert them. I also clicked the permissions for the calendar and screen recording one by one myself.
By separating what to leave to the AI and what to do with my own hands, I was able to play around with it without worry.
What I learned from trying it
Even if you can't write code, you can bring your ideas to life if you can describe what you want. The most important thing this time was looking at what was generated and providing specific feedback on what felt off. Saying things like 'that looks tacky,' 'it's overflowing,' or 'it's showing shared calendar events'—these are just impressions, but the AI turns them into concrete fixes.
Another point is that what I built became a tool for my work. Just having numbers like battery level or memory usage visible at a glance changes how I make decisions.
It started as a hobby project, and before I knew it, it had become a tool I use every day. For a few hours on a Sunday night, that's a pretty great way to spend time.
FAQ
Q. Can a non-engineer build this with Claude Code?
Yes, you can. I didn't write a single line of code for this. I just described what I wanted in words, looked at the screen that was generated, and gave feedback on what I wanted changed.
Q. Does keeping it displayed all the time slow down the Mac?
It doesn't slow it down. In my tests, it used 1-3% CPU and about 160MB of memory.
Q. What kind of information can be displayed?
I'm displaying the time and date, CPU usage, memory usage, apps using the most CPU and memory, charging power, network speed, upcoming events, battery level, and uptime.
Q. Can I install this on other Macs?
Yes, you can. I had Claude Code create a package with instructions, and I just had the AI on another PC read them to install it. You can also change the colors as specified.
Related Articles
People who can use AI won't survive—only those who can judge its accuracy will remain
