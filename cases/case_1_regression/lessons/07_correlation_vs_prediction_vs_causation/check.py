"""Self-check for Lesson 7. Run with `uv run pytest` in this directory.

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


def test_split_shipments_produces_expected_sizes():
    df = lesson.load_clean_shipments()
    train_df, test_df = lesson.split_shipments(df)
    assert len(train_df) == 394
    assert len(test_df) == 99


def test_num_stops_coefficient_is_stable_across_feature_sets():
    df = lesson.load_clean_shipments()
    train_df, _ = lesson.split_shipments(df)

    model_alone = lesson.fit_model_on(train_df, ["num_stops"])
    coef_alone = lesson.coefficient_for(model_alone, ["num_stops"], "num_stops")

    model_full = lesson.fit_model_on(train_df, lesson.FEATURE_COLUMNS)
    coef_full = lesson.coefficient_for(model_full, lesson.FEATURE_COLUMNS, "num_stops")

    assert abs(coef_alone - 3.08023) < 1e-3
    assert abs(coef_full - 3.08826) < 1e-3
    assert abs(coef_alone - coef_full) < 0.05


def test_distance_km_coefficient_is_unstable_when_collinear_feature_added():
    df = lesson.load_clean_shipments()
    train_df, _ = lesson.split_shipments(df)

    model_alone = lesson.fit_model_on(train_df, ["distance_km"])
    coef_alone = lesson.coefficient_for(model_alone, ["distance_km"], "distance_km")

    model_with_planned = lesson.fit_model_on(train_df, ["distance_km", "planned_duration_min"])
    coef_with_planned = lesson.coefficient_for(
        model_with_planned, ["distance_km", "planned_duration_min"], "distance_km"
    )

    assert abs(coef_alone - (-0.01102)) < 1e-3
    assert abs(coef_with_planned - (-0.05449)) < 1e-3
    assert abs(coef_with_planned - coef_alone) > 0.03


def test_distance_km_and_planned_duration_min_are_highly_collinear():
    df = lesson.load_clean_shipments()
    train_df, _ = lesson.split_shipments(df)
    corr = train_df["distance_km"].corr(train_df["planned_duration_min"])
    assert corr > 0.9
