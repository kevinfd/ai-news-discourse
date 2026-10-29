---
id: "7f690324c9130732"
title: "Infini-AI-Lab Releases Hermit, an Open-Source Harness Adapter Framework for AI Agents"
url: "https://marktechpost.com/2026/10/29/infini-ai-lab-hermit-harness-adapter-framework"
link: "https://marktechpost.com/2026/10/29/infini-ai-lab-hermit-harness-adapter-framework"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T08:24:52Z"
published_date: "2026-10-29"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Infini-AI-Lab has released Hermit , an open-source harness adapter framework for AI agents. Hermit is a framework from Infini-AI-Lab that trains an external ‘harness adapter’ while the agent’s model and harness stay frozen. The first release, v0.1.0 , shipped on October 25, 2026. CMU postdoc Haizhong Zheng announced it on X on October 27. For developers, the pitch is simple: adapt Codex or…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "New Releases", "Open Source", "Staff"]
orgs: ["Anthropic", "OpenAI", "DeepSeek"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "summary"
word_count: 1335
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Infini-AI-Lab Releases Hermit, an Open-Source Harness Adapter Framework for AI Agents

MarkTechPost · Asif Razzaq · 2026-10-29

Infini-AI-Lab has released Hermit , an open-source harness adapter framework for AI agents. Hermit is a framework from Infini-AI-Lab that trains an external ‘harness adapter’ while the agent’s model and harness stay frozen. The first release, v0.1.0 , shipped on October 25, 2026. CMU postdoc Haizhong Zheng announced it on X on October 27. For developers, the pitch is simple: adapt Codex or Claude Code agents to new tasks without fine-tuning or forking the harness. 

 TL;DR 

 Footprint: A Python framework. No parameters of its own. Apache-2.0, pip install hermit-harness . 

 Runs on: The offline Quick Start needs no GPU, model account or dataset. Real runs use any API backend or a local vLLM, SGLang or Ollama server. 

 Performance: Reported gains over no-adapter baselines on OfficeQA, CL-Bench and ServeLearnBench, all with GLM 5.3 Flash. 

 Best: MWM adapter hits 0.795 accuracy on CL-Bench database exploration, vs 0.580 for the in-context baseline. 

 Worst: The prompt-only adapter scores 0.470 on the same venue, below that 0.580 baseline. 

 Bottom line: Best: one training loop for 5 harness evolution methods. Worst: most results are single runs, self-reported. 

 What is a harness adapter? 

 A harness adapter is a trainable external harness. It works like a plugin with training support built in. A model adapter, such as LoRA, adapts a model. A harness adapter adapts an existing agent instead. 

 The adapter can hold instructions, skills, memory, tools, executable code and agent coordination logic. It can even be a whole repository. Its specification says which parts are learnable and how updates get checked. The base model and harness never change. 

 The team gives 3 reasons for this design. Many harnesses are closed-source. Editing open ones can break carefully tuned component interactions. And a learned adapter can move between compatible models and harnesses. 

 How does Hermit train an adapter? 

 Hermit uses an RL-style training loop . A Trainer runs a batch of tasks through the acting agent with the current adapter. A judge scores the outputs. An Evolver reads the trajectories and feedback, then proposes a new adapter. The Trainer checks it against the template and commits it as the next version. 

 Every adapter version lives in a git tree. You can inspect, roll back or ship any version. Learner programs can run sandboxed, which requires Linux with bubblewrap. 

 Five evolution methods ship today: GEPA , SkillOpt , MetaWorld Model (MWM), Harness² and Continual Harness . ACE and ReHarness are listed as coming soon. You can also write your own Evolver. 

 Play</button>
 <button class="btn gh" id="mhx-next">Next step</button>
 <button class="btn gh" id="mhx-reset">Reset</button>
 <span class="ver">Adapter version <b id="mhx-v">V0</b></span>
 </div>
 <p class="note">Built-in Evolvers: GEPA, SkillOpt, MetaWorld Model (MWM), Harness², Continual Harness. ACE and ReHarness are listed as coming soon.</p>
 </div>

 <div class="pn" data-i="2">
 <p class="lead">Self-reported results, all with <b>GLM 5.3 Flash</b> as the acting model. Pick a benchmark.</p>
 <div class="seg">
 <button class="tab on" data-b="0">OfficeQA</button>
 <button class="tab" data-b="1">CL-Bench database</button>
 <button class="tab" data-b="2">ServeLearnBench (H)</button>
 </div>
 <div class="bars" id="mhx-bars"></div>
 <p class="note" id="mhx-bnote"></p>
 </div>

 <div class="pn" data-i="3">
 <p class="lead">Train once, then <b>deploy</b> the adapter into an agent workspace or export it as a native plugin.</p>
<div class="term"><span class="p">$</span> pip install hermit-harness
<span class="p">$</span> hermit train --config run.yaml
<span class="p">$</span> hermit eval --config run.yaml --adapter final
<span class="p">$</span> hermit deploy --adapter DIR --workspace WS --host codex
<span class="p">$</span> hermit convert --adapter DIR --output OUT --target claude-code
<span class="c"># other convert targets: codex, pi, hermes</span></div>
 <div class="hosts">
 <span class="chip" data-d="Deploy target and plugin export target.">Codex</span>
 <span class="chip" data-d="Deploy target and plugin export target.">Claude Code</span>
 <span class="chip" data-d="Deploy target and plugin export target.">Pi</span>
 <span class="chip" data-d="Plugin export target.">Hermes</span>
 </div>
 <div class="info" id="mhx-dinfo">Backends by reference: Fireworks, OpenAI, Anthropic, DeepSeek, vLLM, SGLang, Ollama. The offline Quick Start needs no GPU, model account or dataset.</div>
 </div>

 <div class="ft"><span>Source: github.com/Infini-AI-Lab/hermit · self-reported</span><span class="mtp">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-hermit-x');if(!R)return;
function ping(){try{var h=R.offsetHeight+40;parent.postMessage({mtpEmbedHeight:h,height:h,frameHeight:h},'*');}catch(e){}}
var tabs=R.querySelectorAll('.tabs .tab'),pns=R.querySelectorAll('.pn');
tabs.forEach(function(t){t.addEventListener('click',function(){var p=+t.getAttribute('data-p');tabs.forEach(function(x){x.classList.remove('on')});t.classList.add('on');pns.forEach(function(x){x.classList.toggle('on',+x.getAttribute('data-i')===p)});if(p===2)drawBars(cur);setTimeout(ping,60);});});
function wire(sel,out){R.querySelectorAll(sel).forEach(function(c){c.addEventListener('click',function(){R.querySelectorAll(sel).forEach(function(x){x.classList.remove('sel')});c.classList.add('sel');document.getElementById(out).textContent=c.textContent+': '+c.getAttribute('data-d');ping();});});}
wire('.dg .chip','mhx-info');wire('.hosts .chip','mhx-dinfo');
var steps=R.querySelectorAll('.st'),si=-1,ver=0,timer=null;
var msg=['The Trainer runs a batch of tasks through the acting agent with the current adapter.','Your judge scores each output and writes feedback.','An Evolver reads trajectories and feedback, then proposes a new adapter.','The Trainer checks the proposal against the adapter template.','The checked update is committed as the next adapter version.'];
function go(i){si=i;steps.forEach(function(s,k){s.classList.toggle('on',k===i)});document.getElementById('mhx-step').textContent=msg[i];if(i===4){ver++;document.getElementById('mhx-v').textContent='V'+ver;}}
function next(){go((si+1)%5)}
document.getElementById('mhx-next').onclick=function(){stop();next()};
document.getElementById('mhx-play').onclick=function(){if(timer){stop();return}this.textContent='❚❚ Pause';next();timer=setInterval(next,1400)};
function stop(){clearInterval(timer);timer=null;document.getElementById('mhx-play').textContent=' Play'}
document.getElementById('mhx-reset').onclick=function(){stop();si=-1;ver=0;steps.forEach(function(s){s.classList.remove('on')});document.getElementById('mhx-v').textContent='V0';document.getElementById('mhx-step').textContent='Press Play to step through one training iteration.'};
var B=[
{max:1,fmt:3,rows:[['No adapter',.541],['Initial skill',.576],['GEPA',.580],['SkillOpt',.600],['Continual Harness',.634,1],['Harness²',.651,1]],n:'Accuracy on 172 test questions. GEPA and SkillOpt are means of 4 trainings, tested frozen. Continual Harness and Harness² learn while streaming the test set once. Standard error about 3.7 points.'},
{max:1,fmt:3,rows:[['Stateless baseline',.400],['Prompt-only',.470],['ICL baseline',.580],['MWM',.795,1]],n:'Accuracy on a 40-question stream over an undocumented, drifting SQLite database. Mean of 5 stream orders.'},
{max:100,fmt:1,rows:[['Blind',4.5],['Prompt-only',18.8],['SkillOpt (leaderboard)',22.0],['CH (leaderboard)',28.7],['MWM',45.3,1],['Oracle (policy given)',89.2]],n:'retail_l3: 624 serving requests, 537 held-out tests. H = score on tests that need the hidden policy. One run each.'}];
var cur=0;
function drawBars(k){cur=k;var d=B[k],el=document.getElementById('mhx-bars');el.innerHTML='';d.rows.forEach(function(r){var row=document.createElement('div');row.className='row'+(r[2]?' hl':'');row.innerHTML='<span class="lb">'+r[0]+'</span><span class="tr"><span class="fl" style="display:block"></span></span><span class="v">'+r[1].toFixed(d.fmt)+'</span>';el.appendChild(row);var f=row.querySelector('.fl');setTimeout(function(){f.style.width=(r[1]/d.max*100)+'%'},40);});document.getElementById('mhx-bnote').textContent=d.n;setTimeout(ping,60);}
R.querySelectorAll('.seg .tab').forEach(function(b){b.addEventListener('click',function(){R.querySelectorAll('.seg .tab').forEach(function(x){x.classList.remove('on')});b.classList.add('on');drawBars(+b.getAttribute('data-b'));});});
drawBars(0);
window.addEventListener('load',ping);window.addEventListener('resize',ping);setTimeout(ping,300);
})();
</script>
</body></html>"> 
 
 (function(){var f=document.getElementById("mtp-hermit-frame");window.addEventListener("message",function(e){if(!f||e.source!==f.contentWindow)return;var h=e.data&&e.data.mtpEmbedHeight;if(h&&h>100)f.style.height=h+"px";});})(); 

 What are the benchmark results? 

 All runs below use GLM 5.3 Flash as the acting model. The numbers come from the repo’s example READMEs and are self-reported. 

 OfficeQA ( recipe ) asks 172 test questions about U.S. Treasury Bulletins, scored by exact match: 

 Method Accuracy No adapter 0.541 Initial skill 0.576 GEPA 0.580 SkillOpt 0.600 Continual Harness 0.634 Harness² 0.651 

 GEPA and SkillOpt train on 50 questions and are tested frozen. Continual Harness and Harness² instead learn while streaming the test set once. The team reports a +7.6 point gain for Harness² over its reference run, with a 95% interval of +1.7 to +13.4. 

 CL-Bench ( database , poker ) tests stateful environments from the Continual Learning Bench paper . On database exploration, MWM reaches 0.795 accuracy. The benchmark’s in-context baseline scores 0.580. On exploitable poker, MWM wins 3.08 big blinds per hand, vs 2.51 for in-context learning. 

 ServeLearnBench ( recipe ) streams 624 retail support requests under a hidden, shifting policy. MWM scores 45.3 on hidden-policy tests. The best learning method on the leaderboard, CH, scores 28.7. An oracle given the policy scores 89.2. 

 How does Hermit compare with other agent optimizers? 

 Feature Hermit GEPA ACE Agent Lightning What it trains External harness adapter Any text parameter (prompts, code) Context playbook Prompts and model weights Changes model weights No No Not disclosed Yes, via RL or SFT Methods 5 built in, custom Evolvers Reflective evolution, Pareto selection Generator, Reflector, Curator RL, prompt optimization, SFT Deploy targets Codex, Claude Code, Pi; plugin export DSPy ( dspy.GEPA ) Not disclosed LangChain, OpenAI Agents SDK, AutoGen, CrewAI and more License Apache-2.0 MIT Apache-2.0 MIT Key result 0.795 on CL-Bench database (self-reported) AIME 2025: 46.6% to 56.6% (GPT-4.1 Mini) +10.6% on AppWorld Not disclosed 

 How do you install and deploy it? 

 Install from PyPI with pip install hermit-harness , or clone the repo for examples. The CLI covers check , train , eval , deploy and convert . Models are referenced as <backend>/<model id> . Supported backends include Fireworks, OpenAI, Anthropic, DeepSeek, vLLM, SGLang and Ollama. 

 hermit deploy writes a workspace for Codex, Claude Code or Pi. hermit convert exports a trained adapter as a native plugin for Codex, Claude Code, Pi or Hermes. A finished Lean collaboration adapter coordinates 5 Codex agents proving one theorem together. 

 Key Takeaways 

 Hermit trains an external adapter; model and harness stay frozen. 

 5 methods ship: GEPA, SkillOpt, MWM, Harness², Continual Harness. 

 MWM reaches 0.795 on CL-Bench database vs 0.580 in-context. 

 Adapters deploy to Codex, Claude Code and Pi, or export as plugins. 

 Results are self-reported, mostly single runs, with GLM 5.3 Flash. 

 Check out the GitHub repo , project page and docs . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Infini-AI-Lab Releases Hermit, an Open-Source Harness Adapter Framework for AI Agents appeared first on MarkTechPost .
