# data-science-casebook

[![CI](https://github.com/michalmaj/data-science-casebook/actions/workflows/ci.yml/badge.svg)](https://github.com/michalmaj/data-science-casebook/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

From messy questions to defensible conclusions.

## What this is

`data-science-casebook` is a case-study-driven Data Science course. It is not a Python syntax course — it teaches the analytical path: **problem → data → exploration → model → evaluation → communication**. Python, pandas, and scikit-learn are the workshop, not the subject.

Each case tells a small story: an organization has a problem, the data is incomplete or ambiguous, someone expects an answer, and you decide what can honestly be concluded from it. This course assumes you already have Python fundamentals and a first pass at machine learning concepts.

## Course structure

Four cases, each a full analytical cycle, with the amount of guidance decreasing as you go:

| Case | Scenario | Technique | Lessons | Guidance |
|---|---|---|---|---|
| [Case 1 — Regression](cases/case_1_regression/) | TransLine shipment delays | Linear regression | 8 | Heavily guided |
| [Case 2 — Classification](cases/case_2_classification/) | Meridian Outlet returns | Logistic regression | 8 | Guided |
| [Case 3 — Clustering](cases/case_3_clustering/) | Aurora Stream subscriber segmentation | KMeans | 8 | Guided, less interpretive support |
| [Capstone](cases/capstone/) | Your choice of one of three client engagements | Your choice of technique | 6 | Guided capstone (constrained choice) |

The Capstone also has two optional, ungraded lessons after its six core lessons: packaging your preprocessing into a `Pipeline`/`ColumnTransformer`, and — for the LendWell path only — explaining individual model predictions. See [`cases/capstone/README.md`](cases/capstone/README.md) for details.

## Getting started

Install [uv](https://docs.astral.sh/uv/) — it manages Python versions itself, so you don't need Python pre-installed; the commands below will download a compatible interpreter automatically if needed.

```bash
git clone https://github.com/michalmaj/data-science-casebook.git
cd data-science-casebook
uv sync
```

Start JupyterLab:

```bash
uv run jupyter lab
```

Each lesson lives in `cases/<case>/lessons/<NN_lesson_name>/` and follows the same shape:

- `task.py` — the functions you implement (each has a `TODO` docstring explaining what to do)
- `solution.py` — the reference implementation (don't peek before attempting `task.py`)
- `check.py` — the self-check; run it from the lesson's folder with `uv run pytest`
- `lesson.ipynb` — the notebook where you actually work through the lesson
- `README.md` / `README.pl.md` — the lesson brief

`task.py` is where you implement your solution; `lesson.ipynb` is where you run it, see the results, and write your interpretation — think of the notebook as your analytical report, not a scratch pad for writing new code from zero.

**Working through a lesson:**

1. Read the lesson's `README.md` (or `README.pl.md`) for context and the analytical question.
2. Fill in the `TODO`s in `task.py`.
3. From the lesson's folder, run `uv run pytest` to check your work.
4. Open `lesson.ipynb` and work through the analysis and reflection.

If you edit `task.py` after already importing it in a running notebook, restart the kernel (or re-run the import cell) — Python caches imported modules, so a plain re-run of a cell won't pick up your change.

Start at `cases/case_1_regression/lessons/01_defining_the_question/`.

## Bilingual

Every Markdown file has a Polish sibling (`README.md` → `README.pl.md`). English is the source of truth; code, comments, and commit messages are English-only. This includes lesson notebooks (`lesson.ipynb`) — their instructional text is English-only even where the accompanying `README.pl.md` is Polish; the lesson brief is bilingual, the workspace you code in is not.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for local development commands, the bilingual contract, and how to add a lesson or case. Found an error in a lesson, a translation issue, or want to propose a new case or lesson? [Open an issue](https://github.com/michalmaj/data-science-casebook/issues/new/choose) — the template picker will route you to the right form.

## License

[MIT](LICENSE)
