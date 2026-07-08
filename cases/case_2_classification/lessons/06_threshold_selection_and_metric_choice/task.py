"""Lesson 6 task: choose a decision threshold and see what it costs and gains.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"

RANDOM_STATE = 20260707
FEATURE_COLUMNS = ["discount_percent", "previous_returns_count", "account_age_days"]


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and merge Meridian Outlet's two sheets, same as Lessons 2-5.

    TODO: read the "Orders" sheet skipping the two rows above the real
    header, read the "Customers" sheet and rename "Customer ID" to
    "customer_id", then left-merge the two on "customer_id". Return the
    merged DataFrame.
    """
    raise NotImplementedError("load_and_merge_orders is not implemented yet")


def split_orders(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — same as Lesson 5.

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


def predict_at_threshold(
    model: LogisticRegression, df: pd.DataFrame, threshold: float
) -> np.ndarray:
    """Return predictions (0 or 1) using a custom probability threshold.

    TODO: get the predicted probability of class 1 via
    model.predict_proba(df[FEATURE_COLUMNS])[:, 1], then return an array
    of 1 where that probability is >= threshold, else 0.
    """
    raise NotImplementedError("predict_at_threshold is not implemented yet")


def classification_metrics(actual: pd.Series, predicted: np.ndarray) -> dict[str, float]:
    """Return {"precision": ..., "recall": ..., "f1": ...} for the predictions.

    TODO: use precision_score, recall_score, and f1_score from
    sklearn.metrics (pass zero_division=0 to each) to compute the three
    values and return them in a dict with those exact keys.
    """
    raise NotImplementedError("classification_metrics is not implemented yet")
