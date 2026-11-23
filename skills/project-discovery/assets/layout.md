# Shared Layout and Navigation

> Define page shells and shared regions here: headers, navigation bars, sidebars, footers, and similar structure. Use tokens from [design.md](design.md), reusable controls from [components.md](components.md), and reference layout IDs from [screens.md](screens.md). Replace bracketed prompts and remove unused sections.

## 1. Layout Index

| ID | Layout | Used by | Purpose |
| --- | --- | --- | --- |
| LAY-001 | [Layout name] | [Screen IDs or page group] | [Why this layout exists] |

## 2. Layout Specification

### LAY-001: [Layout name]

**Regions and order:** [Header, navigation, main content, sidebar, footer, and their reading order.]

**Content container:** [Maximum width, margins, gutters, and spacing rules; reference `design.md` tokens.]

**Responsive behavior:** [How regions move, collapse, or disappear at supported viewports.]

**Accessibility:** [Landmarks, skip link, focus order, and navigation announcement rules.]

> Repeat for each distinct shell, such as public, signed-in, or admin layouts, if the project needs them.

## 3. Shared Regions

### Header

**Applies to:** [Layout IDs]

**Contents and order:** [Brand, actions, account controls, and other content.]

**Responsive and state behavior:** [Mobile behavior, signed-in/out variants, scrolling behavior, and relevant states.]

### Navigation Bar / Sidebar

**Applies to:** [Layout IDs]

| Destination | Label | Visible to | Active-state rule |
| --- | --- | --- | --- |
| [Screen ID or route] | [Label] | [User type or condition] | [When it is active] |

**Responsive and interaction behavior:** [Menu opening, closing, focus, and mobile behavior.]

### Footer

**Applies to:** [Layout IDs]

**Contents and order:** [Links, legal text, contact details, or other content.]

**Responsive behavior:** [How content wraps or reorders.]

> Remove any shared region the project does not use. If a region is a reusable interactive control, give that control a specification in `components.md` and reference it here.

## 4. Open Layout Decisions

- [Unresolved layout or navigation decision, affected layouts, and decision owner if known.]
