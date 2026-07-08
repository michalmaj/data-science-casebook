"""Lesson 1 task: get your first look at Aurora Stream's subscriber data.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "aurora_stream.sqlite"

REFERENCE_DATE = "2026-04-01"


def list_tables(path: Path = DATA_PATH) -> list[str]:
    """Return the names of every table in the SQLite database at `path`.

    TODO: open a connection with sqlite3.connect, query the sqlite_master
    table for rows where type='table' (e.g. "SELECT name FROM sqlite_master
    WHERE type='table' ORDER BY name"), and return the table names as a
    sorted list of strings.
    """
    raise NotImplementedError("list_tables is not implemented yet")


def load_subscriber_features(path: Path = DATA_PATH) -> pd.DataFrame:
    """Return one row per subscriber with session-based features, joined and aggregated.

    TODO: write a SQL query that LEFT JOINs subscribers to sessions (so
    subscribers with zero sessions aren't dropped), grouped by
    subscriber_id, selecting: subscriber_id, plan_tier, country,
    session_count (COUNT of sessions), total_minutes_watched (SUM of
    minutes_watched, COALESCEd to 0), avg_minutes_per_session (AVG of
    minutes_watched, COALESCEd to 0), and tenure_days (the number of days
    between signup_date and REFERENCE_DATE, using SQLite's julianday()
    function — pass REFERENCE_DATE as a bound query parameter, not a
    literal in the SQL string). Run it with pandas.read_sql_query and
    return the resulting DataFrame.
    """
    raise NotImplementedError("load_subscriber_features is not implemented yet")
