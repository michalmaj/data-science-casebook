"""Self-check for Lesson 5. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

from sklearn.linear_model import LinearRegression

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


def test_load_split_impute_match_lesson_3():
    df = lesson.load_shipments()
    assert len(df) == 493
    train_df, test_df = lesson.split_shipments(df)
    assert len(train_df) == 394
    assert len(test_df) == 99
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    assert train_df.isna().sum().sum() == 0
    assert test_df.isna().sum().sum() == 0


def test_predict_zero_baseline_is_all_zero():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    predicted = lesson.predict_zero_baseline(test_df)
    assert len(predicted) == len(test_df)
    assert (predicted == 0.0).all()


def test_predict_mean_baseline_in_sample_matches_train_mean():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    predicted = lesson.predict_mean_baseline(train_df, train_df)
    assert len(predicted) == len(train_df)
    assert predicted.nunique() == 1
    assert abs(predicted.iloc[0] - 13.09492385786802) < 1e-6


def test_mean_baseline_beats_zero_baseline_in_sample():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    actual = train_df["delay_minutes"]
    mean_pred = lesson.predict_mean_baseline(train_df, train_df)
    zero_pred = lesson.predict_zero_baseline(train_df)

    mean_mae = lesson.mean_absolute_error(actual, mean_pred)
    zero_mae = lesson.mean_absolute_error(actual, zero_pred)
    mean_rmse = lesson.root_mean_squared_error(actual, mean_pred)
    zero_rmse = lesson.root_mean_squared_error(actual, zero_pred)

    assert abs(mean_mae - 11.6070) < 1e-3
    assert abs(zero_mae - 15.5487) < 1e-3
    assert abs(mean_rmse - 14.3083) < 1e-3
    assert abs(zero_rmse - 19.3960) < 1e-3
    assert mean_mae < zero_mae
    assert mean_rmse < zero_rmse


def test_rmse_of_in_sample_mean_baseline_equals_train_std_dev():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    actual = train_df["delay_minutes"]
    mean_pred = lesson.predict_mean_baseline(train_df, train_df)
    rmse = lesson.root_mean_squared_error(actual, mean_pred)
    assert abs(rmse - actual.std(ddof=0)) < 1e-6


def test_fit_model_returns_fitted_linear_regression():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    model = lesson.fit_model(train_df)
    assert isinstance(model, LinearRegression)
    assert len(model.coef_) == 4


def test_model_beats_fair_baseline_beats_zero_baseline_on_test_set():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    model = lesson.fit_model(train_df)
    model_pred = lesson.predict_delay(model, test_df)
    mean_pred = lesson.predict_mean_baseline(train_df, test_df)
    zero_pred = lesson.predict_zero_baseline(test_df)
    actual = test_df["delay_minutes"]

    model_mae = lesson.mean_absolute_error(actual, model_pred)
    model_rmse = lesson.root_mean_squared_error(actual, model_pred)
    mean_mae = lesson.mean_absolute_error(actual, mean_pred)
    mean_rmse = lesson.root_mean_squared_error(actual, mean_pred)
    zero_mae = lesson.mean_absolute_error(actual, zero_pred)
    zero_rmse = lesson.root_mean_squared_error(actual, zero_pred)

    assert abs(model_mae - 10.2127) < 1e-3
    assert abs(model_rmse - 12.8064) < 1e-3
    assert abs(mean_mae - 12.0751) < 1e-3
    assert abs(mean_rmse - 15.1869) < 1e-3
    assert abs(zero_mae - 16.8030) < 1e-3
    assert abs(zero_rmse - 20.4972) < 1e-3
    assert zero_mae > mean_mae > model_mae
    assert zero_rmse > mean_rmse > model_rmse
