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
RANDOM_STATE = 42


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


def split_dataset(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = RANDOM_STATE,
    stratify_column: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split df into (train_df, test_df). Only meaningful for a dataset with a target.

    TODO: import train_test_split from sklearn.model_selection. If
    stratify_column is not None, pass df[stratify_column] as the stratify
    argument to train_test_split — this keeps the same class balance in
    both train_df and test_df, which matters for classification with an
    imbalanced target. Otherwise pass stratify=None. Call it with
    test_size=test_size and random_state=random_state. Return the
    result as (train_df, test_df), in that order. For the two predictive
    datasets in this menu, this is where your train/test split actually
    happens — before anything below computes a fill value or a
    correlation from data that should stay unseen until final
    evaluation. The clustering dataset has no target to protect this
    way, so its notebook branch skips this function and uses
    clean_dataset on the whole dataset instead, same as before.
    """
    raise NotImplementedError("split_dataset is not implemented yet")


def impute_missing(
    train_df: pd.DataFrame, test_df: pd.DataFrame, feature_columns: list[str]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing values in both frames using statistics from train_df only.

    TODO: on copies of train_df and test_df, for every column in
    feature_columns where train_df OR test_df has any missing value: if
    the column is numeric (pandas.api.types.is_numeric_dtype), compute
    fill_value as train_df[column].median(); otherwise as
    train_df[column].mode().iloc[0]. Fill that value into both train_df
    and test_df for that column (never compute a fill value from
    test_df — only train_df). Only touch columns in feature_columns —
    never the target column or any column not in that list, even if it
    has missing values too. Return (train_df, test_df).
    """
    raise NotImplementedError("impute_missing is not implemented yet")


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
