#!/usr/bin/env python3
"""Validate the three output artifacts produced by this skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


REQUIRED_FILES = (
    "design-spec.md",
    "design-tokens.json",
    "design-review-checklist.md",
)

MODE_FILES = {
    "full": REQUIRED_FILES,
    "spec": ("design-spec.md",),
    "tokens": ("design-tokens.json",),
    "checklist": ("design-review-checklist.md",),
}

PLACEHOLDER_PATTERNS = (
    ("英文占位符", re.compile(r"\b(?:TODO|TBD|TBC|FIXME|XXX)\b", re.IGNORECASE)),
    ("示例占位文本", re.compile(r"\blorem\s+ipsum\b", re.IGNORECASE)),
    ("模板变量", re.compile(r"\{\{\s*[^{}\r\n]+\s*\}\}")),
    (
        "中文占位符",
        re.compile(
            r"(?:待填写|待替换|请填写|请替换|示例值|占位符)"
        ),
    ),
    (
        "尖括号占位符",
        re.compile(
            r"<\s*(?:TODO|TBD|TBC|placeholder|fill(?:[-_ ]?in)?|replace[-_ ]?me)"
            r"(?:\s+[^<>\r\n]*)?>",
            re.IGNORECASE,
        ),
    ),
)

EVIDENCE_ID_RE = re.compile(r"^E-[0-9]{3,}$")
SHORT_EVIDENCE_ID_RE = re.compile(r"(?<![A-Za-z0-9])E-([0-9]+)(?![A-Za-z0-9])")
TASK_RE = re.compile(r"^\s*[-*+]\s+\[[ xX]\](?:\s+|$)")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")

VALID_STATUSES = {"measured", "sampled", "observed", "inferred", "adapted"}
VALID_CONFIDENCES = {"high", "medium", "low"}
VALID_DOCUMENT_STATUSES = {"draft", "partial", "verified"}
EXTENSION_KEY = "style-design-spec"
CONTRACT_SCHEMA_PATH = (
    Path(__file__).resolve().parent.parent / "assets" / "design-tokens.schema.json"
)
ISO_DATETIME_RE = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
    r"(?:\.[0-9]+)?(?:Z|[+-][0-9]{2}:[0-9]{2})$"
)


class DuplicateKeyError(ValueError):
    """Raised when JSON contains duplicate object keys."""


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"重复 JSON 键: {key!r}")
        result[key] = value
    return result


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def validate_bundled_schema_contract() -> list[str]:
    try:
        schema = json.loads(CONTRACT_SCHEMA_PATH.read_text(encoding="utf-8"))
        definitions = schema["$defs"]
        token_required = set(definitions["token"]["required"])
        evidence = definitions["evidence"]
        evidence_required = set(evidence["required"])
        status_values = set(evidence["properties"]["status"]["enum"])
        confidence_values = set(evidence["properties"]["confidence"]["enum"])
        root_metadata = definitions["rootExtensions"]["properties"][EXTENSION_KEY]
        root_required = set(root_metadata["required"])
        document_statuses = set(
            root_metadata["properties"]["documentStatus"]["enum"]
        )
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
        return [f"design-tokens.schema.json: 无法读取契约: {exc}"]

    errors: list[str] = []
    expected_token = {"$type", "$value", "$description", "$extensions"}
    expected_evidence = {
        "status",
        "evidenceIds",
        "confidence",
        "confidenceReason",
        "scope",
    }
    expected_root = {"formatVersion", "generatedAt", "targets", "documentStatus"}
    comparisons = (
        (expected_token, token_required, "token required"),
        (expected_evidence, evidence_required, "evidence required"),
        (expected_root, root_required, "root metadata required"),
        (VALID_STATUSES, status_values, "status enum"),
        (VALID_CONFIDENCES, confidence_values, "confidence enum"),
        (VALID_DOCUMENT_STATUSES, document_statuses, "documentStatus enum"),
    )
    for expected, actual, label in comparisons:
        if expected != actual:
            errors.append(
                "design-tokens.schema.json: "
                f"{label} 与校验器不一致；expected={sorted(expected)!r}, "
                f"actual={sorted(actual)!r}"
            )
    return errors


def find_placeholders(filename: str, text: str) -> list[str]:
    errors: list[str] = []
    seen: set[tuple[int, str]] = set()
    for label, pattern in PLACEHOLDER_PATTERNS:
        for match in pattern.finditer(text):
            line = line_number(text, match.start())
            key = (line, match.group(0))
            if key not in seen:
                excerpt = match.group(0).replace("\n", " ")
                errors.append(f"{filename}:{line}: 发现{label}: {excerpt!r}")
                seen.add(key)

    for match in SHORT_EVIDENCE_ID_RE.finditer(text):
        candidate = match.group(0)
        if not EVIDENCE_ID_RE.fullmatch(candidate):
            line = line_number(text, match.start())
            errors.append(
                f"{filename}:{line}: 证据 ID {candidate!r} 不符合 ^E-[0-9]{{3,}}$"
            )
    return errors


def format_path(parts: Iterable[str]) -> str:
    result = "$"
    for part in parts:
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", part):
            result += f".{part}"
        else:
            result += f"[{json.dumps(part, ensure_ascii=False)}]"
    return result


def is_token_candidate(node: dict[str, Any]) -> bool:
    if "$value" in node:
        return True
    has_child_nodes = any(
        not key.startswith("$") and isinstance(value, dict)
        for key, value in node.items()
    )
    extension = node.get("$extensions")
    provenance = extension.get(EXTENSION_KEY) if isinstance(extension, dict) else None
    if (
        not has_child_nodes
        and isinstance(provenance, dict)
        and ({"status", "evidenceIds"} & provenance.keys())
    ):
        return True
    if "$type" not in node:
        return False
    return not has_child_nodes


def validate_evidence_ids(value: Any, location: str, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append(f"{location}.evidenceIds 必须是数组")
        return

    seen: set[str] = set()
    for index, evidence_id in enumerate(value):
        item_location = f"{location}.evidenceIds[{index}]"
        if not isinstance(evidence_id, str) or not EVIDENCE_ID_RE.fullmatch(evidence_id):
            errors.append(f"{item_location} 必须符合 ^E-[0-9]{{3,}}$")
            continue
        if evidence_id in seen:
            errors.append(f"{item_location} 重复引用证据 {evidence_id!r}")
        seen.add(evidence_id)


def validate_token(node: dict[str, Any], path: tuple[str, ...], errors: list[str]) -> None:
    location = format_path(path)

    allowed_keys = {"$type", "$value", "$description", "$extensions"}
    unexpected_keys = sorted(set(node) - allowed_keys)
    for key in unexpected_keys:
        errors.append(f"{location}: token 包含 schema 未允许的键 {key!r}")

    if "$value" not in node:
        errors.append(f"{location}: token 缺少 $value")
    elif node["$value"] is None:
        errors.append(f"{location}.$value 不得为 null")
    elif isinstance(node["$value"], str) and not node["$value"].strip():
        errors.append(f"{location}.$value 不得为空字符串")

    token_type = node.get("$type")
    if not isinstance(token_type, str) or not token_type.strip():
        errors.append(f"{location}: token 缺少非空字符串 $type")

    description = node.get("$description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{location}: token 缺少非空字符串 $description")

    extensions = node.get("$extensions")
    if not isinstance(extensions, dict):
        errors.append(f"{location}: token 缺少对象 $extensions")
        return
    provenance = extensions.get(EXTENSION_KEY)
    if not isinstance(provenance, dict):
        errors.append(f'{location}: token 缺少 $extensions["{EXTENSION_KEY}"] 对象')
        return

    status = provenance.get("status")
    if status not in VALID_STATUSES:
        errors.append(
            f"{location}: status 必须是 {', '.join(sorted(VALID_STATUSES))} 之一"
        )

    confidence = provenance.get("confidence")
    if confidence not in VALID_CONFIDENCES:
        errors.append(
            f"{location}: confidence 必须是 {', '.join(sorted(VALID_CONFIDENCES))} 之一"
        )

    confidence_reason = provenance.get("confidenceReason")
    if not isinstance(confidence_reason, str) or not confidence_reason.strip():
        errors.append(f"{location}: confidenceReason 必须是非空字符串")

    scope = provenance.get("scope")
    if not isinstance(scope, dict) or not scope:
        errors.append(f"{location}: scope 必须是非空对象")

    evidence_ids = provenance.get("evidenceIds")
    validate_evidence_ids(evidence_ids, location, errors)
    if isinstance(evidence_ids, list):
        if status != "adapted" and not evidence_ids:
            errors.append(f"{location}: status={status!r} 时 evidenceIds 不得为空")
    if status == "adapted":
        rationale = provenance.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(f"{location}: adapted token 必须提供非空 rationale")


def is_iso_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not ISO_DATETIME_RE.fullmatch(value):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def validate_root_metadata(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    extensions = data.get("$extensions")
    if not isinstance(extensions, dict):
        return ["design-tokens.json: 根节点缺少对象 $extensions"]
    metadata = extensions.get(EXTENSION_KEY)
    if not isinstance(metadata, dict):
        return [
            f'design-tokens.json: 根节点缺少 $extensions["{EXTENSION_KEY}"] 对象'
        ]

    format_version = metadata.get("formatVersion")
    if not isinstance(format_version, str) or not format_version.strip():
        errors.append("design-tokens.json: 根扩展 formatVersion 必须是非空字符串")

    generated_at = metadata.get("generatedAt")
    if not is_iso_datetime(generated_at):
        errors.append(
            "design-tokens.json: 根扩展 generatedAt 必须是带时区的 ISO-8601 date-time"
        )

    targets = metadata.get("targets")
    if not isinstance(targets, list) or not targets:
        errors.append("design-tokens.json: 根扩展 targets 必须是非空数组")
    elif any(not isinstance(target, str) or not target.strip() for target in targets):
        errors.append("design-tokens.json: 根扩展 targets 的每一项必须是非空字符串")

    document_status = metadata.get("documentStatus")
    if document_status not in VALID_DOCUMENT_STATUSES:
        errors.append(
            "design-tokens.json: 根扩展 documentStatus 必须是 "
            + ", ".join(sorted(VALID_DOCUMENT_STATUSES))
            + " 之一"
        )
    return errors


def validate_tokens_data(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["design-tokens.json: 顶层必须是 JSON 对象"]

    errors.extend(validate_root_metadata(data))
    token_count = 0

    def walk(node: Any, path: tuple[str, ...], *, is_root: bool = False) -> None:
        nonlocal token_count
        if not isinstance(node, dict):
            return
        if is_token_candidate(node):
            token_count += 1
            validate_token(node, path, errors)
            return
        allowed_metadata = {"$description", "$extensions"}
        if not is_root:
            allowed_metadata.add("$type")
        for key, value in node.items():
            if key.startswith("$"):
                if key not in allowed_metadata:
                    errors.append(
                        f"{format_path(path)}: group 包含 schema 未允许的键 {key!r}"
                    )
                elif key == "$extensions" and not isinstance(value, dict):
                    errors.append(f"{format_path(path)}.$extensions 必须是对象")
                continue
            if not isinstance(value, dict):
                errors.append(
                    f"{format_path(path + (key,))}: group 子节点必须是对象"
                )
                continue
            walk(value, path + (key,))

    walk(data, (), is_root=True)
    if token_count == 0:
        errors.append("design-tokens.json: 未找到任何包含 $value 的 token")
    return errors


def validate_tokens_json(text: str) -> list[str]:
    try:
        data = json.loads(text, object_pairs_hook=reject_duplicate_keys)
    except DuplicateKeyError as exc:
        return [f"design-tokens.json: {exc}"]
    except json.JSONDecodeError as exc:
        return [
            "design-tokens.json:"
            f"{exc.lineno}:{exc.colno}: JSON 解析失败: {exc.msg}"
        ]
    return validate_tokens_data(data)


def token_evidence_ids(text: str) -> set[str]:
    try:
        data = json.loads(text, object_pairs_hook=reject_duplicate_keys)
    except (json.JSONDecodeError, DuplicateKeyError):
        return set()

    evidence_ids: set[str] = set()

    def walk(node: Any) -> None:
        if not isinstance(node, dict):
            return
        if is_token_candidate(node):
            extensions = node.get("$extensions")
            provenance = extensions.get(EXTENSION_KEY) if isinstance(extensions, dict) else None
            ids = provenance.get("evidenceIds") if isinstance(provenance, dict) else None
            if isinstance(ids, list):
                evidence_ids.update(item for item in ids if isinstance(item, str))
            return
        for key, value in node.items():
            if not key.startswith("$"):
                walk(value)

    walk(data)
    return evidence_ids


def validate_checklist(text: str) -> list[str]:
    errors: list[str] = []
    fence_char: str | None = None
    fence_length = 0
    task_count = 0
    visible_task_count = 0
    has_review_table = False

    for line_no, line in enumerate(text.splitlines(), start=1):
        fence_match = FENCE_RE.match(line)
        if fence_char is None and fence_match:
            marker = fence_match.group(1)
            fence_char = marker[0]
            fence_length = len(marker)
            continue
        if fence_char is not None:
            closing_fence = re.compile(
                rf"^\s{{0,3}}{re.escape(fence_char)}{{{fence_length},}}\s*$"
            )
            if closing_fence.match(line):
                fence_char = None
                fence_length = 0
                continue

        if TASK_RE.match(line):
            task_count += 1
            if fence_char is None:
                visible_task_count += 1
            else:
                errors.append(
                    "design-review-checklist.md:"
                    f"{line_no}: Markdown 任务项不得放在 fenced code block 内"
                )

        if fence_char is None and line.strip().startswith("|"):
            cells = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
            has_id = "id" in cells or "检查 id" in cells
            has_check = "检查项" in cells or "check" in cells
            has_status = "状态" in cells or "status" in cells
            has_evidence = "证据" in cells or "evidence" in cells
            if has_id and has_check and has_status and has_evidence:
                has_review_table = True

    if task_count == 0 and not has_review_table:
        errors.append("design-review-checklist.md: 未找到可执行任务项或审查表")
    elif visible_task_count == 0:
        if not has_review_table:
            errors.append("design-review-checklist.md: 没有可直接勾选的任务项")
    if fence_char is not None:
        errors.append("design-review-checklist.md: fenced code block 未闭合")
    return errors


def read_required_files(
    output_dir: Path, required_files: tuple[str, ...]
) -> tuple[dict[str, str], list[str]]:
    contents: dict[str, str] = {}
    errors: list[str] = []
    for filename in required_files:
        path = output_dir / filename
        if not path.is_file():
            errors.append(f"{filename}: 文件不存在")
            continue
        try:
            content = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{filename}: 无法读取 UTF-8 文本: {exc}")
            continue
        if not content.strip():
            errors.append(f"{filename}: 文件为空")
        contents[filename] = content
    return contents, errors


def validate_output_dir(output_dir: Path, mode: str = "full") -> list[str]:
    if not output_dir.is_dir():
        return [f"输出目录不存在或不是目录: {output_dir}"]

    contents, errors = read_required_files(output_dir, MODE_FILES[mode])
    if "design-tokens.json" in MODE_FILES[mode]:
        errors.extend(validate_bundled_schema_contract())
    for filename, content in contents.items():
        errors.extend(find_placeholders(filename, content))

    tokens_text = contents.get("design-tokens.json")
    if tokens_text is not None:
        errors.extend(validate_tokens_json(tokens_text))

    checklist_text = contents.get("design-review-checklist.md")
    if checklist_text is not None:
        errors.extend(validate_checklist(checklist_text))

    spec_text = contents.get("design-spec.md")
    if spec_text is not None and tokens_text is not None:
        known_evidence_ids = set(re.findall(r"(?<![A-Za-z0-9])E-[0-9]{3,}(?![A-Za-z0-9])", spec_text))
        missing_ids = sorted(token_evidence_ids(tokens_text) - known_evidence_ids)
        for evidence_id in missing_ids:
            errors.append(
                "design-tokens.json: 证据 ID "
                f"{evidence_id!r} 未在 design-spec.md 中出现"
            )
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="校验设计规范、DTCG token 与设计验收清单。"
    )
    parser.add_argument("output_dir", type=Path, help="包含待校验输出物的目录")
    parser.add_argument(
        "--mode",
        choices=tuple(MODE_FILES),
        default="full",
        help="校验完整实施包或指定的单一产物（默认: full）",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        errors = validate_output_dir(args.output_dir, args.mode)
    except Exception as exc:  # Keep automation callers from mistaking a crash for success.
        print(f"校验器内部错误: {exc}", file=sys.stderr)
        return 2

    if errors:
        print(f"校验失败，共 {len(errors)} 项：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"校验通过: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
