"""Reference solution for Lesson 1. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"


def load_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def target_column_name() -> str:
    return "delay_minutes"


def missing_value_counts(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum()
