---
id: "6470a7f9cc54ddb6"
title: "I’ve tested countless Linux distros, and Pond is unlike anything I’ve tried – here’s why"
url: "https://zdnet.com/tech/pond-distro-arch-linux-unique-ui"
link: "https://zdnet.com/tech/pond-distro-arch-linux-unique-ui"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T17:30:38Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Jack Wallen"]
language: "en"
summary: "Feeling adventurous? This Linux distribution is exciting, efficient and totally unique."
tags: ["Linux"]
orgs: []
topics: ["products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 1015
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/pondhero.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# I’ve tested countless Linux distros, and Pond is unlike anything I’ve tried – here’s why

ZDNet · Jack Wallen · 2026-11-19

ZDNET’s key takeaways
- Pond came out of nowhere and seriously impressed me.
- Using the Niri window manager, this distro has a wonderful UI.
- Pond is based on Arch Linux and is in early development.
Linux is all about choice. From the kernel all the way up to the desktop environment, you get to determine what is used and even how it is used. The staggering number of distributions, desktops, package managers, file managers, and terminal apps provide you with a nearly infinite combination of choices. That choice is and has always been a key aspect of Linux.
Also: My favorite Linux desktop environment for laptops surprised even me
So too is innovation. If there’s one thing that separates Linux from all other operating systems, it’s the willingness to try something different. Linux developers are always pushing the limits of what an operating system is, and this new take on the OS is the epitome of that.
More from ZDNET
The distribution in question is called Pond. According to the developers, “Pond is an opportunity for us to play with familiar conventions and experiment with new ideas that make a computer more natural and satisfying.”
A unique and efficient UI
The developers have achieved something special. Pond takes the standard UI and turns it on its head. Part tiling window manager, part mobile UI, part GNOME, and part something we’ve never before seen, this desktop environment is special. It took me all of five minutes to fall in love with what they’ve created.
The Pond UI consists of the following:
- A sidebar delivers useful information and an app launcher.
- Spatial window arrangements on the desktop are neither tiling nor traditional: It’s something altogether different. When you open a window, Pond automatically arranges it to fit the available space.
- Flowing workspace allows you to arrange the windows as you see fit.
- Powerful, contextual search makes it easy to find what you’re looking for and even to install apps.
Also: The only 4 Linux email clients I recommend
If you’ve ever considered using a tiling window manager, but thought the lack of a mouse made it seem a bit too complicated, Pond is exactly what you want. Here’s how it works:
- Open an app, and it appears in the center of the window.
- Open a second app, and it splits the screen with the first.
- Open a third app, and it’ll bump the second app out of the way.
- If you need to access that second app, click on its icon in the sidebar.
- If you want to rearrange a window, click its icon in the sidebar and drag it to a new location on the grid.
Pond uses the Niri window manager to arrange windows in columns along an infinite strip from left to right. In multi-monitor setups, each display gets its own strip, so windows never “overflow” from one monitor to the next.
Also: How to install Arch Linux without losing your mind
At the same time, workspaces are dynamic, and there’s always a new workspace automatically created to the right of the farthest-right window. The combination of the Pond sidebar and Niri’s way of handling windows makes this UI truly original.
Opening and Installing apps
Pond doesn’t have a traditional desktop menu. Instead, you open the launcher (using the Super+Space key combination), type the name of the app you want to install, and hit Enter when the app name appears on both the display and as an icon in the top portion of the sidebar.
Another thing that sets Pond apart is how you install apps. Yes, you can open a terminal window and install an app using the pacman command, or you can open the launcher, type install, press Enter, and then type the name of the app you want to install. For instance, if you wanted to install LibreOffice, you would type:
install libreoffice
Once you hit Enter a second time, the installation will begin. Many apps install via Flatpak, but on the off-chance an app must be installed via the pacman package manager, you’ll be prompted to type your user password before the installation begins.
I love this system.
Under the hood
As I hinted earlier, Pond is based on Arch Linux, which means it’s a rolling-release distribution. One issue that did give me pause was the lack of a GUI update system, which indicates that updates would have to happen in the terminal, like so:
sudo pacman -Syu
I installed the Shelly GUI frontend, which does have an update component. Personally, I would simply open the terminal window, type sudo pacman -Syu, hit Enter, and let the update run in the background. But if a GUI is your jam, Shelly is what you want.
Also: A super fast distro for anyone ready to move beyond beginner Linux
It would be sweet if the developers allowed updating the system from within the launcher, so it didn’t require opening the terminal first. The Pond launcher does allow running system commands from the launcher, which will then open the terminal window and execute the command. For instance, open the terminal, type a command, hit Enter, and then scroll through the list of available commands that can be run.
Pond ships with kernel 7.3.4-3, so it has outstanding hardware recognition and performance.
Should you dip your toes in the Pond?
You should definitely give Pond a try, especially if you’re adventurous and want to experience something completely different. If, on the other hand, different is not in your stream, then Pond will frustrate you to no end.
Also: Why Nextcloud Office is my new favorite free productivity suite
Pond excited me more than any OS has in a very long time; so much so that I could see this becoming my go-to OS, once it reaches stable release. Until then, I will keep Pond installed on a laptop, keep upgrading, and see what happens next.
Kudos to the Pond OS team for coming up with something truly unique in an already competitive world.
