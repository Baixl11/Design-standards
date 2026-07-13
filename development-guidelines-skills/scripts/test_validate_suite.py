#!/usr/bin/env python3
"""Tests for validate_suite.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_suite import read_json, validate_catalog, validate_evals, validate_skill, validate_suite


ROOT = Path(__file__).resolve().parent.parent


class ValidateSuiteTests(unittest.TestCase):
    def test_current_suite(self) -> None:
        self.assertEqual([], validate_suite(ROOT))

    def test_duplicate_json_key(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"name": "one", "name": "two"}', encoding="utf-8")
            _, errors = read_json(path)
            self.assertTrue(any("duplicate JSON key" in error for error in errors))

    def test_catalog_directory_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalog = {
                "schema_version": 2,
                "settings": {"report_statuses": ["Pass", "Fail", "Blocked", "Not run", "N/A"]},
                "skills": [
                    {
                        "name": "extra-skill",
                        "priority": 1,
                        "modes": ["review"],
                        "workflow_companions": [],
                    }
                ],
            }
            (root / "skill-catalog.json").write_text(
                json.dumps(catalog), encoding="utf-8"
            )
            _, errors = validate_catalog(root, {"actual-skill"})
            self.assertTrue(any("catalog/directory mismatch" in error for error in errors))

    def test_catalog_rejects_wrong_modes_and_malformed_companion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalog = {
                "schema_version": 2,
                "suite": "development-guidelines",
                "suite_version": "2.0.0",
                "install_layout": "flattened",
                "settings": {
                    "max_rework_cycles": 2,
                    "default_change_risk": "module",
                    "report_statuses": ["Pass", "Fail", "Blocked", "Not run", "N/A"],
                },
                "skills": [
                    {
                        "name": "sample-skill",
                        "category": "stack-guidance",
                        "phase": "implementation",
                        "priority": 1,
                        "modes": ["existing"],
                        "workflow_companions": [{"bad": "type"}],
                    }
                ],
            }
            (root / "skill-catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
            _, errors = validate_catalog(root, {"sample-skill"})
            self.assertTrue(any("do not match" in error for error in errors))
            self.assertTrue(any("workflow_companions must contain only strings" in error for error in errors))

    def test_skill_broken_link_and_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "sample-skill"
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                """---
name: sample-skill
description: Use when testing a sample Skill.
---

# Sample

Read [missing](references/missing.md).
""",
                encoding="utf-8",
            )
            (skill / "agents" / "openai.yaml").write_text(
                """interface:
  display_name: "Sample"
  short_description: "Sample validation Skill metadata"
  default_prompt: "Use this sample."
""",
                encoding="utf-8",
            )
            errors = validate_skill(skill)
            self.assertTrue(any("broken relative link" in error for error in errors))
            self.assertTrue(any("must mention $sample-skill" in error for error in errors))

    def test_skill_rejects_extra_frontmatter_field(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "sample-skill"
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                """---
name: sample-skill
description: Use when testing a sample Skill.
version: 1
---
""",
                encoding="utf-8",
            )
            (skill / "agents" / "openai.yaml").write_text(
                """interface:
  display_name: "Sample"
  short_description: "Sample validation Skill metadata"
  default_prompt: "Use $sample-skill for this task."
""",
                encoding="utf-8",
            )
            errors = validate_skill(skill)
            self.assertTrue(any("unsupported frontmatter field" in error for error in errors))

    def test_generated_artifact_is_rejected_anywhere(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generated = root / "scripts" / "__pycache__" / "sample.pyc"
            generated.parent.mkdir(parents=True)
            generated.write_bytes(b"generated")
            errors = validate_suite(root)
            self.assertTrue(any("generated artifact must not be packaged" in error for error in errors))

    def test_eval_unknown_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "evals").mkdir()
            (root / "evals" / "cases.json").write_text(
                json.dumps(
                    [
                        {
                            "id": "unknown",
                            "prompt": "test",
                            "initial_skill": "missing-skill",
                            "followup_skills": [],
                            "expected_execution_mode": None,
                            "expected_risk_mode": None,
                            "expected_status": None,
                            "must": [],
                            "must_not": [],
                        }
                    ]
                ),
                encoding="utf-8",
            )
            errors = validate_evals(root, {"known-skill"})
            self.assertTrue(any("unknown initial Skill" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
