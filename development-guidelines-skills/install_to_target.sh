#!/usr/bin/env bash
set -euo pipefail

source_dir="$(cd "$(dirname "$0")" && pwd -P)"
target=""
update=0
force=0
dry_run=0

usage() {
  echo "Usage: $0 [target] [--update] [--force] [--dry-run]" >&2
}

while (($#)); do
  case "$1" in
    --update)
      update=1
      ;;
    --force)
      force=1
      ;;
    --dry-run)
      dry_run=1
      ;;
    --target)
      shift
      if (($# == 0)) || [[ -n "$target" ]]; then
        usage
        exit 2
      fi
      target="$1"
      ;;
    --*)
      usage
      echo "Unknown option: $1" >&2
      exit 2
      ;;
    *)
      if [[ -n "$target" ]]; then
        usage
        echo "Only one target may be provided." >&2
        exit 2
      fi
      target="$1"
      ;;
  esac
  shift
done

if ((force && !update)); then
  usage
  echo "--force requires --update." >&2
  exit 2
fi

if [[ -n "${PYTHON:-}" ]]; then
  python_bin="$PYTHON"
elif command -v python3 >/dev/null 2>&1; then
  python_bin="$(command -v python3)"
elif command -v python >/dev/null 2>&1; then
  python_bin="$(command -v python)"
else
  echo "Python 3 is required to validate and install this Skill suite." >&2
  exit 1
fi

arguments=(-B "$source_dir/scripts/install_suite.py")
[[ -n "$target" ]] && arguments+=("$target")
if ((update)); then arguments+=(--update); fi
if ((force)); then arguments+=(--force); fi
if ((dry_run)); then arguments+=(--dry-run); fi

exec "$python_bin" "${arguments[@]}"
