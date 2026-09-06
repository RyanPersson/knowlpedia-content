+++
id = "topology/metric-induced-topology"
title = "Metric-induced topology"
kind = "knowl"
summary = "The topology on a metric space in which a set is open if it contains an open ball around each of its points."
aliases = ["metric-induced-topology", "Metric-induced topology"]
domains = ["topology"]
prerequisites = ["topology/metric", "topology/open-ball"]
dependency_review_count = 1
legacy_source_path = "topology/metric-induced-topology.md"
+++

The **metric-induced topology** on a metric space \((X,d)\) is the collection \(\tau_d\) of subsets \(U\subseteq X\) such that, for every \(x\in U\), there is \(r>0\) with \(B_d(x,r)\subseteq U\). Here \(B_d(x,r)\) is the [[topology/open-ball|open ball]] of radius \(r\) centered at \(x\).

The family of open balls is a [[topology/basis-of-topology|basis]] for \(\tau_d\), so the [[topology/open-set|open sets]] are precisely the unions of open balls.

## Examples

- On \(\mathbb R^n\) with the Euclidean metric, \(\tau_d\) is the usual Euclidean topology.
- On a set \(X\) with the discrete metric, \(\tau_d\) is the discrete topology.
