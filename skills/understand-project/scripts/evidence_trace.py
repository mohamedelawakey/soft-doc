#!/usr/bin/env python3
"""Record observations and report documents affected by changed source evidence."""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

CLAIM_ID = re.compile(r"OBS-[0-9]{3,}$")
STATUSES = ("Verified", "Inferred", "Needs-confirmation")
LINE_SPAN = re.compile(r"([1-9][0-9]*):([1-9][0-9]*)$")


def source_file(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError(f"Not a readable project file: {relative}")
    return path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def excerpt(path, span):
    start, end = span
    lines = path.read_text(encoding="utf-8").splitlines()
    if end > len(lines):
        return None
    return "\n".join(lines[start - 1:end])


def make_source(root, specification):
    relative, separator, suffix = specification.rpartition("@")
    match = LINE_SPAN.fullmatch(suffix) if separator else None
    if not match:
        relative = specification
    path = source_file(root, relative)
    source = {"path": path.relative_to(root).as_posix(), "sha256": digest(path)}
    if match:
        start, end = map(int, match.groups())
        if end < start or end - start + 1 > 20:
            raise ValueError("Select 1–20 consecutive lines")
        selected = excerpt(path, [start, end])
        if selected is None or len(selected) > 2000:
            raise ValueError("Source line range is missing or too large")
        source.update({"lines": [start, end], "excerpt": selected})
    return source


def document_refs(root, claim_id, claim):
    paths = list((root / "docs").rglob("*.md"))
    review = root / ".docs-review"
    if review.is_dir():
        paths += list(review.rglob("*.md"))
    pattern = re.compile(rf"(?<![A-Za-z0-9-]){re.escape(claim_id)}(?![A-Za-z0-9-])")
    matches = {}
    for path in paths:
        content = path.read_text(encoding="utf-8")
        if pattern.search(content):
            matches[path.relative_to(root).as_posix()] = "observation_id"
        elif claim in content:
            matches[path.relative_to(root).as_posix()] = "exact_claim_text"
    return dict(sorted(matches.items()))


def inspect(root, entries):
    findings, candidates, errors, seen = [], [], [], set()
    for item in entries:
        claim_id = item.get("id")
        if not isinstance(claim_id, str) or not CLAIM_ID.fullmatch(claim_id) or claim_id in seen:
            errors.append(f"INVALID {claim_id}: duplicate or invalid ID")
            continue
        seen.add(claim_id)
        if item.get("status") not in STATUSES or not isinstance(item.get("claim"), str) or not item["claim"].strip():
            errors.append(f"INVALID {claim_id}: status or claim text")
            continue
        sources = item.get("sources")
        if not isinstance(sources, list) or (item["status"] != "Needs-confirmation" and not sources):
            errors.append(f"INVALID {claim_id}: missing source list")
            continue
        changed, context_changed = [], []
        for source in sources:
            if not isinstance(source, dict):
                errors.append(f"INVALID {claim_id}: source must be an object")
                continue
            relative, fingerprint = source.get("path"), source.get("sha256")
            if not isinstance(relative, str) or not relative or not isinstance(fingerprint, str) or not re.fullmatch(r"[0-9a-f]{64}", fingerprint):
                errors.append(f"INVALID {claim_id}: malformed source path or fingerprint")
                continue
            span = source.get("lines")
            if span is not None and (not isinstance(span, list) or len(span) != 2 or any(type(value) is not int or value < 1 for value in span) or span[1] < span[0] or span[1] - span[0] + 1 > 20 or not isinstance(source.get("excerpt"), str)):
                errors.append(f"INVALID {claim_id}: malformed line range or excerpt")
                continue
            try:
                path = source_file(root, relative)
            except ValueError:
                changed.append({"path": relative, "reason": "missing", "old_excerpt": source.get("excerpt"), "current_excerpt": None})
                continue
            if digest(path) != fingerprint:
                current = None
                if span:
                    try:
                        current = excerpt(path, span)
                    except UnicodeError:
                        pass
                detail = {"path": relative, "reason": "changed", "old_excerpt": source.get("excerpt"), "current_excerpt": current}
                if span and current == source["excerpt"]:
                    detail["reason"] = "changed_elsewhere"
                    context_changed.append(detail)
                elif span and source["excerpt"] in path.read_text(encoding="utf-8"):
                    detail["reason"] = "excerpt_relocated_or_duplicated"
                    context_changed.append(detail)
                else:
                    changed.append(detail)
        matches = document_refs(root, claim_id, item["claim"]) if changed or context_changed else {}
        if changed:
            findings.append({"id": claim_id, "claim": item["claim"], "status": item["status"], "sources": changed, "documents": list(matches), "document_match": matches})
        if context_changed:
            candidates.append({"id": claim_id, "claim": item["claim"], "sources": context_changed, "documents": list(matches), "document_match": matches})
    return findings, candidates, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    for name in ("record", "check", "impact"):
        command = sub.add_parser(name)
        command.add_argument("root", type=Path)
        if name == "record":
            command.add_argument("claim_id")
            command.add_argument("status", choices=STATUSES)
            command.add_argument("claim")
            command.add_argument("sources", nargs="*", help="relative path or path@first:last")
        if name == "impact":
            command.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"Project root does not exist: {root}")
    register = root / "docs" / "evidence-trace.json"
    try:
        entries = json.loads(register.read_text(encoding="utf-8")) if register.exists() else []
        if not isinstance(entries, list) or any(not isinstance(item, dict) for item in entries):
            raise ValueError("Evidence register must contain an array of observation objects")
        if args.action == "record":
            if not CLAIM_ID.fullmatch(args.claim_id) or not args.claim.strip():
                raise ValueError("Supply an OBS-001 style ID and nonempty claim")
            if args.status != "Needs-confirmation" and not args.sources:
                raise ValueError("Verified and Inferred claims require source files")
            source_entries = [make_source(root, value) for value in args.sources]
            entry = {"id": args.claim_id, "status": args.status, "claim": args.claim.strip(), "sources": source_entries}
            entries = [item for item in entries if item.get("id") != args.claim_id] + [entry]
            entries.sort(key=lambda item: item["id"])
            register.parent.mkdir(parents=True, exist_ok=True)
            register.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"Recorded {args.claim_id} in {register}")
            return 0
        if not register.exists():
            raise ValueError(f"Evidence register not found: {register}")
        findings, candidates, errors = inspect(root, entries)
        if args.action == "impact" and args.json:
            print(json.dumps({"affected": findings, "context_review": candidates, "errors": errors}, indent=2, ensure_ascii=False))
        elif args.action == "impact":
            for finding in findings:
                print(f"{finding['id']} — {finding['claim']} [review needed]")
                for source in finding["sources"]:
                    print(f"  Source: {source['path']} ({source['reason']})")
                    if source["old_excerpt"] is not None:
                        print(f"  Previous excerpt: {source['old_excerpt']!r}")
                        print(f"  Current excerpt: {source['current_excerpt']!r}")
                print(f"  Referenced in: {', '.join(finding['documents']) or '(none found; search manually)'}")
            for candidate in candidates:
                print(f"{candidate['id']} — selected excerpt unchanged; surrounding file changed [context review]")
            for error in errors:
                print(error)
            print(f"Affected observations: {len(findings)}; context reviews: {len(candidates)}; register errors: {len(errors)}")
        else:
            for finding in findings:
                for source in finding["sources"]:
                    label = "STALE" if source["reason"] == "changed" else "MISSING"
                    print(f"{label} {finding['id']}: {source['path']}")
            for candidate in candidates:
                for source in candidate["sources"]:
                    print(f"CONTEXT {candidate['id']}: {source['path']}")
            for error in errors:
                print(error)
            print(f"Checked {len(entries)} observations; {sum(len(item['sources']) for item in findings + candidates) + len(errors)} issue(s)")
        return 1 if findings or candidates or errors else 0
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as error:
        print(f"Evidence trace error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
