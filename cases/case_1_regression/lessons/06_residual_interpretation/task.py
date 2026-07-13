"""Lesson 6 task: find out what the model's mistakes are trying to tell you.

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
    missing. Return the result — same as Lesson 5.
    """
    raise NotImplementedError("load_shipments is not implemented yet")


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible.

    TODO: import `train_test_split` from `sklearn.model_selection` and use
    it with `test_size=0.2` and `random_state=RANDOM_STATE`. Return
    (train_df, test_df) in that order — same as Lesson 5.
    """
    raise NotImplementedError("split_shipments is not implemented yet")


def impute_driver_experience(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing `driver_experience_years` using the training set's median only.

    TODO: compute the median of train_df["driver_experience_years"], then
    fill missing values in both train_df and test_df with that single
    median. Return (train_df, test_df) in that order — same as Lesson 5.
    """
    raise NotImplementedError("impute_driver_experience is not implemented yet")


def fit_model(train_df: pd.DataFrame) -> LinearRegression:
    """Fit a LinearRegression on FEATURE_COLUMNS, predicting delay_minutes.

    TODO: create a LinearRegression(), fit it on
    train_df[FEATURE_COLUMNS] and train_df["delay_minutes"], and return it.
    """
    raise NotImplementedError("fit_model is not implemented yet")


def compute_residuals(model: LinearRegression, df: pd.DataFrame) -> pd.Series:
    """Return actual minus predicted delay for every row of `df`.

    TODO: predict on df[FEATURE_COLUMNS], then return
    df["delay_minutes"] minus those predictions (a positive residual
    means the model predicted too low; negative means it predicted too high).
    """
    raise NotImplementedError("compute_residuals is not implemented yet")


def mean_residual_by_weather(df: pd.DataFrame, residuals: pd.Series) -> pd.Series:
    """Return the mean residual grouped by `weather`, sorted worst-underestimate first.

    TODO: group `residuals` by df["weather"] and take the mean, sorted
    descending (largest positive residual — biggest underestimate — first).
    """
    raise NotImplementedError("mean_residual_by_weather is not implemented yet")


def residual_correlation_with_feature(
    df: pd.DataFrame, residuals: pd.Series, column: str
) -> float:
    """Return the correlation between `residuals` and df[column].

    TODO: use pandas' `.corr()` between the two series.
    """
    raise NotImplementedError("residual_correlation_with_feature is not implemented yet")
