---
id: "21f4761ac0bc4960"
title: "Accelerating software delivery with agentic QA automation using Amazon Nova Act – Part 3"
url: "https://aws.amazon.com/blogs/machine-learning/accelerating-software-delivery-with-agentic-qa-automation-using-amazon-nova-act-part-3"
link: "https://aws.amazon.com/blogs/machine-learning/accelerating-software-delivery-with-agentic-qa-automation-using-amazon-nova-act-part-3"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-28T18:12:13Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Vinicius Pedroni"]
language: "en"
summary: "As quality assurance (QA) automation adoption grows inside an organization, a new problem appears that has nothing to do with writing tests. A platform team stands up test automation, then a second team wants to join, then a dozen more. Soon hundreds of test cases belong to different products and squads, and everyone can see everyone else’s tests. No one can answer a basic question at a glance:…"
tags: ["Amazon Nova", "Expert (400)", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "health & science", "products & launches"]
content_source: "fulltext"
word_count: 1788
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Accelerating software delivery with agentic QA automation using Amazon Nova Act – Part 3

AWS Machine Learning Blog · Vinicius Pedroni · 2026-10-28

Artificial Intelligence
Accelerating software delivery with agentic QA automation using Amazon Nova Act – Part 3
As quality assurance (QA) automation adoption grows inside an organization, a new problem appears that has nothing to do with writing tests. A platform team stands up test automation, then a second team wants to join, then a dozen more. Soon hundreds of test cases belong to different products and squads, and everyone can see everyone else’s tests. No one can answer a basic question at a glance: is this application’s test coverage healthy right now? Test authoring stops being the bottleneck. Organizing tests and controlling who can touch them becomes the work.
A second, related question follows close behind: who owns this application and its tests, and who is accountable when coverage slips? Without a clear owner, health problems have no one to land on.
In the first post, we introduced QA Studio, a reference solution built with Amazon Nova Act. Teams use it to define tests in natural language and run them through AI-powered visual navigation. In the second post, we added test suites and a CLI for batch regression testing in continuous integration and continuous delivery (CI/CD) pipelines. In this post, we cover two capabilities that help QA Studio scale across an organization. The first, applications, organizes tests and reports health metrics. The second, team-based user management, controls who can see and change what.
Organizing tests with applications
An application in QA Studio represents the system under test: a website, a web app, a service front end. It’s the container that gives a collection of tests, a home, and an owner. Use cases (the individual tests from Part 1) and test suites (the regression collections from Part 2) belong to an application, and they inherit its ownership. Instead of one flat list of every test in the deployment, each team works inside the applications they own.
Creating an application takes a name, a base URL, and an optional set of environments such as development, staging, and production. From the application page, teams create new use cases directly in context, add existing ones, and group them into test suites. This is also where QA Studio reports on the health of the tests it runs.
Understanding application health with metrics
Tests produce results. Understanding those results over time is what tells a team whether the development lifecycle for an application is healthy, not only whether a single build is ready for release. QA Studio records the outcome of every execution as Amazon CloudWatch custom metrics, dimensioned by application and by environment. It turns these metrics into a health view on the application page.
The top of the page answers the immediate question with three figures: the pass rate over the selected window, the total number of executions, and the current failure count. Alongside them, QA Studio computes a health score of 0–100. The score starts from the pass rate and subtracts a penalty for flaky tests. That way, an application whose tests pass but flip between pass and fail doesn’t present a falsely perfect picture. A team scanning a portfolio of applications can tell the stable ones from the ones that need attention without opening each result.
The metrics tab moves from the current snapshot to trends. Teams choose a 7-day window with hourly granularity or a 30-day window with daily granularity, and QA Studio charts executions, successes, failures, and average duration across that period. Because the underlying metrics carry an environment dimension, teams filter the view to a single environment. For example, they can compare how staging behaves against production for the same set of tests.
Two views target the tests that cost teams the most time. The flaky tests view ranks use cases by how often they flipped between passing and failing over the last seven days. This surfaces the intermittent failures that erode trust in a suite before they turn into a production miss. The recent failures view lists the latest failed executions for quick triage. Each one links back to the Amazon Nova Act trajectory logs and session recordings described in Part 1. That way, moving from “this test is failing” to “here is exactly what the agent saw” takes one click.
Controlling access with teams and roles
Metrics tell a team how their applications are doing. Team-based user management decides which applications are theirs in the first place. QA Studio organizes access around teams, and an application belongs to exactly one team. Members of that team work with its applications. Everyone else doesn’t see them.
Every team member holds one of five roles, and each role includes the permissions of the ones below it:
- Admin: Studio-wide access to every team, application, and user, including creating teams and assigning applications. Admin is a studio-wide role rather than a per-team assignment.
- Team Lead: Manages their own team members and creates applications for the team.
- Editor: Creates and edits use cases and test suites within the team’s applications.
- Executor: Runs use cases and suites but doesn’t modify them.
- Viewer: Read-only access to the team’s applications and results.
Because roles are cumulative, a Team Lead has everything an Editor has, and so on down to Viewer. Access to a use case or a test suite follows the application that contains it. If a member can work with the application, they can work with its tests, bounded by their role. This keeps permission management at the application level instead of on thousands of individual tests.
An administrator sees the whole studio. The Users page lists every account with its team and role in one place. An admin can tell who holds Team Lead on which team and who carries Studio-wide Administrator rights. In the reference deployment shown here, four users span two teams: two Team Leads, one Viewer, and one Studio-wide Administrator. The Teams page rolls the same data up by team, showing each team’s member count and application count side by side. An admin can see which teams are expanding before opening any one of them.
The same membership data, rolled up by team, appears on the Teams page.
Switching from teams to applications, the studio-wide Applications list shows every application across all teams.
Sharing applications between teams
Teams rarely work in complete isolation. A platform team might own an application that a feature team needs to run against, without handing over the ability to change it. QA Studio supports this with shared access: the owning team grants another team access to an application at a view, execute, or full level.
Shared access follows a ceiling rule. A user’s effective permission on a shared application is the lower of their own role and the level of the grant. A Viewer who is given full access to a shared application remains view-only, because their role is the ceiling. This way, an owning team can share widely without granting more than a recipient’s role allows.
What a team lead sees
A team lead works inside a single team rather than the whole studio. Opening My Team presents four tabs that cover everything the lead controls: Members, Applications, Use Cases, and Shared Access. The Members tab lists the people on the team. The lead can change any member’s role inline or add a new one, so day-to-day access management stays with the person closest to the work. In the AWS Team shown here, the lead manages two members, one Team Lead and one Viewer.
The Applications tab shows only the applications the team owns, each with its test-case count and last-run time. This keeps the lead focused on their own surface rather than the full studio inventory. The Shared Access tab is where cross-team sharing becomes concrete. Here the AWS Team has granted the AMZN Team view access to an application, and the lead can grant, revoke, or change the level of that access. Because the grant was view level, an AMZN Team Editor still sees the shared application read-only: the ceiling rule from the previous section, applied in practice.
The same Team Lead’s Shared Access tab records which other teams can reach the team’s applications, and at what level.
How it works
QA Studio builds team-based access control and metrics on the same serverless foundation described in the earlier posts, adding a few AWS services to the mix:
- Amazon Cognito: Each team maps to a set of Cognito groups, one per role. An AWS Lambda authorizer resolves a caller’s groups into API scopes and team context on every request.
- Amazon DynamoDB: Teams, memberships, application ownership, and cross-team share grants are stored in the existing single-table design.
- Amazon CloudWatch: Every execution emits custom metrics in the QAStudio/Executions namespace, dimensioned by application and environment. The metrics API reads them back to build the health view and trend charts.
- AWS Lambda and Amazon API Gateway: The backend enforces access at two layers: the scope a caller’s role grants, and a resource check that confirms the caller’s team owns or has been shared with the application.
Because access is derived from Cognito group membership, the OAuth client credentials flow from Part 2 fits the same model. A CI pipeline authenticates as a machine identity with the scopes it needs and no more.
Getting started
Applications, metrics, and team-based access control are part of the QA Studio reference solution, which you deploy in your own AWS account with the AWS Cloud Development Kit (AWS CDK). All test data, results, and metrics stay within your account boundaries. After deploying, an administrator creates teams, assigns members and roles, and assigns applications to teams. Each team’s health metrics begin populating as their tests run.
For deployment instructions and configuration details, see the QA Studio GitHub repository and its documentation.
Conclusion
In this post, we showed how QA Studio scales agentic QA automation from individual tests to an organization. Applications give every team a home for their use cases and test suites. They report health through pass rate, trend charts, a flaky-adjusted health score, and failure triage built on Amazon CloudWatch metrics. Team-based user management, backed by Amazon Cognito, keeps each team working within the applications they own, with cross-team sharing bounded by a clear ceiling rule.
These capabilities build on the natural language test authoring from Part 1 and the suites and CI/CD integration from Part 2. Together, they help QA automation grow across many teams without losing visibility or control. To try it in your own environment, deploy the reference solution from the QA Studio GitHub repository, create your first team and application, and run a few use cases to watch the metrics take shape. To learn more about the agent behind it, see the Amazon Nova Act product page.
