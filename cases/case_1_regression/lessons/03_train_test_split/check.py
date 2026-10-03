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


def test_load_shipments_returns_493_rows():
    df = lesson.load_shipments()
    assert len(df) == 493


def test_split_shipments_produces_expected_sizes():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    assert len(train_df) == 394
    assert len(test_df) == 99
    assert len(train_df) + len(test_df) == len(df)


def test_split_shipments_is_reproducible():
    df = lesson.load_shipments()
    train_1, test_1 = lesson.split_shipments(df)
    train_2, test_2 = lesson.split_shipments(df)
    assert list(train_1.index) == list(train_2.index)
    assert list(test_1.index) == list(test_2.index)


def test_impute_driver_experience_uses_train_median_only():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    assert train_df["driver_experience_years"].isna().sum() == 7
    assert test_df["driver_experience_years"].isna().sum() == 1

    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    assert train_df["driver_experience_years"].isna().sum() == 0
    assert test_df["driver_experience_years"].isna().sum() == 0
    assert abs(train_df["driver_experience_years"].median() - 12.0) < 1e-9


def test_impute_driver_experience_does_not_use_test_statistics():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    # The full-dataset median (computed before any split) is 13.0 — see
    # Lesson 2's data-quality check. If a solution accidentally pools
    # train+test (or uses the test set alone) before imputing, the fill
    # value drifts away from the train-only median of 12.0 asserted above.
    full_median_before_split = df["driver_experience_years"].median()
    assert abs(full_median_before_split - 13.0) < 1e-9
    train_df, _ = lesson.impute_driver_experience(train_df, test_df)
    assert abs(train_df["driver_experience_years"].median() - full_median_before_split) > 0.5
