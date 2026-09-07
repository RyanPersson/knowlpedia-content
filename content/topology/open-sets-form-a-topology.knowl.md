+++
id = "topology/open-sets-form-a-topology"
title = "Open sets form a topology"
kind = "knowl"
summary = "The open subsets of a metric space satisfy the axioms of a topology."
aliases = ["open-sets-form-a-topology", "Open sets form a topology"]
domains = ["topology"]
legacy_source_path = "topology/open-sets-form-a-topology.md"
prerequisites = ["topology/metric-space", "topology/open-ball", "topology/topology"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 3
+++

Let \((X,d)\) be a [[topology/metric-space|metric space]], and define
\[
\tau_d=\{U\subseteq X:\text{for every }x\in U\text{ there is }r>0\text{ with }B_d(x,r)\subseteq U\},
\]
where \(B_d(x,r)\) is an [[topology/open-ball|open ball]]. Then:

1. \(\varnothing,X\in\tau_d\).
2. Any union of members of \(\tau_d\) belongs to \(\tau_d\).
3. Any finite intersection of members of \(\tau_d\) belongs to \(\tau_d\).

Thus \(\tau_d\) is a [[topology/topology|topology]] on \(X\).

## Proof

The empty set and \(X\) lie in \(\tau_d\). An arbitrary union of members lies in \(\tau_d\), since each point belongs to one of them and has a ball inside it. For a finite intersection, take the minimum of the finitely many positive radii supplied at a point. The empty intersection is \(X\).

## Resulting structure

This is the [[topology/metric-induced-topology|metric-induced topology]]. The proof starts with the metric ball condition, rather than assuming an existing topology and its open sets.
