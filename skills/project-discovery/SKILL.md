---
name: project-discovery
description: "Interview a project owner and build the project's product, requirements, architecture, interface, engineering, testing, and release-plan documents. Use when defining a new software project from an idea."
---

# Project Discovery

Turn a project owner's conversation into project-specific documentation without asking them to edit Markdown. Use the bundled templates as starting structures, not as facts about the project. Work through related decisions in manageable conversations and write the corresponding files as decisions become clear.

## Start

1. Use the software project open in the coding agent as the target, or the project path explicitly provided by the owner. If the open workspace is this template repository, ask for the target project path before writing; do not create an example project folder by default. Never guess the user's home directory. Keep this repository's example documents unchanged.
2. Before the first write, state the resolved target path. If the workspace directory or target cannot be determined, ask the owner which folder to use. Resolve owner-provided relative paths from the workspace directory and keep later files in that same target unless the owner changes it.
3. Inspect existing project documents and code relevant to the current phase. For a missing document, use the matching file in [assets/](assets/) as a starting structure. Preserve confirmed facts and established terminology.
4. Distinguish confirmed decisions, tentative ideas, and unknowns. Do not turn an example or a suggestion into a requirement unless the owner chooses it.

## Route the Conversation

Start with [product discovery](references/product.md). Once its release scope is clear enough, continue with [requirements](references/requirements.md). Then use [system and interface design](references/system-and-interface.md) for the architecture, API, data, and UI documents that apply. Finish with [delivery planning](references/delivery.md) for engineering, testing, and the release plan. Read only the reference for the current phase.

The phases guide dependencies, not a rigid interrogation. Skip irrelevant documents, revisit earlier decisions when later answers expose a conflict, and continue useful independent work while an answer is pending. Do not move a dependent decision forward on an unconfirmed assumption.

## Working Rules

- Ask small groups of related questions in the owner's language. Use prior answers; explain realistic options briefly when a choice matters. Do not demand that the owner fill a template or answer every section at once.
- Write confirmed decisions into the owning document. Keep unresolved decisions in its Open Questions section with their impact. Do not leave example rows looking like real decisions.
- Keep a single source of truth: product goals in `product.md`, behavior in `requirements.md`, component boundaries in `architecture.md`, contracts in `api.md`, data in `data-model.md`, UI rules in design files, and execution status in `plan.md`.
- When the owner confirms a consequential scope or behavior choice, record its source and affected IDs in `decisions.md`. Use the bundled template when creating the file. Do not log every answer or infer a reason the owner did not give.
- Keep IDs stable and references consistent. Do not mark requirements Verified or Locked, or tasks Done, on the strength of an interview alone.
- After each meaningful phase, summarize what was written and the decisions still needed. The owner can correct the summary conversationally; apply corrections to the files yourself.
- After persisting a coherent documentation change, add a brief entry to the target project's `CHANGELOG.md` (use [the bundled template](assets/CHANGELOG.md) if missing). Put the newest entry first and separate entries with `---`. Record actual file changes, not conversation turns or unconfirmed plans.
- If the target project needs model usage tracking, copy [MONITORING.md](assets/MONITORING.md) and [monitor_usage.py](assets/scripts/monitor_usage.py) into its root and `scripts/` directory. Add `/monitoring/` to its `.gitignore`. Agents may submit provider-reported usage events; missing data stays `Unknown`.
- Before declaring the documentation ready for implementation, check for contradictions, missing must-have behavior, broken references, and plan tasks without requirements. State any remaining open decisions that block implementation.
- Run the installed `docs-audit/scripts/check_docs.py` against the target project when available. Resolve mechanical findings or report them as open; inspect semantic consistency separately.

For a feature added to an already documented project, use `feature-change` instead of restarting discovery. For a standalone consistency review, use `docs-audit`.
