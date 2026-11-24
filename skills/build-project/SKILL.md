---
name: build-project
description: "Build an approved software project or release from its requirements, using the owner's plan when provided or creating one automatically before implementation. Use for substantial implementation, not documentation-only planning or audits."
---

# Build Project

Turn the target project's approved requirements and plan into working software. Use an owner-provided plan when one exists; otherwise create the implementation plan as part of this build request. The project documents remain the source of truth. Finish the requested scope instead of stopping at a scaffold or a convincing demo.

## Orient Once

1. Resolve the target from the owner's path or current workspace and state it before writing. If the workspace is this reusable template repository, use an owner-named child project or explicit target; its placeholder documents are not a product specification.
2. Read `AGENTS.md`, the in-scope parts of `docs/product.md`, `docs/requirements.md`, `docs/plan.md`, `docs/architecture.md`, `docs/engineering.md`, and `docs/testing.md`. Follow links to API, data, UI, or detailed plans only for the work at hand. Inspect the current code, manifests, tests, and CI before choosing commands or changing structure. Existing understanding reports and file maps are navigation aids; verify time-sensitive claims against source.
3. Check whether the owner supplied or approved an implementation plan, in `docs/plan.md`, `docs/plans/`, or another location. If so, follow it and check only for material gaps that block the build; do not replace or broadly rewrite it. If no implementation plan exists for a substantial build, invoke the installed `plan-project` skill automatically in the same request, persist its plan, then continue building without asking the owner to invoke another skill. If a plan exists but lacks executable tasks or completion checks, use `plan-project` only to fill those gaps while preserving confirmed choices. Do not expand a small fix into a release plan. Keep a compact working map of deliverables, IDs, affected code, and checks; reuse it instead of repeatedly reading the whole repository. Ask the owner only about essential unresolved behavior or contracts, and continue independent work.

## Build and Check in Slices

- Implement in dependency order, starting with a small end-to-end path that proves the system wiring. Complete each slice through real behavior, relevant tests, and integration with its callers; do not count mock-only UI, stub handlers, or generated boilerplate as finished requirements. For an existing codebase, use its architecture and conventions. For an empty project, choose ordinary tools consistent with the approved constraints, and record actual setup and check commands in `docs/engineering.md` and `docs/testing.md`.
- Keep changes focused on approved scope. Use the owning documents for requirements and contracts; do not rewrite them to match a bug. Preserve `Locked` behavior. Route a newly requested feature or consequential behavior change through `feature-change` when that workflow is available.
- Follow `docs/engineering.md` for code quality, dependencies, security, data access, performance, CI, and Definition of Done. Follow `docs/testing.md` for risk-based tests and regression coverage. Apply their project-specific rules rather than copying generic checklists into the build. If a rule is still a template placeholder, establish the needed project-specific choice from the actual stack and owner decisions before relying on it.
- Choose the formatter, linter, type checker, test runner, and build command from the project's language and manifests. Run the smallest relevant checks during a slice, then the required project gates on the integrated result. Do not guess commands, install tools without a concrete need, or repeatedly rerun broad suites after an unchanged result. Fix introduced failures and distinguish pre-existing failures with evidence.
- Check performance where the requirement or data flow warrants it: inspect query patterns and data volume, measure a representative path, and optimize a demonstrated bottleneck. Avoid speculative caches and invented targets. Check security boundaries where the slice introduces them, including access to another user's resource, input handling, secrets, and external calls. Tests and review should target actual risks, not claim universal security or zero bugs.
- Keep a short progress record in the existing plan for substantial work: completed slice, checks and outcomes, next slice, and blockers. Update it when a slice's status changes, not after every command. Continue across slices while the requested release is feasible; surface only decisions that block dependent work.

## Finish Against Evidence

Review the integrated behavior against every in-scope acceptance criterion and affected existing requirement. Inspect the final diff for unfinished paths, accidental scope changes, weak error handling, unused code, dependency drift, and misleading claims. Run the required format, lint, static, test, and build gates plus relevant performance or security checks. Do not mark `TASK-*` Done or `REQ-*` Verified until the corresponding criteria and checks pass. Record remaining limitations precisely.

Update affected contracts, task status, check commands, and `CHANGELOG.md` for persisted changes. In the handoff, name what works, completed IDs, actual commands and results, and any unverified or blocked behavior. A complete build claim requires the project's Definition of Done; otherwise report the exact remaining work.
