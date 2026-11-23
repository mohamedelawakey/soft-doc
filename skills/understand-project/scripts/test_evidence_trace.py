#!/usr/bin/env python3
"""Exercise the evidence lifecycle on a small, isolated booking project."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("evidence_trace.py")


class EvidenceWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.sandbox = tempfile.TemporaryDirectory()
        self.addCleanup(self.sandbox.cleanup)
        self.root = Path(self.sandbox.name)
        (self.root / "src").mkdir()
        (self.root / "docs").mkdir()
        self.source = self.root / "src" / "booking.py"
        self.source.write_text("CANCELLATION_HOURS = 24\n", encoding="utf-8")

    def run_trace(self, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPT), arguments[0], str(self.root), *arguments[1:]],
            capture_output=True, text=True, check=False,
        )

    def test_change_blocks_use_until_claim_is_rechecked(self):
        original = self.root / "docs" / "requirements.md"
        original.write_text("Current requirements are undecided.\n", encoding="utf-8")
        draft = self.root / ".docs-review" / "booking" / "docs" / "requirements.md"
        draft.parent.mkdir(parents=True)
        draft.write_text("Observed cancellation limit: 24 hours (OBS-001).\n", encoding="utf-8")
        (self.root / "docs" / "api.md").write_text("Cancellation behavior uses OBS-001.\n", encoding="utf-8")

        recorded = self.run_trace("record", "OBS-001", "Verified", "Cancellation limit is 24 hours", "src/booking.py@1:1")
        self.assertEqual(recorded.returncode, 0, recorded.stderr)
        self.assertEqual(self.run_trace("check").returncode, 0)
        self.assertEqual(original.read_text(), "Current requirements are undecided.\n")

        self.source.write_text("CANCELLATION_HOURS = 12\n", encoding="utf-8")
        stale = self.run_trace("check")
        self.assertEqual(stale.returncode, 1)
        self.assertIn("STALE OBS-001", stale.stdout)
        impact = self.run_trace("impact", "--json")
        self.assertEqual(impact.returncode, 1)
        affected = json.loads(impact.stdout)["affected"][0]
        self.assertEqual(affected["id"], "OBS-001")
        self.assertEqual(affected["sources"][0]["old_excerpt"], "CANCELLATION_HOURS = 24")
        self.assertEqual(affected["sources"][0]["current_excerpt"], "CANCELLATION_HOURS = 12")
        self.assertEqual(affected["documents"], [".docs-review/booking/docs/requirements.md", "docs/api.md"])

        draft.write_text("Observed cancellation limit: 12 hours (OBS-001).\n", encoding="utf-8")
        refreshed = self.run_trace("record", "OBS-001", "Verified", "Cancellation limit is 12 hours", "src/booking.py@1:1")
        self.assertEqual(refreshed.returncode, 0, refreshed.stderr)
        self.assertEqual(self.run_trace("check").returncode, 0)
        self.assertEqual(original.read_text(), "Current requirements are undecided.\n")
        self.assertIn("12 hours", draft.read_text())

    def test_missing_source_and_invalid_register_are_reported(self):
        self.run_trace("record", "OBS-002", "Inferred", "Bookings may expire", "src/booking.py")
        self.source.unlink()
        self.assertIn("MISSING OBS-002", self.run_trace("check").stdout)
        (self.root / "docs" / "evidence-trace.json").write_text(json.dumps([{"id": "OBS-002", "status": "Verified", "claim": "", "sources": []}]))
        invalid = self.run_trace("check")
        self.assertEqual(invalid.returncode, 1)
        self.assertIn("INVALID OBS-002", invalid.stdout)

    def test_unrelated_document_and_missing_source(self):
        self.run_trace("record", "OBS-003", "Verified", "Cancellation limit is 24 hours", "src/booking.py")
        (self.root / "docs" / "requirements.md").write_text("No observation ID here.\n", encoding="utf-8")
        self.source.unlink()
        impact = json.loads(self.run_trace("impact", "--json").stdout)["affected"][0]
        self.assertEqual(impact["sources"][0]["reason"], "missing")
        self.assertEqual(impact["documents"], [])

    def test_unrelated_edit_and_shift_are_context_reviews(self):
        self.run_trace("record", "OBS-004", "Verified", "Cancellation limit is 24 hours", "src/booking.py@1:1")
        self.source.write_text(self.source.read_text() + "# unrelated\n")
        first = json.loads(self.run_trace("impact", "--json").stdout)
        self.assertEqual(first["affected"], [])
        self.assertEqual(first["context_review"][0]["sources"][0]["reason"], "changed_elsewhere")
        self.source.write_text("# inserted\nCANCELLATION_HOURS = 24\n")
        shifted = json.loads(self.run_trace("impact", "--json").stdout)
        self.assertEqual(shifted["affected"], [])
        self.assertEqual(shifted["context_review"][0]["sources"][0]["reason"], "excerpt_relocated_or_duplicated")

    def test_exact_claim_text_finds_document_without_id(self):
        claim = "Cancellation limit is 24 hours"
        self.run_trace("record", "OBS-005", "Verified", claim, "src/booking.py@1:1")
        (self.root / "docs" / "requirements.md").write_text(claim + ".\n")
        self.source.write_text("CANCELLATION_HOURS = 12\n")
        finding = json.loads(self.run_trace("impact", "--json").stdout)["affected"][0]
        self.assertEqual(finding["document_match"], {"docs/requirements.md": "exact_claim_text"})


if __name__ == "__main__":
    unittest.main()
