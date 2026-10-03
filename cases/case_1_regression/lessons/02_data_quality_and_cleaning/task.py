"""Lesson 2 task: decide what to do with missing values, and clean the data.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"


def load_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the shipments CSV at `path` into a DataFrame.

    TODO: read the CSV at `path` and return it as a pandas DataFrame.
    """
    raise NotImplementedError("load_shipments is not implemented yet")


def rows_with_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return the subset of rows in `df` that have at least one missing value.

    TODO: use a pandas method to select rows where any column is missing.
    """
    raise NotImplementedError("rows_with_missing_data is not implemented yet")


def drop_missing_weather(df: pd.DataFrame) -> pd.DataFrame:
    """Return `df` with rows that have a missing `weather` value removed.

    TODO: weather can't be reasonably guessed after the fact, and only a
    small fraction of rows are affected, so we drop them rather than invent
    a category.
    """
    raise NotImplementedError("drop_missing_weather is not implemented yet")
