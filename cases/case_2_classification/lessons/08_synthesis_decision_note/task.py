"""Lesson 8 task: build the one table that summarizes this whole case.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"

RANDOM_STATE = 20260707
FEATURE_COLUMNS = ["discount_percent", "previous_returns_count", "account_age_days"]


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and merge Meridian Outlet's two sheets, same as Lessons 2-7.

    TODO: read the "Orders" sheet skipping the two rows above the real
    header, read the "Customers" sheet and rename "Customer ID" to
    "customer_id", then left-merge the two on "customer_id". Return the
    merged DataFrame.
    """
    raise NotImplementedError("load_and_merge_orders is not implemented yet")


def split_orders(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — same as Lessons 5-7.

    TODO: import train_test_split from sklearn.model_selection and use it
    with test_size=0.2, random_state=RANDOM_STATE, and
    stratify=df["is_returned"]. Return (train_df, test_df) in that order.
    """
    raise NotImplementedError("split_orders is not implemented yet")


def fit_classifier(train_df: pd.DataFrame) -> LogisticRegression:
    """Fit a LogisticRegression on FEATURE_COLUMNS, predicting is_returned.

    TODO: create a LogisticRegression(), fit it on
    train_df[FEATURE_COLUMNS] and train_df["is_returned"], and return it.
    """
    raise NotImplementedError("fit_classifier is not implemented yet")


def final_scorecard(
    train_df: pd.DataFrame, test_df: pd.DataFrame, model: LogisticRegression
) -> pd.DataFrame:
    """Return a comparison table of every predictor this case has built.

    TODO: build three sets of predictions on test_df and compare each to
    test_df["is_returned"] with precision_score, recall_score, and
    f1_score from sklearn.metrics (each with zero_division=0):

    - "majority_baseline": predict train_df["is_returned"]'s most common
      value (via value_counts().idxmax()) for every row of test_df.
    - "default_threshold_0.5": model.predict_proba(test_df[FEATURE_COLUMNS])[:, 1]
      thresholded at >= 0.5.
    - "chosen_threshold_0.2": the same probabilities thresholded at >= 0.2.

    Return a DataFrame indexed by ["majority_baseline",
    "default_threshold_0.5", "chosen_threshold_0.2"] with columns
    ["precision", "recall", "f1"].
    """
    raise NotImplementedError("final_scorecard is not implemented yet")
