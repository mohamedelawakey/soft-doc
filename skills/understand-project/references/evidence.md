# Evidence Trace

Record important observed claims in `docs/evidence-trace.json` beside the understanding report. Use stable `OBS-001`, `OBS-002`, etc.; preserve IDs when refreshing a claim and remove or retire claims that no longer describe the project. This register is a snapshot of observations, not a product specification.

Use the bundled script from the installed `understand-project` skill:

```text
python3 <skill>/scripts/evidence_trace.py record <project-root> OBS-001 Verified "Users can cancel a booking" src/bookings/cancel.py
python3 <skill>/scripts/evidence_trace.py check <project-root>
python3 <skill>/scripts/evidence_trace.py impact <project-root>
```

`record` accepts one or more first-party source paths relative to the project root. For a short, nonsecret source excerpt, append `@first:last` to a path, such as `src/bookings/cancel.py@12:16`. This records up to 20 lines and lets `impact` show the previous excerpt beside the current lines after a change. Do not capture secrets or personal data. The script calculates a whole-file SHA-256 fingerprint, so any edit triggers review even if the selected lines stay the same. Use `Verified` only when the source directly establishes the exact claim, `Inferred` when reasoning connects evidence without proving it, and `Needs-confirmation` when evidence is missing or conflicting. For the last status, omit source paths only if none are available. The report should render `Needs-confirmation` as “Needs confirmation.”

`check` reports missing or changed cited files and returns a nonzero exit code when it finds any. `impact` lists affected `OBS-*` IDs and Markdown files under `docs/` and `.docs-review/` that cite the ID or repeat the exact claim text; use `impact <project-root> --json` for machine-readable output. Its `context_review` section covers whole-file edits where the selected excerpt is unchanged or moved. These still need a human or agent to check surrounding behavior. Paraphrased documents without an `OBS-*` ID may be missed, so carry the ID into consequential document changes and inspect related documents manually. A changed fingerprint means **review needed**, not that the claim is false. Reinspect the source, update the report and affected draft documents, then re-record the claim. A clean check does not prove the original interpretation or runtime behavior. Running a test may support a separate validation statement, but source inspection alone does not.

The report's claim IDs, statuses, and source links must agree with the register. Keep the register free of secrets and personal data. For large repositories, record claims after each subsystem batch and recheck only affected claims before carrying them into a documentation draft.
