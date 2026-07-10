# Lesson 2 — Data Preparation

## Mentor's note

"Whatever you found missing in Lesson 1, don't just paper over it. Decide, deliberately, what filling those gaps assumes about the data you don't have — and be ready to defend that choice."

## Lesson goal

Assess data quality and clean the dataset you picked in Lesson 1, using a strategy that works regardless of which columns happen to have gaps.

## Today's analytical question

Which columns in your dataset have missing values, and is filling them with the median/mode actually a defensible choice here?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — three functions: `load_dataset` and `missing_value_counts` (reproduced from Lesson 1), plus one new function, `clean_dataset`
- `lesson.ipynb` — the notebook where you'll check quality and clean

## Working in the notebook

- Load your dataset and check missing values before cleaning.
- Run `clean_dataset` and confirm nothing is missing afterward.
- Note whether median/mode filling is reasonable for your specific columns.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. These checks verify `clean_dataset` actually removes every gap for all three menu datasets — they can't judge whether median/mode filling was the *right* call for your specific dataset.

## Homework

Two to three sentences: pick one column that had missing values in your dataset. What real-world reason might explain why that value was missing — and does median/mode filling handle that reason well or badly?

## Reflection

The mentor asks: `clean_dataset` treats every missing value the same way, regardless of dataset. What's the risk of applying one generic cleaning strategy across very different kinds of data?
