"""Reference solution for Lesson 4. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

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
    df = pd.read_csv(path)
    return df.dropna(subset=["weather"])


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=RANDOM_STATE)
    return train_df, test_df


def impute_driver_experience(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    median_experience = train_df["driver_experience_years"].median()
    train_df = train_df.fillna({"driver_experience_years": median_experience})
    test_df = test_df.fillna({"driver_experience_years": median_experience})
    return train_df, test_df


def correlation_matrix(train_df: pd.DataFrame) -> pd.DataFrame:
    return train_df[NUMERIC_COLUMNS].corr()


def correlation_with_target(train_df: pd.DataFrame, column: str) -> float:
    return correlation_matrix(train_df).loc[column, "delay_minutes"]


def mean_delay_by_weather(train_df: pd.DataFrame) -> pd.Series:
    return train_df.groupby("weather")["delay_minutes"].mean().sort_values(ascending=False)
