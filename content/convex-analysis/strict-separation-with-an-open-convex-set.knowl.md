+++
id = "convex-analysis/strict-separation-with-an-open-convex-set"
title = "Strict Separation When One Set is Open"
kind = "knowl"
summary = "Disjoint convex sets can be separated strictly on the side of an open set."
aliases = ["strict-separation-with-an-open-convex-set", "Strict Separation When One Set is Open"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/norm-normed-vector-space", "convex-analysis/convex-set", "convex-analysis/open-subset", "convex-analysis/dual-space-and-duality-pairing"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/strict-separation-with-an-open-convex-set.md"
+++

Let \(X\) be a real [[convex-analysis/norm-normed-vector-space|normed space]]. Let \(G,\Omega\subset X\) be nonempty, disjoint [[convex-analysis/convex-set|convex sets]], and assume that \(G\) is [[convex-analysis/open-subset|open]].

**Corollary.** There exist a nonzero \(x^\ast \in X^\ast\) (see [[convex-analysis/dual-space-and-duality-pairing|dual space]]) and \(\beta\in\mathbb{R}\) such that
\[
\langle x^\ast,x\rangle < \beta \le \langle x^\ast,y\rangle
\quad\text{for all }x\in G,\ y\in\Omega.
\]

## Remarks

This follows from [[convex-analysis/separation-by-closed-hyperplane-under-interior-condition|closed hyperplane separation under an interior condition]] together with the openness of \(G\), which makes the inequality strict on the \(G\)-side.
