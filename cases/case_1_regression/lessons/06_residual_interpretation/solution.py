"""Reference solution for Lesson 6. Do not open this before attempting task.py."""

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
