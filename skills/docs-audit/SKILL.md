---
name: docs-audit
description: "Audit a project's documentation for broken links, inconsistent IDs, contradictory decisions, missing requirement-to-task coverage, and unsupported completion claims. Use for a documentation consistency review."
---

# Docs Audit

Review the live project documents for concrete inconsistencies and gaps. This skill is read-only unless the user explicitly asks to fix the findings. Distinguish an unfilled template repository, where placeholders are expected, from an active project, where placeholders may indicate unfinished decisions.

## Scope

Start with `README.md`, `AGENTS.md`, `CHANGELOG.md`, `docs/product.md`, `docs/project-understanding.md`, `docs/file-map.md`, `docs/decisions.md`, `docs/requirements.md`, and `docs/plan.md` when present. Follow references to architecture, API, data, UI, engineering, testing, and detailed feature plans only where needed to check a claim. Do not infer a feature from an example row in a template.

## Checks

1. **Links and IDs:** Verify local Markdown links resolve. Check that each ID has one authoritative definition, references point to an existing definition, and index entries agree with their detail sections. An ID appearing in its index and detail is expected; two conflicting definitions are not.
2. **Product to requirements:** For each real Must-have capability in `product.md`, locate one or more requirements with testable acceptance criteria. Flag requirements that conflict with the stated release scope or exclusions. Do not demand API or UI entries for a feature that does not use them.
3. **Requirements to plan:** For each in-scope Must-have requirement, locate implementation task IDs and completion checks. Check task dependencies for missing or circular references and detailed plan links where listed.
4. **Contracts and design:** Compare the actual requirement rules with relevant API operations, entities and data flows, screens, components, and architecture ownership. Report contradictions or missing contracts only when the feature needs them.
5. **Status and evidence:** Check that `Done` tasks have recorded results or evidence, `Verified` and `Locked` requirements have actual verification records, and release readiness is not claimed while blocking decisions or checks remain. A status label is not evidence by itself.
6. **Unfinished decisions:** Identify unresolved questions that block active work and placeholders left in documents being treated as complete. Keep tentative choices separate from approved ones.
7. **Decision trace:** For consequential changes, verify that each confirmed `DEC-###` entry identifies its source, affected IDs, current owning documents, and verification impact. Check whether the owning documents reflect the confirmed rule and whether a superseded decision points to its replacement.
8. **Change history:** Check that material completed changes have concise, factual changelog entries and that entries do not describe proposed work as completed. Do not infer that an old project has complete historical coverage before the changelog was adopted.
9. **Observed structure:** When a file map or understanding report exists, check that important paths still exist and that coverage labels do not claim inspection or validation without linked evidence. Treat these as dated snapshots rather than authoritative product rules.

Use repository search and direct file reads to verify claims. Run `scripts/check_docs.py` against the project root when available, then inspect its findings. The script checks mechanical links and ID coverage; it cannot prove semantic consistency or that a test result is genuine. For semantic gaps, cite the exact files and IDs involved; do not report a missing item merely because a naming pattern differs. Do not invent test results or mark work complete during an audit.

## Result

Report findings by severity: blocking contradiction or missing decision, material coverage gap, then minor link or wording issue. For each, state the evidence, affected IDs, practical impact, and a concrete correction. If nothing material is found, state what was checked and the limits of the audit. When the user asks for fixes, change only confirmed mechanical errors and agreed decisions, then recheck the affected links and references.
