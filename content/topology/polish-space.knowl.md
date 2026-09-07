+++
id = "topology/polish-space"
title = "Polish space"
kind = "definition"
summary = "A separable topological space whose topology is induced by a complete metric."
aliases = ["polish-space", "Polish space"]
domains = ["topology"]
prerequisites = ["topology/complete-metric-space", "topology/separable-space", "topology/metric-induced-topology"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 1
+++

A **Polish space** is a [[topology/separable-space|separable]] topological space \(X\) for which there exists a metric \(d\) whose [[topology/metric-induced-topology|induced topology]] is the given topology and such that \((X,d)\) is a [[topology/complete-metric-space|complete metric space]]. Completeness is required for at least one compatible metric; it need not hold for every metric inducing the topology.

## Examples

- \(\mathbb R^n\), with its usual topology, is Polish for every integer \(n\ge0\): the Euclidean metric is complete and \(\mathbb Q^n\) is a countable dense subset.
- Every open interval \((a,b)\subset\mathbb R\), where \(a<b\) are real numbers, is Polish. Its usual metric is not complete, but a homeomorphism \(h:(a,b)\to\mathbb R\) supplies the compatible complete metric \(d_h(x,y)=|h(x)-h(y)|\).
- \(\mathbb Q\) with its usual topology is not Polish. It is separable, but has no isolated points and is a countable union of nowhere-dense singleton sets, hence is meagre in itself. A nonempty completely metrizable space is Baire, so no compatible metric on this topology can be complete.

## Remarks

Polishness is a property of the topology, not of a selected metric. It is a standard state-space hypothesis in probability and descriptive set theory.
