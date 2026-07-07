"""Lesson 1 task: load the shipments data and take the first look at it.

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


def target_column_name() -> str:
    """Return the name of the column TransLine wants to predict.

    TODO: look at the columns in the CSV and decide which one represents
    the business question ("how late will this shipment be?"). Return its
    exact column name as a string.
    """
    raise NotImplementedError("target_column_name is not implemented yet")


def missing_value_counts(df: pd.DataFrame) -> pd.Series:
    """Return the number of missing values in each column of `df`.

    TODO: use a pandas method to count missing values per column.
    """
    raise NotImplementedError("missing_value_counts is not implemented yet")
