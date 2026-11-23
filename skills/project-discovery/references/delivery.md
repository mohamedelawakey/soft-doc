# Engineering and Delivery Decisions

Read the existing repository manifests, commands, CI configuration, and filled product and technical documents before asking about delivery. Use the matching files in `assets/` when documents are absent.

- `engineering.md`: fill actual language and tool choices, naming and code conventions, dependency manifest and lockfile paths, error handling, logging, security rules, CI gates, and Definition of Done. Do not invent commands or library versions. Keep detailed test strategy in `testing.md`.
- `testing.md`: decide relevant test levels and risk checks, safe test data, isolation, requirement coverage, local commands, and CI suites. Do not invent coverage or performance thresholds.
- `plan.md`: turn requirements into `TASK-###` work with dependencies, deliverables, completion checks, status, owners and reviewers if known, and release readiness. Use `docs/plans/TEMPLATE.md` only for substantial features needing detailed steps. New planning work starts Not started; planning alone does not make any task Done.
- `AGENTS.md`: if the target project uses it, fill only its project context, task routing, actual commands, and concise handoff rules. Avoid duplicating the detailed documents or requiring every document to be read before every edit.

Ask the owner or developer to decide missing stack or process choices that materially affect implementation. Where the answer is genuinely not yet known, preserve an explicit open decision rather than a fake value. Before finishing, check that must-have requirements have tasks and completion checks, and that commands and roles recorded as facts are real.
