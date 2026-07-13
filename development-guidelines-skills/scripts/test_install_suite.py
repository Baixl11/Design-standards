#!/usr/bin/env python3
"""Integration tests for the safe suite installer."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from install_suite import MANIFEST_NAME, InstallError, install_suite


ROOT = Path(__file__).resolve().parent.parent
SKILL_COUNT = 10


class InstallSuiteTests(unittest.TestCase):
    def test_install_skip_and_protected_update(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "skills"
            first = install_suite(ROOT, target, output=lambda _: None)
            self.assertEqual(SKILL_COUNT, first.installed)
            self.assertEqual(0, first.updated)

            manifest = json.loads((target / MANIFEST_NAME).read_text(encoding="utf-8"))
            self.assertEqual(SKILL_COUNT, len(manifest["skills"]))

            second = install_suite(ROOT, target, output=lambda _: None)
            self.assertEqual(SKILL_COUNT, second.skipped)

            installed_skill = target / "react-typescript-web-standard" / "SKILL.md"
            installed_skill.write_text(
                installed_skill.read_text(encoding="utf-8") + "\n<!-- local modification -->\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(InstallError, "refusing to overwrite modified Skill"):
                install_suite(ROOT, target, update=True, output=lambda _: None)

            forced = install_suite(ROOT, target, update=True, force=True, output=lambda _: None)
            self.assertEqual(1, forced.updated)
            self.assertEqual(SKILL_COUNT - 1, forced.up_to_date)
            self.assertIsNotNone(forced.backup_root)
            self.assertNotIn("local modification", installed_skill.read_text(encoding="utf-8"))
            backup_skill = forced.backup_root / "react-typescript-web-standard" / "SKILL.md"  # type: ignore[operator]
            self.assertIn("local modification", backup_skill.read_text(encoding="utf-8"))

    def test_dry_run_does_not_create_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "skills"
            result = install_suite(ROOT, target, dry_run=True, output=lambda _: None)
            self.assertEqual(SKILL_COUNT, result.installed)
            self.assertFalse(target.exists())

    def test_rejects_target_file_and_source_overlap(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target_file = Path(directory) / "skills"
            target_file.write_text("not a directory", encoding="utf-8")
            with self.assertRaisesRegex(InstallError, "target must be a plain directory"):
                install_suite(ROOT, target_file, dry_run=True, output=lambda _: None)

        overlap = ROOT / "installer-overlap-test"
        with self.assertRaisesRegex(InstallError, "must not overlap"):
            install_suite(ROOT, overlap, dry_run=True, output=lambda _: None)
        self.assertFalse(overlap.exists())

    def test_rejects_linked_destination_when_supported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "skills"
            external = root / "external"
            target.mkdir()
            external.mkdir()
            link = target / "react-typescript-web-standard"
            try:
                os.symlink(external, link, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"directory symlink creation is unavailable: {exc}")
            with self.assertRaisesRegex(InstallError, "linked Skill destination"):
                install_suite(ROOT, target, dry_run=True, output=lambda _: None)


if __name__ == "__main__":
    unittest.main()
