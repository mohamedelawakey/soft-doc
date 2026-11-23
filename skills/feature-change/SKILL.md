---
name: feature-change
description: "Add or revise a feature in an already documented software project. Use when the owner requests new behavior, a bug fix, or a change that may affect existing requirements and plans."
---

# Feature Change

Update the project documentation and implementation plan for a requested change without losing agreed behavior. Use the existing project's files as the source of truth; this skill does not create a new project from scratch.

## Find the Impact

1. Read the owner's request and the relevant parts of `docs/product.md`, `docs/requirements.md`, and `docs/plan.md`. Follow their IDs into API, data, architecture, UI, engineering, or testing documents only where the change may affect them.
2. Identify whether this is a new capability, an intended change to existing behavior, or a bug fix restoring documented behavior. List affected `REQ-###` and `NFR-###` IDs, especially any marked `Locked`, plus related `API-###`, `ENT-###`, `FLOW-###`, `CMP-###`, `LAY-###`, `SCR-###`, and `TASK-###` IDs where applicable.
3. Compare the request with release scope, exclusions, dependencies, permissions, errors, and existing acceptance criteria. Ask the owner only for decisions that materially change the outcome. A clear request to change a locked behavior is itself the product decision; do not ask for redundant permission.
4. Before editing, show a concise impact preview: current rule, requested rule, affected IDs and files, regression checks, and unresolved choices. Mark uncertain impacts as possible. This is a reviewable explanation, not a separate approval gate when the owner has already requested the change.

## Update the Sources

- For a new feature, add a new stable requirement ID and acceptance criteria. Update product scope if the release boundary changes. Add or revise only the contracts and design documents the feature actually needs.
- For a bug fix, keep the intended existing requirement and record the defect and its affected behavior. Do not rewrite the requirement to match the bug.
- For an approved behavior change, update the existing requirement's expected behavior and acceptance criteria explicitly. Record the decision, reason, and affected IDs so the change is not silent. Preserve unrelated locked behavior.
- Record a consequential confirmed decision in `docs/decisions.md` using the next stable `DEC-###` ID. Include its source, prior rule, new rule, affected IDs, owning files, and verification impact. Do not invent a rationale or copy private chat transcripts. If the file is absent, use the bundled template at `../project-discovery/assets/decisions.md` when available, or create the same fields directly.
- Add new `TASK-###` work to `docs/plan.md`, with dependencies, completion checks, affected requirements, and a detailed feature plan only if substantial. Keep completed task history; use a follow-up task instead of erasing prior work.
- Update relevant test coverage or planned checks in `docs/testing.md`. Mark a requirement Verified or Locked, or a task Done, only after the corresponding evidence exists.

Write confirmed decisions into their owning files. Keep unresolved decisions in Open Questions with their impact; do not invent them. Maintain existing document style, IDs, and links.

After completing a coherent change, prepend a concise entry to the target project's `CHANGELOG.md`. State what changed and include relevant IDs; separate it from the next entry with `---`. Create the file if missing. Include documentation, code, configuration, dependency, and test changes that actually occurred; do not record proposed work as done.

## Verify and Handoff

Check that the new or changed requirement is reflected in the needed API, data, UI, and plan entries without contradictory old rules. Identify existing requirements whose implementation may be affected by shared code and run or plan their relevant regression checks. If implementation is part of the user's request, follow `AGENTS.md`, `engineering.md`, and `testing.md` to complete it; a documentation-only request does not by itself require code changes.

If `scripts/check_docs.py` is available in the skill package or project, run it against the project root. Treat its output as mechanical findings only; inspect semantic consistency yourself. Fix introduced errors and report pre-existing ones separately.

Report the decision, files and IDs changed, what was verified, and any unresolved impact. Do not claim tests passed unless they were run.
