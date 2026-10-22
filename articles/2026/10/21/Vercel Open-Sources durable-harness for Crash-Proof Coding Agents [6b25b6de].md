---
id: "6b25b6de8fa6cad2"
title: "Vercel Open-Sources durable-harness for Crash-Proof Coding Agents"
url: "https://marktechpost.com/2026/10/21/vercel-durable-harness-crash-proof-coding-agents"
link: "https://marktechpost.com/2026/10/21/vercel-durable-harness-crash-proof-coding-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T22:15:39Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Vercel has released durable-harness , an open-source package that keeps coding agent sessions alive through crashes and timeouts. Vercel durable-harness wraps existing harnesses, including Pi, OpenCode, Claude Code and Codex, without changing them . Each session lives in a durable log. A dead function no longer means lost work. For teams moving agents off laptops and into the cloud, that closes…"
tags: ["Agentic AI", "AI Shorts", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "New Releases", "Open Source", "Staff", "Tech News", "Technology"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "summary"
word_count: 1468
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Vercel Open-Sources durable-harness for Crash-Proof Coding Agents

MarkTechPost · Michal Sutter · 2026-10-21

Vercel has released durable-harness , an open-source package that keeps coding agent sessions alive through crashes and timeouts. Vercel durable-harness wraps existing harnesses, including Pi, OpenCode, Claude Code and Codex, without changing them . Each session lives in a durable log. A dead function no longer means lost work. For teams moving agents off laptops and into the cloud, that closes a real gap. 

 TL;DR 

 Size: npm package, version 0.0.x, Apache-2.0. Adapters cover 5 harnesses: Pi, OpenCode, fx, Claude Code, Codex. 

 Runs on: Vercel Functions plus Vercel Queues, Node.js 22+ with Postgres, or laptop files. Claude Code and Codex need a Vercel Sandbox. 

 Performance: No latency or throughput benchmarks published. All recovery claims are self-reported by Vercel. 

 Best: Finished model and tool calls are read back from the log, never re-run or billed twice. 

 Worst: Experimental 0.0.x API. Claude Code and Codex run only in a Vercel Sandbox, even self-hosted. 

 What is durable-harness? 

 durable-harness is a set of adapters from Vercel that store a harness session in a Workflow SDK World . A World bundles storage, a queue and a stream behind one interface. The package uses the same machinery that powers Vercel’s Workflow SDK . 

 Why do coding agents lose work in the cloud? 

 Harnesses like Pi and Claude Code were designed as long-lived local processes. They keep the session in memory. Locally, the workspace and history sit on the same disk, so resuming takes 1 prompt. In the cloud, a VM with persistent storage does not track which calls completed. Vercel team notes a failed turn or network error then means lost work. 

 How does durable-harness work? 

 It writes each step of a turn to a durable log. Before a model or tool call runs, it records an intent. When the call finishes, it records the outcome. Each turn is backed by a message on Vercel Queues . If the function dies, the queue hands the turn to a new function. That function reads the log and continues. 

 After a crash, the log shows what finished, what was running and what never started: 

 Completed calls are read from the log, so finished model tokens are not billed again. 

 replay: 'safe' tools , such as lookups, can run again. 

 replay: 'never' tools , such as refunds, never run twice. The model is told the call may have happened. 

 Harness session files are mirrored into the log as well. That covers Claude Code’s transcript, Codex’s rollout and OpenCode’s event store. 

 Where do files and shell commands run? 

 Model-chosen commands never run on the function’s own disk. The tools docs list 3 workspace options: 

 virtual() keeps files in the session log, with a bash-compatible shell and no network. It holds about 500 files. 

 virtual({ durable: false }) keeps scratch files in memory and clears them every turn. 

 sandbox() gives each session a Vercel Sandbox , with /workspace on a Drive. 

 Typed JSON documents , such as a to-do list, also live in the log. Each holds at most 64 KB. 

 Run turn</button>
 <button class="b red" id="kill" disabled>Kill function</button>
 <button class="b ghost" id="rst">Reset</button>
 </div>
 <div class="log" id="lg"><div>Press Run turn, then kill the function while CI is running.</div></div>
 <p class="note">Scenario from Vercel's post: an agent adds a pricing page, opens a PR, and waits for CI. Illustrative simulation, not a benchmark.</p>
 </div>

 <div class="pane" id="p2">
 <p class="sub" style="margin-bottom:12px">Click a tool, then crash it mid-call.</p>
 <div class="rules">
 <div class="box tool sel" data-r="safe"><h4><code>get_order</code><span class="pill">replay: 'safe'</span></h4><span class="note">A lookup. Safe to repeat after a crash.</span></div>
 <div class="box tool" data-r="never"><h4><code>refund_order</code><span class="pill">replay: 'never'</span></h4><span class="note">A refund. Must never run twice.</span></div>
 </div>
 <div class="btns"><button class="b red" id="crash">Crash mid-call</button></div>
 <div class="verdict" id="vd">Pick a tool and press Crash mid-call.</div>
 <pre id="code">{ name: 'get_order', replay: 'safe', ... }</pre>
 </div>

 <div class="pane" id="p3">
 <div class="ws">
 <div class="box sel" data-w="0"><h4><code>virtual()</code></h4><span class="note">Files in the session log. Bash-compatible shell, no network.</span></div>
 <div class="box" data-w="1"><h4><code>virtual({durable:false})</code></h4><span class="note">In-memory scratch. Cleared every turn.</span></div>
 <div class="box" data-w="2"><h4><code>sandbox()</code></h4><span class="note">Per-session Vercel Sandbox, <code>/workspace</code> on a Drive.</span></div>
 </div>
 <div class="box" style="margin-top:14px" id="wsd"></div>
 </div>

 <div class="pane" id="p4">
 <div class="worlds">
 <div class="box world sel" data-g="0"><h4>Vercel</h4><span class="note">Vercel World + Agent Runs traces</span></div>
 <div class="box world" data-g="1"><h4>Laptop</h4><span class="note">Local files, zero config</span></div>
 <div class="box world" data-g="2"><h4>Self-host</h4><span class="note">Postgres World, Node.js 22+</span></div>
 </div>
 <pre id="wc"></pre>
 <p class="note" id="wn"></p>
 </div>

 <div class="pane" id="p5">
 <table>
 <tr><th>Harness</th><th>Package</th><th>Runs in</th><th>Status</th></tr>
 <tr><td>Pi</td><td><code>durable-harness/pi-durable</code></td><td>Your function + virtual workspace or Sandbox</td><td class="y">Supported</td></tr>
 <tr><td>OpenCode</td><td><code>durable-harness/opencode</code></td><td>Your function + virtual workspace or Sandbox</td><td class="y">Supported</td></tr>
 <tr><td>fx</td><td><code>libfx</code></td><td>Durable on its own</td><td class="y">Supported</td></tr>
 <tr><td>Claude Code</td><td><code>durable-harness/claude-code</code></td><td>Vercel Sandbox only</td><td class="n">Experimental</td></tr>
 <tr><td>Codex</td><td><code>durable-harness/codex</code></td><td>Vercel Sandbox only</td><td class="n">Experimental</td></tr>
 </table>
 <p class="note">Claude Code and Codex are single-user CLIs that keep state on disk, so each session gets its own Sandbox.</p>
 </div>

 <div class="ft"><span>Source: vercel.com/blog/making-every-harness-durable · Vercel docs · Oct 2026</span><b>© Marktechpost</b></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-dh');
function $(s){return R.querySelector(s)}function $$(s){return R.querySelectorAll(s)}
function rz(){try{parent.postMessage({mtpEmbedHeight:R.offsetHeight+40,id:'mtp-dh'},'*')}catch(e){}}
$$('.tab').forEach(function(t){t.onclick=function(){$$('.tab').forEach(function(x){x.classList.remove('on')});$$('.pane').forEach(function(x){x.classList.remove('on')});t.classList.add('on');$('#'+t.dataset.t).classList.add('on');if(t.dataset.t==='p3')ws(cur);setTimeout(rz,60)}});
var S=[['model','Plan the change',1],['read','app/page.tsx',0],['write','app/pricing/page.tsx',0],['run','gh pr create',0],['wait','CI checks on the PR',0],['model','Reply with the result',1]];
function draw(id){var o=$(id);o.innerHTML='';S.forEach(function(s){var li=document.createElement('li');li.innerHTML='<span class="k">'+s[0]+'</span>'+s[1];o.appendChild(li)})}
var i=0,tm=null,killed=false,ma=0,mb=0;
function log(t,c){var l=$('#lg'),d=document.createElement('div');d.className=c||'';d.textContent=t;l.appendChild(d);while(l.children.length>6)l.removeChild(l.firstChild)}
function reset(){clearTimeout(tm);i=0;killed=false;ma=mb=0;draw('#sA');draw('#sB');$('#aRe').textContent=0;$('#bRe').textContent=0;$('#aMc').textContent=0;$('#bMc').textContent=0;$('#go').disabled=false;$('#kill').disabled=true;$('#lg').innerHTML='<div>Press Run turn, then kill the function while CI is running.</div>'}
function li(id,n){return $(id).children[n]}
function step(){if(i>=S.length){$('#kill').disabled=true;log('turn complete','o');return}
 ['#sA','#sB'].forEach(function(id){var e=li(id,i);e.className='run'});
 log('intent '+S[i][0]+' '+S[i][1],'i');
 tm=setTimeout(function(){['#sA','#sB'].forEach(function(id){li(id,i).className='done'});if(S[i][2]){ma++;mb++;$('#aMc').textContent=ma;$('#bMc').textContent=mb}log('outcome '+S[i][0]+' ok','o');i++;step()},i===4?1800:700)}
$('#go').onclick=function(){reset();$('#go').disabled=true;$('#kill').disabled=false;$('#lg').innerHTML='';step()};
$('#rst').onclick=reset;
$('#kill').onclick=function(){if(i>=S.length)return;clearTimeout(tm);killed=true;$('#kill').disabled=true;var k=i;
 li('#sA',k).className='dead';li('#sB',k).className='dead';log('function 1 died at step '+(k+1),'x');
 setTimeout(function(){log('without durability: manual restart, turn starts over','x');
 draw('#sA');var re=0,j=0;(function a(){if(j>=S.length){$('#aRe').textContent=re;return}var e=li('#sA',j);e.className='run';setTimeout(function(){e.className=j<k?'rerun':'done';if(j<k){re++;$('#aRe').textContent=re}if(S[j][2]){ma++;$('#aMc').textContent=ma}j++;a()},260)})();
 log('with durable-harness: queue hands turn to function 2','o');
 for(var q=0;q<k;q++)li('#sB',q).className='fromlog';
 i=k;(function b(){if(i>=S.length){log('turn complete, 0 steps repeated','o');return}var e=li('#sB',i);e.className='run';setTimeout(function(){e.className='done';if(S[i][2]){mb++;$('#bMc').textContent=mb}i++;b()},450)})();
 },600)};
reset();
var rule='safe';
$$('.tool').forEach(function(t){t.onclick=function(){$$('.tool').forEach(function(x){x.classList.remove('sel')});t.classList.add('sel');rule=t.dataset.r;$('#vd').textContent='Pick a tool and press Crash mid-call.';$('#code').textContent=rule==='safe'?"{ name: 'get_order', replay: 'safe', ... }":"{ name: 'refund_order', replay: 'never', ... }"}});
$('#crash').onclick=function(){var v=$('#vd');v.style.opacity=0;setTimeout(function(){v.innerHTML=rule==='safe'?'<b style="color:#50e3c2">Resumed:</b> the interrupted lookup can run again. Pi reruns it; Claude Code, Codex and OpenCode tell the model it is safe to repeat.':'<b style="color:#f5a623">Never re-run:</b> the model is told the refund may or may not have happened, so it can check first. Every harness waits for the log to record a \'never\' call before it starts.';v.style.transition='opacity .3s';v.style.opacity=1;rz()},150)};
var W=[{t:'Short tasks and small workspaces',f:['Files kept','In the session log'],m:[['Workspace size','about 500 files',55]],x:'A crash mid-call leaves nothing behind, and the call runs again. Cost: function CPU plus log events and storage.'},
{t:'Scratch work within a turn',f:['Files kept','Cleared every turn'],m:[['Persistence','none across turns',8]],x:'Nothing goes to the log. The model is told files are cleared. Cost: function CPU only.'},
{t:'Real projects and long-running work',f:['Files kept','On a Drive that outlives every Sandbox'],m:[['Isolation','1 Sandbox per session',100]],x:'A command a crash interrupts may have partly run, and the model is told. Cost: Sandbox and Drive usage, plus a start on first use.'}];
var cur=0;function ws(n){cur=n;var w=W[n];$('#wsd').innerHTML='<h4>Best for: '+w.t+'</h4><div class="note">'+w.f[0]+': <b style="color:#fff">'+w.f[1]+'</b></div>'+w.m.map(function(m){return '<div class="meter"><i></i></div><div class="ml"><span>'+m[0]+'</span><span>'+m[1]+'</span></div>'}).join('')+'<p class="note">'+w.x+' Typed JSON documents live in the log too, up to 64 KB each.</p>';setTimeout(function(){$$('#wsd .meter i').forEach(function(e){e.style.width=w.m[0][2]+'%'});rz()},40)}
$$('.ws .box').forEach(function(b){b.onclick=function(){$$('.ws .box').forEach(function(x){x.classList.remove('sel')});b.classList.add('sel');ws(+b.dataset.w)}});ws(0);
var G=[["// On Vercel: @workflow/world-vercel is picked automatically\nimport { claudeCode } from 'durable-harness/claude-code'\nexport const agent = claudeCode({ model: 'anthropic/claude-sonnet-5.5' })",'Sessions show up in Agent Runs with each model and tool call. Resumed turns appear in the same trace.'],
["# Local dev: @workflow/world-local, no configuration\n# sessions live in .workflow-data by default\nnpm install durable-harness",'The local World suits development and a single server with a persistent disk.'],
["# Self-host: 2 variables move every agent to Postgres\nWORKFLOW_TARGET_WORLD=\"@workflow/world-postgres\"\nWORKFLOW_POSTGRES_URL=\"postgres://user:password@host:5432/database\"",'Needs @workflow/world-postgres 5.0.4+ and Node.js 22+. It is a reference implementation: no route auth, no encryption, not tuned for scale.']];
function wd(n){$('#wc').textContent=G[n][0];$('#wn').textContent=G[n][1];rz()}
$$('.world').forEach(function(b){b.onclick=function(){$$('.world').forEach(function(x){x.classList.remove('sel')});b.classList.add('sel');wd(+b.dataset.g)}});wd(0);
window.addEventListener('load',rz);window.addEventListener('resize',rz);setTimeout(rz,300);
})();
</script>
</body></html>
"> 

window.addEventListener('message',function(e){if(e.data&&e.data.id==='mtp-dh'&&e.data.mtpEmbedHeight){var f=document.getElementById('mtp-dh-frame');if(f){f.style.height=e.data.mtpEmbedHeight+'px';}}});

 Where can you run durable-harness? 

 The agent code stays the same across Worlds: 

 Vercel: the Vercel World, with every session traced in Agent Runs . 

 Local: files on your machine, with no configuration. 

 Self-hosted: the Postgres World , version 5.0.4 or later, on Node.js 22+. Vercel’s blog also lists MongoDB, Redis and Turso. 

 2 environment variables, WORKFLOW_TARGET_WORLD and WORKFLOW_POSTGRES_URL , move an agent to Postgres. 

 How does durable-harness compare? 

 Feature durable-harness Temporal + OpenAI Agents SDK Inngest AgentKit Cloudflare Agents SDK What it is Durability adapters for existing coding harnesses Durable execution wrapper for OpenAI Agents SDK TypeScript multi-agent framework Stateful agents on Durable Objects Wraps Claude Code / Codex Yes, experimental, Sandbox-only Not disclosed Not disclosed Not disclosed Durability backend Workflow SDK World (Vercel, local, Postgres) Temporal server or Temporal Cloud Inngest orchestration engine Durable Objects, Cloudflare Workflows Language TypeScript Python TypeScript TypeScript License Apache-2.0 MIT (server) Apache-2.0 MIT Status 0.0.x, experimental GA since Mar 23, 2026 Not disclosed Not disclosed 

 Key Takeaways 

 durable-harness logs every model and tool call, then resumes crashed turns on a new function. 

 Finished calls are never repeated, so tokens are not billed twice. 

 Pi and OpenCode run in your function; Claude Code and Codex need a Vercel Sandbox. 

 Self-hosting works with 2 env vars and a Postgres World. 

 It is 0.0.x and experimental, with no published benchmarks. 

 Check out the GitHub repo , docs and Vercel’s announcement . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Vercel Open-Sources durable-harness for Crash-Proof Coding Agents appeared first on MarkTechPost .
