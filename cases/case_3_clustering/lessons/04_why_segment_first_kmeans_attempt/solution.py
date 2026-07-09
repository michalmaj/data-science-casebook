"""Reference solution for Lesson 4. Do not open this before attempting task.py."""

import sqlite3
from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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
    query = """
        SELECT
            s.subscriber_id,
            s.plan_tier,
            s.country,
            COUNT(se.session_date) AS session_count,
            COALESCE(SUM(se.minutes_watched), 0) AS total_minutes_watched,
            COALESCE(AVG(se.minutes_watched), 0) AS avg_minutes_per_session,
            CAST(julianday(?) - julianday(s.signup_date) AS INTEGER) AS tenure_days
        FROM subscribers s
        LEFT JOIN sessions se ON s.subscriber_id = se.subscriber_id
        GROUP BY s.subscriber_id
    """
    conn = sqlite3.connect(path)
    df = pd.read_sql_query(query, conn, params=(REFERENCE_DATE,))
    conn.close()

    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[FEATURE_COLUMNS])
    scaled_df = pd.DataFrame(scaled, columns=FEATURE_COLUMNS)
    scaled_df.insert(0, "subscriber_id", df["subscriber_id"].values)
    return scaled_df


def fit_kmeans(df: pd.DataFrame, k: int = N_CLUSTERS, random_state: int = RANDOM_STATE) -> KMeans:
    model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    model.fit(df[FEATURE_COLUMNS])
    return model
