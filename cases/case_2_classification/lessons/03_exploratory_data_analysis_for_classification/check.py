"""Self-check for Lesson 3. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


def test_load_and_merge_orders_returns_700_rows():
    df = lesson.load_and_merge_orders()
    assert df.shape == (700, 9)


def test_class_balance_shows_returns_are_rare():
    df = lesson.load_and_merge_orders()
    balance = lesson.class_balance(df)
    assert list(balance.index) == [0, 1]
    assert abs(balance[0] - 0.86) < 1e-9
    assert abs(balance[1] - 0.14) < 1e-9


def test_return_rate_by_category_ranks_clothing_worst():
    df = lesson.load_and_merge_orders()
    rates = lesson.return_rate_by_category(df)
    assert list(rates.index) == ["clothing", "books", "electronics", "home_goods"]
    assert abs(rates["clothing"] - 0.20430107526881722) < 1e-6
    assert abs(rates["home_goods"] - 0.06993006993006994) < 1e-6


def test_correlation_with_return_account_age_is_the_strongest_numeric_signal():
    df = lesson.load_and_merge_orders()
    r_discount = lesson.correlation_with_return(df, "discount_percent")
    r_history = lesson.correlation_with_return(df, "previous_returns_count")
    r_age = lesson.correlation_with_return(df, "account_age_days")
    assert abs(r_discount - 0.06284010311118024) < 1e-6
    assert abs(r_history - 0.092348926373032) < 1e-6
    assert abs(r_age - (-0.18337519836527483)) < 1e-6
    assert abs(r_age) > abs(r_discount)
    assert abs(r_age) > abs(r_history)
