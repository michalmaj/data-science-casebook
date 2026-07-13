"""Reference solution for Lesson 8. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
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


def final_scorecard(
    train_df: pd.DataFrame, test_df: pd.DataFrame, model: LinearRegression
) -> pd.DataFrame:
    actual = test_df["delay_minutes"]

    zero_pred = pd.Series(0.0, index=test_df.index)
    mean_pred = pd.Series(train_df["delay_minutes"].mean(), index=test_df.index)
    model_pred = model.predict(test_df[FEATURE_COLUMNS])

    rows = {}
    for name, predicted in [
        ("zero_baseline", zero_pred),
        ("mean_baseline", mean_pred),
        ("linear_model", model_pred),
    ]:
        rows[name] = {
            "mae": mean_absolute_error(actual, predicted),
            "rmse": root_mean_squared_error(actual, predicted),
        }
    return pd.DataFrame(rows).T[["mae", "rmse"]]
