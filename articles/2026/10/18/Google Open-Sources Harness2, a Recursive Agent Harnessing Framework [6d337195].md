---
id: "6d337195a5a3deef"
title: "Google Open-Sources Harness2, a Recursive Agent Harnessing Framework"
url: "https://marktechpost.com/2026/10/18/google-harness2-recursive-agent-harnessing-framework"
link: "https://marktechpost.com/2026/10/18/google-harness2-recursive-agent-harnessing-framework"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-18T08:15:04Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Google Cloud AI Research has open-sourced Harness² . It is a recursive agent harnessing framework that improves the code and files around a frozen model. For developers, the pitch is simple. Your agent may get better without a better model. \n\n TL;DR \n\n Size: A framework, not a model. 0 parameters trained; 8 editable harness components. Version 0.1.0 . \n\n Runs on: Linux with Python 3.12 or 3.13…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "Language Model", "Large Language Model"]
orgs: ["Google", "Meta"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "summary"
word_count: 1414
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google Open-Sources Harness2, a Recursive Agent Harnessing Framework

MarkTechPost · Asif Razzaq · 2026-10-18

Google Cloud AI Research has open-sourced Harness² . It is a recursive agent harnessing framework that improves the code and files around a frozen model. For developers, the pitch is simple. Your agent may get better without a better model. 

 TL;DR 

 Size: A framework, not a model. 0 parameters trained; 8 editable harness components. Version 0.1.0 . 

 Runs on: Linux with Python 3.12 or 3.13 and uv. Model runs call models through Vertex AI. GPU requirement: Not disclosed. 

 Performance: 1 refinement step improved all 4 model and harness setups on all 3 benchmarks. 

 Best: GLM-5 under OpenCode rose from 64.2 to 75.7 on WorkBuddy-Bench (+11.5 points). 

 Worst: GLM-5 under Codex gained only 1.2 points on JobBench (23.6 to 24.8). 

 What is Harness²? 

 Harness² is a plug-and-play framework from Google Research that refines an agent’s harness during deployment. A harness is everything around the model: prompts, tools, memory, skills and orchestration . Harnessing is the process of optimizing that system. Model weights never change. 

 The target setting is the open world. Tasks arrive unseen, and no verifier says whether an answer is right. The research team argues that most self-improvement methods assume labels or test cases. Harness² is built to work without them. 

 What are the 8 harness components? 

 Harness² exposes 8 editable components , each mounted as a file: 

 System prompt 

 Guardrails 

 Memory 

 Tool guidance 

 Subagents 

 Skills 

 Scripts 

 Plugins (middleware) 

 They cover context construction, the tool interface, delegation and behavior inside the tool loop. The layout extends the 7-file split from earlier Agentic Harness Engineering work by 1 component. 

 How does recursive agent harnessing work? 

 The framework runs two linked levels of recursion : 

 Task-level recursion uses a contrastive Propose, Probe, Compose step. First, the agent runs the task once with the base harness. An editor then proposes 2 candidates. The invariant candidate targets general agent failures such as planning or tool use. The domain candidate targets knowledge and procedures for the current domain. Both candidates run on the same task. The composer compares their trajectories against the reference and keeps only edits backed by observed behavior. 

 Harnessing-level recursion happens after each task. A reflector stores the adopted harness plus an EXPERIENCE.md file of lessons. This library guides future proposals. Each new task still starts from the base harness. 

 The budget k scales the search. Parallel mode probes k invariant and k domain candidates, then makes k compositions. Sequential mode chains k refinement steps. 

 Play</button><button class="btn" id="h2-step">Step →</button><button class="btn" id="h2-reset">↺ Reset</button><div class="prog"><i id="h2-prog"></i></div></div>
<div class="fn">At k=1: 1 reference + 2 probes + 1 final run per task. Parallel mode probes k invariant and k domain candidates; sequential mode chains k steps.</div>
</div>

<div class="pn" id="h2-p2">
<div class="cg" id="h2-cg"></div>
<div class="note" id="h2-cnote" style="border-left-color:#4285F4">Click a component to see its runtime role.</div>
<div class="lg"><span style="--c:#4285F4">Context construction</span><span style="--c:#EA4335">Tool interface</span><span style="--c:#FBBC04">Orchestration</span><span style="--c:#34A853">Middleware</span></div>
</div>

<div class="pn" id="h2-p3">
<div class="sel" id="h2-sel"></div>
<div class="bm" id="h2-bm"></div>
<div class="fn">Single improvement step (k=1). Means over 3 runs. LAB = Partial pass rate (%). Source: Harness<sup>2</sup> paper, Tables 1 and 2.</div>
</div>

<div class="pn" id="h2-p4">
<div class="sel" id="h2-sel2"></div>
<div class="bx rk" id="h2-rk"></div>
<div class="fn">Gemini 3.5 Flash executor. Bar axis starts at 50. Meta-Harness is optimized offline on separate training tasks. Scores as measured in the Harness<sup>2</sup> paper.</div>
</div>

<div class="ft"><span>Sources: arXiv 2610.14224 · github.com/google-research/harness2</span><a href="https://www.marktechpost.com" target="_blank" rel="noopener">© Marktechpost</a></div>

<script>
(function(){
var R=document.getElementById('mtp-h2x');
function $(s){return R.querySelector(s)}function $$(s){return R.querySelectorAll(s)}
function sz(){try{parent.postMessage({mtpH2xHeight:R.offsetHeight+40},'*')}catch(e){}}
$$('.tab').forEach(function(t){t.onclick=function(){$$('.tab').forEach(function(x){x.classList.remove('on')});$$('.pn').forEach(function(x){x.classList.remove('on')});t.classList.add('on');$('#h2-'+t.dataset.t).classList.add('on');if(t.dataset.t==='p3')drawB();if(t.dataset.t==='p4')drawR();setTimeout(sz,50)}});
/* pipeline */
var nd=$$('.nd'),i=-1,tm=null;
var notes=["<b>Reference.</b> The frozen model runs the task with the base harness H0. This shows how the harness behaves, not whether the answer is correct.",
"<b>Propose.</b> An editor drafts 2 candidates: an <b>invariant</b> one for general agent failures (planning, tool use) and a <b>domain</b> one for task knowledge and procedures.",
"<b>Probe.</b> Each candidate runs on the same task. Comparing trajectories against the reference gives a behavioral contrast. No ground-truth labels needed.",
"<b>Compose.</b> The composer reads all evidence and diffs. It may merge, revise, adopt 1 candidate, or keep the current harness.",
"<b>Execute.</b> The composed harness runs and returns the final deliverable.",
"<b>Reflect.</b> The full improvement record is reviewed. Lessons are kept only if execution contrasts support them.",
"<b>Update.</b> The adopted harness and an <code>EXPERIENCE.md</code> of lessons join the improvement library.",
"<b>Next task.</b> The executor resets to H0, but the library now guides proposals and composition. Removing it cut WorkBuddy from 77.5 to 74.4."];
function show(k){nd.forEach(function(n,j){n.classList.toggle('lit',j<=k)});$('#h2-note').innerHTML=k<0?"Press <b>Play</b> or <b>Step</b> to walk through 1 Harness<sup>2</sup> improvement step.":notes[k];$('#h2-prog').style.width=((k+1)/nd.length*100)+'%';sz()}
function step(){i=(i+1)%nd.length;show(i)}
$('#h2-step').onclick=function(){stop();step()};
$('#h2-reset').onclick=function(){stop();i=-1;show(-1)};
function stop(){if(tm){clearInterval(tm);tm=null;$('#h2-play').textContent=' Play'}}
$('#h2-play').onclick=function(){if(tm){stop();return}if(i>=nd.length-1)i=-1;step();tm=setInterval(function(){if(i>=nd.length-1){stop();return}step()},1900);this.textContent='❚❚ Pause'};
/* components */
var C=[["System prompt","Context construction","#4285F4","Persona and top-level procedure followed on every call."],
["Guardrails","Context construction","#4285F4","Process rules, e.g. verify outputs before finishing."],
["Memory","Context construction","#4285F4","Persistent context made available to the agent."],
["Tool guidance","Tool interface","#EA4335","How to use specific tools and handle formats precisely."],
["Subagents","Orchestration","#FBBC04","Delegated roles with their own instructions."],
["Skills","Context construction","#4285F4","Reusable domain procedures, e.g. a reconciliation skill."],
["Scripts","Tool interface","#EA4335","Executable helpers, e.g. a script that reopens and checks files."],
["Plugins","Middleware control","#34A853","Middleware that shapes behavior inside the tool loop."]];
var cg=$('#h2-cg');C.forEach(function(c,k){var b=document.createElement('button');b.className='cp';b.style.setProperty('--c',c[2]);b.innerHTML='<em>C'+(k+1)+' · '+c[1]+'</em><b>'+c[0]+'</b>';b.onclick=function(){$$('.cp').forEach(function(x){x.classList.remove('on')});b.classList.add('on');var n=$('#h2-cnote');n.style.borderLeftColor=c[2];n.innerHTML='<b>'+c[0]+'</b> ('+c[1].toLowerCase()+'): '+c[3]+' Each component is a file the editor can rewrite.';sz()};cg.appendChild(b)});
/* benchmarks */
var D={"Gemini 3.5 Flash · OpenCode":[[72.4,77.5],[31.5,36.0],[79.9,81.9]],"Gemini 3.5 Flash · Codex":[[74.5,77.5],[33.9,35.3],[71.6,75.6]],"GLM-5 · OpenCode":[[64.2,75.7],[20.6,24.2],[59.6,71.4]],"GLM-5 · Codex":[[64.4,75.3],[23.6,24.8],[58.1,65.9]]};
var BN=["WorkBuddy-Bench (avg)","JobBench","LAB Partial (%)"],cur="GLM-5 · OpenCode";
var sel=$('#h2-sel');Object.keys(D).forEach(function(k){var b=document.createElement('button');b.className='chip'+(k===cur?' on':'');b.textContent=k;b.onclick=function(){cur=k;$$('#h2-sel .chip').forEach(function(x){x.classList.remove('on')});b.classList.add('on');drawB()};sel.appendChild(b)});
function drawB(){var bm=$('#h2-bm');bm.innerHTML='';D[cur].forEach(function(v,k){var d=(v[1]-v[0]).toFixed(1);var x=document.createElement('div');x.className='bx';x.innerHTML='<h4>'+BN[k]+'</h4><div class="row"><span>Base</span><div class="tr"><i style="background:#5f6368" data-w="'+v[0]+'"></i></div><b>'+v[0].toFixed(1)+'</b></div><div class="row"><span>Harness²</span><div class="tr"><i style="background:linear-gradient(90deg,#4285F4,#34A853)" data-w="'+v[1]+'"></i></div><b>'+v[1].toFixed(1)+'</b></div><div class="dl">+'+d+(k===2?' pp':' pts')+'</div>';bm.appendChild(x)});
requestAnimationFrame(function(){setTimeout(function(){$$('#h2-bm .tr i').forEach(function(e){e.style.width=e.dataset.w+'%'})},30)});sz()}
/* baselines */
var RK={"WorkBuddy avg · OpenCode":[["Base harness",72.4],["ReasoningBank",73.4],["Harness Scaling",75.3],["Meta-Harness",76.4],["Harness² k=1",77.5],["Harness² k=5",80.8]],
"JobBench · OpenCode":[["Base harness",31.5],["ReasoningBank",30.8],["Harness Scaling",32.9],["Meta-Harness",35.8],["Harness² k=1",36.0]],
"LAB Partial · Codex":[["Base harness",71.6],["ReasoningBank",74.8],["Harness Scaling",67.9],["Meta-Harness",76.5],["Harness² k=1",75.6]]};
var rc="WorkBuddy avg · OpenCode",s2=$('#h2-sel2');
Object.keys(RK).forEach(function(k){var b=document.createElement('button');b.className='chip'+(k===rc?' on':'');b.textContent=k;b.onclick=function(){rc=k;$$('#h2-sel2 .chip').forEach(function(x){x.classList.remove('on')});b.classList.add('on');drawR()};s2.appendChild(b)});
function drawR(){var rk=$('#h2-rk');rk.innerHTML='';var mx=Math.max.apply(null,RK[rc].map(function(r){return r[1]}));
RK[rc].forEach(function(r){var h=r[0].indexOf('Harness²')===0;var c=h?'linear-gradient(90deg,#4285F4,#34A853)':(r[1]===mx?'#FBBC04':'#5f6368');var x=document.createElement('div');x.className='row';x.innerHTML='<span'+(h?' style="color:#e8eaed;font-weight:700"':'')+'>'+r[0]+'</span><div class="tr"><i style="background:'+c+'" data-w="'+((r[1]-50)/40*100)+'"></i></div><b>'+r[1].toFixed(1)+'</b>';rk.appendChild(x)});
requestAnimationFrame(function(){setTimeout(function(){$$('#h2-rk .tr i').forEach(function(e){e.style.width=e.dataset.w+'%'})},30)});sz()}
show(-1);window.addEventListener('load',sz);window.addEventListener('resize',sz);setTimeout(sz,300);
})();
</script>
</div>
</body></html>"> 
 
(function(){var f=document.getElementById('mtp-h2x-frame');window.addEventListener('message',function(e){if(e.source===f.contentWindow&&e.data&&e.data.mtpH2xHeight){f.style.height=e.data.mtpH2xHeight+'px';}});})();

 How does Harness² perform on benchmarks? 

 The research team tested 3 professional benchmarks: WorkBuddy-Bench , JobBench and Harvey’s LAB . Executors were Gemini 3.5 Flash and GLM-5 under OpenCode and Codex. The default editor was Claude Opus 4.8. Results are means over 3 runs. 

 Setup (single step, k=1) WorkBuddy Avg JobBench LAB Partial Gemini 3.5 Flash, OpenCode 72.4 → 77.5 31.5 → 36.0 79.9 → 81.9 Gemini 3.5 Flash, Codex 74.5 → 77.5 33.9 → 35.3 71.6 → 75.6 GLM-5, OpenCode 64.2 → 75.7 20.6 → 24.2 59.6 → 71.4 GLM-5, Codex 64.4 → 75.3 23.6 → 24.8 58.1 → 65.9 

 Source: Harness² paper, Tables 1 and 2 . 

 Weaker executors gained more. After 1 step, GLM-5 beat base Gemini 3.5 Flash on WorkBuddy-Bench. Parallel recursion at k=5 lifted Gemini under OpenCode to 80.8 on WorkBuddy . On WorkBuddy-Bench, 3 of 4 setups also used fewer steps per task. Gemini under OpenCode fell from 25.4 to 21.9. 

 How does it compare with other harness methods? 

 Feature Harness² Meta-Harness ReasoningBank Harness Scaling Developers Google Cloud AI Research, Northwestern Stanford IRIS Lab and co-authors Google Research and co-authors Wang et al. What changes Full 8-component harness, per task Harness code, searched offline Retrieved memory; harness fixed Harness, revised per instance Needs training split No Yes No No Learns across tasks Yes (library + lessons) Deploys 1 best harness Yes (memory) No Code license Apache-2.0 MIT Not disclosed Not disclosed WorkBuddy Avg, Gemini/OpenCode* 77.5 (80.8 at k=5) 76.4 73.4 75.3 JobBench, Gemini/OpenCode* 36.0 35.8 30.8 32.9 LAB Partial, Gemini/Codex* 75.6 76.5 74.8 67.9 

 *Scores as measured in the Harness² paper ; the other methods did not report these benchmarks themselves. 

 How do you install and run Harness²? 

 The README targets Linux, Python 3.12 and uv. A local demo runs both recursion modes without model credentials: 

 Copy Code Copied Use a different Browser uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -e '.[render]'
harness2-demo --output runs/demo --k 2 

 Model-backed runs need Node.js 20+, the Google Cloud CLI and a Vertex AI project. LAB needs Pandoc and Poppler. WorkBuddy-Bench needs Docker. Executors are OpenCode by default, or Codex with --substrate cx . 

 Key Takeaways 

 Harness² rewrites an agent’s harness at test time; weights stay frozen. 

 1 step lifted GLM-5 by 11.5 points on WorkBuddy-Bench. 

 Propose, Probe, Compose replaces ground-truth labels with behavioral contrasts. 

 A lessons library carries improvements to future tasks. 

 Expect extra runs per task, and sandbox it yourself. 

 Check out the Paper , GitHub Repo , Paper and Project Page . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Google Open-Sources Harness2, a Recursive Agent Harnessing Framework appeared first on MarkTechPost .
