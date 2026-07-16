# Lesson 1 — Defining the Question

**Estimated time:** 25-35 min

## Learning outcomes

- You'll be able to turn a vague stakeholder complaint into a specific, testable analytical question.
- You'll be able to spot a data-leakage risk hiding in the brief itself, before writing any code.
- You'll be able to read a missing-value count and start reasoning about what a gap in each column actually means.

## Mentor's note

"Welcome aboard. TransLine's ops manager just told me — quote — 'shipments are late, fix it.' That's not a question we can answer with data yet. Before you touch a model, you need to turn that complaint into something specific enough to actually test. One more thing from that meeting: whatever we build has to work the moment a shipment leaves the depot — not with information we only find out afterward, like the weather it actually drove through. Keep that in mind as you get to know the data."

## Lesson goal

Turn TransLine's vague complaint into a specific, measurable analytical question, and take a first, critical look at the data you've been given.

## Today's analytical question

Given the shipment data TransLine has recorded, what exactly should we predict, and can we trust the data enough to start?

## What you're given

- `data/transport_delays.csv` (500 shipments, loaded via `data/generate.py` in the case folder)
- `task.py` — three functions to implement: `load_shipments`, `target_column_name`, `missing_value_counts`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Look at `df.describe()` — which columns make sense as predictors, and which look suspicious?
4. Confirm which single column answers TransLine's real question, and write down why you picked it.
5. Check `missing_value_counts(df)` — note which columns have gaps and how many.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: if you had to go back to TransLine's ops manager with one clarifying question before doing any modeling, what would it be, and why?

## Reflection

The mentor asks: two columns have missing values. Would you drop those rows, fill them in, or ask the client first — and does your answer depend on which column it is?
