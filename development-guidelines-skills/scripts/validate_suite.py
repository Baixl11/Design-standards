#!/usr/bin/env python3
"""Validate the development-guidelines Skill suite with standard library only."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]*)?\)")
ALLOWED_SKILL_ENTRIES = {"SKILL.md", "agents", "assets", "references", "scripts"}
REQUIRED_REPORT_STATUSES = ["Pass", "Fail", "Blocked", "Not run", "N/A"]
RISK_MODES = ["local", "module", "contract", "data-migration", "security-critical"]
EXECUTION_MODES = ["decision-only", "greenfield", "existing-project", "review"]
EXPECTED_MODES_BY_CATEGORY = {
    "technology-decision": ["decision-only", "greenfield"],
    "stack-guidance": ["greenfield", "existing-project", "review"],
    "change-safety": RISK_MODES,
}
GENERATED_ARTIFACT_NAMES = {".DS_Store", "__pycache__"}
TEXT_SUFFIXES = {".json", ".md", ".ps1", ".py", ".sh", ".toml", ".yaml", ".yml"}
COMMON_ENVELOPE_FIELDS = [
    "schema_version",
    "artifact_type",
    "artifact_id",
    "project_root",
    "created_at",
    "mode",
    "status",
    "source_artifacts",
    "evidence",
    "unresolved",
]
PROHIBITED_TEXT = {
    "/Users/cyan/": "包含个人绝对路径",
    "任何修改完成后，必须触发": "仍包含无风险分级的强制触发规则",
    "项目初始化必须生成的文件": "仍按文档数量强制初始化",
}


class DuplicateKeyError(ValueError):
    pass


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def read_json(path: Path) -> tuple[Any | None, list[str]]:
    try:
        return (
            json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys),
            [],
        )
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateKeyError) as exc:
        return None, [f"{path}: invalid JSON: {exc}"]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return {}, [f"{path}: cannot read UTF-8: {exc}"]
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing YAML frontmatter"]
    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {}, [f"{path}: unclosed YAML frontmatter"]

    values: dict[str, str] = {}
    errors: list[str] = []
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if not match:
            errors.append(f"{path}: invalid frontmatter line: {line!r}")
            continue
        field, raw_value = match.groups()
        if field not in {"name", "description"}:
            errors.append(f"{path}: unsupported frontmatter field {field!r}")
            continue
        if field in values:
            errors.append(f"{path}: duplicate frontmatter field {field!r}")
            continue
        if raw_value.startswith('"'):
            try:
                value = json.loads(raw_value)
            except json.JSONDecodeError as exc:
                errors.append(f"{path}: invalid quoted {field}: {exc}")
                continue
            if not isinstance(value, str):
                errors.append(f"{path}: {field} must be a string")
                continue
        else:
            if (
                not raw_value
                or raw_value.startswith(("-", "?", ":", "!", "&", "*", "{", "[", "|", ">", "@", "`", "'"))
                or re.search(r":\s|\s#", raw_value)
                or raw_value.casefold() in {"null", "true", "false", "yes", "no", "on", "off", "~"}
            ):
                errors.append(f"{path}: {field} must use an unambiguous one-line YAML string")
                continue
            value = raw_value
        values[field] = value
    for field in ("name", "description"):
        if not values.get(field):
            errors.append(f"{path}: frontmatter missing {field}")
    return values, errors


def parse_openai_yaml(path: Path) -> tuple[dict[str, str], list[str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return {}, [f"{path}: cannot read UTF-8: {exc}"]
    fields = ("display_name", "short_description", "default_prompt")
    values: dict[str, str] = {}
    errors: list[str] = []
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines or lines[0] != "interface:":
        errors.append(f"{path}: root must be exactly interface")
        return values, errors
    for line in lines[1:]:
        match = re.match(r"^  ([a-z_]+):\s*(.+?)\s*$", line)
        if not match:
            errors.append(f"{path}: invalid interface line: {line!r}")
            continue
        field, raw_value = match.groups()
        if field not in fields:
            errors.append(f"{path}: unsupported interface field {field!r}")
            continue
        if field in values:
            errors.append(f"{path}: duplicate interface field {field!r}")
            continue
        try:
            value = json.loads(raw_value)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: interface.{field} must be a quoted JSON/YAML string: {exc}")
            continue
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: interface.{field} must be a non-empty string")
            continue
        values[field] = value
    errors.extend(
        f"{path}: missing quoted interface.{field}" for field in fields if field not in values
    )
    return values, errors


def validate_markdown_links(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_root = skill_dir.resolve()
    for markdown in skill_dir.rglob("*.md"):
        try:
            text = markdown.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{markdown}: cannot read UTF-8: {exc}")
            continue
        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip().strip("<>")
            if not raw or re.match(r"^(?:https?://|mailto:|#)", raw):
                continue
            target = (markdown.parent / raw).resolve()
            try:
                target.relative_to(skill_root)
            except ValueError:
                errors.append(f"{markdown}: relative link escapes Skill root: {raw}")
                continue
            if not target.exists():
                errors.append(f"{markdown}: broken relative link: {raw}")
    return errors


def validate_skill_contract(text: str, category: str | None, skill_name: str) -> list[str]:
    errors: list[str] = []
    required: list[str] = []
    if category == "technology-decision":
        required = EXPECTED_MODES_BY_CATEGORY[category] + ["unsupported", "degraded"]
    elif category == "stack-guidance":
        required = (
            EXPECTED_MODES_BY_CATEGORY[category]
            + RISK_MODES
            + REQUIRED_REPORT_STATUSES
            + ["$change-impact-analysis", "$data-consistency-regression-test", "degraded"]
        )
    elif category == "change-safety":
        required = RISK_MODES + ["degraded"]
        if skill_name == "change-impact-analysis":
            required += ["Blocked", "Not run", "N/A", "$data-consistency-regression-test"]
        elif skill_name == "data-consistency-regression-test":
            required += REQUIRED_REPORT_STATUSES + ["$change-impact-analysis"]

    for marker in required:
        if marker not in text:
            errors.append(f"{skill_name}/SKILL.md: missing suite contract marker {marker!r}")
    return errors


def validate_skill(skill_dir: Path, category: str | None = None) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    metadata, metadata_errors = parse_frontmatter(skill_md)
    errors.extend(metadata_errors)

    name = metadata.get("name")
    if name:
        if name != skill_dir.name:
            errors.append(f"{skill_md}: name {name!r} does not match directory {skill_dir.name!r}")
        if not NAME_RE.fullmatch(name):
            errors.append(f"{skill_md}: invalid Skill name {name!r}")

    try:
        text = skill_md.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        text = ""
    if text.count("\n") + 1 > 300:
        errors.append(f"{skill_md}: exceeds suite limit of 300 lines")
    errors.extend(validate_skill_contract(text, category, name or skill_dir.name))

    for artifact in skill_dir.rglob("*"):
        if not artifact.is_file():
            continue
        try:
            artifact_text = artifact.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        except OSError as exc:
            errors.append(f"{artifact}: cannot read: {exc}")
            continue
        for needle, message in PROHIBITED_TEXT.items():
            if needle in artifact_text:
                errors.append(f"{artifact}: {message}: {needle!r}")

    unexpected = sorted(entry.name for entry in skill_dir.iterdir() if entry.name not in ALLOWED_SKILL_ENTRIES)
    for entry in unexpected:
        errors.append(f"{skill_dir}: unexpected Skill entry {entry!r}")

    agent_file = skill_dir / "agents" / "openai.yaml"
    if not agent_file.is_file():
        errors.append(f"{skill_dir}: missing agents/openai.yaml")
    else:
        agent, agent_errors = parse_openai_yaml(agent_file)
        errors.extend(agent_errors)
        if name and f"${name}" not in agent.get("default_prompt", ""):
            errors.append(f"{agent_file}: default_prompt must mention ${name}")

    errors.extend(validate_markdown_links(skill_dir))
    return errors


def validate_distribution_text(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.casefold() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path}: cannot read as UTF-8 text: {exc}")
            continue
        if "\ufffd" in text:
            errors.append(f"{path}: contains Unicode replacement characters")
    return errors


def validate_artifact_templates(root: Path) -> list[str]:
    errors: list[str] = []
    templates = {
        "ai-dev-tech-stack-orchestrator/assets/stack-decision-template.md": {
            "artifact_type": "StackDecision",
            "modes": ["decision-only", "greenfield"],
            "statuses": ["Ready", "Blocked", "Unsupported"],
            "iteration": False,
        },
        "change-impact-analysis/assets/change-impact-manifest-template.md": {
            "artifact_type": "ChangeImpactManifest",
            "modes": RISK_MODES,
            "statuses": ["Ready", "Blocked"],
            "iteration": True,
        },
        "data-consistency-regression-test/assets/verification-report-template.md": {
            "artifact_type": "VerificationReport",
            "modes": RISK_MODES,
            "statuses": REQUIRED_REPORT_STATUSES,
            "iteration": True,
        },
    }
    for relative, contract in templates.items():
        path = root / relative
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path}: cannot read artifact template: {exc}")
            continue
        positions: list[int] = []
        for field in COMMON_ENVELOPE_FIELDS:
            match = re.search(rf"^{re.escape(field)}:\s*", text, re.MULTILINE)
            if not match:
                errors.append(f"{path}: missing envelope field {field!r}")
            else:
                positions.append(match.start())
        if positions != sorted(positions):
            errors.append(f"{path}: common envelope fields are out of order")
        if f"artifact_type: {contract['artifact_type']}" not in text:
            errors.append(f"{path}: artifact_type does not match template contract")
        for mode in contract["modes"]:
            if mode not in text:
                errors.append(f"{path}: missing mode {mode!r}")
        for status in contract["statuses"]:
            if status not in text:
                errors.append(f"{path}: missing status {status!r}")
        has_iteration = bool(re.search(r"^verification_iteration:\s*", text, re.MULTILINE))
        if has_iteration != contract["iteration"]:
            errors.append(f"{path}: verification_iteration presence does not match contract")
    return errors


def validate_catalog(root: Path, actual_names: set[str]) -> tuple[dict[str, Any] | None, list[str]]:
    catalog, errors = read_json(root / "skill-catalog.json")
    if not isinstance(catalog, dict):
        return None, errors or ["skill-catalog.json: root must be an object"]
    if catalog.get("schema_version") != 2:
        errors.append("skill-catalog.json: schema_version must be 2")
    if catalog.get("suite") != "development-guidelines":
        errors.append("skill-catalog.json: suite must be 'development-guidelines'")
    suite_version = catalog.get("suite_version")
    if not isinstance(suite_version, str) or not SEMVER_RE.fullmatch(suite_version):
        errors.append("skill-catalog.json: suite_version must be semantic x.y.z")
    if catalog.get("install_layout") != "flattened":
        errors.append("skill-catalog.json: install_layout must be 'flattened'")

    settings = catalog.get("settings")
    if not isinstance(settings, dict):
        errors.append("skill-catalog.json: settings must be an object")
        settings = {}
    if settings.get("max_rework_cycles") != 2:
        errors.append("skill-catalog.json: max_rework_cycles must be 2")
    if settings.get("default_change_risk") not in RISK_MODES:
        errors.append("skill-catalog.json: default_change_risk is invalid")
    if settings.get("report_statuses") != REQUIRED_REPORT_STATUSES:
        errors.append("skill-catalog.json: report_statuses do not match suite contract")

    skills = catalog.get("skills")
    if not isinstance(skills, list):
        errors.append("skill-catalog.json: skills must be an array")
        return catalog, errors

    names: list[str] = []
    for index, item in enumerate(skills):
        location = f"skill-catalog.json.skills[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{location}: must be an object")
            continue
        name = item.get("name")
        if not isinstance(name, str):
            errors.append(f"{location}: missing name")
            continue
        names.append(name)
        category = item.get("category")
        if category not in EXPECTED_MODES_BY_CATEGORY:
            errors.append(f"{location}: invalid category {category!r}")
        phase = item.get("phase")
        if not isinstance(phase, str) or not phase:
            errors.append(f"{location}: phase must be a non-empty string")
        expected_phase = (
            "planning"
            if category == "technology-decision"
            else "implementation"
            if category == "stack-guidance"
            else "pre-change"
            if name == "change-impact-analysis"
            else "post-change"
            if name == "data-consistency-regression-test"
            else None
        )
        if expected_phase is not None and phase != expected_phase:
            errors.append(f"{location}: phase must be {expected_phase!r}")
        if not isinstance(item.get("priority"), int):
            errors.append(f"{location}: priority must be an integer")
        modes = item.get("modes")
        if not isinstance(modes, list) or not modes:
            errors.append(f"{location}: modes must be a non-empty array")
        elif any(not isinstance(mode, str) for mode in modes):
            errors.append(f"{location}: modes must contain only strings")
        elif category in EXPECTED_MODES_BY_CATEGORY and modes != EXPECTED_MODES_BY_CATEGORY[category]:
            errors.append(
                f"{location}: modes {modes!r} do not match {category!r} contract "
                f"{EXPECTED_MODES_BY_CATEGORY[category]!r}"
            )
        if "companions" in item:
            errors.append(f"{location}: use workflow_companions/standard_options, not companions")
        workflow = item.get("workflow_companions")
        if not isinstance(workflow, list):
            errors.append(f"{location}: workflow_companions must be an array")
            workflow = []
        else:
            for companion in workflow:
                if not isinstance(companion, str):
                    errors.append(f"{location}: workflow_companions must contain only strings")
                elif companion == name:
                    errors.append(f"{location}: Skill cannot be its own workflow companion")
                elif companion not in actual_names:
                    errors.append(f"{location}: unknown workflow companion {companion!r}")
            if len(workflow) != len({value for value in workflow if isinstance(value, str)}):
                errors.append(f"{location}: duplicate workflow_companions")

        expected_workflow = (
            ["data-consistency-regression-test"]
            if name == "change-impact-analysis"
            else ["change-impact-analysis"]
            if name == "data-consistency-regression-test"
            else ["change-impact-analysis", "data-consistency-regression-test"]
        )
        if workflow != expected_workflow:
            errors.append(
                f"{location}: workflow_companions {workflow!r} do not match "
                f"{expected_workflow!r}"
            )

        if category == "technology-decision":
            if item.get("selection") != "one":
                errors.append(f"{location}: selection must be 'one'")
            options = item.get("standard_options")
            if not isinstance(options, list) or not options:
                errors.append(f"{location}: standard_options must be a non-empty array")
            elif any(not isinstance(option, str) for option in options):
                errors.append(f"{location}: standard_options must contain only strings")
            elif len(options) != len(set(options)):
                errors.append(f"{location}: duplicate standard_options")
        elif "standard_options" in item or "selection" in item:
            errors.append(f"{location}: only technology-decision may define standard_options/selection")

    if len(names) != len(set(names)):
        errors.append("skill-catalog.json: duplicate Skill names")
    catalog_names = set(names)
    if catalog_names != actual_names:
        errors.append(
            "skill-catalog.json: catalog/directory mismatch; "
            f"missing={sorted(actual_names - catalog_names)!r}, "
            f"extra={sorted(catalog_names - actual_names)!r}"
        )
    stack_names = [
        item.get("name")
        for item in skills
        if isinstance(item, dict) and item.get("category") == "stack-guidance"
    ]
    orchestrator = next(
        (
            item
            for item in skills
            if isinstance(item, dict) and item.get("category") == "technology-decision"
        ),
        None,
    )
    if isinstance(orchestrator, dict) and orchestrator.get("standard_options") != stack_names:
        errors.append(
            "skill-catalog.json: orchestrator standard_options must list every "
            "stack-guidance Skill in catalog order"
        )
    return catalog, errors


def validate_evals(root: Path, actual_names: set[str]) -> list[str]:
    path = root / "evals" / "cases.json"
    cases, errors = read_json(path)
    if cases is None:
        return errors
    if not isinstance(cases, list) or not cases:
        return [f"{path}: expected a non-empty array"]
    seen: set[str] = set()
    for index, case in enumerate(cases):
        location = f"{path}[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{location}: must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{location}: missing id")
        elif case_id in seen:
            errors.append(f"{location}: duplicate id {case_id!r}")
        else:
            seen.add(case_id)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"{location}: missing prompt")
        for field in (
            "initial_skill",
            "followup_skills",
            "expected_execution_mode",
            "expected_risk_mode",
            "expected_status",
            "must",
            "must_not",
        ):
            if field not in case:
                errors.append(f"{location}: missing field {field}")
        initial_skill = case.get("initial_skill")
        if not isinstance(initial_skill, str) or not initial_skill.strip():
            errors.append(f"{location}: initial_skill must be a non-empty string")
        elif initial_skill not in actual_names:
            errors.append(f"{location}: unknown initial Skill {initial_skill!r}")

        for field in ("followup_skills", "must", "must_not"):
            value = case.get(field)
            if not isinstance(value, list):
                errors.append(f"{location}: {field} must be an array")
                continue
            if any(not isinstance(item, str) or not item.strip() for item in value):
                errors.append(f"{location}: {field} must contain only non-empty strings")
            if len(value) != len({item for item in value if isinstance(item, str)}):
                errors.append(f"{location}: {field} contains duplicates")
        followup_skills = case.get("followup_skills")
        if isinstance(followup_skills, list):
            for skill in followup_skills:
                if isinstance(skill, str) and skill not in actual_names:
                    errors.append(f"{location}: unknown follow-up Skill {skill!r}")
            if initial_skill in followup_skills:
                errors.append(f"{location}: initial_skill must not repeat in followup_skills")

        execution_mode = case.get("expected_execution_mode")
        if execution_mode is not None and execution_mode not in EXECUTION_MODES:
            errors.append(f"{location}: invalid expected_execution_mode {execution_mode!r}")
        risk_mode = case.get("expected_risk_mode")
        if risk_mode is not None and risk_mode not in RISK_MODES:
            errors.append(f"{location}: invalid expected_risk_mode {risk_mode!r}")
        status = case.get("expected_status")
        if status is not None and status not in REQUIRED_REPORT_STATUSES:
            errors.append(f"{location}: invalid expected_status {status!r}")
        must = case.get("must")
        must_not = case.get("must_not")
        if isinstance(must, list) and isinstance(must_not, list):
            overlap = {item for item in must if isinstance(item, str)} & {
                item for item in must_not if isinstance(item, str)
            }
            if overlap:
                errors.append(f"{location}: must/must_not overlap: {sorted(overlap)!r}")
    return errors


def validate_suite(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for required in (
        "README.md",
        "skill-catalog.json",
        "install_to_target.sh",
        "install_to_target.ps1",
        "scripts/install_suite.py",
        "scripts/evaluate_outputs.py",
        "scripts/validate_suite.py",
        "evals/cases.json",
    ):
        if not (root / required).is_file():
            errors.append(f"{root}: missing {required}")
    for artifact in root.rglob("*"):
        if artifact.name in GENERATED_ARTIFACT_NAMES or artifact.suffix == ".pyc":
            errors.append(f"{artifact}: generated artifact must not be packaged")
    errors.extend(validate_distribution_text(root))
    errors.extend(validate_artifact_templates(root))

    skill_dirs = sorted(
        path for path in root.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()
    )
    actual_names = {path.name for path in skill_dirs}
    catalog, catalog_errors = validate_catalog(root, actual_names)
    errors.extend(catalog_errors)
    raw_catalog_items = catalog.get("skills", []) if isinstance(catalog, dict) else []
    if not isinstance(raw_catalog_items, list):
        raw_catalog_items = []
    catalog_items = {
        item.get("name"): item
        for item in raw_catalog_items
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    }
    for skill_dir in skill_dirs:
        item = catalog_items.get(skill_dir.name, {})
        category = item.get("category") if isinstance(item, dict) else None
        errors.extend(validate_skill(skill_dir, category))
    errors.extend(validate_evals(root, actual_names))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the development-guidelines Skill suite.")
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    errors = validate_suite(args.root)
    if errors:
        print(f"Suite validation failed with {len(errors)} issue(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    skill_count = sum(1 for path in args.root.iterdir() if path.is_dir() and (path / "SKILL.md").is_file())
    print(f"Suite is valid: {skill_count} Skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
