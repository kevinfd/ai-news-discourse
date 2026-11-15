---
id: "5cac50b57a422ebf"
title: "Show HN: Gamma PDF – AI-native PDF reader, self-hosted"
url: "https://gammapdf.com"
link: "https://gammapdf.com"
source: "Gamma PDF"
domain: "gammapdf.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-14T08:08:11Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["tim4431"]
language: "en"
summary: "Author here. I have been reading papers and taking notes for years, using Zotero for the PDFs, Obsidian for the notes, and, recently, an AI chat tab for my questions. Gamma PDF is my attempt to make that one place. In Gamma, you open a paper by simply pasting an arXiv (or DOI) link. Highlight a sentence, or drag a box round a figure, and it becomes a note beside the page with the quote and a…"
tags: []
orgs: ["Anthropic", "OpenAI", "Apple", "Google", "Microsoft"]
topics: ["products & launches", "agents & coding", "models & research", "search & media"]
content_source: "fulltext"
word_count: 924
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50495073"
score: 10
comments: 3
community: "Hacker News"
---

# Show HN: Gamma PDF – AI-native PDF reader, self-hosted

Gamma PDF · tim4431 · 2026-11-14

Windows
Microsoft Store
Or the standalone installer (SmartScreen: More info → Run anyway).
Open source · self-hosted 
for people who read papers
Keep what you learn.
A PDF annotator with outliner notes, live math and an AI that reads along — on your own machine.
Highlight, annotate & draw
Highlight, draw or type on the page. Each mark lands in your notes, and a click jumps back to the passage.
Take notes
An outliner right next to the paper, with live Markdown and LaTeX, links between pages, and handwriting on a sheet.
Ask an AI about your papers
Get cited answers that jump to the passage, with your own Anthropic or OpenAI key or a paid ChatGPT plan.
Browser, desktop, iPad and Android. Offline copies sync themselves.
Search notes, highlights and every PDF at once.
Title, authors and venue fill in on open. Copy BibTeX in one click.
The browser extension saves the paper you're reading, with its metadata, to the folder you pick.
Shared workspaces, live cursors, and comments on any note or highlight.
Import from Zotero, Obsidian, Logseq and Notion. Connect Codex, Claude Code and any MCP client.
SQLite and files in one folder. No account with us, no telemetry. Export everything at any time.
A library we keep running for you, if you'd rather not run a server.
See the plans
Get Gamma
A self-contained app: no Docker, Python or Node. Latest release.
First launch: System Settings → Privacy & Security → Open Anyway.
Debian / Ubuntu, x64.
docker run -d --name gamma -p 9001:9001 -v gamma-data:/data ghcr.io/tim4431/gamma:latest
Open localhost:9001 as admin; the password is in docker logs gamma. More ↓
Install Apple's TestFlight app, then open the link on the iPad. Keeps a workspace on the iPad for the Pencil with no connection.
Android 10 or later on 64-bit ARM, phones and tablets. Open the APK on the device and allow your browser to install it. Keeps a workspace on the device for the stylus with no connection.
Gamma Connector, for Chrome, Edge and other Chromium browsers. Or the .zip.
Codex, Claude Code and any MCP client can search and read your papers, notes and highlights, read-only, for one workspace you approve.
claude mcp add --transport http --scope user gamma <your Gamma>/mcpcodex mcp add gamma --url <your Gamma>/mcp
One-command setup in Settings → AI → Integrations. Connection guide
Self-host
One Docker image for amd64 and arm64, with all your data in one /data volume.
Users and shared workspaces are managed in the app. Put Caddy or nginx in front for your own domain. The Watchtower service in the compose file keeps it upgraded.
services:
  gamma:
    container_name: gamma
    image: ghcr.io/tim4431/gamma:latest
    build: .
    ports:
      - "9001:9001"
    volumes:
      # Named volume: Docker manages the storage location. To keep the data in
      # a real folder next to this file instead, use a bind mount:
      #   - ./data:/data
      - gamma-data:/data
    # environment:
      # With a bind mount, set these to your host user's ids (`id -u` / `id -g`)
      # so the files Gamma creates belong to you instead of root:
      # PUID: 1000
      # PGID: 1000
      # Behind a reverse proxy (Caddy, nginx for a domain with TLS), the
      # proxy's address, so Gamma believes its X-Forwarded-For and rate
      # limits count each visitor instead of the proxy. For a proxy container
      # in this file, the subnet of the network below (pinned, so it is
      # known). Leave it unset when nothing sits in front of the port. The
      # proxy needs no compression of its own for the app's files: Gamma
      # sends the Brotli or gzip copies its build made.
      # FORWARDED_ALLOW_IPS: 10.203.0.0/24
      # Off-site copies of the databases and uploaded files to an S3-compatible
      # bucket are set up by an admin in Settings -> Backups; a container can
      # set them with GAMMA_S3_BUCKET and the other GAMMA_S3_* / GAMMA_OFFSITE*
      # variables instead (docs/dev/debugging.md "Off-site copies in a bucket").
    restart: unless-stopped
  # Keeps the gamma container on the newest image: Watchtower polls the
  # registry every six hours, pulls a new image and restarts gamma, which
  # runs an upgrade's global steps as it starts and each workspace's own as
  # the workspace is first opened (a snapshot of the databases is taken
  # first; see docs/dev/migrations.md). Scoped to this container, so it
  # never touches others on the host. The image is the maintained fork of
  # Watchtower (github.com/nicholas-fedor/watchtower), pinned to its major
  # version; it holds the Docker socket, which is root on the host. Remove
  # the service to update by hand with
  # `docker compose pull && docker compose up -d`.
  watchtower:
    container_name: gamma-watchtower
    image: nickfedor/watchtower:1
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --cleanup --interval 21600 gamma
    restart: unless-stopped
volumes:
  gamma-data:
# With a proxy container next to gamma, pin the compose network's subnet and
# name it in FORWARDED_ALLOW_IPS above:
# networks:
#   default:
#     ipam:
#       config:
#         - subnet: 10.203.0.0/24
Draw with a stylus or the mouse anywhere. On an iPad, the Pencil writes with pressure: in the iPad app (a TestFlight beta, which also works with no connection) or after Add to Home Screen from Safari. On Android, the Android app captures an S Pen, USI or Wacom stylus natively and works with no connection too. See Install as an app.
Windows, macOS and Debian/Ubuntu on the desktop; the iPad through TestFlight; Android 10 or later on 64-bit ARM through the APK on each release, and Google Play once it is listed; Docker (amd64, arm64) or Python 3.11+ and Node 18+ on a server.
