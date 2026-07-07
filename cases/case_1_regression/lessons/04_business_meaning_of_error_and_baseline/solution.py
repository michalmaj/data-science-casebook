"""Reference solution for Lesson 4. Do not open this before attempting task.py."""

from pathlib import Path

import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"


def load_clean_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.dropna(subset=["weather"])
    median_experience = df["driver_experience_years"].median()
    return df.fillna({"driver_experience_years": median_experience})


def predict_mean_baseline(df: pd.DataFrame) -> pd.Series:
    mean_delay = df["delay_minutes"].mean()
    return pd.Series(mean_delay, index=df.index)


def predict_zero_baseline(df: pd.DataFrame) -> pd.Series:
    return pd.Series(0.0, index=df.index)


def mean_absolute_error(actual: pd.Series, predicted: pd.Series) -> float:
    return float(np.mean(np.abs(actual - predicted)))


def root_mean_squared_error(actual: pd.Series, predicted: pd.Series) -> float:
    return float(np.sqrt(np.mean((actual - predicted) ** 2)))
