"""Self-check for Lesson 4. Run with `uv run pytest` in this directory.

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


def test_load_clean_shipments_returns_493_rows():
    df = lesson.load_clean_shipments()
    assert len(df) == 493


def test_predict_mean_baseline_matches_historical_mean():
    df = lesson.load_clean_shipments()
    predicted = lesson.predict_mean_baseline(df)
    assert len(predicted) == len(df)
    assert abs(predicted.iloc[0] - 13.2331) < 1e-3
    assert predicted.nunique() == 1


def test_predict_zero_baseline_is_all_zero():
    df = lesson.load_clean_shipments()
    predicted = lesson.predict_zero_baseline(df)
    assert len(predicted) == len(df)
    assert (predicted == 0.0).all()


def test_mean_baseline_beats_zero_baseline_on_both_metrics():
    df = lesson.load_clean_shipments()
    actual = df["delay_minutes"]
    mean_pred = lesson.predict_mean_baseline(df)
    zero_pred = lesson.predict_zero_baseline(df)

    mean_mae = lesson.mean_absolute_error(actual, mean_pred)
    zero_mae = lesson.mean_absolute_error(actual, zero_pred)
    mean_rmse = lesson.root_mean_squared_error(actual, mean_pred)
    zero_rmse = lesson.root_mean_squared_error(actual, zero_pred)

    assert abs(mean_mae - 11.7029) < 1e-3
    assert abs(zero_mae - 15.8006) < 1e-3
    assert abs(mean_rmse - 14.4884) < 1e-3
    assert abs(zero_rmse - 19.6221) < 1e-3
    assert mean_mae < zero_mae
    assert mean_rmse < zero_rmse


def test_rmse_of_mean_baseline_equals_population_std_dev():
    df = lesson.load_clean_shipments()
    actual = df["delay_minutes"]
    mean_pred = lesson.predict_mean_baseline(df)
    rmse = lesson.root_mean_squared_error(actual, mean_pred)
    assert abs(rmse - actual.std(ddof=0)) < 1e-6
