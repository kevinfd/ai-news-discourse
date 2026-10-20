---
id: "e550562a67c846f2"
title: "People are using AI to make their smart TVs smarter"
url: "https://mashable.com/tech/smart-tv-ads-claude-code-ai-cleanup"
link: "https://mashable.com/tech/smart-tv-ads-claude-code-ai-cleanup"
source: "Mashable"
domain: "mashable.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-19T18:53:36Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Olivia Tauber"]
language: "en"
summary: "These days, turning on the TV means getting past everything it wants you to watch first. A sponsored banner here, a row of recommendations there, and an app you never asked for that keeps showing up when you just wanted to open Netflix. But some smart TV owners have had enough, and are putting AI coding assistants to work. \n \n This Tweet is currently unavailable. It might be loading or has been…"
tags: []
orgs: ["Anthropic", "Google", "Apple", "Amazon", "Samsung"]
topics: ["agents & coding", "models & research", "search & media", "products & launches"]
content_source: "fulltext"
word_count: 1230
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# People are using AI to make their smart TVs smarter

Mashable · Olivia Tauber · 2026-10-19

People are using AI to make their smart TVs smarter
These days, turning on the TV means getting past everything it wants you to watch first. A sponsored banner here, a row of recommendations there, and an app you never asked for that keeps showing up when you just wanted to open Netflix.
But some smart TV owners have had enough, and are putting AI coding assistants to work.
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
Developers and other users on social media are sharing experiments in using tools such as Anthropic's Claude Code to disable unwanted software, replace busy home screens, and make their TVs feel more responsive. The results range from simple app menus to personalized interfaces, with open-source projects that collect tools and prompts for anyone interested in trying them themselves.
You May Also Like
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
For one developer, his motivation was fixing his parents' television. In an Oct. 17 post on X, he described using Claude Code to overhaul a Xiaomi TV that displayed an advertisement before they could reach Netflix. He said the assistant connected over Wi-Fi, removed 25 software packages, and built a replacement home screen.
"Looks like an Apple TV now lol," he wrote.
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
Another X user reportedly got rid of his "ads, bloatware, spyware [and] laggy UI."
"I also got a beautiful screensaver with my revenue, calendar, weather, and notifications for new Stripe payments. It was super easy!" he added.
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
These experiments have become a part of CleanYourTV, an open-source project originally called "tv-vibehack." Its goal? Replace the promotional clutter with an interface organized around the apps you actually use. And people trying it seem excited about how much less work their TVs now require.
"Now my TV is running super smooth, same as [a] new one," an X user wrote, who added a lightweight interface, a custom wallpaper slideshow, and a switch between Hindi/English for his parents.
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
I can understand the appeal. Pressing Home and seeing your own photos and favorite apps sounds a lot more inviting than being greeted by another round of things to buy.
Plus, there's documented frustration. In its Q4 2025 Video Trends Report, TiVo found that more than one-third of respondents reported excessive advertising on their TV’s home page.
But those screens simultaneously provide valuable real estate for the companies running them. Roku, for example, names making more money from its home screen as a key growth initiative in its 2025 annual report.
That leaves some owners turning to AI to make changes the TV companies have little incentive to offer themselves.
How to try it on your own TV
If you're wondering what people are actually typing into Claude Code, here's one prompt behind the makeover, which tells the coding assistant how to connect to the television, back up its settings, disable unwanted software, and build a simpler home screen.
To do it yourself, you need Claude Code, or another coding assistant with command-line access, running on a computer. Pasting the instructions into a regular chatbot conversation won’t give it access to your television.
This particular prompt is written for Android TV and Google TV devices. It isn’t designed for Samsung’s Tizen, LG’s webOS, or Amazon Fire TV, which require different approaches. Check your television’s operating system and model before starting:
- Connect your computer and TV to the same Wi-Fi network.
- Enable Developer options on the television. On many supported models, go to Settings → Device Preferences → About, highlight Build, and press OK seven times. The menu names may differ on your set.
- Turn on debugging. Return to Settings, open Developer options, and enable USB debugging. If your TV also shows Network debugging or ADB debugging, enable that option. Despite the name, this workflow doesn’t require connecting a USB cable.
- Open Claude Code on your computer. Paste in the project prompt (found in the link below), replacing the bracketed text with your TV’s exact model number.
- Stay nearby and follow along. You’ll need to approve the debugging connection on the TV and answer questions about which apps and features you want to keep. If the assistant can’t find the television, it may ask for the TV's IP address, which is usually listed in the TV’s network settings.
See here for the full project prompt, which includes additional troubleshooting and design details. There are other how-to's in the X posts below.
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
Once you paste it in the prompt, expect some back-and-forth. The assistant should ask which apps you use, what shortcuts you want, and whether to keep features such as casting and voice search. Review its proposed changes before approving them, especially if you don’t recognize a service.
One practical heads-up: Debugging can temporarily cut power to USB accessories on some TVs. If a connected speaker or drive stops working, it may come back when you switch debugging off.
That setup might sound like a whole afternoon’s project, but some users say they got through it much faster. One X user who tried it on a Sansui Google TV reported finishing in 25 minutes. "Damn, that was smooth!" they wrote.
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
Still, your TV model may restrict which software you can disable or whether you can replace the home screen at all. And a coding assistant can make mistakes, so a successful before-and-after post doesn’t mean you should approve every change it suggests.
It also matters which prompt you paste. Take the associated open-source project, dumbtv, which provides scripts to disable ads and tracking services and to replace the home screen on compatible TVs. Its developer documents testing on a Fire TV Edition television, but its cleanup also makes changes you might not want, including disabling Alexa and blocking software updates.
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
Undoing the changes can take some work, too. The project includes a restoration script, but its documentation says that some streaming apps it uninstalls must be reinstalled from the store.
The TV adjustments go beyond getting rid of ads, too. Another user shared a more unusual addition: "Gave my TV live @Polymarket game odds charts," they wrote. "You really can just do things nowadays."
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
For TV companies, there's a message in all this tinkering. People are willing to literally spend an afternoon working with a coding assistant to get a simpler television. Giving them that option in Settings would save everyone some trouble, don't you think?
Olivia Tauber is the deputy editor of digital culture, covering creators, media, movies, beauty, and more. Based in New York, her work has appeared in The New York Times, Vanity Fair, The Cut, Teen Vogue, Complex, and Interview Magazine. She holds a Master's degree in Journalism from NYU and a Bachelor's from the University of Michigan. She also runs Fan Mail, a weekly pop-culture newsletter.
