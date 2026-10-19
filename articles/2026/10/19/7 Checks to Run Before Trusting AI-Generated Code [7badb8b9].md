---
id: "7badb8b91e4ff93c"
title: "7 Checks to Run Before Trusting AI-Generated Code"
url: "https://kdnuggets.com/7-checks-to-run-before-trusting-ai-generated-code"
link: "https://kdnuggets.com/7-checks-to-run-before-trusting-ai-generated-code"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-10-19T12:00:43Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Kanwal Mehreen"]
language: "en"
summary: "AI makes writing code cheap. Verifying it is still your job."
tags: []
orgs: ["OpenAI", "Anthropic", "Microsoft"]
topics: ["agents & coding", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1759
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/kdn-7-checks-to-run-before-trusting-ai-generated-code-feature.png"
discussion_url: null
score: null
comments: null
community: null
---

# 7 Checks to Run Before Trusting AI-Generated Code

KDnuggets · Kanwal Mehreen · 2026-10-19

7 Checks to Run Before Trusting AI-Generated Code
AI makes writing code cheap. Verifying it is still your job.
AI coding assistants can generate a large amount of working code in a few minutes. This increases productivity but it also makes them dangerous. Bad AI-generated code does not necessarily look bad. It may compile, pass tests, and use clean variable names while still making the wrong assumption about an API, authorization rule, edge case, or dependency. GitHub warns that AI-generated code can be semantically incorrect and recommends carefully reviewing and testing it before merging. So instead of asking "Does this AI-generated code look good?", run these 7 checks.
Does this AI-generated code look good?
1. Inspecting the Diff Before Running Anything
Your first check should not be ChatGPT, Copilot, Claude Code, or another model.
It should be Git.
When coding agents are given access to an entire repository, they sometimes modify more than the task requires. A small bug fix can unexpectedly become a refactor, dependency update, configuration change, and formatting sweep.
Start with:
git status
git diff --stat
git diff
git diff --stat gives you an immediate picture of the scope.
Suppose you asked the agent:
Add validation to the email signup endpoint.
You expected changes in two files. But the diff says:
12 files changed, 437 insertions(+), 186 deletions(-)
Stop there.
Before examining whether the code works, ask why the task required hundreds of changed lines.
While reviewing the diff, look specifically for:
- files unrelated to the task
- deleted tests, disabled validation, and new configuration values
- permission changes
- changes to dependency files
- large refactors hidden inside a feature
- duplicated helper functions and error handling that ignores failures
The goal is simple: make sure the AI solved the task you gave it rather than a larger task it invented.
2. Making the Compiler, Linter, and Type Checker Judge It
Humans are terrible compilers.
Do not spend ten minutes visually checking syntax that a deterministic tool can check in seconds.
For a Python project, your first automated checks might look like:
python -m compileall .
ruff check .
mypy .
For JavaScript or TypeScript:
npm run lint
npx tsc --noEmit
npm run build
Static type checking is particularly useful with AI-generated code because models can confidently connect values that happen to look compatible but are not.
For example:
def get_user_id(user: dict[str, str]) -> int:
    return user["id"]
The code looks harmless. But the declared dictionary contains strings while the function claims to return an integer. A type checker can flag this immediately.
3. Verifying Every New Dependency and API
This deserves special attention because it is an AI-specific failure mode.
Models sometimes invent package names, and those names can look completely plausible.
For example, an AI might suggest:
pip install fastapi-jwt-auth-plus
Do not assume a dependency exists simply because the name sounds reasonable.
A 2025 study analyzed 576,000 large language model (LLM)-generated code samples and documented package hallucinations across Python and JavaScript — 5.2% for commercial models and 21.7% for open-source models. This is important because hallucinated package names create an opportunity known as slopsquatting: someone can register a package under a commonly hallucinated name and potentially trick developers into installing it. So whenever AI adds a dependency, verify it independently.
For Python:
pip index versions package-name
For npm:
npm view package-name
Then check:
- Does the package actually exist?
- Is this the official package? Who maintains it? When was it last updated?
- Does the project genuinely need it?
- Does the version match the documentation the code appears to use?
- Did the lockfile suddenly change substantially?
- Does it introduce known vulnerabilities?
Do the same for APIs.
If the AI writes:
client.responses.stream_async(...)
do not assume the method exists because it resembles the rest of an SDK.
Open the current official documentation and confirm:
class → method → parameters → return type → supported version
This is especially important for rapidly changing AI SDKs, cloud APIs, and JavaScript frameworks. Every newly introduced package and every unfamiliar external API should be traceable to an authoritative registry or official documentation.
4. Testing the Behavior, Not the Implementation
Now run the existing test suite.
For example:
pytest -q
But a green test suite is only the beginning. The more important question is:
What important case is not being tested?
Suppose the AI generated:
def apply_discount(price, discount):
    return price - (price * discount / 100)
And generated this test:
def test_discount():
    assert apply_discount(100, 10) == 90
Great.
But what about:
discount = 0
discount = 100
discount = -10
discount = 150
price = 0
price = None
price = "100"
AI frequently generates the happy path because the happy path is also what appears most prominently in examples and documentation. For every generated feature, test at least four categories:
Normal input
Boundary input
Invalid input
Failure condition
For an API endpoint, that might mean:
Valid request
Missing field
Malformed field
Unauthorized request
Database/service failure
Also make sure the AI did not "fix" a failing test by deleting it or weakening the assertion. For critical functions, consider writing the test before showing the implementation to another model. The feature should survive tests for what happens when the user, network, database, file system, and input data do something unexpected.
5. Attacking the Security Boundaries
Functional correctness and security are different tests. This function may work:
query = f"SELECT * FROM users WHERE email = '{email}'"
cursor.execute(query)
It may even pass all your unit tests.
It is still unsafe.
Whenever AI-generated code touches user-controlled input, authentication, databases, files, shell commands, or external URLs, switch from a functional mindset to an adversarial one.
Search the patch for areas involving:
SQL queries
authentication
authorization
file paths
subprocess execution
HTML rendering
deserialization
redirects
HTTP requests
tokens
passwords
API keys
Ask questions like:
Can the user control this string?
Can they access somebody else's resource?
Can this path escape its intended directory?
Can this query be parameterized?
Can this command execute arbitrary input?
What happens if this URL points to an internal service?
Are permissions checked server-side?
Then run static security tooling where appropriate.
One general-purpose option is Semgrep:
semgrep scan --config auto
Semgrep documents this configuration for automatically selecting relevant scanning rules.
Python projects can also use Bandit:
bandit -r .
Bandit analyzes Python's abstract syntax tree for common security problems.
Repositories using GitHub can enable CodeQL code scanning, which can analyze supported languages on pull requests and protected branches.
One more check is important: Search for secrets. Look for:
API keys
database passwords
OAuth tokens
private keys
cloud credentials
connection strings
GitHub's secret scanning exists specifically to detect credentials accidentally committed into repositories. An AI assistant should never turn this:
api_key = os.environ["API_KEY"]
into:
api_key = "sk-..."
just because it saw a credential in its environment or context. No untrusted input should cross a security boundary without you understanding exactly how it is validated, escaped, authorized, or isolated.
6. Following the Failure Path
AI-generated code often looks strong when everything works. So deliberately examine what happens when everything does not work.
Consider this generated code:
try:
    response = requests.get(url)
    return response.json()
except Exception:
    return {}
It appears robust because it contains error handling. But in reality, it can hide:
- timeouts
- connection failures
- authentication errors
- invalid JSON
- HTTP 500 errors
- programming bugs
And every one of them becomes:
{}
This makes debugging considerably harder. Look for broad patterns such as:
except Exception:
    passcatch (e) {
  console.log(e);
}
or:
return None
being used for multiple unrelated failures.
Also inspect:
Retries
Does the AI retry forever?
while True:
    try:
        ...
    except Exception:
        continue
Timeouts
Does a network request have one?
requests.get(url, timeout=10)
Transactions
If operation three fails, are operations one and two rolled back?
Async Code
Are tasks awaited correctly?
Shared State
Could two requests modify the same data simultaneously?
Cleanup
Are database connections, temporary files, sockets, and locks released after an error?
A useful test is to deliberately break each external dependency. For example:
Turn off the database.
Return HTTP 500 from the API.
Provide corrupt JSON.
Remove file permissions.
Force a request timeout.
Submit the same request twice simultaneously.
Observe what your application does. The question is not:
Does it fail?
It is:
Does it fail predictably, safely, and visibly?
7. Asking Whether the Code Should Exist at All
 
The final check is the one developers often skip. Suppose the AI generated this:
def transform_items(items):
    output = []
    for item in items:
        transformed_item = transform_single_item(item)
        output.append(transformed_item)
    return output
And:
def transform_single_item(item):
    return item["name"]
The whole thing could simply be:
[item["name"] for item in items]
This is not about shorter code. AI coding agents can generate unnecessary:
- wrappers, classes, and helper functions
- configuration layers and abstractions
- comments, fallback logic, and duplicated utilities
Before merging, ask:
Did this feature introduce a new abstraction?
Could an existing function already do this?
Did we add a library for something available in the standard library?
Did the AI duplicate an existing helper?
Can this implementation be reduced by 30% without losing clarity?
Would I understand this code six months from now?
But do not optimize for the smallest possible line count.
Optimize for the smallest amount of new complexity necessary to solve the problem.
This is also where human understanding becomes the final gate.
Take the most important generated function and explain it without the AI.
If you cannot explain:
what goes in
what comes out
what state changes
what can fail
why this approach was chosen
then you are not ready to own that code in production.
Final Thoughts
AI coding tools dramatically reduce the cost of producing code. They do not reduce the cost of proving that code is correct. The wrong response is to distrust every line an AI writes.
The best AI coding workflow is therefore not generate and trust.
It is generate and verify.
AI can be the fastest programmer on your team. Your job is to make sure it still has to pass the same gates as everyone else.
Kanwal Mehreen is a machine learning engineer and a technical writer with a profound passion for data science and the intersection of AI with medicine. She co-authored the ebook "Maximizing Productivity with ChatGPT". As a Google Generation Scholar 2022 for APAC, she champions diversity and academic excellence. She's also recognized as a Teradata Diversity in Tech Scholar, Mitacs Globalink Research Scholar, and Harvard WeCode Scholar. Kanwal is an ardent advocate for change, having founded FEMCodes to empower women in STEM fields.
