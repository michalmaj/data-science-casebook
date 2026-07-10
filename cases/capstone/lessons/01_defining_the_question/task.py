"""Lesson 1 task: pick a client from the menu and load their data.

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


def list_datasets(data_dir: Path = DATA_DIR) -> list[str]:
    """Return the names of every dataset available in data_dir, sorted.

    TODO: use data_dir.glob("*.csv") to find every CSV file in data_dir,
    take each file's stem (filename without the .csv extension) as its
    dataset name, and return the names sorted alphabetically as a list.
    """
    raise NotImplementedError("list_datasets is not implemented yet")


def load_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load the dataset called `name` from data_dir.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv and return
    the resulting DataFrame.
    """
    raise NotImplementedError("load_dataset is not implemented yet")


def missing_value_counts(df: pd.DataFrame) -> pd.Series:
    """Return the number of missing values in each column of df.

    TODO: use df.isna().sum() and return the result.
    """
    raise NotImplementedError("missing_value_counts is not implemented yet")
