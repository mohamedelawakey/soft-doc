# Implementation Plan

> Fill out this template for each release. Replace bracketed prompts, remove unused examples, and update task status as work progresses. This file owns execution order and progress. Product scope belongs in [product.md](product.md), expected behavior in [requirements.md](requirements.md), technical boundaries in [architecture.md](architecture.md), engineering rules in [engineering.md](engineering.md), and test strategy in [testing.md](testing.md). Link to those sources instead of copying their details here.

Use this file as the current release overview. Keep detailed plans for substantial features in [plans/](plans/README.md) and link them from the relevant tasks. Small tasks can be described here without a separate file.

## 1. Plan Scope

**Release or milestone:** [Name or version]

**Outcome:** [What will be usable or delivered when this plan is complete?]

**Requirements covered:** [REQ and NFR IDs]

**Out of scope:** [Work explicitly excluded from this plan; refer to product.md when applicable.]

**Planning assumptions:** [Assumptions that affect order, effort, or scope. Move unresolved decisions to Open Decisions.]

## 2. Delivery Phases

Use phases to group work into reviewable outcomes. Choose phases that fit this project; do not assume a fixed sequence for every system.

| Phase | Outcome / deliverable | Task IDs | Exit condition |
| --- | --- | --- | --- |
| [Phase name] | [What can be reviewed or used] | [TASK IDs] | [How completion is confirmed] |

## 3. Task Index

Keep task IDs stable. Split work so each task has a clear result and can be reviewed. A task may reference several requirements, and a requirement may need several tasks.

| ID | Task | Phase | Priority | Depends on | Requirement IDs | Owner | Reviewer | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-001 | [Action and deliverable] | [Phase] | [Must / Should] | [TASK IDs or None] | [REQ/NFR IDs] | [Person or agent] | [Person or review role] | Not started |

> Statuses: Not started, In progress, Blocked, In review, Done. Use Blocked only with a recorded blocker and next action. Mark Done only when the task's completion checks pass.

## 4. Task Details

### TASK-001: [Action and deliverable]

**Goal and deliverable:** [What concrete result should this task produce?]

**Related requirements:** [REQ/NFR IDs and, when relevant, API/SCR/ENT IDs]

**Dependencies:** [TASK IDs or None; explain external prerequisites if any.]

**Owner:** [Person or agent responsible for delivery.]

**Reviewer:** [Person or role responsible for reviewing the result.]

**Expected areas affected:** [Components, interfaces, or documents likely to change; avoid guessing exact files if unknown.]

**Implementation notes:** [Only decisions needed to carry out this task; link to architecture or design documents for detail.]

**Detailed plan (if needed):** [Link to `plans/REQ-###-short-name.md`, or "None".]

**Completion checks:**

- [ ] [Specific deliverable exists and satisfies the linked acceptance criteria.]
- [ ] [Relevant tests or checks from testing.md pass, including regressions for affected Locked requirements.]
- [ ] [Affected contracts and documentation are updated, if applicable.]

**Status:** [Not started / In progress / Blocked / In review / Done]

**Blocker and next action (if blocked):** [What is preventing progress, who or what can unblock it, and the next step.]

**Result or evidence (when done):** [Link to change, test result, review, or other evidence.]

> Repeat for TASK-002, TASK-003, and so on. Do not use this section to duplicate full requirements or API schemas.

## 5. Dependencies and Critical Path

**Key sequence:** [List the tasks that determine when the release can be completed.]

**External dependencies:** [People, services, approvals, content, or decisions the work depends on.]

**Parallel work (if applicable):** [Tasks that can proceed independently without conflicting changes.]

## 6. Risks and Open Decisions

| ID | Risk or decision | Impact on plan | Owner | Next action / due point | Status |
| --- | --- | --- | --- | --- | --- |
| PLAN-001 | [Risk or unresolved decision] | [Tasks, scope, or timing affected] | [Owner or Unknown] | [Action and when it must be resolved] | Open |

## 7. Progress Log

Keep entries brief and dated. Record changes that affect the next step or explain a plan change; detailed implementation history belongs in version control.

| Date | Completed or changed | Evidence / reason | Next step |
| --- | --- | --- | --- |
| [YYYY-MM-DD] | [Task IDs and result, or plan change] | [Link or brief reason] | [Next task or decision] |

## 8. Release Readiness

Complete this check after the planned tasks are done. Link evidence rather than relying only on task statuses.

- [ ] All Must-have requirements for this release are Verified or Locked, with acceptance criteria checked.
- [ ] Critical user journeys work end to end in the intended environment.
- [ ] Required checks in `engineering.md` and `testing.md` pass, including regression checks for affected Locked requirements.
- [ ] Blocking risks and decisions are resolved, or an explicit release decision records their impact.
- [ ] Required deployment, rollback, monitoring, and support arrangements for this release are ready, if applicable.

**Release decision and evidence:** [Ready / Not ready, decision owner, date, and links to verification results.]

## 9. Plan Change Rules

- Add new features as new requirements and tasks with new IDs. Recheck dependencies and phase exits.
- Keep completed task records for traceability; create a follow-up task for a bug fix or new change instead of silently reopening or rewriting old work.
- Keep completed feature plans for traceability. When their release is no longer active, move them to `plans/archive/` and update links; do not delete them automatically.
- Identify existing `Locked` requirements affected by a new task. Follow the change and regression rules in `requirements.md` before changing their behavior.
- When scope, order, or completion criteria change, update the task details, index, and progress log together.
- Link consequential scope or behavior changes to their entry in [decisions.md](decisions.md), so completed work remains traceable.
