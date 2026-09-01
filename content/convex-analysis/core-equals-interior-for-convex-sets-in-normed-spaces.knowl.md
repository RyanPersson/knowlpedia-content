+++
id = "convex-analysis/core-equals-interior-for-convex-sets-in-normed-spaces"
title = "Core Equals Interior for Convex Sets in Normed Spaces"
kind = "knowl"
summary = "For convex sets with nonempty interior, algebraic and topological interiors coincide."
aliases = ["core-equals-interior-for-convex-sets-in-normed-spaces", "Core Equals Interior for Convex Sets in Normed Spaces"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/norm-normed-vector-space", "convex-analysis/convex-set", "convex-analysis/interior-of-a-set", "convex-analysis/algebraic-interior-core"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/core-equals-interior-for-convex-sets-in-normed-spaces.md"
+++

Let \(X\) be a [[convex-analysis/norm-normed-vector-space|normed vector space]] and let \(\Omega\subseteq X\) be [[convex-analysis/convex-set|convex]] with nonempty [[convex-analysis/interior-of-a-set|interior]]. Then its [[convex-analysis/algebraic-interior-core|algebraic interior]] equals its topological interior:
\[
\operatorname{core}(\Omega)=\operatorname{int}(\Omega).
\]

## Proof idea

The inclusion \(\operatorname{int}(\Omega)\subseteq\operatorname{core}(\Omega)\) is direct. For the reverse inclusion, translate so that \(0\in\operatorname{int}(\Omega)\) and use convexity together with [[convex-analysis/segments-from-interior-points-stay-in-the-interior|the interior-segment lemma]].
