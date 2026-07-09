"""Reference solution for Lesson 2. Do not open this before attempting task.py."""

import sqlite3
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "aurora_stream.sqlite"

REFERENCE_DATE = "2026-04-01"
FEATURE_COLUMNS = [
    "session_count",
    "total_minutes_watched",
    "avg_minutes_per_session",
    "tenure_days",
]


def load_subscriber_features(path: Path = DATA_PATH) -> pd.DataFrame:
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
    return df


def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[FEATURE_COLUMNS])
    scaled_df = pd.DataFrame(scaled, columns=FEATURE_COLUMNS)
    scaled_df.insert(0, "subscriber_id", df["subscriber_id"].values)
    return scaled_df
