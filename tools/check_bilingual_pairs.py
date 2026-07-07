"""Fail if any Markdown file is missing its .pl.md sibling.

Only considers files git would track (respects .gitignore), so CLAUDE.md,
do_poczytania.txt, and anything under docs/ are correctly skipped.
"""

import subprocess
import sys
from pathlib import Path


def markdown_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [Path(line) for line in result.stdout.splitlines() if line]


def missing_pl_siblings(md_files: list[Path]) -> list[Path]:
    known = set(md_files)
    missing = []
    for md_file in md_files:
        if md_file.name.endswith(".pl.md"):
            continue
        sibling = md_file.with_name(md_file.stem + ".pl.md")
        if sibling not in known:
            missing.append(md_file)
    return missing


def main() -> int:
    md_files = markdown_files()
    missing = missing_pl_siblings(md_files)
    if missing:
        print("Missing .pl.md sibling for:")
        for path in missing:
            print(f"  {path}")
        return 1
    source_count = len([f for f in md_files if not f.name.endswith(".pl.md")])
    print(f"All {source_count} Markdown file(s) have a .pl.md sibling.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
