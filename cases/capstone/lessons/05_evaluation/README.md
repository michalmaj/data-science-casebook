# Lesson 5 — Evaluation

## Mentor's note

"Lesson 4 only told you how your model does on data it already saw. That's not evaluation, that's a rehearsal. This is where you find out if it actually learned anything."

## Lesson goal

Evaluate your Lesson 4 baseline and model on held-out test data — data the model never saw while fitting — using the metric that actually fits your problem type.

## Today's analytical question

Does your model's test-set performance still beat the baseline, the way its training-set performance did in Lesson 4?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — the five functions from Lesson 4, reproduced, plus three new ones: `evaluate_regression`, `evaluate_classification`, `evaluate_clustering` (use only the one that matches your dataset)
- `lesson.ipynb` — the notebook where you'll run your full pipeline and evaluate it

## Working in the notebook

- Run only the cell matching your dataset's problem type — it loads, splits, fits, and evaluates in one place.
- Compare the test-set result to what you saw in Lesson 4.
- Decide whether the model is actually good enough to act on.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. These checks verify the evaluation numbers for the suggested feature sets — they can't tell you whether your model is good enough for your actual Lesson 1 question.

## Homework

Two to three sentences: would you actually recommend this model to your Lesson 1 client as-is, or does it need more work first? Be specific about what the evaluation number tells you.

## Reflection

The mentor asks: for classification and regression, you now have both a training-set result (Lesson 4) and a test-set result (this lesson). If those two numbers told very different stories, what would that tell you about your model — and which number would you trust more, and why?
