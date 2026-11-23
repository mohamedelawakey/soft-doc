# UI Components

> Define reusable UI elements once here. Use visual tokens from [design.md](design.md), shared page structure from [layout.md](layout.md), and reference component IDs from [screens.md](screens.md). Replace bracketed prompts, remove unused examples, and add a section for each component used by the project.

## 1. Component Index

| ID | Component | Purpose | Used on |
| --- | --- | --- | --- |
| CMP-001 | [Component name] | [What it helps users do or understand] | [Screen IDs or “Shared”] |

## 2. Component Specification

### CMP-001: [Component name]

**Purpose:** [What is this component for?]

**Anatomy:** [Visible parts, labels, icons, and optional parts.]

**Variants:** [Variants and when each should be used; write “None” if there are no variants.]

**Sizes and layout:** [Dimensions, spacing, alignment, wrapping, and responsive behavior. Reference tokens from `design.md` where possible.]

**Interaction:** [What happens on click, touch, keyboard input, or other actions. Link to requirement IDs for business behavior.]

**States:**

| State | Appearance | Behavior or message |
| --- | --- | --- |
| Default | [Visual treatment] | [Expected behavior] |
| Hover / focus | [Visual treatment] | [Expected behavior] |
| Disabled / loading / error / success | [Visual treatment, where applicable] | [Expected behavior or feedback] |

**Accessibility:** [Name, role, focus behavior, keyboard behavior, and screen-reader announcements as applicable.]

**Content rules:** [Label length, icon-only use, helper text, or other copy constraints.]

**Do / avoid:** [Usage guidance that prevents inconsistent use.]

> Repeat this section for buttons, fields, cards, lists, tables, dialogs, notifications, and other reusable elements needed by the project. Only document states that apply.

## 3. Shared Form Behavior (if applicable)

**Validation timing:** [When are fields validated: while typing, on blur, on submit, or a defined combination?]

**Field errors:** [Where error messages appear, how they are announced, and when they clear.]

**Submission:** [How the form behaves during submission, including loading, duplicate submissions, and success feedback.]

**Submission failure:** [How form-level errors appear, whether entered values remain, and how the user retries.]

> Describe shared presentation and interaction here. Field rules and business validation belong in `requirements.md`.

## 4. Open Component Decisions

- [Unresolved component choice, affected IDs, and decision owner if known.]
