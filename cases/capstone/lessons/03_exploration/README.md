# Lesson 3 — Exploration

## Mentor's note

"Before you fit anything, look at what's actually in the data. Some features will turn out to matter a lot for your question, some barely at all — and you want to know which is which before you build a model around the wrong ones."

## Lesson goal

Explore how the numeric features in your chosen dataset relate to each other, and start forming a view on which ones are likely to matter for your Lesson 1 question.

## Today's analytical question

Which of your dataset's numeric features look most related to each other — and to whatever you're trying to predict or understand?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — two functions: `load_clean_dataset` (Lessons 1-2 combined) and one new function, `numeric_correlations`
- `lesson.ipynb` — the notebook where you'll explore

## Working in the notebook

- Load and clean your dataset in one step.
- Compute the numeric correlation matrix.
- Sort the relationships to see which stand out, high or low.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. These checks verify the correlation numbers themselves — they can't tell you which relationships actually matter for your specific question.

## Homework

Two to three sentences: based on what you found, which feature are you most confident will help answer your Lesson 1 question, and which are you tempted to drop? What could go wrong with that judgment?

## Reflection

The mentor asks: a strong correlation between two features doesn't tell you which one (if either) is the one actually worth building your analysis around. What would you need to check before deciding that?
