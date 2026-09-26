"""
test_vibe_audit.py -- Unit tests for Vibe Researching Third-Order Audit integration.
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys

# Ensure audit dir is in sys.path
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from vibe_audit import audit_vibe_project, format_markdown_audit_report
from sandbox import DeltaType


class TestVibeAuditIntegration(unittest.TestCase):

    def setUp(self):
        self.repo_root = current_dir.parent
        self.demo_project = self.repo_root / "demo-project"

    def test_audit_demo_project(self):
        """Verify that demo-project passes Order 1, Order 2, and progressive Order 3."""
        self.assertTrue(self.demo_project.exists(), "demo-project directory must exist")
        res = audit_vibe_project(self.demo_project)
        obj = res["research_object"]

        # Order 1 must pass
        self.assertTrue(obj.order1_pass(), "demo-project must state a falsification condition")
        self.assertIn("FC1", obj.falsification_conditions[0].id)
        self.assertIn("slope", obj.falsification_conditions[0].text.lower())

        # Order 2 must pass
        self.assertTrue(obj.order2_pass(), "demo-project must reference external grounds")
        self.assertGreater(len(res["external_anchors"]), 0)

        # Order 3 must be progressive
        prog = res["sandbox_report"]["programme_level"]
        self.assertGreater(prog["total_revision_events"], 0)
        self.assertIsNotNone(prog["constraint_ratio"])
        self.assertGreaterEqual(prog["constraint_ratio"], 0.0)

        # Zero structural flags
        self.assertEqual(obj.flags(), [])

        # Formatted report generates without error
        md = format_markdown_audit_report(res)
        self.assertIn("Third-Order Epistemic Audit Report", md)
        self.assertIn("PASS", md)

    def test_failing_project_missing_falsification(self):
        """Verify that a project without a falsification condition fails Order 1 & 2."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            rq = tmppath / "research_question.md"
            rq.write_text("# Research Question\n\n## Question\nCan AI write poetry?\n\n## Falsification\nTBD\n", encoding="utf-8")

            res = audit_vibe_project(tmppath)
            obj = res["research_object"]

            self.assertFalse(obj.order1_pass())
            self.assertFalse(obj.order2_pass())
            self.assertIn("NO_FALSIFICATION_CONDITION", obj.flags())


if __name__ == "__main__":
    unittest.main()
