"""Generate the synthetic Case 3 Aurora Stream subscriber dataset (SQLite, two tables).

Deterministic (fixed seed) and committed as a static file — every student
works from the same data. Re-run only if you intend to change the dataset
itself, and re-commit the resulting file.
"""

import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260709
N_SUBSCRIBERS = 300
OUTPUT_PATH = Path(__file__).parent / "aurora_stream.sqlite"

PLAN_TIERS = ["basic", "standard", "premium"]
PLAN_TIER_PROBS = [0.4, 0.4, 0.2]
COUNTRIES = ["USA", "Canada", "UK", "Germany", "Poland", "Brazil"]
DEVICE_TYPES = ["tv", "mobile", "desktop", "tablet"]
DEVICE_TYPE_PROBS = [0.4, 0.35, 0.15, 0.1]

# Three rough, deliberately-not-perfectly-separable viewing archetypes.
ARCHETYPES = ["binge", "casual", "at_risk"]
ARCHETYPE_PROBS = [0.3, 0.45, 0.25]
ARCHETYPE_SESSION_RATE = {"binge": 45, "casual": 18, "at_risk": 4}
ARCHETYPE_MINUTES_MEAN = {"binge": 95, "casual": 45, "at_risk": 20}

WINDOW_DAYS = 90
REFERENCE_DATE = pd.Timestamp("2026-04-01")


def generate_subscribers(rng: np.random.Generator) -> tuple[pd.DataFrame, np.ndarray]:
    subscriber_ids = [f"SUB-{i:04d}" for i in range(1, N_SUBSCRIBERS + 1)]
    signup_offsets = rng.integers(30, 900, N_SUBSCRIBERS)
    signup_dates = [REFERENCE_DATE - pd.Timedelta(days=int(d)) for d in signup_offsets]
    plan_tier = rng.choice(PLAN_TIERS, N_SUBSCRIBERS, p=PLAN_TIER_PROBS)
    country = rng.choice(COUNTRIES, N_SUBSCRIBERS)
    archetype = rng.choice(ARCHETYPES, N_SUBSCRIBERS, p=ARCHETYPE_PROBS)

    subscribers_df = pd.DataFrame(
        {
            "subscriber_id": subscriber_ids,
            "signup_date": [d.strftime("%Y-%m-%d") for d in signup_dates],
            "plan_tier": plan_tier,
            "country": country,
        }
    )
    return subscribers_df, archetype


def generate_sessions(
    rng: np.random.Generator, subscribers_df: pd.DataFrame, archetype: np.ndarray
) -> pd.DataFrame:
    rows = []
    for idx, row in subscribers_df.iterrows():
        arch = archetype[idx]
        n_sessions = max(0, int(rng.poisson(ARCHETYPE_SESSION_RATE[arch])))
        if n_sessions == 0:
            continue
        session_day_offsets = rng.integers(0, WINDOW_DAYS, n_sessions)
        minutes = rng.normal(
            ARCHETYPE_MINUTES_MEAN[arch], ARCHETYPE_MINUTES_MEAN[arch] * 0.3, n_sessions
        )
        minutes = np.clip(minutes, 2, None).round().astype(int)
        devices = rng.choice(DEVICE_TYPES, n_sessions, p=DEVICE_TYPE_PROBS)
        for offset, mins, device in zip(session_day_offsets, minutes, devices, strict=True):
            session_date = REFERENCE_DATE - pd.Timedelta(days=int(offset))
            rows.append(
                {
                    "subscriber_id": row["subscriber_id"],
                    "session_date": session_date.strftime("%Y-%m-%d"),
                    "minutes_watched": int(mins),
                    "device_type": device,
                }
            )
    return pd.DataFrame(rows)


def main() -> None:
    rng = np.random.default_rng(SEED)
    subscribers_df, archetype = generate_subscribers(rng)
    sessions_df = generate_sessions(rng, subscribers_df, archetype)

    if OUTPUT_PATH.exists():
        OUTPUT_PATH.unlink()
    conn = sqlite3.connect(OUTPUT_PATH)
    subscribers_df.to_sql("subscribers", conn, index=False)
    sessions_df.to_sql("sessions", conn, index=False)
    conn.close()

    n_subscribers, n_sessions = len(subscribers_df), len(sessions_df)
    print(f"Wrote {n_subscribers} subscribers and {n_sessions} sessions to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
