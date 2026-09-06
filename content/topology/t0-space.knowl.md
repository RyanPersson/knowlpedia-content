+++
id = "topology/t0-space"
title = "T₀ space"
kind = "knowl"
summary = "A topological space in which some open set distinguishes each pair of distinct points."
aliases = ["t0-space", "T0 space"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "topology/open-set"]
dependency_review_count = 1
legacy_source_path = "topology/t0-space.md"
+++

A **\(T_0\) space** is a [[topology/topological-space|topological space]] \(X\) such that for any distinct points \(x,y\in X\), there is an [[topology/open-set|open set]] containing exactly one of them.

This is the weakest of the common separation axioms. Every [[topology/t1-space|\(T_1\) space]], and hence every [[topology/hausdorff-space|Hausdorff space]], is \(T_0\).

## Examples

- The Sierpiński space on \(\{0,1\}\), with open sets \(\varnothing\), \(\{1\}\), and \(\{0,1\}\), is \(T_0\) but not \(T_1\).
- Every [[topology/metric-space|metric space]] is \(T_0\), since it is Hausdorff.
