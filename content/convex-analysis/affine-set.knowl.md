+++
id = "convex-analysis/affine-set"
title = "Affine set"
kind = "knowl"
summary = "A set containing the entire line through any two of its points."
aliases = ["affine-set", "Affine Set"]
domains = ["convex-analysis"]
prerequisites = ["linear-algebra/vector-space", "convex-analysis/line-connecting-two-points"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/affine-set.md"
+++

Let \(X\) be a [[linear-algebra/vector-space|vector space]]. A subset \(\Omega\subseteq X\) is **affine** if for all \(a,b\in\Omega\),
\[
L[a,b]\subseteq \Omega,
\]

where \(L[a,b]\) is the [[convex-analysis/line-connecting-two-points|line connecting \(a\) and \(b\)]].

## Examples

- Any linear subspace is affine.
- In \(\mathbb{R}^n\), a set of the form \(x_0+L\) with \(L\) a subspace is affine.
- A [[convex-analysis/convex-set|convex set]] need not be affine; affine sets are "flat," while convex sets may be curved.

## Equivalent characterizations

A nonempty subset \(\Omega\) is affine if and only if it is a translate of a [[convex-analysis/linear-subspace|linear subspace]] (see [[convex-analysis/affine-sets-are-translates-of-subspaces|the translate characterization]]). Under the line-based definition above, the empty set is also affine.
