# Coverage Workflow for Large Repositories

Use this when the repository is too large to inspect in one context window. The report itself is the checkpoint, so another run can resume without relying on chat history.

1. Build a file inventory and group first-party files by subsystem, such as entry points, domain areas, data layer, UI, integrations, tests, and deployment. Record generated, vendored, dependency, and cache areas separately as exclusions. Do not send or read the entire repository in one batch.
2. Create `docs/project-understanding.md` after the inventory with a coverage table, and create `docs/file-map.md` with an annotated tree. For each subsystem record its paths, status, evidence links, remaining work, and last checked date or source revision. Prioritize the central user flows and shared boundaries.
3. Inspect one subsystem at a time. Follow its entry points, internal calls, data access, interfaces, error paths, and representative tests. Write what the files establish, record material `OBS-*` claims with source fingerprints using [the evidence workflow](evidence.md), then update its coverage row and file-map annotations before moving on. Search across subsystem boundaries when a flow crosses them.
4. On a later run, check `docs/evidence-trace.json` for changed or missing sources and compare the report's revision or dates with the current tree. Revisit affected claims, then continue from the remaining work. Do not carry forward stale claims without checking them.

Use these coverage levels consistently:

| Level | Meaning |
| --- | --- |
| Pending | Identified but not inspected. |
| Indexed | Files and likely responsibilities mapped from names and structure; behavior not established. |
| Read | Relevant source and documentation inspected; important flows may still be untraced. |
| Traced | Main behavior followed across boundaries with linked source evidence. |
| Validated | The subsystem was traced, and a specific claim was checked by an actual test, run, or other observed result. State exactly which claim and check; this level does not certify the whole subsystem. |

Do not turn `Indexed` into `Read` because a directory name looks descriptive, or `Traced` into `Validated` because tests exist. A subsystem can be well understood at `Traced` while runtime validation remains unperformed. Mark the report `Complete` only when every meaningful first-party subsystem has been traced or its narrower review scope is explicitly justified, and all remaining unknowns and exclusions are visible. If time, access, or context runs out, preserve `In progress` and a concrete next inspection step; do not ask the owner to reconstruct progress.
