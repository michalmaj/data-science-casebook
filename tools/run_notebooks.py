"""Execute every lesson notebook with solution.py swapped into task.py.

task.py is a student stub (its functions raise NotImplementedError), so a
notebook's real behavior can only be verified by temporarily running it
against the reference solution. task.py is always restored afterward,
regardless of outcome — this script is safe to run both in CI's throwaway
checkout and against a real local working tree.

Run with: uv run python tools/run_notebooks.py
"""

import contextlib
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import nbformat

REPO_ROOT = Path(__file__).resolve().parent.parent

# Notebooks with a DATASET_NAME + if/elif/else dispatch that only exercises
# one branch by default. Hardcoded rather than auto-detected: this is a
# small, well-known, rarely-changing set, and auto-detecting "which
# notebooks branch on what values" via regex/parsing would be more fragile
# than keeping this list in sync by hand when a new multi-branch lesson is
# added.
MULTI_BRANCH_NOTEBOOKS: dict[str, list[str]] = {
    "cases/capstone/lessons/04_modeling/lesson.ipynb": [
        "clinic_wait_times",
        "lendwell_loan_default",
        "retail_store_segments",
    ],
    "cases/capstone/lessons/05_evaluation/lesson.ipynb": [
        "clinic_wait_times",
        "lendwell_loan_default",
        "retail_store_segments",
    ],
    "cases/capstone/lessons/06_synthesis_decision_note/lesson.ipynb": [
        "clinic_wait_times",
        "lendwell_loan_default",
        "retail_store_segments",
    ],
    "cases/capstone/lessons/07_packaging_for_deployment/lesson.ipynb": [
        "clinic_wait_times",
        "lendwell_loan_default",
        "retail_store_segments",
    ],
}


@dataclass
class ExecutionResult:
    lesson: str
    branch: str | None
    passed: bool
    error: str

    @property
    def label(self) -> str:
        return self.lesson if self.branch is None else f"{self.lesson} [{self.branch}]"


def find_lesson_notebooks() -> list[Path]:
    return sorted(REPO_ROOT.glob("cases/*/lessons/*/lesson.ipynb"))


@contextlib.contextmanager
def solution_as_task(lesson_dir: Path):
    """Temporarily overwrite task.py with solution.py's content, then restore it."""
    task_path = lesson_dir / "task.py"
    solution_path = lesson_dir / "solution.py"
    original = task_path.read_text()
    try:
        task_path.write_text(solution_path.read_text())
        yield
    finally:
        task_path.write_text(original)


def execute_notebook(notebook_path: Path) -> tuple[bool, str]:
    """Execute notebook_path via nbconvert, writing output to a throwaway location.

    notebook_path must already be in its lesson's own directory (alongside
    task.py) — nbconvert resolves `from task import ...` relative to the
    executing notebook file's own directory, not the process's cwd.
    """
    output_dir = REPO_ROOT / ".nbconvert-ci-output"
    output_dir.mkdir(exist_ok=True)
    # notebook_path.stem is "lesson" (or ".ci_patched_<dataset>") for every
    # lesson, and lesson directory names like "01_defining_the_question"
    # repeat across cases — use the full relative path to guarantee unique
    # output filenames instead of silently overwriting between cases.
    unique_name = notebook_path.relative_to(REPO_ROOT).as_posix().replace("/", "__").lstrip(".")
    output_path = output_dir / f"{unique_name}"
    result = subprocess.run(
        [
            "uv",
            "run",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            str(notebook_path),
            "--output",
            str(output_path),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return True, ""
    error_lines = result.stderr.strip().splitlines()
    summary = "\n".join(error_lines[-20:])
    return False, summary


@contextlib.contextmanager
def patched_dataset_name_notebook(notebook_path: Path, dataset_name: str):
    """Write a throwaway copy of notebook_path, alongside it, with DATASET_NAME patched.

    Yields the copy's path; always deletes the copy afterward, regardless
    of outcome. Written alongside the original (not in a separate temp
    directory) because `from task import ...` inside the notebook resolves
    relative to the executing notebook file's own directory.
    """
    nb = nbformat.read(notebook_path, as_version=4)
    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = cell["source"]
        if isinstance(source, list):
            source = "".join(source)
        has_assignment = any(
            line.strip().startswith("DATASET_NAME =") for line in source.splitlines()
        )
        if patched or not has_assignment:
            continue
        new_lines = []
        for line in source.splitlines():
            if line.strip().startswith("DATASET_NAME ="):
                new_lines.append(f'DATASET_NAME = "{dataset_name}"')
            else:
                new_lines.append(line)
        cell["source"] = "\n".join(new_lines)
        patched = True
    if not patched:
        raise RuntimeError(f"No DATASET_NAME assignment line found in {notebook_path}")

    patched_path = notebook_path.parent / f".ci_patched_{dataset_name}.ipynb"
    nbformat.write(nb, patched_path)
    try:
        yield patched_path
    finally:
        patched_path.unlink(missing_ok=True)


def run_single_branch(notebook_path: Path, lesson_label: str) -> ExecutionResult:
    passed, error = execute_notebook(notebook_path)
    return ExecutionResult(lesson=lesson_label, branch=None, passed=passed, error=error)


def run_multi_branch(
    notebook_path: Path, lesson_label: str, dataset_names: list[str]
) -> list[ExecutionResult]:
    results = []
    for dataset_name in dataset_names:
        with patched_dataset_name_notebook(notebook_path, dataset_name) as patched_path:
            passed, error = execute_notebook(patched_path)
        results.append(
            ExecutionResult(lesson=lesson_label, branch=dataset_name, passed=passed, error=error)
        )
    return results


def main() -> int:
    notebooks = find_lesson_notebooks()
    if not notebooks:
        print("No lesson notebooks found under cases/*/lessons/*/lesson.ipynb — check discovery.")
        return 1

    results: list[ExecutionResult] = []
    for notebook_path in notebooks:
        lesson_dir = notebook_path.parent
        # .as_posix() (not str()) so MULTI_BRANCH_NOTEBOOKS's forward-slash
        # keys still match if this ever runs on Windows, where str(Path)
        # uses backslashes.
        rel_notebook = notebook_path.relative_to(REPO_ROOT).as_posix()
        lesson_label = lesson_dir.relative_to(REPO_ROOT).as_posix()
        with solution_as_task(lesson_dir):
            if rel_notebook in MULTI_BRANCH_NOTEBOOKS:
                dataset_names = MULTI_BRANCH_NOTEBOOKS[rel_notebook]
                results.extend(run_multi_branch(notebook_path, lesson_label, dataset_names))
            else:
                results.append(run_single_branch(notebook_path, lesson_label))

    passed = [r for r in results if r.passed]
    failed = [r for r in results if not r.passed]

    print(f"\n{'=' * 70}")
    print(f"Notebook execution summary: {len(passed)}/{len(results)} passed")
    print(f"{'=' * 70}")
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"  {status}  {result.label}")

    if failed:
        print(f"\n{len(failed)} execution(s) failed:\n")
        for result in failed:
            print(f"--- {result.label} ---")
            print(result.error)
            print()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
