"""Flag a few recurring Polish-prose style issues for a human to look at.

This is not an AI-detector and is not trying to be one — it only catches
patterns this course has deliberately decided to move away from: dual-gender
verb forms written as "zrobiłeś/zrobiłaś", English-style decimal points
outside of code, and a short, explicit list of Polish-English hybrids we're
phasing out. It always exits 0 and never blocks CI — it's a lint for editors,
not a gate.

Run with: uv run python tools/check_polish_style.py
"""

import re
import subprocess
import sys
from pathlib import Path

_CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")

# Matches dual-gender pairs like "zrobiłeś/zrobiłaś", "musiał/musiała",
# "gotów/gotowa" — a word ending in a past-tense/adjective gender marker,
# a slash, then the feminine counterpart. The feminine side can carry its
# own trailing "ś" (the direct 2nd-person form, "zrobiłaś") in addition to
# the plain 3rd-person/adjective form ("zrobiła", "gotowa") — both occur in
# this repo's prose, and missing the "ś" variant was an earlier false
# negative that let real dual-gender forms through uncaught.
_DUAL_GENDER_RE = re.compile(
    r"\b[A-Za-zĄąĘęÓóŁłŚśŻżŹźĆćŃń]*(?:ł[aeiouy]?ś?|ów|gotów)"
    r"/[A-Za-zĄąĘęÓóŁłŚśŻżŹźĆćŃń]*(?:ł[aeiouy]ś?|owa)\b"
)

# Short adjective pairs that don't fit the participle pattern above (no "ł"
# or "ów" stem) but are just as gendered — "sam/sama", "gotowy/gotowa",
# "pewny/pewna". Kept as an explicit list rather than widening the main
# regex, which would start matching unrelated word pairs.
_SHORT_ADJECTIVE_PAIRS = [
    "sam/sama",
    "gotowy/gotowa",
    "pewny/pewna",
    "zdecydowany/zdecydowana",
]

# English-style decimal point in prose, e.g. "0.5" where Polish prose should
# read "0,5". Only meaningful outside of code, which is stripped before this
# runs.
_DECIMAL_POINT_RE = re.compile(r"\b\d+\.\d+\b")

# Polish-English hybrids we've decided to eliminate from prose. Extend this
# list as the team agrees on more — it's deliberately short and explicit
# rather than a general anglicism detector.
_ANGLICISM_RES = [
    re.compile(r"\bbaseline'[a-ząęółśżźćń]+\b", re.IGNORECASE),
    re.compile(r"\bfeature'[a-ząęółśżźćń]+\b", re.IGNORECASE),
    re.compile(r"\bmodel'[a-ząęółśżźćń]+\b", re.IGNORECASE),
    re.compile(r"\bdataset'[a-ząęółśżźćń]+\b", re.IGNORECASE),
]

# Phrases that are fine once but read as filler/ritual when they recur. Flag
# any occurrence for a human to reconsider, rather than trying to guess a
# "too many" threshold.
_RITUAL_PHRASES = [
    "warto zauważyć",
    "kluczowym aspektem",
    "kluczowe jest to, że",
    "teraz twoja kolej",
    "twój ruch",
]

# "faktycznie" is a legitimate emphasis word in small doses, but dense use
# reads as a verbal tic. Only warn above a per-file threshold, not on every
# occurrence.
_FAKTYCZNIE_WARN_THRESHOLD = 4


def strip_code(text: str) -> str:
    """Remove fenced and inline code spans so code identifiers never trigger a match."""
    text = _CODE_FENCE_RE.sub("", text)
    return _INLINE_CODE_RE.sub("", text)


def tracked_pl_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.pl.md"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [Path(line) for line in result.stdout.splitlines() if line]


def check_file(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    prose = strip_code(raw)
    warnings = []

    dual_gender_hits = sorted(set(_DUAL_GENDER_RE.findall(raw)))
    lowered_raw = raw.lower()
    for pair in _SHORT_ADJECTIVE_PAIRS:
        if pair in lowered_raw:
            dual_gender_hits.append(pair)
    if dual_gender_hits:
        joined = ", ".join(dual_gender_hits)
        warnings.append(f"dual-gender forms (zrobiłeś/zrobiłaś style): {joined}")

    decimal_hits = sorted(set(_DECIMAL_POINT_RE.findall(prose)))
    if decimal_hits:
        joined = ", ".join(decimal_hits)
        warnings.append(f"English-style decimal point in prose (use a comma): {joined}")

    for pattern in _ANGLICISM_RES:
        hits = sorted(set(pattern.findall(prose)))
        if hits:
            warnings.append(f"Polish-English hybrid to eliminate: {', '.join(hits)}")

    lowered = prose.lower()
    for phrase in _RITUAL_PHRASES:
        if phrase in lowered:
            warnings.append(f'ritual phrase: "{phrase}"')

    faktycznie_count = lowered.count("faktycznie")
    if faktycznie_count > _FAKTYCZNIE_WARN_THRESHOLD:
        warnings.append(
            f'"faktycznie" appears {faktycznie_count} times — check each use adds meaning'
        )

    return warnings


def main() -> int:
    files = tracked_pl_files()
    total_warnings = 0
    for path in files:
        warnings = check_file(path)
        if warnings:
            print(f"{path}:")
            for warning in warnings:
                print(f"  - {warning}")
            total_warnings += len(warnings)

    if total_warnings:
        print(f"\n{total_warnings} warning(s) in {len(files)} file(s) — for review, not a CI gate.")
    else:
        print(f"No style warnings in {len(files)} Polish file(s).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
