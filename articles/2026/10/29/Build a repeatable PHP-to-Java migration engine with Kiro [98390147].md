---
id: "983901472b072637"
title: "Build a repeatable PHP-to-Java migration engine with Kiro"
url: "https://aws.amazon.com/blogs/machine-learning/build-a-repeatable-php-to-java-migration-engine-with-kiro"
link: "https://aws.amazon.com/blogs/machine-learning/build-a-repeatable-php-to-java-migration-engine-with-kiro"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-29T18:14:17Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Sarat Guttikonda"]
language: "en"
summary: "When your team moves a mature PHP application to Java, you gain stronger type safety, broader library support, and more predictable scaling. A PHP codebase built over the years with Laravel, Symfony, or Doctrine carries business rules in places that are not obvious, from Eloquent traits to XML mapping files, so a structurally similar Java port can compile cleanly and still behave differently. \n…"
tags: ["Advanced (300)", "AWS Transform", "Kiro", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 1918
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Build a repeatable PHP-to-Java migration engine with Kiro

AWS Machine Learning Blog · Sarat Guttikonda · 2026-10-29

Artificial Intelligence
Build a repeatable PHP-to-Java migration engine with Kiro
When your team moves a mature PHP application to Java, you gain stronger type safety, broader library support, and more predictable scaling. A PHP codebase built over the years with Laravel, Symfony, or Doctrine carries business rules in places that are not obvious, from Eloquent traits to XML mapping files, so a structurally similar Java port can compile cleanly and still behave differently.
This post shows how to turn PHP-to-Java migration from a one-time leap of faith into a measurable, repeatable process using Kiro. Kiro is an AI integrated development environment (IDE) that pairs an AI agent with your codebase to run multi-step engineering tasks with you in the loop. The approach centers on a reusable engine: a shared methodology, a mechanical discovery scanner, and an eight-phase workflow. This engine treats the original PHP application as the specification and refuses to declare the Java port correct until a parity harness verifies it.
Prerequisites
Before getting started, you need:
- Familiarity with PHP (Laravel/Eloquent or Symfony/Doctrine). Java knowledge (Spring Boot, JPA) helps you review the generated output, but the engine produces idiomatic Java for you, so you don’t need to rewrite the application in Java yourself.
- A Kiro workspace with access to Skills and Steering files.
- PHP 8.0 or newer on the machine running the discovery scanner, and Java 21 with Maven for the generated Spring Boot projects.
- A basic understanding of migration planning (discovery, translation, and validation).
What you will learn in this post
You start with an open repository, so you can run the engine yourself rather than read about it. Everything the engine knows lives in a small set of skill files, and with those files, you can run the same methodology in more than one way.
Two ways to run the engine: Kiro and AWS Transform
Everything here is packaged as skill files: versioned Markdown capability packages that encode the migration methodology (php-to-java-migration) and the discovery scanner workflow (php-model-discovery). Because that knowledge lives in files rather than any one tool, you can run the same methodology in two ways.
Method 1: Kiro, interactive and developer-in-the-loop
Kiro brings an AI agent into your editor to drive a migration step by step. Open the repository root as a Kiro workspace and the skills activate automatically when you ask Kiro to migrate a PHP application. Kiro then walks the eight-phase workflow with explicit approval gates, so you review the discovery manifest, approve the rulebook, and sign off on each phase before the next begins. It’s the mode used for every example in this post.
Method 2: AWS Transform, agentic and at portfolio scale
AWS Transform is the AWS agentic AI service for large-scale migration and modernization, and it now integrates natively with Kiro. Through that integration, you can hand AWS Transform the same skill files that govern an interactive Kiro session, so discovery before translation, the parity harness as referee, and ‘fix the loop, not the code’ apply to an autonomous run.
When each path fits
- Control and autonomy: Use Kiro to work through the code first: run the skill on one application, read the generated Java, and run the tests. When you want to migrate more, AWS Transform runs the same methodology agentically with review at the checkpoints the skill defines.
- Scale and novelty: Kiro handles one application at a time and suits first-of-a-kind frameworks. AWS Transform runs many applications as parallel jobs.
- A shared feedback loop: Both paths read the same skill files, so every rulebook fix made in Kiro improves the next AWS Transform run, and vice versa.
Solution overview: One shared brain, many projects
The engine is organized around a single principle: one shared brain, many projects. To open it, clone the repository locally, then in Kiro open a folder and select the repository root (the folder containing .kiro/). Kiro loads the skills and steering automatically, with fuller steps in “Getting started.”
The workspace separates a shared methodology layer from the individual projects that use it, as shown in the following diagram. At the top is a global .kiro/ layer that every project draws on. Beneath it sit the per-project folders, each with its own PHP source, Java output, and specification sub-folder.
Those same shared skill files can be run in two different ways, shown in the following diagram. The identical eight-phase, parity-first pipeline can be driven either by Kiro (interactive, one application at a time) or by AWS Transform (agentic, at portfolio scale), and both convert PHP source into parity-verified Spring Boot Java.
A shared, global layer under .kiro/ holds two Skills, php-model-discovery (the scanner) and php-to-java-migration (the eight-phase playbook), plus the core-workflow.md Steering file. Each per-project folder holds its own PHP source, Java output, and spec sub-folder under .kiro/specs/, so improving the methodology once lets every project inherit the gain.
Discovery before translation
The single most important rule fires before anything else: Don’t read, guess at, or hand-translate a model or entity file until the scanner has run.
The scanner works in a single pass with no dependencies, as shown in the following diagram. It applies three discovery strategies to the source tokens and emits one JSON manifest, with anything ambiguous routed to a review-flag queue for a human to resolve.
The scanner is discover-models.php, a single-file, dependency-free PHP command-line tool that doesn’t execute the target code. It only reads source text as tokens, so it runs against apps of your choice whether its dependencies are installed. It runs three strategies on every scan: Eloquent model discovery (walking the class inheritance chain to Illuminate\Database\Eloquent\Model), Doctrine attribute detection (the #[ORM\Entity] attribute), and ORM XML mapping (external *.orm.xml files). The output is a single JSON manifest. A models[] array carries every field, cast, relationship, and visibility rule, and a flags[] array appears on every entry. The scanner flags ambiguity rather than guessing. For example, a $fillable list built from a runtime expression becomes a plain-English flag, and that flag list is the human review queue.
The parity-first pipeline
Phase 0 is preparatory: it runs the scanner and assembles the inventory. The first three phases then concentrate human expertise. Phase 1 builds the parity harness before Java is written, replaying request/response pairs against both the PHP original and the Java port. The harness must pass against working PHP and fail when you break it deliberately, because a harness that misses injected breakage is not trusted. Phase 2 seeds the rulebook and gap inventory (RULEBOOK.md, GAP_INVENTORY.md), and Phase 3 stress-tests it against representative files before committing it across the application.
The first four phases concentrate human expertise. Phase 0 runs the scanner and assembles the inventory. Phase 1 builds the parity harness before Java is written, replaying request/response pairs against both the PHP original and the Java port. The harness must pass against working PHP and fail when you break it deliberately, because a harness that misses injected breakage is not trusted. Phase 2 seeds the rulebook and gap inventory (RULEBOOK.md, GAP_INVENTORY.md), and Phase 3 stress-tests it against representative files before committing it across the application.
Phases 4–8 are mostly self-driving loops: Phase 4 scaffolds the project, Phase 5 translates the data model from the manifest, Phase 6 translates the I/O layer (routes become controllers, middleware becomes filters, validation becomes annotated data transfer objects), Phase 7 converts business logic in batches, and Phase 8 proves parity against the harness and cuts over. Two principles govern the loop. First, the PHP code is the specification: the port is done when the referee agrees, or each mismatch is logged as an approved change. Second, you fix the loop, not the code, amending the rulebook and regenerating rather than hand-patching.
Walkthrough: From Eloquent to Spring Boot
The laravel-eloquent-sample project is a working, bounded example: a read-only slice of an open source Laravel application, with the Book, Chapter, Page, and User models migrated to Spring Boot 3.4.1 on Java 21 with Maven and an in-memory H2 database.
The mapping from PHP to Spring Boot is mechanical and traceable, as shown in the following diagram. Each manifest entry on the left maps to a Java construct on the right, producing the layered runtime architecture of the generated application slice.
The mappings are mechanical and traceable back to the manifest: a PHP namespace becomes a Java package, an Eloquent model becomes a JPA @Entity, has Many and belongs to relationships become @OneToMany and @ManyToOne, and Eloquent query scopes become Spring Data repository methods. The discipline shows in serialization: html, markdown, and text carry @JsonIgnore because the manifest recorded them in Page’s $hidden list, while Book’s description deliberately doesn’t.
The spec is candid that only 4 of 37 models were ported and, most important, that the parity harness was never built for this slice, which it calls “the single biggest gap.” Documenting where it falls short is itself part of the design.
Getting started
The complete migration engine is available in the sample PHP-to-Java migration repository.
To use it:
- Clone the repository and open its root as your Kiro workspace (open a folder and select the folder containing .kiro/). Nothing to install beyond PHP 8.0+ for the scanner and Java 21 with Maven.
- Fetch the PHP source into the project’s source-php/ folder. The README pins the exact upstream commits used for parity so anyone can reproduce the baseline.
- Ask Kiro to migrate the application. The php-to-java-migration skill activates automatically, runs the scanner first, generates a fresh spec under .kiro/specs/, and walks you through the approval gates.
- For an agentic run, point AWS Transform at the same skill files, so its agents execute the identical methodology across your portfolio.
The methodology auto-detects Laravel, Symfony, CodeIgniter, and plain PHP, and extension is additive: add a detection row and a references/<framework>-to-spring.md guide for a new framework. Because Kiro and AWS Transform read the same files, refining them once upgrades both engines.
Clean up
If you deployed the sample Spring Boot application during this walkthrough:
- Stop the running Spring Boot application (the in-memory H2 database is ephemeral and requires no separate cleanup).
- Remove the generated Java project folder from your workspace if no longer needed.
- The discovery scanner produces only a JSON manifest file. Delete the discovery scanner’s JSON manifest from your working directory if you don’t plan to reference it.
- No AWS resources are provisioned by the migration engine itself, so there are no cloud resources to deprovision.
Conclusion
We showed how to build a repeatable PHP-to-Java migration engine with Kiro that turns large-scale rewrites into a measurable, compounding process. The key principles are:
- Discovery before translation: A mechanical scanner inventories every model, field, and relationship, so you don’t guess at structure.
- Build the judge before the code: A parity harness defines done before the first line of Java is written.
- Fix the loop, not the code: When the same mistake appears across files, amend the rulebook and regenerate rather than hand-patching.
- One shared brain: The methodology is written once, shared across projects, and improves with each migration.
None of this is specific to PHP or Java. The same shape applies to other migrations where the old system is the only complete specification. Clone the sample PHP-to-Java migration repository, open it as a Kiro workspace, and explore the Skills and Steering capabilities that power it, or bring the same skill files to AWS Transform. For more about language migration patterns on AWS, see the AWS Prescriptive Guidance documentation.
