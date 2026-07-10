"""Reference solution for Lesson 3. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATASET_MENU = [
    "clinic_wait_times",
    "lendwell_loan_default",
    "retail_store_segments",
]


def load_clean_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    df = pd.read_csv(data_dir / f"{name}.csv")
    cleaned = df.copy()
    for column in cleaned.columns:
        if cleaned[column].isna().any():
            if pd.api.types.is_numeric_dtype(cleaned[column]):
                cleaned[column] = cleaned[column].fillna(cleaned[column].median())
            else:
                mode_value = cleaned[column].mode().iloc[0]
                cleaned[column] = cleaned[column].fillna(mode_value)
    return cleaned


def numeric_correlations(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include="number").corr()
