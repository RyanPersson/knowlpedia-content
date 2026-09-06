+++
id = "topology/closed-sets-are-complements-of-open-sets"
title = "Closed sets are complements of open sets"
kind = "knowl"
summary = "A set is closed iff its complement is open; closed sets are stable under intersections"
aliases = ["closed-sets-are-complements-of-open-sets", "Closed sets are complements of open sets"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "topology/closed-set", "topology/open-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "topology/closed-sets-are-complements-of-open-sets.md"
+++

In a [[topology/topological-space|topological space]] \(X\), a subset \(F\subseteq X\) is [[topology/closed-set|closed]] if and only if its complement \(X\setminus F\) is [[topology/open-set|open]].

Consequently:
- arbitrary intersections of closed sets are closed, and
- finite unions of closed sets are closed.

This duality between open and closed sets is a basic tool in topology and analysis, especially for [[topology/closure|closure]], [[topology/limit-point|limit points]], and compactness arguments.
