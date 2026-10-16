---
id: "3e99722b0dece030"
title: "5 AutoHotkey Scripts for Data Scientists"
url: "https://kdnuggets.com/5-autohotkey-scripts-for-data-scientists"
link: "https://kdnuggets.com/5-autohotkey-scripts-for-data-scientists"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-10-13T12:00:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Nahla Davies"]
language: "en"
summary: "Five AutoHotkey v2 scripts that handle repetitive Windows desktop work around data analysis: launching a project workspace, converting clipboard IDs to Python or SQL lists, fixing file paths, and snapping windows into place."
tags: []
orgs: []
topics: ["models & research", "agents & coding", "health & science"]
content_source: "fulltext"
word_count: 1825
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/kdn-5-autohotkey-scripts-for-data-scientists-feature.png"
discussion_url: null
score: null
comments: null
community: null
---

# 5 AutoHotkey Scripts for Data Scientists

KDnuggets · Nahla Davies · 2026-10-13

5 AutoHotkey Scripts for Data Scientists
Five AutoHotkey v2 scripts that handle repetitive Windows desktop work around data analysis: launching a project workspace, converting clipboard IDs to Python or SQL lists, fixing file paths, and snapping windows into place.
The notebook is ready and the actual work has not started. First the project folder, then the editor, then the terminal, then the tab with the docs. Then a column of customer IDs arrives in a spreadsheet and has to become a Python list, so it goes through a web formatter of uncertain ownership. Then a file path copied from Explorer has to lose its backslashes before the notebook will read it. Then the windows get dragged into the same arrangement as yesterday. None of that is analysis, and all of it happens before analysis on most Windows machines, most days.
AutoHotkey exists for this layer. The five scripts below are small, and each removes one of those rituals without touching the data pipeline itself. That boundary is the point, so it gets a section of its own first.
The five scripts, the desktop chore each one takes over, the AutoHotkey feature that does the work, and the first thing to watch. Alt text: four-column reference table listing a workspace launcher, a clipboard-to-list converter, analysis hotstrings, a path formatter, and a window layout hotkey with chore, feature, and caution columns. Credit: original reference table based on the AutoHotkey v2 documentation.
Before the Scripts: Keep AutoHotkey in Its Lane
AutoHotkey is a free, open-source automation utility for Windows, and its scripting language was built around one idea: a keyboard shortcut can run any code you like. The tool is Windows-only in the plainest sense: on a Mac or a Linux box the same jobs go to Hammerspoon, Keyboard Maestro, AutoKey, or a shell alias, and none of what follows transfers. Everything here is AutoHotkey v2. The v1 line is no longer maintained, but a decade of forum answers were written in it, and most of them will not run under v2 unchanged. A #Requires AutoHotkey v2.0 line at the top of the file makes that mismatch fail loudly instead of strangely. Ten seconds well spent, every time.
The fit is narrow and useful. AutoHotkey is good at the desktop moments around data work: launching things, reshaping whatever is on the clipboard, expanding text you type constantly, and moving windows. AutoHotkey is the wrong tool for anything that should be reproducible. A transformation that matters to the analysis belongs in Python, R, or SQL — in a file under version control, with a test. A script that types keystrokes into a production admin console is not automation; it is a liability with a hotkey. One more thing before the clipboard scripts: the clipboard is where customer IDs, tokens, and query results sit for a moment, and a script that reads it reads whatever happens to be there. Decide what a script logs, and where it pastes, with that in mind.
1. Launching the Whole Analysis Workspace
Returning to the same project means opening the same four things in the same order every time. One hotkey can open all of them.
#Requires AutoHotkey v2.0
#SingleInstance Force
project := "C:\work\churn-model"
^!w:: {                                   ; Ctrl+Alt+W
    Run 'explorer.exe "' project '"'
    Run 'code "' project '"'
    Run 'wt -d "' project '"'             ; Windows Terminal in the project folder
    Run "http://localhost:8888/lab"       ; the notebook server, if it is running
}
Run launches executables, folders, and URLs alike, so the same block can open Explorer, VS Code, a terminal, and a browser tab. The gain over four taskbar shortcuts is that the bundle opens as a unit in the project folder, and switching projects means changing one variable. Two habits keep this script harmless. The paths belong to one machine, so leave them at the top of the file where the next person will trip over them on purpose. And never put a credential or an API key in there, however tempting a one-key login looks. A script file is plain text that ends up in backups and shared drives.
2. Turning Copied IDs Into a Python or SQL List
The clipboard-to-list script earns the install on its own. A column of IDs or category labels arrives in a spreadsheet or a ticket export. The notebook wants ['a', 'b', 'c'] and the query wants IN ('a', 'b', 'c'), and the spreadsheet offers neither. Copy the column, press one hotkey, paste.
^!l::PasteList("[", "]")                  ; Python list
^!+l::PasteList("(", ")")                 ; SQL IN (...)
PasteList(open, close) {
    items := []
    for line in StrSplit(A_Clipboard, "`n", "`r ")
        if line != ""
            items.Push("'" line "'")
    out := open
    for i, item in items
        out .= (i > 1 ? ", " : "") item
    A_Clipboard := out close
    SendText A_Clipboard
}
A_Clipboard is the clipboard as text, readable and writable like any variable. The function splits it on newlines, trims stray carriage returns and spaces, quotes each value, and joins them. SendText then pastes the result literally, so a bracket in the data is not read as a keystroke. Values containing quotes need escaping the script does not do. For a column of IDs that rarely matters, and anything messier has outgrown a hotkey. The reshaping is deliberately temporary: it lives next to the clipboard and is gone once the paste is done.
If the copied values came out of customer data, should they be pasted into a random web formatter at all? The formatter sites work fine, and every one of them is a third party receiving a column of identifiers it has no reason to see. Once the reshaping is something the analysis depends on every week, though, it stops being desktop glue. Move it into the notebook or a small module, next to the Python scripts that do the real CSV processing, where it can be reviewed and rerun.
3. Expanding Analysis Boilerplate With Hotstrings
Hotstrings replace an abbreviation with longer text as you type it. The standard import block, a notebook section heading, and an exploratory data analysis (EDA) checklist get typed dozens of times a month, never change, and are too short to justify a snippet manager — which is hotstring territory exactly.
:*:;;imp::
{
    SendText "import pandas as pd`nimport numpy as np`nimport matplotlib.pyplot as plt`n"
}
:*:;;eda::
{
    SendText "## EDA checklist`n- shape and dtypes`n- missing values per column`n- target balance`n- duplicates`n"
}
The ;; prefix keeps the abbreviations from firing inside ordinary words. The * option fires them as soon as the last character is typed, with no space needed. SendText matters here because the plain Send function treats #, ^, +, !, and braces as modifiers and key names, so a markdown heading or a dictionary literal sent the ordinary way arrives mangled. Keep the expansions boring: a hotstring is for text that is identical every time. The moment it starts carrying a preprocessing function or a model configuration, it is hiding logic that a project template, a notebook snippet library, or a package should own.
4. Making Windows Paths Notebook-Friendly
Right-click a file in Explorer and choose "Copy as path", and what lands on the clipboard is "C:\Users\nd\data\raw.csv", quotes and all. Paste that into a notebook and Python gets as far as \U, decides a Unicode escape is starting, and refuses the string. Two hotkeys fix it on the way in.
^!p:: {                                   ; raw string:  r'C:\Users\nd\data\raw.csv'
    A_Clipboard := "r'" Trim(A_Clipboard, '"') "'"
    SendText A_Clipboard
}
^!+p:: {                                  ; forward slashes:  C:/Users/nd/data/raw.csv
    A_Clipboard := StrReplace(Trim(A_Clipboard, '"'), "\", "/")
    SendText A_Clipboard
}
The first strips the quotes and wraps the path as a raw string. The second swaps the separators, which Windows accepts in most contexts and pathlib normalizes anyway.
One honest caveat: path conventions differ between teams, projects, and environments, and a paste helper should follow the project's convention rather than quietly inventing one. If the repository uses pathlib and forward slashes, bind that form and drop the other. And keep the scope small: cross-platform path handling, moving files, renaming batches, and converting formats belong in Python, where the file-task scripts can be tested and run on the machine that has the data.
5. Snapping the Notebook, Terminal, and Docs Into Place
A review or debugging session has a shape: the notebook on one side, the terminal or logs below it, the editor or the docs on the other monitor. Rebuilding that arrangement by hand every morning is the kind of thing nobody notices they are doing. A hotkey can put the windows back.
^!1:: {
    Place("ahk_exe WindowsTerminal.exe", 0, 720, 1280, 720)
    Place("JupyterLab", 0, 0, 1280, 720)
    Place("ahk_exe Code.exe", 1280, 0, 1280, 1440)
}
Place(title, x, y, w, h) {
    if WinExist(title) {
        WinActivate
        WinMove x, y, w, h
    }
}
WinMove sets a window's position and size in pixels and WinActivate brings it forward. The WinExist check skips a window that is not open instead of raising an error. Windows are matched by process name or by a substring of the title, so "JupyterLab" catches the browser tab whatever the notebook is called. The caveats are real, and the documentation states them. On systems with several screens at different DPI settings, the final position and size can differ from what was requested. Negative coordinates are how a monitor to the left is addressed. And a window running with administrator privileges will ignore a script that is not. The layout is per-machine configuration and should be treated that way: numbers at the top of the file, a small edit expected after every monitor change, and a hotkey that is easy to switch off on the days a session does not fit the template.
Keep AutoHotkey as Glue, Not the Pipeline
Five jobs: launch, reshape, expand, format, and arrange. Start with whichever one matches the annoyance you hit most often last week — which for most analysts on Windows is the copied-ID list. Add the others only when their ritual becomes noticeable. All five fit in one .ahk file that a colleague can read in a minute, and it should stay that size.
The dividing line is the one the setup section drew, and it doesn't move. AutoHotkey smooths the desktop around the analysis. Every transformation, filter, and join that someone might one day need to rerun or defend lives in a notebook, a script, or a test under version control, and for the steps that have to be quick and reproducible at the same time, the command line is a better home than a hotkey. A script that saves a keystroke is worth keeping exactly as long as the workflow it serves exists. When the workflow changes, delete it, and write the next one.
 
Nahla Davies is a software developer and tech writer. Before devoting her work full time to technical writing, she managed—among other intriguing things—to serve as a lead programmer at an Inc. 5,000 experiential branding organization whose clients include Samsung, Time Warner, Netflix, and Sony.
