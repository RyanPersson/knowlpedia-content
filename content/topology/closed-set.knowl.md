+++
id = "topology/closed-set"
title = "Closed set"
kind = "knowl"
summary = "A subset whose complement is open in the ambient space."
aliases = ["closed-set", "Closed set"]
domains = ["topology"]
legacy_source_path = "topology/closed-set.md"
prerequisites = ["topology/topological-space", "shared-foundations/subset", "topology/open-set", "shared-foundations/complement"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

A **closed set** in a [[topology/topological-space|topological space]] \((X,\mathcal T)\) is a [[shared-foundations/subset|subset]] \(F\subseteq X\) whose complement \(X\setminus F\) is a [[topology/open-set|open set]].

The [[topology/closure|closure]] of \(A\subseteq X\) is the smallest closed set containing \(A\). A map is [[topology/continuous-map|continuous]] if and only if the preimage of every closed set is closed.

## Examples

- In \(\mathbb R\) with its usual topology, \([0,1]\) is closed.
- In the discrete topology on \(X\), every subset of \(X\) is closed.
- In the indiscrete topology on \(X\), the only closed sets are \(\varnothing\) and \(X\).
