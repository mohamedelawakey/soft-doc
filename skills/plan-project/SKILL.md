---
name: plan-project
description: "Create or strengthen an implementation plan for an approved software project or substantial release, connecting requirements to ordered tasks, detailed feature plans, risks, and verification. Use when the owner asks for a build plan or when a build lacks an executable plan."
---

# Plan Project

Produce a plan that a coding agent or engineer can execute and review without inventing product behavior. Use `docs/plan.md` for the release overview and `docs/plans/REQ-###-short-name.md` only where a feature needs more detail. Product behavior remains in `docs/requirements.md`; engineering commands and quality rules remain in `docs/engineering.md` and `docs/testing.md`.

## Establish the Planning Basis

1. Resolve and state the target project. If the current workspace is the reusable template repository, use an owner-named child project or explicit target; placeholder examples are not approved decisions.
2. Read the in-scope parts of `docs/product.md`, `docs/requirements.md`, `docs/architecture.md`, `docs/engineering.md`, `docs/testing.md`, and the existing plan. Follow API, data, design, or detailed plan links only where they affect an in-scope task. Inspect existing code, manifests, and CI enough to distinguish already implemented work from remaining work; use a dated understanding report or file map for navigation, then verify material claims against source.
3. State the release outcome, in-scope `REQ-*`/`NFR-*` IDs, constraints, current state, and decisions still open. Ask the owner only about choices that change the result or block sequencing. Keep unconfirmed choices explicit rather than selecting a stack, API, policy, or visual rule on the owner's behalf. Continue planning independent work while an answer is pending.

## Shape the Release Plan

- In `docs/plan.md`, arrange reviewable phases by dependency and usable outcome. Give each `TASK-*` a concrete deliverable, linked requirement IDs, prerequisite tasks or external dependencies, owner and reviewer when known, and an observable completion check. Prefer a vertical path through real input, behavior, data, and output early enough to test the architecture; plan later work around the remaining approved requirements.
- Map every in-scope must-have acceptance criterion to a task and a verification approach. Include affected existing and `Locked` requirements in regression planning. Cover relevant integration, failure, permission, performance, and operational risks using the project rules in `docs/testing.md` and `docs/engineering.md`; do not invent thresholds or claim a check already passes.
- Create a detailed plan from `docs/plans/TEMPLATE.md` when a feature spans several subsystems, migrations, external integrations, or sequencing that would be unclear in the release overview. Specify implementation steps with expected results, contracts touched, dependencies, verification, rollback or recovery where needed, and open risks. Link it from the owning `TASK-*`. Keep small tasks in `docs/plan.md`; avoid one file per trivial step.
- Mark new work `Not started`. Preserve completed task history and evidence. For existing work, separate observed implementation from verified completion; a file or a `Done` label alone does not prove acceptance. Update only affected tasks when replanning, and retain stable IDs.

## Check That the Plan Is Executable

Review the plan as if starting implementation: Can the first task begin with current decisions and dependencies? Does each task end in a reviewable result? Are there missing requirement links, circular dependencies, unowned contracts, impossible checks, or hidden deployment and data-migration steps? Run the repository's documentation checker when available, then inspect semantic consistency yourself. Fix gaps supported by approved facts; record unresolved decisions with their impact and next owner action.

Update `CHANGELOG.md` for the persisted planning change. Hand off the phase order, first executable task, coverage of required behavior, major risks, and blocking decisions. Planning does not mark implementation complete or run code checks it has not actually executed.
