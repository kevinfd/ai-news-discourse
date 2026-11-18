---
id: "27ad588651ca49f1"
title: "Anthropic Adds Code Mode to Claude Code: Claude Now Chains Tool Calls in JavaScript"
url: "https://marktechpost.com/2026/11/17/anthropic-claude-code-code-mode-javascript-tool-calls"
link: "https://marktechpost.com/2026/11/17/anthropic-claude-code-code-mode-javascript-tool-calls"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T06:53:28Z"
published_date: "2026-11-18"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Anthropic has added Code Mode to Claude Code as an experimental, opt-in feature. Claude Code Code Mode is a mode in which Claude writes JavaScript that makes several tool calls in 1 step. It shipped in Claude Code v2.1.323 last week . For developers, it changes how the agent spends round-trips on multi-step work. You can check the deployment options and specs here through our GPULeaderboard.com…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Context Engineering", "Editors Pick", "For Devs", "New Releases", "Python", "Software Engineering", "Staff"]
orgs: ["Anthropic", "Google", "Amazon"]
topics: ["agents & coding", "models & research"]
content_source: "summary"
word_count: 1625
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic Adds Code Mode to Claude Code: Claude Now Chains Tool Calls in JavaScript

MarkTechPost · Michal Sutter · 2026-11-18

Anthropic has added Code Mode to Claude Code as an experimental, opt-in feature. Claude Code Code Mode is a mode in which Claude writes JavaScript that makes several tool calls in 1 step. It shipped in Claude Code v2.1.323 last week . For developers, it changes how the agent spends round-trips on multi-step work. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 TL;DR 

 Works with: It works with Claude Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2. 

 Runs on: An interactive terminal session on the native build, v2.1.323 or later. Windows needs Git for Windows. Anthropic API or Claude subscription only. 

 Performance: Anthropic publishes no benchmark or token-saving figure for Code Mode. 

 Best: Background code can run for up to 2 hours while you keep talking to Claude. 

 Worst: Code that Claude waits on stops after 10 minutes. No Bedrock, Google Cloud, Foundry, -p , Agent SDK, VS Code or Desktop. 

 Bottom line: Best: related tool calls run as 1 program. Worst: narrow availability and coarser auto-mode review. 

 What is Code Mode in Claude Code? 

 Without Code Mode, Claude requests each Bash, Read or Edit call directly. It reads every result before choosing the next step. With Code Mode, Claude writes a piece of JavaScript, and Claude Code runs it in your session. 

 According to the docs , one piece of code can run commands in parallel. It can feed one result into the next call. It can also return only the output Claude needs to read. 

 Anthropic’s example raises a retry limit. The code finds the file, edits it and runs the tests: 

 Copy Code Copied Use a different Browser const files = await $`rg -l "function retryPolicy" src`.text();
const target = files.trim().split("\n")[0];
await edit(target, "maxAttempts: 3", "maxAttempts: 5");
({ edited: target, tests: $`npm test -- retryPolicy`.nothrow() }); 

 In the conversation, you see the tool calls, such as the diff. You do not see the code by default. Press Ctrl+O to open the transcript viewer and expand a collapsed Code row. 

 Play side by side</button><button class="btn g" id="code">Show the code</button>
 <span class="note">Blue dashed = model turn. Clay = tool work.</span></div>
 <pre id="cb" style="display:none"><code><span class="k">const</span> files = <span class="k">await</span> $`rg -l "function retryPolicy" src`.text();
<span class="k">const</span> target = files.trim().split("\n")[0];
<span class="k">await</span> edit(target, "maxAttempts: 3", "maxAttempts: 5");
({ edited: target, tests: $`npm test -- retryPolicy`.nothrow() });</code></pre>
 <p class="note" style="margin-top:10px">You see the tool calls (such as the diff), not the code. Press <code>Ctrl+O</code> to open the transcript and expand a Code row.</p>
 </div>

 <div class="panel" id="p2">
 <div class="grid2">
 <div class="card"><div class="lbl">Set the variable</div>
 <span class="pill on" data-s="s1">macOS / Linux / WSL</span><span class="pill" data-s="s2">PowerShell</span><span class="pill" data-s="s3">settings.json</span>
 <pre class="sv" id="s1"><code>CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 claude</code></pre>
 <pre class="sv" id="s2" style="display:none"><code>$env:CLAUDE_CODE_EXPERIMENTAL_CODE_MODE = "1"
claude</code></pre>
 <pre class="sv" id="s3" style="display:none"><code>// ~/.claude/settings.json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_CODE_MODE": "1" } }</code></pre>
 </div>
 <div class="card"><div class="lbl c">Steps</div><ol class="steps">
 <li>Run <code>claude --version</code>; update if older than v2.1.323</li>
 <li>Start with the variable set to 1</li>
 <li>Pick "Yes, turn on Code Mode"</li>
 <li>Give Claude a many-tool-call task</li>
 <li>Press <code>Ctrl+O</code> to read the code</li></ol></div>
 </div>
 <div class="warn">A 0 in your shell or settings wins over a 1. Admins can set 0 in managed settings to block it org-wide, but cannot force it on.</div>
 </div>

 <div class="panel" id="p3">
 <span class="pill on" data-m="auto">Auto mode</span><span class="pill" data-m="other">Other permission modes</span>
 <div class="card" style="margin-top:8px" id="mtxt"></div>
 <div class="warn">Every tool call inside the code still passes your deny and ask rules and PreToolUse hooks under its usual name. To inspect the code, hook the <code>REPL</code> tool and read <code>tool_input.code</code>.</div>
 </div>

 <div class="panel" id="p4">
 <div class="card">
 <div class="bar"><div class="t"><span>Claude waits for the code</span><b>10 min max</b></div><div class="tr"><div class="f" data-w="8.33" style="background:#B0AEA5"></div></div></div>
 <div class="bar"><div class="t"><span>Code runs in the background (you keep chatting)</span><b style="color:#D97757">2 hr max</b></div><div class="tr"><div class="f" data-w="100" style="background:#D97757"></div></div></div>
 <p class="note">The 10-minute limit includes time spent at permission prompts. Background runs need a session started in auto or bypassPermissions mode.</p>
 </div>
 </div>

 <div class="panel" id="p5">
 <div class="x">
 <div class="card"><div class="lbl c">Claude Code Code Mode</div><div class="stat">JS</div><p class="note">Built-in tools in the CLI. No published token figure.</p></div>
 <div class="card"><div class="lbl">Claude API PTC</div><div class="stat">37%</div><p class="note">Python. Avg tokens 43,588 to 27,297 on complex research tasks.</p></div>
 <div class="card"><div class="lbl">Code execution with MCP</div><div class="stat">98.7%</div><p class="note">150,000 to 2,000 tokens in 1 Anthropic example.</p></div>
 </div>
 <div class="warn">Figures come from different tasks and setups. They are not a head-to-head benchmark. Cloudflare coined "Code Mode" (TypeScript, V8 isolates) on Sept 26, 2025.</div>
 </div>

 <div class="foot"><span>Sources: code.claude.com/docs/en/code-mode · anthropic.com/engineering</span><b>© Marktechpost</b></div>
</div>
<script>
(function(){var r=document.getElementById('mtp-ccm');
function rs(){try{parent.postMessage({mtpH:r.offsetHeight+40,id:'mtp-ccm'},'*')}catch(e){}}
r.querySelectorAll('.tab').forEach(function(t){t.onclick=function(){r.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});r.querySelectorAll('.panel').forEach(function(x){x.classList.remove('on')});t.classList.add('on');var p=document.getElementById(t.dataset.p);p.classList.add('on');if(t.dataset.p==='p4')bars();rs()}});
var timers=[];function play(){timers.forEach(clearTimeout);timers=[];var a=[].slice.call(document.querySelectorAll('#fa .node')),b=[].slice.call(document.querySelectorAll('#fb .node'));a.concat(b).forEach(function(n){n.classList.remove('lit')});
a.forEach(function(n,i){timers.push(setTimeout(function(){n.classList.add('lit')},450*(i+1)))});
b.forEach(function(n,i){timers.push(setTimeout(function(){n.classList.add('lit')},i===0?450:(i===4?1350:900)))});}
document.getElementById('play').onclick=play;
document.getElementById('code').onclick=function(){var c=document.getElementById('cb');var s=c.style.display==='none';c.style.display=s?'block':'none';this.textContent=s?'Hide the code':'Show the code';rs()};
r.querySelectorAll('[data-s]').forEach(function(p){p.onclick=function(){r.querySelectorAll('[data-s]').forEach(function(x){x.classList.remove('on')});p.classList.add('on');r.querySelectorAll('.sv').forEach(function(x){x.style.display='none'});document.getElementById(p.dataset.s).style.display='block';rs()}});
var M={auto:'<b>A classifier reviews each piece of code before it runs, not each tool call.</b><br><span class="note">It does not see values computed at run time, such as a path taken from search output. Keep rules or hooks for calls you must control. You can still be prompted when new code starts while earlier code runs.</span>',other:'<b>The code starts without a review.</b><br><span class="note">You are prompted for each tool call that would prompt you in that mode, exactly as without Code Mode.</span>'};
var mt=document.getElementById('mtxt');mt.innerHTML=M.auto;
r.querySelectorAll('[data-m]').forEach(function(p){p.onclick=function(){r.querySelectorAll('[data-m]').forEach(function(x){x.classList.remove('on')});p.classList.add('on');mt.innerHTML=M[p.dataset.m];rs()}});
function bars(){r.querySelectorAll('.f').forEach(function(f){f.style.width='0';setTimeout(function(){f.style.width=f.dataset.w+'%'},60)})}
window.addEventListener('load',function(){rs();setTimeout(play,400)});window.addEventListener('resize',rs);setInterval(rs,1500);
})();
</script>
</body></html>
" style="width:100%;height:600px;border:0;display:block;background:#141413;border-radius:16px;" loading="lazy"> 
 
 window.addEventListener("message",function(e){if(e.data&&e.data.id==="mtp-ccm"&&e.data.mtpH){document.getElementById("mtp-ccm-frame").style.height=e.data.mtpH+"px";}}); 

 How do you turn on Code Mode? 

 Set CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 in your shell, or in the env block of ~/.claude/settings.json . Before the first session, Claude Code asks you to confirm. Select “Yes, turn on Code Mode”. 

 Claude Code then restarts and shows ‘Code Mode (experimental) is on’. 

 A Code Mode session resumes only with the variable still set to 1. Setting 0 anywhere turns it off, even if 1 is set elsewhere. Admins can block it org-wide with a 0 in managed settings . They cannot force it on. 

 When should developers use Code Mode? 

 Anthropic recommends it for tasks with many related tool calls: 

 A change that repeats across many files 

 A search whose results need filtering before Claude reads them 

 Several independent commands that can run at the same time 

 How does Code Mode handle permissions and long-running code? 

 Each tool call inside the code still passes your deny and ask rules. It also passes PreToolUse hooks under the tool’s usual name, such as Bash. 

 Review differs by permission mode: 

 Auto mode: a classifier reviews each piece of code, not each tool call. It cannot see values computed at run time, such as a path from search output. 

 Other modes: code starts without review, and you are prompted per tool call as usual. 

 Hook authors should check each part of a command. A git push can arrive as cd 'app' && git push . To inspect the code itself, match the REPL tool and read tool_input.code . 

 If Claude waits, the code stops after 10 minutes, including time at permission prompts. In the background, it can run for up to 2 hours while you keep chatting. Background runs need a session started in auto or bypassPermissions mode. 

 What are the requirements and limitations? 

 Version: v2.1.323 or later; v2.1.326 or later with agent teams 

 Account: Claude subscription or Console account. Not available through gateways, Amazon Bedrock, Claude Platform on AWS, Google Cloud, or Microsoft Foundry 

 Organization: no HIPAA configuration or zero data retention 

 Surface: interactive terminal only. No -p , Agent SDK, VS Code panel, Desktop app or cloud sessions 

 Blocked settings: API key helper, OpenTelemetry export or DISABLE_TELEMETRY 

 Unavailable features: Remote Control, Claude in Chrome and computer use 

 How does Code Mode compare with other code-first tool calling? 

 Cloudflare coined ‘Code Mode’ on September 26, 2025 . Its Agents SDK turns MCP schemas into a TypeScript API that runs in V8 isolates. 

 Anthropic then published code execution with MCP . In one example, token use fell from 150,000 to 2,000, a 98.7% saving. Its API feature, Programmatic Tool Calling , uses Python. It cut average usage from 43,588 to 27,297 tokens on complex research tasks. 

 Claude Code’s version applies the pattern to the CLI’s own tools. The docs give no token figure. One independent test reported system-tool context of 11.1k tokens with Code Mode versus 24.6k without. Treat that as a single third-party measurement. 

 Feature Claude Code Code Mode Claude API Programmatic Tool Calling Cloudflare Code Mode Standard tool calling Where it runs Claude Code CLI, your session ( docs ) Code execution tool, Claude API ( Anthropic ) Agents SDK, V8 isolates ( Cloudflare ) Any tool-use API Language Claude writes JavaScript Python TypeScript None (JSON calls) Tools it orchestrates Built-in tools (Bash, Read, Edit) Developer-defined tools MCP servers as TypeScript APIs Any Status Experimental, off by default Launched Nov 2025 Worker Loader API in closed beta GA Published token figure Not disclosed 43,588 to 27,297 avg (37%) Not disclosed in launch post Baseline Max run time 10 min waiting, 2 hr background Not disclosed Not disclosed Per call Cloud providers Anthropic API only Not on Bedrock or Google Cloud ( docs ) Cloudflare Workers Broad 

 Key Takeaways 

 Claude writes JavaScript that chains Bash, Read and Edit calls in 1 step. 

 Opt in with CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 on v2.1.323 or later. 

 Background code runs up to 2 hours; waiting code stops at 10 minutes. 

 Auto mode reviews the code, not each tool call. 

 Terminal and Anthropic API only: no Bedrock, Google Cloud, SDK or IDE panel. 

 Check out the Code Mode documentation and the Claude Code changelog . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Anthropic Adds Code Mode to Claude Code: Claude Now Chains Tool Calls in JavaScript appeared first on MarkTechPost .
