+++
id = "convex-analysis/parallel-affine-set"
title = "Parallel Affine Set"
kind = "knowl"
summary = "An affine set Ω is parallel to a subspace L if Ω=ω+L for some ω∈Ω."
aliases = ["parallel-affine-set", "Parallel Affine Set"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/parallel-affine-set.md"
prerequisites = ["linear-algebra/vector-space", "convex-analysis/affine-set", "convex-analysis/linear-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[linear-algebra/vector-space|vector space]]. An [[convex-analysis/affine-set|affine set]] \(\Omega\subset X\) is said to be **parallel** to a [[convex-analysis/linear-subspace|linear subspace]] \(L\subset X\) if
\[
\Omega=\omega+L
\]

for some \(\omega\in\Omega\).

## Examples

- In \(\mathbb{R}^n\), any affine subspace is parallel to its direction subspace (the translation of the affine set through the origin).

## Remarks

By [[convex-analysis/affine-sets-are-translates-of-subspaces|the translate characterization]], every nonempty affine set is parallel to at least one subspace. The parallel subspace is unique and can be written explicitly as \(\Omega-\Omega\); see [[convex-analysis/parallel-subspace-to-an-affine-set-is|the Ω−Ω proposition]].
