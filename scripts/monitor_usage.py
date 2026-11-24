#!/usr/bin/env python3
"""Record provider-reported model usage and render a local Markdown report."""

import argparse
import json
import os
import sys
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

BUCKETS = ("input", "cached_input", "cache_write", "output")
BEGIN = "<!-- usage-report:start -->"
END = "<!-- usage-report:end -->"


def fail(message):
    raise ValueError(message)


def nonempty(value, name):
    if not isinstance(value, str) or not value.strip() or "\n" in value:
        fail(f"{name} must be a nonempty single-line string")
    return value.strip()


def validate(event):
    if not isinstance(event, dict):
        fail("event must be a JSON object")
    allowed = {"timestamp", "task_id", "request_id", "agent", "provider", "model", "usage_source", "tokens", "pricing"}
    if set(event) - allowed:
        fail(f"unsupported fields: {', '.join(sorted(set(event) - allowed))}")
    result = {key: nonempty(event.get(key), key) for key in ("task_id", "request_id", "agent", "provider", "model", "usage_source")}
    stamp = nonempty(event.get("timestamp"), "timestamp")
    try:
        parsed = datetime.fromisoformat(stamp)
    except ValueError:
        fail("timestamp must be ISO 8601")
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        fail("timestamp must include a timezone offset")
    result["timestamp"] = stamp
    tokens = event.get("tokens")
    if tokens is not None:
        if not isinstance(tokens, dict) or set(tokens) != set(BUCKETS):
            fail(f"tokens must contain exactly: {', '.join(BUCKETS)}")
        for key in BUCKETS:
            if type(tokens[key]) is not int or tokens[key] < 0:
                fail(f"tokens.{key} must be a nonnegative integer")
    result["tokens"] = tokens
    pricing = event.get("pricing")
    if pricing is not None:
        if not isinstance(pricing, dict) or set(pricing) != {"currency", "effective_date", "source", "per_million"}:
            fail("pricing needs currency, effective_date, source, and per_million")
        for key in ("currency", "effective_date", "source"):
            nonempty(pricing[key], f"pricing.{key}")
        try:
            datetime.fromisoformat(pricing["effective_date"])
        except ValueError:
            fail("pricing.effective_date must be an ISO date")
        rates = pricing["per_million"]
        if not isinstance(rates, dict) or set(rates) != set(BUCKETS):
            fail(f"pricing.per_million must contain exactly: {', '.join(BUCKETS)}")
        for key in BUCKETS:
            if rates[key] is not None:
                try:
                    rate = Decimal(str(rates[key]))
                except InvalidOperation:
                    fail(f"pricing.per_million.{key} must be numeric or null")
                if not rate.is_finite() or rate < 0:
                    fail(f"pricing.per_million.{key} must be finite and nonnegative")
    result["pricing"] = pricing
    cost = None
    if tokens is not None and pricing is not None:
        rates = pricing["per_million"]
        if all(tokens[key] == 0 or rates[key] is not None for key in BUCKETS):
            cost = sum(Decimal(tokens[key]) * Decimal(str(rates[key] or 0)) for key in BUCKETS) / Decimal(1_000_000)
    result["estimated_cost"] = str(cost) if cost is not None else None
    return result


def read_events(path):
    if not path.exists():
        return []
    events = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            fail(f"invalid ledger line {line_number}: {exc}")
    return events


def safe(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(events):
    lines = ["| Date | Task | Request | Agent | Provider / model | Input | Cached | Cache write | Output | Estimated cost |", "| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |"]
    totals = {}
    task_totals = {}
    unknown = 0
    for event in sorted(events, key=lambda item: item["timestamp"], reverse=True):
        tokens = event["tokens"]
        cost = event["estimated_cost"]
        currency = event["pricing"]["currency"] if event["pricing"] else None
        if cost is None:
            unknown += 1
        else:
            totals[currency] = totals.get(currency, Decimal(0)) + Decimal(cost)
            task_key = (event["task_id"], currency)
            task_totals[task_key] = task_totals.get(task_key, Decimal(0)) + Decimal(cost)
        cells = [event["timestamp"], event["task_id"], event["request_id"], event["agent"], event["provider"] + " / " + event["model"]]
        cells += [tokens[key] if tokens else "Unknown" for key in BUCKETS]
        cells += [f"{cost} {currency}" if cost is not None else "Unknown"]
        lines.append("| " + " | ".join(safe(cell) for cell in cells) + " |")
    summary = ", ".join(f"{amount} {currency}" for currency, amount in sorted(totals.items())) or "None"
    task_lines = ["| Task | Requests | Estimated cost | Unknown costs |", "| --- | ---: | ---: | ---: |"]
    for task in sorted({event["task_id"] for event in events}):
        grouped = [event for event in events if event["task_id"] == task]
        amounts = ", ".join(f"{amount} {currency}" for (task_id, currency), amount in sorted(task_totals.items()) if task_id == task) or "None"
        missing = sum(event["estimated_cost"] is None for event in grouped)
        task_lines.append(f"| {safe(task)} | {len(grouped)} | {amounts} | {missing} |")
    return "\n".join([f"Recorded requests: {len(events)}. Estimated totals: {summary}. Requests with unknown cost: {unknown}.", "", "### By task", "", *task_lines, "", "### By model request", "", *lines])


def write_report(path, events):
    content = path.read_text(encoding="utf-8")
    if content.count(BEGIN) != 1 or content.count(END) != 1 or content.index(BEGIN) > content.index(END):
        fail(f"{path} needs one ordered report marker pair")
    start = content.index(BEGIN) + len(BEGIN)
    end = content.index(END)
    updated = content[:start] + "\n\n" + render(events) + "\n\n" + content[end:]
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(updated, encoding="utf-8")
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("record", "report"))
    parser.add_argument("event", nargs="?", help="JSON event file for record; omit to read stdin")
    parser.add_argument("--ledger", type=Path, default=Path("monitoring/usage.jsonl"))
    parser.add_argument("--report", type=Path, default=Path("MONITORING.md"))
    args = parser.parse_args()
    if args.command == "report" and args.event:
        parser.error("report does not accept an event")
    try:
        args.ledger.parent.mkdir(parents=True, exist_ok=True)
        with (args.ledger.parent / ".usage.lock").open("w") as lock:
            import fcntl
            fcntl.flock(lock, fcntl.LOCK_EX)
            events = read_events(args.ledger)
            if args.command == "record":
                raw = Path(args.event).read_text(encoding="utf-8") if args.event else sys.stdin.read()
                event = validate(json.loads(raw))
                if any((old["provider"], old["request_id"]) == (event["provider"], event["request_id"]) for old in events):
                    fail("duplicate provider/request_id")
                with args.ledger.open("a", encoding="utf-8") as output:
                    output.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n")
                events.append(event)
            write_report(args.report, events)
        print(f"{len(events)} request(s); report: {args.report}")
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        parser.exit(1, f"error: {exc}\n")


if __name__ == "__main__":
    main()
