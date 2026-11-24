# Soft Doc

Markdown templates and agent skills for defining, planning, building, and maintaining software projects. This repository is a **toolkit**, not an application or a finished project. The files in `docs/` are blank templates; their placeholders are not project decisions.

## Use the skills in your project

Open **your software project** in your coding agent. Install the eight folders inside this repository's `skills/` into your project's `.agents/skills/` for Codex. Each skill already carries the templates, references, and scripts it uses. Other agents may use a different skills directory. Do not copy this whole repository over the root of your project.

Clone this repository **beside** your project. Replace `/path/to/your-project` with the real path. This copies all eight complete skill folders and skips any same-name skill already present:

```bash
git clone https://github.com/mohamedelawakey/soft-doc.git soft-doc
project=/path/to/your-project
mkdir -p "$project/.agents/skills"
for skill in soft-doc/skills/*; do
  name=${skill##*/}
  if [ -e "$project/.agents/skills/$name" ] || [ -L "$project/.agents/skills/$name" ]; then
    printf 'Skipped existing skill: %s\n' "$name"
  else
    cp -R "$skill" "$project/.agents/skills/"
  fi
done
```

```text
your-project/
├── docs/                  # this project's documents, created or updated by the skills
└── .agents/skills/        # eight complete skill folders
```

The skills read and update **the project's** `docs/` when needed. They use their bundled `assets/`, `references/`, and `scripts/`; the top-level `docs/` and `scripts/` of this source repository are not required for these workflows and are not copied by this command. The templates inside skill packages stay unchanged while the project's documents are updated. Start a new agent session in your project after installation. If the agent does not discover a skill, point it to `.agents/skills/<skill-name>/SKILL.md`.

In this source repository, edit reusable document templates in `docs/`. Run `python3 scripts/sync_skill_assets.py` to refresh the portable copies under `project-discovery/assets/`, then `python3 scripts/sync_skill_assets.py --check` to confirm they match. The same sync covers the monitoring template and recorder script. This is a maintainer step; users of an installed skill do not need to run it.

`build-project` can call `plan-project` when the project has no usable plan; install both for that flow. `sync-project-docs` uses `understand-project` and `update-project-docs`; install all three together.

## Conversation-Driven Workflows

These skills let a project owner make decisions in conversation while the agent writes and maintains the Markdown:

| Skill | Use it for |
| --- | --- |
| [project-discovery](skills/project-discovery/SKILL.md) | Interview the owner and build the project-specific product, requirements, technical, UI, engineering, testing, and plan documents. It uses the bundled templates when a document is missing. |
| [plan-project](skills/plan-project/SKILL.md) | Turn approved requirements and current project evidence into an executable release plan, with detailed plans for substantial features. |
| [build-project](skills/build-project/SKILL.md) | Build a documented project or release in working slices, using its engineering and testing rules for code quality, performance, security, and verification. |
| [feature-change](skills/feature-change/SKILL.md) | Add a feature, revise agreed behavior, or document a bug fix while tracking affected existing requirements and plans. |
| [docs-audit](skills/docs-audit/SKILL.md) | Review links, IDs, coverage, contradictions, and completion evidence across the documentation. |
| [understand-project](skills/understand-project/SKILL.md) | Inspect an existing project in manageable parts and write an evidence-linked report and source-fingerprint register with coverage status. |
| [update-project-docs](skills/update-project-docs/SKILL.md) | Check evidence freshness, draft supported updates to an existing project's documents, review the proposed diff with the owner, then apply the approved files. |
| [sync-project-docs](skills/sync-project-docs/SKILL.md) | Run project understanding and evidence-backed documentation drafting in one request, then present one proposal for review. |

The owner supplies decisions in conversation; the agent updates the files. The `skills/` directory contains the source packages. This repository also exposes them through `.agents/skills/` for agents that support that project-level convention. If your agent does not discover them automatically, point it to the relevant `SKILL.md` file.

Before granting an agent access to a project, read the [security policy](SECURITY.md) for guidance on permissions, untrusted content, and handling secrets.

## Common workflows

Start your agent **inside the target project**. These are example requests; the owner supplies product decisions in conversation while the agent updates the relevant files.

Define a new project:

```text
Use the project-discovery skill to help define this project. My idea is: [your idea].
```

`project-discovery` writes into the project open in the agent, or an explicit project path you provide. If you run it from this template repository, it asks for the target project path before writing. `./booking-demo/` was only an illustrative child-folder name in older instructions; it is not a generated folder or an executable script.

Plan or build an approved release:

```text
Use the plan-project skill to turn the approved requirements into an executable release plan.
Use the build-project skill to implement the current release. Follow my plan if I have one; otherwise create one first. Run the relevant project checks.
```

Change an existing feature or inspect an existing codebase:

```text
Use the feature-change skill to add [feature] to this release and update the affected requirements and plan.
Use the understand-project skill to inspect this project and write an evidence-linked report.
```

Synchronize documentation with existing code:

```text
Use the sync-project-docs skill to inspect the project and prepare one reviewable documentation update. Show me the proposed changes before applying them.
```

That workflow writes an understanding report, file map, and evidence register. It stages proposed document changes in `.docs-review/` and applies them after the owner reviews the concrete draft. `docs-audit` can separately report broken links, inconsistent IDs, coverage gaps, and unsupported completion claims; ask it to fix confirmed findings if edits are wanted.

## Use the templates manually

If you prefer not to install skills, copy only the documents your project needs from [docs/](docs/) and fill them with real decisions. Start with [product](docs/product.md), [requirements](docs/requirements.md), [architecture](docs/architecture.md), [engineering](docs/engineering.md), [testing](docs/testing.md), and [plan](docs/plan.md). The other files cover API, data, design, screens, and components when relevant. Keep completed changes in [CHANGELOG.md](CHANGELOG.md); [AGENTS.md](AGENTS.md) is a starting point for project-specific agent guidance.

| Document | Source of truth for |
| --- | --- |
| [Product](docs/product.md), [requirements](docs/requirements.md), [decisions](docs/decisions.md) | Users and scope; testable behavior and IDs; reasons for consequential changes. |
| [Architecture](docs/architecture.md), [API](docs/api.md), [data model](docs/data-model.md) | Boundaries, interfaces, and data. |
| [Design](docs/design.md), [components](docs/components.md), [layout](docs/layout.md), [screens](docs/screens.md) | Visual rules and user-facing flows when applicable. |
| [Engineering](docs/engineering.md), [testing](docs/testing.md) | Project conventions, commands, quality gates, and verification. |
| [Plan](docs/plan.md), [feature plans](docs/plans/README.md) | Current release tasks and detailed work when needed. |
| [File map](docs/file-map.md), generated project understanding | Observed repository layout and evidence-backed findings. |
| [Changelog](CHANGELOG.md), [monitoring](MONITORING.md) | Completed changes; measured model usage and estimated cost. |

Requirements progress from `Draft` to `Approved`, `Implemented`, `Verified`, and `Locked`. A status is not proof of a passing check. Keep stable IDs across requirements, contracts, tasks, and decisions; archive old completed feature plans rather than deleting their history.

The [monitoring template](MONITORING.md) and [usage recorder](scripts/monitor_usage.py) can log provider-reported model requests and calculate estimated token cost from dated rate snapshots. They cannot read hidden usage from every agent or determine a final bill. See the monitoring file for the event format.

## Repository checks and releases

Run the documentation checker on a project with these templates:

```bash
python3 skills/docs-audit/scripts/check_docs.py /path/to/project
```

The checker catches mechanical issues such as broken local links, duplicate IDs, and missing plan references. It cannot judge whether a requirement is sensible or whether a claimed test actually ran.

The [understanding evidence tool](skills/understand-project/scripts/evidence_trace.py) records source fingerprints. After code changes, run `python3 .agents/skills/understand-project/scripts/evidence_trace.py check .` in a project with the skill installed to flag stale findings; `impact .` lists affected observations and documents. A clean fingerprint check means the cited files are unchanged, not that every interpretation is correct.

The [impact benchmark](benchmarks/RESULTS.md) has 18 controlled cases using Click, Requests, and Flask source copies. It tests the evidence tool's change detection and document matching, not complete skill quality or generated project correctness. The [benchmark script](benchmarks/impact_benchmark.py) and [recorded results](benchmarks/results-2026-11-23.json) are included; reruns need separate checkouts of those projects.

This repository's GitHub workflow publishes a release on every push to `main`, including a merged pull request. Tags use `v1.0.<workflow run number>` and release notes come from GitHub. Other branches do not publish releases. The workflow does not create release branches or edit the changelog. Read [SECURITY.md](SECURITY.md) before granting an agent access to a project.

## License

The templates are licensed under [CC BY 4.0](LICENSE). You may adapt them, including commercially; credit **mohamedelawakey**, link to the license and original repository when sharing, and indicate changes.

Example attribution: “Documentation templates adapted from [soft-doc](https://github.com/mohamedelawakey/soft-doc) by mohamedelawakey, licensed under CC BY 4.0. Changes were made for this project.”
