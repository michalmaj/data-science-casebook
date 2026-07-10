"""Lesson 2 task: assess data quality and clean it before doing anything else.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATASET_MENU = [
    "clinic_wait_times",
    "lendwell_loan_default",
    "retail_store_segments",
]


def load_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load the dataset called `name` from data_dir, same as Lesson 1.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv and return
    the resulting DataFrame.
    """
    raise NotImplementedError("load_dataset is not implemented yet")


def missing_value_counts(df: pd.DataFrame) -> pd.Series:
    """Return the number of missing values in each column of df, same as Lesson 1.

    TODO: use df.isna().sum() and return the result.
    """
    raise NotImplementedError("missing_value_counts is not implemented yet")


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Fill every missing value: numeric columns get the median, others get the mode.

    TODO: work on a copy of df (df.copy()). For every column that has any
    missing values (column.isna().any()): if the column is numeric
    (pandas.api.types.is_numeric_dtype(column)), fill its missing values
    with the column's median (column.median()); otherwise, fill them with
    the column's most frequent value (column.mode().iloc[0]). Return the
    resulting DataFrame — same shape as the input, with no missing values
    left in any column.
    """
    raise NotImplementedError("clean_dataset is not implemented yet")
