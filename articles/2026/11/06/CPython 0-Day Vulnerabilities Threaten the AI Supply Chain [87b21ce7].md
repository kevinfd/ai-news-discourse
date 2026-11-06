---
id: "87b21ce74953eaed"
title: "CPython 0-Day Vulnerabilities Threaten the AI Supply Chain"
url: "https://runsybil.com/blog/cpython-0-day-vulnerabilities-threaten-the-ai-supply-chain"
link: "https://runsybil.com/blog/cpython-0-day-vulnerabilities-threaten-the-ai-supply-chain"
source: "RunSybil"
domain: "runsybil.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T00:17:41Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Thrumpwart"]
language: "en"
summary: "Vulnerability in cpython that neither cpython guys, jinja guys, or huggingface has fixed despite being informed."
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 1724
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xoyr90/cpython_0day_vulnerabilities_threaten_the_ai/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# CPython 0-Day Vulnerabilities Threaten the AI Supply Chain

RunSybil · Thrumpwart · 2026-11-06

CPython 0-Day Vulnerabilities Threaten the AI Supply Chain
RunSybil found a zero-day vulnerability in a core component of nearly all Large Language Models (LLMs) that could enable attackers to breach AI hosting platforms at the world’s largest companies. A memory-safety flaw in the CPython interpreter allows attackers to escape a code sandbox and execute code hidden in a specially crafted model.
These hosting platforms are foundational to deploying AI for real-world use, powering a large number of applications for enterprises worldwide. By exploiting this vulnerability, attackers could gain a foothold inside servers responsible for processing millions of user requests. They also could strike directly at the underlying cloud infrastructure hosting those workloads.
We disclosed this vulnerability to the organizations we consider most capable of handling the root cause (CPython, the Pallets Project, and Hugging Face). Unfortunately, we have not found an owner willing to implement a holistic solution for those at risk in the supply chain.
As a result, large portions of real-world CPython deployments remain vulnerable to exploitation, with only difficult mitigation options. We’re continuing to work with the companies affected by this type of bug to try to ensure those who run AI workloads can do so safely.
We discuss success stories and mitigation strategies later in this article.
Escaping a Model’s Chat Template Sandbox for Code Execution
Python sandboxes are ubiquitous in the AI ecosystem, notably in the form of Jinja chat templates, which structure interactions between LLMs and users. Breaking out of the chat template sandbox and executing code represents a supply chain risk that endangers inference providers, library developers, and model users.
The AI supply chain increasingly depends on the assumption that untrusted model components can be safely contained by sandboxes running under CPython. Our research shows how quickly that assumption can collapse, and how a single CPython flaw can become an arbitrary code-execution path across major inference platforms.
This isn’t the first time a flaw in CPython has led to a sandbox escape. In a previous exploitation, we leaned on a documented out-of-bounds read in CPython to do exactly that. In continued research, we used an out-of-bounds read that had not been previously reported. Human effort paired with GPT-5.6 Sol enabled us to discover the exploit in less than a day. Our findings demonstrate that memory-safety flaws in the CPython ecosystem pose a growing risk as AI models get better at discovering them.
The following is a technical explanation of the mechanism we used for exploitation.
Reaching CPython's Type Machinery From a Sandbox
The bug we discovered abuses CPython's handling of generic types to accomplish a breakout. We exploited it using objects that sandboxes make available in every template, even in empty sandbox contexts.
Writing dict[str, int] in Python creates an object referred to as a generic alias. This example describes a dict with string keys and integer values.
Not all parameters are fixed. We can use a TypeVar to leave a slot blank to fill in later:
Fig 1. Parameter substitution in a generic alias
To know where the blanks are, CPython finds them once and caches them in a tuple, __parameters__. CPython doesn't require a blank to be a real TypeVar. Any object with a __typing_subst__ method counts, and CPython calls that method to get the replacement. A second hook, __typing_prepare_subst__, runs before substitution begins. Crafted objects with these hooks therefore let us run our own code partway through substitution, allowing us to modify the cache after its bounds are checked.
What Happens When a Parameter Arrives After Caching?
As an example, we construct an alias with three arguments: first, second, and late. When CPython builds its cache, first and second have __typing_subst__, but late does not. CPython therefore records only the first two as parameters.
While CPython is filling the alias, one of our callbacks adds __typing_subst__ to late. Now all three arguments look like blanks, but the cached parameter list still contains only the original two:
When CPython reaches late, it sees the newly added hook and tries to find the corresponding entry in the old cache. That search returns -1.
The vulnerable code in _Py_subs_parameters assumed this could not happen:
In a normal release build, the assertion is compiled out. Thus, CPython reads argitems[-1] and passes the result to our substitution callback as a Python object pointer.
While an invalid address will generally crash the interpreter, an address pointing to a useful live Python object gives our callback a reference to that object (even when the sandbox never intends to expose it).
Primitive: Turning a Tuple Hash into an Object Pointer
What sits immediately before the argitems array depends on the interpreter distribution and the shape of the substitution input. For brevity (and because CPython has declined our request to backport our patch as a security fix to older supported versions) we will only discuss a single exploitation path affecting CPython >= 3.14.
Starting in 3.14, CPython stores a tuple's cached hash immediately before its element pointers:
This gives us control over the word that CPython will read. Hashing a tuple of integers uses deterministic arithmetic. So for live addresses, we can work backward through that arithmetic and choose two integers whose tuple hash equals a desired address.
The template creates that tuple and uses it as a dictionary key, forcing CPython to calculate and cache its hash. Our preparation callbacks use the same tuple as the final substitution input. When the late parameter triggers the invalid access, CPython reads our chosen address from the hash field and hands the object at that address to our callback.
We used a Jinja macro to receive the object and save it in a namespace. The substitution hook receives the recovered object as a macro argument. At that point, the template has a usable object reference. We converted a manufactured hash into an object the sandbox did not give us.
From a Recovered Object to Code Execution
We needed to leak a useful Python object and targeted a class object first, since disclosing the address of one is trivial. The live str class’s address is exposed in the string representation of ''.maketrans, a public method available inside the sandbox. The template extracts that address and uses the generic alias primitive to recover the class itself.
Recovering the str class lets us traverse attributes that direct template access would reject. We use it to obtain representations that disclose the addresses of the live type and code classes, then repeat the generic alias primitive to recover both objects.
With type available, we applied it to Jinja’s range global. In a sandboxed environment, that global is the Python-defined safe_range wrapper, and its type is the function class. At that point, we had the various constructors needed to build a code object and call it.
Chat Templates Allow Code Execution on Inference Engines
The above escape describes the mechanism we used to achieve code execution in a Jinja ImmutableSandboxEnvironment. Using it, we were able to create a version of Qwen/Qwen2.5-0.5B-Instruct that had a backdoored chat_template.jinja. Upon interacting with this model with an inference serving engine like vLLM, we were able to execute arbitrary code in the serving process.
We shared proof-of-concept exploits with many inference providers supporting bring-your-own-model (BYOM) features. The outcome was a very diverse set of responses and post-exploitation security postures.
For Many, This Won’t be Patched
CPython’s memory-safety bugs break some of the Python ecosystem’s core security invariants. We’ve attempted to coordinate with the organizations that have a major stake in a coherent response to this bug class, but have not yet had luck building support. Ownership is unclear, and resistance to our use of LLMs in research further hindered some of our collaboration with the open-source community.
CPython’s stance on our memory bugs is documented, and was reiterated to us:
CPython does not support sandboxing untrusted Python code as a security boundary, so escapes from such a sandbox are not vulnerabilities in Python and should be reported to the sandbox’s developers instead.
The maintainers of Jinja provided a response at odds with CPython’s guidance:
Report this to cpython. It's problem with cpython, not with Jinja.
Please read and follow our AI policy before continuing: https://palletsprojects.com/contributing/llm-ai
Hugging Face did not respond to our attempts to contact them in the 90-day disclosure window.
vLLM acknowledged our report but has not decided whether it will offer a mitigation.
With our hands somewhat tied, we’ve followed the guidance of the Python Security Response Team. The best way to provide a path forward for CPython users was discreetly submitting a public patch for this memory bug. We will do the same for other bugs we find. However, these bugs will not be backported to all supported versions, leaving large portions of real-world CPython deployments vulnerable to exploitation. With major portions of the AI ecosystem still solidly aligned on Python 3.12, we might not see organic adoption of our memory-safety fixes until late 2028 when it reaches its end-of-life date.
We are continuing to work with the wider community to protect affected users.
Success Stories
We want to highlight both DigitalOcean’s strong remediation and their defense-in-depth strategy around untrusted models. They’ve had the foresight to plan for an attack like ours and guarded their BYOM solutions with multi-tier isolation. During remediation, their team was responsive and worked with us directly to discover how well these mitigating controls contained the attack. We are delighted to report the attack was fully contained and we found no way to move laterally in their infrastructure.
We’d also like to highlight AWS (Amazon Web Services) for their strong handling of our report. They expeditiously worked with us to implement a mitigation in AWS Bedrock for the issue.
Recommendations
As in our previous article, we recommend considering “security fix only” versions of CPython unsafe for any workloads that lean on sandboxed code, template engines, and expression evaluators.
Consider the security guarantees provided by these types of software components to be best-effort. Assume an attacker will be able to achieve arbitrary code execution through them.
This is the second part in a series of publications on sandbox escapes and memory safety in the Python ecosystem. RunSybil is continuing to explore how issues like this affect common software.
Come hack with us: runsybil.com/careers.
Subscribe to RunSybil Blog
A weekly newsletter covering stories, techniques, guides and the latest product innovations coming.
