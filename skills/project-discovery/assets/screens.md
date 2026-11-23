# Screens and Pages

> Define each user-facing screen here. Reference functional behavior by ID from [requirements.md](requirements.md), shared layouts from [layout.md](layout.md), reusable elements from [components.md](components.md), and visual rules from [design.md](design.md). Do not duplicate definitions owned by those files. Replace bracketed prompts and repeat the screen section as needed.

## 1. Screen Index

| ID | Screen | Route or entry point | User types | Layout | Requirement IDs |
| --- | --- | --- | --- | --- | --- |
| SCR-001 | [Screen name] | [Path or navigation entry] | [Who can access it] | [LAY ID] | [REQ IDs] |

## 2. Screen Specification

### SCR-001: [Screen name]

**Purpose:** [What task does this screen help the user complete?]

**Entry and access:** [How users reach it; any access conditions. Link to requirement IDs for authorization rules.]

**Access states (if applicable):**

| Condition | What the user sees | Next action or destination | Requirement ID |
| --- | --- | --- | --- |
| Not signed in | [Message, redirect, or public view] | [Sign-in path or other action] | [REQ ID] |
| No permission | [Message or restricted view] | [Safe destination or other action] | [REQ ID] |

> Remove rows that cannot occur. Authorization rules belong in `requirements.md`; this table describes how the screen presents their outcomes.

**Layout:** [LAY ID and any screen-specific arrangement.]

**Content hierarchy:**

1. [First section and its purpose.]
2. [Next section and its purpose.]
3. [Primary action and where it appears.]

**Components:** [CMP IDs used here and any screen-specific configuration.]

**User actions and destinations:**

| Action | Result or destination | Requirement ID |
| --- | --- | --- |
| [Action] | [Visible result or target screen] | [REQ ID] |

**Screen states:**

| State | What the user sees | Available actions |
| --- | --- | --- |
| Initial / default | [Content] | [Actions] |
| Loading | [Progress treatment] | [Actions allowed] |
| Empty | [Message and guidance] | [Recovery or primary action] |
| Error | [Message and recovery option] | [Retry or other action] |
| Success | [Confirmation or updated content] | [Next action] |

**Responsive notes:** [Only behavior specific to this screen; shared rules belong in `design.md` and `layout.md`.]

**Accessibility notes:** [Only screen-specific focus, announcements, or reading-order details.]

**Reference:** [Link to approved mockup or screenshot, if available.]

> Repeat for SCR-002, SCR-003, and so on. Remove states that cannot occur on a screen.

## 3. Open Screen Decisions

- [Unresolved screen decision, affected screen IDs, and decision owner if known.]
