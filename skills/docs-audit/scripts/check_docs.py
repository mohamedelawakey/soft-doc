#!/usr/bin/env python3
"""Check mechanical links and traceability in a project's Markdown documents."""

import argparse
import re
from pathlib import Path
from urllib.parse import unquote


ID = re.compile(r"\b(?:DEC|REQ|NFR|API|ENT|FLOW|CMP|LAY|SCR|TASK)-\d{3}\b")
HEADING = re.compile(r"^#{2,6}\s+((?:DEC|REQ|NFR|API|ENT|FLOW|CMP|LAY|SCR|TASK)-\d{3})\b", re.M)
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PREFIX_FILE = {
    "DEC": "decisions.md",
    "REQ": "requirements.md",
    "NFR": "requirements.md",
    "API": "api.md",
    "ENT": "data-model.md",
    "FLOW": "data-model.md",
    "CMP": "components.md",
    "LAY": "layout.md",
    "SCR": "screens.md",
    "TASK": "plan.md",
}


def is_example(line):
    return "[" in line and "]" in line and not LINK.search(line)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Root directory of the project to check")
    args = parser.parse_args()
    root = args.project.resolve()
    docs = root / "docs"
    if not docs.is_dir():
        parser.error(f"No docs/ directory found in {root}")

    files = sorted(root.glob("*.md")) + sorted(docs.rglob("*.md"))
    definitions = {}
    errors = []
    warnings = []
    content = {}

    for file in files:
        text = file.read_text(encoding="utf-8")
        content[file] = text
        if file == root / "CHANGELOG.md":
            entries = list(re.finditer(r"^##\s+\d{4}-\d{2}-\d{2}\s+[—-]\s+.+$", text, re.M))
            for previous, current in zip(entries, entries[1:]):
                if not re.search(r"^---\s*$", text[previous.end():current.start()], re.M):
                    errors.append(f"CHANGELOG.md: missing --- between entries before line {text.count(chr(10), 0, current.start()) + 1}")
        for line_number, line in enumerate(text.splitlines(), 1):
            for match in LINK.finditer(line):
                target = match.group(1).split()[0].strip("<>").split("#", 1)[0]
                if not target or "://" in target or target.startswith(("mailto:", "#")):
                    continue
                if not (file.parent / unquote(target)).exists():
                    errors.append(f"{file.relative_to(root)}:{line_number}: broken link {target}")
        if file.parent != docs:
            continue
        for match in HEADING.finditer(text):
            identifier = match.group(1)
            if is_example(text.splitlines()[text.count("\n", 0, match.start())]):
                continue
            if identifier in definitions:
                errors.append(f"{file.relative_to(root)}: duplicate definition {identifier}")
            else:
                definitions[identifier] = file

    requirements = docs / "requirements.md"
    plan = docs / "plan.md"
    if requirements in content:
        for line in content[requirements].splitlines():
            if line.startswith("| NFR-") and not is_example(line):
                identifier = ID.search(line).group()
                if identifier in definitions:
                    errors.append(f"docs/requirements.md: duplicate definition {identifier}")
                else:
                    definitions[identifier] = requirements

    decision_file = docs / "decisions.md"
    if decision_file in content:
        for section in re.split(r"(?=^### DEC-\d{3}:)", content[decision_file], flags=re.M)[1:]:
            identifier = re.match(r"### (DEC-\d{3})", section).group(1)
            if is_example(section.splitlines()[0]):
                continue
            for field in ("Status", "Source", "Decision", "Affected IDs", "Owning documents", "Verification impact"):
                match = re.search(rf"^\*\*{re.escape(field)}:\*\*\s*(.*)$", section, re.M)
                if not match or not match.group(1).strip() or is_example(match.group(1)):
                    errors.append(f"docs/decisions.md: {identifier} missing {field}")
            affected = re.search(r"^\*\*Affected IDs:\*\*\s*(.*)$", section, re.M)
            if affected:
                for ref in ID.findall(affected.group(1)):
                    if ref not in definitions:
                        errors.append(f"docs/decisions.md: {identifier} references undefined {ref}")

    if requirements in content:
        for identifier, source in definitions.items():
            if source != requirements or not identifier.startswith(("REQ-", "NFR-")):
                continue
            if plan in content and identifier not in content[plan]:
                warnings.append(f"{identifier}: no reference in docs/plan.md")
            if plan not in content:
                warnings.append(f"{identifier}: docs/plan.md is missing")
    if plan in content:
        for line in content[plan].splitlines():
            if not line.startswith("| TASK-") or is_example(line):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            for ref in ID.findall(cells[5] if len(cells) > 5 else ""):
                if ref not in definitions:
                    errors.append(f"docs/plan.md: task references undefined {ref}")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN: {message}")
    print(f"Checked {len(files)} Markdown files; {len(errors)} errors, {len(warnings)} warnings.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
