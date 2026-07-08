"""Lesson 4 task: build the simplest possible classifier and see what accuracy hides.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and merge Meridian Outlet's two sheets, same as Lessons 2-3.

    TODO: read the "Orders" sheet skipping the two rows above the real
    header, read the "Customers" sheet and rename "Customer ID" to
    "customer_id", then left-merge the two on "customer_id". Return the
    merged DataFrame.
    """
    raise NotImplementedError("load_and_merge_orders is not implemented yet")


def predict_majority_baseline(df: pd.DataFrame) -> pd.Series:
    """Return a prediction of the majority `is_returned` class for every row.

    TODO: find which value (0 or 1) is more common in df["is_returned"],
    then return a Series of that single constant value, one per row of
    `df`, indexed like `df`.
    """
    raise NotImplementedError("predict_majority_baseline is not implemented yet")


def accuracy(actual: pd.Series, predicted: pd.Series) -> float:
    """Return the proportion of predictions that exactly match `actual`.

    TODO: compare `actual` and `predicted` elementwise and return the
    fraction that are equal.
    """
    raise NotImplementedError("accuracy is not implemented yet")


def confusion_counts(actual: pd.Series, predicted: pd.Series) -> dict[str, int]:
    """Return the four confusion-matrix counts as a dict.

    TODO: return {"tp": ..., "fp": ..., "tn": ..., "fn": ...} where
    tp = actual 1 and predicted 1, fp = actual 0 and predicted 1,
    tn = actual 0 and predicted 0, fn = actual 1 and predicted 0.
    """
    raise NotImplementedError("confusion_counts is not implemented yet")
