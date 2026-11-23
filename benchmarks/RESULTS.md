# Evidence Impact Benchmark — 2026-11-23

This is a controlled test of `evidence_trace.py`, not an evaluation of the agent's ability to understand a whole project or write correct documentation. The complete case-by-case output and source revisions are in [results-2026-11-23.json](results-2026-11-23.json).

## Method

The benchmark uses source files from public checkouts of Click, Requests, and Flask. For each project it records one narrow claim about an existing function declaration, then tests six isolated cases: no edit, function declaration changed, unrelated edit in the same file, changed declaration with no observation ID in the document, changed declaration with a paraphrased document, and an unrelated line inserted before the declaration. Each case copies the real source file to a temporary project; it never modifies the checkout. Expected outcomes are labeled by the benchmark author.

Run the same benchmark with local checkouts:

```bash
python3 -B benchmarks/impact_benchmark.py --click /path/to/click --requests /path/to/requests --flask /path/to/flask
```

## Results

| Measure | TP | FP | FN | TN | Precision | Recall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Changed observation detection | 9 | 0 | 0 | 9 | 100% | 100% |
| Affected document mapping | 6 | 0 | 3 | 9 | 100% | 66.7% |

The three document misses were paraphrased descriptions without an `OBS-*` ID. Exact claim text or an explicit ID was found. Unrelated edits and shifted line positions were separated into `context_review`, so they did not count as changed observations; they still require review because context can affect behavior.

## Limits

These are deliberately simple, synthetic mutations to real source files. The claims concern function declarations, so the numbers do not measure semantic behavior changes, multi-file flows, the quality of generated documentation, or end-to-end agent performance. The examples do not justify a general 100% accuracy claim. A longer evaluation needs independent human labels, more varied repositories and languages, natural changes from history, and actual agent runs of `sync-project-docs` with reviewed drafts.
