---
id: "b295e50f8cea1a7b"
title: "Transforming Ripgrep's Documentation with AI Automation and MkDocs"
url: "https://entropicdrift.com/blog/mkdocs-drift-automation"
link: "https://entropicdrift.com/blog/mkdocs-drift-automation"
source: "Entropic Drift"
domain: "entropicdrift.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-14T05:19:51Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["ankitg12"]
language: "en"
summary: "From Two Files to Comprehensive Documentation#\nripgrep is one of the most popular command-line search tools, with over 57,000 stars on GitHub. Despite its popularity and rich feature set, the documentation consisted of just two files: a feature-focused README and a tutorial-style GUIDE. While these files were well-written, they left gaps:\n- No structured learning path from basics to advanced…"
tags: []
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1936
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50494244"
score: 14
comments: 4
community: "Hacker News"
---

# Transforming Ripgrep's Documentation with AI Automation and MkDocs

Entropic Drift · ankitg12 · 2026-11-14

From Two Files to Comprehensive Documentation#
ripgrep is one of the most popular command-line search tools, with over 57,000 stars on GitHub. Despite its popularity and rich feature set, the documentation consisted of just two files: a feature-focused README and a tutorial-style GUIDE. While these files were well-written, they left gaps:
- No structured learning path from basics to advanced features
- Limited visual aids to explain complex concepts
- Features scattered across different sections
- No dedicated troubleshooting or reference sections
Using an evolved version of my documentation automation workflow (originally built for Prodigy’s documentation), I generated 50+ pages of enhanced documentation, now live at https://iepathos.github.io/ripgrep.
This post documents how the workflow evolved to handle:
- Intelligent page splitting - Breaking monolithic chapters into focused subpages
- Automated visual enhancement - Adding diagrams, admonitions, and annotations where they help
- Mermaid diagram validation - Ensuring all generated diagrams render correctly
What Changed: MkDocs vs mdBook#
The original workflow used mdBook, a simple static site generator popular in the Rust ecosystem. MkDocs Material offers significantly more features:
The Enhanced Workflow Architecture#
The ripgrep workflow introduced critical improvements over previous iterations. The complete flow:
- Setup Phase: 
  - Analyze codebase features
  - Detect documentation gaps and create stub pages
  - Analyze page sizes and structural complexity
  - Automatically split oversized pages into focused subpages
  - Auto-discover all markdown files (including newly split pages)
- Map Phase (per-page): 
  - Analyze page for drift (subsection-aware)
  - Fix detected drift with validation
  - Enhance with visual features (diagrams, admonitions, annotations)
- Reduce Phase (holistic): 
  - Validate with strict build (mkdocs build --strict)
  - Check structure and feature consistency
  - Validate Mermaid diagrams with official renderer
  - Auto-fix any issues found
Full workflow YAML available on GitHub
Four Key Innovations#
1. Intelligent Page Splitting#
The breakthrough feature: automatic page splitting based on structural analysis.
The original GUIDE.md was over 1,400 lines—a monolithic wall of text. The workflow now analyzes page structure before processing and automatically splits oversized pages into focused subpages based on:
- Line count and section depth (>300 lines or >5 major sections triggers splitting)
- Topic cohesion within sections
- Natural split points at heading boundaries
For ripgrep, this transformed:
- GUIDE.md (1,400 lines) → basics/ directory with 8 focused pages
- Binary Data section (350 lines) → binary-data/ directory with 5 specialized pages
- Troubleshooting → troubleshooting/ directory with 6 topic-specific pages
Benefits:
- Context-aware agents: Each agent works on focused topics, not overwhelming monoliths
- Better enhancement: Visual features applied to coherent topics
- Improved navigation: Readers find specific information faster
- Maintainability: Smaller pages easier to update
2. Exhaustive Page Discovery#
After page splitting creates new files, we ensure every page gets processed with direct filesystem scanning:
find $DOCS_DIR -name "*.md" -type f | jq -R -s 'split("\n") | map(select(length > 0)) | ...'
This is critical because:
- Comprehensive coverage: Every .md file processed, including newly split pages
- No manual tracking: Filesystem is source of truth
- Orphaned pages caught: Pages that exist but aren’t linked are discovered
- Deterministic: Same files every time
3. Visual Enhancement Per Page#
After drift is fixed, each page gets enhanced in the map phase (not reduce), meaning each agent has full context about what the page covers:
- Mermaid diagrams for architecture and workflow visualization
- Admonitions (warnings, tips, notes) for important callouts
- Code annotations with numbered inline explanations
- Tabbed content for alternative approaches
The AI attempts context-aware decisions: “Pattern matching is decision-heavy, add a decision tree. Installation varies by platform, use tabbed content.”
4. Mermaid Diagram Validation with Mermaid-Sonar#
When you generate dozens of Mermaid diagrams automatically, some will have syntax errors and many will be too complex to be readable. What started as a simple syntax validation step in the workflow evolved into a standalone tool: mermaid-sonar.
The evolution: Initially, the workflow used @mermaid-js/mermaid-cli to catch syntax errors before build. But I noticed a pattern: AI agents would create syntactically valid diagrams that were cognitively overwhelming. An 80-node decision tree for a binary choice. A complex flowchart for a 3-item list. Diagrams that rendered correctly but hurt comprehension.
Syntax validation alone wasn’t enough. I needed complexity validation to guide AI toward readable diagrams.
Mermaid-sonar uses static code analysis and research-backed heuristics to measure diagram complexity and provide actionable feedback to AI agents:
- shell: "mermaid-sonar $DOCS_DIR --strict"
  on_failure:
    claude: "/prodigy-fix-mermaid-diagrams ${shell.output}"
What makes it effective for AI workflows:
- Static analysis: Parses diagram source code, calculates graph metrics (nodes, edges, density, branching)
- Research-backed thresholds: Based on cognitive load research (50/100 node limits), graph theory, and Mermaid performance characteristics
- Specific feedback: Instead of “too complex,” provides “12 parallel branches (>8 max) → use LR layout or split”
- Fast execution: No rendering required, optimized for CI/CD loops
- Machine-readable output: JSON format allows AI agents to understand and fix issues automatically
The validation caught 8 broken diagrams in ripgrep’s docs that would have failed during build, plus 12 overly complex diagrams that needed simplification.
Complexity issues detected:
- Diagrams with >50 nodes (high-density) or >100 nodes (low-density)
- Wide tree diagrams with >8 parallel branches
- Graphs exceeding 100 connections (Mermaid’s O(n²) limit)
- High graph density (>0.3) indicating visual clutter
- Layout mismatches (TD layout for wide trees, LR for deep hierarchies)
The key insight: AI agents need quantitative feedback to understand “too complex.” By converting subjective readability into measurable metrics with clear thresholds, mermaid-sonar guides AI toward diagrams that actually help readers instead of overwhelming them.
This is the difference between “catch errors” and “guide toward quality.” Traditional validation tells you what’s broken. Heuristic-based validation tells you what needs improvement and how to improve it—feedback AI agents can act on automatically.
Real Results: ripgrep Documentation Transformation#
Before:
- 2 documentation files (README.md, GUIDE.md)
- ~1,800 total lines of markdown
- No visual diagrams
- Limited structure (linear reading path)
After:
- 55 focused documentation pages
- Organized into 7 major sections
- 87 Mermaid diagrams explaining workflows and decision trees
- 358 admonitions highlighting warnings and tips
- 180+ code annotations with inline explanations
- Tabbed installation instructions for different platforms
- 100% strict build success - no broken links or invalid syntax
Example: Pattern Matching Page Transformation#
Before (from GUIDE.md): Plain text explaining regex vs literal patterns, scattered across multiple sections.
After (docs/basics/pattern-matching.md):
Added decision tree diagram helping users choose between literal and regex patterns, converted important notes to styled admonitions (tips for when to use -F flag), and annotated code examples with numbered callouts explaining each flag’s purpose.
The page went from “walls of text” to “guided learning.”
Key Insights#
1. Page Splitting Unlocks Comprehensive Documentation#
The most impactful innovation wasn’t visual enhancements—it was automatic page splitting. No reader wants to scroll through 1,400 lines to find information about case sensitivity. The workflow handles splitting automatically by:
- Identifying oversized pages (>300 lines or >5 major sections)
- Determining logical split points (section boundaries)
- Creating focused subpages with proper hierarchy
- Updating cross-references and navigation
Documentation that expands organically from codebase analysis becomes navigable and learnable, not an overwhelming wall of text.
2. Visual Features Need Intelligence#
You can’t apply visual enhancements mechanically. A rule-based system would either over-apply (cluttering simple pages) or under-apply (missing opportunities). AI agents with context make nuanced decisions about which features help specific content.
3. Complexity Validation Catches AI Over-Engineering#
Syntax validation alone isn’t enough for AI-generated diagrams. AI agents tend to over-engineer visualizations, creating elaborate flowcharts for simple categorizations. Mermaid-sonar’s complexity analysis catches these issues automatically by measuring:
- Cognitive load: Research shows 50-node limit for readable high-density graphs
- Visual hierarchy: Detects wide trees (>8 branches) that should use horizontal layout
- Performance limits: Flags graphs approaching Mermaid’s O(n²) rendering threshold
Automated complexity validation → automated fixes → readable diagrams. Manual review still catches poor diagram type choices, but complexity issues are handled automatically.
4. Per-Page Enhancement Beats Bulk Processing#
Running enhancement in the map phase (per-page) instead of reduce phase (bulk) means each agent has full context about what the page covers. Decisions are informed by content, not position. The extra parallelization complexity is worth it.
Comparing the Three Generations#
The evolution: accuracy → precision → transformation.
How to Adapt This Workflow#
Want to build something similar? Here’s the condensed path:
1. Start with MkDocs Material#
Configure with features you want: admonitions, code annotations, Mermaid diagrams, tabbed content.
2. Build Auto-Discovery#
Use find and jq to discover all markdown files as your source of truth.
3. Create Enhancement Logic#
Write prompts that analyze page content and add:
- Mermaid diagrams for architecture/workflows
- Admonitions for warnings/tips/notes
- Code annotations for complex examples
- Tabs for alternative approaches
4. Add Multi-Layer Validation#
- Per-page (map phase): Each page meets quality standards
- Build validation (reduce): mkdocs build --strict
- Consistency (reduce): Pages use similar enhancements
- Diagram validation: Verify Mermaid syntax with mermaid-sonar docs/ --strict
5. Iterate and Refine#
Run the workflow, review output, adjust. Because agents enhance existing documentation rather than replacing it, manual improvements become context for the next run. The documentation becomes iterative: agents enhance, you refine, agents use refinements as context.
Full implementation details in the GitHub workflow
Future Enhancements#
The workflow is production-ready, but opportunities abound:
Screenshot Management: Detect when UI screenshots are outdated and regenerate using browser automation.
Interactive Examples: Generate runnable code examples with embedded outputs.
Version-Specific Documentation: Integrate with mike to maintain documentation for multiple versions automatically. When a new version releases, run drift workflow against the new codebase and generate version-specific docs with accurate examples.
Conclusion#
By combining intelligent page splitting, auto-discovery, subsection-aware drift detection, per-page visual enhancement, multi-layer validation, and strict build enforcement, we’ve created a workflow that can help transform a project’s minimal documentation into more comprehensive guides with AI assistance.
The ripgrep documentation demonstrates this transformation in production. Every page split, diagram, admonition, and annotation was generated automatically from the original README, GUIDE, and code. The workflow preserved the authors’ clarity and intent while making it dramatically more accessible.
The docs aren’t perfect. We’ve only begun to codify the rules and heuristics needed to guide AI to mimic a skilled technical writer. This is just an early run of this workflow on a third party open source library to explore the limits of AI documentation automation. At the end of this journey, we hope to have an open source solution that anyone can use to produce high quality docs for code bases.
The pattern is reusable. Point it at any project with well-written code, and watch it transform into comprehensive guides with visual aids and structured learning paths.
Resources#
Live Documentation Examples:
- ripgrep Docs (transformed from 2 files): https://iepathos.github.io/ripgrep/
- Prodigy Docs (MkDocs Material): https://iepathos.github.io/prodigy/
- Debtmap Docs (mdBook): https://iepathos.github.io/debtmap/
Blog Posts:
- Original automation case study: Automating Documentation Maintenance with Prodigy
Workflows (showing evolution):
- Generation 1: Debtmap book-docs-drift.yml (chapter-level)
- Generation 2: Prodigy book-docs-drift.yml (subsection-aware)
- Generation 3: ripgrep mkdocs-drift.yml (page splitting + visual enhancements + diagram validation)
Tools:
- Prodigy: GitHub | Crates.io
- Debtmap: GitHub | Crates.io
- Mermaid-Sonar: GitHub | npm
- ripgrep: GitHub | Fork with MkDocs
- MkDocs Material: https://squidfunk.github.io/mkdocs-material/
This blog post documents the third generation of the documentation automation workflow. The first generation (Debtmap) proved the concept at the chapter level. The second generation (Prodigy book-docs) added subsection precision. This third generation (ripgrep mkdocs) adds intelligent page splitting, visual engagement, and diagram validation. The workflow transformed ripgrep’s 2-file documentation into 55+ comprehensive pages—proving that AI automation can enhance existing open source projects without replacing their authors’ expertise.
