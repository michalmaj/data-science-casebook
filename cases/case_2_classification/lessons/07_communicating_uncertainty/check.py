"""Self-check for Lesson 7. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

from sklearn.linear_model import LogisticRegression

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


def test_split_orders_produces_expected_sizes_and_preserves_balance():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    assert len(train_df) == 560
    assert len(test_df) == 140
    assert train_df["is_returned"].sum() == 78
    assert test_df["is_returned"].sum() == 20


def test_fit_classifier_returns_fitted_logistic_regression():
    df = lesson.load_and_merge_orders()
    train_df, _ = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    assert isinstance(model, LogisticRegression)
    assert model.n_features_in_ == 3


def test_risk_tier_assigns_low_medium_high_at_the_right_boundaries():
    assert lesson.risk_tier(0.05) == "Low"
    assert lesson.risk_tier(0.14) == "Low"
    assert lesson.risk_tier(0.15) == "Medium"
    assert lesson.risk_tier(0.29) == "Medium"
    assert lesson.risk_tier(0.30) == "High"
    assert lesson.risk_tier(0.90) == "High"


def test_risk_report_shape_and_tier_counts_on_test_set():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    report = lesson.risk_report(model, test_df)

    assert report.shape == (140, 3)
    assert list(report.columns) == ["order_id", "probability", "risk_tier"]

    counts = report["risk_tier"].value_counts()
    assert counts["Low"] == 79
    assert counts["Medium"] == 44
    assert counts["High"] == 17


def test_risk_report_tiers_show_real_but_noisy_return_rates():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    report = lesson.risk_report(model, test_df)

    combined = report.assign(actual=test_df["is_returned"].values)
    rates = combined.groupby("risk_tier")["actual"].mean()

    assert abs(rates["Low"] - 0.08860759493670886) < 1e-9
    assert abs(rates["Medium"] - 0.22727272727272727) < 1e-9
    assert abs(rates["High"] - 0.17647058823529413) < 1e-9


def test_tier_summary_shape_and_columns():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    summary = lesson.tier_summary(model, test_df, "is_returned")

    assert summary.shape == (3, 3)
    assert list(summary.columns) == ["count", "mean_predicted", "mean_observed"]
    assert list(summary.index) == ["Low", "Medium", "High"]


def test_tier_summary_matches_known_values():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    summary = lesson.tier_summary(model, test_df, "is_returned")

    assert summary.loc["Low", "count"] == 79
    assert summary.loc["Medium", "count"] == 44
    assert summary.loc["High", "count"] == 17
    assert abs(summary.loc["Low", "mean_predicted"] - 0.09100661556291169) < 1e-9
    assert abs(summary.loc["Medium", "mean_predicted"] - 0.2209558203307167) < 1e-9
    assert abs(summary.loc["High", "mean_predicted"] - 0.38254349551732125) < 1e-9
    assert abs(summary.loc["Low", "mean_observed"] - 0.08860759493670886) < 1e-9
    assert abs(summary.loc["Medium", "mean_observed"] - 0.22727272727272727) < 1e-9
    assert abs(summary.loc["High", "mean_observed"] - 0.17647058823529413) < 1e-9


def test_tier_summary_reveals_high_tier_overconfidence():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    summary = lesson.tier_summary(model, test_df, "is_returned")

    gap = summary.loc["High", "mean_predicted"] - summary.loc["High", "mean_observed"]
    assert gap > 0.15


def test_brier_score_matches_known_value():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    score = lesson.brier_score(model, test_df, "is_returned")
    assert abs(score - 0.12423584361192758) < 1e-9
