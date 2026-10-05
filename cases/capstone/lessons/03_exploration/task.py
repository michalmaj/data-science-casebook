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
RANDOM_STATE = 42


def load_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load the dataset called `name` — no cleaning yet, same as Lesson 2.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv and return it.
    Used by the two predictive paths, which split and impute below instead
    of cleaning the whole dataset the way load_clean_dataset does.
    """
    raise NotImplementedError("load_dataset is not implemented yet")


def split_dataset(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = RANDOM_STATE,
    stratify_column: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split df into (train_df, test_df), same recipe as Lesson 2.

    TODO: import train_test_split from sklearn.model_selection. If
    stratify_column is not None, pass df[stratify_column] as the stratify
    argument to train_test_split. Otherwise pass stratify=None. Call it
    with test_size=test_size and random_state=random_state. Return the
    result as (train_df, test_df), in that order. For the two predictive
    datasets, exploring a feature's relationship to the target only ever
    makes sense on train_df — seeing that relationship using rows that
    will later become your test set previews information you're supposed
    to hold out.
    """
    raise NotImplementedError("split_dataset is not implemented yet")


def impute_missing(
    train_df: pd.DataFrame, test_df: pd.DataFrame, feature_columns: list[str]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing values in both frames using statistics from train_df only, same as Lesson 2.

    TODO: on copies of train_df and test_df, for every column in
    feature_columns where train_df OR test_df has any missing value: if
    the column is numeric (pandas.api.types.is_numeric_dtype), compute
    fill_value as train_df[column].median(); otherwise as
    train_df[column].mode().iloc[0]. Fill that value into both train_df
    and test_df for that column. Return (train_df, test_df).
    """
    raise NotImplementedError("impute_missing is not implemented yet")


def load_clean_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load and clean the dataset called `name`, same as Lessons 1-2 combined.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv. Then, on a
    copy of that DataFrame, for every column with any missing values: if
    the column is numeric (pandas.api.types.is_numeric_dtype), fill it
    with the column's median; otherwise fill it with the column's most
    frequent value (column.mode().iloc[0]). Return the cleaned DataFrame.
    Used only by the segmentation path — there's no train/test split to
    protect for a clustering problem, so the whole dataset is explored at
    once, same as Lesson 2's clean_dataset.
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
