+++
id = "convex-analysis/algebraic-interior-core"
title = "Algebraic Interior (Core)"
kind = "knowl"
summary = "Points from which every vector-space direction remains in the set for a sufficiently short segment."
aliases = ["algebraic-interior-core", "Algebraic Interior (Core)"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/algebraic-interior-core.md"
prerequisites = ["linear-algebra/vector-space", "convex-analysis/norm-normed-vector-space", "convex-analysis/interior-of-a-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a real [[linear-algebra/vector-space|vector space]] and let \(\Omega\subseteq X\).

The **algebraic interior** (or **core**) of \(\Omega\) is
\[
\operatorname{core}(\Omega):=\Big\{x\in\Omega \ \Big|\ \forall v\in X,\ \exists \delta>0\ \text{s.t.}\ x+tv\in\Omega\ \text{for all }|t|<\delta\Big\}.
\]

## Remarks

When \(X\) is a [[convex-analysis/norm-normed-vector-space|normed vector space]],
\[
\operatorname{int}(\Omega)\subseteq \operatorname{core}(\Omega)\subseteq \Omega,
\]

where \(\operatorname{int}(\Omega)\) is the usual [[convex-analysis/interior-of-a-set|interior]]. Convexity is not needed for these inclusions.

## Examples

- If \(\Omega\) is an open ball in a normed space, then \(\operatorname{core}(\Omega)=\Omega\).
- If \(L\) is a proper linear subspace of \(X\), then \(\operatorname{core}(L)=\varnothing\): a direction outside \(L\) immediately leaves \(L\).
