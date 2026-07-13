#!/usr/bin/env python3
"""Validate captured forward-test routing and assertion evidence."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from validate_suite import read_json


ROUTING_FIELDS = {
    "initial_skill": "initial_skill",
    "followup_skills": "followup_skills",
    "execution_mode": "expected_execution_mode",
    "risk_mode": "expected_risk_mode",
    "status": "expected_status",
}


def index_records(records: Any, label: str) -> tuple[dict[str, dict[str, Any]], list[str]]:
    errors: list[str] = []
    indexed: dict[str, dict[str, Any]] = {}
    if not isinstance(records, list):
        return {}, [f"{label}: root must be an array"]
    for index, record in enumerate(records):
        location = f"{label}[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{location}: must be an object")
            continue
        case_id = record.get("case_id", record.get("id"))
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{location}: missing case_id/id")
        elif case_id in indexed:
            errors.append(f"{location}: duplicate case id {case_id!r}")
        else:
            indexed[case_id] = record
    return indexed, errors


def validate_assertions(
    case_id: str,
    case: dict[str, Any],
    response: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    assertions = response.get("assertions")
    if not isinstance(assertions, list):
        return [f"{case_id}: assertions must be an array"]

    actual: dict[tuple[str, str], dict[str, Any]] = {}
    for index, assertion in enumerate(assertions):
        location = f"{case_id}.assertions[{index}]"
        if not isinstance(assertion, dict):
            errors.append(f"{location}: must be an object")
            continue
        kind = assertion.get("kind")
        expectation = assertion.get("expectation")
        if kind not in {"must", "must_not"} or not isinstance(expectation, str):
            errors.append(f"{location}: requires kind=must/must_not and an expectation string")
            continue
        key = (kind, expectation)
        if key in actual:
            errors.append(f"{location}: duplicate assertion {key!r}")
            continue
        actual[key] = assertion

    expected = {
        (kind, expectation)
        for kind in ("must", "must_not")
        for expectation in case.get(kind, [])
        if isinstance(expectation, str)
    }
    missing = expected - set(actual)
    extra = set(actual) - expected
    if missing:
        errors.append(f"{case_id}: missing assertions {sorted(missing)!r}")
    if extra:
        errors.append(f"{case_id}: unexpected assertions {sorted(extra)!r}")

    raw_response = response.get("response")
    for key in expected & set(actual):
        assertion = actual[key]
        if assertion.get("passed") is not True:
            errors.append(f"{case_id}: failed assertion {key!r}")
        evidence = assertion.get("evidence")
        if not isinstance(evidence, str) or not evidence.strip():
            errors.append(f"{case_id}: assertion {key!r} requires evidence")
        evidence_type = assertion.get("evidence_type", "review-note")
        if evidence_type not in {"quote", "review-note"}:
            errors.append(f"{case_id}: assertion {key!r} has invalid evidence_type")
        if (
            evidence_type == "quote"
            and isinstance(evidence, str)
            and isinstance(raw_response, str)
            and evidence not in raw_response
        ):
            errors.append(f"{case_id}: quoted evidence is absent from response for {key!r}")
    return errors


def evaluate_records(cases: Any, responses: Any, *, allow_partial: bool = False) -> list[str]:
    case_index, errors = index_records(cases, "cases")
    response_index, response_errors = index_records(responses, "responses")
    errors.extend(response_errors)
    if not allow_partial:
        missing = set(case_index) - set(response_index)
        if missing:
            errors.append(f"responses: missing cases {sorted(missing)!r}")
    extra = set(response_index) - set(case_index)
    if extra:
        errors.append(f"responses: unknown cases {sorted(extra)!r}")

    for case_id in sorted(set(case_index) & set(response_index)):
        case = case_index[case_id]
        response = response_index[case_id]
        raw_response = response.get("response")
        if not isinstance(raw_response, str) or not raw_response.strip():
            errors.append(f"{case_id}: response must be non-empty text")
        for actual_field, expected_field in ROUTING_FIELDS.items():
            if response.get(actual_field) != case.get(expected_field):
                errors.append(
                    f"{case_id}: {actual_field}={response.get(actual_field)!r}; "
                    f"expected {case.get(expected_field)!r}"
                )
        errors.extend(validate_assertions(case_id, case, response))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("responses", type=Path, help="captured response records in JSON")
    parser.add_argument(
        "--cases",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "evals" / "cases.json",
    )
    parser.add_argument("--allow-partial", action="store_true")
    args = parser.parse_args(argv)

    cases, case_errors = read_json(args.cases)
    responses, response_errors = read_json(args.responses)
    errors = case_errors + response_errors
    if not errors:
        errors.extend(evaluate_records(cases, responses, allow_partial=args.allow_partial))
    if errors:
        print(f"Forward evaluation failed with {len(errors)} issue(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    count = len(responses) if isinstance(responses, list) else 0
    print(f"Forward evaluation passed: {count} captured case(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
