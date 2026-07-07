"""Reference solution for Lesson 7. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"

RANDOM_STATE = 20260707
FEATURE_COLUMNS = ["distance_km", "num_stops", "driver_experience_years", "vehicle_age_years"]


def load_clean_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.dropna(subset=["weather"])
    median_experience = df["driver_experience_years"].median()
    return df.fillna({"driver_experience_years": median_experience})


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=RANDOM_STATE)
    return train_df, test_df


def fit_model_on(train_df: pd.DataFrame, feature_columns: list[str]) -> LinearRegression:
    model = LinearRegression()
    model.fit(train_df[feature_columns], train_df["delay_minutes"])
    return model


def coefficient_for(model: LinearRegression, feature_columns: list[str], column: str) -> float:
    return model.coef_[feature_columns.index(column)]
