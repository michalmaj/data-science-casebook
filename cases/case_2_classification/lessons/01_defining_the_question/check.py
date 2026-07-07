"""Self-check for Lesson 1. Run with `uv run pytest` in this directory.

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


def test_list_sheet_names_returns_both_sheets():
    assert lesson.list_sheet_names() == ["Orders", "Customers"]


def test_load_raw_orders_sheet_reveals_the_header_problem():
    df = lesson.load_raw_orders_sheet()
    assert df.shape == (702, 7)
    assert df.columns[0] == "Q1 2026 Order Export"


def test_target_column_name_is_is_returned():
    assert lesson.target_column_name() == "is_returned"
