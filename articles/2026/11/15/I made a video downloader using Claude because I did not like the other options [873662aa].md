---
id: "873662aa4d2559c2"
title: "I made a video downloader using Claude because I did not like the other options"
url: "https://github.com/nolsen42/ClipHarbor"
link: "https://github.com/nolsen42/ClipHarbor"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T15:55:52Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["nolsen42"]
language: "en"
summary: "I didn't like the other available options out there, and I was annoyed about how some applications charge just to download, so I started off using \"Craft Anything\" by ArtCraft, which was using claude code under the hood, to make me an alternative to \"4kvideodownloader\" that I used for over a decade, and then had Claude code desktop app to continue on that work. I thought it was so good, I…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches", "models & research", "agents & coding", "search & media"]
content_source: "fulltext"
word_count: 1178
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xwyxkf/i_made_a_video_downloader_using_claude_because_i/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a video downloader using Claude because I did not like the other options

GitHub · nolsen42 · 2026-11-15

A free, open-source video and audio downloader for Windows, macOS and Linux. No download caps, no playlist limits, no account.
- Paste Link: copy a link, press the button (or Ctrl+V, ⌘V on a Mac), choose your options and download. You can also drag links onto the window or pass them on the command line.
- Video or audio only: MP4, MKV or WEBM video up to the best quality the site offers (4K/8K included), or MP3, M4A, OPUS, FLAC or WAV audio.
- GIF and animated WebP: turn short clips (like videos on X/Twitter that were meant to be GIFs) into looping GIF or WebP files, in small, medium, large or full size. You can also right-click any finished video and choose Make a GIF or Make an animated WebP.
- Send from your browser: right-click a video, a link or an X post and choose Download with ClipHarbor or Make a GIF with ClipHarbor (see below).
- Whole playlists and channels: pick which videos you want, optionally saved into a folder named after the playlist.
- Subtitles: choose languages, saved as files or embedded in the video.
- Smart Mode: save your choices once and every link afterwards downloads in one click.
- Subscriptions: follow a channel or playlist and new videos download automatically. ClipHarbor keeps running in the system tray (menu bar on a Mac) after you close the window, so checks keep happening, and it can start hidden when you sign in to your computer.
- Download list: progress, speed and time left. Pause, resume, retry, open the file or show it in its folder. You can search and filter the list.
- Settings: light, dark or system look, how many downloads run at once, speed limit, proxy, file-name template, browser sign-in for private or age-restricted videos, and embedded cover art and metadata.
Get the latest version from the Releases page and download the file for your computer:
Updates: ClipHarbor checks this repository's Releases when it starts and once a day. When there's a newer version it shows a banner; press Update now to see what's new, and it downloads the update, checks it against the checksum GitHub publishes, and restarts. You can turn the automatic check off, or check by hand, under Settings → About ClipHarbor. If ClipHarbor can't replace itself where it's installed (for example in Program Files), it opens the download page instead.
Want to try the newest changes before they're released? Every update is also built by GitHub Actions: open the Actions tab, pick the latest Build run and download your system's file from Artifacts (it comes wrapped in an extra .zip).
First start on a Mac: ClipHarbor isn't signed with a paid Apple developer account, so macOS will say it can't check the app. Open System Settings → Privacy & Security, scroll down and press Open Anyway next to ClipHarbor. You only need to do this once.
On Linux the "show a notice when downloads finish" option uses notify-send, installing the converter uses tar with xz support, and dates are shown in your local format with the libicu library. All three come with almost every desktop Linux.
The Send to ClipHarbor browser extension adds two choices to the right-click menu: Download with ClipHarbor and Make a GIF with ClipHarbor. Right-click a video, a link to one, or anywhere on a page. On X/Twitter, right-click anywhere on a post (even in your timeline) and that post is sent. The toolbar button sends the page you're on, and Alt+Shift+D / Alt+Shift+G do the same from the keyboard.
ClipHarbor must have been started at least once, so your computer knows it opens clipharbor:// links. The first time, the browser asks whether to open ClipHarbor; tick "always allow" to skip that question afterwards. With Smart Mode on, the download starts straight away; otherwise you get the usual choices first.
Installing the extension:
- Firefox (140 or newer): open ClipHarbor-extension-firefox.xpi in Firefox and press Add. It's signed by Mozilla, so it stays installed, and it updates itself when a new version comes out.
- Chrome, Edge, Brave, Vivaldi, Opera (until it's in the Chrome Web Store): download ClipHarbor-extension-chrome.zip from the Releases page and unzip it. Open the extensions page (chrome://extensions), turn on Developer mode, press Load unpacked and pick the unzipped folder.
No extension? Make a bookmark with this as its address, and click it on a video page:
javascript:location.href='clipharbor://download?url='+encodeURIComponent(location.href)
Use clipharbor://gif?url= instead for a GIF.
The extension only works on the page you send, and only when you ask. It doesn't read your browsing or send anything anywhere except to ClipHarbor on your own computer. See the privacy policy.
ClipHarbor downloads from video sites with two free, open-source tools that are not included in this repository:
- yt-dlp (Unlicense), which reads and downloads from video sites
- FFmpeg (LGPL/GPL), which joins high-quality video and audio and converts formats. ClipHarbor uses the builds from yt-dlp/FFmpeg-Builds on Windows and Linux, and from ffmpeg.martin-riedl.de on macOS.
The first time you run ClipHarbor, press Install engine. The app downloads both tools for your system (about 100–200 MB) into:
If yt-dlp and ffmpeg are already installed (for example with Homebrew, apt or winget), or you point to them in Settings, ClipHarbor uses those instead. Direct links to media files (for example .mp4 or .mp3) work without the engine.
You need the free .NET 10 SDK on Windows, macOS or Linux. The interface is built with Avalonia (MIT), which NuGet downloads automatically.
dotnet build -c Release
dotnet run -c Release
To make a single program file that runs without .NET installed, pick your system's ID (win-x64, osx-arm64, osx-x64, linux-x64 or linux-arm64):
dotnet publish -c Release -r linux-x64 --self-contained true -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true -p:EnableCompressionInSingleFile=true -o publish
GitHub Actions (see .github/workflows/build.yml) builds all five versions, wraps the Mac ones as a .app, and checks that the app starts on each system. It also zips the browser extension, and for releases has Mozilla sign the Firefox copy when the repository secrets AMO_JWT_ISSUER and AMO_JWT_SECRET hold API keys from addons.mozilla.org.
Open the Actions tab, pick Build, press Run workflow, choose patch (fixes), minor (new features) or major, and press the green Run workflow button. The build works out the next version from the last release (for example v1.1.0 → v1.1.1), builds everything, writes the release notes from the commit titles since the last release, and publishes the release with all the files attached. Publishing a release by hand on the Releases page still works too.
ClipHarbor --screenshot out.png starts the app without taking focus, saves a picture of the window and exits. Automated checks use this option.
Your download list, subscriptions and settings are saved in state.json in:
By default, downloads go to a ClipHarbor folder inside your Videos folder (Movies on a Mac).
Only download content you have the right to download. Respect copyright and each website's terms of service. ClipHarbor is an independent project. It is not affiliated with or endorsed by any video website or any other download software.
MIT. The download tools named above, and Avalonia, have their own licenses.
