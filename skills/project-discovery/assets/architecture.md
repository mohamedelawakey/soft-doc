# System Architecture

> Fill out this template for each project. Replace text in square brackets and remove unused prompts. Record decisions based on the project's requirements; this template does not prescribe a technology stack. Keep the directory and file layout in a separate project structure document.

## 1. System Overview

**Summary:** [Describe the system's main parts and how they work together in a few sentences.]

**Architecture diagram (optional):** [Add a diagram or link when it makes the system easier to understand.]

**Relevant requirements:** [Link to the requirements or product goals that drive the architecture.]

## 2. Architecture Drivers and Constraints

List the needs that shape the design, such as user volume, reliability, security, deployment environment, or external dependencies. Use measurable values when known; do not invent targets.

| Driver or constraint | Source | Architectural impact |
| --- | --- | --- |
| [Need or constraint] | [Requirement ID, product decision, or external obligation] | [How it affects the design] |

## 3. Components and Responsibilities

Describe the major runtime components and their boundaries. State where business rules and authoritative decisions live.

| Component | Responsibility | Owns or manages | Communicates with |
| --- | --- | --- | --- |
| [Component name] | [What it does] | [Data, decisions, or processes it owns] | [Other components or systems] |

## 4. Interactions and Data Flow

Describe the path of each important user action or system event across components. Link to detailed API contracts elsewhere when applicable.

### [Flow name]

**Trigger:** [What starts the flow?]

1. [Component or actor] → [component]: [What is sent or requested?]
2. [Component] → [component]: [What happens next?]
3. [Component] → [actor or component]: [What is returned or changed?]

**Failure path:** [Where can the flow fail, and which component handles the failure?]

## 5. Data Ownership and Consistency

**Source of truth:** [Which component or store owns each important kind of data?]

**Data lifecycle:** [How is data created, updated, retained, and deleted at a high level?]

**Consistency needs:** [Which operations must be immediately consistent? Where, if anywhere, is delayed consistency acceptable?]

> Put schemas, fields, and relationships in `data-model.md`.

## 6. Cross-Cutting Design

Fill in only the topics that apply to this system.

- **Identity and authorization:** [Where are users identified, and where are access decisions enforced?]
- **Error handling:** [How do components detect, communicate, and recover from failures?]
- **Security and privacy:** [How are sensitive data and trust boundaries handled?]
- **Background work and events:** [What runs asynchronously, and how are retries or duplicate events handled?]
- **Observability:** [What logs, metrics, or traces are needed to diagnose important failures?]
- **Performance and scaling:** [What are the expected bottlenecks and planned responses, if known?]

## 7. External Systems and Dependencies

| System or service | Purpose | Data exchanged | Failure or availability consideration |
| --- | --- | --- | --- |
| [External dependency] | [Why it is needed] | [What crosses the boundary] | [What happens if it is unavailable] |

## 8. Runtime and Deployment Overview

**Environments:** [Which environments exist, such as development, staging, and production?]

**Runtime units:** [What processes or services run, and how are they connected?]

**Configuration and secrets:** [Where configuration comes from and how secrets are supplied, without listing secret values.]

**Deployment constraints:** [Hosting, networking, regional, or operational constraints that affect the design.]

## 9. Technology Choices and Decisions

Record the choices made for this project, their reasons, and the requirements they support. Leave undecided choices under "Open Questions".

| Decision | Choice | Reason and trade-off | Related requirements |
| --- | --- | --- | --- |
| [Decision topic] | [Selected approach or technology] | [Why this fits; important trade-off] | [Requirement IDs] |

## 10. Open Questions

- [Unresolved architecture decision? What information or owner is needed to decide?]
