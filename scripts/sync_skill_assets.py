#!/usr/bin/env python3
"""Keep portable project-discovery assets in sync with source templates."""

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "skills/project-discovery/assets"


def sources():
    for source in sorted((ROOT / "docs").rglob("*.md")):
        target = ASSETS / source.relative_to(ROOT / "docs")
        yield source, target
    yield ROOT / "MONITORING.md", ASSETS / "MONITORING.md"
    yield ROOT / "scripts/monitor_usage.py", ASSETS / "scripts/monitor_usage.py"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()
    changed = []
    pairs = list(sources())
    for source, target in pairs:
        if not source.is_file():
            parser.error(f"missing source: {source}")
        if not target.is_file() or source.read_bytes() != target.read_bytes():
            changed.append(target.relative_to(ROOT))
            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
    if changed:
        action = "Out of sync" if args.check else "Updated"
        for path in changed:
            print(f"{action}: {path}")
    else:
        print(f"All {len(pairs)} shared assets are in sync.")
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
