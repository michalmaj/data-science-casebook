"""Reference solution for Lesson 3. Do not open this before attempting task.py."""

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
    df = pd.read_csv(path)
    df = df.dropna(subset=["weather"])
    median_experience = df["driver_experience_years"].median()
    return df.fillna({"driver_experience_years": median_experience})


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df[NUMERIC_COLUMNS].corr()


def correlation_with_target(df: pd.DataFrame, column: str) -> float:
    return correlation_matrix(df).loc[column, "delay_minutes"]


def mean_delay_by_weather(df: pd.DataFrame) -> pd.Series:
    return df.groupby("weather")["delay_minutes"].mean().sort_values(ascending=False)
