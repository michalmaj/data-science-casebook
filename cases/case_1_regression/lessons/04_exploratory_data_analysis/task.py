"""Lesson 3 task: explore the cleaned data and find predictive signal.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"

NUMERIC_COLUMNS = [
    "distance_km",
    "planned_duration_min",
    "actual_duration_min",
    "driver_experience_years",
    "num_stops",
    "vehicle_age_years",
    "delay_minutes",
]


def load_clean_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV, drop rows missing `weather`, impute `driver_experience_years`.

    TODO: same cleaning as Lesson 2 — drop rows where `weather` is missing,
    then fill missing `driver_experience_years` with the median of what's left.
    """
    raise NotImplementedError("load_clean_shipments is not implemented yet")


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Return the correlation matrix of NUMERIC_COLUMNS in `df`.

    TODO: select NUMERIC_COLUMNS from `df` and compute their correlation matrix.
    """
    raise NotImplementedError("correlation_matrix is not implemented yet")


def correlation_with_target(df: pd.DataFrame, column: str) -> float:
    """Return the correlation between `column` and `delay_minutes` in `df`.

    TODO: use correlation_matrix (or compute directly) and pick out the
    value for (column, "delay_minutes").
    """
    raise NotImplementedError("correlation_with_target is not implemented yet")


def mean_delay_by_weather(df: pd.DataFrame) -> pd.Series:
    """Return mean `delay_minutes` grouped by `weather`, sorted worst first.

    TODO: group `df` by "weather", take the mean of "delay_minutes", and
    sort descending.
    """
    raise NotImplementedError("mean_delay_by_weather is not implemented yet")
