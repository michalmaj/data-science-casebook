# Instructor Guide

This is a companion for anyone running this course as a class, a cohort, or one-on-one mentoring — not for students working through it solo (they should start with the root [`README.md`](README.md)). It covers how the four cases fit together, the mistakes students actually make (drawn from this course's own history, not hypotheticals), and how to read [`ASSESSMENT_RUBRIC.md`](ASSESSMENT_RUBRIC.md) in practice.

## 1. Course structure and ordering

Four cases, each a full analytical cycle, with guidance decreasing as you go — this table matches the root README's:

| Case | Guidance | Lessons | Estimated time |
|---|---|---:|---:|
| Case 1 — Regression | Heavily guided | 8 | 275-355 min (~4.5-6 hr) |
| Case 2 — Classification | Guided | 8 | 290-370 min (~5-6 hr) |
| Case 3 — Clustering | Guided, less interpretive support | 8 | 330-420 min (~5.5-7 hr) |
| Capstone (required) | Guided capstone (constrained choice) | 6 | 295-365 min (~5-6 hr) |
| Capstone (optional extras) | Ungraded, Lesson 7 all paths / Lesson 8 LendWell only | 2 | ~85-110 min (~1.5-2 hr) |

**Total for the 30 required lessons: roughly 1190-1510 minutes (~20-25 hours).** Add the two optional Capstone lessons and it's closer to 1275-1620 minutes (~21-27 hours). These are the same per-lesson editorial estimates from each lesson's own README — not measured, just summed.

**Recommended order: Case 1 → Case 2 → Case 3 → Capstone**, matching the root README's listed order. Each case removes a support the previous one relied on:

- **Case 1 (regression)** is the simplest entry point — a labeled target, a straightforward train/test split, and the first place students meet data leakage and baseline comparison. Get this discipline right here, because every later case assumes it.
- **Case 2 (classification)** keeps a labeled target but adds two things Case 1 didn't need: an imbalanced class, and a decision threshold that has to be chosen deliberately (with its own validation split) rather than defaulting to 0.5.
- **Case 3 (clustering)** removes the labeled target entirely — there's nothing to check predictions against, so "is this good?" has to be answered with different tools (silhouette score, stability under resampling) and a lot more interpretive judgment. This is also where students first meet the risk of overinterpreting a pattern the data doesn't actually support.
- **Capstone** removes the prescribed brief. The student picks the dataset, the target, the technique, and the question — and has to combine everything from the first three cases without being told which tool applies. It's the only case where "did they choose well" is itself part of what's being assessed.

Don't skip a case or reorder these expecting the same outcome — Case 3's clustering-specific judgment calls and Case 2's threshold-tuning discipline are exactly the muscles Capstone assumes are already built.

## 2. Common student mistakes, by case

These are real mistakes — this course's own reference material had every one of them at some point, caught either by an external audit or a later self-review, and fixed in a tracked PR. They're listed here because a mistake worth fixing in the reference material is exactly the kind of mistake a student is likely to make too.

### Data leakage before the train/test split (Case 1, Capstone)

**What it looks like:** A student computes a statistic — a median for imputing missing values, in this course's own past bug — from the *entire* dataset, then splits into train/test afterward. Both splits end up touched by the same "leaked" statistic.

**Why it's wrong:** The test set is supposed to simulate data the model has never seen. If a preprocessing statistic was computed using test-set rows, the test set has already leaked information into training, even though the model itself never saw the raw test rows. The evaluation is now optimistic in a way that won't reproduce in production.

**What it looked like in this course:** Case 1's `load_clean_shipments` computed a median for `driver_experience_years` from the whole dataset before any split existed (fixed in PR #34). Capstone's `load_clean_dataset` did the same thing generically for any column with gaps (fixed in PR #35, same underlying bug pattern).

**What would catch it:** Rubric criterion 4 (Modeling/evaluation correctness) — "Developing" level explicitly names "preprocessing fit before the split." If grading by hand without running `check.py`, look for whether `impute_*`/`scale_*` functions take `train_df` and `test_df` as separate arguments and only ever compute statistics from `train_df`.

### Fitting KMeans on unscaled features (Capstone)

**What it looks like:** A student fits `KMeans` directly on raw feature columns without standardizing them first.

**Why it's wrong:** KMeans measures distance directly on feature values. A column in the tens of thousands (e.g. revenue) will dominate the distance calculation over a column that's a small decimal (e.g. a return rate), regardless of which one actually separates the data meaningfully — the clustering ends up driven by units, not signal.

**What it looked like in this course:** Capstone's `fit_clustering_model` fit directly on raw features; the resulting clusters were dominated by whichever raw-unit column happened to have the largest scale (fixed in the same PR #35 as the leakage fix above — both bugs lived in the same file).

**What would catch it:** Rubric criterion 4 again ("Insufficient" level: no baseline, no held-out evaluation, or — by extension — a methodologically unsound fit). By hand: check whether a `StandardScaler` (or equivalent) is applied before `KMeans.fit`, not after.

### Tuning a decision threshold by looking at test-set results (Case 2)

**What it looks like:** A student compares a classifier's precision/recall across several candidate thresholds (0.5, 0.3, 0.2, ...) directly on the test set, then picks whichever threshold looks best there.

**Why it's wrong:** This is leakage through decision-making rather than through preprocessing — the test set is supposed to be touched exactly once, for a final, already-decided evaluation. Comparing thresholds against it and picking the winner means the "test" result no longer reflects how the model would perform on genuinely unseen data; the threshold was fit to the test set as surely as a model parameter would be.

**What it looked like in this course:** Case 2's Lesson 6 originally compared thresholds 0.5/0.3/0.2 directly on the test set and picked 0.2 based on that comparison (fixed in PR #33) — the fix carves a validation split out of the training data specifically for threshold comparisons, touching the test set only once, at the end, with the already-chosen threshold.

**What would catch it:** Rubric criterion 4 — "Proficient" level explicitly allows this gap ("validation for tuning decisions... may be skipped") but "Exemplary" requires "no fitting or tuning decisions made using test data." By hand: ask specifically how the threshold was chosen, and whether that choice used the same data as the final reported metric.

### Interpretation overreach (Case 1, Case 2, Case 3)

Five related patterns, all real, all caught in the same audit and fixed in one PR (#44):

- **Comparing raw regression coefficients across differently-scaled features** without noting they're not on comparable units (a coefficient of 6.9 on a feature ranging 0-10 isn't "bigger" than a coefficient of -2.3 on a feature ranging 0-1000 in any meaningful sense) — Case 1.
- **Claiming a model has a uniform prediction bias** ("the model underestimates delays") without checking whether that's true across every subgroup, or only some — Case 1's model actually *overpredicted* delay in clear weather (70% of shipments) while underpredicting in rain/snow; the unconditional claim was backwards for the majority case.
- **Recommending an operational threshold** (e.g. "flag anything over 20 minutes") **without checking its precision/recall** — a threshold can sound reasonable and still flag mostly false positives.
- **Stating an operational cost as fact without a basis in the brief or the data** — Case 2's exemplar originally stated a false alarm "just costs a few minutes" as if it were given, when nothing in the client brief supported that; the fix reframes it as an assumption to confirm with the client, and adds the actual volume this decision affects (45 of 140 test orders flagged, ~32%) so the assumption's real stakes are visible.
- **Conflating resampling-based cluster stability with K-means initialization sensitivity** — a stability check that only varies the *sample* (holding `random_state` fixed) says nothing about whether a different random initialization would have found the same clusters. These are different questions with different answers — Case 3.

**Why these are worth watching for:** none of these are "wrong code" — `check.py` won't catch any of them, because the numbers are all computed correctly. The problem is entirely in what the numbers are claimed to mean. This is exactly rubric criterion 5 (Interpretation and limitations)'s territory.

**What would catch it:** Rubric criterion 5 — "Insufficient" level: "the analysis is presented as more certain than the evidence supports." By hand: for every claim in the "Interpretation" or "Recommendation" section, ask "what would have to be true, that wasn't actually checked, for this claim to be false?"

## 3. Reading the rubric

[`ASSESSMENT_RUBRIC.md`](ASSESSMENT_RUBRIC.md) already defines all 7 criteria with a one-sentence Exemplary/Proficient/Developing/Insufficient definition each — this section doesn't repeat that, it adds the practical judgment call a grader actually faces at the Exemplary/Proficient boundary, and points to a worked example.

1. **Problem/question definition (15%)** — the practical tell: Proficient states a question; Exemplary also says what's explicitly out of scope. If a submission never says what it *isn't* answering, it's Proficient at best, however sharp the question itself is. See Case 1's exemplar, "1. Business question."
2. **Data recognition/quality (15%)** — the practical tell: does the submission mention issues it *didn't* find as well as ones it did? Exemplary explicitly rules out leakage and imbalance even when neither is present in the chosen dataset, not just handles the issues that happen to exist. See Case 2's exemplar, "2. Approach" (imbalance is checked and stated even before it becomes the case's central theme).
3. **Exploration/justification of decisions (20%)** — the practical tell: can you trace *every* modeling decision back to a specific number or plot from exploration, or just most of them? One unexplained choice (why this feature set, why this k) drops a submission from Exemplary to Proficient even if the rest is airtight. See Case 3's exemplar, "2. Approach" and "4. Choosing k and checking stability" together — inertia and silhouette actually disagreed on the best k there, so the choice is explicitly traced to a resampling-stability check (ARI = 1.0 across five seeds) instead, not asserted from whichever single metric looked best.
4. **Modeling/evaluation correctness (20%)** — the practical tell covered in Section 2 above: Proficient allows a validation-split gap for tuning decisions; Exemplary doesn't. This is the criterion most directly checkable against `check.py` output, but `check.py` can't verify *reasoning* about a threshold or split choice — only that the code runs correctly. See Case 2's exemplar, "4. Threshold and metric choice."
5. **Interpretation/limitations (15%)** — the practical tell: are the stated limitations specific to *this* analysis, or would they apply to any analysis of any dataset ("more data would help")? Generic limitations read as a checkbox exercise, not real interpretation. See Case 1's exemplar, "6. Limitations" — each limitation names a specific, checkable consequence for the recommendation, not a vague caveat.
6. **Communication (10%)** — the practical tell: read only the "Recommendation" section in isolation. Could a stakeholder with zero data-science background act on it without reading anything else? If understanding it requires the "Results" section's numbers, it's Proficient, not Exemplary. See any exemplar's "7. Recommendation."
7. **Readability/reproducibility (5%)** — the lowest-weight criterion but the fastest to check: run the notebook top to bottom before reading a word of the analysis. If it doesn't run clean, nothing else in the submission can be verified as claimed — this criterion is a gate on trusting the rest of the grading, not just its own 5%.

Each case's exemplar decision note ends with a "Why this is a strong answer" section that explicitly ties its choices back to specific rubric criteria — read that section first if you want the fastest orientation to what "Exemplary" looks like in that case's own voice, then check a real submission against it criterion by criterion rather than trying to hold all 7 in your head verbatim.
