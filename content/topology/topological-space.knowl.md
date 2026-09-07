+++
id = "topology/topological-space"
title = "Topological space"
kind = "knowl"
summary = "A set equipped with a topology, specifying which subsets are open."
aliases = ["topological-space", "Topological space"]
domains = ["topology"]
legacy_source_path = "topology/topological-space.md"
prerequisites = ["shared-foundations/set", "shared-foundations/subset", "shared-foundations/union", "shared-foundations/intersection"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 3
+++

A **topological space** is a pair \((X,\mathcal T)\), where \(X\) is a [[shared-foundations/set|set]] and \(\mathcal T\) is a collection of [[shared-foundations/subset|subsets]] of \(X\), satisfying:

1. **Empty set and whole space:** \(\varnothing,X\in\mathcal T\).
2. **Arbitrary unions:** the union of any collection of members of \(\mathcal T\) belongs to \(\mathcal T\).
3. **Finite intersections:** the intersection of finitely many members of \(\mathcal T\) belongs to \(\mathcal T\).

The collection \(\mathcal T\) is the [[topology/topology|topology]] of the space.

## Constructions

Here \(\mathcal{P}(X)\) denotes the [[shared-foundations/power-set|power set]] of \(X\), and the members of \(\mathcal{T}\) are the [[topology/open-set|open sets]] (whose complements are the [[topology/closed-set|closed sets]]). Many standard constructions—such as the [[topology/subspace-topology|subspace topology]], [[topology/product-topology|product topology]], and [[topology/quotient-topology|quotient topology]]—produce new topological spaces from existing ones.

## Examples

- \(\mathbb{R}\) with its usual topology (open sets are unions of open intervals).
- Any set \(X\) with the discrete topology \(\mathcal{T}=\mathcal{P}(X)\).
- Any [[topology/metric-space|metric space]] \((X,d)\), using the [[topology/metric-induced-topology|topology induced by the metric]].
