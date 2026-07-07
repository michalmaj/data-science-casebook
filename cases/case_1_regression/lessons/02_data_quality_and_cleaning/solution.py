"""Reference solution for Lesson 2. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"


def load_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def rows_with_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.isna().any(axis=1)]


def drop_missing_weather(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(subset=["weather"])


def impute_missing_experience(df: pd.DataFrame) -> pd.DataFrame:
    median_experience = df["driver_experience_years"].median()
    return df.fillna({"driver_experience_years": median_experience})


def clean_shipments(df: pd.DataFrame) -> pd.DataFrame:
    return impute_missing_experience(drop_missing_weather(df))
