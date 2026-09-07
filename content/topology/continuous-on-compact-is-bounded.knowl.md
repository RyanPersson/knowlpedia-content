+++
id = "topology/continuous-on-compact-is-bounded"
title = "Continuous functions on compact sets are bounded"
kind = "knowl"
summary = "A continuous real-valued function on a compact set has finite sup norm"
aliases = ["continuous-on-compact-is-bounded", "Continuous functions on compact sets are bounded"]
domains = ["topology"]
legacy_source_path = "topology/continuous-on-compact-is-bounded.md"
prerequisites = ["topology/compact-set", "topology/continuous-map", "real-analysis/absolute-value", "topology/extreme-value-theorem"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

A [[topology/continuous-map|continuous function]] \(f:K\to\mathbb R\) on a [[topology/compact-set|compact topological space]] \(K\) is **bounded**: there exists \(M\geq0\) such that
\[
|f(x)|\le M\qquad(x\in K).
\]

## Proof

If \(K\) is empty the assertion is vacuous. Otherwise the [[topology/extreme-value-theorem|extreme value theorem]] gives a minimum \(m\) and maximum \(M_+\); take \(M=\max\{|m|,|M_+|\}\).

## Scope

No metric on the domain is required. Applied to a compact subset of another space, continuity means continuity for the subspace topology.
