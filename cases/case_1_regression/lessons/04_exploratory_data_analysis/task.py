"""Lesson 4 task: explore the training data and find predictive signal.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"

RANDOM_STATE = 20260707

NUMERIC_COLUMNS = [
    "distance_km",
    "planned_duration_min",
    "actual_duration_min",
    "driver_experience_years",
    "num_stops",
    "vehicle_age_years",
    "delay_minutes",
]


def load_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV and drop rows missing `weather`.

    TODO: read the CSV at `path`, then drop rows where `weather` is
    missing. Return the result — same cleaning as Lessons 2-3.
    """
    raise NotImplementedError("load_shipments is not implemented yet")


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible.

    TODO: same as Lesson 3 — `train_test_split` with `test_size=0.2` and
    `random_state=RANDOM_STATE`.
    """
    raise NotImplementedError("split_shipments is not implemented yet")


def impute_driver_experience(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing `driver_experience_years` using the training set's median only.

    TODO: same as Lesson 3 — compute the median from train_df only, apply
    to both frames.
    """
    raise NotImplementedError("impute_driver_experience is not implemented yet")


def correlation_matrix(train_df: pd.DataFrame) -> pd.DataFrame:
    """Return the correlation matrix of NUMERIC_COLUMNS in `train_df`.

    TODO: select NUMERIC_COLUMNS from `train_df` and compute their
    correlation matrix. Only ever call this with the training split —
    test_df stays in the sealed envelope.
    """
    raise NotImplementedError("correlation_matrix is not implemented yet")


def correlation_with_target(train_df: pd.DataFrame, column: str) -> float:
    """Return the correlation between `column` and `delay_minutes` in `train_df`.

    TODO: use correlation_matrix (or compute directly) and pick out the
    value for (column, "delay_minutes").
    """
    raise NotImplementedError("correlation_with_target is not implemented yet")


def mean_delay_by_weather(train_df: pd.DataFrame) -> pd.Series:
    """Return mean `delay_minutes` grouped by `weather` in `train_df`, sorted worst first.

    TODO: group `train_df` by "weather", take the mean of "delay_minutes",
    and sort descending.
    """
    raise NotImplementedError("mean_delay_by_weather is not implemented yet")
