# Lesson 8 (Optional, LendWell only) — Explainability & Limits

## Mentor's note

"Lesson 7 packaged this model for deployment. This one asks what deploying
it *responsibly* actually requires — using the one path here where a wrong
answer has a real person's outcome attached to it. This lesson only applies
if you picked LendWell in Lesson 1; the other two paths don't have a
decision like this one to explain."

## Lesson goal

Implement `reason_codes` and `reason_code_frequency`, then use them on the
test set to see which features actually drive this model's denials — and
where that explanation runs out.

## Today's analytical question

When this model denies an applicant, what does it say is the reason — and
how often is the same reason behind every single denial?

## What you're given

- `lendwell_loan_default.csv` — no dataset choice this time, this lesson is
  LendWell-only
- `task.py` — five functions reproduced from Lesson 4 (`load_dataset`,
  `split_dataset`, `impute_missing`, `scale_features`,
  `fit_classification_baseline_and_model`), plus two new ones:
  `reason_codes` and `reason_code_frequency`
- `lesson.ipynb` — the notebook where you'll fit the model and inspect its
  reasons

## Working in the notebook

- Run the setup cell — it loads, splits, imputes, scales, and fits, the
  same sequence as Lessons 4-6, except scaling now applies before fitting
  the classifier too (see the note in the notebook about why).
- Call `reason_codes` on a real applicant your model would deny, and read
  off the top three features driving that decision.
- Call `reason_code_frequency` across the whole test set — see which
  feature shows up in almost every denial.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. Like Lessons 4-7, these
checks verify exact values — they confirm your `reason_codes`/
`reason_code_frequency` code behaves correctly, not that the underlying
model or feature set is the right call.

## Homework

None — this lesson is optional and ungraded.

## Reflection

The mentor asks, five questions, no code required — write two or three
sentences on whichever interests you most in the "Your notes" cell:

1. This dataset has no demographic columns. What would you need — and who
   would need to give it to you — to actually check whether this model
   denies certain groups of applicants disproportionately?
2. `debt_to_income_ratio` shows up in the top-3 reasons for every single
   denied applicant in the test set. Does that make it a fair basis for a
   lending decision, a red flag that it might be standing in for something
   else, or both — and how would you tell the difference?
3. False positives (denying a loan to someone who would have repaid) and
   false negatives (approving a loan that defaults) don't cost LendWell —
   or the applicant — the same amount. Who bears each kind of mistake, and
   should that change where you'd set the decision threshold?
4. `reason_codes` gives you a technically correct answer. Is a list of
   feature names and signed numbers actually something a rejected
   applicant could understand as "why"? What would you change about the
   output if a real person had to read it?
5. Would you want every prediction this model makes to go straight to a
   decision, or are there applicants — e.g., those close to the model's
   decision boundary — where a person should look before the answer is
   final?
