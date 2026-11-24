# Changelog

## 2026-11-24 — Keep portable templates synchronized

- Added a sync and check command for shared documentation templates, monitoring template, and recorder script, plus a GitHub check that catches drift on pushes and pull requests.
- Clarified that project files are the output of a skill run, while the repository templates are maintained as sources.

---

## 2026-11-24 — Clarify what installed skills use

- Updated the README install example to copy all eight self-contained skill folders, skipping existing names, and distinguished bundled resources from the target project's documents.
- Clarified where the documentation checker lives after installation.

---

## 2026-11-24 — Reorganize setup and workflow guidance

- Reorganized the README around safe installation, detailed conversation-driven skill descriptions, common workflows, document ownership, evidence checks, releases, and license terms.
- Changed `project-discovery` to ask for a target path when run from this template repository instead of assuming an example child folder.

---

## 2026-11-23 — Record model usage by request

- Added a provider-neutral event recorder with local JSONL history, dated rate snapshots, estimated token costs, duplicate protection, and a generated Markdown request report.
- Updated agent and project-discovery guidance to use the recorder when provider usage data is available.

---

## 2026-11-23 — Add usage and cost monitoring template

- Added a root `MONITORING.md` ledger for dated activity, measured usage, cost basis, evidence, and unknown coverage; included a project-discovery asset and linked the guidance from agent instructions and README.

---

## 2026-11-23 — Add executable release planning

- Added `plan-project` to turn approved requirements into ordered release tasks, detailed plans for substantial features, and verification coverage.
- Connected `build-project` to use an owner-provided plan or automatically create one within the same build request, preserving existing plans and confirmed choices; documented both workflows.

---

## 2026-11-23 — Add project implementation skill

- Added `build-project` to implement documented releases in working slices, reuse project engineering and testing standards, select stack-specific checks, and verify completed requirements.
- Exposed the skill through the repository's agent convention and documented installation and use.

---

## 2026-11-23 — Publish releases from main pushes

- Changed the release workflow to publish from each push to `main`, including direct pushes and merged pull requests, with tags based on workflow run numbers.
- Updated the README to explain the trigger and tag format.

---

## 2026-11-23 — Align automatic release tags with the first release

- Started merge-based release tags at `v1.0.<PR number>` after the earlier Release Please PR recorded version `1.0.0`.

---

## 2026-11-23 — Publish releases on merge

- Replaced Release Please with a workflow that publishes a tagged GitHub Release when a pull request is merged into `main`, without a release branch or release pull request.
- Documented the automatic tag format and trigger in the README.

---

## 2026-11-23 — Add reviewed release automation

- Configured Release Please to prepare GitHub Release pull requests from Conventional Commits while preserving the manually maintained changelog.
- Documented the GitHub Actions setting needed to create release pull requests.

---

## 2026-11-23 — Document safe skill use

- Added a security policy explaining agent permissions, secret handling, untrusted instructions, and private vulnerability reporting; linked it from the README.

---

## 2026-11-23 — Ignore local working files

- Added a focused `.gitignore` for review drafts, caches, local environments, secrets, and editor files while keeping skills, docs, and benchmark evidence publishable.

---

## 2026-11-23 — Clarify benchmark publication scope

- Explained in the README which benchmark files to publish, what the 18 controlled cases measure, and what they cannot establish.

---

## 2026-11-23 — Benchmark evidence impact on public project code

- Added a reproducible 18-case impact benchmark using Click, Requests, and Flask source files, with results and stated measurement limits.
- Separated unchanged or moved source excerpts into context review and added exact-claim document matching.

---

## 2026-11-23 — Map documentation affected by source changes

- Added `evidence_trace.py impact` to show stale `OBS-*` claims, citing documents, and short before/after source excerpts when recorded.
- Updated the understanding and documentation skills to use impact findings during review, with a focused test of the changed-source workflow.

---

## 2026-11-23 — Add a single project documentation workflow

- Added `sync-project-docs` to combine project understanding, evidence checks, and one reviewable documentation update in a single request.
- Documented project-local installation and use of the combined skill.

---

## 2026-11-22 — Trace project observations to source evidence

- Added `OBS-*` evidence records with source fingerprints and freshness checks to `understand-project`.
- Updated `update-project-docs` to recheck cited sources and carry observation evidence into its review draft.
- Added an isolated evidence-lifecycle test and clear errors for malformed evidence records.

---

From this log's adoption onward, record each completed, persisted project change in a short entry. Group files changed for one purpose into one entry. Write the outcome, not a transcript or a list of keystrokes. Add the newest entry at the top and separate entries with `---`. Do not claim a change or check happened unless it did.

## 2026-11-22 — Add file mapping and reviewed documentation updates

- Added a file-map template and taught `understand-project` to produce an annotated project tree without requiring tool installation.
- Added `update-project-docs` to stage evidence-based documentation updates for owner review before applying them.
- Updated project guidance and the README for the new workflow.

---

## 2026-11-21 — Track coverage while understanding large projects

- Added a subsystem coverage workflow and resumable progress to `understand-project`.
- Updated the README to explain partial reports and coverage levels.

---

## 2026-11-21 — Save project understanding as a report

- Updated `understand-project` to write and refresh an evidence-linked `docs/project-understanding.md` in the target project.
- Updated the README and agent guidance to explain the saved report.

---

## 2026-11-21 — Add independent project orientation

- Added the read-only `understand-project` skill to inspect and explain an existing project without an interview.
- Documented its installation and example prompt in the README.

---

## 2026-11-21 — Keep discovered projects in the open workspace

- Updated project discovery to resolve relative project names inside the current workspace and announce the target path before writing.
- Clarified the default location and test prompt in the README.

---

## 2026-11-21 — Add project change history

- Added a changelog template and guidance for recording project changes.
- Updated the skills and repository instructions to keep this file current.

---

## 2026-11-21 — Add decision trace and documentation checks

- Added a decision log and a documentation checker for links and IDs.
- Updated the skills to preview change impact and record consequential decisions.
