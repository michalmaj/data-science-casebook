# Lesson 1 — Defining the Question

**Estimated time:** 45-55 min

## The decision to make

Every other case handed you a client and a question already defined. This time you pick both. Read the menu in the case-level `README.md`, pick the client whose problem interests you, and turn their vague complaint into something you could actually build a model against — a specific analytical question, a target variable, and a success metric.

Also decide, on your own, which technique — regression, classification, or clustering — actually fits the problem your chosen client has. Nothing in the brief hints at it.

## What you have to work with

- Three datasets under `data/`: `clinic_wait_times.csv`, `lendwell_loan_default.csv`, `retail_store_segments.csv` — each with a light brief in the case's `README.md`, no target variable or metric given.
- In `task.py`, implement `list_datasets`, `load_dataset`, `missing_value_counts`.
- In the notebook: list the available datasets, load the one you picked, check its shape and missing values, and write down your analytical question, target variable, and success metric.

## Justify it

From this lesson's folder, run:

```bash
uv run pytest
```

These checks only verify that the loading functions work correctly for all three datasets — they can't check which client got picked, or whether the question is a good one.

Two to three sentences: why that target variable and that metric, specifically? What would a wrong choice here cost later in the capstone? And: of the three clients on the menu, which one would have been hardest to say no to if a real client asked, even if the data doesn't fully support answering their real question — and how would you push back?
