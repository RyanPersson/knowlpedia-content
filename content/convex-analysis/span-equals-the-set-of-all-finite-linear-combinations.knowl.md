+++
id = "convex-analysis/span-equals-the-set-of-all-finite-linear-combinations"
title = "Span equals finite linear combinations"
kind = "knowl"
summary = "The span of a set consists exactly of its finite linear combinations"
aliases = ["span-equals-the-set-of-all-finite-linear-combinations", "Span equals finite linear combinations"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/subspace-generated-by-a-set-span", "convex-analysis/linear-combination"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/span-equals-the-set-of-all-finite-linear-combinations.md"
+++

**Theorem.**
Let \(X\) be a vector space over \(K\), and let \(A\subseteq X\). Then the [[convex-analysis/subspace-generated-by-a-set-span|span]] of \(A\) is
\[
\left\{\sum_{i=1}^m \alpha_i x_i \ \middle|\ m\ge 0,\ \alpha_i\in K,\ x_i\in A\right\},
\]

the set of all finite [[convex-analysis/linear-combination|linear combinations]] of elements of \(A\). The case \(m=0\) denotes the empty sum \(0\), so the formula also covers \(A=\varnothing\).

**Proof sketch.** Let \(Y\) be the set of all such finite linear combinations. One checks that \(Y\) is a linear subspace and contains \(A\), hence \(\operatorname{span}(A)\subset Y\) by minimality. Conversely, \(\operatorname{span}(A)\) is a subspace containing \(A\), so it is closed under forming finite linear combinations of elements of \(A\), giving \(Y\subset \operatorname{span}(A)\).
