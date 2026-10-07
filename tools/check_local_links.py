"""Flag Markdown links that point at a local file or anchor that doesn't exist.

Walks every tracked *.md file, extracts [text](target) links whose target is
local (not http(s):// or mailto:), resolves path targets relative to the
linking file's directory, and checks the file exists on disk. A target with
an anchor (#heading or path#heading) also gets a best-effort check of the
anchor against the target file's actual headers, using a GitHub-style slug
(lowercase, spaces to hyphens, punctuation stripped) — this is approximate
(it doesn't handle duplicate-heading disambiguation suffixes like "-1"), so
treat anchor misses as a hint to double check by eye, not as certain as a
missing file.

Always exits 0 — this is a report for a human to act on, not a CI gate.

Run with: uv run python tools/check_local_links.py
"""

import re
import subprocess
import sys
from pathlib import Path

_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
_HEADER_RE = re.compile(r"^(#{1,6})\s+(.+)$")
_PUNCT_RE = re.compile(r"[^\w\- ]")


def markdown_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [Path(line) for line in result.stdout.splitlines() if line]


def is_local(target: str) -> bool:
    if target.startswith(("http://", "https://", "mailto:")):
        return False
    return True


def slugify(heading: str) -> str:
    """Approximate GitHub's heading-to-anchor slug rule."""
    text = heading.strip().lower()
    text = _PUNCT_RE.sub("", text)
    text = text.replace(" ", "-")
    return text


def anchors_in(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    anchors = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = _HEADER_RE.match(line)
        if match:
            anchors.add(slugify(match.group(2)))
    return anchors


def check_file(md_file: Path) -> tuple[int, list[tuple[int, str, str]]]:
    """Return (local_link_count, [(line_no, target, reason), ...]) for a file."""
    broken = []
    local_count = 0
    lines = md_file.read_text(encoding="utf-8", errors="replace").splitlines()
    for line_no, line in enumerate(lines, start=1):
        for _text, target in _LINK_RE.findall(line):
            if not is_local(target):
                continue
            local_count += 1
            path_part, _, anchor_part = target.partition("#")

            if path_part:
                resolved = (md_file.parent / path_part).resolve()
                if resolved.is_dir():
                    if anchor_part:
                        broken.append((line_no, target, "anchor on a directory link"))
                    continue
                if not resolved.is_file():
                    broken.append((line_no, target, "file not found"))
                    continue
                check_target = resolved
            else:
                # Pure anchor like "#some-heading" — check against this file.
                check_target = md_file

            if anchor_part:
                if slugify(anchor_part) not in anchors_in(check_target):
                    broken.append((line_no, target, "anchor not found"))

    return local_count, broken


def main() -> int:
    files = markdown_files()
    total_links = 0
    total_broken = 0

    for md_file in files:
        local_count, broken = check_file(md_file)
        total_links += local_count
        for line_no, target, reason in broken:
            print(f"{md_file}:{line_no} -> {target}  [{reason}]")
            total_broken += 1

    print(f"\nChecked {total_links} local link(s) in {len(files)} file(s); {total_broken} broken.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
