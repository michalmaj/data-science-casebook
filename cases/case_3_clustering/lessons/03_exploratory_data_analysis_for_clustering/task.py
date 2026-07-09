"""Lesson 3 task: look for structure in Aurora Stream's features before you cluster anything.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "aurora_stream.sqlite"

REFERENCE_DATE = "2026-04-01"
FEATURE_COLUMNS = [
    "session_count",
    "total_minutes_watched",
    "avg_minutes_per_session",
    "tenure_days",
]


def load_scaled_features(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load, join, and scale Aurora Stream's subscriber features, same as Lessons 1-2.

    TODO: run the same SQL as Lesson 1 (LEFT JOIN subscribers to sessions,
    grouped by subscriber_id, using REFERENCE_DATE as a bound query
    parameter) to get subscriber_id, plan_tier, country, and the four
    FEATURE_COLUMNS. Then standardize the four FEATURE_COLUMNS with
    sklearn.preprocessing.StandardScaler, same as Lesson 2, and return a
    DataFrame with subscriber_id plus the scaled FEATURE_COLUMNS.
    """
    raise NotImplementedError("load_scaled_features is not implemented yet")


def feature_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """Return the correlation matrix of the four FEATURE_COLUMNS in `df`.

    TODO: use df[FEATURE_COLUMNS].corr() to get the pairwise Pearson
    correlation between every pair of scaled features. Return the
    resulting DataFrame.
    """
    raise NotImplementedError("feature_correlations is not implemented yet")
