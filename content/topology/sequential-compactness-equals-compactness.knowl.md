+++
id = "topology/sequential-compactness-equals-compactness"
title = "Sequential compactness equals compactness"
kind = "knowl"
summary = "In metric spaces, compactness is equivalent to sequential compactness"
aliases = ["sequential-compactness-equals-compactness", "Sequential compactness equals compactness"]
domains = ["topology"]
legacy_source_path = "topology/sequential-compactness-equals-compactness.md"
prerequisites = ["topology/metric-space", "topology/compact-set", "topology/sequentially-compact-set"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

**Sequential compactness equals compactness:** Let \((X,d)\) be a [[topology/metric-space|metric space]] and let \(K\subseteq X\). Then \(K\) is [[topology/compact-set|compact]] if and only if \(K\) is [[topology/sequentially-compact-set|sequentially compact]], meaning every sequence in \(K\) has a [[real-analysis/subsequence|subsequence]] that is [[topology/convergent-sequence|convergent]] to a point of \(K\).

## Scope

This equivalence fails in general [[topology/topological-space|topological spaces]] but is fundamental in metric topology and connects compactness to arguments using sequences.
