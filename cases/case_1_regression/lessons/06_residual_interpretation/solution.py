"""Reference solution for Lesson 6. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"

RANDOM_STATE = 20260707
FEATURE_COLUMNS = ["distance_km", "num_stops", "driver_experience_years", "vehicle_age_years"]


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


def fit_model(train_df: pd.DataFrame) -> LinearRegression:
    model = LinearRegression()
    model.fit(train_df[FEATURE_COLUMNS], train_df["delay_minutes"])
    return model


def compute_residuals(model: LinearRegression, df: pd.DataFrame) -> pd.Series:
    predicted = model.predict(df[FEATURE_COLUMNS])
    return df["delay_minutes"] - predicted


def mean_residual_by_weather(df: pd.DataFrame, residuals: pd.Series) -> pd.Series:
    return residuals.groupby(df["weather"]).mean().sort_values(ascending=False)


def residual_correlation_with_feature(
    df: pd.DataFrame, residuals: pd.Series, column: str
) -> float:
    return residuals.corr(df[column])
