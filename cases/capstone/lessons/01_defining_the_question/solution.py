"""Reference solution for Lesson 1. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATASET_MENU = [
    "clinic_wait_times",
    "lendwell_loan_default",
    "retail_store_segments",
]


def list_datasets(data_dir: Path = DATA_DIR) -> list[str]:
    return sorted(path.stem for path in data_dir.glob("*.csv"))


def load_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    return pd.read_csv(data_dir / f"{name}.csv")


def missing_value_counts(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum()
