# Data Model

> Fill out this template for each project. Replace bracketed prompts, repeat sections as needed, and remove unused guidance. Describe domain data and its rules without assuming SQL, NoSQL, or another storage technology. Link behavior to [requirements.md](requirements.md), API representations to [api.md](api.md), and component-level flow to [architecture.md](architecture.md). Record unresolved decisions under "Open Questions" instead of guessing.

## 1. Data Overview

**Summary:** [What important information does the system create, store, or exchange?]

**Data boundaries:** [Which data is owned by this system, and which is only received from or referenced in external systems?]

## 2. Entity Index

| ID | Entity or record | Purpose | Source of truth | Related requirements |
| --- | --- | --- | --- | --- |
| ENT-001 | [Entity name] | [What it represents] | [Owning component or external system] | [REQ IDs] |

## 3. Entity Specifications

### ENT-001: [Entity name]

**Meaning:** [What one record represents in the product domain.]

**Identity:** [How a record is uniquely identified.]

| Field | Meaning | Type or format | Required / nullable | Default | Validation or allowed values |
| --- | --- | --- | --- | --- | --- |
| [Field name] | [Business meaning] | [Logical type or format] | [Rule] | [Value or None] | [Limits or allowed values] |

**Uniqueness and invariants:** [Rules that must always remain true for this entity.]

**Ownership and permissions:** [Who can create, view, change, or delete it? Link to requirement IDs for detailed authorization rules.]

**Lifecycle:** [When it is created, updated, archived, deleted, or restored.]

> Repeat for ENT-002, ENT-003, and so on. Keep API-only response fields in `api.md` unless they also represent domain data.

## 4. Relationships

| From | Relationship | To | Cardinality | Required? | On deletion or separation |
| --- | --- | --- | --- | --- | --- |
| [ENT ID] | [Relationship meaning] | [ENT ID] | [One-to-one / one-to-many / many-to-many / other] | [Yes / No] | [Restrict, detach, cascade, preserve history, or other rule] |

**Relationship diagram (optional):** [Add a diagram or link if the relationships are easier to understand visually.]

## 5. Cross-Entity Rules

- [Rule that must remain true across multiple entities, with related ENT and REQ IDs.]

**Atomic changes (if applicable):** [Which related updates must succeed or fail together? Describe the business need; implementation details belong in `architecture.md`.]

## 6. Data Flows and Lifecycle

Document meaningful data movement and changes, especially creation, external import/export, sensitive data use, archival, and deletion. This section follows the data; `architecture.md` describes component interactions.

### FLOW-001: [Flow name]

**Related requirements:** [REQ IDs]

**Data involved:** [ENT IDs and important fields or categories.]

**Trigger and origin:** [What starts the flow, and where does the data come from?]

| Step | Data action | Result or destination | Validation / access rule |
| --- | --- | --- | --- |
| 1 | [Collected, created, read, transformed, shared, updated, archived, or deleted] | [What changes or receives the data] | [Checks and who may perform them] |

**Failure and recovery:** [What happens to the data if a step fails or is repeated?]

**End of life:** [When the data is retained, archived, anonymized, or deleted.]

> Repeat for FLOW-002 and later flows. Do not repeat low-level API calls or every field assignment unless they change a domain rule.

## 7. Access Patterns (if applicable)

Describe important reads and searches so storage design can support real usage. Record the required behavior here; physical indexes and query implementation belong in the technical design.

| Pattern | Data involved | Filter / sort / grouping | Expected scale or frequency | Related requirement |
| --- | --- | --- | --- | --- |
| [e.g., list a user's recent records] | [ENT IDs] | [Criteria and ordering] | [Known volume or "Unknown"] | [REQ ID] |

## 8. Derived Data and Change History (if applicable)

### Derived Data

| Value | Source data | Calculation or update rule | Stored or calculated on demand? | Related requirement |
| --- | --- | --- | --- | --- |
| [Calculated value] | [Fields or ENT IDs] | [Exact rule, including rounding or timing if relevant] | [Choice or "Undecided"] | [REQ ID] |

### Change History

**Changes to record:** [Which entities, fields, or events need a history? Write "None" if not required.]

**History details:** [Who changed what, when, previous/new values, and any reason or source that must be captured.]

**Access and retention:** [Who can view the history and how long it is kept.]

## 9. Sensitive Data and Retention

| Data category or field | Classification | Access or protection rule | Retention / deletion rule | Related requirement |
| --- | --- | --- | --- | --- |
| [Data] | [Public / internal / personal / sensitive, as applicable] | [Who may access it and relevant protection expectations] | [Duration or event; write "Undecided" if not set] | [REQ ID] |

## 10. Existing Data and Migrations (if applicable)

**Current state:** [Describe existing data or write "New system; no existing data".]

**Proposed change:** [What data shape or rule changes?]

**Migration and verification:** [How existing records will be transformed, checked, and recovered if migration fails.]

## 11. Open Questions

- [Unresolved data decision, affected ENT/FLOW/REQ IDs, and decision owner if known.]
