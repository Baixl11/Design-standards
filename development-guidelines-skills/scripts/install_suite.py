#!/usr/bin/env python3
"""Safely install the cataloged development-guidelines Skills."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterator

from validate_suite import read_json, validate_suite


MANIFEST_NAME = ".development-guidelines-install.json"
MANIFEST_SCHEMA_VERSION = 1


class InstallError(RuntimeError):
    pass


@dataclass(frozen=True)
class InstallAction:
    name: str
    source: Path
    destination: Path
    kind: str
    entries: dict[str, str]


@dataclass(frozen=True)
class InstallResult:
    installed: int
    updated: int
    up_to_date: int
    skipped: int
    backup_root: Path | None


def is_link_like(path: Path) -> bool:
    if path.is_symlink():
        return True
    is_junction = getattr(path, "is_junction", None)
    return bool(is_junction and is_junction())


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def assert_disjoint(source: Path, target: Path) -> None:
    source_real = source.resolve(strict=True)
    target_real = target.expanduser().resolve(strict=False)
    if source_real == target_real or is_within(target_real, source_real) or is_within(source_real, target_real):
        raise InstallError(f"source and target must not overlap: source={source_real}; target={target_real}")


def assert_plain_tree(root: Path, label: str) -> None:
    if is_link_like(root):
        raise InstallError(f"{label} must not be a symlink or junction: {root}")
    for path in root.rglob("*"):
        if is_link_like(path):
            raise InstallError(f"{label} contains a symlink or junction: {path}")


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def hash_tree(root: Path) -> dict[str, str]:
    if not root.is_dir() or is_link_like(root):
        raise InstallError(f"expected a plain directory: {root}")
    entries: dict[str, str] = {}
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        if is_link_like(path):
            raise InstallError(f"directory tree contains a symlink or junction: {path}")
        relative = path.relative_to(root).as_posix()
        if path.is_dir():
            entries[f"{relative}/"] = "directory"
        elif path.is_file():
            entries[relative] = hash_file(path)
        else:
            raise InstallError(f"unsupported filesystem entry: {path}")
    return entries


def load_manifest(target: Path) -> dict[str, object]:
    path = target / MANIFEST_NAME
    if not path.exists():
        return {
            "schema_version": MANIFEST_SCHEMA_VERSION,
            "suite": "development-guidelines",
            "suite_version": None,
            "skills": {},
        }
    if is_link_like(path) or not path.is_file():
        raise InstallError(f"install manifest must be a plain file: {path}")
    manifest, errors = read_json(path)
    if errors:
        raise InstallError(f"invalid install manifest {path}: {errors[0]}")
    if not isinstance(manifest, dict):
        raise InstallError(f"invalid install manifest root: {path}")
    if manifest.get("schema_version") != MANIFEST_SCHEMA_VERSION:
        raise InstallError(f"unsupported install manifest schema: {path}")
    if manifest.get("suite") != "development-guidelines":
        raise InstallError(f"install manifest belongs to another suite: {path}")
    skills = manifest.get("skills")
    if not isinstance(skills, dict):
        raise InstallError(f"install manifest skills must be an object: {path}")
    for name, record in skills.items():
        if not isinstance(name, str) or not isinstance(record, dict):
            raise InstallError(f"invalid Skill record in install manifest: {name!r}")
        entries = record.get("entries")
        if not isinstance(entries, dict) or any(
            not isinstance(key, str) or not isinstance(value, str)
            for key, value in entries.items()
        ):
            raise InstallError(f"invalid entries for {name!r} in install manifest")
    return manifest


def version_key(value: object) -> tuple[int, int, int] | None:
    if not isinstance(value, str):
        return None
    core = value.split("-", 1)[0].split(".")
    if len(core) != 3 or any(not item.isdigit() for item in core):
        return None
    return tuple(int(item) for item in core)  # type: ignore[return-value]


def load_catalog(source: Path) -> tuple[dict[str, object], list[str]]:
    errors = validate_suite(source)
    if errors:
        preview = "\n".join(f"- {error}" for error in errors[:20])
        suffix = "\n- ..." if len(errors) > 20 else ""
        raise InstallError(f"source suite validation failed:\n{preview}{suffix}")
    catalog, json_errors = read_json(source / "skill-catalog.json")
    if json_errors or not isinstance(catalog, dict):
        raise InstallError("cannot read validated skill-catalog.json")
    raw_skills = catalog.get("skills")
    if not isinstance(raw_skills, list):
        raise InstallError("catalog skills must be an array")
    names = [item.get("name") for item in raw_skills if isinstance(item, dict)]
    if not names or any(not isinstance(name, str) for name in names):
        raise InstallError("catalog contains no installable Skills")
    return catalog, [name for name in names if isinstance(name, str)]


def validate_destination(target: Path, name: str) -> Path:
    destination = target / name
    if destination.parent != target:
        raise InstallError(f"Skill destination escapes target: {destination}")
    if destination.exists() or is_link_like(destination):
        if is_link_like(destination):
            raise InstallError(f"refusing linked Skill destination: {destination}")
        if not destination.is_dir():
            raise InstallError(f"Skill destination exists but is not a directory: {destination}")
        assert_plain_tree(destination, "Skill destination")
    return destination


def manifest_entries(manifest: dict[str, object], name: str) -> dict[str, str] | None:
    skills = manifest.get("skills")
    if not isinstance(skills, dict):
        return None
    record = skills.get(name)
    if not isinstance(record, dict):
        return None
    entries = record.get("entries")
    if not isinstance(entries, dict):
        return None
    if any(not isinstance(key, str) or not isinstance(value, str) for key, value in entries.items()):
        return None
    return dict(entries)


def plan_install(
    source: Path,
    target: Path,
    names: list[str],
    manifest: dict[str, object],
    update: bool,
    force: bool,
) -> tuple[list[InstallAction], list[InstallAction], list[str]]:
    changes: list[InstallAction] = []
    current: list[InstallAction] = []
    skipped: list[str] = []
    for name in names:
        source_dir = source / name
        if not source_dir.is_dir() or is_link_like(source_dir):
            raise InstallError(f"cataloged Skill is not a plain directory: {source_dir}")
        assert_plain_tree(source_dir, "source Skill")
        source_entries = hash_tree(source_dir)
        destination = validate_destination(target, name)
        if not destination.exists():
            changes.append(InstallAction(name, source_dir, destination, "install", source_entries))
            continue

        destination_entries = hash_tree(destination)
        if not update:
            skipped.append(name)
            continue
        if destination_entries == source_entries:
            current.append(InstallAction(name, source_dir, destination, "up-to-date", source_entries))
            continue

        recorded = manifest_entries(manifest, name)
        if recorded is None and not force:
            raise InstallError(
                f"refusing to update unmanaged Skill {name!r}; rerun with --force to preserve it in a backup"
            )
        if recorded is not None and destination_entries != recorded and not force:
            raise InstallError(
                f"refusing to overwrite modified Skill {name!r}; rerun with --force to preserve it in a backup"
            )
        changes.append(InstallAction(name, source_dir, destination, "update", source_entries))
    return changes, current, skipped


@contextmanager
def install_lock(parent: Path, target_name: str) -> Iterator[None]:
    token = f"pid={os.getpid()} uuid={uuid.uuid4()}"
    lock_path = parent / f".{target_name}-development-guidelines-install.lock"
    try:
        descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise InstallError(f"another install may be running; lock exists: {lock_path}") from exc
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(token)
        yield
    finally:
        try:
            if lock_path.read_text(encoding="utf-8") == token:
                lock_path.unlink()
        except OSError:
            pass


def remove_generated_tree(path: Path, parent: Path, prefix: str) -> None:
    if not path.exists():
        return
    if path.parent.resolve(strict=True) != parent.resolve(strict=True) or not path.name.startswith(prefix):
        raise InstallError(f"refusing to clean unexpected staging path: {path}")
    shutil.rmtree(path)


def write_manifest(
    target: Path,
    catalog: dict[str, object],
    previous: dict[str, object],
    managed: list[InstallAction],
) -> None:
    previous_skills = previous.get("skills")
    skills: dict[str, object] = dict(previous_skills) if isinstance(previous_skills, dict) else {}
    for action in managed:
        skills[action.name] = {"entries": action.entries}
    payload = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "suite": "development-guidelines",
        "suite_version": catalog.get("suite_version"),
        "installed_at": datetime.now(timezone.utc).isoformat(),
        "skills": skills,
    }
    temporary = target / f"{MANIFEST_NAME}.{uuid.uuid4().hex}.tmp"
    try:
        temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(temporary, target / MANIFEST_NAME)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def install_suite(
    source: Path,
    target: Path,
    *,
    update: bool = False,
    force: bool = False,
    dry_run: bool = False,
    output: Callable[[str], None] = print,
) -> InstallResult:
    source = source.expanduser().resolve(strict=True)
    target = target.expanduser().resolve(strict=False)
    assert_disjoint(source, target)
    if target.exists() and (is_link_like(target) or not target.is_dir()):
        raise InstallError(f"target must be a plain directory: {target}")

    catalog, names = load_catalog(source)
    manifest = load_manifest(target)
    existing_version = version_key(manifest.get("suite_version"))
    source_version = version_key(catalog.get("suite_version"))
    if update and existing_version and source_version and existing_version > source_version and not force:
        raise InstallError(
            f"refusing suite downgrade {manifest.get('suite_version')} -> {catalog.get('suite_version')}; use --force"
        )

    changes, current, skipped_names = plan_install(source, target, names, manifest, update, force)
    for action in changes:
        output(f"{action.kind.title()}: {action.name}")
    for action in current:
        output(f"Up-to-date: {action.name}")
    for name in skipped_names:
        output(f"Skip existing Skill: {name}")
    if dry_run:
        output(f"Dry run target: {target}")
        return InstallResult(
            installed=sum(action.kind == "install" for action in changes),
            updated=sum(action.kind == "update" for action in changes),
            up_to_date=len(current),
            skipped=len(skipped_names),
            backup_root=None,
        )

    target.parent.mkdir(parents=True, exist_ok=True)
    if is_link_like(target.parent):
        raise InstallError(f"target parent must not be a symlink or junction: {target.parent}")

    transaction = uuid.uuid4().hex
    stage_root = target.parent / f".{target.name}-development-guidelines-stage-{transaction}"
    backup_root = (
        target.parent
        / f".{target.name}-development-guidelines-backups"
        / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{transaction}"
    )
    swapped: list[tuple[InstallAction, Path | None]] = []

    with install_lock(target.parent, target.name):
        try:
            target.mkdir(parents=True, exist_ok=True)
            for action in changes:
                staged = stage_root / action.name
                staged.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(action.source, staged)
                if hash_tree(staged) != action.entries:
                    raise InstallError(f"staged copy hash mismatch: {action.name}")

            for action in changes:
                staged = stage_root / action.name
                backup: Path | None = None
                if action.destination.exists():
                    backup = backup_root / action.name
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(action.destination, backup)
                try:
                    os.replace(staged, action.destination)
                except BaseException:
                    if backup is not None and backup.exists():
                        os.replace(backup, action.destination)
                    raise
                swapped.append((action, backup))

            if changes or current:
                write_manifest(target, catalog, manifest, changes + current)
        except BaseException as exc:
            rollback_errors: list[str] = []
            for action, backup in reversed(swapped):
                try:
                    if action.destination.exists():
                        rollback_target = stage_root / f"rollback-{action.name}"
                        rollback_target.parent.mkdir(parents=True, exist_ok=True)
                        os.replace(action.destination, rollback_target)
                    if backup is not None and backup.exists():
                        os.replace(backup, action.destination)
                except OSError as rollback_exc:
                    rollback_errors.append(f"{action.name}: {rollback_exc}")
            detail = f"; rollback errors: {rollback_errors}" if rollback_errors else ""
            if isinstance(exc, InstallError):
                raise InstallError(f"{exc}{detail}") from exc
            raise InstallError(f"installation failed: {exc}{detail}") from exc
        finally:
            remove_generated_tree(
                stage_root,
                target.parent,
                f".{target.name}-development-guidelines-stage-",
            )

    kept_backup = backup_root if backup_root.exists() else None
    output(f"Target: {target}")
    output(
        "Installed: "
        f"{sum(action.kind == 'install' for action in changes)}; "
        f"updated: {sum(action.kind == 'update' for action in changes)}; "
        f"up-to-date: {len(current)}; skipped: {len(skipped_names)}"
    )
    if kept_backup is not None:
        output(f"Previous versions preserved at: {kept_backup}")
    return InstallResult(
        installed=sum(action.kind == "install" for action in changes),
        updated=sum(action.kind == "update" for action in changes),
        up_to_date=len(current),
        skipped=len(skipped_names),
        backup_root=kept_backup,
    )


def default_target() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    return Path(codex_home).expanduser() / "skills" if codex_home else Path.home() / ".codex" / "skills"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path, default=default_target())
    parser.add_argument("--update", action="store_true", help="replace cataloged managed Skills")
    parser.add_argument("--force", action="store_true", help="allow downgrade or modified/unmanaged targets")
    parser.add_argument("--dry-run", action="store_true", help="show the plan without writing")
    args = parser.parse_args(argv)
    if args.force and not args.update:
        parser.error("--force requires --update")
    try:
        install_suite(
            Path(__file__).resolve().parent.parent,
            args.target,
            update=args.update,
            force=args.force,
            dry_run=args.dry_run,
        )
    except InstallError as exc:
        print(f"Install failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
