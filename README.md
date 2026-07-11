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
| [Case 2 — Classification](cases/case_2_classification/) | Meridian Outlet returns | Logistic regression | 8 | Partially guided |
| [Case 3 — Clustering](cases/case_3_clustering/) | Aurora Stream subscriber segmentation | KMeans | 8 | Brief + data only |
| [Capstone](cases/capstone/) | Your choice of one of three client engagements | Your choice of technique | 6 | Fully independent |

## Getting started

Install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Each lesson lives in `cases/<case>/lessons/<NN_lesson_name>/` and follows the same shape:

- `task.py` — the functions you implement (each has a `TODO` docstring explaining what to do)
- `solution.py` — the reference implementation (don't peek before attempting `task.py`)
- `check.py` — the self-check; run it from the lesson's folder with `uv run pytest`
- `lesson.ipynb` — the notebook where you actually work through the lesson
- `README.md` / `README.pl.md` — the lesson brief

Start at `cases/case_1_regression/lessons/01_defining_the_question/`.

## Bilingual

Every Markdown file has a Polish sibling (`README.md` → `README.pl.md`). English is the source of truth; code, comments, and commit messages are English-only.

## Contributing

Found an error in a lesson, a translation issue, or want to propose a new case or lesson? [Open an issue](https://github.com/michalmaj/data-science-casebook/issues/new/choose) — the template picker will route you to the right form.

## License

[MIT](LICENSE)
