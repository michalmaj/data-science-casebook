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


def load_clean_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV, drop rows missing `weather`, impute `driver_experience_years`.

    TODO: same cleaning as Lessons 2-4 — drop rows where `weather` is
    missing, then fill missing `driver_experience_years` with the median
    of what's left.
    """
    raise NotImplementedError("load_clean_shipments is not implemented yet")


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible.

    TODO: import `train_test_split` from `sklearn.model_selection` and use
    it with `test_size=0.2` and `random_state=RANDOM_STATE`. Return
    (train_df, test_df) in that order.
    """
    raise NotImplementedError("split_shipments is not implemented yet")


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
