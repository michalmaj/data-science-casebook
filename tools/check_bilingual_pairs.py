"""Fail if any Markdown file is missing its .pl.md sibling.

Only considers files git would track (respects .gitignore), so CLAUDE.md,
do_poczytania.txt, and anything under docs/ are correctly skipped.
"""

import re
import subprocess
import sys
from pathlib import Path

_HEADER_RE = re.compile(r"^(#{1,6})\s")


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


def header_levels(path: Path) -> list[int]:
    levels = []
    for line in path.read_text().splitlines():
        match = _HEADER_RE.match(line)
        if match:
            levels.append(len(match.group(1)))
    return levels


def structural_drift(md_files: list[Path]) -> list[tuple[Path, Path, str]]:
    """Return (source, sibling, reason) for every EN/PL pair whose header-level
    sequence differs. Ignores prose content — only the # / ## / ### nesting
    structure — so natural differences in translation length never trigger
    a false positive; this enforces CONTRIBUTING.md's structural-parity
    contract, not word-for-word parity.
    """
    known = set(md_files)
    drifted = []
    for md_file in md_files:
        if md_file.name.endswith(".pl.md"):
            continue
        sibling = md_file.with_name(md_file.stem + ".pl.md")
        if sibling not in known:
            continue  # already reported by missing_pl_siblings
        source_levels = header_levels(md_file)
        sibling_levels = header_levels(sibling)
        if source_levels != sibling_levels:
            if len(source_levels) != len(sibling_levels):
                reason = f"{len(source_levels)} headers vs {len(sibling_levels)}"
            else:
                reason = f"header level sequence differs: {source_levels} vs {sibling_levels}"
            drifted.append((md_file, sibling, reason))
    return drifted


def main() -> int:
    md_files = markdown_files()
    missing = missing_pl_siblings(md_files)
    if missing:
        print("Missing .pl.md sibling for:")
        for path in missing:
            print(f"  {path}")
        return 1

    drifted = structural_drift(md_files)
    if drifted:
        print("Structural drift between EN/PL pairs (header levels don't match):")
        for source, sibling, reason in drifted:
            print(f"  {source} vs {sibling}: {reason}")
        return 1

    source_count = len([f for f in md_files if not f.name.endswith(".pl.md")])
    print(f"All {source_count} Markdown file(s) have a .pl.md sibling and matching structure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
