---
id: "77b5083a79f022cb"
title: "Show HN: Cyberviber – a $15 touch screen to show which Claude session needs you"
url: "https://cyberviber.de"
link: "https://cyberviber.de"
source: "cyberviber.de"
domain: "cyberviber.de"
source_type: "community"
collector: "hackernews"
date: "2026-11-14T12:54:07Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["d1351r43"]
language: "en"
summary: "at a glance.\ncyberviber is a 2.4″ touch display that lists the Claude Code sessions running on your computer and shows the state of each. Tapping a session focuses its terminal: the pane, the tab and the window.\nAlso shows Mistral Vibe sessions.\nESP32-2432S024R\n240×320 · LVGL 9\nXPT2046 touch\nsorted by urgency.\nClaude Code hooks report to a small daemon, which tracks whether each session is…"
tags: []
orgs: ["Anthropic", "Mistral", "Amazon"]
topics: ["products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 618
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50496642"
score: 12
comments: 2
community: "Hacker News"
---

# Show HN: Cyberviber – a $15 touch screen to show which Claude session needs you

cyberviber.de · d1351r43 · 2026-11-14

at a glance.
cyberviber is a 2.4″ touch display that lists the Claude Code sessions running on your computer and shows the state of each. Tapping a session focuses its terminal: the pane, the tab and the window.
Also shows Mistral Vibe sessions.
ESP32-2432S024R
240×320 · LVGL 9
XPT2046 touch
sorted by urgency.
Claude Code hooks report to a small daemon, which tracks whether each session is working, waiting for input, finished or idle. Sessions that need you are listed first.
!
needs you
A permission prompt or a question. Blinks and wakes the backlight.
PermissionRequest · AskUserQuestion
✓
ready
The turn is finished, e.g. “Done · 3 files changed”.
Stop
✻
working
Thinking or running tools. The activity line shows the current step.
UserPromptSubmit · PreToolUse
◦
idle
Ready, but no events for ten minutes (configurable).
ready + 10 min
Mistral Vibe sessions appear in the same list. Vibe has fewer hooks than Claude Code: a session shows up with its first tool call or finished turn, a question shows as needs you, but a permission prompt does not (it stays working), and there is no context usage.
the terminal.
The tap goes back over USB. The daemon focuses the multiplexer pane first, then the tab, then the window. Works on macOS and on Linux with Hyprland.
claudehooks + session registry
Every hook event is posted to localhost. Sessions that started earlier are found in ~/.claude/sessions.
cyberviberdgo · launchd / systemd
Keeps the session list: state, idle timer, process check, context usage.
usb serialjson lines · 115200
One cable for power and data. Wi-Fi is not used.
esp32 + lvglstateless renderer
Draws what the daemon sends, reports taps, dims the backlight when idle.
your terminalpane → tab → window
zellij or herdr pane, Tabby tab, kitty window, Ghostty, foot.
named after desktop tools.
Rendered at 240×320. On the device, swipe or press BOOT to switch. The previews run on demo data; tapping a session shows the focus message.
from Omarchy.
State colours use each palette’s red, yellow and green; the accent is used for selection and focus. Set one with cyberviber theme nord. Selecting one here also changes this page.
    GhosttykittyTabbypluginfootzellijherdralacrittyHyprland0.57+macOSOmarchy
  
Missing your terminal, multiplexer, OS or coding agent? Pull requests are welcome. Multiplexers and terminal apps are pluggable in the daemon.
- 01The board An ESP32-2432S024R — the 2.4″ “Cheap Yellow Display” with a resistive XPT2046 touch panel and a CH340 USB bridge. Available on Amazon and AliExpress. Search for: 
  - ESP32-2432S024R
  - ESP32 2.4 inch TFT touch display
  - Cheap Yellow Display 2.4
The trailing R means resistive touch, which the firmware expects. The C variant (capacitive) and the 2.8″ ESP32-2432S028 are different boards.
- 02A case For example the mini monitor case on MakerWorld. Check that it fits the 2.4″ board.
- 03One USB cable Power and data. The daemon detects the port.
- 04Flash & calibrate PlatformIO builds the firmware. On first boot, tap the four arrow tips. Hold a finger on the screen while plugging in to calibrate again.
~/cyberviber — zsh
# daemon + hooks + status line
❯ go install github.com/d135-1r43/cyberviber/cmd/cyberviber@latest
❯ ~/go/bin/cyberviber install
  ✓ hooks       ~/.claude/settings.json
  ✓ statusline  cyberviber statusline
  ✓ daemon      dev.cyberviber.daemon
  ✓ vibe hooks  ~/.vibe/hooks.toml (only if ~/.vibe exists)
# firmware
❯ cyberviber release 120
❯ pio run -d firmware -t upload
❯ cyberviber release 1
# without hardware: browser simulator with live sessions
❯ cyberviber sim → http://127.0.0.1:7337/
cyberviber statussession table in your shellcyberviber layout tilingwaybar · tiling · btop · walker · hyprlockcyberviber theme nordstored on the devicecyberviber brightness 60backlight in percentcyberviber dim 15dim after 15 idle minutescyberviber usb bottomflip it, USB port downcyberviber screenshot out.pngthe device screen as PNGcyberviber uninstallremoves hooks, daemon and plugin
