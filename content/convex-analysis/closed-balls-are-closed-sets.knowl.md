+++
id = "convex-analysis/closed-balls-are-closed-sets"
title = "Closed balls are closed"
kind = "knowl"
summary = "Every closed ball in a metric space is a closed subset."
aliases = ["closed-balls-are-closed-sets", "Closed balls are closed"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/closed-balls-are-closed-sets.md"
prerequisites = ["convex-analysis/metric-metric-space", "convex-analysis/closed-subset", "topology/metric-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

In a metric space \((X,d)\), every closed ball
\[
\overline B(x_0,r)=\{x\in X:d(x,x_0)\le r\},
\qquad r\ge0,
\]
is a [[convex-analysis/closed-subset|closed set]].

## Remarks

If \(x\notin\overline B(x_0,r)\), let \(\delta=d(x,x_0)-r>0\). If \(d(y,x)<\delta\), then
\[
d(y,x_0)\ge d(x,x_0)-d(y,x)>r.
\]
Thus \(B(x,\delta)\) lies in the complement, so the complement is open.
