+++
id = "topology/complete-metric-space"
title = "Complete metric space"
kind = "knowl"
summary = "A metric space in which every Cauchy sequence converges to a point of the space."
aliases = ["complete-metric-space", "Complete metric space"]
domains = ["topology"]
legacy_source_path = "topology/complete-metric-space.md"
prerequisites = ["topology/metric-space", "topology/cauchy-sequence", "topology/convergent-sequence"]
dependency_heuristic = "semantic-foundations-review-v1"
dependency_review_count = 1
+++

A **complete metric space** is a metric space \((X,d)\) in which every [[topology/cauchy-sequence|Cauchy sequence]] converges (as a [[topology/convergent-sequence|convergent sequence]]) to a point of \(X\).

## Remarks

The sequence of rational decimal truncations of \(\sqrt 2\) is Cauchy in
\(\mathbb{Q}\), but it has no limit in \(\mathbb{Q}\). Completeness therefore
depends on the space as well as on its metric.

Completeness is central in analysis and topology; for example it interacts strongly with [[topology/compact-set|compactness]] (see [[topology/compact-iff-complete-totally-bounded|compact iff complete and totally bounded]]) and with the [[topology/baire-category-theorem|Baire category theorem]] (see [[topology/complete-metric-space-is-baire|complete metric spaces are Baire]]).

## Examples

- \((\mathbb{R}^n,\|\cdot\|_2)\) is complete.
- \((\mathbb{Q},|\cdot|)\) is not complete.
