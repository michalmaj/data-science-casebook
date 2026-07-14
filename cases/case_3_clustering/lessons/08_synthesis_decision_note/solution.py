"""Reference solution for Lesson 8. Do not open this before attempting task.py."""

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
SCALED_FEATURE_COLUMNS = [f"{column}_scaled" for column in FEATURE_COLUMNS]
K = 2
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

    features = df[["subscriber_id", *FEATURE_COLUMNS]].copy()
    scaler = StandardScaler()
    features[SCALED_FEATURE_COLUMNS] = scaler.fit_transform(features[FEATURE_COLUMNS])
    return features


def final_segment_table(
    df: pd.DataFrame, k: int = K, random_state: int = RANDOM_STATE
) -> pd.DataFrame:
    model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    labels = model.fit_predict(df[SCALED_FEATURE_COLUMNS])

    working = df.copy()
    working["cluster"] = labels

    table = working.groupby("cluster")[FEATURE_COLUMNS].mean()
    table["size"] = working.groupby("cluster").size()
    table["share"] = table["size"] / len(df)
    return table
