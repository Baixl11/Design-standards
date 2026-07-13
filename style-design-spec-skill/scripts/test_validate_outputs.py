#!/usr/bin/env python3
"""Tests for validate_outputs.py using temporary output packages."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_outputs import validate_output_dir


SPEC = """# Product design specification

Status: partial

## Evidence

| ID | Source | Method |
|---|---|---|
| E-001 | Runtime page | Computed style inspection |

## Unresolved

The compact density mode remains 待确认 because it was outside the observed scope.
"""

CHECKLIST_TABLE = """# Design Review Checklist

| ID | 检查项 | 状态 | 证据 | 严重度 |
|---|---|---|---|---|
| EX-001 | Exact values have evidence | Not tested | E-001 | High |
"""

CHECKLIST_TASK = """# Design Review Checklist

- [ ] Verify exact values against E-001.
"""


def token_document(*, evidence_ids: list[str] | None = None) -> dict[str, object]:
    ids = ["E-001"] if evidence_ids is None else evidence_ids
    return {
        "$description": "Evidence-backed tokens for the observed scope.",
        "$extensions": {
            "style-design-spec": {
                "formatVersion": "1.0",
                "generatedAt": "2026-07-10T08:00:00Z",
                "targets": ["web"],
                "documentStatus": "partial",
            }
        },
        "color": {
            "semantic": {
                "text": {
                    "primary": {
                        "$type": "color",
                        "$value": "#111111",
                        "$description": "Primary text on the default surface.",
                        "$extensions": {
                            "style-design-spec": {
                                "status": "measured",
                                "evidenceIds": ids,
                                "confidence": "high",
                                "confidenceReason": "Repeated computed styles matched.",
                                "scope": {"theme": "light", "state": "default"},
                            }
                        },
                    }
                }
            }
        },
    }


class ValidateOutputsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_text(self, name: str, content: str) -> None:
        (self.output_dir / name).write_text(content, encoding="utf-8")

    def write_json(self, data: dict[str, object]) -> None:
        self.write_text(
            "design-tokens.json",
            json.dumps(data, ensure_ascii=False, indent=2),
        )

    def write_valid_full_package(self) -> None:
        self.write_text("design-spec.md", SPEC)
        self.write_json(token_document())
        self.write_text("design-review-checklist.md", CHECKLIST_TABLE)

    def test_valid_full_package(self) -> None:
        self.write_valid_full_package()
        self.assertEqual([], validate_output_dir(self.output_dir, "full"))

    def test_tokens_only_mode(self) -> None:
        self.write_json(token_document())
        self.assertEqual([], validate_output_dir(self.output_dir, "tokens"))

    def test_full_mode_requires_all_files(self) -> None:
        errors = validate_output_dir(self.output_dir, "full")
        self.assertEqual(3, len(errors))

    def test_duplicate_json_key_fails(self) -> None:
        duplicate = json.dumps(token_document(), ensure_ascii=False)
        duplicate = duplicate.replace(
            '"$type": "color"',
            '"$type": "color", "$type": "dimension"',
            1,
        )
        self.write_text("design-tokens.json", duplicate)
        errors = validate_output_dir(self.output_dir, "tokens")
        self.assertTrue(any("重复 JSON 键" in error for error in errors))

    def test_missing_token_contract_fields_fail(self) -> None:
        data = token_document(evidence_ids=[])
        token = data["color"]["semantic"]["text"]["primary"]  # type: ignore[index]
        token.pop("$description")  # type: ignore[union-attr]
        provenance = token["$extensions"]["style-design-spec"]  # type: ignore[index]
        provenance["scope"] = {}  # type: ignore[index]
        self.write_json(data)
        errors = validate_output_dir(self.output_dir, "tokens")
        self.assertTrue(any("$description" in error for error in errors))
        self.assertTrue(any("scope 必须是非空对象" in error for error in errors))
        self.assertTrue(any("evidenceIds 不得为空" in error for error in errors))

    def test_adapted_token_requires_rationale(self) -> None:
        data = token_document(evidence_ids=[])
        token = data["color"]["semantic"]["text"]["primary"]  # type: ignore[index]
        provenance = token["$extensions"]["style-design-spec"]  # type: ignore[index]
        provenance["status"] = "adapted"  # type: ignore[index]
        self.write_json(data)
        errors = validate_output_dir(self.output_dir, "tokens")
        self.assertTrue(any("rationale" in error for error in errors))

    def test_token_evidence_must_appear_in_spec_for_full_mode(self) -> None:
        self.write_text("design-spec.md", SPEC.replace("E-001", "E-002"))
        self.write_json(token_document())
        self.write_text("design-review-checklist.md", CHECKLIST_TABLE)
        errors = validate_output_dir(self.output_dir, "full")
        self.assertTrue(any("未在 design-spec.md 中出现" in error for error in errors))

    def test_review_table_is_accepted(self) -> None:
        self.write_text("design-review-checklist.md", CHECKLIST_TABLE)
        self.assertEqual([], validate_output_dir(self.output_dir, "checklist"))

    def test_visible_task_is_accepted(self) -> None:
        self.write_text("design-review-checklist.md", CHECKLIST_TASK)
        self.assertEqual([], validate_output_dir(self.output_dir, "checklist"))

    def test_fenced_task_fails(self) -> None:
        self.write_text(
            "design-review-checklist.md",
            "# Checklist\n\n```text\n- [ ] Hidden task\n```\n",
        )
        errors = validate_output_dir(self.output_dir, "checklist")
        self.assertTrue(any("fenced code block" in error for error in errors))

    def test_legitimate_unresolved_language_is_allowed(self) -> None:
        self.write_text("design-spec.md", SPEC)
        self.assertEqual([], validate_output_dir(self.output_dir, "spec"))

    def test_template_placeholder_fails(self) -> None:
        self.write_text("design-spec.md", "# {{TARGET_NAME}}\n")
        errors = validate_output_dir(self.output_dir, "spec")
        self.assertTrue(any("模板变量" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
