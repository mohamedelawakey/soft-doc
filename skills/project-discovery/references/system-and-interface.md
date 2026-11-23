# System and Interface Decisions

Read the filled requirements and only the target documents relevant to this system. Use matching files in `assets/` when absent. Ask about consequences and constraints before choosing a technology or pattern; the owner may delegate a choice to the developer, in which case document the decision and rationale when made.

- `architecture.md`: identify components, responsibilities, trust boundaries, significant flows, data ownership, external services, runtime needs, and technology decisions. Do not put the directory tree here.
- `api.md`: create this when components or clients need a documented interface. Let the owner or developer choose REST, GraphQL, SOAP, or another style. Define shared rules and one `API-###` contract per operation, linked to requirements. Keep only the fields for the chosen style and include representative examples where they clarify the contract.
- `data-model.md`: define the data the system owns, logical entities and fields, relationships, invariants, lifecycle, access patterns, and meaningful `FLOW-###` data flows. Keep storage technology choices in architecture.
- UI documents: if there is a user-facing interface, define shared tokens and interaction rules in `design.md`, reusable elements in `components.md`, shared shells in `layout.md`, and page-specific behavior in `screens.md`. Link `SCR-###` entries to `REQ-###` and reuse `CMP-###` and `LAY-###` IDs rather than copying definitions.

Ask short, related questions for each applicable document. Skip irrelevant sections and do not invent design values, integrations, security policies, performance targets, or data retention periods. Surface contradictions with requirements for a product decision. Review cross-document IDs and ownership boundaries before delivery planning.
