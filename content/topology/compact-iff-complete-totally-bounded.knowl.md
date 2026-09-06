+++
id = "topology/compact-iff-complete-totally-bounded"
title = "Compact iff complete and totally bounded"
kind = "knowl"
summary = "A metric space is compact exactly when it is complete and totally bounded."
aliases = ["compact-iff-complete-totally-bounded", "Compact iff complete and totally bounded"]
domains = ["topology"]
legacy_source_path = "topology/compact-iff-complete-totally-bounded.md"
prerequisites = ["topology/metric-space", "topology/compact-set", "topology/complete-metric-space", "topology/totally-bounded-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Compact iff complete and totally bounded:** Let \((X,d)\) be a [[topology/metric-space|metric space]]. Then the following are equivalent:

1. \(X\) is a [[topology/compact-set|compact set]].
2. \(X\) is a [[topology/complete-metric-space|complete metric space]] and [[topology/totally-bounded-set|totally bounded]].

## Equivalent characterizations

Equivalently, a subset \(K\subseteq X\) is compact in the [[topology/subspace-topology|subspace topology]] if and only if \((K,d|_{K\times K})\) is complete and totally bounded.

## Remarks

This characterization packages [[topology/compactness-implies-completeness|compactness implies completeness]] and [[topology/compactness-implies-total-boundedness|compactness implies total boundedness]] into a single criterion that is often easier to verify than the [[topology/open-cover|open cover]] definition.
