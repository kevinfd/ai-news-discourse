---
id: "b08daa645d121933"
title: "Meet Factory Droid 1.0: A Model-Independent Coding Agent Harness Built on Script Mode"
url: "https://marktechpost.com/2026/10/31/factory-droid-1-0-frontier-harness"
link: "https://marktechpost.com/2026/10/31/factory-droid-1-0-frontier-harness"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-31T10:38:14Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Factory has released Droid 1.0 , the largest update yet to the Factory Droid agent harness. The main change is programmatic tool calling, now on by default. The model writes a program that runs its tools. One model request can now drive hundreds of tool calls. \n\n TL;DR \n\n Size: Base prompt is 13,055 input tokens, down 37% from 20,887. Only 2 tool definitions ship up front, down from 11. \n\n Runs…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "New Releases", "Software Engineering"]
orgs: ["OpenAI", "Anthropic", "Cursor"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 1417
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Factory Droid 1.0: A Model-Independent Coding Agent Harness Built on Script Mode

MarkTechPost · Asif Razzaq · 2026-10-31

Factory has released Droid 1.0 , the largest update yet to the Factory Droid agent harness. The main change is programmatic tool calling, now on by default. The model writes a program that runs its tools. One model request can now drive hundreds of tool calls. 

 TL;DR 

 Size: Base prompt is 13,055 input tokens, down 37% from 20,887. Only 2 tool definitions ship up front, down from 11. 

 Runs on: macOS and Windows desktop app, a terminal UI, and the Node SDK @factory/droid-sdk . Works with any supported model, including your own API keys. 

 Performance: Highest pass rate of every harness Factory tested, on the same model, at lower cost. 

 Best: 65.2% on Terminal-Bench 4 with Claude Opus 5.5, at $4.73 per passed task (self-reported). 

 Worst: With GPT-6.1 Sol, Droid takes 10% longer per passed task than Codex. 

 What is Droid 1.0? 

 Droid 1.0 is a model-independent coding agent harness from Factory. Factory defines a harness as everything around the model. That means the prompts, the tools, how tool results return, and the loop . Users pick a model or let Factory Router choose a cost-efficient mix. 

 How does programmatic tool calling work? 

 In a standard loop, every tool output lands in the model’s context. With programmatic tool calling (PTC), the model writes a program instead. Droid implements this as a Script tool . The model writes JavaScript that runs in a sandbox. The sandbox has no file, network, or system access of its own. 

 Raw files, search results, and logs stay inside the program. Only printed output returns to the model. Independent calls run concurrently. 

 The idea builds on CodeAct (Wang et al., 2024) . Factory reports these results from its own sessions: 

 Unit test fix: 15 tool calls took 5 model calls instead of 10. The task finished in 41.6 s instead of 56.8 s. 

 Linear cleanup: 151 issues moved and verified in 312 tool calls. The Script used 2 requests and about 61,000 tokens. Factory models direct calls at 36 requests and about 3.1M tokens. 

 CI sweep: 5,384 jobs across 547 runs, in 2 requests. Under 0.1% of tool results reached the model’s context. 

 On Claude Opus 5.5, Script mode cuts Droid’s cost by 15% versus direct tool calling. It is on by default for 10 models, including GPT-6.1 Sol and Kimi K3. 

 Play the race</button>
 <div class="race">
 <div class="lane"><b>Direct tool calls</b><div class="dots" id="lnA"></div><div class="stat"><span>Model calls <strong id="aM">0</strong></span><span>Tool calls <strong id="aT">0</strong></span><span>Time <strong id="aS">0.0 s</strong></span></div></div>
 <div class="lane"><b>Script tool</b><div class="dots" id="lnB"></div><div class="stat"><span>Model calls <strong id="bM">0</strong></span><span>Tool calls <strong id="bT">0</strong></span><span>Time <strong id="bS">0.0 s</strong></span></div></div>
 </div>
 <div class="lg"><span><i style="background:#2f6bff"></i>Model call</span><span><i style="background:#c9c9c9"></i>Tool call</span><span><i style="background:#111"></i>Script</span></div>
 <p class="note">The Script is JavaScript in a sandbox with no file, network or system access of its own. Raw tool results stay in the program; only printed output returns to the model.</p>
 </div>

 <div class="pn" id="p2">
 <h3>Terminal-Bench 4 pass rate, same model per harness</h3>
 <div class="seg"><button class="on" data-m="opus">Claude Opus 5.5</button><button data-m="sol">GPT-6.1 Sol</button></div>
 <div id="fdxBars"></div>
 <p class="note" id="fdxCost"></p>
 <p class="note">Self-reported by Factory. 3 trials per task, run October 23 to 28, 2026. Cursor was not tested on GPT-6.1 Sol.</p>
 </div>

 <div class="pn" id="p3">
 <h3>Moving 151 Linear issues: 312 tool calls</h3>
 <p>Each issue was moved to the backlog, then checked so that only its status changed.</p>
 <button class="btn gh" id="fdxLin"> Compare</button>
 <div class="cmp" style="margin-top:12px">
 <div class="box"><div class="lbl">Direct calls (modeled, 10 per request)</div><div class="big" id="lA">0</div><div class="lbl">model requests</div><div class="big" id="lAt" style="font-size:22px;margin-top:8px">0</div><div class="lbl">input tokens</div><div class="tk"><div id="lAb" style="background:#9aa6bf"></div></div></div>
 <div class="box"><div class="lbl">One Script</div><div class="big b" id="lB">0</div><div class="lbl">model requests</div><div class="big b" id="lBt" style="font-size:22px;margin-top:8px">0</div><div class="lbl">input tokens</div><div class="tk"><div id="lBb" style="background:#2f6bff"></div></div></div>
 </div>
 <p class="note">Direct-call figures are Factory's estimates; the Script figures come from a real session.</p>
 </div>

 <div class="pn" id="p4">
 <h3>Other changes in Droid 1.0 (tap a card)</h3>
 <div class="cards">
 <div class="cd"><div class="n">−37%</div><div class="t">Base prompt</div><div class="x">First request fell from 20,887 to 13,055 input tokens. Droid now sends 2 tool definitions up front instead of 11.</div></div>
 <div class="cd"><div class="n">98%</div><div class="t">Cache reads</div><div class="x">A typical production request reads 98% of its input from cache. Newly loaded tools are appended at the end so the cached prefix holds.</div></div>
 <div class="cd"><div class="n">−15%</div><div class="t">Script mode cost</div><div class="x">Script mode cuts Droid's cost by 15% on Claude Opus 5.5 compared with direct tool calling.</div></div>
 <div class="cd"><div class="n">16K</div><div class="t">Compaction room</div><div class="x">Compaction summaries can now hold 16,000 tokens, up from 8,000. 3 identical tool calls trigger a nudge; 6 stop the loop.</div></div>
 <div class="cd"><div class="n">488 ms</div><div class="t">First paint</div><div class="x">Median time to first paint fell from 1,839 ms to 488 ms. Median quit time fell from 648 ms to 30 ms.</div></div>
 <div class="cd"><div class="n">~20 MB</div><div class="t">Per extra session</div><div class="x">Sessions now share the daemon process, adding about 20 MB each instead of about 350 MB per process.</div></div>
 </div>
 </div>

 <div class="ft"><span>Source: <a href="https://factory.com/news/frontier-harness" target="_blank" rel="noopener">Factory Research, Oct 29, 2026</a> · figures self-reported</span><span class="mtp">© Marktechpost</span></div>
</div>
<script>
(function(){
var W=document.getElementById('fdx-wrap');
function rs(){try{parent.postMessage({fdxHeight:W.offsetHeight+40},'*')}catch(e){}}
W.querySelectorAll('.tab').forEach(function(t){t.onclick=function(){W.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});W.querySelectorAll('.pn').forEach(function(x){x.classList.remove('on')});t.classList.add('on');document.getElementById(t.dataset.p).classList.add('on');if(t.dataset.p==='p2')bars(cur);setTimeout(rs,60)}});
/* race */
var A=[[1,2],[1,1],[1,1],[1,1],[1,1],[1,2],[1,2],[1,2],[1,2],[1,1]],B=[[1,6],[1,2],[1,2],[1,4],[1,1]];
function race(){var la=document.getElementById('lnA'),lb=document.getElementById('lnB');la.innerHTML='';lb.innerHTML='';
function seq(steps,lane,ids,total,scr){var items=[];steps.forEach(function(s,i){items.push('m');var last=(i===steps.length-1);if(scr&&!last){items.push('s')}for(var k=0;k<s[1];k++)items.push('t')});
var m=0,t=0,i=0,step=total/items.length;var iv=setInterval(function(){if(i>=items.length){clearInterval(iv);document.getElementById(ids[2]).textContent=total.toFixed(1)+' s';return}var d=document.createElement('span');d.className='d '+items[i];lane.appendChild(d);setTimeout(function(){d.classList.add('show')},20);if(items[i]==='m')m++;if(items[i]==='t')t++;document.getElementById(ids[0]).textContent=m;document.getElementById(ids[1]).textContent=t;document.getElementById(ids[2]).textContent=(step*(i+1)).toFixed(1)+' s';i++;rs()},step*45)}
seq(A,la,['aM','aT','aS'],56.8,false);seq(B,lb,['bM','bT','bS'],41.6,true)}
document.getElementById('fdxRun').onclick=race;
/* bars */
var D={opus:{rows:[['Droid',65.2],['Cursor',62.1],['OpenCode',62.1],['Devin',59.6],['Claude Code',57.6]],c:'Droid: $4.73 per passed task, up to 24% cheaper and 16% to 26% faster than every other harness on Opus 5.5.'},sol:{rows:[['Droid',57.6],['Codex',54.0],['OpenCode',51.0],['Devin',45.0]],c:'Droid: $0.79 per passed task, 12% cheaper than Codex but 10% slower per passed task.'}},cur='opus';
function bars(k){cur=k;var h='';D[k].rows.forEach(function(r){h+='<div class="bar"><span>'+r[0]+'</span><div class="trk"><div class="fill'+(r[0]==='Droid'?' me':'')+'" data-w="'+(r[1]/70*100)+'"></div></div><span class="val">'+r[1].toFixed(1)+'%</span></div>'});var b=document.getElementById('fdxBars');b.innerHTML=h;document.getElementById('fdxCost').textContent=D[k].c;setTimeout(function(){b.querySelectorAll('.fill').forEach(function(f){f.style.width=f.dataset.w+'%'})},40);rs()}
W.querySelectorAll('.seg button').forEach(function(b){b.onclick=function(){W.querySelectorAll('.seg button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');bars(b.dataset.m)}});
/* linear */
function cnt(el,to,fmt,ms){var s=null;function f(ts){if(!s)s=ts;var p=Math.min((ts-s)/ms,1);el.textContent=fmt(to*p);if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
document.getElementById('fdxLin').onclick=function(){cnt(document.getElementById('lA'),36,function(v){return Math.round(v)},1100);cnt(document.getElementById('lB'),2,function(v){return Math.round(v)},600);cnt(document.getElementById('lAt'),3.1,function(v){return '~'+v.toFixed(1)+'M'},1100);cnt(document.getElementById('lBt'),61,function(v){return '~'+Math.round(v)+'K'},600);document.getElementById('lAb').style.width='100%';document.getElementById('lBb').style.width=(61/3100*100).toFixed(2)+'%'};
W.querySelectorAll('.cd').forEach(function(c){c.onclick=function(){c.classList.toggle('open');setTimeout(rs,380)}});
bars('opus');window.addEventListener('load',rs);window.addEventListener('resize',rs);setTimeout(rs,300);
})();
</script>
</body></html>
"> 

window.addEventListener('message',function(e){if(e.data&&e.data.fdxHeight){var f=document.getElementById('fdx-frame');if(f)f.style.height=e.data.fdxHeight+'px';}});

 How does Droid 1.0 score on Terminal-Bench 4? 

 Factory ran each harness against Droid on the same model. Each harness ran 3 trials per task, from October 23 to 28, 2026. Only tasks both harnesses passed in all 3 trials count toward cost and time. 

 Claude Opus 5.5: Droid scores 65.2%. Cursor and OpenCode score 62.1%, Devin 59.6%, Claude Code 57.6%. Droid costs up to 24% less. 

 GPT-6.1 Sol: Droid scores 57.6% at $0.79 per passed task. Codex scores 54.0%, OpenCode 51.0%, Devin 45.0%. 

 Speed: On Opus 5.5, Droid takes 16% to 26% less time per passed task. Against Claude Code, it also uses 17% fewer tokens. 

 What else changed in the harness? 

 Most changes came from an internal Agent Factory loop. Agents read failures and propose changes, tested on every affected model family. Engineers review and merge. 

 Prompt cache: Newly loaded tools are appended to the request end. The typical production request reads 98% of input from cache. 

 Leaner first request: Tool definitions fell 46%. Rarely used tools now load on demand. 

 Bounded autonomy: 3 identical tool calls trigger a nudge, and 6 stop the loop. Compaction summaries now hold 16,000 tokens, up from 8,000. 

 App latency: First paint fell from 1,839 ms to 488 ms. Each extra session now adds about 20 MB, not 350 MB. 

 Comparison: Droid 1.0 vs other coding agent harnesses 

 Feature Droid 1.0 ( Factory ) Codex CLI Claude Code OpenCode Developer Factory OpenAI Anthropic Anomaly Model support Model-independent, BYOK, Factory Router ChatGPT plan or API key Native harness for Claude ( Factory ) 75+ LLM providers, local models License Not disclosed (SDK is Apache 2.0 ) Apache-2.0 Anthropic Commercial Terms MIT Programmatic tool calling Default (Script tool) Yes, per Factory Not disclosed Not disclosed TB4, Claude Opus 5.5* 65.2% Not tested 57.6% 62.1% TB4, GPT-6.1 Sol* 57.6% 54.0% Not tested 51.0% Time per passed task vs Droid* Baseline Droid 10% slower (Sol) Droid 26% faster (Opus) Droid 4% to 24% faster Pricing From $20/mo ChatGPT plan or API Not disclosed Free, open source 

 *Terminal-Bench 4 figures are Factory’s own runs, from its methodology section . 

 How can developers try it? 

 Droid 1.0 ships as a desktop app and terminal UI . The Droid SDK runs the same harness from Node, with sessions, streaming and MCP tools. Paid plans start at $20 per month . 

 Key Takeaways 

 Droid 1.0 makes programmatic tool calling the default. 

 1 Script can run hundreds of tool calls per model request. 

 65.2% on Terminal-Bench 4 with Opus 5.5, self-reported. 

 Base prompt shrank 37%, to 13,055 tokens. 

 Codex still wins on speed with GPT-6.1 Sol. 

 Check out the full Factory research post , the Droid SDK on GitHub and the Droid docs . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Meet Factory Droid 1.0: A Model-Independent Coding Agent Harness Built on Script Mode appeared first on MarkTechPost .
