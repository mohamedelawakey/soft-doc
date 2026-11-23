# Requirements

> Fill out this template for each project. Replace text in square brackets and duplicate the requirement section for every feature or distinct behavior. Remove instructions and unused placeholders when complete. Record unresolved behavior under "Open Questions" rather than letting an implementer guess.

## 1. Scope and References

**Release:** [Name or version of the release covered by this document]

**Product context:** See [product.md](product.md) for users, goals, and release scope.

> Include only requirements for the release described in `product.md`. Keep design details in `design.md`, API contracts in `api.md`, and implementation choices in `architecture.md`.

## 2. Requirements Index

Use stable IDs so tasks, tests, and discussions can refer to the same requirement. Use the same priorities as `product.md`.

| ID | Requirement | Priority | User type | Status |
| --- | --- | --- | --- | --- |
| REQ-001 | [Short name] | Must have | [User type] | Draft |

> Statuses: Draft → Approved → Implemented → Verified → Locked. Use `Verified` after the acceptance criteria pass. Use `Locked` only after the completed behavior has been reviewed and accepted. Update status only when the corresponding step has actually happened.

### Change and Regression Rules

- Keep requirement IDs stable. Add a new ID for a new feature; do not silently rewrite an existing requirement.
- Treat `Locked` requirements as protected behavior. Do not change their expected behavior as part of unrelated work.
- A bug fix may touch a locked feature to restore its documented behavior. Record the bug and verify the affected acceptance criteria again.
- If a new feature needs to change a locked feature, document the proposed behavior change and get a product decision before implementing it. Record the affected requirement IDs and update their acceptance criteria.
- Record consequential confirmed behavior changes in [decisions.md](decisions.md), including the decision source, affected IDs, and verification impact. A clear owner request is a decision; do not add a redundant approval step.
- After any change that touches code used by an existing requirement, run the relevant regression checks. A `Locked` status alone does not prove that the behavior still works.

## 3. Functional Requirements

### REQ-001: [Short, action-oriented name]

**User type:** [Who uses or triggers this behavior?]

**Goal:** [What outcome does the user need?]

**Priority:** [Must have / Should have]

**Dependencies (if any):** [IDs of requirements that must be completed first, or "None".]

**Affected existing requirements (if any):** [IDs whose implementation or expected behavior may be affected, or "None". Explain any intended behavior change before implementation.]

**Preconditions:**

- [What must already be true before this flow begins? Write "None" if there are no preconditions.]

**Trigger:** [What action or event starts the flow?]

**Inputs and outputs (if applicable):**

- **Inputs:** [Information or actions supplied by the user or another system. Include required fields and meaningful limits; leave exact data schemas to `data-model.md` or `api.md`.]
- **Outputs:** [Information, confirmation, or other result the user or another system receives.]

**Main flow:**

1. [User action or system event.]
2. [Expected system behavior.]
3. [Result visible to the user or another system.]

**Business rules and permissions:**

- [Rule, limit, calculation, or condition that changes the outcome.]
- [Who may perform this action? Who may not?]

**State changes (if applicable):**

- [Starting state] → [Resulting state]: [Trigger, conditions, and who is allowed to cause the change.]

**Error and edge cases:**

- **[Condition]:** [Expected behavior and what the user sees, if applicable.]

**Acceptance criteria:**

- [ ] Given [starting state], when [action], then [observable result].
- [ ] Given [invalid or restricted state], when [action], then [observable result].

> Repeat this entire section for REQ-002, REQ-003, and so on. Keep each requirement small enough that its behavior and acceptance criteria can be reviewed together.

## 4. Cross-Cutting Requirements

Use this section for behavior that applies to several features. Give each item a stable ID and measurable acceptance criteria. Add only categories relevant to the project.

| ID | Area | Requirement | Acceptance criterion |
| --- | --- | --- | --- |
| NFR-001 | [Accessibility / Performance / Security / Reliability / Localization / Other] | [Specific expected behavior or constraint] | [How will it be verified? Include a target when applicable.] |

## 5. Open Questions

- [Unresolved behavior or rule? Who will decide, if known? Which requirement does it affect?]
