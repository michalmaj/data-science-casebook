"""Lesson 7 task: turn a predicted probability into words Meridian Outlet can act on.

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
    """Load and merge Meridian Outlet's two sheets, same as Lessons 2-6.

    TODO: read the "Orders" sheet skipping the two rows above the real
    header, read the "Customers" sheet and rename "Customer ID" to
    "customer_id", then left-merge the two on "customer_id". Return the
    merged DataFrame.
    """
    raise NotImplementedError("load_and_merge_orders is not implemented yet")


def split_orders(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — same as Lessons 5-6.

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


def risk_tier(probability: float) -> str:
    """Return "Low", "Medium", or "High" for a predicted return probability.

    TODO: return "Low" if probability is below 0.15, "Medium" if it's
    below 0.30, and "High" otherwise. These cutoffs turn a raw number
    into a category a non-technical stakeholder can act on.
    """
    raise NotImplementedError("risk_tier is not implemented yet")


def risk_report(model: LogisticRegression, df: pd.DataFrame) -> pd.DataFrame:
    """Return order_id, probability, and risk_tier for every row of `df`.

    TODO: use model.predict_proba(df[FEATURE_COLUMNS])[:, 1] to get each
    row's predicted probability, apply risk_tier to each one, and return
    a DataFrame with columns "order_id", "probability", "risk_tier" (in
    that order), one row per order in `df`.
    """
    raise NotImplementedError("risk_report is not implemented yet")
