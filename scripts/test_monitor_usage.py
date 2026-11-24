import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("monitor_usage.py")
TEMPLATE = SCRIPT.parent.parent / "MONITORING.md"


class MonitorUsageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.report = self.root / "MONITORING.md"
        self.report.write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")
        self.ledger = self.root / "monitoring" / "usage.jsonl"
        self.event = {
            "timestamp": "2026-11-23T12:00:00+02:00",
            "task_id": "TASK-1", "request_id": "req-1", "agent": "agent-a",
            "provider": "provider-a", "model": "model-a", "usage_source": "response.usage",
            "tokens": {"input": 1000, "cached_input": 200, "cache_write": 0, "output": 300},
            "pricing": {"currency": "USD", "effective_date": "2026-11-23", "source": "example-rate",
                        "per_million": {"input": "1", "cached_input": "0.1", "cache_write": None, "output": "2"}},
        }

    def run_cli(self, command, event=None):
        return subprocess.run(
            [sys.executable, str(SCRIPT), command, "--ledger", str(self.ledger), "--report", str(self.report)],
            input=json.dumps(event) if event is not None else None, text=True, capture_output=True,
        )

    def test_estimate_and_rebuild_report(self):
        self.assertEqual(self.run_cli("record", self.event).returncode, 0)
        saved = json.loads(self.ledger.read_text(encoding="utf-8").strip())
        self.assertEqual(saved["estimated_cost"], "0.00162")
        self.report.write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")
        self.assertEqual(self.run_cli("report").returncode, 0)
        self.assertIn("0.00162 USD", self.report.read_text(encoding="utf-8"))

    def test_unknown_cost_and_duplicate(self):
        self.event["pricing"] = None
        self.assertEqual(self.run_cli("record", self.event).returncode, 0)
        self.assertIn("Requests with unknown cost: 1", self.report.read_text(encoding="utf-8"))
        duplicate = self.run_cli("record", self.event)
        self.assertNotEqual(duplicate.returncode, 0)
        self.assertIn("duplicate", duplicate.stderr)
        self.assertEqual(len(self.ledger.read_text(encoding="utf-8").splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
