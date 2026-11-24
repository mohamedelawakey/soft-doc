# Agent Instructions

> This file is a reusable starting point. In a software project, replace the bracketed fields with that project's facts and remove this note. This repository currently contains documentation templates and authoring skills, not an implemented product. Do not treat unfilled placeholders in `docs/` as approved project decisions.

## Project Context

**Project:** [Name and one-sentence purpose.]

**Current release:** [Name or version; see `docs/plan.md`.]

**Source layout:** [Link to `docs/file-map.md` when the project's structure has been mapped.]

Start with [README.md](README.md) for orientation. Use [product.md](docs/product.md) for users, goals, and release scope. Read only the documents relevant to the current task.

Record every completed, persisted project change in [CHANGELOG.md](CHANGELOG.md). Use one brief entry per coherent change, newest first, with `---` between entries. Describe the result and relevant IDs; do not log read-only work or claim checks that did not run.

When provider usage metadata is available, record each model call with `python3 scripts/monitor_usage.py record event.json` as specified in [MONITORING.md](MONITORING.md). Use one task ID for a user's request and distinct provider request IDs for its calls. If usage or pricing is unavailable, record it as `Unknown`; do not invent token counts or prices. Keep prompts and secrets out of the event. Agents without access to provider usage cannot capture it automatically.

## Find the Right Source

| Task concerns | Read |
| --- | --- |
| Feature behavior, permissions, or edge cases | `docs/requirements.md` |
| Why a consequential scope or behavior rule changed | `docs/decisions.md` |
| What changed in the project over time | `CHANGELOG.md` |
| Usage, metered activity, or costs | `MONITORING.md` |
| Detailed orientation to the current repository | `docs/project-understanding.md`, when generated; verify time-sensitive claims against source files |
| File and folder structure | `docs/file-map.md`, when generated; verify the map against the current tree |
| System boundaries or technical decisions | `docs/architecture.md` |
| API operations or shared data types | `docs/api.md` |
| Domain data, relationships, or data flows | `docs/data-model.md` |
| Visual rules, reusable UI, shared layout, or pages | `docs/design.md`, `docs/components.md`, `docs/layout.md`, or `docs/screens.md` as relevant |
| Code conventions, dependencies, security, or CI | `docs/engineering.md` |
| Test strategy, test data, or regression coverage | `docs/testing.md` |
| Current tasks or substantial feature plans | `docs/plan.md` and the linked file in `docs/plans/`, if any |

Follow the documented source of truth for each decision. If documents disagree or a required decision is open, identify the conflict and resolve it with the project owner before implementing the dependent behavior. Do not invent product rules, API contracts, or visual specifications.

## Working on a Change

1. Identify the request's scope, affected requirement IDs, and relevant files. For a small fix, use the necessary context without creating a separate feature plan.
2. Check existing behavior before editing. Preserve `Locked` requirements; follow `docs/requirements.md` for bug fixes and approved behavior changes.
3. Keep implementation focused and follow `docs/engineering.md`. Use the existing architecture and project structure; update their documentation when an approved change alters them.
4. Run the checks relevant to the change using `docs/testing.md` and the project commands below. Check regressions for affected existing requirements.
5. Update affected contracts, documentation, and task status when the work and its checks are complete. Report the result, verification performed, and any remaining issue.

## Project Commands

Fill these in after choosing the project's stack. Do not guess commands or mark a check as passed without running it.

| Purpose | Command |
| --- | --- |
| Setup | [Command or documentation link] |
| Format | [Command or documentation link] |
| Lint / static checks | [Command or documentation link] |
| Focused tests | [Command or documentation link] |
| Full tests | [Command or documentation link] |
| Build | [Command or documentation link] |

## Completion and Handoff

- A task is complete when its linked acceptance criteria and relevant checks pass, and affected documentation is current. Use the Definition of Done in `docs/engineering.md`.
- Keep completed tasks and feature plans for traceability. Archive older completed feature plans as described in `docs/plan.md`; do not delete them automatically.
- Before handoff, add a concise `CHANGELOG.md` entry for the completed change. Keep one entry per coherent result and separate entries with `---`.
- In the handoff, name changed areas and requirement IDs, summarize observed test results, and state any unverified behavior or unresolved decision.
