#!/usr/bin/env python3
"""Tests for captured forward-evaluation validation."""

from __future__ import annotations

import unittest

from evaluate_outputs import evaluate_records


class EvaluateOutputsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.case = {
            "id": "sample",
            "prompt": "sample request",
            "initial_skill": "sample-standard",
            "followup_skills": ["change-impact-analysis"],
            "expected_execution_mode": "existing-project",
            "expected_risk_mode": "module",
            "expected_status": None,
            "must": ["inspect versions"],
            "must_not": ["upgrade major"],
        }
        self.response = {
            "case_id": "sample",
            "initial_skill": "sample-standard",
            "followup_skills": ["change-impact-analysis"],
            "execution_mode": "existing-project",
            "risk_mode": "module",
            "status": None,
            "response": "I inspected versions and will preserve the installed major.",
            "assertions": [
                {
                    "kind": "must",
                    "expectation": "inspect versions",
                    "passed": True,
                    "evidence_type": "quote",
                    "evidence": "inspected versions",
                },
                {
                    "kind": "must_not",
                    "expectation": "upgrade major",
                    "passed": True,
                    "evidence_type": "review-note",
                    "evidence": "The response preserves the installed major.",
                },
            ],
        }

    def test_complete_evidence_passes(self) -> None:
        self.assertEqual([], evaluate_records([self.case], [self.response]))

    def test_routing_and_assertion_failures_are_reported(self) -> None:
        self.response["risk_mode"] = "local"
        self.response["assertions"][0]["passed"] = False
        errors = evaluate_records([self.case], [self.response])
        self.assertTrue(any("risk_mode" in error for error in errors))
        self.assertTrue(any("failed assertion" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
