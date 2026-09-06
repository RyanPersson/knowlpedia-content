+++
id = "topology/sequentially-compact-set"
title = "Sequentially compact set"
kind = "knowl"
summary = "A set where every sequence has a convergent subsequence with limit in the set."
aliases = ["sequentially-compact-set", "Sequentially compact set"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "real-analysis/subsequence", "topology/convergent-sequence"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "topology/sequentially-compact-set.md"
+++

A subset \(K\) of a [[topology/topological-space|topological space]] \(X\) is **sequentially compact** if every sequence \((x_n)\) in \(K\) has a [[real-analysis/subsequence|subsequence]] \((x_{n_k})\) that [[topology/convergent-sequence|converges]] in \(X\) to a point of \(K\).

## Relation to compactness

In [[topology/metric-space|metric spaces]], sequential compactness is equivalent to [[topology/compact-set|compactness]]. In general topological spaces, neither property implies the other without additional hypotheses.
