# Testing Strategy

> Fill out this template for each project. Replace bracketed prompts and remove unused sections. This file owns test strategy and execution details; [engineering.md](engineering.md) defines the code-quality workflow and CI gates. Link tests to requirement IDs where behavior is specified.

## 1. Testing Goals and Scope

**Main risks to catch:** [The failures that would matter most to users or the business.]

**Test environments:** [Where each test suite runs and which services or dependencies it needs.]

## 2. Test Levels

| Level | What it verifies | When to use it | Command |
| --- | --- | --- | --- |
| Unit | [Pure logic or focused component behavior] | [Project rule] | [Command] |
| Integration | [Boundaries, storage, external adapters, or contracts] | [Project rule] | [Command] |
| End-to-end | [Critical user journeys] | [Project rule] | [Command] |

> Keep only levels that apply. Choose the lowest level that gives reliable evidence for the behavior, then cover critical journeys end to end when needed.

## 3. Risk-Based Checks

Test levels describe *where* a check runs. Use this table to decide *what risks* need dedicated checks. Keep only categories relevant to the project and link each one to the requirement or quality target it protects.

| Risk area | Behavior or contract to verify | Test level and tool | Requirement or target |
| --- | --- | --- | --- |
| API contracts | [Request, response, schema, or compatibility behavior] | [Level and tool] | [REQ/API ID] |
| Security and permissions | [Access control, input boundaries, or other relevant risk] | [Level and tool] | [REQ/NFR ID] |
| Performance | [Scenario, realistic data volume, and measurable target] | [Level and tool] | [NFR ID or target] |
| Accessibility | [Keyboard, assistive technology, or other applicable behavior] | [Level and tool] | [NFR ID or target] |

> Do not invent performance targets or run every category for every project. Choose checks based on documented risks.

## 4. Requirement and Regression Coverage

| Requirement ID | Behavior to verify | Test location or suite | Notes |
| --- | --- | --- | --- |
| REQ-001 | [Acceptance criterion or important edge case] | [Path or suite] | [Relevant setup or limitation] |

- Add tests for new behavior and meaningful error paths where they protect against a realistic regression.
- When changing shared code or a `Locked` requirement, identify affected requirement IDs and run their relevant tests.
- Do not treat a passing test suite as proof of behavior it does not cover; record uncovered risks.

## 5. Test Data and Isolation

**Data creation:** [How tests create safe, representative data and which fixtures or factories they use.]

**Isolation and cleanup:** [How tests avoid depending on execution order or data left by other tests; specify transactions, disposable stores, cleanup, or equivalent approach.]

**External services:** [Which dependencies are real, simulated, or replaced with controlled test doubles, and why.]

**Sensitive data:** [Rules for avoiding real secrets and personal data in test fixtures and logs.]

## 6. Test Design Rules

- Test observable behavior and contracts rather than mirroring implementation details.
- Keep tests deterministic and independent. Control time, randomness, external services, and shared state where necessary.
- Use readable fixtures and assertions that explain the expected outcome.
- Test authorization, validation boundaries, and failure recovery for behavior where those risks exist.
- Investigate tests that pass only sometimes. Do not treat repeated reruns until a pass as a fix; record the cause and repair or explicitly quarantine the test with an owner and follow-up.

## 7. Execution and CI

**Local quick checks:** [Commands and expected runtime.]

**Full suite:** [Command and when to run it.]

**CI test jobs:** [Which suites run on each change or release.]

**Coverage or quality threshold (if used):** [Threshold and what it means; do not use a metric as a substitute for meaningful assertions.]

## 8. Open Testing Decisions

- [Unresolved test approach, affected requirements, and decision owner if known.]
