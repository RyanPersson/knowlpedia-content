+++
id = "convex-analysis/properties-of-the-minkowski-functional-of-a-convex-set"
title = "Properties of the Minkowski Gauge of a Convex Set"
kind = "knowl"
summary = "For absorbing convex Ω, pΩ is sublinear and its level sets describe core(Ω) and lin(Ω)."
aliases = ["properties-of-the-minkowski-functional-of-a-convex-set", "Properties of the Minkowski Gauge of a Convex Set"]
domains = ["convex-analysis"]
prerequisites = ["linear-algebra/vector-space", "convex-analysis/balanced-and-absorbing-sets", "convex-analysis/convex-set", "convex-analysis/minkowski-function-gauge-of-a-set", "convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions", "convex-analysis/algebraic-interior-core", "convex-analysis/linear-closure"]
dependency_review_count = 1
legacy_source_path = "convex-analysis/properties-of-the-minkowski-functional-of-a-convex-set.md"
+++

Let \(X\) be a real [[linear-algebra/vector-space|vector space]] and let \(\Omega\subseteq X\) be [[convex-analysis/balanced-and-absorbing-sets|absorbing]] and [[convex-analysis/convex-set|convex]]. Then the [[convex-analysis/minkowski-function-gauge-of-a-set|Minkowski gauge]] \(p_\Omega\) is finite-valued and [[convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions|sublinear]]. Moreover,

1. the strict sublevel set is the [[convex-analysis/algebraic-interior-core|algebraic interior]]:
   \[
   \{x\in X:p_\Omega(x)<1\}=\operatorname{core}(\Omega);
   \]
2. the non-strict sublevel set is the [[convex-analysis/linear-closure|linear closure]]:
   \[
   \{x\in X:p_\Omega(x)\le 1\}=\operatorname{lin}(\Omega).
   \]

## Application

These level-set formulas connect the geometry of \(\Omega\) with a canonical sublinear functional and lead to [[convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core|separation via the core]].
