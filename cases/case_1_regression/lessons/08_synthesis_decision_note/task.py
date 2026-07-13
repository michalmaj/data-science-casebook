"""Lesson 8 task: build the one table that summarizes this whole case.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"

RANDOM_STATE = 20260707
FEATURE_COLUMNS = ["distance_km", "num_stops", "driver_experience_years", "vehicle_age_years"]


def load_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV and drop rows missing `weather`.

    TODO: read the CSV at `path`, then drop rows where `weather` is
    missing. Return the result — same as Lessons 5-7.
    """
    raise NotImplementedError("load_shipments is not implemented yet")


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible.

    TODO: import `train_test_split` from `sklearn.model_selection` and use
    it with `test_size=0.2` and `random_state=RANDOM_STATE`. Return
    (train_df, test_df) in that order — same as Lessons 5-7.
    """
    raise NotImplementedError("split_shipments is not implemented yet")


def impute_driver_experience(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing `driver_experience_years` using the training set's median only.

    TODO: compute the median of train_df["driver_experience_years"], then
    fill missing values in both train_df and test_df with that single
    median. Return (train_df, test_df) in that order — same as Lessons 5-7.
    """
    raise NotImplementedError("impute_driver_experience is not implemented yet")


def fit_model(train_df: pd.DataFrame) -> LinearRegression:
    """Fit a LinearRegression on FEATURE_COLUMNS, predicting delay_minutes.

    TODO: create a LinearRegression(), fit it on
    train_df[FEATURE_COLUMNS] and train_df["delay_minutes"], and return it.
    Same as Lesson 5's fit_model.
    """
    raise NotImplementedError("fit_model is not implemented yet")


def final_scorecard(
    train_df: pd.DataFrame, test_df: pd.DataFrame, model: LinearRegression
) -> pd.DataFrame:
    """Return a comparison table of every predictor this case has built.

    TODO: for each of "zero_baseline" (always predict 0), "mean_baseline"
    (always predict train_df["delay_minutes"].mean()), and "linear_model"
    (model.predict on test_df[FEATURE_COLUMNS]), compute MAE and RMSE
    against test_df["delay_minutes"] (use sklearn.metrics.mean_absolute_error
    and sklearn.metrics.root_mean_squared_error). Return a DataFrame indexed
    by ["zero_baseline", "mean_baseline", "linear_model"] with columns
    ["mae", "rmse"].
    """
    raise NotImplementedError("final_scorecard is not implemented yet")
