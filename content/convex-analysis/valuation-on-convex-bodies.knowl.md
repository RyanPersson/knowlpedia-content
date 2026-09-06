+++
id = "convex-analysis/valuation-on-convex-bodies"
title = "Valuation on convex bodies"
kind = "definition"
summary = "A finitely additive functional on convex bodies, with continuity and symmetry as additional properties."
aliases = ["convex-body valuation", "continuous translation-invariant valuation", "valuation on convex sets"]
domains = ["convex-analysis", "integral-geometry"]
section_mode = "progressive"
prerequisites = ["convex-analysis/convex-body", "linear-algebra/vector-space", "algebra-groups/abelian-group", "topology/hausdorff-distance"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal K(V)\) be the family of
[[convex-analysis/convex-body|convex bodies]] in a finite-dimensional real
[[linear-algebra/vector-space|vector space]]. A function
\(\phi:\mathcal K(V)\to A\), with values in an
[[algebra-groups/abelian-group|abelian group]] \(A\), is a **valuation** if
\[
\phi(K\cup L)+\phi(K\cap L)=\phi(K)+\phi(L)
\]
whenever \(K,L,K\cup L\in\mathcal K(V)\).

## Regularity and invariance

A real- or complex-valued valuation is **continuous** if it is continuous for
the [[topology/hausdorff-distance|Hausdorff metric]]. It is
**translation-invariant** if \(\phi(K+x)=\phi(K)\) for every \(x\in V\), and
**\(G\)-invariant** for a linear group \(G\) if \(\phi(gK)=\phi(K)\) for every
\(g\in G\). These are additional predicates, not part of finite additivity.

## Examples

Euclidean volume and the constant Euler-characteristic valuation
\(\chi(K)=1\) are continuous and translation-invariant. Fixing all but one
argument of a [[convex-analysis/mixed-volume|mixed volume]] gives another
standard family. Pluripotential theory supplies further examples by applying
Hessian measures to [[convex-analysis/support-function|support functions]].

## Group-invariant theory

If a compact subgroup \(G\subseteq O(V)\) acts transitively on the
[[linear-algebra/unit-sphere|unit sphere]],
the space of continuous translation- and \(G\)-invariant valuations is finite
dimensional. Quaternionic groups and the exceptional group
\(\operatorname{Spin}(9)\) enter valuation theory through this principle.

## References

1. Peter McMullen and Rolf Schneider, “Valuations on convex bodies,” in *Convexity and Its Applications*, Birkhäuser, 1983, 170–247. [DOI record](https://doi.org/10.1007/978-3-0348-5858-8_9).
2. Semyon Alesker, “Valuations on convex sets, non-commutative determinants, and pluripotential theory,” *Advances in Mathematics* 195 (2005), 561–595. [arXiv record](https://arxiv.org/abs/math/0401219).
