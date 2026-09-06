+++
id = "convex-analysis/auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core"
title = "Auxiliary Separation Lemma"
kind = "knowl"
summary = "Disjoint convex sets are separable if one has nonempty core and the sets are disjoint."
aliases = ["auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core", "Auxiliary Separation Lemma"]
domains = ["convex-analysis"]
prerequisites = ["linear-algebra/vector-space", "convex-analysis/convex-set", "convex-analysis/algebraic-interior-core", "convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core", "convex-analysis/separation-by-a-hyperplane"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core.md"
+++

Let \(X\) be a real [[linear-algebra/vector-space|vector space]], and let \(\Omega_1,\Omega_2\subseteq X\) be nonempty [[convex-analysis/convex-set|convex sets]]. If
\[
\operatorname{core}(\Omega_1)\neq\varnothing
\qquad\text{and}\qquad
\Omega_1\cap\Omega_2=\varnothing,
\]
then \(\Omega_1\) and \(\Omega_2\) can be [[convex-analysis/separation-by-a-hyperplane|separated by a hyperplane]].

## Remarks

The proof reduces separation of two sets to separation of a point from a convex set by applying [[convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core|point-versus-set separation]] to the Minkowski difference \(\Omega_1-\Omega_2\).
