"""Lesson 3 task: look at how your dataset's numeric features relate to each other.

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


def load_clean_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load and clean the dataset called `name`, same as Lessons 1-2 combined.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv. Then, on a
    copy of that DataFrame, for every column with any missing values: if
    the column is numeric (pandas.api.types.is_numeric_dtype), fill it
    with the column's median; otherwise fill it with the column's most
    frequent value (column.mode().iloc[0]). Return the cleaned DataFrame.
    """
    raise NotImplementedError("load_clean_dataset is not implemented yet")


def numeric_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """Return the pairwise Pearson correlation matrix of df's numeric columns.

    TODO: use df.select_dtypes(include="number") to keep only the numeric
    (int/float) columns — this automatically excludes ID columns,
    category columns, and boolean columns regardless of what they're
    called. Call .corr() on the result and return it.
    """
    raise NotImplementedError("numeric_correlations is not implemented yet")
