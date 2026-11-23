---
name: sync-project-docs
description: "Understand an existing project and prepare one evidence-backed update of its documentation. Use when the owner wants the whole project inspected and its docs synchronized in one request."
---

# Sync Project Docs

Run the project-understanding and documentation-update workflows as one continuous job. The owner makes one request and reviews one consolidated proposal. This skill is for an existing project; use `project-discovery` when defining a new product from an idea.

## Run the Workflow

1. Resolve the target to the current workspace unless the owner supplies a path. State that path. Never fall back to the home directory. If the workspace is the reusable template repository, inspect that repository only when the owner explicitly asks for it; otherwise use the owner-named project in the open workspace.
2. Read the installed sibling [understand-project skill](../understand-project/SKILL.md) and follow its investigation and report workflow. Inventory and trace the actual project, write or refresh `docs/project-understanding.md`, `docs/file-map.md`, and `docs/evidence-trace.json`, and check the evidence register. Record coverage honestly; continue across subsystems without stopping for routine questions. These observed-state files are created in the target project, not in the reusable skill package.
3. Without asking the owner to invoke another skill, read the installed sibling [update-project-docs skill](../update-project-docs/SKILL.md) and follow its drafting and checking workflow. Run the evidence impact report to identify stale observations and referenced documents. Use the fresh report and source evidence to stage applicable document updates under one `.docs-review/<change-name>/` directory. Include a `REVIEW.md` manifest, changed-file summary, observation IDs and sources, previous/current excerpts when available, unresolved conflicts, and checks. Do not present inferred behavior as an approved product rule or change a `Locked` requirement to match observed code.
4. Present one consolidated handoff: understanding report, file map, coverage limits, proposed documentation diff, and open questions. Ask for approval only after the concrete draft is ready. If the investigation cannot cover a meaningful subsystem, mark the report and proposal partial and state exactly what remains; do not imply the whole project was synchronized.
5. If the owner corrects the draft, revise and recheck it. When the owner approves the concrete proposal, recheck original documents and cited source files, then apply only the approved staged updates using the update workflow. If sources or originals changed materially, reconcile and show the changed proposal again. Record the understanding snapshot when saved and the approved document update when applied in `CHANGELOG.md`; do not claim canonical docs were updated while they are still staged.

Keep investigation and drafting in the same run. Do not ask the owner to choose or trigger the component skills separately. Source-code edits, product decisions, and publication are outside this workflow unless separately requested.
