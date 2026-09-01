+++
id = "topology/convergent-sequence"
title = "Convergent sequence"
kind = "knowl"
summary = "A sequence whose terms eventually remain in every neighborhood of a limit point."
aliases = ["convergent-sequence", "Convergent sequence"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "topology/neighborhood", "topology/metric-space", "topology/hausdorff-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "topology/convergent-sequence.md"
+++

A sequence \((x_n)\) in a [[topology/topological-space|topological space]] \(X\) **converges** to \(x\in X\) if, for every [[topology/neighborhood|neighborhood]] \(U\) of \(x\), there is \(N\in\mathbb N\) such that \(x_n\in U\) for all \(n\geq N\).

In a [[topology/metric-space|metric space]] \((X,d)\), this is equivalent to \(d(x_n,x)\to 0\). In a [[topology/hausdorff-space|Hausdorff space]], limits of convergent sequences are unique.

## Examples

- In \(\mathbb R\) with the usual metric, the sequence \(x_n=1/n\) converges to \(0\).
- In a space with the discrete metric, a sequence converges if and only if it is eventually constant.
