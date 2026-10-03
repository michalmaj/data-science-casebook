"""Lesson 5 task: split the data properly, fit a real model, and beat the baseline.

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

    TODO: read the CSV at `path` with pandas.read_csv, then drop rows
    where `weather` is missing. Return the result. (`driver_experience_years`
    may still have missing values here — that's handled after the split,
    in `impute_driver_experience`, not here.)
    """
    raise NotImplementedError("load_shipments is not implemented yet")


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible.

    TODO: import `train_test_split` from `sklearn.model_selection` and use
    it with `test_size=0.2` and `random_state=RANDOM_STATE`. Return
    (train_df, test_df) in that order.
    """
    raise NotImplementedError("split_shipments is not implemented yet")


def impute_driver_experience(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing `driver_experience_years` using the training set's median only.

    TODO: compute the median of train_df["driver_experience_years"] (pandas'
    .median() ignores missing values by default). Fill missing values in
    both train_df and test_df with that single median — never compute a
    separate median from test_df, and never recompute it from the two
    frames combined. Return (train_df, test_df) in that order.
    """
    raise NotImplementedError("impute_driver_experience is not implemented yet")


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
