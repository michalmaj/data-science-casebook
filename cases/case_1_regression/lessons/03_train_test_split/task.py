"""Lesson 3 task: split the data before you look at it any further.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "transport_delays.csv"

RANDOM_STATE = 20260707


def load_shipments(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV and drop rows missing `weather`.

    TODO: read the CSV at `path`, then drop rows where `weather` is
    missing. Return the result — same cleaning as Lesson 2.
    """
    raise NotImplementedError("load_shipments is not implemented yet")


def split_shipments(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split `df` into (train_df, test_df) — 80/20, reproducible.

    TODO: import `train_test_split` from `sklearn.model_selection` and use
    it with `test_size=0.2` and `random_state=RANDOM_STATE`. Return
    (train_df, test_df) in that order.

    Do this before anything else in this case touches the data again —
    everything from here on (exploration, feature choices, baselines,
    models) may only look at train_df. test_df goes into a sealed
    envelope until the final evaluation.
    """
    raise NotImplementedError("split_shipments is not implemented yet")


def impute_driver_experience(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing `driver_experience_years` using the training set's median only.

    TODO: compute the median of train_df["driver_experience_years"] (pandas'
    .median() ignores missing values by default). Fill missing values in
    both train_df and test_df with that single median — never compute a
    separate median from test_df, and never recompute it from the two
    frames combined. Return (train_df, test_df) in that order.
    """
    raise NotImplementedError("impute_driver_experience is not implemented yet")
