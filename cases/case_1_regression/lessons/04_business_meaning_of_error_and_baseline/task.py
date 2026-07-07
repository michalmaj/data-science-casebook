"""Lesson 4 task: give TransLine a baseline to beat, in minutes they understand.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"


def load_clean_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV, drop rows missing `weather`, impute `driver_experience_years`.

    TODO: same cleaning as Lessons 2-3 — drop rows where `weather` is
    missing, then fill missing `driver_experience_years` with the median
    of what's left.
    """
    raise NotImplementedError("load_clean_shipments is not implemented yet")


def predict_mean_baseline(df: pd.DataFrame) -> pd.Series:
    """Return a prediction for every row equal to the historical mean delay.

    TODO: compute `df["delay_minutes"].mean()` and return a Series of that
    same value, one per row of `df`, indexed like `df`.
    """
    raise NotImplementedError("predict_mean_baseline is not implemented yet")


def predict_zero_baseline(df: pd.DataFrame) -> pd.Series:
    """Return a prediction of 0 (i.e. "on time") for every row.

    TODO: return a Series of 0.0, one per row of `df`, indexed like `df`.
    """
    raise NotImplementedError("predict_zero_baseline is not implemented yet")


def mean_absolute_error(actual: pd.Series, predicted: pd.Series) -> float:
    """Return the mean absolute error between `actual` and `predicted`.

    TODO: average of the absolute differences between the two series.
    """
    raise NotImplementedError("mean_absolute_error is not implemented yet")


def root_mean_squared_error(actual: pd.Series, predicted: pd.Series) -> float:
    """Return the root mean squared error between `actual` and `predicted`.

    TODO: square root of the average of the squared differences.
    """
    raise NotImplementedError("root_mean_squared_error is not implemented yet")
