# Engineering Standards

> Fill out this template for each project. Replace bracketed prompts and remove rules that do not apply to its language or runtime only after documenting the reason. These rules apply to all new and changed code. Product behavior belongs in [requirements.md](requirements.md), system boundaries in [architecture.md](architecture.md), and test strategy in [testing.md](testing.md). Directory layout belongs in a separate project-structure document.

## 1. Project Conventions and Commands

**Languages and versions:** [Languages and supported versions.]

**Formatter:** [Tool and command.]

**Linter / static analysis:** [Tools and commands.]

**Type checker (if applicable):** [Tool and command.]

**Build or compile command:** [Command.]

**Testing:** See [testing.md](testing.md) for test levels, commands, and coverage of changed behavior.

## 2. Readability and Simplicity

- Write code that a maintainer can understand from its names, structure, and nearby context.
- Prefer the simplest implementation that satisfies the documented requirement. Avoid unused code, speculative abstractions, and clever shortcuts that make behavior harder to review.
- Keep each module, function, and class focused on one clear responsibility. Separate unrelated behavior.
- Make control flow explicit. Limit nesting and split complex conditions into well-named concepts.
- Remove dead code and obsolete paths when replacing behavior, subject to the project's compatibility requirements.

## 3. Naming and Variables

**Naming convention:** [Language-specific rules for files, classes, functions, variables, constants, and tests.]

- Use names that reveal what a value represents and, when useful, its unit or state.
- Do not use vague names such as `x`, `data`, or `temp`, including loop variables, when the value has a meaningful role. Standard short names are allowed only where the meaning is unmistakable in a very small scope.
- Avoid misleading abbreviations. Use the same domain terms as `product.md`, `requirements.md`, and `data-model.md`.
- Keep variable scope narrow; avoid mutable shared state unless the design requires it.
- Replace unexplained literals with named constants or configuration when they express a business rule or policy.

## 4. Functions and Methods

**Preferred maximum size:** [Project-defined guideline in lines or another reviewable measure; include exceptions for declarative code if needed.]

- Give each function one clear purpose and a name that describes its result or action.
- Keep inputs and outputs explicit. Avoid hidden side effects and long parameter lists; group related inputs when it improves clarity.
- Extract a helper when a function mixes responsibilities or becomes difficult to read. Do not split a straightforward function solely to satisfy a line count.
- State assumptions with types, validation, or preconditions where the language permits.
- Return or raise meaningful outcomes; do not disguise failures as valid results.

## 5. Classes and Files

- Put one primary class in each source file. Name the file after that class according to the language's naming convention.
- Keep closely related helpers or types in the same file only when they support that primary class and improve understanding. Document language or framework exceptions here: [Exceptions or "None".]
- Keep files cohesive. A file may contain related functions when a class would add no value.
- Use descriptive file names that reveal their purpose.

## 6. Reuse and Duplication

- Do not duplicate business rules, validation rules, or substantial behavior across the codebase. Keep one authoritative implementation.
- Extract genuinely shared behavior into a shared module, such as a `utils` area when appropriate. Place domain-specific logic near its domain instead of a generic utility folder.
- Group related helpers in one file; use separate files when responsibilities differ. Name each file by its purpose.
- Do not create a shared abstraction for coincidentally similar code with different business meanings. Review duplication in the context of future change.

## 7. Comments and Documentation

- Let names, types, and structure explain what the code does. Do not add comments that merely restate a function name or each line of code.
- Add a comment when it explains **why** a non-obvious rule, workaround, ordering, or unusual behavior is necessary. Place it next to the relevant code and link to a requirement or decision when useful.
- Update or remove comments when behavior changes. Never leave misleading comments.
- Use public API documentation where consumers need a contract; keep detailed API contracts in `api.md`.

## 8. Dependencies and Versions

**Dependency manifest(s):** [Paths to the language-native manifest files, such as requirements.txt, pyproject.toml, package.json, Cargo.toml, or equivalent.]

**Lockfile(s), if supported:** [Paths and update command.]

- Declare every direct dependency used by the project in the appropriate manifest, with the project's version policy. Do not keep a separate manual version list that can drift from the installable manifest.
- Commit and update the lockfile when the ecosystem uses one. Follow the project's policy for generated lockfiles and reproducible builds.
- Add a dependency only when it solves a concrete need; record the purpose and check maintenance, license, and security implications during review.
- Remove unused dependencies and update manifests, lockfiles, and code together.

## 9. Error Handling

- Validate expected failure conditions and return or raise meaningful errors at the right boundary.
- Never silently swallow an exception. Catch only errors the code can handle; preserve the original cause when rethrowing or wrapping.
- Give users safe, actionable error messages without exposing internal details. Keep diagnostic details available to maintainers through approved logging.
- Define retry, fallback, and cleanup behavior for operations that can fail partway through.

## 10. Logging and Observability

**Logging interface or shared module:** [Location or approach chosen by the project.]

**Format and destination:** [Text / structured JSON / other; where logs are collected.]

**Levels and fields:** [When to use each level and which fields, such as request or correlation IDs, are required.]

- Use the shared logging approach consistently; do not scatter ad hoc print statements through application code.
- Log enough context to diagnose failures without recording passwords, tokens, secrets, or unnecessary personal data.
- Avoid duplicate logs for one failure at every layer. Preserve error context and log at the boundary that can act on it.

## 11. Security Practices

- Treat external input as untrusted. Validate type, size, format, range, and business meaning at the appropriate trust boundary; set explicit limits for text and collections where relevant.
- Do not rely on generic input “sanitization” to prevent injection. Use parameterized SQL queries or safe ORM binding; use context-aware output encoding when placing untrusted content into HTML or other output contexts.
- Enforce authentication and authorization on the server or authoritative boundary for every protected action and resource. Apply least privilege to accounts and services.
- If the system stores passwords, use a current adaptive password-hashing algorithm and library, such as Argon2id where suitable, with per-password salts and reviewed parameters. Never use MD5, SHA-1, or other fast general-purpose hashes for password storage.
- Keep secrets out of source code and logs. Load them through the project's approved secret-management approach.
- Review dependency advisories and security-sensitive changes using the project's chosen tools and process.

> Review [OWASP input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html), [SQL injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html), and [password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) when implementing these controls.

## 12. Data Access and Performance

- Use the access patterns in `data-model.md` to design queries and loading behavior.
- Watch for N+1 queries when loading collections or related records. Use batching, joins, eager loading, or another appropriate approach and verify query behavior for representative data sizes.
- Measure before adding caches or complex optimizations. Document any cache invalidation rule and its effect on correctness.

## 13. Change Workflow and Review

1. Identify the affected requirement IDs, architecture boundaries, API contracts, data model, and UI specifications before editing.
2. Keep changes focused. Preserve `Locked` requirements unless fixing a documented bug or implementing an approved behavior change, following the rules in `requirements.md`.
3. Run the project formatter, linter, static checks, relevant tests, and build using the commands recorded above and in `testing.md`.
4. Review the diff for unnecessary complexity, duplicated logic, accidental behavior changes, unsafe input handling, missing error paths, and dependency changes.
5. Update the affected documentation and record any remaining risk or unresolved decision. Add a concise entry to the project-root `CHANGELOG.md` for the completed change.

## 14. CI/CD Gates

**CI platform and configuration:** [Tool and config path.]

**Required checks:** [Formatting, linting, type checking, tests, build, dependency/security checks, or other project-specific gates.]

**Merge rule:** [Which checks and review approvals must pass before merging.]

**Deployment flow:** [How approved changes reach each environment and how failures are detected or rolled back.]

> CI should run the same commands developers can run locally. Test selection and test quality rules live in `testing.md`.

## 15. Definition of Done

- [ ] The change satisfies its documented requirements and acceptance criteria.
- [ ] Existing affected behavior, especially `Locked` requirements, has been checked for regressions.
- [ ] Required format, lint, static checks, tests, and build pass, or a failure is documented and resolved before merge.
- [ ] Errors, logs, permissions, input validation, and data access have been reviewed where affected.
- [ ] Dependency manifests and lockfiles are current; affected docs and contracts are updated.
- [ ] `CHANGELOG.md` records the completed change in a short, factual entry.
- [ ] The code and diff are readable, focused, and ready for review.

## 16. Exceptions and Open Decisions

| Rule or decision | Exception or open question | Reason | Owner / review date |
| --- | --- | --- | --- |
| [Rule or topic] | [Exception or question] | [Why] | [Owner and date, if known] |
