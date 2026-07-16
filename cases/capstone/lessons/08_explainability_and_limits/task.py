"""Lesson 8 task (optional, LendWell only): explain individual predictions and know their limits.

This lesson is not graded and only applies if you picked lendwell_loan_default
in Lesson 1 — the reflection questions and reason-code mechanics don't
transfer to the other two datasets. Fill in each TODO below. Run
`uv run pytest` in this directory to check your work.
"""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
RANDOM_STATE = 42
FEATURE_COLUMNS = [
    "loan_amount",
    "annual_income",
    "credit_score",
    "debt_to_income_ratio",
    "employment_years",
    "previous_defaults",
]
TARGET_COLUMN = "defaulted"


def load_dataset(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load the LendWell dataset — no cleaning yet, same as Lesson 4.

    TODO: read data_dir / "lendwell_loan_default.csv" with pandas.read_csv
    and return it.
    """
    raise NotImplementedError("load_dataset is not implemented yet")


def split_dataset(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = RANDOM_STATE
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split df into (train_df, test_df), stratified on the target.

    TODO: import train_test_split from sklearn.model_selection. Call it with
    test_size=test_size, random_state=random_state, and
    stratify=df[TARGET_COLUMN] — this keeps the same default rate in both
    splits, which matters for this dataset's imbalanced target (most
    applicants don't default). Return (train_df, test_df).
    """
    raise NotImplementedError("split_dataset is not implemented yet")


def impute_missing(
    train_df: pd.DataFrame, test_df: pd.DataFrame, feature_columns: list[str]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing values in both frames using statistics from train_df only.

    TODO: on copies of train_df and test_df, for every column in
    feature_columns where train_df OR test_df has any missing value: if the
    column is numeric (pandas.api.types.is_numeric_dtype), compute
    fill_value as train_df[column].median(); otherwise as
    train_df[column].mode().iloc[0]. Fill that value into both frames for
    that column (never compute a fill value from test_df). Return
    (train_df, test_df).
    """
    raise NotImplementedError("impute_missing is not implemented yet")


def scale_features(
    df: pd.DataFrame, feature_columns: list[str]
) -> tuple[pd.DataFrame, StandardScaler]:
    """Standardize feature_columns to zero mean, unit variance (z-scores).

    TODO: import StandardScaler from sklearn.preprocessing. Build a
    StandardScaler(), and on a copy of df, replace df[feature_columns] with
    scaler.fit_transform(df[feature_columns]). Return (df, scaler). Unlike
    Lesson 4's classification path (which fits on raw features), this
    lesson scales before fitting: comparing coefficient magnitudes across
    features (which reason_codes does) is only meaningful when every
    feature is on the same scale — loan_amount (raw range ~1000-40000) and
    debt_to_income_ratio (raw range ~0.05-0.6) aren't comparable
    unscaled.
    """
    raise NotImplementedError("scale_features is not implemented yet")


def fit_classification_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[int, LogisticRegression]:
    """Fit a majority-class baseline and a LogisticRegression model on train_df.

    TODO: compute baseline as train_df[target_column].mode().iloc[0]. Build
    a LogisticRegression(max_iter=1000) — the default max_iter=100 does not
    converge here — fit it on train_df[feature_columns] and
    train_df[target_column]. Pass this function an already-scaled train_df
    (see scale_features) — reason_codes below assumes the model was fit on
    scaled features. Return (baseline, fitted_model).
    """
    raise NotImplementedError("fit_classification_baseline_and_model is not implemented yet")


def reason_codes(
    model: LogisticRegression,
    scaler: StandardScaler,
    applicant: pd.Series,
    feature_columns: list[str],
    top_n: int = 3,
) -> list[tuple[str, float]]:
    """Top-N features driving this applicant's prediction, ranked by |contribution|.

    TODO: scale this one applicant's raw feature values with
    scaler.transform(applicant[feature_columns].to_frame().T)[0] to get a
    1D array of scaled values. Multiply elementwise by model.coef_[0] to
    get each feature's contribution (positive pushes toward "defaulted",
    negative toward "repaid" — same sign convention as the model's
    decision function). Pair each feature name with its contribution,
    sort by descending absolute contribution, and return the first top_n
    pairs as a list of (feature_name, contribution) tuples. This mirrors
    what a real adverse-action notice (ECOA/Reg B in the US) has to give
    a rejected applicant: not just a decision, but the specific factors
    behind it.
    """
    raise NotImplementedError("reason_codes is not implemented yet")


def reason_code_frequency(
    model: LogisticRegression,
    scaler: StandardScaler,
    test_df: pd.DataFrame,
    feature_columns: list[str],
    top_n: int = 3,
) -> dict[str, int]:
    """How often each feature appears in the top-N reasons across every predicted denial.

    TODO: scale test_df[feature_columns] with scaler.transform, predict on
    the scaled values with model.predict to find which rows are predicted
    as a default (prediction == 1). For each such row (using the row's
    original, unscaled values — reason_codes does its own scaling), call
    reason_codes(model, scaler, row, feature_columns, top_n=top_n) and
    tally each returned feature name into a dict of counts (a
    collections.Counter works well here). Return the counts as a plain
    dict. This answers: is one feature dominating every denial, which
    would be worth a closer look even without demographic data to check
    for disparate impact directly.
    """
    raise NotImplementedError("reason_code_frequency is not implemented yet")
