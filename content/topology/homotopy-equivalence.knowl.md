+++
id = "topology/homotopy-equivalence"
title = "Homotopy equivalence"
kind = "knowl"
summary = "A pair of maps inverse to one another up to continuous deformation."
aliases = ["homotopy equivalent", "homotopy equivalence"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "topology/continuous-map", "topology/homotopy"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

Two [[topology/topological-space|topological spaces]] \(X\) and \(Y\) are **homotopy equivalent** if there are [[topology/continuous-map|continuous maps]] \(f:X\to Y\) and \(g:Y\to X\) such that \(g\circ f\) is [[topology/homotopy|homotopic]] to \(\operatorname{id}_X\) and \(f\circ g\) is homotopic to \(\operatorname{id}_Y\).

## Consequences

Homotopy equivalence preserves homotopy invariants, such as homotopy groups and singular homology, but it is weaker than [[topology/homeomorphism|homeomorphism]]. It records the large-scale deformation type rather than the exact local topology.
