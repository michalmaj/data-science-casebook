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


def test_load_and_merge_orders_returns_700_rows():
    df = lesson.load_and_merge_orders()
    assert df.shape == (700, 9)


def test_predict_majority_baseline_always_predicts_not_returned():
    df = lesson.load_and_merge_orders()
    predicted = lesson.predict_majority_baseline(df)
    assert len(predicted) == len(df)
    assert predicted.nunique() == 1
    assert predicted.iloc[0] == 0


def test_accuracy_of_majority_baseline_matches_class_balance():
    df = lesson.load_and_merge_orders()
    predicted = lesson.predict_majority_baseline(df)
    acc = lesson.accuracy(df["is_returned"], predicted)
    assert abs(acc - 0.86) < 1e-9


def test_confusion_counts_show_zero_true_positives():
    df = lesson.load_and_merge_orders()
    predicted = lesson.predict_majority_baseline(df)
    counts = lesson.confusion_counts(df["is_returned"], predicted)
    assert counts == {"tp": 0, "fp": 0, "tn": 602, "fn": 98}
    assert sum(counts.values()) == len(df)
