# Design Foundations

> Fill out this template for each project. Replace bracketed prompts and remove unused sections. Define shared visual and experience rules here; document reusable UI elements in [components.md](components.md), shared page structure in [layout.md](layout.md), and individual pages in [screens.md](screens.md). Do not invent values when a decision is open.

## 1. Design Goals

| Goal | User or product reason | How to evaluate it |
| --- | --- | --- |
| [Design goal] | [Why it matters] | [Observable result or review method] |

## 2. References and Source of Truth

| Reference | Purpose | Authority |
| --- | --- | --- |
| [Link to Figma, image, brand guide, or other reference] | [What to use it for] | [Exact specification / guidance / inspiration] |

**Conflict rule:** [Which source wins if references disagree? Who decides unresolved conflicts?]

## 3. Visual Tokens

Use semantic names so the intended use is clear. Add actual values for the project; avoid describing a token only as “nice” or “modern.”

### Colors

| Token | Value | Use | Contrast or state notes |
| --- | --- | --- | --- |
| [e.g., color.text.primary] | [Value] | [Where it is used] | [Relevant contrast or state guidance] |

### Typography

| Role | Font family | Size / line height / weight | Use |
| --- | --- | --- | --- |
| [e.g., body] | [Font or token] | [Values] | [Where it is used] |

### Spacing, Shape, and Effects

| Token or rule | Value | Use |
| --- | --- | --- |
| [Spacing, radius, border, shadow, or motion token] | [Value] | [Where it is used] |

**Icons and imagery:** [Style, source, sizing, and usage rules.]

### Themes (if applicable)

**Supported themes:** [Light, dark, system preference, or other themes. Write "One theme" if switching is not supported.]

**Theme selection:** [How the initial theme is chosen, whether users can change it, and whether the choice is saved.]

| Semantic token | [Theme name] value | [Other theme name] value |
| --- | --- | --- |
| [e.g., color.surface.primary] | [Value] | [Value] |

> Keep the same semantic token names across themes. Remove the extra column if the product has only one theme.

## 4. Responsive Design

**Supported viewports and devices:** [List the intended range.]

| Breakpoint or condition | Layout behavior | Navigation behavior | Content behavior |
| --- | --- | --- | --- |
| [Width or device condition] | [Columns, widths, spacing] | [How navigation changes] | [Reflow, truncation, hiding, or scrolling rules] |

> Describe behavior at each size, not only breakpoint numbers. Shared header, navigation, sidebar, and footer details belong in [layout.md](layout.md).

## 5. Interaction and Feedback Principles

- **Feedback:** [How the UI confirms actions and reports progress or failure.]
- **Focus and keyboard use:** [How focus is shown and how interactive elements are reached.]
- **Motion:** [When animation is used, its purpose, and reduced-motion behavior.]
- **Touch and pointer:** [Minimum target guidance and hover-independent behavior, if applicable.]

## 6. Content and Localization

**Supported languages and direction:** [Languages, left-to-right or right-to-left needs.]

**Voice and terminology:** [Tone, terms to use consistently, and terms to avoid.]

**Formatting:** [Dates, times, numbers, currency, and other locale-sensitive display rules.]

## 7. Accessibility Baseline

- **Contrast:** [Target standard or project-specific requirements.]
- **Text and zoom:** [Expected behavior when text is enlarged.]
- **Forms and errors:** [Labeling and error announcement expectations.]
- **Non-text content:** [Alternative text and decorative-image rules.]

## 8. Open Design Decisions

- [Unresolved decision, its impact, and who will decide it if known.]
