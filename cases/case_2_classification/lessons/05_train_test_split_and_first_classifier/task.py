"""Lesson 5 task: split the data properly, fit a real classifier, and see what it catches.

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
    """Load and merge Meridian Outlet's two sheets, same as Lessons 2-4.

    TODO: read the "Orders" sheet skipping the two rows above the real
    header, read the "Customers" sheet and rename "Customer ID" to
    "customer_id", then left-merge the two on "customer_id". Return the
    merged DataFrame.
    """
    raise NotImplementedError("load_and_merge_orders is not implemented yet")


def split_orders(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible, class balance preserved.

    TODO: import train_test_split from sklearn.model_selection and use it
    with test_size=0.2, random_state=RANDOM_STATE, and
    stratify=df["is_returned"] — with only 14% of orders returned, a plain
    random split could easily give the test set a very different return
    rate than the train set, so stratifying keeps both sets representative.
    Return (train_df, test_df) in that order.
    """
    raise NotImplementedError("split_orders is not implemented yet")


def fit_classifier(train_df: pd.DataFrame) -> LogisticRegression:
    """Fit a LogisticRegression on FEATURE_COLUMNS, predicting is_returned.

    TODO: create a LogisticRegression(), fit it on
    train_df[FEATURE_COLUMNS] and train_df["is_returned"], and return it.
    """
    raise NotImplementedError("fit_classifier is not implemented yet")


def predict_return(model: LogisticRegression, df: pd.DataFrame) -> np.ndarray:
    """Return the model's predictions (0 or 1, at the default 0.5 threshold).

    TODO: call model.predict on df[FEATURE_COLUMNS] and return the result.
    """
    raise NotImplementedError("predict_return is not implemented yet")
