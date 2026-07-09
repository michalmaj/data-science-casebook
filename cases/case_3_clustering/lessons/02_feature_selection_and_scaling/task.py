"""Lesson 2 task: decide which columns describe behavior, then put them on the same scale.

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


def load_subscriber_features(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and aggregate Aurora Stream's two tables, same as Lesson 1.

    TODO: same SQL as Lesson 1 — LEFT JOIN subscribers to sessions,
    grouped by subscriber_id, selecting subscriber_id, plan_tier,
    country, session_count, total_minutes_watched,
    avg_minutes_per_session, and tenure_days (using REFERENCE_DATE as a
    bound query parameter). Return the resulting DataFrame.
    """
    raise NotImplementedError("load_subscriber_features is not implemented yet")


def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """Return subscriber_id plus the four FEATURE_COLUMNS, standardized.

    TODO: use sklearn.preprocessing.StandardScaler to fit_transform
    df[FEATURE_COLUMNS] (mean 0, unit variance per column). Build a new
    DataFrame with those scaled values under the same FEATURE_COLUMNS
    names, and insert df["subscriber_id"] as the first column (left
    untouched — it's an identifier, not something to scale). Return the
    result.
    """
    raise NotImplementedError("scale_features is not implemented yet")
