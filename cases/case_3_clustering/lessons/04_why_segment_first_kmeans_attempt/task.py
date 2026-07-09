"""Lesson 4 task: make the case for segmentation, then fit a first KMeans model.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "aurora_stream.sqlite"

REFERENCE_DATE = "2026-04-01"
FEATURE_COLUMNS = [
    "session_count",
    "total_minutes_watched",
    "avg_minutes_per_session",
    "tenure_days",
]
N_CLUSTERS = 4
RANDOM_STATE = 42


def load_scaled_features(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load, join, and scale Aurora Stream's subscriber features, same as Lessons 1-3.

    TODO: run the same SQL as Lesson 1 (LEFT JOIN subscribers to sessions,
    grouped by subscriber_id, using REFERENCE_DATE as a bound query
    parameter) to get subscriber_id, plan_tier, country, and the four
    FEATURE_COLUMNS. Then standardize the four FEATURE_COLUMNS with
    sklearn.preprocessing.StandardScaler, same as Lesson 2, and return a
    DataFrame with subscriber_id plus the scaled FEATURE_COLUMNS.
    """
    raise NotImplementedError("load_scaled_features is not implemented yet")


def fit_kmeans(df: pd.DataFrame, k: int = N_CLUSTERS, random_state: int = RANDOM_STATE) -> KMeans:
    """Fit a KMeans model with k clusters on the four FEATURE_COLUMNS in `df`.

    TODO: build sklearn.cluster.KMeans(n_clusters=k, random_state=random_state,
    n_init=10), call .fit(df[FEATURE_COLUMNS]) on it, and return the fitted
    model.
    """
    raise NotImplementedError("fit_kmeans is not implemented yet")
