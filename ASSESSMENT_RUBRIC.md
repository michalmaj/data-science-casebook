# Assessment Rubric

Every case in this course ends with a decision note — a written argument for what a stakeholder should do, grounded in your analysis. `check.py` can verify that your code produces the right numbers; it cannot verify that your recommendation is honest, well-argued, or actually useful. That's what this rubric is for.

## Weighting

| Criterion | Weight |
|---|---:|
| Problem / question definition | 15% |
| Data recognition / quality | 15% |
| Exploration and justification of decisions | 20% |
| Modeling / evaluation correctness | 20% |
| Interpretation and limitations | 15% |
| Communication | 10% |
| Readability / reproducibility | 5% |

## Criteria in detail

Each criterion is scored at one of four levels: **Exemplary**, **Proficient**, **Developing**, **Insufficient**.

### 1. Problem / question definition (15%)

- **Exemplary:** States a specific, measurable, falsifiable analytical question tied directly to a real stakeholder decision; explicitly separates what's in scope from what isn't.
- **Proficient:** States a clear analytical question tied to the stakeholder's need, though scope boundaries are implicit rather than stated.
- **Developing:** A question is present but vague — it restates the brief without sharpening it into something measurable.
- **Insufficient:** No clear question, or the question doesn't map to any decision the stakeholder could actually act on.

### 2. Data recognition / quality (15%)

- **Exemplary:** Identifies every quality issue (missingness, leakage risk, class imbalance, scale mismatches) before touching the model, and justifies each handling decision.
- **Proficient:** Identifies the main quality issues and handles them reasonably, with brief justification.
- **Developing:** Handles quality issues mechanically ("fill missing values") without explaining why, or without checking for leakage.
- **Insufficient:** Quality issues are missed, ignored, or introduced (e.g. using post-outcome information as a feature).

### 3. Exploration and justification of decisions (20%)

- **Exemplary:** Every modeling decision (feature choice, split strategy, preprocessing) is traced back to a specific finding from exploration.
- **Proficient:** Exploration is present and mostly informs decisions, with a few choices left unexplained.
- **Developing:** Exploration happens but reads as disconnected from the decisions that follow it.
- **Insufficient:** Little or no exploration; decisions appear arbitrary.

### 4. Modeling / evaluation correctness (20%)

- **Exemplary:** Correct train/validation/test discipline throughout (no leakage, no fitting or tuning decisions made using test data); baseline included; metric matches the business question.
- **Proficient:** Train/test split is correct and a baseline is present, though validation for tuning decisions (e.g. a classification threshold) may be skipped.
- **Developing:** A model is fit and evaluated, but with a methodological gap (e.g. preprocessing fit before the split, a threshold tuned by looking at test-set results).
- **Insufficient:** No baseline, no held-out evaluation, or training-set performance presented as if it were generalization.

### 5. Interpretation and limitations (15%)

- **Exemplary:** Distinguishes correlation from causation where relevant; states at least two concrete, case-specific limitations and their practical consequence for the recommendation.
- **Proficient:** States limitations, though some are generic ("more data would help") rather than specific to this analysis.
- **Developing:** Interpretation restates the numbers without saying what they mean for the decision at hand.
- **Insufficient:** No limitations stated, or the analysis is presented as more certain than the evidence supports.

### 6. Communication (10%)

- **Exemplary:** A non-technical stakeholder could read the decision note and act on it without needing to see any code.
- **Proficient:** Mostly plain language, with a few unexplained technical terms.
- **Developing:** Written for a reader who already knows the method (e.g. "the R² was 0.6") without translating to business terms.
- **Insufficient:** The decision note is a description of the steps taken, not a recommendation.

### 7. Readability / reproducibility (5%)

- **Exemplary:** The notebook runs top-to-bottom with no manual steps; code is clear enough that the grader doesn't need the student present to follow it.
- **Proficient:** The notebook runs with minor manual intervention (e.g. must set a variable first).
- **Developing:** The notebook mostly runs but has at least one broken cell or an out-of-order dependency.
- **Insufficient:** The notebook doesn't run, or the code is illegible enough that correctness can't be verified.

## Self-assessment checklist

Run through this before you consider a decision note done:

- [ ] My analytical question is specific enough that someone could prove it wrong.
- [ ] I checked for data leakage — no test-set information touched my preprocessing, feature choices, or tuning decisions.
- [ ] I have a baseline, and my model actually beats it on held-out data, not training data.
- [ ] Every number in my "Results" section came from data my model never saw while fitting or tuning.
- [ ] I named at least two real, case-specific limitations — not generic ones.
- [ ] I could hand this note to someone who has never opened the notebook, and they would understand what to do.
- [ ] My notebook runs top-to-bottom without errors, in order, with no manual steps I forgot to write down.
- [ ] If asked "how confident are you?", I have a specific answer, not just a metric.
