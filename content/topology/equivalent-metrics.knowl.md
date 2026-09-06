+++
id = "topology/equivalent-metrics"
title = "Equivalent metrics"
kind = "knowl"
summary = "Two metrics on the same set that generate the same open sets, hence the same topology."
aliases = ["equivalent-metrics", "Equivalent metrics"]
domains = ["topology"]
prerequisites = ["topology/metric-induced-topology"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "topology/equivalent-metrics.md"
+++

Two metrics \(d\) and \(d'\) on a set \(X\) are **equivalent** if they induce the same [[topology/metric-induced-topology|topology]] on \(X\).

## Equivalent characterizations

Equivalently, \(\operatorname{id}_X:(X,d)\to(X,d')\) is a [[topology/homeomorphism|homeomorphism]].

## Remarks

Equivalent metrics have the same open sets and therefore the same convergent sequences, but they may differ in which sequences are [[topology/cauchy-sequence|Cauchy]] and whether the space is [[topology/complete-metric-space|complete]].

## Examples

- For any metric \(d\), the bounded metric \(d'(x,y)=\min\{1,d(x,y)\}\) is equivalent to \(d\).
- On \(\mathbb R^n\), the Euclidean and taxicab metrics are equivalent.
