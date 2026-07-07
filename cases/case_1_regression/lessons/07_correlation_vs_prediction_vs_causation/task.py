"""Lesson 7 task: find out which coefficients you can trust, and which you can't.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"

RANDOM_STATE = 20260707
FEATURE_COLUMNS = ["distance_km", "num_stops", "driver_experience_years", "vehicle_age_years"]


def load_clean_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV, drop rows missing `weather`, impute `driver_experience_years`.

    TODO: same cleaning as Lessons 2-6 — drop rows where `weather` is
    missing, then fill missing `driver_experience_years` with the median
    of what's left.
    """
    raise NotImplementedError("load_clean_shipments is not implemented yet")


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible.

    TODO: import `train_test_split` from `sklearn.model_selection` and use
    it with `test_size=0.2` and `random_state=RANDOM_STATE`. Return
    (train_df, test_df) in that order — same as Lessons 5-6.
    """
    raise NotImplementedError("split_shipments is not implemented yet")


def fit_model_on(train_df: pd.DataFrame, feature_columns: list[str]) -> LinearRegression:
    """Fit a LinearRegression on an arbitrary list of feature columns.

    TODO: create a LinearRegression(), fit it on
    train_df[feature_columns] and train_df["delay_minutes"], and return it.
    Unlike Lesson 5's fit_model, this takes the feature list as an
    argument so you can compare different feature sets.
    """
    raise NotImplementedError("fit_model_on is not implemented yet")


def coefficient_for(model: LinearRegression, feature_columns: list[str], column: str) -> float:
    """Return the fitted coefficient for `column`, given the feature_columns order it was fit with.

    TODO: find the index of `column` in `feature_columns`, and return
    model.coef_ at that index.
    """
    raise NotImplementedError("coefficient_for is not implemented yet")
