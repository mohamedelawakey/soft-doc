#!/usr/bin/env python3
"""Measure evidence impact detection on controlled edits to real Python source files."""

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TRACE = Path(__file__).resolve().parents[1] / "skills/understand-project/scripts/evidence_trace.py"
CASES = {
    "click": ("src/click/utils.py", "def echo("),
    "requests": ("src/requests/api.py", "def get("),
    "flask": ("src/flask/app.py", "    def run("),
}


def run_trace(root, *arguments):
    result = subprocess.run([sys.executable, str(TRACE), arguments[0], str(root), *arguments[1:]], capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr or result.stdout)
    return result


def one_case(project, source_root, scenario):
    relative, needle = CASES[project]
    original = source_root / relative
    if not original.is_file():
        raise ValueError(f"Missing {original}")
    with tempfile.TemporaryDirectory(prefix=f"impact-{project}-") as temporary:
        root = Path(temporary)
        source = root / relative
        source.parent.mkdir(parents=True)
        shutil.copyfile(original, source)
        lines = source.read_text(encoding="utf-8").splitlines()
        matches = [index for index, line in enumerate(lines, 1) if line.startswith(needle)]
        if len(matches) != 1:
            raise ValueError(f"Expected one anchor in {original}; found {len(matches)}")
        line_number = matches[0]
        docs = root / "docs"
        docs.mkdir()
        cite = scenario not in ("missing_document_id", "paraphrased_document")
        sentence = f"The source defines {needle.strip()} {'(OBS-001)' if cite else ''}.\n"
        if scenario == "paraphrased_document":
            sentence = f"A callable named {needle.strip().removeprefix('def ').removeprefix('def ')} exists in this module.\n"
        (docs / "project-understanding.md").write_text(sentence, encoding="utf-8")
        recorded = run_trace(root, "record", "OBS-001", "Verified", f"The source defines {needle.strip()}", f"{relative}@{line_number}:{line_number}")
        if recorded.returncode != 0:
            raise RuntimeError(recorded.stdout)
        if scenario in ("behavior_change", "missing_document_id", "paraphrased_document"):
            lines[line_number - 1] = lines[line_number - 1].replace(needle, needle.replace("(", "_changed("), 1)
            source.write_text("\n".join(lines) + "\n", encoding="utf-8")
        elif scenario == "unrelated_edit":
            source.write_text(source.read_text(encoding="utf-8") + "\n# unrelated benchmark note\n", encoding="utf-8")
        elif scenario == "line_shift":
            source.write_text("# inserted unrelated line\n" + source.read_text(encoding="utf-8"), encoding="utf-8")
        result = run_trace(root, "impact", "--json")
        finding = json.loads(result.stdout)["affected"]
        predicted_claim = bool(finding)
        predicted_document = bool(finding and finding[0]["documents"])
        expected_claim = scenario in ("behavior_change", "missing_document_id", "paraphrased_document")
        expected_document = expected_claim
        return {
            "project": project,
            "scenario": scenario,
            "expected_claim": expected_claim,
            "predicted_claim": predicted_claim,
            "expected_document": expected_document,
            "predicted_document": predicted_document,
            "observed_reason": finding[0]["sources"][0]["reason"] if finding else None,
        }


def metrics(rows, expected, predicted):
    tp = sum(row[expected] and row[predicted] for row in rows)
    fp = sum(not row[expected] and row[predicted] for row in rows)
    fn = sum(row[expected] and not row[predicted] for row in rows)
    tn = sum(not row[expected] and not row[predicted] for row in rows)
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn, "precision": round(tp / (tp + fp), 3) if tp + fp else None, "recall": round(tp / (tp + fn), 3) if tp + fn else None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for project in CASES:
        parser.add_argument(f"--{project}", type=Path, required=True, help=f"local checkout of {project}")
    args = parser.parse_args()
    rows = []
    revisions = {}
    for project in CASES:
        source_root = getattr(args, project).resolve()
        revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=source_root, capture_output=True, text=True, check=True)
        revisions[project] = revision.stdout.strip()
        for scenario in ("unchanged", "behavior_change", "unrelated_edit", "missing_document_id", "paraphrased_document", "line_shift"):
            rows.append(one_case(project, source_root, scenario))
    print(json.dumps({"revisions": revisions, "cases": rows, "claim_detection": metrics(rows, "expected_claim", "predicted_claim"), "document_mapping": metrics(rows, "expected_document", "predicted_document")}, indent=2))


if __name__ == "__main__":
    main()
