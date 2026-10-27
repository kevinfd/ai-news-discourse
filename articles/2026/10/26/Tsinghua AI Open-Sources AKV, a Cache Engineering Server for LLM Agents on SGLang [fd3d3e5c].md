---
id: "fd3d3e5cdcaec682"
title: "Tsinghua AI Open-Sources AKV, a Cache Engineering Server for LLM Agents on SGLang"
url: "https://marktechpost.com/2026/10/26/tsinghua-akv-kv-cache-engineering-llm-agents"
link: "https://marktechpost.com/2026/10/26/tsinghua-akv-kv-cache-engineering-llm-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-26T07:56:45Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Tsinghua University and CUHK researchers open-sourced AKV , a serving system for KV cache engineering in LLM agents. Instead of summarizing old history, agents drop selected KV cache entries and keep reusing the rest. Across 3 models and 4 agent benchmarks, average cost falls 27.7% . Average task score rises 1.7 points. The code is Apache-2.0 licensed and builds on SGLang . \n\n TL;DR \n\n What it…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "New Releases", "Open Source", "Software Engineering", "Staff"]
orgs: ["Nvidia", "OpenAI"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "policy & regulation"]
content_source: "summary"
word_count: 1934
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Tsinghua AI Open-Sources AKV, a Cache Engineering Server for LLM Agents on SGLang

MarkTechPost · Asif Razzaq · 2026-10-26

Tsinghua University and CUHK researchers open-sourced AKV , a serving system for KV cache engineering in LLM agents. Instead of summarizing old history, agents drop selected KV cache entries and keep reusing the rest. Across 3 models and 4 agent benchmarks, average cost falls 27.7% . Average task score rises 1.7 points. The code is Apache-2.0 licensed and builds on SGLang . 

 TL;DR 

 What it is: Serving system plus policy library, no weights. Tested on GPT-OSS-120B (5.1B active), MiniMax-M2.7 (230B total, 10B active) and MiroThinker-1.7-Mini (30B total, 3B active). 

 Runs on: NVIDIA GPUs via SGLang. Paper used 8 A800-80GB GPUs in BF16. Quick start serves GPT-OSS-120B on 2 GPUs (tensor parallel 2). 

 Performance: 27.7% lower average cost and +1.7 points average score versus threshold summarization. 

 Best: GPT-OSS-120B on SWE-bench Verified: cost per task 20.0 to 9.7 cents, score 40.0 to 43.2. 

 Worst: MiniMax-M2.7 on BrowseComp-Plus scores 58.9, 3.4 points below Text Engineering’s 62.3. 

 What is cache engineering, and how is it different from context engineering? 

 AKV is a Tsinghua serving system that lets LLM agents drop and reposition their own KV cache. 

 Context engineering trims or summarizes the text history. Editing that prefix invalidates every later KV state. The retained suffix must then be re-prefilled. Harnesses therefore summarize late and aggressively, which can lose details from middle rounds. 

 Cache engineering leaves the text trajectory untouched. It only changes which KV entries stay visible to attention. Retained entries are reused without recomputation. They can still carry information from dropped messages. In the research paper’s cost analysis, KV cache reads made up 82.4% of total API cost. 

 How does AKV work? 

 AKV defines 3 cache operations. Append is the standard update for new tokens. Drop removes selected entries from future attention without changing positions. Repos rewrites retained keys to positions 0 through r-1 using a RoPE rotation . Values stay unchanged, so no hidden states are recomputed. In ablations, adding Repos raised GPT-OSS-120B’s BrowseComp-Plus pass rate from 55% to 62%. 

 The hard part is serving. Identical tokens can produce different cache states under different operation histories. Plain prefix matching could reuse the wrong states. AKV extends SGLang’s radix tree with drop and reposition nodes. It frees dropped KV only when no active request still needs it. Segment-batch attention restores evicted states in 1 prefill pass. 

 What does the AKV API look like? 

 The interface is stateless and OpenAI-compatible . Clients send the full message history and two optional fields. drop_message maps a trigger message index to the messages to drop. reposition lists the indices after which positions get compacted. 

 A CachePolicy builds those fields from a trigger, a selector and a reposition rule. Built-in policies are turn-based, token-based or model-based. A CacheTool lets the model call drop_context itself. 

 How does AKV perform on agent benchmarks? 

 The main policy is a tool-response rolling drop that keeps the latest 12 tool responses. The Standard baseline summarizes at 96K tokens (192K for MiroThinker). Text Engineering summarizes at 48K. Benchmarks are BrowseComp-Plus , GAIA-Text , SWE-bench Verified and xbench-DeepSearch-2510 . 

 Model Standard score / cost Text Eng. score / cost AKV score / cost MiniMax-M2.7 52.4 / 5.0 52.8 / 5.7 53.7 / 4.4 GPT-OSS-120B 51.0 / 11.2 48.3 / 10.2 53.1 / 7.3 MiroThinker-1.7-Mini 44.1 / 20.4 37.1 / 18.1 45.8 / 14.8 

 Average pass rate (%) and cost (US cents per task) across 4 benchmarks. Source: Table 1 of the paper . 

 AKV also cuts cost 21.9% versus Text Engineering. The accuracy gap opens on long runs. On BrowseComp-Plus at 96K tokens and above, GPT-OSS-120B scores 37% with AKV. Standard scores 24% and Text Engineering 32%, per the project page . 

 Costs are API-equivalent estimates from published rates. Repositioned tokens are charged at the cache-hit rate, a deliberately conservative choice. 

 Trim old tool result A</button><button class="btn" id="mtp-akv-reset">Reset</button></div>
 <div class="cmp" style="margin-top:12px">
 <div class="box"><h4>Context engineering (summarize text)</h4>
 <div class="lane" id="mtp-akv-ce"></div>
 <div class="meter"><i id="mtp-akv-cem" style="width:0%"></i></div>
 <div class="mtxt" id="mtp-akv-cet">Re-prefill work: 0 blocks</div>
 </div>
 <div class="box"><h4>Cache engineering (AKV drop)</h4>
 <div class="lane" id="mtp-akv-ae"></div>
 <div class="meter"><i id="mtp-akv-aem" style="width:0%"></i></div>
 <div class="mtxt" id="mtp-akv-aet">Re-prefill work: 0 blocks</div>
 </div>
 </div>
 <p class="note" id="mtp-akv-n1">Both agents hold a user prompt, assistant turns and tool results. Press the button to remove old tool result <b>A</b>.</p>
 <div class="lg"><span><i style="background:#5a3a6a"></i>User</span><span><i style="background:#7d2f93"></i>Assistant</span><span><i style="background:#a64bbd"></i>Tool result</span><span><i style="background:#ffb347"></i>Recomputed</span><span><i style="background:#76B900"></i>New turn</span></div>
</div>

<!-- P2 -->
<div class="panel" id="mtp-akv-p2">
 <div class="row">
 <button class="btn" data-op="append">1. Append D</button>
 <button class="btn" data-op="drop">2. Drop B</button>
 <button class="btn" data-op="repos">3. Repos</button>
 <button class="btn" data-op="reset2">Reset</button>
 </div>
 <div class="lbl">Active KV cache (number = position encoding index)</div>
 <div class="lane" id="mtp-akv-ops"></div>
 <p class="note" id="mtp-akv-n2">Start state: tokens A, B, C sit at positions 0, 1, 2. Step through the 3 operations.</p>
 <pre id="mtp-akv-req">{"messages": [...], "drop_message": {}, "reposition": []}</pre>
</div>

<!-- P3 -->
<div class="panel" id="mtp-akv-p3">
 <div class="lbl" style="margin-top:0">Model</div>
 <div class="row" id="mtp-akv-models"></div>
 <div class="lbl">Benchmark</div>
 <div class="row" id="mtp-akv-bench"></div>
 <div class="grid2" style="margin-top:14px">
 <div><div class="lbl" style="margin-top:0">Pass rate (%) · higher is better</div><div class="bars" id="mtp-akv-sc"></div></div>
 <div><div class="lbl" style="margin-top:0">Cost (US cents per task) · lower is better</div><div class="bars" id="mtp-akv-co"></div></div>
 </div>
 <p class="note" id="mtp-akv-n3"></p>
</div>

<!-- P4 -->
<div class="panel" id="mtp-akv-p4">
 <div class="lbl" style="margin-top:0">Concurrency: <b id="mtp-akv-cv" style="color:#f3eaf6">14</b> · GPT-OSS-120B · 80 long-context SWE-bench Verified tasks · 8 A800 GPUs</div>
 <input type="range" id="mtp-akv-c" min="0" max="4" step="1" value="3">
 <div class="grid2" style="margin-top:12px">
 <div><div class="lbl" style="margin-top:0">P95 request latency (s) · lower is better</div><div class="bars" id="mtp-akv-lat"></div></div>
 <div><div class="lbl" style="margin-top:0">Output throughput (tokens/s) · higher is better</div><div class="bars" id="mtp-akv-out"></div></div>
 </div>
 <div class="stats" style="margin-top:14px">
 <div class="stat"><div class="big">1.18x</div><span>Output throughput, peak vs peak</span></div>
 <div class="stat"><div class="big">1.53x</div><span>Input throughput, peak vs peak</span></div>
 <div class="stat"><div class="big">1.51x</div><span>Faster P95 latency, peak vs peak</span></div>
 <div class="stat"><div class="big">2.849ms</div><span>Full attention per decode step (was 7.082)</span></div>
 </div>
 <p class="note" id="mtp-akv-n4"></p>
</div>

<!-- P5 -->
<div class="panel" id="mtp-akv-p5">
 <ul class="lim" id="mtp-akv-lim">
 <li>Few supported model families<em>Drop and Repos are enabled for Qwen, GPT-OSS and MiniMax-M2 text architectures. Linear attention models are future work.</em></li>
 <li>Self-hosted only<em>You run the AKV server yourself. It extends SGLang with cache-operation support.</em></li>
 <li>Self-reported, single hardware setup<em>All results come from the authors, on 8 A800-80GB GPUs in BF16.</em></li>
 <li>Different measurement windows<em>High-concurrency AKV runs were measured through the first 30 task completions. Standard used a 1-hour window.</em></li>
 <li>Not every benchmark improves<em>MiniMax-M2.7 on BrowseComp-Plus scores 58.9 with AKV, below Text Engineering at 62.3.</em></li>
 <li>Dropping reasoning cache hurts<em>On SWE-bench Verified, dropping reasoning cache fell to 36.5, and dropping both to 34.5, versus 41.0 for tool drop.</em></li>
 </ul>
 <p class="note">Tap a row to expand it.</p>
</div>

<div class="ft">
 <span>Sources: <a href="https://arxiv.org/abs/2610.28577" target="_blank" rel="noopener">Paper</a> · <a href="https://github.com/thu-nics/AKV" target="_blank" rel="noopener">GitHub</a> · <a href="https://fuvty.github.io/thinking_yard_project_page/projects/akv/" target="_blank" rel="noopener">Project page</a> · numbers self-reported</span>
 <span class="mtp">© Marktechpost</span>
</div>

<script>
(function(){
var R=document.getElementById('mtp-akv');
function $(id){return document.getElementById('mtp-akv-'+id)}
function post(){try{var h=R.offsetHeight+40;parent.postMessage({mtpAkvHeight:h},'*')}catch(e){}}
R.querySelectorAll('.tab').forEach(function(b){b.addEventListener('click',function(){
 R.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});
 R.querySelectorAll('.panel').forEach(function(x){x.classList.remove('on')});
 b.classList.add('on');$(b.getAttribute('data-t').replace('p','p')).classList.add('on');
 if(b.getAttribute('data-t')==='p3')drawBench();
 if(b.getAttribute('data-t')==='p4')drawServe();
 setTimeout(post,60);setTimeout(post,500);
})});
function blk(t,cls,sub){var d=document.createElement('div');d.className='blk '+cls;d.innerHTML=t+(sub!==undefined?'<small>'+sub+'</small>':'');return d}
/* P1 */
var seq=[['U','k-u'],['A','k-t'],['B','k-a'],['C','k-t'],['D','k-a']];
function initP1(){var ce=$('ce'),ae=$('ae');ce.innerHTML='';ae.innerHTML='';
 seq.forEach(function(s){ce.appendChild(blk(s[0],s[1]));ae.appendChild(blk(s[0],s[1]))});
 $('cem').style.width='0%';$('aem').style.width='0%';$('cet').textContent='Re-prefill work: 0 blocks';$('aet').textContent='Re-prefill work: 0 blocks';
 $('n1').innerHTML='Both agents hold a user prompt, assistant turns and tool results. Press the button to remove old tool result <b>A</b>.';}
initP1();
var playing=false;
$('play').addEventListener('click',function(){if(playing)return;playing=true;initP1();
 var ce=$('ce').children,ae=$('ae').children;
 setTimeout(function(){ce[1].classList.add('drop');ae[1].classList.add('drop');
 $('n1').innerHTML='Step 1: A is removed. Left: the text is summarized, so the prefix changes.';},300);
 setTimeout(function(){for(var i=2;i<5;i++)ce[i].classList.add('re');$('cem').style.width='75%';$('cet').textContent='Re-prefill work: 3 blocks (B, C, D recomputed)';
 $('n1').innerHTML='Step 2: <b>Context engineering</b> must re-prefill everything after the edit. <b>AKV</b> only hides A from attention.';},1300);
 setTimeout(function(){for(var i=2;i<5;i++)ce[i].classList.remove('re');
 var n1=blk('E','k-n new');var n2=blk('E','k-n new');$('ce').appendChild(n1);$('ae').appendChild(n2);
 $('aet').textContent='Re-prefill work: 0 blocks (B, C, D reused)';
 $('n1').innerHTML='Step 3: both append new turn E. AKV reused B, C and D as-is, and they still carry what they learned from A.';playing=false;post();},3000);
});
$('reset').addEventListener('click',function(){playing=false;initP1()});
/* P2 */
var st;function initP2(){st={toks:[['A',0],['B',1],['C',2]],dropped:{},next:3,stage:0,drop:{},rep:[]};renderP2();
 $('n2').innerHTML='Start state: tokens A, B, C sit at positions 0, 1, 2. Step through the 3 operations.';$('req').textContent='{"messages": [m0:A, m1:B, m2:C], "drop_message": {}, "reposition": []}';}
function renderP2(mark){var L=$('ops');L.innerHTML='';st.toks.forEach(function(t){var c=t[0]==='D'?'k-n':(t[0]==='B'?'k-a':'k-t');
 var b=blk(t[0],c,'pos '+t[1]);if(st.dropped[t[0]])b.classList.add('drop');if(mark&&mark.indexOf(t[0])>-1)b.classList.add(mark==='D'?'new':'mv');L.appendChild(b)});post();}
initP2();
R.querySelectorAll('[data-op]').forEach(function(b){b.addEventListener('click',function(){var op=b.getAttribute('data-op');
 R.querySelectorAll('[data-op]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
 if(op==='reset2'){initP2();b.classList.remove('on');return}
 if(op==='append'){if(st.toks.some(function(t){return t[0]==='D'})){$('n2').innerHTML='D is already appended. Try <b>Drop B</b>.';return}
 st.toks.push(['D',st.next]);st.next++;renderP2('D');
 $('n2').innerHTML='<b>Append</b>: D is computed against the active cache and takes the next position index.';
 $('req').textContent='{"messages": [m0:A, m1:B, m2:C, m3:D], "drop_message": {}, "reposition": []}';}
 if(op==='drop'){if(!st.toks.some(function(t){return t[0]==='D'})){$('n2').innerHTML='Append D first, then drop B.';b.classList.remove('on');return}st.dropped.B=true;renderP2();
 $('n2').innerHTML='<b>Drop</b>: B leaves future attention. Positions do not change, and the text history keeps B.';
 $('req').textContent='{"messages": [m0..m3], "drop_message": {"3": [1]}, "reposition": []}';}
 if(op==='repos'){if(!st.dropped.B){$('n2').innerHTML='Drop B first, so there is a gap to compact.';return}
 var p=0;st.toks.forEach(function(t){if(!st.dropped[t[0]]){t[1]=p;p++}});st.next=p;
 st.toks=st.toks.filter(function(t){return !st.dropped[t[0]]});st.dropped={};renderP2(['A','C','D']);
 $('n2').innerHTML='<b>Repos</b>: retained keys are re-rotated (RoPE) to positions 0 to '+(p-1)+'. Values are untouched, so nothing is recomputed.';
 $('req').textContent='{"messages": [m0..m3], "drop_message": {"3": [1]}, "reposition": [3]}';}
})});
/* P3 */
var M={'MiniMax-M2.7':{s:[[58.9,35.0,75.2,40.5,52.4],[62.3,36.9,72.0,40.0,52.8],[58.9,40.8,74.4,40.5,53.7]],c:[[5.2,2.4,7.0,5.5,5.0],[5.3,2.7,9.4,5.2,5.7],[4.8,2.6,5.5,4.7,4.4]]},
'GPT-OSS-120B':{s:[[57.5,68.0,40.0,38.5,51.0],[52.7,65.1,36.8,38.5,48.3],[61.9,69.9,43.2,37.5,53.1]],c:[[13.1,5.4,20.0,6.2,11.2],[12.6,6.8,15.8,5.4,10.2],[11.4,4.1,9.7,3.8,7.3]]},
'MiroThinker-1.7-Mini':{s:[[60.0,68.0,7.8,40.5,44.1],[45.7,66.0,4.2,32.5,37.1],[63.5,68.9,7.4,43.5,45.8]],c:[[25.2,9.2,33.6,13.5,20.4],[17.6,11.0,28.4,15.3,18.1],[15.3,9.5,26.3,8.1,14.8]]}};
var B=['BrowseComp-Plus','GAIA-Text','SWE-bench Verified','xbench-DS','Average'];var mSel='GPT-OSS-120B',bSel=4;
var NM=['Standard','Text Eng.','AKV'],CL=['c-s','c-t','c-a'];
Object.keys(M).forEach(function(k){var b=document.createElement('button');b.className='btn'+(k===mSel?' on':'');b.textContent=k;b.onclick=function(){mSel=k;$('models').querySelectorAll('.btn').forEach(function(x){x.classList.toggle('on',x===b)});drawBench()};$('models').appendChild(b)});
B.forEach(function(k,i){var b=document.createElement('button');b.className='btn'+(i===bSel?' on':'');b.textContent=k;b.onclick=function(){bSel=i;$('bench').querySelectorAll('.btn').forEach(function(x){x.classList.toggle('on',x===b)});drawBench()};$('bench').appendChild(b)});
function bars(el,vals,max,fmt){el.innerHTML='';vals.forEach(function(v,i){var r=document.createElement('div');r.className='bar';
 r.innerHTML='<div class="nm">'+NM[i]+'</div><div class="tr"><div class="fl '+CL[i]+'"></div></div><div class="v">'+fmt(v)+'</div>';el.appendChild(r);
 (function(f,w){setTimeout(function(){f.style.width=w+'%'},40)})(r.querySelector('.fl'),Math.max(2,v/max*100));});}
function drawBench(){var d=M[mSel];var s=d.s.map(function(r){return r[bSel]}),c=d.c.map(function(r){return r[bSel]});
 bars($('sc'),s,100,function(v){return v.toFixed(1)});bars($('co'),c,Math.max.apply(null,c)*1.1,function(v){return v.toFixed(1)+'¢'});
 var ds=(s[2]-s[0]).toFixed(1),dc=((c[2]/c[0]-1)*100).toFixed(1);
 $('n3').innerHTML='<b>'+mSel+' · '+B[bSel]+'</b>: AKV vs Standard is '+(ds>=0?'+':'')+ds+' points and '+(dc>0?'+':'')+dc+'% cost. Source: Table 1, self-reported.';post();}
/* P4 */
var C=[8,10,12,14,16],LAT=[[43.57,45.03,43.16,108.86,229.90],[43.57,50.27,52.82,60.67,69.96],[25.93,27.11,27.18,28.49,30.63]],OUT=[[217,254,313,146,138],[228,246,264,267,267],[245,295,339,369,369]];
function drawServe(){var i=+$('c').value;$('cv').textContent=C[i];
 bars($('lat'),LAT.map(function(r){return r[i]}),235,function(v){return v.toFixed(2)+'s'});
 bars($('out'),OUT.map(function(r){return r[i]}),380,function(v){return v});
 var x=(LAT[0][i]/LAT[2][i]).toFixed(2);
 $('n4').innerHTML='At concurrency '+C[i]+', AKV P95 latency is <b>'+x+'x</b> faster than Standard. '+(i>=3?'Above 12, KV pressure forces Standard into re-prefill, so its latency jumps.':'Peak-vs-peak compares AKV at 14 with Standard at 12.');post();}
$('c').addEventListener('input',drawServe);
/* P5 */
R.querySelectorAll('#mtp-akv-lim li').forEach(function(li){li.addEventListener('click',function(){li.classList.toggle('open');post()})});
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</div>
</body></html>"> 
 (function(){var f=document.getElementById("mtp-akv-frame");window.addEventListener("message",function(e){if(e.data&&e.data.mtpAkvHeight&&e.source===f.contentWindow){f.style.height=e.data.mtpAkvHeight+"px";}});})(); 

 How fast is AKV in serving benchmarks? 

 Serving tests ran GPT-OSS-120B on 80 long-context SWE-bench Verified tasks. At each method’s peak setting, AKV delivers 1.18x output throughput and 1.53x input throughput. P95 request latency is 1.51x faster. 

 At concurrency 16, Standard’s P95 latency hits 229.90 seconds versus 30.63 for AKV. KV pressure pushes Standard into repeated re-prefill. Per decode step, full-attention time falls from 7.082 to 2.849 ms. 

 On 100 SWE-bench Verified tasks under a GPU budget, AKV reached about 47% pass rate. Standard reached 40.7% and Text Engineering 32.3%. 

 Can agents tune their own cache policy? 

 MiniMax-M2.7 refined policies on 20 BrowseComp-Plus tasks, then ran 100 held-out tasks. The iteration-6 policy cut cost 17.8% versus Standard at baseline accuracy. The abstract reports 7.1% savings beyond the expert-designed policy. 

 Exposing cache control as a tool also helped accuracy. GPT-OSS-120B rose from 52.1 to 61.0 on a 100-task subset. MiniMax-M2.7’s cost rose, though, from 5.4 to 5.9 cents. 

 AKV vs other KV cache approaches 

 Metrics AKV Threshold summarization SGLang RadixAttention StreamingLLM SnapKV Works on KV cache, agent-directed Text history KV cache, prefix reuse KV cache, fixed window Prompt KV cache What gets dropped Chosen by policy or model tool call History older than a token threshold Nothing, shared prefixes reused Middle tokens; keeps sinks and recent tokens Low-attention prompt positions Re-prefill after reduction No Yes, retained suffix Not applicable No cache refresh needed Not applicable Target workload Multi-turn tool-calling agents Agent harnesses General and agentic serving Streaming dialogue Long prompts Reported headline -27.7% cost, +1.7 pts Baseline in AKV paper Up to 6.4x throughput Up to 22.2x vs sliding-window recompute 3.6x faster generation at 16K Models Qwen, GPT-OSS, MiniMax-M2 Any Broad Llama-2, MPT, Falcon, Pythia Llama, Mistral, Mixtral Fine-tuning needed No No No No No License Apache-2.0 Harness-dependent Apache-2.0 MIT Apache-2.0 

 The main numbers come from each project’s own paper and use different setups. They are not directly comparable. 

 Key Takeaways 

 AKV lets agents drop and reposition KV cache instead of rewriting history. 

 Average cost falls 27.7% and score rises 1.7 points across 3 models. 

 Repos lifts GPT-OSS-120B on BrowseComp-Plus from 55% to 62%. 

 At concurrency 16, P95 latency drops from 229.90 to 30.63 seconds. 

 Support covers only Qwen, GPT-OSS and MiniMax-M2 text models today. 

 Check out the Paper , GitHub Repo and Project Page . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Tsinghua AI Open-Sources AKV, a Cache Engineering Server for LLM Agents on SGLang appeared first on MarkTechPost .
