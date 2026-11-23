# Requirements Discovery

Read the filled `docs/product.md` and existing `docs/requirements.md`. Use `assets/requirements.md` if the latter is absent. Turn each in-scope capability into one or more reviewable `REQ-###` items; use `NFR-###` for measurable requirements spanning features.

For each feature, ask only for missing decisions about actor and goal, trigger and preconditions, main flow, inputs and outputs, business rules, permissions, state changes, errors and edge cases, and dependencies. Ask how success or failure can be observed. Break a large feature into multiple requirements when one set of acceptance criteria would be hard to review together.

Write acceptance criteria as observable outcomes, including meaningful denied or invalid cases. Keep API transport, exact schema, UI styling, and code structure in their own documents. Use stable IDs, link each must-have capability from `product.md`, and record undecided behavior under Open Questions. Draft is the default status until the owner actually approves behavior; do not claim implementation, verification, or locking from conversation alone.

Before moving on, check that each must-have capability has a corresponding requirement and that scope, priority, actors, and exclusions agree with `product.md`.
