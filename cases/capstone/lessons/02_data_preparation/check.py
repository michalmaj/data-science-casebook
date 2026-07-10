"""Self-check for Lesson 2. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

import pytest

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


@pytest.mark.parametrize(
    ("name", "expected_len"),
    [
        ("clinic_wait_times", 400),
        ("lendwell_loan_default", 400),
        ("retail_store_segments", 250),
    ],
)
def test_load_dataset_returns_expected_row_count(name, expected_len):
    df = lesson.load_dataset(name)
    assert len(df) == expected_len


@pytest.mark.parametrize(
    ("name", "expected_missing"),
    [
        ("clinic_wait_times", {"department": 8, "staff_on_duty": 10}),
        ("lendwell_loan_default", {"employment_years": 10}),
        ("retail_store_segments", {"foot_traffic": 8}),
    ],
)
def test_missing_value_counts_matches_known_gaps(name, expected_missing):
    df = lesson.load_dataset(name)
    counts = lesson.missing_value_counts(df)
    for column, expected_count in expected_missing.items():
        assert counts[column] == expected_count


@pytest.mark.parametrize(
    ("name", "expected_shape"),
    [
        ("clinic_wait_times", (400, 8)),
        ("lendwell_loan_default", (400, 9)),
        ("retail_store_segments", (250, 8)),
    ],
)
def test_clean_dataset_removes_all_missing_and_preserves_shape(name, expected_shape):
    df = lesson.load_dataset(name)
    cleaned = lesson.clean_dataset(df)
    assert cleaned.shape == expected_shape
    assert cleaned.isna().sum().sum() == 0


@pytest.mark.parametrize(
    ("name", "column", "expected_value"),
    [
        ("clinic_wait_times", "department", "General"),
        ("clinic_wait_times", "staff_on_duty", 4.0),
        ("lendwell_loan_default", "employment_years", 15.0),
        ("retail_store_segments", "foot_traffic", 5815.0),
    ],
)
def test_clean_dataset_matches_known_fill_values(name, column, expected_value):
    df = lesson.load_dataset(name)
    original_missing_idx = df.index[df[column].isna()]
    cleaned = lesson.clean_dataset(df)
    filled_values = cleaned.loc[original_missing_idx, column]
    assert (filled_values == expected_value).all()
