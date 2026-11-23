---
name: update-project-docs
description: "Synchronize an existing project's documentation with observed code and a completed project-understanding report. Draft reviewable updates, check them, and apply them only after the owner approves the concrete proposal. Use when the owner asks to update all project docs from the current system."
---

# Update Project Docs

Bring an existing project's documentation into line with evidence from its current implementation. Work independently through investigation and drafting. The owner reviews one concrete proposal at the end, then may approve it or give corrections. This skill updates the target project's copies of documents; never edit the reusable templates or skill source to represent one project.

## Establish Evidence

1. Use the current workspace as the target unless the owner supplied a path. State the resolved path. Never default to the home directory.
2. Read `docs/project-understanding.md` and `docs/file-map.md` if present. Check their snapshot and coverage against current files. If either is absent or materially stale, perform the `understand-project` workflow first when available, or carry out the same inventory and tracing before drafting. Continue autonomously while access allows.
   If `docs/evidence-trace.json` exists, run the [evidence check and impact report](../understand-project/references/evidence.md) before using its claims. Reinspect stale sources and the listed documents, then refresh affected claims. Search related documents that may omit the observation ID. A clean hash check establishes only that cited files have not changed; re-read sources before relying on a claim for a consequential update.
3. Use source code and configuration as evidence for implemented behavior, and existing approved product documents for intended behavior. When they disagree, record the discrepancy; do not rewrite an approved or `Locked` requirement to match a bug. Label inferences and unknowns, and keep unconfirmed product choices as Open Questions. Do not invent success metrics, policies, commands, test results, or completed task statuses.

## Prepare a Reviewable Draft

1. Identify applicable documents: product, requirements, architecture, API, data model, design, components, layout, screens, engineering, testing, plan, agent instructions, and file map. Skip documents with no relevant system surface. Preserve useful existing content and stable IDs. Use the bundled project templates if available when creating a missing document; copy them into the draft, not into the skill package.
2. Create a review directory under the target project, such as `.docs-review/<change-name>/`, mirroring the paths of proposed files. Keep the canonical files untouched. Record each original file's current version or fingerprint in `REVIEW.md`, plus the evidence for the proposed changes. Do not overwrite an existing review directory or unrelated owner work.
3. Update only claims supported by inspected files or confirmed decisions. Carry `OBS-*` IDs and source links into the draft or `REVIEW.md` so the owner can inspect each consequential change and future impact reports can locate it. For changed evidence, include the previous/current excerpt when available and explain the proposed correction in `REVIEW.md`; never infer a new rule from a hash change alone. A `Verified` observation may describe implemented behavior; it does not override an approved product decision. Keep `Inferred` and `Needs confirmation` claims out of definitive product rules and list them as questions or tentative observations. Never mark requirements Verified or Locked, tasks Done, or checks Passed without actual evidence. If the understanding report is still `In progress`, continue tracing meaningful areas before claiming an all-project update; if progress is constrained, draft only covered areas and label the proposal partial.
4. Compare the draft with the originals and inspect the diff. Run the documentation checker against a complete staged document tree when available; validate links to source code against their intended final paths in the real project, since source files may not exist inside the draft directory. Otherwise check local links, IDs, and cross-document consistency directly. Resolve introduced mechanical errors and list unresolved semantic conflicts. Prepare `REVIEW.md` with changed files, concise before/after summary, evidence, open questions, checks run, and the exact scope that would be applied.

## Review and Apply

- Present the finished draft and its diff or review manifest to the owner. Ask once for approval of the concrete changes. Do not copy staged files over the canonical documents before approval. Do not ask for per-file permission or pause during routine investigation.
- If the owner reports problems, revise the staged files, rerun relevant checks, and present the revised proposal. Treat each comment as a specific correction; do not claim approval from silence.
- When the owner approves, ensure the originals and cited source files have not changed since the preview. Run the evidence check again; if anything is stale, reinspect and reconcile before applying, and present any materially changed proposal again. Apply only the approved staged files to their corresponding project paths, rerun the relevant documentation checks, and add one concise `CHANGELOG.md` entry for the actual applied update. Preserve unrelated files and completed history.
- Report what was applied, what was checked, and any remaining open questions. If the owner does not approve, leave canonical documents unchanged and point to the staged review for later continuation.
