# API Contracts

> Fill out this template for each project. Choose the API style or styles the system actually uses, then keep only the relevant operation formats below. Replace bracketed prompts and remove unused examples. Give every operation a stable `API-###` ID and link it to its `REQ-###` requirements. Do not assume REST, GraphQL, SOAP, or any other style by default.

## 1. API Overview

**Purpose and consumers:** [Which components or external clients use this API, and for what purpose?]

| Interface | Style or protocol | Consumers | Contract source |
| --- | --- | --- | --- |
| [Interface name] | [REST / GraphQL / SOAP / other] | [Who calls it] | [This file, OpenAPI, GraphQL schema, WSDL, or other authoritative reference] |

**Base address or connection point:** [Base URL, endpoint, transport, or environment-specific reference. Do not include secrets.]

**Version and compatibility policy:** [How versions are identified, what changes are compatible, and how breaking changes are introduced.]

## 2. Shared Contract Rules

**Authentication:** [How callers identify themselves, if required.]

**Authorization:** [Where access is enforced and how permission failures are represented. Link to relevant requirements.]

**Data format and naming:** [JSON, XML, scalar formats, naming conventions, timestamps, IDs, nullability, and encoding as applicable.]

**Error format:** [Common error shape and how callers distinguish validation, access, missing data, and server failures.]

**Pagination, filtering, and sorting (if applicable):** [Shared rules, defaults, limits, and response metadata.]

**Retries and duplicate requests (if applicable):** [Which operations may be retried and how duplicate effects are prevented.]

**Rate limits or timeouts (if applicable):** [Documented limits and caller behavior.]

## 3. Operation Index

| ID | Operation | Interface / style | Related requirement | Status |
| --- | --- | --- | --- | --- |
| API-001 | [Short operation name] | [Interface / style] | [REQ ID] | Draft |

> Keep IDs stable. Suggested statuses: Draft, Approved, Implemented, Verified. Update existing contracts explicitly when behavior changes.

## 4. Operation Contracts

Copy the relevant format below for each operation. Keep the common fields, then use only the fields for that operation's API style. If a project uses multiple styles, repeat this section for each operation across all styles.

### API-001: [Action and resource or operation name]

**Interface / style:** [REST / GraphQL / SOAP / other]

**Related requirements:** [REQ IDs]

**Purpose:** [What this operation lets a caller accomplish.]

**Caller and authorization:** [Who may call it and what access is required.]

**Trigger or usage:** [When a client should call it.]

**Request:** [Required and optional inputs, types, validation, defaults, and a representative example or link to a schema.]

**Success result:** [Result shape, important fields, and a representative example or link to a schema.]

**Errors:** [Each expected failure condition, its protocol-specific representation, and whether retrying makes sense.]

**Rules and side effects:** [Business constraints, data changes, ordering, and duplicate-request behavior.]

**Related contracts:** [Shared type IDs, schema links, or other operations this one depends on.]

**Examples:** [For operations with nontrivial inputs, outputs, or errors, include one complete successful request and response plus one representative error. For simple operations, a concise example or authoritative schema link is enough. Use the format of this operation's API style.]

```text
[Successful request or invocation]

[Successful response or result]

[Representative failed request or condition]

[Error response, fault, or failure result]
```

#### REST fields (use only for REST operations)

**Method and path:** [e.g., GET /resource]

**Path, query, and header parameters:** [Name, type, required/optional, validation, and default for each.]

**Request body:** [Media type and schema or “None”.]

**Success status and response:** [HTTP status, media type, and body or “No body”.]

**Error statuses:** [HTTP status → condition → response body.]

#### GraphQL fields (use only for GraphQL operations)

**Operation type and name:** [Query / mutation / subscription and name.]

**Variables:** [Names, types, required/optional, validation, and defaults.]

**Selection or payload:** [Returned fields or payload type; link to the authoritative schema.]

**GraphQL errors:** [Error conditions, `errors` details or extensions, and any partial-data behavior.]

#### SOAP fields (use only for SOAP operations)

**Service and operation:** [Service name, operation name, and WSDL reference.]

**Binding and endpoint:** [Binding, protocol, and endpoint reference.]

**Request message:** [XML element/type, required fields, and example or schema reference.]

**Response message:** [XML element/type and example or schema reference.]

**Faults:** [Fault code and detail for each expected failure.]

#### Other interface fields (use for other styles)

**Transport and operation identifier:** [How the caller addresses or invokes the operation.]

**Message or request format:** [Schema, required fields, and example.]

**Result or acknowledgement format:** [Schema, timing, and delivery behavior.]

**Failure representation:** [How failures are reported and handled.]

> Repeat the operation contract as API-002, API-003, and so on. Remove all style-specific subsections that do not apply to each operation.

## 5. Shared Data Types

Define types reused by multiple operations, or link to the authoritative machine-readable schema. Keep domain relationships and persistence details in `data-model.md`.

### TYPE-001: [Type name]

| Field | Type | Required / nullable | Meaning and constraints |
| --- | --- | --- | --- |
| [Field name] | [Type] | [Rule] | [Meaning, format, and allowed values] |

## 6. Contract Changes and Open Questions

**Change record:** [List changes that affect existing consumers, the affected API IDs, and the compatibility or migration plan.]

**Open questions:**

- [Unresolved contract decision, affected API IDs, and decision owner if known.]
