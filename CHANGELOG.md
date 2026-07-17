# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-17

### Added

- **Course scaffold**: `uv` + `pyproject.toml`, `ruff`, `pytest`, GitHub Actions CI, bilingual Markdown convention (#1)
- **Case 1 — Regression** (TransLine shipment delays, 8 lessons): Lesson 1 Defining the Question (#1), Lesson 2 Data Quality and Cleaning (#2), Lesson 3 Exploratory Data Analysis (#3), Lesson 4 Business Meaning of Error and Baseline (#4), Lesson 5 Train/Test Split and First Model (#5), Lesson 6 Residual Interpretation (#6), Lesson 7 Correlation vs. Prediction vs. Causation (#7), Lesson 8 Synthesis — Decision Note (#8)
- **Case 2 — Classification** (Meridian Outlet returns, 8 lessons): Lesson 1 Defining the Question (#9), Lesson 2 Data Wrangling — Multi-Sheet Excel (#10), Lesson 3 Exploratory Data Analysis for Classification (#11), Lesson 4 Imbalanced Classes and Baseline (#12), Lesson 5 Train/Test Split and First Classifier (#13), Lesson 6 Threshold Selection and Metric Choice (#14), Lesson 7 Communicating Uncertainty (#15), Lesson 8 Synthesis — Decision Note (#16)
- **Case 3 — Clustering** (Aurora Stream subscriber segmentation, 8 lessons): Lesson 1 Defining the Question (#17), Lesson 2 Feature Selection and Scaling (#18), Lesson 3 Exploratory Data Analysis for Clustering (#19), Lesson 4 Why Segment? First KMeans Attempt (#20), Lesson 5 Choosing k — Comparing Solutions (#21), Lesson 6 Interpreting and Naming Segments (#22), Lesson 7 Segment Stability and the Risk of Overinterpretation (#23), Lesson 8 Synthesis — Decision Note (#24)
- **Capstone** (student-chosen engagement, 6 lessons): data generator + Lesson 1 Defining the Question (#25), Lesson 2 Data Preparation (#26), Lesson 3 Exploration (#27), Lesson 4 Modeling (#28), Lesson 5 Evaluation (#29), Lesson 6 Synthesis — Decision Note (#30)
- **`ASSESSMENT_RUBRIC.md`**: the 7-criterion, 4-level grading rubric referenced by every case's decision note (#32)
- **Capstone preprocessing methodology** brought `impute_missing`/`split_dataset`/clustering evaluation in line with Case 3's own conventions — `impute_missing` restricted to `feature_columns`, stratified classification split, `cluster_stability` ported from Case 3, scaler returned from `scale_features` (#39)
- **Capstone Lesson 7 (optional, ungraded)** — packaging preprocessing as an `sklearn.pipeline.Pipeline`/`ColumnTransformer`, bringing in a categorical column each dataset path had but never used as a feature (#42)
- **Case 2 Lesson 7 calibration** — `tier_summary`/`brier_score`, extending the existing risk-tier lesson to check whether predicted probabilities are actually calibrated, not just correctly ordered (#43)
- **`tools/run_notebooks.py`** and a new `notebooks` CI job — executes every lesson notebook against its reference solution (all 3 dataset branches for the 4 multi-path Capstone notebooks), closing a gap where CI never actually ran a notebook (#45)
- **Capstone Lesson 8 (optional, ungraded, LendWell path only)** — per-applicant and aggregate model explainability (`reason_codes`, `reason_code_frequency`), closing with reflection questions on what explainability can't tell you without demographic data (#46)
- **Learning outcomes and estimated time** added to every one of the 32 lesson READMEs (#48)
- **`INSTRUCTOR_GUIDE.md`** — course structure/ordering, common student mistakes drawn from this project's own fix history, and a companion to reading the assessment rubric (#49)

### Fixed

- **Four methodology bugs (P0) found by an external audit**, all involving data leakage or unscaled features reaching a model before/without proper handling: a classification threshold tuned by looking at test-set results instead of a validation split (Case 2, #33); an imputation statistic computed from the whole dataset before the train/test split existed (Case 1, #34); the same leak plus `KMeans` fit on unscaled features (Capstone, #35)
- **CI never triggered on a version tag push**, ran an unpinned dependency resolution, and didn't cap BLAS/OpenMP thread counts (~34s → ~3.3s test time after the fix) (#36)
- **Cluster profiles reported in scaled/z-score units** instead of real-world units in Case 3 and Capstone decision notes — reversed an earlier design call after two independent audits flagged the same readability problem (#40)
- **Case 1's brief never disclosed that `weather` isn't known at prediction time** until five lessons after a student first sees it as a seemingly-useful column (#41)
- **Eight places across Case 1/2/3** where an exemplar or README's interpretation outran what the underlying analysis actually supported — comparing regression coefficients across differently-scaled features without a units caveat, a "floor" claim that was backwards for most of the data, an operational threshold recommended without a precision/recall check, cluster-stability testing conflated with K-means initialization sensitivity, and more (#44)
- **Two more instances of the same fragility class** — `check.py` tests asserting a cluster property against a specific KMeans label number, which sklearn gives no ordering guarantee for across versions — found and fixed after #47's initial pass missed them, closing the class out repo-wide (#51)

### Changed

- **Onboarding docs** (root `README.md`, `CONTRIBUTING.md`) rewritten for a first-time contributor: `uv`-only setup instructions, corrected claims about how strictly `check.py` verifies exact values, guidance-level relabeling per case (#37)
- **All 30 original `lesson.ipynb` files** gained a `%load_ext autoreload` cell; Capstone's three per-dataset "only" cells consolidated into one `DATASET_NAME`-dispatched cell; Case 2 Lesson 6's hardcoded threshold became an explicit `CHOSEN_THRESHOLD` variable (#38)
- **`tools/check_bilingual_pairs.py`** now also checks EN/PL header-level structural parity, not just sibling-file existence (#47)
- **Two `check.py` assertions in Case 2** corrected: a wording overclaim about which Lesson 3 signals actually reach the model, and an exemplar that cited only test-set threshold metrics without disclosing the weaker validation-set numbers that selected that threshold (#50)
