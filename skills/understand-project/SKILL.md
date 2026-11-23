---
name: understand-project
description: "Independently inspect an existing software project or documentation repository, write a detailed project-understanding report, and explain its findings. Use when the owner asks to understand, map, or summarize the whole project."
---

# Understand Project

Produce a detailed, evidence-based orientation to the project without requiring the owner to guide the investigation. Write the report to `docs/project-understanding.md` and an annotated structure map to `docs/file-map.md` inside the target project, then summarize them in the conversation. These are dated snapshots of observed state, not the source of truth for product rules or architecture decisions.

## Investigate

1. Use the coding agent's current workspace as the target unless the owner supplied a path. State the resolved target. If no workspace or accessible target exists, ask for the project folder; otherwise continue independently.
2. Inventory the repository before drawing conclusions. Identify source roots, entry points, manifests and lockfiles, configuration, tests, documentation, migrations, deployment files, and generated or vendored areas. Use file listing and search tools already available in the environment; do not require the owner to install `tree` or another package. Follow imports, routes, calls, and IDs to trace important behavior. Ignore build artifacts, caches, dependencies, and secrets unless their role matters. For a large repository, follow [the coverage workflow](references/coverage.md) instead of trying to load everything at once.
3. Read `README.md`, `AGENTS.md`, product and architecture documents, requirements, data/API/UI specifications, plan, decisions, and changelog when present. Verify significant claims against code and configuration when code exists. If the repository is only templates or documentation, explain that accurately.
4. Trace the main user or system flows from entry point through business logic, persistence, integrations, and observable output. Identify ownership of data and important boundaries, including authentication and authorization when present. Inspect representative tests to understand what is actually verified.
5. Resolve ordinary ambiguity by inspecting more files. Do not interrupt the owner for architecture or product questions merely because documentation is incomplete. Mark unsupported conclusions as inferences or unknowns. Do not expose secret values or copy personal data into the report.

## Write the Report

Create or refresh `docs/project-understanding.md` in the target project and link to `docs/file-map.md`. Use clear headings, enough detail to orient a developer who has never seen the repository, and relative links to the files that support material claims. Include:

For each material behavior or architecture claim, assign a stable `OBS-*` ID and record it in `docs/evidence-trace.json` using [the evidence workflow](references/evidence.md). Show its ID, status, and linked source paths beside the claim in the report. Capture a short line excerpt when safe and useful for later comparison. Use `Verified` only when the cited source directly supports the wording; use `Inferred` for a reasoned interpretation and `Needs confirmation` when evidence is insufficient. A source-backed claim is not automatically runtime validated. Do not invent evidence for product intent or claim that uninspected files prove behavior.

- Snapshot date, source revision when available, overall status (`In progress` or `Complete`), inspected scope, and any important files or areas not inspected.
- A coverage table for every first-party subsystem: paths, level reached, evidence, remaining questions or files, and last check. Use the levels in [the coverage workflow](references/coverage.md). Do not mark the report complete while a meaningful subsystem is only indexed or pending.
- Purpose, users, current state, and what can be run or used now.
- Repository map and first-party file inventory: each meaningful file or small related group, its responsibility, and how the parts connect. Group generated, vendored, and repetitive files and state that they were grouped.
- Main flows from entry point to result, domain rules, data model and persistence, API or interfaces, UI, background work, and external integrations where applicable.
- Stack, configuration and environment variables without secret values, dependencies, build/test/deployment path, and observed checks. Distinguish commands found in files from commands actually run.
- Current plan and recent changes; gaps or conflicts between documentation and implementation.
- Risks, unresolved questions, and the best files to read first when continuing work.

Create or refresh `docs/file-map.md` from the actual inventory. Use an annotated tree and a table of meaningful first-party files or groups, their responsibilities, related paths, and coverage evidence. Link to relevant `OBS-*` IDs for behavior descriptions. Group generated, vendored, dependency, cache, and repetitive files explicitly. A path found by listing is only `Indexed`; do not claim to know its behavior until inspected. Use the bundled [file-map template](../project-discovery/assets/file-map.md) when available, or follow the same structure directly.

Adjust the sections to the actual project. For large repositories, inspect one subsystem at a time and save findings, file-map annotations, and coverage status after each meaningful batch. Continue independently while the current run allows; if the work cannot finish, leave an honest `In progress` report with the exact next areas to inspect so a later run can resume. Never claim to have read every file or verified runtime behavior unless that happened. Prefer a navigable file map and connected explanation over a raw file dump. Label each inference and unknown clearly. Do not change source code, product specifications, or other project files while investigating. If a prior report exists, recheck its claims against current files and refresh it rather than appending a second stale report. After saving the report, add one concise `CHANGELOG.md` entry for this documentation change, following the project's format.

Finish with a short conversation summary and links to the report and file map, mentioning the most important finding and any material coverage limit.
