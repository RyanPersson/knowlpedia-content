+++
id = "topology/basis-of-topology"
title = "Basis of a topology"
kind = "knowl"
summary = "A collection of sets whose unions give all open sets."
aliases = ["basis-of-topology", "Basis of a topology"]
domains = ["topology"]
legacy_source_path = "topology/basis-of-topology.md"
prerequisites = ["topology/topology", "shared-foundations/subset"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

A **basis** of a [[topology/topology|topology]] \(\mathcal T\) on \(X\) is a collection \(\mathcal B\subseteq\mathcal T\) such that every member of \(\mathcal T\) is a union of members of \(\mathcal B\).

## Generating a topology

A collection \(\mathcal B\) of subsets of a set \(X\) is a basis for some topology if and only if:

1. Every \(x\in X\) belongs to a member of \(\mathcal B\).
2. Whenever \(x\in B_1\cap B_2\) for \(B_1,B_2\in\mathcal B\), there is \(B_3\in\mathcal B\) with \(x\in B_3\subseteq B_1\cap B_2\).

The generated topology consists of all unions of members of \(\mathcal B\), including the empty union. Its open sets are exactly the sets \(U\) such that each \(x\in U\) lies in some \(B\in\mathcal B\) with \(B\subseteq U\).

## Examples

- In \(\mathbb{R}\) with the usual topology, the open intervals \((a,b)\) form a basis.
- In a [[topology/metric-space|metric space]], the family of [[topology/open-ball|open balls]] forms a basis for the [[topology/metric-induced-topology|metric-induced topology]].
- In a product \(X\times Y\) with the [[topology/product-topology|product topology]], the sets \(U\times V\) with \(U\) open in \(X\) and \(V\) open in \(Y\) form a basis.
