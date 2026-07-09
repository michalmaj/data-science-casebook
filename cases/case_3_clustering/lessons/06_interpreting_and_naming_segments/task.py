"""Lesson 6 task: interpret and name the segments the k=2 solution actually found.

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
K = 2
RANDOM_STATE = 42


def load_scaled_features(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load, join, and scale Aurora Stream's subscriber features, same as Lessons 1-5.

    TODO: run the same SQL as Lesson 1 (LEFT JOIN subscribers to sessions,
    grouped by subscriber_id, using REFERENCE_DATE as a bound query
    parameter) to get subscriber_id, plan_tier, country, and the four
    FEATURE_COLUMNS. Then standardize the four FEATURE_COLUMNS with
    sklearn.preprocessing.StandardScaler, same as Lesson 2, and return a
    DataFrame with subscriber_id plus the scaled FEATURE_COLUMNS.
    """
    raise NotImplementedError("load_scaled_features is not implemented yet")


def segment_profiles(
    df: pd.DataFrame, k: int = K, random_state: int = RANDOM_STATE
) -> pd.DataFrame:
    """Fit KMeans at k and return each cluster's mean feature values and size.

    TODO: build sklearn.cluster.KMeans(n_clusters=k, random_state=random_state,
    n_init=10), fit_predict it on df[FEATURE_COLUMNS] to get cluster labels.
    Group df by those labels and compute the mean of each FEATURE_COLUMNS
    column per cluster, then add a "size" column with the number of
    subscribers in each cluster. Return the resulting DataFrame, indexed by
    cluster label, with columns FEATURE_COLUMNS followed by "size".
    """
    raise NotImplementedError("segment_profiles is not implemented yet")
