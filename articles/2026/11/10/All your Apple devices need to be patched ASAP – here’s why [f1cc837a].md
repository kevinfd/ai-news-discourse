---
id: "f1cc837a3f8817af"
title: "All your Apple devices need to be patched ASAP – here’s why"
url: "https://zdnet.com/tech/apple-27-2-1-security-fix-iphone-ipad-mac-watch-patch"
link: "https://zdnet.com/tech/apple-27-2-1-security-fix-iphone-ipad-mac-watch-patch"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-10T16:54:11Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Jada Jones"]
language: "en"
summary: "Security updates for iPhones, iPads, Macs, Apple Watches, and Vision Pro just rolled out."
tags: ["Security"]
orgs: ["Apple"]
topics: ["chips & infrastructure"]
content_source: "fulltext"
word_count: 624
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/DSC00893.jpeg"
discussion_url: null
score: null
comments: null
community: null
---

# All your Apple devices need to be patched ASAP – here’s why

ZDNet · Jada Jones · 2026-11-10

ZDNET’s key takeaways
- Apple releases 12 software updates to patch security issues.
- iPhones, iPads, Macs, Apple Watches, and Vision Pro devices are affected.
- The security patches target wireless vulnerabilities.
On Tuesday, Apple released security patches for iOS, iPadOS, MacOS, WatchOS, and VisionOS, which address wireless security flaws in Bluetooth pairing, AirPlay, and Messages.
According to Apple’s security notes, vulnerabilities can allow attackers to establish a Bluetooth connection without user interaction, bypass AirPlay connection rate limits, and join an iMessage group chat and receive its messages. Around half of these flaws were found internally by Apple, while the others were submitted by researchers.
Attackers can access your group chat
Apple’s security notes list a fix for Messages to prevent attackers from remotely joining an iMessage group chat and reading its messages. According to Apple, “an authorization issue was addressed with improved validation” to fix the issue.
There was likely a flaw in Apple’s iMessage authorization logic that allowed an unauthorized user to inject themselves into a group chat roster without permission from an existing member.
Also: Your iPhone can spot scams for you with iOS 27
Another issue in Messages could allow an authorized added member to access messages within a group chat that were sent before they joined. According to Apple, the code that caused this issue has been removed.
Several wireless vulnerabilities
One security fix across devices and software versions addresses an issue where a malicious actor could establish a Bluetooth connection to your device without user interaction.
Apple was not specific about which kind of Bluetooth attack this fix addresses; however, it’s reminiscent of Bluetooth Low Energy Re-Pairing vulnerabilities found earlier this year by French researchers.
This study explains how bad actors can exploit vulnerabilities in Bluetooth Low Energy pairing logic to execute one-click or zero-click impersonation and man-in-the-middle attacks against unsuspecting devices, regardless of Bluetooth version or security level.
Also: Beware of Bluetooth sniffers: Your favorite gadgets could expose you
The study was published in January of this year, and the researchers reported initial findings to Apple, which “[appeared] to have hardened the re-pairing logic in MacOS/iOS 26,” according to the study. It’s possible that Apple internally found another vulnerability in the same Bluetooth pairing logic, given how many devices across Bluetooth versions are affected.
According to Apple, this issue was fixed with “improved checks,” likely meaning strengthened verification steps during pairing.
Another vulnerability pertains to AirPlay, allowing an attacker within Bluetooth range or on the same network to bypass the rate limit on AirPlay pairing code attempts. This issue also affects iOS, iPadOS, MacOS, VisionOS, and WatchOS.
This vulnerability is similar to the AirBorne attack method. This report, published in 2025 by Oligo, describes how zero-click remote code execution, user-interaction bypass, denial-of-service, man-in-the-middle, and other techniques can be used to take control of a device that supports AirPlay.
However, the current security issue is likely less serious or far-reaching and was discovered internally.
For this issue, when you pair a device with an AirPlay receiver, such as an Apple TV, AirPlay-enabled TV, or Mac, it will prompt you for a security PIN to verify your device. You can only input an incorrect PIN a certain number of times before you’re denied pairing for a period of time.
Also: The new Apple TV 4K is always listening for ‘Hey Siri’
A vulnerability in this defense mechanism can allow an attacker within Bluetooth range of, or on the same network as, your device to use a brute-force attack, bypassing the mechanism that limits the number of incorrect PIN attempts, and eventually gain access to your device. There are only so many PIN combinations.
According to Apple, “a logic issue was addressed with improved state management” to fix this problem.
