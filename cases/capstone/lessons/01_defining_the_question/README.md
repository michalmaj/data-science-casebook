# Lesson 1 — Defining the Question

## Mentor's note

"Every other case, I handed you a client and a question. This time you're picking both. Read the menu, pick the client whose problem interests you, and turn their vague complaint into something you could actually build a model against."

## Lesson goal

Pick one client from the capstone menu, load their data, and independently define the specific analytical question, target variable, and success metric you'll pursue for the rest of the capstone.

## Today's analytical question

There isn't one yet — that's what you're building this lesson. Which client will you help, and what specific, measurable question will you answer for them?

## What you're given

- Three datasets under `data/`: `clinic_wait_times.csv`, `lendwell_loan_default.csv`, `retail_store_segments.csv`
- Light client briefs for each in the case-level `README.md` — no target variable or metric given
- `task.py` — three functions to implement: `list_datasets`, `load_dataset`, `missing_value_counts`
- `lesson.ipynb` — the notebook where you'll pick a client and start exploring

## Working in the notebook

- List the available datasets and read their briefs.
- Load the one you picked and check its shape and missing values.
- Write your own analytical question, target variable, and success metric.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. These checks only verify that your loading functions work correctly for all three datasets — they cannot check which client you picked or whether your question is a good one.

## Homework

Two to three sentences: why did you pick that target variable and that metric, specifically? What would a wrong choice here cost you later in the capstone?

## Reflection

The mentor asks: of the three clients on the menu, which one would have been hardest to say no to if a real client asked, even if the data doesn't fully support answering their real question — and how would you push back?
