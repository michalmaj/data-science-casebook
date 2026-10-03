"""Lesson 5 task: set a fair baseline, then see if a real model beats it.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"

RANDOM_STATE = 20260707
FEATURE_COLUMNS = ["distance_km", "num_stops", "driver_experience_years", "vehicle_age_years"]


def load_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV and drop rows missing `weather`.

    TODO: read the CSV at `path`, then drop rows where `weather` is
    missing. Return the result — same cleaning as Lessons 2-4.
    """
    raise NotImplementedError("load_shipments is not implemented yet")


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible.

    TODO: same as Lessons 3-4 — `train_test_split` with `test_size=0.2`
    and `random_state=RANDOM_STATE`.
    """
    raise NotImplementedError("split_shipments is not implemented yet")


def impute_driver_experience(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing `driver_experience_years` using the training set's median only.

    TODO: same as Lessons 3-4 — compute the median from train_df only,
    apply to both frames.
    """
    raise NotImplementedError("impute_driver_experience is not implemented yet")


def predict_zero_baseline(df: pd.DataFrame) -> pd.Series:
    """Return a prediction of 0 (i.e. "on time") for every row of `df`.

    TODO: return a Series of 0.0, one per row of `df`, indexed like `df`.
    """
    raise NotImplementedError("predict_zero_baseline is not implemented yet")


def predict_mean_baseline(train_df: pd.DataFrame, target_df: pd.DataFrame) -> pd.Series:
    """Predict the training mean delay for every row of `target_df`.

    TODO: compute `train_df["delay_minutes"].mean()`, then return a Series
    of that value, one per row of `target_df`, indexed like `target_df`.
    Call this with `target_df=train_df` to see the baseline in-sample, or
    `target_df=test_df` for the fair, held-out comparison — never compute
    the mean from `target_df` itself when it's the test set.
    """
    raise NotImplementedError("predict_mean_baseline is not implemented yet")


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


def fit_model(train_df: pd.DataFrame) -> LinearRegression:
    """Fit a LinearRegression on FEATURE_COLUMNS, predicting delay_minutes.

    TODO: create a LinearRegression(), fit it on
    train_df[FEATURE_COLUMNS] and train_df["delay_minutes"], and return it.
    """
    raise NotImplementedError("fit_model is not implemented yet")


def predict_delay(model: LinearRegression, df: pd.DataFrame) -> np.ndarray:
    """Return the model's predictions for FEATURE_COLUMNS in `df`.

    TODO: call model.predict on df[FEATURE_COLUMNS] and return the result.
    """
    raise NotImplementedError("predict_delay is not implemented yet")
