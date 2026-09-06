+++
id = "linear-algebra/banach-space"
title = "Banach space"
kind = "knowl"
summary = "A complete normed vector space."
aliases = ["banach-space", "Banach space"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/banach-space.md"
prerequisites = ["linear-algebra/normed-vector-space", "topology/complete-metric-space", "topology/cauchy-sequence"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **Banach space** is a [[linear-algebra/normed-vector-space|normed vector space]] \((X,\|\cdot\|)\) such that every [[topology/cauchy-sequence|Cauchy sequence]] in \(X\) converges (in the norm) to a point of \(X\).

## Equivalent characterizations

Equivalently, the metric \(d(x,y)=\|x-y\|\) makes \(X\) a [[topology/complete-metric-space|complete metric space]]. Completeness is a property of the metric induced by the [[linear-algebra/norm|norm]], and it is essential for many limit processes in analysis.

## Examples

By contrast, the polynomials on \([0,1]\) with the sup norm are not a Banach
space: uniform limits of polynomials can be arbitrary continuous functions,
so the polynomial subspace is dense but incomplete.

- \(\mathbb{R}^n\) with the [[linear-algebra/euclidean-norm|Euclidean norm]] (indeed, \(\mathbb{R}^n\) is Banach for any norm).
- The space \(C([0,1])\) of continuous real-valued functions on \([0,1]\) with the sup norm \(\|f\|_\infty=\sup_{x\in[0,1]}|f(x)|\).
