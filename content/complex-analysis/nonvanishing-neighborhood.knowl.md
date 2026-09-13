+++
id = "complex-analysis/nonvanishing-neighborhood"
title = "Nonvanishing on a neighborhood of a compact set"
kind = "proposition"
summary = "A positive lower bound on a compact set persists on a sufficiently small neighborhood."
aliases = ["zero-free neighborhood", "uniform exclusion of zeros"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["topology/compact-set", "topology/continuous-map", "real-analysis/modulus-on-c"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(f\) be continuous near a [[topology/compact-set|compact set]] \(K\) and suppose \(|f(x)|\ge c>0\) on \(K\). Then there is an open neighborhood \(V\) of \(K\) on which \(|f|>c/2\). Continuity supplies a suitable neighborhood at each point; finitely many cover \(K\).

## Holomorphic denominators and parameters

For holomorphic \(f\), this gives a region where \(1/f\) is holomorphic and bounded. A jointly continuous compact parameter family with the same margin admits a common neighborhood by applying the argument on the compact product. For a noncompact family, uniformity needs a separate estimate. Being nonzero at each real point for each parameter does not by itself furnish a common complex neighborhood or a bounded inverse.
