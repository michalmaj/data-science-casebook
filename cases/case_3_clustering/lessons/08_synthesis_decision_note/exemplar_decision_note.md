# Exemplar Decision Note — Case 3 (Aurora Stream)

*This is a model answer, written after completing all of Case 3. Don't read it before writing your own — the point of the exercise is to reach these conclusions yourself; this exists so you can compare your reasoning to a strong answer afterward, not so you can copy it.*

## 1. Business question

Does Aurora Stream's subscriber base actually split into distinct behavioral groups — beyond the plan tiers we already track — that would justify different retention offers, or is "one offer for everyone" already the right call?

## 2. Approach

I extracted four engagement/tenure features per subscriber (`session_count`, `total_minutes_watched`, `avg_minutes_per_session`, `tenure_days`) via SQL, standardized them with `StandardScaler`, and fit KMeans at several values of k. I compared inertia and silhouette score across k, checked cluster-assignment stability under resampling, and settled on k=2.

## 3. Results (final segment table, k=2)

| Segment | Size | Share | Notes |
|---|---:|---:|---|
| 0 | 219 | 73% | Below-average engagement across all three viewing features |
| 1 | 81 | 27% | Above-average engagement across all three viewing features |

## 4. Choosing k and checking stability

Inertia and silhouette score didn't agree on a single "best" k, so the deciding factor was stability: re-running KMeans across five different resampled seeds gave k=2 a perfectly consistent segment assignment (ARI = 1.0 every time), which is a stronger practical argument than either metric alone — a segmentation that reshuffles under a different random seed isn't one Aurora Stream's retention team can build a durable offer around.

## 5. Interpreting the segments

The two segments separate almost entirely on viewing engagement — session count, total minutes watched, and average session length are all higher in Segment 1 — while tenure, plan tier, and country don't meaningfully differ between the groups. In plain terms: this isn't "long-time subscribers vs. new ones" or "premium vs. basic plan" — it's genuinely about how much people are watching, independent of how long they've been a customer or what they pay.

## 6. Limitations

- (Resolved) Earlier drafts of this analysis reported segment profiles in standardized (z-score) units — correct for fitting KMeans, but not directly meaningful to a non-technical stakeholder. This has been fixed: the segment tables now cluster on standardized features internally but report each segment's actual session counts, minutes watched, and tenure in their original units.
- Segment 1 (81 subscribers, 27% of the base) is meaningfully smaller than Segment 0 — any retention offer aimed at it will be tested on a smaller population, so early read-outs on its effectiveness should be treated cautiously until more data accumulates.

## 7. Recommendation

Propose two retention tracks as a hypothesis to test, not a settled plan: a "re-engagement" track for Segment 0 (the 73% majority, currently under-engaged) focused on nudging usage back up, and a "reward high engagement" track for Segment 1 (the 27% minority) focused on retention through recognition rather than re-engagement, since they're already using the product heavily. The clustering shows these two groups engage differently — it says nothing about whether either track would actually reduce churn or which subscribers are worth the investment. Before committing budget to both, have the retention team sanity-check the segment profiles against subscribers they already know, and run the two tracks as a controlled test against a holdout group rather than rolling them out everywhere at once.

---

## Why this is a strong answer

This note earns "Exemplary" on **Modeling/evaluation correctness** (Section 4) because the k choice is justified by stability under resampling, not just by whichever k happened to produce the best single metric — and the ARI=1.0 number is stated precisely rather than asserted vaguely. It earns "Exemplary" on **Interpretation and limitations** by naming a genuine, concrete constraint — Segment 1's smaller size (Section 6) and what that means for testing caution — rather than a generic disclaimer, and by being specific about which features actually separate the segments (Section 5) rather than describing the clusters only by their size.
