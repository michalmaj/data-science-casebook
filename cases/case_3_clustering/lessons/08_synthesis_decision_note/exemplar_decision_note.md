# Exemplar Decision Note — Case 3 (Aurora Stream)

*This is a model answer, written after completing all of Case 3. Don't read it before writing your own — the point of the exercise is to reach these conclusions yourself; this exists so you can compare your reasoning to a strong answer afterward, not so you can copy it.*

## 1. Business question

Does Aurora Stream's subscriber base actually split into distinct behavioral groups — beyond the plan tiers we already track — that would justify different retention offers, or is "one offer for everyone" already the right call?

## 2. Approach

I extracted four engagement/tenure features per subscriber (`session_count`, `total_minutes_watched`, `avg_minutes_per_session`, `tenure_days`) via SQL, standardized them with `StandardScaler`, and fit KMeans at several values of k. I compared inertia and silhouette score across k, checked cluster-assignment stability under resampling and under KMeans's random initialization, checked how much the result depends on which features were used (robust at k=2, less so at finer k), and settled on k=2.

## 3. Results (final segment table, k=2)

| Segment | Size | Share | Notes |
|---|---:|---:|---|
| 0 | 219 | 73% | Below-average engagement across all three viewing features |
| 1 | 81 | 27% | Above-average engagement across all three viewing features |

## 4. Choosing k and checking stability

Inertia and silhouette score didn't agree on a single "best" k — inertia has no sharp elbow across k=2 to 8, and silhouette peaks at k=2 but doesn't rank the rest of the range cleanly. k=2 is the strongest candidate on the full set of evidence taken together: the best silhouette score among those tried, perfect stability under resampling (ARI = 1.0 across five reshuffled seeds, the best of any k tested), no sensitivity to KMeans's random initialization at any k tested, a segmentation that survives swapping out two of the three redundant engagement features for a single representative one, and a two-segment story simple enough for a retention team to actually act on. None of that proves two segments is how many "truly" exist in Aurora Stream's subscriber base — it means k=2 is a simple, stable, interpretable *working* segmentation, worth treating as an operating hypothesis to test rather than a discovered fact about the population.

## 5. Interpreting the segments

The two segments separate almost entirely on viewing engagement — session count, total minutes watched, and average session length are all higher in Segment 1 — while tenure, plan tier, and country don't meaningfully differ between the groups. In plain terms: this isn't "long-time subscribers vs. new ones" or "premium vs. basic plan" — it's genuinely about how much people are watching, independent of how long they've been a customer or what they pay.

## 6. Limitations

- (Resolved) Earlier drafts of this analysis reported segment profiles in standardized (z-score) units — correct for fitting KMeans, but not directly meaningful to a non-technical stakeholder. This has been fixed: the segment tables now cluster on standardized features internally but report each segment's actual session counts, minutes watched, and tenure in their original units.
- Segment 1 (81 subscribers, 27% of the base) is meaningfully smaller than Segment 0 — any retention offer aimed at it will be tested on a smaller population, so early read-outs on its effectiveness should be treated cautiously until more data accumulates.
- This analysis checked stability under resampling and under KMeans's random initialization, but not stability over time — the data is a single 90-day snapshot, so there's no way to tell from it alone whether the same two segments would reappear next quarter.
- The k=2 split is robust to dropping two of the three highly-correlated engagement features (session count and the exactly-derived average-minutes-per-session) — but that robustness doesn't hold at finer k values, where feature choice visibly changes which subscribers land in which cluster. Treat k=2 as a genuinely stable coarse split, not as proof that any finer segmentation of this population would be equally trustworthy.

## 7. Recommendation

Propose two retention tracks as a hypothesis to test, not a settled plan: a "re-engagement" track for Segment 0 (the 73% majority, currently under-engaged) focused on nudging usage back up, and a "reward high engagement" track for Segment 1 (the 27% minority) focused on retention through recognition rather than re-engagement, since they're already using the product heavily. The clustering shows these two groups engage differently — it says nothing about whether either track would actually reduce churn or which subscribers are worth the investment. Before committing budget to both, have the retention team sanity-check the segment profiles against subscribers they already know, and run the two tracks as a controlled test against a holdout group rather than rolling them out everywhere at once.

---

## Why this is a strong answer

This note earns "Exemplary" on **Modeling/evaluation correctness** (Section 4) because the k choice is justified by a full set of evidence — silhouette, resampling stability, initialization stability, feature-set robustness — rather than any single metric, and because it explicitly stops short of calling k=2 the "true" number of segments. It earns "Exemplary" on **Interpretation and limitations** by naming genuine, concrete constraints (Section 6) — Segment 1's smaller size, what hasn't been checked (stability over time), and where the k=2 result's robustness does and doesn't extend (feature-set sensitivity at finer k) — rather than generic disclaimers, and by being specific about which features actually separate the segments (Section 5) rather than describing the clusters only by their size.
